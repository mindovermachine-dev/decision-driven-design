// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

using System;
using System.Collections.Generic;
using System.Security.Cryptography;
using System.Text;
using Xunit;

namespace Canon.Tests;

/// <summary>
/// A repository laid out the way this one is at v0.5.0: canon.yaml, a
/// changelog with a frozen 4.x tail, canon under core/, and a format 2
/// descriptor for v0.5.0 whose ratified head is the commit that carries it
/// and its changelog section. It is built with canon's own commands (the
/// changelog written by canon changelog, the head filled by canon ratify),
/// then pushed, so origin's main holds a landed, ratified descriptor.
/// </summary>
internal sealed class ReleaseRepository : IDisposable
{
    public const string Repository = "test/canon-fixture";
    public const string Version = "v0.5.0";
    public const string Tail = "## 4.7 — The volume layer (boundary charter)\n\nHistory under the earlier numbering, kept unedited.\n";

    public ReleaseRepository(IReadOnlyList<string>? gates = null)
    {
        Sandbox = new Sandbox();
        GitHub = new GitHubServer(Repository);

        string gateList = string.Join(", ", gates ?? ["git", "--version"]);
        Sandbox.Write("canon.yaml", $"""
            github: {Repository}
            gates: [{gateList}]
            changelog:
              tail-from: "## 4.7 — The volume layer (boundary charter)"
              tail-sha256: {Sha256(Tail)}
            """);
        Sandbox.Write("CHANGELOG.md", "# Changelog\n\n" + Tail);
        Sandbox.Write("core/claims/DDD-tool-01.yaml", "id: DDD-tool-01\n");
        Sandbox.Commit("canon before the release");

        Sandbox.Write("releases/v0.5.0.yaml", """
            format: 2
            version: v0.5.0
            # The ratified head is filled by canon ratify; this comment must survive it.
            date: 2026-11-02
            prerelease: true
            basis:
              - DDD-tool-01
            title: 'Ready to try: the method as a preview'
            summary: |
              The first release whose version is the method's.
            """);
        Expect(Sandbox.Canon(GitHub.Environment(), "changelog"), 0);
        RatifiedHead = Sandbox.Commit("v0.5.0 proposed: descriptor and its changelog section");

        Expect(Sandbox.Canon(GitHub.Environment(), "ratify", Version), 0);
        Head = Sandbox.Commit("releases/v0.5.0.yaml: ratified_head filled");
        Sandbox.Git("push", "--quiet", "origin", "main");
    }

    public Sandbox Sandbox { get; }

    public GitHubServer GitHub { get; }

    /// <summary>The commit the principal ratified: the descriptor and its changelog section.</summary>
    public string RatifiedHead { get; }

    /// <summary>origin/main: the ratified head plus the ratified_head line.</summary>
    public string Head { get; }

    public static string Sha256(string text) =>
        Convert.ToHexStringLower(SHA256.HashData(Encoding.UTF8.GetBytes(text)));

    public static void Expect((int Exit, string Out, string Err) result, int exit) =>
        Assert.True(result.Exit == exit, $"expected exit {exit}, got {result.Exit}\nout:\n{result.Out}\nerr:\n{result.Err}");

    public void Dispose()
    {
        GitHub.Dispose();
        Sandbox.Dispose();
    }
}
