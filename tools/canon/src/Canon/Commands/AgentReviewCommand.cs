// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

using System.Collections.Generic;
using System.Globalization;
using System.IO;
using Canon.AgentReview;
using Canon.GitHub;

namespace Canon.Commands;

/// <summary>
/// Agent review (DDD-dec-109), ported from Varve's eng/agent-review.cs:
///
///   canon agent-review &lt;pr&gt; [--post]          judge the pull request's current head
///   canon agent-review --commit &lt;sha&gt; [--post] judge the pull request behind a land/ push
///
/// The identity map is .github/identities.json in this checkout, and the
/// pinned app is read from .github/repo-standard.yaml in this checkout. The
/// workflow runs it from main's checkout, so both are main's.
///
/// Without --post it prints the verdict: exit 0 approved, 1 not. With --post
/// it creates or updates the check run "agent review" on the head with
/// GATES_TOKEN, the gates App's token, and exits 0 whatever the verdict: a
/// failing verdict is a posted failure, not a failing job (as Varve). Exit 2
/// when it could not run.
/// </summary>
internal static class AgentReviewCommand
{
    public const string CheckName = "agent review";

    public static int Run(Context context, IReadOnlyList<string> arguments)
    {
        int? pullRequest = null;
        string? commit = null;
        bool post = false;
        for (int i = 0; i < arguments.Count; i++)
        {
            switch (arguments[i])
            {
                case "--post":
                    post = true;
                    break;
                case "--commit" when i + 1 < arguments.Count:
                    commit = arguments[++i];
                    break;
                default:
                    if (int.TryParse(arguments[i].TrimStart('#'), NumberStyles.None, CultureInfo.InvariantCulture, out int number) && number > 0)
                    {
                        pullRequest = number;
                        break;
                    }

                    context.Err.WriteLine($"agent-review: unknown argument '{arguments[i]}'");
                    return Exit.CouldNotRun;
            }
        }

        if (pullRequest is null == commit is null)
        {
            context.Err.WriteLine("agent-review: give a pull request number or --commit <sha>, one of them");
            return Exit.CouldNotRun;
        }

        string mapPath = Path.Combine(context.Root, IdentityMap.DefaultPath);
        if (!File.Exists(mapPath))
        {
            context.Err.WriteLine($"agent-review: no {IdentityMap.DefaultPath}, so nobody could approve");
            return Exit.CouldNotRun;
        }

        IdentityMap map = IdentityMap.Parse(File.ReadAllText(mapPath), IdentityMap.DefaultPath);

        string? gatesToken = context.Env("GATES_TOKEN");
        if (post && gatesToken is null)
        {
            context.Err.WriteLine("agent-review: --post without GATES_TOKEN; the verdict cannot be posted where the ruleset reads it");
            return Exit.CouldNotRun;
        }

        using GitHubClient? github = ReleaseCommand.GitHubFor(context, required: true, "agent-review");
        if (github is null)
        {
            return Exit.CouldNotRun;
        }

        Verdict verdict = pullRequest is int pr
            ? Judge.PullRequest(github, map, pr)
            : Judge.Commit(github, map, context.Git.Resolve(commit!) ?? commit!);

        foreach (string line in verdict.Lines)
        {
            context.Out.WriteLine(line);
        }

        if (!post)
        {
            return verdict.Approved ? Exit.Ok : Exit.Refused;
        }

        string standard = Path.Combine(context.Root, RequiredChecks.DefaultPath);
        long? pinned = RequiredChecks.OnTrunk(File.Exists(standard) ? File.ReadAllText(standard) : null)
            .TryGetValue(CheckName, out long? app) ? app : null;

        using GitHubClient? gates = ReleaseCommand.GitHubFor(context, required: true, "agent-review", gatesToken);
        gates!.PostCheck(
            CheckName,
            verdict.Head,
            verdict.Approved,
            verdict.Approved ? "Approved" : "Not approved",
            string.Join("\n", verdict.Lines),
            pinned);
        context.Out.WriteLine($"ok  posted '{CheckName}' = {(verdict.Approved ? "success" : "failure")} on {verdict.Head}");
        return Exit.Ok;
    }
}
