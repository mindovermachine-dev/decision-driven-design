// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using Canon.Commands;
using Canon.Configuration;
using Canon.Infrastructure;

namespace Canon;

/// <summary>
/// The command line. Hand-parsed, as Varve's eng/ scripts are: five commands
/// with a handful of flags each do not need a parser library, and an
/// argument list read in plain code is easy to audit.
/// </summary>
internal static class Cli
{
    private const string Usage = """
        usage: canon [--repo <path>] <command> [arguments]

          land <pr> [--main] | land --commit <rev> [--main]   land by fast-forward (Varve's land.cs)
          release <version> [--plan]                         cut a release from its landed descriptor
          ratify <version> [--head <sha>]                    fill ratified_head in releases/<version>.yaml
          changelog [--check | --tail-sha256]                CHANGELOG.md as the projection of releases/
          issue-refs [--base <ref>] [--head <ref>] [--basis] Refs #N, and Basis: on canon commits
          check [gate ...] [--compare] [--markdown] [--list]  the graph gates (SHACL via Varve); --compare against Python

        exit codes: 0 done or conformant, 1 refused, 2 could not run
        """;

    public static int Run(IReadOnlyList<string> arguments, TextWriter output, TextWriter error, string directory, IReadOnlyDictionary<string, string> environment)
    {
        List<string> rest = [.. arguments];
        string? repo = null;
        if (rest.Count >= 2 && rest[0] == "--repo")
        {
            repo = rest[1];
            rest.RemoveRange(0, 2);
        }

        if (rest.Count == 0 || rest[0] is "--help" or "-h" or "help")
        {
            (rest.Count == 0 ? error : output).WriteLine(Usage);
            return rest.Count == 0 ? Exit.CouldNotRun : Exit.Ok;
        }

        try
        {
            string start = Path.GetFullPath(repo ?? directory);
            ProcessResult top = Processes.Run("git", start, ["rev-parse", "--show-toplevel"]);
            if (top.Exit != 0)
            {
                error.WriteLine($"canon: {start} is not inside a git repository");
                return Exit.CouldNotRun;
            }

            string root = top.Output.Trim();
            Context context = new(root, CanonConfig.Load(root), output, error, environment);
            IReadOnlyList<string> tail = rest.Skip(1).ToList();
            return rest[0] switch
            {
                "land" => LandCommand.Run(context, tail),
                "release" => ReleaseCommand.Run(context, tail),
                "ratify" => RatifyCommand.Run(context, tail),
                "changelog" => ChangelogCommand.Run(context, tail),
                "issue-refs" => IssueRefsCommand.Run(context, tail),
                "check" => CheckCommand.Run(context, tail),
                _ => UnknownCommand(rest[0], error),
            };
        }
        catch (CanonException exception)
        {
            error.WriteLine("canon: " + exception.Message);
            return Exit.CouldNotRun;
        }
#pragma warning disable CA1031 // Any other failure is canon's defect: it could not run, which is exit 2, never a pass.
        catch (Exception exception)
#pragma warning restore CA1031
        {
            error.WriteLine($"canon: internal error, could not run: {exception}");
            return Exit.CouldNotRun;
        }
    }

    private static int UnknownCommand(string name, TextWriter error)
    {
        error.WriteLine($"canon: unknown command '{name}'");
        error.WriteLine(Usage);
        return Exit.CouldNotRun;
    }
}
