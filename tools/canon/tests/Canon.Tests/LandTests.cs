// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

using System;
using System.Collections.Generic;
using Canon.Infrastructure;
using Xunit;

namespace Canon.Tests;

/// <summary>
/// canon land, Varve's land.cs semantics, against a real bare remote that
/// carries refs/pull/N/head as GitHub's does.
/// </summary>
public sealed class LandTests
{
    private static readonly Dictionary<string, string> NoEnvironment = [];

    private static (Sandbox Sandbox, string Main) Repository()
    {
        Sandbox sandbox = new();
        sandbox.Write("README.md", "canon\n");
        string main = sandbox.Commit("base\n\nRefs #1");
        sandbox.Git("push", "--quiet", "origin", "main");
        return (sandbox, main);
    }

    private static string PullRequest(Sandbox sandbox, int number, string file)
    {
        sandbox.Git("checkout", "--quiet", "-b", "pr-" + number);
        sandbox.Write(file, "change\n");
        string head = sandbox.Commit("the change\n\nRefs #1");
        sandbox.Git("push", "--quiet", "origin", $"HEAD:refs/pull/{number}/head");
        sandbox.Git("checkout", "--quiet", "main");
        return head;
    }

    [Fact]
    public void LandsAPullRequestByFastForwardInTwoSteps()
    {
        (Sandbox sandbox, _) = Repository();
        using Sandbox owned = sandbox;
        string head = PullRequest(sandbox, 7, "a.txt");
        Git git = new(sandbox.Work);

        var push = sandbox.Canon(NoEnvironment, "land", "7");
        ReleaseRepository.Expect(push, 0);
        Assert.Equal(head, git.RemoteRef("origin", "refs/heads/land/pr-7"));
        Assert.Contains("canon land 7 --main", push.Out, StringComparison.Ordinal);

        var main = sandbox.Canon(NoEnvironment, "land", "7", "--main");
        ReleaseRepository.Expect(main, 0);
        Assert.Equal(head, git.RemoteRef("origin", "refs/heads/main"));
        Assert.Null(git.RemoteRef("origin", "refs/heads/land/pr-7"));
        Assert.Equal("", Sandbox.Run(sandbox.Remote, "rev-list", "--merges", "main"));
    }

    [Fact]
    public void MainRefusesToMoveWithoutTheCheckedLandBranch()
    {
        (Sandbox sandbox, string main) = Repository();
        using Sandbox owned = sandbox;
        PullRequest(sandbox, 8, "b.txt");

        var result = sandbox.Canon(NoEnvironment, "land", "8", "--main");

        ReleaseRepository.Expect(result, 1);
        Assert.Contains("there is no land/pr-8", result.Err, StringComparison.Ordinal);
        Assert.Equal(main, new Git(sandbox.Work).RemoteRef("origin", "refs/heads/main"));
    }

    [Fact]
    public void MainRefusesWhenTheHeadMovedAfterItWasChecked()
    {
        (Sandbox sandbox, string main) = Repository();
        using Sandbox owned = sandbox;
        PullRequest(sandbox, 9, "c.txt");
        ReleaseRepository.Expect(sandbox.Canon(NoEnvironment, "land", "9"), 0);

        sandbox.Git("checkout", "--quiet", "pr-9");
        sandbox.Write("c.txt", "changed again\n");
        sandbox.Commit("a later push\n\nRefs #1");
        sandbox.Git("push", "--quiet", "--force", "origin", "HEAD:refs/pull/9/head");

        var result = sandbox.Canon(NoEnvironment, "land", "9", "--main");

        ReleaseRepository.Expect(result, 1);
        Assert.Contains("the head moved since it was pushed", result.Err, StringComparison.Ordinal);
        Assert.Equal(main, new Git(sandbox.Work).RemoteRef("origin", "refs/heads/main"));
    }

    [Fact]
    public void RefusesAHeadThatMainIsNotAnAncestorOf()
    {
        (Sandbox sandbox, _) = Repository();
        using Sandbox owned = sandbox;
        PullRequest(sandbox, 10, "d.txt");
        sandbox.Write("e.txt", "main moved\n");
        sandbox.Commit("main moved on\n\nRefs #1");
        sandbox.Git("push", "--quiet", "origin", "main");

        var result = sandbox.Canon(NoEnvironment, "land", "10");

        ReleaseRepository.Expect(result, 1);
        Assert.Contains("cannot be fast-forwarded", result.Err, StringComparison.Ordinal);
        Assert.Null(new Git(sandbox.Work).RemoteRef("origin", "refs/heads/land/pr-10"));
    }

    [Fact]
    public void AHeadThatAddsADescriptorLandsAsARelease()
    {
        (Sandbox sandbox, _) = Repository();
        using Sandbox owned = sandbox;
        string head = PullRequest(sandbox, 11, "releases/v0.6.0.yaml");

        var result = sandbox.Canon(NoEnvironment, "land", "11");

        ReleaseRepository.Expect(result, 0);
        Assert.Equal(head, new Git(sandbox.Work).RemoteRef("origin", "refs/heads/land/release-v0.6.0"));
    }

    [Fact]
    public void PrintRunsNothing()
    {
        (Sandbox sandbox, _) = Repository();
        using Sandbox owned = sandbox;
        PullRequest(sandbox, 12, "f.txt");

        var result = sandbox.Canon(NoEnvironment, "land", "12", "--print");

        ReleaseRepository.Expect(result, 0);
        Assert.Contains("$ git push origin", result.Out, StringComparison.Ordinal);
        Assert.Null(new Git(sandbox.Work).RemoteRef("origin", "refs/heads/land/pr-12"));
    }
}
