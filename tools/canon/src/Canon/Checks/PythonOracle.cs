// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;
using Canon.Graph;
using Canon.Infrastructure;

namespace Canon.Checks;

/// <summary>
/// The Python validators, run as they are, with their findings mapped to
/// canon's rule codes so the two can be compared (DESIGN.md §8.3). The
/// mapping is a table of the Python messages, one line per rule; a message no
/// line matches maps to PY-UNMAPPED and is therefore a disagreement, never
/// silently equal.
/// </summary>
internal static partial class PythonOracle
{
    private static readonly (Regex Pattern, string Code)[] Table =
    [
        (new(@"^format missing or unsupported"), "FORMAT"),
        (new(@"^id does not match"), "CLAIM-ID"),
        (new(@"^kind missing or illegal"), "CLAIM-KIND"),
        (new(@"^status missing or illegal"), "CLAIM-STATUS"),
        (new(@"^statement missing"), "CLAIM-STATEMENT"),
        (new(@"^region missing"), "CLAIM-REGION"),
        (new(@"^changed missing"), "CLAIM-CHANGED"),
        (new(@"requires at least one evidence entry"), "CLAIM-EVIDENCE"),
        (new(@"requires a derivation evidence entry"), "CLAIM-DERIVATION"),
        (new(@"^retired claim requires supersedes"), "CLAIM-RETIRED-PROVENANCE"),
        (new(@"^\[falsifier-presence\]"), "CLAIM-FALSIFIER"),
        (new(@"^\[falsifier-strict\]"), "CLAIM-FALSIFIER-STRICT"),
        (new(@"^\[single-limb\]"), "CLAIM-SINGLE-LIMB"),
        (new(@"^\[retired-from\] retired claim requires retired_from"), "CLAIM-RETIRED-FROM-MISSING"),
        (new(@"^\[retired-from\] retired_from is legal only"), "CLAIM-RETIRED-FROM-NOT-RETIRED"),
        (new(@"^\[retired-from\] retired_from illegal"), "CLAIM-RETIRED-FROM-ILLEGAL"),
        (new(@"^\[retired-from\] retired_from 'unrecoverable' requires"), "CLAIM-RETIRED-FROM-NOTES"),
        (new(@"^duplicate ids"), "DUPLICATE-ID"),
        (new(@"no accountable principal"), "DEC-PRINCIPAL"),
        (new(@"no basedOn edges"), "DEC-BASEDON"),
        (new(@"no resolution"), "DEC-RESOLUTION"),
        (new(@"no made timestamp"), "DEC-MADE"),
        (new(@"^descriptor is not a YAML mapping"), "REL-NOT-MAPPING"),
        (new(@"^version missing or not"), "REL-VERSION"),
        (new(@"^filename .* disagrees with version"), "REL-FILENAME"),
        (new(@"^title missing"), "REL-TITLE-MISSING"),
        (new(@"^title must be one line"), "REL-TITLE-ONE-LINE"),
        (new(@"^title starts with a version"), "REL-TITLE-VERSION-PREFIX"),
        (new(@"^commit is not a hex SHA"), "REL-COMMIT"),
        (new(@"^date is not YYYY-MM-DD"), "REL-DATE"),
        (new(@"^basis missing or empty"), "REL-BASIS-MISSING"),
        (new(@"^basis must be a list"), "REL-BASIS-NOT-LIST"),
        (new(@"^basis entry is not"), "REL-BASIS-ENTRY"),
        (new(@"does not resolve to core/claims/"), "REL-BASIS-UNRESOLVED"),
        (new(@"^summary missing"), "REL-SUMMARY"),
        (new(@"^ratified_head missing or not"), "REL-RATIFIED-HEAD"),
        (new(@"^ratified_head is a format 2 field"), "REL-RATIFIED-HEAD-FORMAT1"),
        (new(@"must be a boolean"), "REL-FLAG-BOOLEAN"),
        (new(@"^duplicate versions"), "REL-DUPLICATE-VERSION"),
        (new(@"^no claims or decisions found"), "REL-NO-CANON"),
    ];

    /// <summary>One run of a Python validator: its exit code, its findings in canon's terms (file name, code, warning), and its raw output.</summary>
    internal sealed record Run(int Exit, IReadOnlyList<(string File, string Code, bool Warning)> Findings, string Output);

    public static Run Execute(string root, string script, string target, bool decisions, CanonKind kind, CanonGraph.Load canonLoad)
    {
        List<string> arguments = [script, target];
        if (decisions)
        {
            arguments.Add("--decisions");
        }

        ProcessResult result = Processes.Run("python3", root, arguments);
        if (result.Exit == Processes.NotFound)
        {
            throw new CanonException("python3 is not installed; the comparison needs the Python validators");
        }

        Dictionary<string, string> owner = Owners(canonLoad, kind);
        List<(string, string, bool)> findings = [];
        bool warnings = false;
        foreach (string raw in (result.Error + "\n" + result.Output).Split('\n'))
        {
            string line = raw.TrimEnd('\r');
            if (line.Contains("warning(s) across", StringComparison.Ordinal))
            {
                warnings = true;
                continue;
            }

            if (line.StartsWith("INVALID", StringComparison.Ordinal))
            {
                warnings = false;
                continue;
            }

            if (line.StartsWith("Traceback", StringComparison.Ordinal))
            {
                findings.Add(("*", "PY-CRASH", false));
                continue;
            }

            if (!line.StartsWith("  ", StringComparison.Ordinal) || line.StartsWith("   ", StringComparison.Ordinal))
            {
                continue;
            }

            string body = line[2..];
            int colon = body.IndexOf(": ", StringComparison.Ordinal);
            if (colon < 0)
            {
                continue;
            }

            string where = body[..colon];
            string message = body[(colon + 2)..];
            string code = Table.FirstOrDefault(t => t.Pattern.IsMatch(message)).Code ?? "PY-UNMAPPED " + message;
            code = code switch
            {
                "FORMAT" => kind == CanonKind.Release ? "REL-FORMAT" : "CLAIM-FORMAT",
                "DUPLICATE-ID" => kind == CanonKind.Decision ? "DEC-DUPLICATE-ID" : "CLAIM-DUPLICATE-ID",
                _ => code,
            };
            string file = where == "global" ? "*" : owner.TryGetValue(where, out string? found) ? found : Path.GetFileName(where);
            findings.Add((file, code, warnings));
        }

        return new Run(result.Exit, findings, (result.Error + result.Output).Trim());
    }

    /// <summary>What Python prints as a finding's "where" (an id, a version, or a path), to the file name.</summary>
    private static Dictionary<string, string> Owners(CanonGraph.Load load, CanonKind kind)
    {
        Dictionary<string, string> owner = new(StringComparer.Ordinal);
        foreach (CanonGraph.Source source in load.Sources)
        {
            string name = Path.GetFileName(source.Path);
            owner[source.Path] = name;
            owner[name] = name;
            string? key = kind == CanonKind.Release ? GraphGates.Text(source.Json["version"]) : GraphGates.Text(source.Json["id"]);
            if (key is not null)
            {
                owner.TryAdd(key, name);
            }
        }

        return owner;
    }
}
