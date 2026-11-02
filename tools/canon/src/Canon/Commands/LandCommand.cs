// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

using System;
using System.Collections.Generic;
using System.Globalization;
using System.Text.RegularExpressions;
using Canon.Infrastructure;

namespace Canon.Commands;

/// <summary>
/// Landing, as two commands, ported from Varve's eng/land.cs (Hafeok/varve
/// 5f5c5a9) with its semantics unchanged (DESIGN.md §4.2):
///
///   canon land &lt;pr&gt;             push the pull request's head to land/&lt;name&gt;
///   canon land &lt;pr&gt; --main      fast-forward main to it, then delete land/&lt;name&gt;
///   canon land --commit &lt;rev&gt;   the same for a commit of one's own
///     --name &lt;name&gt;  --print
///
/// It automates the landing Emil's protection ruling defines and decides
/// nothing: the rulesets judge. main moves only by a fast-forward push of the
/// exact commit whose checks ran on land/&lt;name&gt;. It never calls GitHub's
/// merge API and never makes a merge commit.
///
/// Not ported: land.cs's advisory look for an "approve &lt;sha&gt;" comment,
/// which belongs to Varve's agent-review gate. This repository has none.
/// </summary>
internal static partial class LandCommand
{
    public static int Run(Context context, IReadOnlyList<string> arguments)
    {
        int? pullRequest = null;
        string? commit = null;
        string? name = null;
        bool toMain = false;
        bool print = false;

        for (int i = 0; i < arguments.Count; i++)
        {
            switch (arguments[i])
            {
                case "--main":
                    toMain = true;
                    break;
                case "--print":
                    print = true;
                    break;
                case "--commit" when i + 1 < arguments.Count:
                    commit = arguments[++i];
                    break;
                case "--name" when i + 1 < arguments.Count:
                    name = arguments[++i];
                    break;
                default:
                    if (int.TryParse(arguments[i].TrimStart('#'), NumberStyles.None, CultureInfo.InvariantCulture, out int number) && number > 0)
                    {
                        pullRequest = number;
                        break;
                    }

                    context.Err.WriteLine($"land: unknown argument '{arguments[i]}'");
                    return Exit.CouldNotRun;
            }
        }

        if (pullRequest is null == commit is null)
        {
            context.Err.WriteLine("land: give a pull request number or --commit <rev>, one of them");
            return Exit.CouldNotRun;
        }

        Git git = context.Git;
        string remote = context.Config.Remote;
        string trunk = context.Config.Trunk;

        git.Run("fetch", "--quiet", "--no-tags", remote, $"refs/heads/{trunk}");
        string main = git.Run("rev-parse", "FETCH_HEAD");

        string head;
        if (pullRequest is int pr)
        {
            git.Run("fetch", "--quiet", "--no-tags", remote, $"refs/pull/{pr}/head");
            head = git.Run("rev-parse", "FETCH_HEAD");
        }
        else
        {
            head = git.Resolve(commit!) ?? throw new CanonException($"{commit} does not name a commit");
        }

        bool namedByHand = name is not null;
        name ??= ReleaseName(context, main, head) ?? (pullRequest is int n ? $"pr-{n}" : head[..12]);
        string land = $"refs/heads/land/{name}";
        string what = pullRequest is int p ? $"#{p}'s head {head[..12]}" : head[..12];

        if (main == head)
        {
            context.Out.WriteLine($"land: {trunk} is already at {head[..12]}; nothing to land");
            return Exit.Ok;
        }

        if (!git.IsAncestor(main, head))
        {
            context.Err.WriteLine($"land: {trunk} ({main[..12]}) is not an ancestor of {what}, so {trunk} cannot be fast-forwarded to it. Bring {trunk} into the branch first.");
            return Exit.Refused;
        }

        string? landed = git.RemoteRef(remote, land);

        if (!toMain)
        {
            if (landed == head)
            {
                context.Out.WriteLine($"land: land/{name} is at {head[..12]} already; its checks are running or done.");
            }
            else if (Push(context, print, $"{head}:{land}") != 0)
            {
                context.Err.WriteLine($"land: {remote} refused land/{name}");
                return Exit.Refused;
            }

            string target = pullRequest is int again ? again.ToString(CultureInfo.InvariantCulture) : $"--commit {head[..12]}";
            context.Out.WriteLine();
            context.Out.WriteLine($"Next, once the checks on land/{name} are green:");
            context.Out.WriteLine($"  canon land {target}{(namedByHand ? $" --name {name}" : "")} --main");
            return Exit.Ok;
        }

        if (landed != head)
        {
            context.Err.WriteLine(landed is null
                ? $"land: there is no land/{name} on {remote}; push it first (without --main) and let its checks run"
                : $"land: land/{name} is at {landed[..12]}, not {what}; the head moved since it was pushed. Land it again, without --main.");
            return Exit.Refused;
        }

        if (Push(context, print, $"{head}:refs/heads/{trunk}") != 0)
        {
            context.Err.WriteLine($"land: {remote} refused to move {trunk}. If a required check on land/{name} has not passed yet, wait for it and run this again.");
            return Exit.Refused;
        }

        Push(context, print, "--delete", land);
        if (print)
        {
            return Exit.Ok;
        }

        context.Out.WriteLine();
        context.Out.WriteLine($"land: {trunk} is at {head[..12]}.{(name.StartsWith("release-", StringComparison.Ordinal) ? " The release it carries is cut next: canon release " + name["release-".Length..] : "")}");
        return Exit.Ok;
    }

    /// <summary>release-&lt;version&gt;, when the head adds a descriptor the trunk does not have.</summary>
    private static string? ReleaseName(Context context, string main, string head)
    {
        string releases = context.Config.Releases.TrimEnd('/');
        foreach (string path in context.Git.Run("diff", "--name-only", "--diff-filter=A", main, head, "--", releases + "/")
                     .Split('\n', StringSplitOptions.RemoveEmptyEntries))
        {
            Match match = DescriptorPath().Match(path);
            if (match.Success)
            {
                return $"release-{match.Groups[1].Value}";
            }
        }

        return null;
    }

    private static int Push(Context context, bool print, params string[] what)
    {
        List<string> arguments = ["push", context.Config.Remote, .. what];
        context.Out.WriteLine("$ git " + string.Join(' ', arguments));
        if (print)
        {
            return 0;
        }

        ProcessResult result = context.Git.Try([.. arguments]);
        if (result.Exit != 0)
        {
            context.Err.Write(result.Error);
        }

        return result.Exit;
    }

    [GeneratedRegex(@"/(v[^/]+)\.yaml$")]
    private static partial Regex DescriptorPath();
}
