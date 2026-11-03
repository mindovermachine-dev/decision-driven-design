// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.Json.Nodes;
using Canon.Infrastructure;
using Xunit;

namespace Canon.Tests;

/// <summary>
/// Agent review (DDD-dec-109), Detroit-style: canon runs as a process would,
/// over a real repository, against a real HTTP server holding a pull
/// request's state as GitHub does. Nothing in canon is replaced. The tamper
/// cases Emil ruled are marked TAMPER.
/// </summary>
public sealed class AgentReviewTests : IDisposable
{
    private const string Repository = "mindovermachine-dev/test";
    private const string Head = "1234567890abcdef1234567890abcdef12345678";
    private const string Earlier = "fedcba0987654321fedcba0987654321fedcba09";
    private const long Emil = 2194785;
    private const long ClaudeApp = 1236702;
    private const long GatesApp = 5220446;
    private const long Actions = 15368;
    private const string Session = "the change\n\nRefs #1\n\nClaude-Session: https://claude.ai/code/session_x";

    internal const string Identities = """
        {
          "humans": [
            { "id": "emil", "name": "Emil", "github": "Hafeok", "github_id": 2194785,
              "emails": ["emil@okkels-klein.dk"], "delegates": [] },
            { "id": "erin", "name": "Erin", "github": "erin", "github_id": 42,
              "emails": ["erin@example.invalid"], "delegates": [] }
          ],
          "agents": [
            { "id": "claude-code", "name": "Claude Code sessions", "trailer": "Claude-Session",
              "emails": ["claude+emil@okkels-klein.dk"], "apps": [1236702], "responsible": "emil" }
          ]
        }
        """;

    internal const string Standard = """
        rulesets:
        - name: trunk
          target: branch
          enforcement: active
          conditions:
            ref_name:
              exclude: []
              include:
              - ~DEFAULT_BRANCH
          rules:
          - type: required_status_checks
            parameters:
              strict_required_status_checks_policy: false
              required_status_checks:
              - context: pipeline (devcontainer)
                integration_id: 15368
              - context: agent review
                integration_id: 5220446
          bypass_actors: []
        """;

    private readonly Sandbox sandbox = new();
    private readonly GitHubServer github = new(Repository);

    public AgentReviewTests()
    {
        sandbox.Write("canon.yaml", $"github: {Repository}\n");
        sandbox.Write(".github/identities.json", Identities);
        sandbox.Write(".github/repo-standard.yaml", Standard);
        sandbox.Commit("base\n\nRefs #1");
        sandbox.Git("push", "--quiet", "origin", "main");
        github.TokenApps["test-token"] = Actions;
        github.TokenApps["gates-token"] = GatesApp;
    }

    public void Dispose()
    {
        github.Dispose();
        sandbox.Dispose();
    }

    private (int Exit, string Out, string Err) Review(params string[] arguments) =>
        sandbox.Canon(github.Environment(), ["agent-review", .. arguments]);

    private void SessionPullRequest(int number = 7, string head = Head) =>
        github.AddPullRequest(number, head, (Session, "claude+emil@okkels-klein.dk"));

    [Fact]
    public void NoApprovalIsNotGreen()
    {
        SessionPullRequest();
        var result = Review("7");
        ReleaseRepository.Expect(result, 1);
        Assert.Contains("needs a comment 'approve " + Head, result.Out, StringComparison.Ordinal);
    }

    [Fact]
    public void EmilsApprovalByHandWithTwelveCharactersIsGreen()
    {
        SessionPullRequest();
        github.AddComment(7, "Hafeok", Emil, $"approve {Head[..12]}");
        ReleaseRepository.Expect(Review("7"), 0);
    }

    [Fact]
    public void TheFullHeadAmongOtherWordsIsGreen()
    {
        SessionPullRequest();
        github.AddComment(7, "Hafeok", Emil, $"Read it twice.\nApprove {Head}\nThanks.");
        ReleaseRepository.Expect(Review("7"), 0);
    }

    [Fact]
    public void ElevenCharactersAreNotEnough()
    {
        SessionPullRequest();
        github.AddComment(7, "Hafeok", Emil, $"approve {Head[..11]}");
        ReleaseRepository.Expect(Review("7"), 1);
    }

    /// <summary>TAMPER: an approval of an older head does not count.</summary>
    [Fact]
    public void AnApprovalOfAnEarlierHeadDoesNotCount()
    {
        SessionPullRequest();
        github.AddComment(7, "Hafeok", Emil, $"approve {Earlier}");
        var result = Review("7");
        ReleaseRepository.Expect(result, 1);
        Assert.Contains("which is not the head", result.Out, StringComparison.Ordinal);
    }

    /// <summary>
    /// TAMPER: a session's comment, which GitHub shows under Emil's own login
    /// and id but records as made through the Claude app, does not count.
    /// </summary>
    [Fact]
    public void ASessionAuthoredCommentDoesNotCount()
    {
        SessionPullRequest();
        github.AddComment(7, "Hafeok", Emil, $"approve {Head}", app: ClaudeApp);
        var result = Review("7");
        ReleaseRepository.Expect(result, 1);
        Assert.Contains("which performs the writes of 'claude-code', not by hand", result.Out, StringComparison.Ordinal);
    }

