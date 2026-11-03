// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.Json;
using System.Text.Json.Nodes;
using Canon.Infrastructure;

namespace Canon.AgentReview;

/// <summary>A human who may approve: their GitHub login and numeric id, and their delegates.</summary>
internal sealed record Human(string Id, string GitHub, long GitHubId, IReadOnlyList<string> Emails, IReadOnlyList<string> Delegates);

/// <summary>
/// An agent: identified on a commit by its trailer (Claude-Session) or an
/// author email, and on GitHub by the apps that perform its writes. Its
/// responsible human holds Approve for it.
/// </summary>
internal sealed record Agent(string Id, string Trailer, IReadOnlyList<string> Emails, IReadOnlyList<long> Apps, string Responsible);

/// <summary>
/// .github/identities.json, the counterpart of Varve's eng/identities.json
/// (ADR 0087; DDD-dec-109). It is read from main's checkout, never from the
/// change being judged, so a change cannot authorise itself.
/// </summary>
internal sealed class IdentityMap
{
    public const string DefaultPath = ".github/identities.json";

    private IdentityMap(IReadOnlyList<Human> humans, IReadOnlyList<Agent> agents)
    {
        Humans = humans;
        Agents = agents;
    }

    public IReadOnlyList<Human> Humans { get; }

    public IReadOnlyList<Agent> Agents { get; }

    public static IdentityMap Parse(string json, string where)
    {
        JsonObject root;
        try
        {
            root = JsonNode.Parse(json) as JsonObject ?? throw new CanonException($"{where}: not a JSON object");
        }
        catch (JsonException exception)
        {
            throw new CanonException($"{where}: {exception.Message}", exception);
        }

        List<Human> humans = [];
        foreach (JsonObject human in Objects(root, "humans", where))
        {
            humans.Add(new Human(
                Text(human, "id", where),
                Text(human, "github", where),
                human["github_id"]?.GetValue<long>() ?? throw new CanonException($"{where}: a human has no github_id"),
                Strings(human, "emails"),
                Strings(human, "delegates")));
        }

        List<Agent> agents = [];
        foreach (JsonObject agent in Objects(root, "agents", where))
        {
            string responsible = Text(agent, "responsible", where);
            if (humans.All(h => h.Id != responsible))
            {
                throw new CanonException($"{where}: agent '{Text(agent, "id", where)}' names '{responsible}', who is not a human of the map");
            }

            agents.Add(new Agent(
                Text(agent, "id", where),
                Text(agent, "trailer", where),
                Strings(agent, "emails"),
                (agent["apps"] as JsonArray ?? []).Select(a => a!.GetValue<long>()).ToList(),
                responsible));
        }

        if (humans.Count == 0)
        {
            throw new CanonException($"{where}: no humans, so nobody could approve");
        }

        return new IdentityMap(humans, agents);
    }

    /// <summary>The human with this login and this numeric id; a renamed or reused login does not match.</summary>
    public Human? HumanByAccount(string login, long id) =>
        Humans.FirstOrDefault(h => string.Equals(h.GitHub, login, StringComparison.OrdinalIgnoreCase) && h.GitHubId == id);

    /// <summary>The agents a commit is by: its trailer, or its author email.</summary>
    public IEnumerable<Agent> AgentsOf(string message, string authorEmail) =>
        Agents.Where(agent =>
            message.Split('\n').Any(line => line.TrimStart().StartsWith(agent.Trailer + ":", StringComparison.OrdinalIgnoreCase))
            || agent.Emails.Contains(authorEmail, StringComparer.OrdinalIgnoreCase));

    /// <summary>The agent whose writes this app performs, if any.</summary>
    public Agent? AgentByApp(long app) => Agents.FirstOrDefault(agent => agent.Apps.Contains(app));

    /// <summary>Approve for an agent: its responsible human, or one of that human's delegates.</summary>
    public bool HoldsApprove(Human human, Agent agent) =>
        human.Id == agent.Responsible
        || Humans.Any(h => h.Id == agent.Responsible && h.Delegates.Contains(human.Id, StringComparer.Ordinal));

    private static IEnumerable<JsonObject> Objects(JsonObject root, string key, string where) =>
        (root[key] as JsonArray ?? []).Select(n => n as JsonObject ?? throw new CanonException($"{where}: an entry of {key} is not an object"));

    private static string Text(JsonObject node, string key, string where) =>
        node[key]?.GetValue<string>() is { Length: > 0 } text ? text : throw new CanonException($"{where}: an entry has no {key}");

    private static List<string> Strings(JsonObject node, string key) =>
        (node[key] as JsonArray ?? []).Select(n => n!.GetValue<string>()).ToList();
}
