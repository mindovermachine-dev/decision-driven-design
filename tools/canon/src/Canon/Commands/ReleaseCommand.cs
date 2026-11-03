// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using Canon.GitHub;
using Canon.Infrastructure;
using Canon.Releases;

namespace Canon.Commands;

/// <summary>
/// canon release &lt;version&gt; [--plan]: descriptor, guard, signed tag,
/// GitHub Release (DESIGN.md §4.3). Each step refuses with exit 1 and leaves
/// nothing behind; --plan runs every check and makes no change.
///
///   1. the descriptor is well formed for a release
///   2. the version exists nowhere: no local tag, no tag on the remote
///      (ls-remote), no GitHub Release. The v0.5.0 lesson.
///   3. the commit under release (commit:, else the remote trunk's head) is
///      an ancestor of the remote trunk (rule 3)
///   4. the release-head guard (rule 7)
///   5. every gate passes at that commit, in a clean worktree
///   6. CHANGELOG.md there is the projection of releases/ (DDD-dec-104)
///   7. a signed, annotated tag "&lt;version&gt; — &lt;title&gt;" (rule 2); never unsigned
///   8. the tag pushed, then read back with ls-remote
///   9. the GitHub Release: name as the tag message, body the summary,
///      pre-release from the descriptor
/// </summary>
internal static class ReleaseCommand
{
    public static int Run(Context context, IReadOnlyList<string> arguments)
    {
        string? version = null;
        bool plan = false;
        foreach (string argument in arguments)
        {
            switch (argument)
            {
                case "--plan":
                    plan = true;
                    break;
                case { } value when !value.StartsWith('-') && version is null:
                    version = value;
                    break;
                default:
                    context.Err.WriteLine($"release: unknown argument '{argument}'");
                    return Exit.CouldNotRun;
            }
        }

        if (version is null)
        {
            context.Err.WriteLine("release: usage: canon release <version> [--plan]");
            return Exit.CouldNotRun;
        }

        Git git = context.Git;
        string remote = context.Config.Remote;
        string relative = context.Config.DescriptorPath(version);

        // Step 2 needs GitHub before anything else can be trusted: a release
        // that cannot ask GitHub whether the version exists does not proceed.
        using GitHubClient? github = GitHubFor(context, required: true);
        if (github is null)
        {
            return Exit.CouldNotRun;
        }

        // 1. The descriptor, as it is on the remote trunk: what landed.
        git.Run("fetch", "--quiet", "--no-tags", remote, $"refs/heads/{context.Config.Trunk}");
        string trunk = git.Run("rev-parse", "FETCH_HEAD");
        string? text = git.Show(trunk, relative);
        if (text is null)
        {
            return Refuse(context, 1, $"{relative} is not on {remote}/{context.Config.Trunk} ({trunk[..12]}); a release is cut only from a landed descriptor");
        }

        Descriptor descriptor = Descriptor.Parse(relative, text);
        IReadOnlyList<string> problems = descriptor.Problems(version);
        if (problems.Count > 0)
        {
            return Refuse(context, 1, $"{relative}: " + string.Join("; ", problems));
        }

        Pass(context, 1, $"{relative} at {trunk[..12]} is well formed");

        // 2. Nowhere already.
        IReadOnlyList<(TagSite Site, string Detail)> found = TagPresence.Find(git, remote, github, version);
        if (found.Count > 0)
        {
            return Refuse(context, 2, $"{version} already exists: " + string.Join("; ", found.Select(f => $"[{TagPresence.Name(f.Site)}] {f.Detail}"))
                + ". A cut version is never cut again (rule 1); a correction is a new version.");
        }

        Pass(context, 2, $"{version} exists nowhere: no local tag, no tag on {remote}, no GitHub Release");

        // 3. The commit under release.
        string underRelease = descriptor.Commit is { } pinned
            ? git.Resolve(pinned) ?? "" : trunk;
        if (underRelease.Length == 0)
        {
            return Refuse(context, 3, $"commit {descriptor.Commit} does not name a commit here");
        }

        if (!git.IsAncestor(underRelease, trunk))
        {
            return Refuse(context, 3, $"{underRelease[..12]} is not an ancestor of {remote}/{context.Config.Trunk} (rule 3)");
        }

        Pass(context, 3, $"the commit under release is {underRelease[..12]}");

        // 4. The guard.
        if (descriptor.Format == "2")
        {
            IReadOnlyList<string> misses = ReleaseHeadGuard.Check(git, descriptor.RatifiedHead!, underRelease, relative);
            if (misses.Count > 0)
            {
                return Refuse(context, 4, string.Join("; ", misses));
            }

            Pass(context, 4, $"ratified_head {descriptor.RatifiedHead} plus at most the descriptor");
        }
        else
        {
            Pass(context, 4, "format 1: no ratified_head, no guard (spec §4)");
        }

        // 5 and 6. Gates and the changelog, at that commit, in a clean worktree.
        string worktree = Path.Combine(Path.GetTempPath(), "canon-release-" + Guid.NewGuid().ToString("N")[..12]);
        git.Run("worktree", "add", "--quiet", "--detach", worktree, underRelease);
        try
        {
            ProcessResult gates = Processes.Run(context.Config.Gates[0], worktree, context.Config.Gates.Skip(1));
            if (gates.Exit != 0)
            {
                context.Err.Write(gates.Output);
                context.Err.Write(gates.Error);
                return Refuse(context, 5, $"the gates ({string.Join(' ', context.Config.Gates)}) failed at {underRelease[..12]}, exit {gates.Exit}");
            }

            Pass(context, 5, $"the gates ({string.Join(' ', context.Config.Gates)}) pass at {underRelease[..12]}");

            (string? projection, IReadOnlyList<string> changelogProblems) = Changelog.Project(worktree, context.Config);
            string changelog = Path.Combine(worktree, context.Config.ChangelogPath);
            if (projection is null)
            {
                return Refuse(context, 6, string.Join("; ", changelogProblems));
            }

            if (!File.Exists(changelog) || File.ReadAllText(changelog) != projection)
            {
                return Refuse(context, 6, $"{context.Config.ChangelogPath} at {underRelease[..12]} is not the projection of {context.Config.Releases}/ (DDD-dec-104)");
            }

            Pass(context, 6, $"{context.Config.ChangelogPath} is the projection");
        }
        finally
        {
            git.Try("worktree", "remove", "--force", worktree);
        }

        string message = $"{version} — {descriptor.Title!.Trim()}";
        if (git.Config("user.signingkey") is null)
        {
            return Refuse(context, 7, "git has no user.signingkey; canon never creates an unsigned tag");
        }

        if (plan)
        {
            context.Out.WriteLine($"release: plan complete. Would tag {underRelease[..12]} as {version} (\"{message}\"), signed, push it, and create the GitHub Release.");
            return Exit.Ok;
        }

        // 7. The signed tag.
        ProcessResult tag = git.Try("tag", "-s", version, underRelease, "-m", message);
        if (tag.Exit != 0)
        {
            return Refuse(context, 7, $"git tag -s failed: {tag.Error.Trim()}");
        }

        Pass(context, 7, $"signed tag {version} at {underRelease[..12]}");

        // 8. Push, then read back.
        string tagObject = git.Run("rev-parse", "refs/tags/" + version);
        ProcessResult push = git.Try("push", remote, $"refs/tags/{version}:refs/tags/{version}");
        string? pushed = git.RemoteRef(remote, "refs/tags/" + version);
        if (push.Exit != 0 || pushed != tagObject)
        {
            return Incomplete(context, 8, $"pushing the tag failed or {remote} holds a different object ({pushed ?? "none"}): {push.Error.Trim()}",
                $"The tag exists locally ({tagObject[..12]}). It is not deleted; push it by hand or delete the local tag once you know why.");
        }

        Pass(context, 8, $"{remote} holds refs/tags/{version} = {tagObject[..12]}");

        // 9. The GitHub Release.
        try
        {
            github.CreateRelease(version, message, descriptor.Summary!.Trim(), descriptor.Prerelease);
        }
        catch (CanonException exception)
        {
            return Incomplete(context, 9, exception.Message,
                $"The tag {version} is pushed and stays: a tag is a fact about history (rule 1). Create the Release by hand from {relative}.");
        }

        Pass(context, 9, $"GitHub Release {version}{(descriptor.Prerelease ? " (pre-release)" : "")}");
        context.Out.WriteLine($"release: {version} is cut at {underRelease[..12]}.");
        return Exit.Ok;
    }

