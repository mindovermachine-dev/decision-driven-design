// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

using System;
using System.Collections.Generic;
using Xunit;

namespace Canon.Tests;

public sealed class ChangelogAndRatifyTests
{
    private static readonly Dictionary<string, string> Offline = new() { ["CANON_GITHUB_API"] = GitHubServer.Unreachable() };

    [Fact]
    public void TheProjectionIsCheckedAndAHandEditAboveTheTailIsRefused()
    {
        using ReleaseRepository repo = new();
        ReleaseRepository.Expect(repo.Sandbox.Canon(repo.GitHub.Environment(), "changelog", "--check"), 0);

        string changelog = repo.Sandbox.Read("CHANGELOG.md");
        Assert.StartsWith("# Changelog\n", changelog, StringComparison.Ordinal);
        Assert.Contains("## v0.5.0 — Ready to try: the method as a preview\n\n2026-11-02 · pre-release · descriptor [`releases/v0.5.0.yaml`](releases/v0.5.0.yaml)\n\nThe first release whose version is the method's.\n\n", changelog, StringComparison.Ordinal);
        Assert.EndsWith(ReleaseRepository.Tail, changelog, StringComparison.Ordinal);

        repo.Sandbox.Write("CHANGELOG.md", changelog.Replace("The first release", "Proposed, not cut. The first release", StringComparison.Ordinal));
        var stale = repo.Sandbox.Canon(repo.GitHub.Environment(), "changelog", "--check");
        ReleaseRepository.Expect(stale, 1);
        Assert.Contains("is not the projection", stale.Err, StringComparison.Ordinal);

        ReleaseRepository.Expect(repo.Sandbox.Canon(repo.GitHub.Environment(), "changelog"), 0);
        Assert.Equal(changelog, repo.Sandbox.Read("CHANGELOG.md"));
    }

    [Fact]
    public void AnEditToTheFrozenTailIsRefusedAndNeverRewritten()
    {
        using ReleaseRepository repo = new();
        string changelog = repo.Sandbox.Read("CHANGELOG.md");
        string edited = changelog.Replace("kept unedited", "edited after all", StringComparison.Ordinal);
        repo.Sandbox.Write("CHANGELOG.md", edited);

        var result = repo.Sandbox.Canon(repo.GitHub.Environment(), "changelog");

        ReleaseRepository.Expect(result, 1);
        Assert.Contains("the frozen tail of CHANGELOG.md was edited", result.Err, StringComparison.Ordinal);
        Assert.Equal(edited, repo.Sandbox.Read("CHANGELOG.md"));
    }

    [Fact]
    public void NewestVersionComesFirstByPrecedenceNotByName()
    {
        using ReleaseRepository repo = new();
        foreach (string version in new[] { "v0.10.0", "v0.6.0" })
        {
            repo.Sandbox.Write($"releases/{version}.yaml", $"""
                format: 2
                version: {version}
                date: 2026-12-01
                basis: [DDD-tool-01]
                title: Release {version}
                summary: Notes for {version}.
                """);
        }

        ReleaseRepository.Expect(repo.Sandbox.Canon(repo.GitHub.Environment(), "changelog"), 0);
        string changelog = repo.Sandbox.Read("CHANGELOG.md");
        int ten = changelog.IndexOf("## v0.10.0", StringComparison.Ordinal);
        int six = changelog.IndexOf("## v0.6.0", StringComparison.Ordinal);
        int five = changelog.IndexOf("## v0.5.0", StringComparison.Ordinal);
        Assert.True(ten >= 0 && ten < six && six < five, changelog);
    }

    [Fact]
    public void TheTailHashIsPrintedForTheDeclaration()
    {
        using ReleaseRepository repo = new();
        var result = repo.Sandbox.Canon(repo.GitHub.Environment(), "changelog", "--tail-sha256");
        ReleaseRepository.Expect(result, 0);
        Assert.Equal(ReleaseRepository.Sha256(ReleaseRepository.Tail), result.Out.Trim());
    }

