// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

using System;
using System.Collections.Generic;
using System.Linq;

namespace Canon.Infrastructure;

/// <summary>git, as a process, in one working tree.</summary>
internal sealed class Git(string root, IReadOnlyDictionary<string, string>? environment = null)
{
    public string Root { get; } = root;

    public ProcessResult Try(params string[] arguments) =>
        Processes.Run("git", Root, arguments, environment);

    /// <summary>Runs git and returns its trimmed output, or throws: for calls that must succeed.</summary>
    public string Run(params string[] arguments)
    {
        ProcessResult result = Try(arguments);
        if (result.Exit == Processes.NotFound)
        {
            throw new CanonException("git is not installed");
        }

        return result.Exit == 0
            ? result.Output.Trim()
            : throw new CanonException($"git {string.Join(' ', arguments)} failed: {result.Error.Trim()}");
    }

    /// <summary>The full sha a revision names, or null when it names nothing.</summary>
    public string? Resolve(string revision)
    {
        ProcessResult result = Try("rev-parse", "--verify", "--quiet", revision + "^{commit}");
        return result.Exit == 0 ? result.Output.Trim() : null;
    }

    public bool IsAncestor(string ancestor, string descendant) =>
        Try("merge-base", "--is-ancestor", ancestor, descendant).Exit == 0;

    public bool LocalTagExists(string tag) =>
        Try("rev-parse", "--verify", "--quiet", "refs/tags/" + tag).Exit == 0;

    /// <summary>
    /// What a ref is on a remote, read with ls-remote: no fetch, so it sees a
    /// ref this clone never fetched. Null when the remote has no such ref.
    /// </summary>
    public string? RemoteRef(string remote, string reference)
    {
        ProcessResult result = Try("ls-remote", remote, reference);
        if (result.Exit != 0)
        {
            throw new CanonException($"git ls-remote {remote} {reference} failed: {result.Error.Trim()}");
        }

        string line = result.Output.Split('\n', StringSplitOptions.RemoveEmptyEntries)
            .FirstOrDefault(l => l.EndsWith("\t" + reference, StringComparison.Ordinal)) ?? "";
        return line.Length == 0 ? null : line.Split('\t')[0];
    }

    /// <summary>The paths that differ between two commits.</summary>
    public IReadOnlyList<string> ChangedPaths(string from, string to) =>
        Run("diff", "--name-only", "--no-renames", from, to)
            .Split('\n', StringSplitOptions.RemoveEmptyEntries);

    /// <summary>A file's content at a commit, or null when it does not exist there.</summary>
    public string? Show(string commit, string path)
    {
        ProcessResult result = Try("show", commit + ":" + path);
        return result.Exit == 0 ? result.Output : null;
    }

    public string? Config(string key)
    {
        ProcessResult result = Try("config", "--get", key);
        string value = result.Output.Trim();
        return result.Exit == 0 && value.Length > 0 ? value : null;
    }
}