    /// <summary>
    /// The GitHub client for this repository, or null (with the reason
    /// written) when GitHub is required and cannot be asked. Repository from
    /// canon.yaml's github:, else the remote's URL. API from CANON_GITHUB_API.
    /// </summary>
    internal static GitHubClient? GitHubFor(Context context, bool required, string command = "release", string? token = null)
    {
        string? repository = context.Config.GitHub
            ?? GitHubClient.RepositoryFromRemote(context.Git.Config($"remote.{context.Config.Remote}.url") ?? "");
        if (repository is null)
        {
            if (required)
            {
                context.Err.WriteLine($"{command}: cannot tell which GitHub repository this is; set github: in canon.yaml");
            }

            return null;
        }

        string api = context.Env("CANON_GITHUB_API") ?? GitHubClient.DefaultApi;
        return new GitHubClient(new Uri(api), repository, token ?? context.Env("GH_TOKEN") ?? context.Env("GITHUB_TOKEN"));
    }

    private static void Pass(Context context, int step, string what) =>
        context.Out.WriteLine($"  ok   {step}. {what}");

    private static int Refuse(Context context, int step, string why)
    {
        context.Err.WriteLine($"release: refused at step {step}: {why}");
        return Exit.Refused;
    }

    private static int Incomplete(Context context, int step, string why, string state)
    {
        context.Err.WriteLine($"release: step {step} failed after the tag was created: {why}");
        context.Err.WriteLine("release: " + state);
        return Exit.Refused;
    }
}