    [Fact]
    public void ACommentThroughAnyOtherAppDoesNotCount()
    {
        SessionPullRequest();
        github.AddComment(7, "Hafeok", Emil, $"approve {Head}", app: 999);
        ReleaseRepository.Expect(Review("7"), 1);
    }

    [Fact]
    public void AStrangerDoesNotCount()
    {
        SessionPullRequest();
        github.AddComment(7, "mallory", 666, $"approve {Head}");
        ReleaseRepository.Expect(Review("7"), 1);
    }

    [Fact]
    public void EmilsLoginOnAnotherAccountDoesNotCount()
    {
        SessionPullRequest();
        github.AddComment(7, "Hafeok", 31337, $"approve {Head}");
        ReleaseRepository.Expect(Review("7"), 1);
    }

    /// <summary>A session can edit Emil's comment under his account; an edit is not attributed.</summary>
    [Fact]
    public void AnEditedCommentDoesNotCount()
    {
        SessionPullRequest();
        github.AddComment(7, "Hafeok", Emil, $"approve {Head}", edited: true);
        var result = Review("7");
        ReleaseRepository.Expect(result, 1);
        Assert.Contains("edited after it was made", result.Out, StringComparison.Ordinal);
    }

    /// <summary>A session's commit is known by its Claude-Session trailer, whatever its author email says.</summary>
    [Fact]
    public void TheTrailerMakesACommitASessionsSoOnlyItsResponsibleHumanApproves()
    {
        github.AddPullRequest(7, Head, (Session, "emil@okkels-klein.dk"));
        github.AddComment(7, "erin", 42, $"approve {Head}");
        var result = Review("7");
        ReleaseRepository.Expect(result, 1);
        Assert.Contains("does not hold Approve for 'claude-code'", result.Out, StringComparison.Ordinal);

        github.AddComment(7, "Hafeok", Emil, $"approve {Head}");
        ReleaseRepository.Expect(Review("7"), 0);
    }

    [Fact]
    public void APullRequestWithNoSessionCommitsStillNeedsAnApproval()
    {
        github.AddPullRequest(7, Head, ("by hand\n\nRefs #1", "emil@okkels-klein.dk"));
        ReleaseRepository.Expect(Review("7"), 1);

        github.AddComment(7, "erin", 42, $"approve {Head}");
        ReleaseRepository.Expect(Review("7"), 0);
    }

    [Fact]
    public void ALandPushOfAnApprovedPullRequestsHeadIsGreen()
    {
        SessionPullRequest();
        github.AddComment(7, "Hafeok", Emil, $"approve {Head}");
        ReleaseRepository.Expect(Review("--commit", Head), 0);
    }

    [Fact]
    public void ACommitThatIsNoPullRequestsHeadIsNotGreen()
    {
        SessionPullRequest();
        github.AddComment(7, "Hafeok", Emil, $"approve {Head}");
        var result = Review("--commit", Earlier);
        ReleaseRepository.Expect(result, 1);
        Assert.Contains("is not the head of an approved pull request", result.Out, StringComparison.Ordinal);
    }

    [Fact]
    public void PostWritesTheVerdictAsTheGatesAppAndUpdatesItInPlace()
    {
        SessionPullRequest();
        Dictionary<string, string> environment = new(github.Environment()) { ["GATES_TOKEN"] = "gates-token" };

        ReleaseRepository.Expect(sandbox.Canon(environment, "agent-review", "7", "--post"), 0);
        JsonObject run = Assert.Single(github.CheckRuns);
        Assert.Equal("failure", run["conclusion"]?.GetValue<string>());
        Assert.Equal(GatesApp, run["app"]?["id"]?.GetValue<long>());

        github.AddComment(7, "Hafeok", Emil, $"approve {Head}");
        ReleaseRepository.Expect(sandbox.Canon(environment, "agent-review", "7", "--post"), 0);
        run = Assert.Single(github.CheckRuns);
        Assert.Equal("success", run["conclusion"]?.GetValue<string>());
        Assert.Equal("agent review", run["name"]?.GetValue<string>());
        Assert.Equal(Head, run["head_sha"]?.GetValue<string>());
    }

    /// <summary>A run of the same name by another app is left alone; the gates App writes its own.</summary>
    [Fact]
    public void PostDoesNotAdoptAnotherAppsRunOfTheSameName()
    {
        SessionPullRequest();
        github.AddCheckRun(Head, "agent review", Actions, "success");
        github.AddComment(7, "Hafeok", Emil, $"approve {Head}");
        Dictionary<string, string> environment = new(github.Environment()) { ["GATES_TOKEN"] = "gates-token" };

        ReleaseRepository.Expect(sandbox.Canon(environment, "agent-review", "7", "--post"), 0);

        Assert.Equal(2, github.CheckRuns.Count);
        Assert.Contains(github.CheckRuns, r => r["app"]?["id"]?.GetValue<long>() == GatesApp && r["conclusion"]?.GetValue<string>() == "success");
    }

