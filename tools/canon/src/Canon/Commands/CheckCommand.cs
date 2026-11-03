// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using Canon.Checks;
using Canon.Graph;

namespace Canon.Commands;

/// <summary>
/// canon check [gate ...] [--compare] [--markdown] [--list]
///
/// The gates canon has ported (DESIGN.md §4.1, §6): claims, decisions and
/// releases through Varve's SHACL over the YAML mapped to RDF, the releases
/// gate's git half (cut and guard), and canon's own verdicts on the shared
/// fixtures. Gates not ported yet (core-order, the What, the How examples) are
/// named and left to scripts/ci.py, which CI runs beside this.
///
/// --compare runs each ported validator in both implementations over every
/// fixture and the live tree and compares them: the verdict, and the multiset
/// of (file, rule, severity) findings (DESIGN.md §8.3). Any disagreement exits
/// 1. Nothing is excluded or allowed to fail.
/// </summary>
internal static class CheckCommand
{
    private static readonly (string Name, string What)[] Gates =
    [
        ("claims", "core/claims/ against the claim shapes (SHACL, Varve)"),
        ("decisions", "core/decisions/ against the decision shapes: no escaped decisions"),
        ("releases", "release descriptors against the release shapes; the guard or the cut check for each"),
        ("fixtures", "each graph gate accepts its accept tree and refuses its refuse cases"),
    ];

    private static readonly string[] NotPorted = ["core-order", "what", "how"];

    public static int Run(Context context, IReadOnlyList<string> arguments)
    {
        bool compare = arguments.Contains("--compare");
        bool markdown = arguments.Contains("--markdown");
        if (arguments.Contains("--list"))
        {
            foreach ((string name, string what) in Gates)
            {
                context.Out.WriteLine($"{name,-10}  {what}");
            }

            context.Out.WriteLine($"not ported, run by scripts/ci.py: {string.Join(", ", NotPorted)}");
            return Exit.Ok;
        }

        List<string> named = arguments.Where(a => !a.StartsWith('-')).ToList();
        foreach (string unknown in named.Where(n => Gates.All(g => g.Name != n)))
        {
            context.Err.WriteLine($"check: unknown gate '{unknown}'; see canon check --list");
            return Exit.CouldNotRun;
        }

        int failed = 0;
        foreach ((string name, string what) in Gates.Where(g => named.Count == 0 || named.Contains(g.Name)))
        {
            (List<Finding> findings, List<string> notes) = name switch
            {
                "claims" => (GraphGates.Claims(context.Root, CanonDirectory(context, "claims")).Findings, new List<string>()),
                "decisions" => (GraphGates.Decisions(context.Root, CanonDirectory(context, "decisions")).Findings, new List<string>()),
                "releases" => ReleasesGate(context),
                _ => FixturesGate(context),
            };

            int errors = findings.Count(f => !f.Warning);
            failed += errors > 0 ? 1 : 0;
            context.Out.WriteLine($"{(errors > 0 ? "FAIL" : "ok  ")} {name,-10}  {what}");
            foreach (string note in notes)
            {
                context.Out.WriteLine("       " + note);
            }

            foreach (Finding finding in findings)
            {
                (finding.Warning ? context.Out : context.Err).WriteLine("       " + finding);
            }
        }

        context.Out.WriteLine($"not ported, run by scripts/ci.py: {string.Join(", ", NotPorted)}");

        if (compare)
        {
            failed += Compare(context, markdown) ? 0 : 1;
        }

        context.Out.WriteLine(failed == 0 ? "canon check: all gates passed" : $"canon check: {failed} failed");
        return failed == 0 ? Exit.Ok : Exit.Refused;
    }

    private static string CanonDirectory(Context context, string which) =>
        context.Config.CanonDirectories.FirstOrDefault(d => d.TrimEnd('/').EndsWith(which, StringComparison.Ordinal)) ?? "core/" + which;

    private static (List<Finding>, List<string>) ReleasesGate(Context context)
    {
        (List<Finding> findings, _) = GraphGates.Releases(context.Root, context.Config.Releases, context.Config);
        if (findings.Any(f => !f.Warning))
        {
            return (findings, []);
        }

        List<string> descriptors = GraphGates.Files(context.Root, context.Config.Releases).Select(f => f.Path).ToList();
        (List<Finding> cuts, List<string> notes) = ReleaseCuts.Check(context.Git, context.Config.Remote, descriptors);
        return ([.. findings, .. cuts], notes);
    }

    private static (List<Finding>, List<string>) FixturesGate(Context context)
    {
        List<Finding> findings = [];
        List<string> notes = [];
        foreach (Case c in Cases(context).Where(c => !c.Live))
        {
            List<Finding> got = Canon(context, c).Findings;
            bool refused = got.Any(f => !f.Warning);
            bool ok = c.Refuse == refused;
            notes.Add($"{(ok ? "ok  " : "FAIL")} {(c.Refuse ? "refuse" : "accept")} {c.Label}");
            if (!ok)
            {
                findings.Add(new Finding(c.Target, "FIXTURE", false, $"expected to {(c.Refuse ? "refuse" : "accept")}; canon found {got.Count(f => !f.Warning)} error(s)"));
            }
        }

        return (findings, notes);
    }

    private sealed record Case(CanonKind Kind, string Label, string Target, bool Refuse, bool Live);

