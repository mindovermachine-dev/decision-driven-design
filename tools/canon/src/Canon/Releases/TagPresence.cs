// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

using System;
using System.Collections.Generic;
using Canon.GitHub;
using Canon.Infrastructure;

namespace Canon.Releases;

/// <summary>Where a version can already exist (DESIGN.md §4.3, step 2).</summary>
internal enum TagSite
{
    /// <summary>A tag in this clone.</summary>
    Local,

    /// <summary>A tag on the remote, read with ls-remote.</summary>
    Remote,

    /// <summary>A GitHub Release, published or draft, with or without a tag.</summary>
    GitHubRelease,
}

/// <summary>
/// Whether a version is cut, asked of all three places. The v0.5.0 lesson:
/// scripts/ci.py asks only the local clone (scripts/ci.py:57), so a clone that
/// never fetched a tag calls a cut release uncut. Any one site is enough to
/// say "cut".
/// </summary>
internal static class TagPresence
{
    public static IReadOnlyList<(TagSite Site, string Detail)> Find(Git git, string remote, GitHubClient? github, string version)
    {
        List<(TagSite, string)> found = [];
        if (git.LocalTagExists(version))
        {
            found.Add((TagSite.Local, "refs/tags/" + version + " in this clone"));
        }

        string? remoteTag = git.RemoteRef(remote, "refs/tags/" + version);
        if (remoteTag is not null)
        {
            found.Add((TagSite.Remote, $"refs/tags/{version} on {remote} (ls-remote: {remoteTag[..12]})"));
        }

        if (github is not null && github.FindRelease(version) is { } release)
        {
            found.Add((TagSite.GitHubRelease, "a GitHub Release (" + string.Join(", ", GitHubClient.Describe(release)) + ")"));
        }

        return found;
    }

    public static string Name(TagSite site) => site switch
    {
        TagSite.Local => "local",
        TagSite.Remote => "remote",
        TagSite.GitHubRelease => "github-release",
        _ => throw new ArgumentOutOfRangeException(nameof(site)),
    };
}
