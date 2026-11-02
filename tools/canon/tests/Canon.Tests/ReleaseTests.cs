// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

using Canon.Infrastructure;
using Xunit;

namespace Canon.Tests;

/// <summary>
/// canon release. The first four tests recreate the v0.5.0 case: the version
/// already exists in one place, and canon must find it there, whichever
/// place it is (DESIGN.md §4.3, step 2; prediction P-9).
/// </summary>
public sealed class ReleaseTests
{
    [Fact]
    public void RefusesWhenTheTagExistsOnlyInThisClone()
    {
        using ReleaseRepository repo = new();
        repo.Sandbox.Git("tag", "v0.5.0", repo.Head);

        var result = repo.Sandbox.Canon(repo.GitHub.Environment(), "release", "v0.5.0", "--plan");

        ReleaseRepository.Expect(result, 1);
        Assert.Contains("refused at step 2", result.Err, System.StringComparison.Ordinal);
        Assert.Contains("[local]", result.Err, System.StringComparison.Ordinal);
        Assert.DoesNotContain("[remote]", result.Err, System.StringComparison.Ordinal);
    }

    /// <summary>
    /// The v0.5.0 lesson itself. The tag was cut elsewhere and pushed; this
    /// clone never fetched it, so a check of local tags (scripts/ci.py:57)
    /// says "not cut". ls-remote says otherwise.
    /// </summary>
    [Fact]
    public void RefusesWhenTheTagExistsOnlyOnTheRemoteInACloneThatNeverFetchedIt()
    {
        using ReleaseRepository repo = new();
        string elsewhere = repo.Sandbox.Clone("emils-clone");
        Sandbox.Run(elsewhere, "tag", "v0.5.0", repo.Head);
        Sandbox.Run(elsewhere, "push", "--quiet", "origin", "refs/tags/v0.5.0");

        Assert.False(new Git(repo.Sandbox.Work).LocalTagExists("v0.5.0"));

        var result = repo.Sandbox.Canon(repo.GitHub.Environment(), "release", "v0.5.0", "--plan");

        ReleaseRepository.Expect(result, 1);
        Assert.Contains("refused at step 2", result.Err, System.StringComparison.Ordinal);
        Assert.Contains("[remote] refs/tags/v0.5.0 on origin (ls-remote:", result.Err, System.StringComparison.Ordinal);
        Assert.DoesNotContain("[local]", result.Err, System.StringComparison.Ordinal);
    }

    [Fact]
    public void RefusesWhenOnlyADraftGitHubReleaseExists()
    {
        using ReleaseRepository repo = new();
        repo.GitHub.AddRelease("v0.5.0", draft: true);

        var result = repo.Sandbox.Canon(repo.GitHub.Environment(), "release", "v0.5.0", "--plan");

        ReleaseRepository.Expect(result, 1);
        Assert.Contains("[github-release] a GitHub Release (tag v0.5.0, draft)", result.Err, System.StringComparison.Ordinal);
        Assert.False(new Git(repo.Sandbox.Work).LocalTagExists("v0.5.0"));
        Assert.Null(new Git(repo.Sandbox.Work).RemoteRef("origin", "refs/tags/v0.5.0"));
    }

    [Fact]
    public void NamesEverySiteWhenTheVersionExistsInAllThree()
    {
        using ReleaseRepository repo = new();
        repo.Sandbox.Git("tag", "v0.5.0", repo.Head);
        repo.Sandbox.Git("push", "--quiet", "origin", "refs/tags/v0.5.0");
        repo.GitHub.AddRelease("v0.5.0", draft: false);

        var result = repo.Sandbox.Canon(repo.GitHub.Environment(), "release", "v0.5.0", "--plan");

        ReleaseRepository.Expect(result, 1);
        Assert.Contains("[local]", result.Err, System.StringComparison.Ordinal);
        Assert.Contains("[remote]", result.Err, System.StringComparison.Ordinal);
        Assert.Contains("[github-release]", result.Err, System.StringComparison.Ordinal);
    }

