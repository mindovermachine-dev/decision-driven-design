// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

using System;
using System.Collections.Generic;
using Xunit;

namespace Canon.Tests;

public sealed class IssueRefsTests
{
    private static readonly Dictionary<string, string> NoEnvironment = [];

    private static (Sandbox Sandbox, string Base) Repository(string declaration = "")
    {
        Sandbox sandbox = new();
        sandbox.Write("canon.yaml", declaration);
        sandbox.Write("graph/upstream.yaml", "pins:\n  - id: DDD-ground-06\n");
        sandbox.Write("core/decisions/DDD-dec-01.yaml", "id: DDD-dec-01\n");
        return (sandbox, sandbox.Commit("base\n\nRefs #1"));
    }

    [Fact]
    public void EveryCommitNeedsRefsOrClosesAndABareHashIsNotEnough()
    {
        (Sandbox sandbox, string start) = Repository();
        using Sandbox owned = sandbox;
        sandbox.Commit("good\n\nRefs #46");
        sandbox.Commit("also good\n\ncloses #46");
        sandbox.Commit("prose only\n\nAs #46 describes.");

        var result = sandbox.Canon(NoEnvironment, "issue-refs", "--base", start);

        ReleaseRepository.Expect(result, 1);
        Assert.Contains("prose only: no 'Refs #N' or 'Closes #N' line", result.Err, StringComparison.Ordinal);
        Assert.Contains("1 finding(s)", result.Err, StringComparison.Ordinal);
    }

    [Fact]
    public void MergeCommitsAndExemptAuthorsAreNotChecked()
    {
        (Sandbox sandbox, string start) = Repository("issue-refs:\n  exempt-authors: [bot@example.invalid]\n");
        using Sandbox owned = sandbox;
        sandbox.Git("checkout", "--quiet", "-b", "side");
        sandbox.Commit("side work\n\nRefs #2");
        sandbox.Git("checkout", "--quiet", "main");
        sandbox.Commit("main work\n\nRefs #2");
        sandbox.Git("merge", "--quiet", "--no-ff", "side", "-m", "Merge side");
        sandbox.Git("-c", "user.email=bot@example.invalid", "commit", "--quiet", "--allow-empty", "-m", "chore: bump");

        ReleaseRepository.Expect(sandbox.Canon(NoEnvironment, "issue-refs", "--base", start), 0);
    }

    [Fact]
    public void CommitsThatDoNotDescendFromTheStartAreNotChecked()
    {
        (Sandbox sandbox, string start) = Repository();
        using Sandbox owned = sandbox;
        sandbox.Git("checkout", "--quiet", "-b", "old-line");
        sandbox.Commit("old work, before the convention");
        sandbox.Git("checkout", "--quiet", "main");
        string from = sandbox.Commit("the convention starts\n\nRefs #46");
        sandbox.Write("canon.yaml", $"issue-refs:\n  from: {from}\n");
        sandbox.Commit("declare it\n\nRefs #46");
        sandbox.Git("merge", "--quiet", "--no-ff", "old-line", "-m", "Merge the old line\n\nRefs #46");

        ReleaseRepository.Expect(sandbox.Canon(NoEnvironment, "issue-refs", "--base", start), 0);
    }

    [Fact]
    public void BasisIsRequiredOnCanonCommitsOnly()
    {
        (Sandbox sandbox, string start) = Repository();
        using Sandbox owned = sandbox;
        sandbox.Write("README.md", "not canon\n");
        sandbox.Commit("docs\n\nRefs #46");
        sandbox.Write("core/decisions/DDD-dec-02.yaml", "id: DDD-dec-02\n");
        sandbox.Commit("canon without a basis\n\nRefs #46");

        var result = sandbox.Canon(NoEnvironment, "issue-refs", "--base", start, "--basis");

        ReleaseRepository.Expect(result, 1);
        Assert.Contains("canon without a basis: changes core/ and has no Basis: line", result.Err, StringComparison.Ordinal);
        Assert.DoesNotContain("docs:", result.Err, StringComparison.Ordinal);

        // Without --basis, only Refs is checked, and every commit has one.
        ReleaseRepository.Expect(sandbox.Canon(NoEnvironment, "issue-refs", "--base", start), 0);
    }

    [Fact]
    public void BasisPresenceStartsAtItsCommitAndResolutionLater()
    {
        (Sandbox sandbox, string start) = Repository();
        using Sandbox owned = sandbox;
        sandbox.Write("core/decisions/DDD-dec-02.yaml", "id: DDD-dec-02\n");
        sandbox.Commit("canon before the rule\n\nRefs #46");

        sandbox.Write("core/decisions/DDD-dec-03.yaml", "id: DDD-dec-03\n");
        string rule = sandbox.Commit("the rule written\n\nBasis: DDD-dec-99\nRefs #46");

        sandbox.Write("core/decisions/DDD-dec-04.yaml", "id: DDD-dec-04\n");
        string resolve = sandbox.Commit("resolution starts\n\nBasis: DDD-dec-04; DDD-ground-06\nRefs #46");

        sandbox.Write("core/decisions/DDD-dec-05.yaml", "id: DDD-dec-05\n");
        sandbox.Commit("names an id that is nowhere\n\nBasis: DDD-dec-05; DDD-cost-11\nRefs #46");

        sandbox.Write("canon.yaml", $"basis:\n  from: {rule}\n  resolve-from: {resolve}\n");
        sandbox.Commit("declare\n\nRefs #46");

        var result = sandbox.Canon(NoEnvironment, "issue-refs", "--base", start, "--basis");

        ReleaseRepository.Expect(result, 1);
        Assert.Contains("Basis id DDD-cost-11 resolves to no file", result.Err, StringComparison.Ordinal);
        Assert.DoesNotContain("canon before the rule", result.Err, StringComparison.Ordinal);
        Assert.DoesNotContain("DDD-dec-99", result.Err, StringComparison.Ordinal);
        Assert.DoesNotContain("DDD-ground-06", result.Err, StringComparison.Ordinal);
        Assert.Contains("1 finding(s)", result.Err, StringComparison.Ordinal);
    }
}