    [Fact]
    public void PostWithoutTheGatesTokenCouldNotRun()
    {
        SessionPullRequest();
        var result = Review("7", "--post");
        ReleaseRepository.Expect(result, 2);
        Assert.Empty(github.CheckRuns);
    }

    [Fact]
    public void GitHubUnreachableCouldNotRunAndIsNeverAPass()
    {
        var result = sandbox.Canon(
            new Dictionary<string, string> { ["CANON_GITHUB_API"] = GitHubServer.Unreachable(), ["GH_TOKEN"] = "t" },
            "agent-review", "7");
        ReleaseRepository.Expect(result, 2);
    }
}

/// <summary>
/// canon land under agent review (DDD-dec-109): main's
/// .github/repo-standard.yaml pins "agent review" to the gates App, and both
/// steps refuse a head without that App's successful check run.
/// </summary>
public sealed class LandUnderAgentReviewTests : IDisposable
{
    private readonly Sandbox sandbox = new();
    private readonly GitHubServer github = new("mindovermachine-dev/test");
    private readonly string head;

    public LandUnderAgentReviewTests()
    {
        sandbox.Write("canon.yaml", "github: mindovermachine-dev/test\n");
        sandbox.Write(".github/repo-standard.yaml", AgentReviewTests.Standard);
        sandbox.Commit("base\n\nRefs #1");
        sandbox.Git("push", "--quiet", "origin", "main");
        sandbox.Git("checkout", "--quiet", "-b", "pr-7");
        sandbox.Write("a.txt", "change\n");
        head = sandbox.Commit("the change\n\nRefs #1");
        sandbox.Git("push", "--quiet", "origin", "HEAD:refs/pull/7/head");
        sandbox.Git("checkout", "--quiet", "main");
    }

    public void Dispose()
    {
        github.Dispose();
        sandbox.Dispose();
    }

    private string? Remote(string reference) => new Git(sandbox.Work).RemoteRef("origin", reference);

    [Fact]
    public void RefusesWhenAgentReviewIsNotGreen()
    {
        var result = sandbox.Canon(github.Environment(), "land", "7");

        ReleaseRepository.Expect(result, 1);
        Assert.Contains("'agent review' is not green", result.Err, StringComparison.Ordinal);
        Assert.Contains("approve " + head, result.Err, StringComparison.Ordinal);
        Assert.Null(Remote("refs/heads/land/pr-7"));
    }

    /// <summary>TAMPER: a successful "agent review" from anything but the gates App does not count.</summary>
    [Fact]
    public void ASuccessFromAnotherAppDoesNotCount()
    {
        github.AddCheckRun(head, "agent review", 15368, "success");
        github.AddCheckRun(head, "agent review", 1236702, "success");

        ReleaseRepository.Expect(sandbox.Canon(github.Environment(), "land", "7"), 1);
        Assert.Null(Remote("refs/heads/land/pr-7"));
    }

    [Fact]
    public void AFailureFromTheGatesAppDoesNotCount()
    {
        github.AddCheckRun(head, "agent review", 5220446, "failure");
        ReleaseRepository.Expect(sandbox.Canon(github.Environment(), "land", "7"), 1);
    }

    [Fact]
    public void LandsBothStepsWhenTheGatesAppPostedSuccess()
    {
        github.AddCheckRun(head, "agent review", 5220446, "success");

        ReleaseRepository.Expect(sandbox.Canon(github.Environment(), "land", "7"), 0);
        Assert.Equal(head, Remote("refs/heads/land/pr-7"));
        ReleaseRepository.Expect(sandbox.Canon(github.Environment(), "land", "7", "--main"), 0);
        Assert.Equal(head, Remote("refs/heads/main"));
    }

    /// <summary>TAMPER: the head cannot unpin the check; the pin is read from main.</summary>
    [Fact]
    public void AHeadThatRemovesThePinIsStillJudgedByMains()
    {
        sandbox.Git("checkout", "--quiet", "pr-7");
        sandbox.Write(".github/repo-standard.yaml", "rulesets: []\n");
        string unpinned = sandbox.Commit("drop the pin\n\nRefs #1");
        sandbox.Git("push", "--quiet", "--force", "origin", "HEAD:refs/pull/7/head");

        var result = sandbox.Canon(github.Environment(), "land", "7");

        ReleaseRepository.Expect(result, 1);
        Assert.Null(Remote("refs/heads/land/pr-7"));
        Assert.NotEqual(head, unpinned);
    }

    [Fact]
    public void GitHubUnreachableRefusesToLand()
    {
        var result = sandbox.Canon(
            new Dictionary<string, string> { ["CANON_GITHUB_API"] = GitHubServer.Unreachable(), ["GH_TOKEN"] = "t" },
            "land", "7");
        ReleaseRepository.Expect(result, 2);
        Assert.Null(Remote("refs/heads/land/pr-7"));
    }
}