    private static IEnumerable<Case> Cases(Context context)
    {
        string fixtures = context.Config.Fixtures.TrimEnd('/');
        foreach ((CanonKind kind, string name, string live) in new[]
                 {
                     (CanonKind.Claim, "claims", CanonDirectory(context, "claims")),
                     (CanonKind.Decision, "decisions", CanonDirectory(context, "decisions")),
                     (CanonKind.Release, "releases", context.Config.Releases),
                 })
        {
            yield return new Case(kind, $"{name}/accept", $"{fixtures}/{name}/accept", false, false);
            string refuse = Path.Combine(context.Root, fixtures, name, "refuse");
            IEnumerable<string> entries = !Directory.Exists(refuse)
                ? []
                : kind == CanonKind.Release
                    ? Directory.GetDirectories(refuse)
                    : Directory.GetFiles(refuse, "*.yaml");
            foreach (string entry in entries.OrderBy(e => e, StringComparer.Ordinal))
            {
                string leaf = Path.GetFileName(entry);
                yield return new Case(kind, $"{name}/refuse/{leaf}", $"{fixtures}/{name}/refuse/{leaf}", true, false);
            }

            yield return new Case(kind, $"{name} (live: {live})", live, false, true);
        }
    }

    private static (List<Finding> Findings, CanonGraph.Load Load) Canon(Context context, Case c) => c.Kind switch
    {
        CanonKind.Claim => GraphGates.Claims(context.Root, c.Target),
        CanonKind.Decision => GraphGates.Decisions(context.Root, c.Target),
        _ => GraphGates.Releases(context.Root, c.Target, context.Config),
    };

    /// <summary>Both implementations over every case; true when every case agrees.</summary>
    private static bool Compare(Context context, bool markdown)
    {
        context.Out.WriteLine();
        context.Out.WriteLine("compare: canon (Varve SHACL) against the Python validators, every fixture and the live tree");
        context.Out.WriteLine(markdown
            ? "\n| case | python | canon | findings (python / canon) | agree |\n|---|---|---|---|---|"
            : $"  {"case",-52} {"python",-8} {"canon",-8} {"findings",-10} agree");

        int disagreements = 0;
        HashSet<string> exercised = new(StringComparer.Ordinal);
        foreach (Case c in Cases(context))
        {
            (List<Finding> findings, CanonGraph.Load load) = Canon(context, c);
            exercised.UnionWith(findings.Select(f => f.Code));
            string script = c.Kind == CanonKind.Release ? context.Config.PythonReleases : context.Config.PythonClaims;
            PythonOracle.Run python = PythonOracle.Execute(context.Root, script, c.Target, c.Kind == CanonKind.Decision, c.Kind, load);

            List<string> canonKeys = findings.Select(f => Key(f.File == "*" ? "*" : Path.GetFileName(f.File), f.Code, f.Warning)).OrderBy(k => k, StringComparer.Ordinal).ToList();
            List<string> pythonKeys = python.Findings.Select(f => Key(f.File, f.Code, f.Warning)).OrderBy(k => k, StringComparer.Ordinal).ToList();
            bool canonRefuses = findings.Any(f => !f.Warning);
            bool pythonRefuses = python.Exit != 0;
            bool agree = canonRefuses == pythonRefuses && canonKeys.SequenceEqual(pythonKeys, StringComparer.Ordinal);
            disagreements += agree ? 0 : 1;

            string pv = pythonRefuses ? "refuse" : "accept";
            string cv = canonRefuses ? "refuse" : "accept";
            string counts = $"{pythonKeys.Count} / {canonKeys.Count}";
            context.Out.WriteLine(markdown
                ? $"| `{c.Label}` | {pv} | {cv} | {counts} | {(agree ? "yes" : "**no**")} |"
                : $"  {c.Label,-52} {pv,-8} {cv,-8} {counts,-10} {(agree ? "yes" : "NO")}");

            if (!agree)
            {
                foreach (string only in pythonKeys.Except(canonKeys, StringComparer.Ordinal).Concat(Surplus(pythonKeys, canonKeys)).Distinct())
                {
                    context.Err.WriteLine($"      python only: {only}");
                }

                foreach (string only in canonKeys.Except(pythonKeys, StringComparer.Ordinal).Concat(Surplus(canonKeys, pythonKeys)).Distinct())
                {
                    context.Err.WriteLine($"      canon only:  {only}");
                }
            }
        }

        List<string> all = GraphGates.AllCodes().Distinct(StringComparer.Ordinal).OrderBy(c => c, StringComparer.Ordinal).ToList();
        List<string> unexercised = all.Where(c => !exercised.Contains(c)).ToList();
        context.Out.WriteLine($"compare: rules exercised by the corpus: {all.Count - unexercised.Count} of {all.Count}. Not exercised, so not compared: {(unexercised.Count == 0 ? "none" : string.Join(", ", unexercised))}");
        context.Out.WriteLine(disagreements == 0
            ? "compare: every case agrees"
            : $"compare: {disagreements} case(s) disagree. Each is a defect in one of the two, to be recorded in tools/canon/parallel-run.md and fixed, never suppressed.");
        return disagreements == 0;
    }

    private static string Key(string file, string code, bool warning) => $"{file} {code}{(warning ? " (warning)" : "")}";

    /// <summary>Keys present in both but more often in the first: a multiset difference.</summary>
    private static IEnumerable<string> Surplus(List<string> first, List<string> second) =>
        first.GroupBy(k => k, StringComparer.Ordinal)
            .Where(g => second.Contains(g.Key, StringComparer.Ordinal) && g.Count() > second.Count(k => k == g.Key))
            .Select(g => $"{g.Key} x{g.Count() - second.Count(k => k == g.Key)} more");
}
