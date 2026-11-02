// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

using System.Collections.Generic;
using System.IO;
using Canon.Releases;

namespace Canon.Commands;

/// <summary>
/// canon changelog              write CHANGELOG.md from releases/
/// canon changelog --check      CHANGELOG.md is exactly the projection
/// canon changelog --tail-sha256  print the SHA-256 of the current frozen tail
/// </summary>
internal static class ChangelogCommand
{
    public static int Run(Context context, IReadOnlyList<string> arguments)
    {
        bool check = false;
        bool hash = false;
        foreach (string argument in arguments)
        {
            switch (argument)
            {
                case "--check":
                    check = true;
                    break;
                case "--tail-sha256":
                    hash = true;
                    break;
                default:
                    context.Err.WriteLine($"changelog: unknown argument '{argument}'");
                    return Exit.CouldNotRun;
            }
        }

        string path = Path.Combine(context.Root, context.Config.ChangelogPath);
        if (hash)
        {
            if (context.Config.ChangelogTailFrom is null || !File.Exists(path)
                || Changelog.Tail(File.ReadAllText(path), context.Config.ChangelogTailFrom) is not { } tail)
            {
                context.Err.WriteLine("changelog: no frozen tail to hash (changelog.tail-from unset, or its line is missing)");
                return Exit.Refused;
            }

            context.Out.WriteLine(Changelog.Sha256(tail));
            return Exit.Ok;
        }

        (string? projection, IReadOnlyList<string> problems) = Changelog.Project(context.Root, context.Config);
        if (projection is null)
        {
            foreach (string problem in problems)
            {
                context.Err.WriteLine("changelog: " + problem);
            }

            return Exit.Refused;
        }

        string current = File.ReadAllText(path);
        if (check)
        {
            if (current == projection)
            {
                context.Out.WriteLine($"changelog: {context.Config.ChangelogPath} is the projection of {context.Config.Releases}/");
                return Exit.Ok;
            }

            context.Err.WriteLine($"changelog: {context.Config.ChangelogPath} is not the projection of {context.Config.Releases}/; run canon changelog");
            return Exit.Refused;
        }

        if (current == projection)
        {
            context.Out.WriteLine($"changelog: {context.Config.ChangelogPath} is up to date");
            return Exit.Ok;
        }

        File.WriteAllText(path, projection);
        context.Out.WriteLine($"changelog: wrote {context.Config.ChangelogPath}");
        return Exit.Ok;
    }
}
