// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;
using Canon.GitHub;
using Canon.Infrastructure;
using Canon.Releases;

namespace Canon.Commands;

/// <summary>
/// canon ratify &lt;version&gt; [--head &lt;sha&gt;]: fills ratified_head
/// (DESIGN.md §4.4).
///
/// The head defaults to HEAD: the commit the principal ratifies, which must
/// already carry the descriptor and its CHANGELOG.md section. Under
/// DDD-dec-104 adding a descriptor also changes CHANGELOG.md, so a head taken
/// from before the descriptor (v0.5.0's process) would fail the guard: more
/// than the descriptor would change after it (rule 7). With the head at the
/// descriptor's own commit, the line this command writes is the only change
/// after it. canon refuses when the version is cut (by any of the three
/// sites), when ratified_head already names a different commit (a changed
/// head is a new descriptor commit, rule 7), when the head does not carry the
/// descriptor, when it is not an ancestor of HEAD, or when anything but the
/// descriptor changed between it and HEAD. It edits one line and commits
/// nothing: the commit is the principal's.
/// </summary>
internal static partial class RatifyCommand
{
    public static int Run(Context context, IReadOnlyList<string> arguments)
    {
        string? version = null;
        string? head = null;
        for (int i = 0; i < arguments.Count; i++)
        {
            switch (arguments[i])
            {
                case "--head" when i + 1 < arguments.Count:
                    head = arguments[++i];
                    break;
                case { } value when !value.StartsWith('-') && version is null:
                    version = value;
                    break;
                default:
                    context.Err.WriteLine($"ratify: unknown argument '{arguments[i]}'");
                    return Exit.CouldNotRun;
            }
        }

        if (version is null)
        {
            context.Err.WriteLine("ratify: usage: canon ratify <version> [--head <sha>]");
            return Exit.CouldNotRun;
        }

        string relative = context.Config.DescriptorPath(version);
        string path = Path.Combine(context.Root, relative);
        if (!File.Exists(path))
        {
            context.Err.WriteLine($"ratify: {relative} does not exist");
            return Exit.Refused;
        }

        using GitHubClient? github = ReleaseCommand.GitHubFor(context, required: false);
        IReadOnlyList<(TagSite Site, string Detail)> found = TagPresence.Find(context.Git, context.Config.Remote, github, version);
        if (found.Count > 0)
        {
            context.Err.WriteLine($"ratify: {version} is cut, so its descriptor is immutable (spec/release-format.md rule 6). Found: {string.Join("; ", found.Select(f => f.Detail))}");
            return Exit.Refused;
        }

        string text = File.ReadAllText(path);
        Descriptor descriptor = Descriptor.Parse(relative, text);

        string? resolved = context.Git.Resolve(head ?? "HEAD");
        if (resolved is null)
        {
            context.Err.WriteLine($"ratify: {head ?? "HEAD"} does not name a commit");
            return Exit.Refused;
        }

        if (context.Git.Show(resolved, relative) is null)
        {
            context.Err.WriteLine($"ratify: {resolved[..12]} does not carry {relative}. The ratified head is the commit that holds the descriptor and its {context.Config.ChangelogPath} section (DDD-dec-104); commit them, then ratify.");
            return Exit.Refused;
        }

        if (descriptor.RatifiedHead is { } existing && Descriptor.ShaPattern().IsMatch(existing))
        {
            if (resolved.StartsWith(existing, StringComparison.Ordinal))
            {
                context.Out.WriteLine($"ratify: {relative} already names {existing}; nothing to do");
                return Exit.Ok;
            }

            context.Err.WriteLine($"ratify: {relative} already names ratified_head {existing}, not {resolved[..12]}. A changed head is a new descriptor commit (spec/release-format.md rule 7); edit it by hand in that commit.");
            return Exit.Refused;
        }

        if (!context.Git.IsAncestor(resolved, "HEAD"))
        {
            context.Err.WriteLine($"ratify: {resolved[..12]} is not an ancestor of HEAD");
            return Exit.Refused;
        }

        List<string> extra = context.Git.ChangedPaths(resolved, "HEAD").Where(p => p != relative).ToList();
        if (extra.Count > 0)
        {
            context.Err.WriteLine($"ratify: between {resolved[..12]} and HEAD more than the descriptor changed ({string.Join(", ", extra.Take(5))}); the guard would refuse this release");
            return Exit.Refused;
        }

        string updated = RatifiedHeadLine().IsMatch(text)
            ? RatifiedHeadLine().Replace(text, "ratified_head: " + resolved, 1)
            : InsertAfterVersion(text, resolved);
        if (ReferenceEquals(updated, text) || updated == text)
        {
            context.Err.WriteLine($"ratify: {relative} has no version: line to place ratified_head after");
            return Exit.Refused;
        }

        File.WriteAllText(path, updated);
        context.Out.WriteLine($"ratify: {relative}: ratified_head {resolved}. Not committed.");
        return Exit.Ok;
    }

    private static string InsertAfterVersion(string text, string sha)
    {
        Match match = VersionLine().Match(text);
        return match.Success
            ? text.Insert(match.Index + match.Length, "\nratified_head: " + sha)
            : text;
    }

    [GeneratedRegex(@"^ratified_head:[^\n]*", RegexOptions.Multiline)]
    private static partial Regex RatifiedHeadLine();

    [GeneratedRegex(@"^version:[^\n]*", RegexOptions.Multiline)]
    private static partial Regex VersionLine();
}