    [Fact]
    public void RatifyFillsTheHeadThatCarriesTheDescriptorAndKeepsEveryOtherByte()
    {
        using ReleaseRepository repo = new();
        string descriptor = repo.Sandbox.Read("releases/v0.5.0.yaml");

        Assert.Contains("version: v0.5.0\nratified_head: " + repo.RatifiedHead + "\n# The ratified head is filled by canon ratify; this comment must survive it.\n", descriptor, StringComparison.Ordinal);
        string before = Sandbox.Run(repo.Sandbox.Work, "show", repo.RatifiedHead + ":releases/v0.5.0.yaml");
        Assert.Equal(before, descriptor.Replace("ratified_head: " + repo.RatifiedHead + "\n", "", StringComparison.Ordinal).TrimEnd('\n'));
        Assert.Equal(["releases/v0.5.0.yaml"], repo.Sandbox.Git("diff", "--name-only", repo.RatifiedHead, repo.Head).Split('\n'));
    }

    [Fact]
    public void RatifyIsANoOpForTheSameHeadAndRefusesADifferentOne()
    {
        using ReleaseRepository repo = new();
        var same = repo.Sandbox.Canon(repo.GitHub.Environment(), "ratify", "v0.5.0", "--head", repo.RatifiedHead);
        ReleaseRepository.Expect(same, 0);
        Assert.Contains("nothing to do", same.Out, StringComparison.Ordinal);

        var different = repo.Sandbox.Canon(repo.GitHub.Environment(), "ratify", "v0.5.0", "--head", repo.Head);
        ReleaseRepository.Expect(different, 1);
        Assert.Contains("already names ratified_head", different.Err, StringComparison.Ordinal);
    }

    [Fact]
    public void RatifyRefusesACutVersionFoundOnlyOnTheRemote()
    {
        using ReleaseRepository repo = new();
        string elsewhere = repo.Sandbox.Clone("emils-clone");
        Sandbox.Run(elsewhere, "tag", "v0.5.0", repo.Head);
        Sandbox.Run(elsewhere, "push", "--quiet", "origin", "refs/tags/v0.5.0");
        string before = repo.Sandbox.Read("releases/v0.5.0.yaml");

        var result = repo.Sandbox.Canon(repo.GitHub.Environment(), "ratify", "v0.5.0", "--head", repo.Head);

        ReleaseRepository.Expect(result, 1);
        Assert.Contains("v0.5.0 is cut, so its descriptor is immutable", result.Err, StringComparison.Ordinal);
        Assert.Equal(before, repo.Sandbox.Read("releases/v0.5.0.yaml"));
    }

    [Fact]
    public void RatifyCannotRunWhenGitHubCannotBeAsked()
    {
        using ReleaseRepository repo = new();
        string before = repo.Sandbox.Read("releases/v0.5.0.yaml");

        var result = repo.Sandbox.Canon(Offline, "ratify", "v0.5.0", "--head", repo.Head);

        ReleaseRepository.Expect(result, 2);
        Assert.Contains("GitHub could not be reached", result.Err, StringComparison.Ordinal);
        Assert.Equal(before, repo.Sandbox.Read("releases/v0.5.0.yaml"));
    }

    [Fact]
    public void RatifyRefusesAHeadThatDoesNotCarryTheDescriptor()
    {
        using GitHubServer github = new("test/none");
        using Sandbox sandbox = new();
        sandbox.Write("canon.yaml", "github: test/none\n");
        sandbox.Write("README.md", "canon\n");
        string before = sandbox.Commit("before the descriptor");
        sandbox.Write("releases/v0.6.0.yaml", "format: 2\nversion: v0.6.0\ntitle: T\nbasis: [DDD-x-01]\nsummary: S\n");
        sandbox.Commit("descriptor");

        var result = sandbox.Canon(github.Environment(), "ratify", "v0.6.0", "--head", before);

        ReleaseRepository.Expect(result, 1);
        Assert.Contains("does not carry releases/v0.6.0.yaml", result.Err, StringComparison.Ordinal);
    }
}
