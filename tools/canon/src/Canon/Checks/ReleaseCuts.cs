// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using Canon.Graph;
using Canon.Infrastructure;
using Canon.Releases;

namespace Canon.Checks;

/// <summary>
/// The releases gate's git half, as scripts/ci.py's release_cuts does it
/// (main at e8fde2a): whether each version is cut is decided from origin
/// (git ls-remote --tags origin, peeling annotated tags), and from local tags
/// only when origin cannot be reached, which the note says. A cut
/// descriptor must be byte-identical at HEAD to its blob at the tag; an uncut
/// one must satisfy the release-head guard at HEAD (DDD-dec-84).
/// </summary>
internal static class ReleaseCuts
{
    public static (List<Finding> Findings, List<string> Notes) Check(Git git, string remote, IReadOnlyList<string> descriptors)
    {
        List<Finding> findings = [];
        List<string> notes = [];
        Dictionary<string, string> cut = Cut(git, remote, descriptors.Select(d => Path.GetFileNameWithoutExtension(d)).ToList(), notes);

        foreach (string path in descriptors)
        {
            string version = Path.GetFileNameWithoutExtension(path);
            if (cut.TryGetValue(version, out string? commit))
            {
                ProcessResult at = git.Try("show", $"{commit}:{path}");
                ProcessResult head = git.Try("show", $"HEAD:{path}");
                if (at.Exit != 0)
                {
                    findings.Add(new Finding(path, "REL-CUT-MISSING", false, $"{version} is cut at {commit[..7]}, but that commit or its {path} is not in this clone; run git fetch --force --tags {remote}"));
                }
                else if (head.Output != at.Output)
                {
                    findings.Add(new Finding(path, "REL-CUT-EDITED", false, $"{path} at HEAD differs from the file at the tag ({commit[..7]}): the descriptor changed after it was cut. A cut release's descriptor is immutable"));
                }
                else
                {
                    notes.Add($"{version}: cut at {commit[..7]}; {path} at HEAD equals the file at the tag; immutable, not re-guarded");
                }

                continue;
            }

            string? text = git.Show("HEAD", path);
            Descriptor? descriptor = text is null ? null : Descriptor.Parse(path, text);
            if (descriptor?.RatifiedHead is not { } ratified)
            {
                findings.Add(new Finding(path, "REL-GUARD", false, $"{version} is not cut and has no ratified_head at HEAD, so the release-head guard cannot pass"));
                continue;
            }

            foreach (string miss in ReleaseHeadGuard.Check(git, ratified, "HEAD", path))
            {
                findings.Add(new Finding(path, "REL-GUARD", false, miss));
            }

            notes.Add($"{version}: not cut; the release-head guard ran at HEAD");
        }

        return (findings, notes);
    }

    private static Dictionary<string, string> Cut(Git git, string remote, List<string> versions, List<string> notes)
    {
        ProcessResult listing = git.Try("ls-remote", "--tags", remote);
        if (listing.Exit == 0)
        {
            Dictionary<string, string> refs = new(StringComparer.Ordinal);
            foreach (string line in listing.Output.Split('\n', StringSplitOptions.RemoveEmptyEntries))
            {
                string[] parts = line.Split('\t');
                if (parts.Length != 2)
                {
                    continue;
                }

                string name = parts[1].Trim()["refs/tags/".Length..];
                if (name.EndsWith("^{}", StringComparison.Ordinal))
                {
                    refs[name[..^3]] = parts[0];
                }
                else
                {
                    refs.TryAdd(name, parts[0]);
                }
            }

            notes.Add($"cut decided from {remote} (git ls-remote --tags {remote})");
            return versions.Where(refs.ContainsKey).ToDictionary(v => v, v => refs[v], StringComparer.Ordinal);
        }

        string why = listing.Error.Trim().Split('\n').FirstOrDefault() is { Length: > 0 } first ? first : "no origin";
        notes.Add($"offline: {remote} not reachable ({why}); cut decided from LOCAL tags, which may be missing or stale");
        Dictionary<string, string> local = new(StringComparer.Ordinal);
        foreach (string version in versions)
        {
            if (git.Resolve($"refs/tags/{version}") is { } commit)
            {
                local[version] = commit;
            }
        }

        return local;
    }
}
