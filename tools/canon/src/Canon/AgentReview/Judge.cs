// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text.Json.Nodes;
using System.Text.RegularExpressions;
using Canon.GitHub;

namespace Canon.AgentReview;

/// <summary>A verdict on one head: approved or not, and why, line by line.</summary>
internal sealed record Verdict(string Head, int? PullRequest, bool Approved, IReadOnlyList<string> Lines);

/// <summary>
/// Agent review's rule (DDD-dec-109), ported from Varve's eng/agent-review.cs
/// (ADR 0087). A head is approved when a pull request whose current head it
/// is carries a conversation comment "approve &lt;sha&gt;", at least
/// <see cref="MinimumShaPrefix"/> characters of the head, that is:
///
///   - by a human of the identity map, matched by login and numeric id;
///   - made by hand: GitHub records no app as having performed it, because a
///     session's comments are performed by the Claude app under Emil's login;
///   - not edited since it was made, because an edit is not attributed;
///   - by a holder of Approve for every agent whose commits are in the pull
///     request (its responsible human, or a delegate).
///
/// Unlike Varve, every pull request needs it, not only one with an agent's
/// commits: under one account, a commit with no trailer cannot be told from
/// Emil's own. Review submissions are not consulted. The pull request is read
/// through the API as data; nothing from it is run.
/// </summary>
internal static partial class Judge
{
    public const int MinimumShaPrefix = 12;

    /// <summary>The pull request's current head, judged.</summary>
    public static Verdict PullRequest(GitHubClient github, IdentityMap map, int number)
    {
        JsonNode pull = github.Get($"pulls/{number.ToString(CultureInfo.InvariantCulture)}");
        string head = pull["head"]?["sha"]?.GetValue<string>() ?? throw new Infrastructure.CanonException($"GitHub: pull request #{number} has no head");
        List<string> lines = [];

        HashSet<Agent> agents = [];
        int commits = 0;
        foreach (JsonObject commit in github.GetAll($"pulls/{number.ToString(CultureInfo.InvariantCulture)}/commits"))
        {
            if (commit["parents"] is JsonArray { Count: > 1 })
            {
                continue;
            }

            commits++;
            string message = commit["commit"]?["message"]?.GetValue<string>() ?? "";
            string email = commit["commit"]?["author"]?["email"]?.GetValue<string>() ?? "";
            agents.UnionWith(map.AgentsOf(message, email));
        }

        lines.Add($"note #{number}: head {head}, {commits} commit(s), agent(s): {(agents.Count == 0 ? "none" : string.Join(", ", agents.Select(a => a.Id)))}");

        Human? approver = null;
        foreach (JsonObject comment in github.GetAll($"issues/{number.ToString(CultureInfo.InvariantCulture)}/comments"))
        {
            string body = comment["body"]?.GetValue<string>() ?? "";
            MatchCollection approvals = Approval().Matches(body);
            string id = comment["id"]?.ToJsonString() ?? "?";
            string login = comment["user"]?["login"]?.GetValue<string>() ?? "";
            if (approvals.Count == 0)
            {
                continue;
            }

            if (!approvals.Any(m => head.StartsWith(m.Groups["sha"].Value, StringComparison.OrdinalIgnoreCase)))
            {
                lines.Add($"skip comment {id} by {login}: approves {approvals[0].Groups["sha"].Value[..MinimumShaPrefix]}, which is not the head");
                continue;
            }

            long account = comment["user"]?["id"]?.GetValue<long>() ?? -1;
            Human? human = map.HumanByAccount(login, account);

            if (human is null)
            {
                lines.Add($"skip comment {id} by {login} ({account}): not a human of the identity map");
            }
            else if (comment["performed_via_github_app"] is JsonObject app)
            {
                long appId = app["id"]?.GetValue<long>() ?? -1;
                string whose = map.AgentByApp(appId) is Agent agent ? $", which performs the writes of '{agent.Id}'" : "";
                lines.Add($"skip comment {id} by {login}: made through the app {app["slug"]?.GetValue<string>() ?? "?"} ({appId}){whose}, not by hand");
            }
            else if (comment["updated_at"]?.GetValue<string>() != comment["created_at"]?.GetValue<string>())
            {
                lines.Add($"skip comment {id} by {login}: edited after it was made");
            }
            else if (agents.FirstOrDefault(agent => !map.HoldsApprove(human, agent)) is Agent unheld)
            {
                lines.Add($"skip comment {id} by {login}: does not hold Approve for '{unheld.Id}'");
            }
            else
            {
                approver = human;
                lines.Add($"ok  comment {id}: {login} approves {head[..MinimumShaPrefix]} by hand");
                break;
            }
        }

        if (approver is null)
        {
            string who = string.Join(", ", map.Humans.Select(h => h.GitHub));
            lines.Add($"not approved: #{number} needs a comment 'approve {head}' (at least {MinimumShaPrefix} characters of the head), "
                + $"written by hand by {who}, not edited");
        }

        return new Verdict(head, number, approver is not null, lines);
    }

    /// <summary>
    /// A commit, as pushed to land/: approved when it is the current head of a
    /// pull request whose own verdict is approved. A commit that is no pull
    /// request's head is not.
    /// </summary>
    public static Verdict Commit(GitHubClient github, IdentityMap map, string sha)
    {
        List<string> lines = [];
        foreach (JsonObject pull in github.GetAll($"commits/{sha}/pulls"))
        {
            if (pull["head"]?["sha"]?.GetValue<string>() != sha || pull["number"]?.GetValue<int>() is not int number)
            {
                continue;
            }

            Verdict verdict = PullRequest(github, map, number);
            lines.AddRange(verdict.Lines);
            if (verdict.Approved)
            {
                return verdict with { Lines = lines };
            }
        }

        lines.Add($"not approved: {sha[..Math.Min(sha.Length, MinimumShaPrefix)]} is not the head of an approved pull request; push an approved pull request's head, unchanged");
        return new Verdict(sha, null, false, lines);
    }

    [GeneratedRegex(@"\bapprove\s+(?<sha>[0-9a-fA-F]{12,40})\b", RegexOptions.IgnoreCase | RegexOptions.CultureInvariant)]
    private static partial Regex Approval();
}
