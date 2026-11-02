// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;
using Canon.Infrastructure;

namespace Canon.Commands;

/// <summary>
/// canon issue-refs [--base &lt;ref&gt;] [--head &lt;ref&gt;] [--basis]
///
/// As Varve's eng/issue-refs.cs: every non-merge commit in the range carries
/// "Refs #N" or "Closes #N" (also Fixes, Resolves) as a line of its body. A
/// bare "#N" is not enough. Merge commits are exempt by parent count, and
/// authors on canon.yaml's closed exempt list are exempt. The issue's
/// existence is not checked: that needs the network in a gate that must run
/// offline.
///
/// --basis adds DDD-dec-105: a non-merge commit that changes a path under
/// basis.paths (core/) carries a Basis: line, from basis.from (99d0a0f) on;
/// and from basis.resolve-from on, every id on it resolves at that commit, to
/// a file in a canon directory or to an id named in the pins file.
///
/// "From X on" means: X and every commit X is an ancestor of. A commit in the
/// range that does not descend from X (one brought in by a merge from a line
/// that branched earlier) is not covered.
/// </summary>
internal static partial class IssueRefsCommand
{
    public static int Run(Context context, IReadOnlyList<string> arguments)
    {
        string? baseRef = null;
        string head = "HEAD";
        bool basis = false;
        for (int i = 0; i < arguments.Count; i++)
        {
            switch (arguments[i])
            {
                case "--base" when i + 1 < arguments.Count:
                    baseRef = arguments[++i];
                    break;
                case "--head" when i + 1 < arguments.Count:
                    head = arguments[++i];
                    break;
                case "--basis":
                    basis = true;
                    break;
                default:
                    context.Err.WriteLine($"issue-refs: unknown argument '{arguments[i]}'");
                    return Exit.CouldNotRun;
            }
        }

        Git git = context.Git;
        baseRef ??= DefaultBase(context);
        string? baseSha = git.Resolve(baseRef);
        string? headSha = git.Resolve(head);
        if (baseSha is null || headSha is null)
        {
            context.Err.WriteLine($"issue-refs: cannot resolve {(baseSha is null ? baseRef : head)}");
            return Exit.CouldNotRun;
        }

        string? refsFrom = Resolve(context, context.Config.RefsFrom, "issue-refs.from");
        string? basisFrom = Resolve(context, context.Config.BasisFrom, "basis.from");
        string? resolveFrom = Resolve(context, context.Config.BasisResolveFrom, "basis.resolve-from");
        if ((context.Config.RefsFrom is not null && refsFrom is null)
            || (basis && ((context.Config.BasisFrom is not null && basisFrom is null)
                || (context.Config.BasisResolveFrom is not null && resolveFrom is null))))
        {
            return Exit.CouldNotRun;
        }

        string[] commits = git.Run("rev-list", "--no-merges", "--reverse", $"{baseSha}..{headSha}")
            .Split('\n', StringSplitOptions.RemoveEmptyEntries);

        List<string> failures = [];
        int refsChecked = 0;
        int basisChecked = 0;
        foreach (string commit in commits)
        {
            string author = git.Run("show", "-s", "--format=%ae", commit);
            if (context.Config.ExemptAuthors.Contains(author, StringComparer.OrdinalIgnoreCase))
            {
                continue;
            }

            string body = git.Run("show", "-s", "--format=%B", commit);
            string subject = git.Run("show", "-s", "--format=%s", commit);
            string label = $"{commit[..12]} {subject}";

            if (Covers(git, refsFrom, commit))
            {
                refsChecked++;
                if (!IssueReference().IsMatch(body))
                {
                    failures.Add($"{label}: no 'Refs #N' or 'Closes #N' line");
                }
            }

            if (basis && Covers(git, basisFrom, commit) && TouchesBasisPaths(context, commit))
            {
                basisChecked++;
                List<string> lines = body.Split('\n').Where(l => l.StartsWith("Basis:", StringComparison.Ordinal)).ToList();
                if (lines.Count == 0)
                {
                    failures.Add($"{label}: changes {string.Join(", ", context.Config.BasisPaths)} and has no Basis: line (DDD-dec-105)");
                }
                else if (Covers(git, resolveFrom, commit))
                {
                    foreach (string id in lines.SelectMany(l => Id().Matches(l).Select(m => m.Value)).Distinct())
                    {
                        if (!Resolves(context, commit, id))
                        {
                            failures.Add($"{label}: Basis id {id} resolves to no file in {string.Join(", ", context.Config.CanonDirectories)} and no pin in {context.Config.Pins} at this commit (DDD-dec-105)");
                        }
                    }
                }
            }
        }

        foreach (string failure in failures)
        {
            context.Err.WriteLine("issue-refs: " + failure);
        }

        string summary = $"{commits.Length} commits in {baseSha[..12]}..{headSha[..12]}; Refs checked on {refsChecked}"
            + (basis ? $", Basis on {basisChecked}" : "");
        if (failures.Count > 0)
        {
            context.Err.WriteLine($"issue-refs: refused, {failures.Count} finding(s). {summary}");
            return Exit.Refused;
        }

        context.Out.WriteLine($"issue-refs: ok. {summary}");
        return Exit.Ok;
    }

    private static string DefaultBase(Context context)
    {
        if (context.Env("GITHUB_BASE_REF") is { } pullRequestBase)
        {
            return $"{context.Config.Remote}/{pullRequestBase}";
        }

        if (context.Env("CANON_PUSH_BEFORE") is { } before && !before.All(c => c == '0'))
        {
            return before;
        }

        return $"{context.Config.Remote}/{context.Config.Trunk}";
    }

    private static string? Resolve(Context context, string? revision, string key)
    {
        if (revision is null)
        {
            return null;
        }

        string? sha = context.Git.Resolve(revision);
        if (sha is null)
        {
            context.Err.WriteLine($"issue-refs: {key} names {revision}, which is not a commit here (a shallow clone? fetch the history)");
        }

        return sha;
    }

    private static bool Covers(Git git, string? from, string commit) =>
        from is null || git.IsAncestor(from, commit);

    private static bool TouchesBasisPaths(Context context, string commit) =>
        context.Git.Run("diff-tree", "--root", "--no-commit-id", "--name-only", "-r", commit)
            .Split('\n', StringSplitOptions.RemoveEmptyEntries)
            .Any(p => context.Config.BasisPaths.Any(b => p.StartsWith(b, StringComparison.Ordinal)));

    private static bool Resolves(Context context, string commit, string id)
    {
        foreach (string directory in context.Config.CanonDirectories)
        {
            if (context.Git.Try("cat-file", "-e", $"{commit}:{directory.TrimEnd('/')}/{id}.yaml").Exit == 0)
            {
                return true;
            }
        }

        string? pins = context.Git.Show(commit, context.Config.Pins);
        return pins is not null && Regex.IsMatch(pins, $@"(?<![A-Za-z0-9-]){Regex.Escape(id)}(?![0-9])");
    }

    [GeneratedRegex(@"^\s*(Refs|Closes|Fixes|Resolves)\s+#[0-9]+\b", RegexOptions.Multiline | RegexOptions.IgnoreCase)]
    private static partial Regex IssueReference();

    [GeneratedRegex(@"DDD-[a-z]+-[0-9]+")]
    private static partial Regex Id();
}
