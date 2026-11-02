// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

using System.Collections.Generic;
using System.Linq;
using Canon.Infrastructure;

namespace Canon.Releases;

/// <summary>
/// spec/release-format.md rule 7, ported from scripts/check-release-head.py:
/// at the commit under release, ratified_head is an ancestor, and nothing but
/// the descriptor changed between them. With a merge commit whose second
/// parent carries the ratified head, that parent is compared, as the Python
/// guard does.
/// Git ancestry is not a graph fact, so this stays code (DESIGN.md §5.3).
/// </summary>
internal static class ReleaseHeadGuard
{
    public static IReadOnlyList<string> Check(Git git, string ratifiedHead, string underRelease, string descriptorPath)
    {
        string? ratified = git.Resolve(ratifiedHead);
        if (ratified is null)
        {
            return [$"ratified_head {ratifiedHead} does not name a commit in this repository"];
        }

        string? head = git.Resolve(underRelease);
        if (head is null)
        {
            return [$"{underRelease} does not name a commit"];
        }

        // Check 2: the ratified canon is in the release.
        if (!git.IsAncestor(ratified, head))
        {
            return [$"ratified_head {ratified[..12]} is not an ancestor of {head[..12]}: the release would be cut from before the ratified head"];
        }

        // Check 3, against T = A^2 when A is a merge whose merged side carries
        // the ratified head, else A itself (check-release-head.py, lines 82-85).
        string merged = head;
        string[] split = git.Run("rev-list", "--parents", "-n", "1", head).Split(' ');
        if (split.Length > 2 && git.IsAncestor(ratified, split[2]))
        {
            merged = split[2];
        }

        List<string> extra = git.ChangedPaths(ratified, merged).Where(p => p != descriptorPath).ToList();
        return extra.Count == 0
            ? []
            : [$"between ratified_head {ratified[..12]} and the merged head {merged[..12]}, more than the descriptor changed: {string.Join(", ", extra.Take(10))}{(extra.Count > 10 ? $" and {extra.Count - 10} more" : "")}"];
    }
}
