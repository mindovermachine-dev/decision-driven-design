// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

using System;
using System.IO;
using System.Linq;
using Canon.AgentReview;
using Xunit;
using YamlDotNet.RepresentationModel;

namespace Canon.Tests;

/// <summary>
/// This repository's own declarations, read as they are on disk: the
/// rulesets, the identity map and the agent review workflow. These are the
/// parts of DDD-dec-109 and DDD-dec-110 that no code path exercises, so a
/// test reads the files themselves (as Varve's agent-review-tamper.cs reads
/// its workflow).
/// </summary>
public sealed class RepositoryDeclarationTests
{
    private static readonly string Root = FindRoot();

    private static string FindRoot()
    {
        for (DirectoryInfo? directory = new(AppContext.BaseDirectory); directory is not null; directory = directory.Parent)
        {
            if (File.Exists(Path.Combine(directory.FullName, "canon.yaml"))
                && File.Exists(Path.Combine(directory.FullName, ".github", "identities.json")))
            {
                return directory.FullName;
            }
        }

        throw new InvalidOperationException("the repository root (canon.yaml and .github/identities.json) is not above the test binaries");
    }

    private static string Read(string path) => File.ReadAllText(Path.Combine(Root, path));

    private static YamlMappingNode Yaml(string path)
    {
        YamlStream stream = [];
        stream.Load(new StringReader(Read(path)));
        return (YamlMappingNode)stream.Documents[0].RootNode;
    }

    private static YamlNode Child(YamlNode node, string key) => ((YamlMappingNode)node).Children[new YamlScalarNode(key)];

    private static string Text(YamlNode node, string key) => ((YamlScalarNode)Child(node, key)).Value!;

    /// <summary>TAMPER: a check from anything but its pinned app must not satisfy the ruleset, so both are pinned.</summary>
    [Fact]
    public void TheTrunkPinsEachRequiredCheckToItsApp()
    {
        var checks = RequiredChecks.OnTrunk(Read(".github/repo-standard.yaml"));

        Assert.Equal(15368, checks["pipeline (devcontainer)"]);
        Assert.NotNull(checks["agent review"]);
        Assert.All(checks, check => Assert.NotNull(check.Value));
    }

    [Fact]
    public void TheTrunkHasNoBypass()
    {
        YamlNode trunk = ((YamlSequenceNode)Child(Yaml(".github/repo-standard.yaml"), "rulesets"))
            .Single(r => Text(r, "name") == "trunk");
        Assert.Empty((YamlSequenceNode)Child(trunk, "bypass_actors"));
    }

    [Fact]
    public void SignedCommitsIsBypassedByTheAdminRoleAlone()
    {
        YamlNode signed = ((YamlSequenceNode)Child(Yaml(".github/repo-standard.yaml"), "rulesets"))
            .Single(r => Text(r, "name") == "Signed Commits");
        YamlNode actor = Assert.Single((YamlSequenceNode)Child(signed, "bypass_actors"));
        Assert.Equal("RepositoryRole", Text(actor, "actor_type"));
        Assert.Equal("5", Text(actor, "actor_id"));
    }

    [Fact]
    public void TheIdentityMapNamesEmilAsResponsibleForTheSessions()
    {
        IdentityMap map = IdentityMap.Parse(Read(".github/identities.json"), ".github/identities.json");

        Human emil = Assert.Single(map.Humans);
        Assert.Equal(("Hafeok", 2194785L), (emil.GitHub, emil.GitHubId));
        Agent sessions = Assert.Single(map.Agents);
        Assert.Equal("Claude-Session", sessions.Trailer);
        Assert.Equal("emil", sessions.Responsible);
        Assert.Contains(1236702L, sessions.Apps);
    }

    /// <summary>
    /// TAMPER: the workflow cannot run a pull request's copy of the judge. It
    /// runs on main's triggers only, checks out main by name, mints the gates
    /// App's token from its environment, and no job is itself named
    /// "agent review".
    /// </summary>
    [Fact]
    public void TheWorkflowJudgesWithMainsCopyOnTrustedTriggersOnly()
    {
        const string Path = ".github/workflows/agent-review.yml";
        YamlMappingNode workflow = Yaml(Path);
        string text = Read(Path);

        Assert.Equal(
            ["issue_comment", "pull_request_target"],
            ((YamlMappingNode)Child(workflow, "on")).Children.Keys.Select(k => ((YamlScalarNode)k).Value!).Order(StringComparer.Ordinal));
        Assert.Empty((YamlMappingNode)Child(workflow, "permissions"));

        YamlMappingNode jobs = (YamlMappingNode)Child(workflow, "jobs");
        YamlNode judge = Assert.Single(jobs.Children).Value;
        Assert.Equal("gates", Text(judge, "environment"));
        Assert.NotEqual("agent review", Text(judge, "name"));

        YamlSequenceNode steps = (YamlSequenceNode)Child(judge, "steps");
        YamlNode checkout = steps.Single(s => ((YamlMappingNode)s).Children.ContainsKey(new YamlScalarNode("uses"))
            && Text(s, "uses").StartsWith("actions/checkout@", StringComparison.Ordinal));
        Assert.Equal("${{ github.event.repository.default_branch }}", Text(Child(checkout, "with"), "ref"));
        Assert.Contains(steps, s => ((YamlMappingNode)s).Children.ContainsKey(new YamlScalarNode("run"))
            && Text(s, "run").Contains("agent-review", StringComparison.Ordinal) && Text(s, "run").Contains("--post", StringComparison.Ordinal));

        Assert.DoesNotContain("pull_request.head", text, StringComparison.Ordinal);
        Assert.DoesNotContain("refs/pull/", text, StringComparison.Ordinal);
        Assert.DoesNotContain("github.sha", text, StringComparison.Ordinal);
    }
}