    [Fact]
    public void CutsASignedTagPushesItAndCreatesTheRelease()
    {
        using ReleaseRepository repo = new();
        string key = repo.Sandbox.UseSigningKey();

        var result = repo.Sandbox.Canon(repo.GitHub.Environment(), "release", "v0.5.0");

        ReleaseRepository.Expect(result, 0);
        string tag = repo.Sandbox.Git("cat-file", "tag", "v0.5.0");
        Assert.Contains("-----BEGIN SSH SIGNATURE-----", tag, System.StringComparison.Ordinal);

        // Signed with the test's own key, not any key of the machine's: the
        // signature verifies against that key alone.
        string signers = System.IO.Path.Combine(repo.Sandbox.Directory, "allowed_signers");
        System.IO.File.WriteAllText(signers, "canon-test@example.invalid " + System.IO.File.ReadAllText(key + ".pub"));
        repo.Sandbox.Git("config", "gpg.ssh.allowedSignersFile", signers);
        Assert.True(Sandbox.Try(repo.Sandbox.Work, "tag", "-v", "v0.5.0"), "the tag does not verify against the test's own key");
        Assert.Contains("v0.5.0 — Ready to try: the method as a preview", tag, System.StringComparison.Ordinal);
        Assert.Equal(repo.Head, repo.Sandbox.Git("rev-parse", "v0.5.0^{commit}"));
        Assert.Equal(repo.Sandbox.Git("rev-parse", "v0.5.0"), new Git(repo.Sandbox.Work).RemoteRef("origin", "refs/tags/v0.5.0"));

        var created = Assert.Single(repo.GitHub.Releases);
        Assert.Equal("v0.5.0", created["tag_name"]!.GetValue<string>());
        Assert.Equal("v0.5.0 — Ready to try: the method as a preview", created["name"]!.GetValue<string>());
        Assert.True(created["prerelease"]!.GetValue<bool>());
        Assert.Equal("The first release whose version is the method's.", created["body"]!.GetValue<string>());
        Assert.All(repo.GitHub.Requests, r => Assert.Equal("Bearer test-token", r.Authorization));

        // Cut once; a second run refuses at step 2 on all three sites.
        var again = repo.Sandbox.Canon(repo.GitHub.Environment(), "release", "v0.5.0");
        ReleaseRepository.Expect(again, 1);
        Assert.Contains("[local]", again.Err, System.StringComparison.Ordinal);
        Assert.Contains("[remote]", again.Err, System.StringComparison.Ordinal);
        Assert.Contains("[github-release]", again.Err, System.StringComparison.Ordinal);
    }

    [Fact]
    public void PlanChecksEverythingAndChangesNothing()
    {
        using ReleaseRepository repo = new();
        repo.Sandbox.UseSigningKey();

        var result = repo.Sandbox.Canon(repo.GitHub.Environment(), "release", "v0.5.0", "--plan");

        ReleaseRepository.Expect(result, 0);
        Assert.Contains("6. CHANGELOG.md is the projection", result.Out, System.StringComparison.Ordinal);
        Assert.False(new Git(repo.Sandbox.Work).LocalTagExists("v0.5.0"));
        Assert.Null(new Git(repo.Sandbox.Work).RemoteRef("origin", "refs/tags/v0.5.0"));
        Assert.Empty(repo.GitHub.Releases);
        Assert.DoesNotContain(repo.GitHub.Requests, r => r.Method == "POST");
    }

    [Fact]
    public void CannotRunWhenGitHubCannotBeAskedAndLeavesNoTag()
    {
        using ReleaseRepository repo = new();
        repo.Sandbox.UseSigningKey();
        var environment = new System.Collections.Generic.Dictionary<string, string>
        {
            ["CANON_GITHUB_API"] = GitHubServer.Unreachable(),
            ["GH_TOKEN"] = "test-token",
        };

        var result = repo.Sandbox.Canon(environment, "release", "v0.5.0");

        ReleaseRepository.Expect(result, 2);
        Assert.Contains("GitHub could not be reached", result.Err, System.StringComparison.Ordinal);
        Assert.False(new Git(repo.Sandbox.Work).LocalTagExists("v0.5.0"));
    }

    [Fact]
    public void TheGuardRefusesACanonChangeLandedAfterTheRatifiedHead()
    {
        using ReleaseRepository repo = new();
        repo.Sandbox.UseSigningKey();
        repo.Sandbox.Write("core/claims/DDD-tool-02.yaml", "id: DDD-tool-02\n");
        repo.Sandbox.Commit("an unratified canon change after the descriptor");
        repo.Sandbox.Git("push", "--quiet", "origin", "main");

        var result = repo.Sandbox.Canon(repo.GitHub.Environment(), "release", "v0.5.0");

        ReleaseRepository.Expect(result, 1);
        Assert.Contains("refused at step 4", result.Err, System.StringComparison.Ordinal);
        Assert.Contains("core/claims/DDD-tool-02.yaml", result.Err, System.StringComparison.Ordinal);
        Assert.False(new Git(repo.Sandbox.Work).LocalTagExists("v0.5.0"));
    }

    [Fact]
    public void RefusesWhenTheGatesFailAtTheCommitUnderRelease()
    {
        using ReleaseRepository repo = new(gates: ["git", "this-is-not-a-git-command"]);
        repo.Sandbox.UseSigningKey();

        var result = repo.Sandbox.Canon(repo.GitHub.Environment(), "release", "v0.5.0");

        ReleaseRepository.Expect(result, 1);
        Assert.Contains("refused at step 5", result.Err, System.StringComparison.Ordinal);
        Assert.False(new Git(repo.Sandbox.Work).LocalTagExists("v0.5.0"));
        Assert.DoesNotContain(repo.Sandbox.Git("worktree", "list", "--porcelain").Split('\n'), l => l.Contains("canon-release-", System.StringComparison.Ordinal));
    }

    [Fact]
    public void NeverCutsAnUnsignedTag()
    {
        using ReleaseRepository repo = new();

        var result = repo.Sandbox.Canon(repo.GitHub.Environment(), "release", "v0.5.0");

        ReleaseRepository.Expect(result, 1);
        Assert.Contains("refused at step 7", result.Err, System.StringComparison.Ordinal);
        Assert.Contains("never creates an unsigned tag", result.Err, System.StringComparison.Ordinal);
        Assert.False(new Git(repo.Sandbox.Work).LocalTagExists("v0.5.0"));
    }

    [Fact]
    public void RefusesADescriptorThatHasNotLanded()
    {
        using ReleaseRepository repo = new();
        repo.Sandbox.UseSigningKey();

        var result = repo.Sandbox.Canon(repo.GitHub.Environment(), "release", "v0.6.0", "--plan");

        ReleaseRepository.Expect(result, 1);
        Assert.Contains("refused at step 1", result.Err, System.StringComparison.Ordinal);
        Assert.Contains("is not on origin/main", result.Err, System.StringComparison.Ordinal);
    }

    [Fact]
    public void RefusesWhenTheChangelogIsNotTheProjectionAtTheCommitUnderRelease()
    {
        using ReleaseRepository repo = new();
        repo.Sandbox.UseSigningKey();
        string changelog = repo.Sandbox.Read("CHANGELOG.md");
        repo.Sandbox.Write("CHANGELOG.md", changelog.Replace("The first release", "A hand edit to the first release", System.StringComparison.Ordinal));
        repo.Sandbox.Commit("a hand edit to the changelog");
        repo.Sandbox.Git("push", "--quiet", "origin", "main");

        var result = repo.Sandbox.Canon(repo.GitHub.Environment(), "release", "v0.5.0", "--plan");

        // The guard sees CHANGELOG.md changed after the ratified head before step 6 runs.
        ReleaseRepository.Expect(result, 1);
        Assert.Contains("refused at step 4", result.Err, System.StringComparison.Ordinal);
        Assert.Contains("CHANGELOG.md", result.Err, System.StringComparison.Ordinal);
    }
}
