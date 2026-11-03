// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.Json.Nodes;
using Canon.Configuration;
using Canon.Graph;

namespace Canon.Checks;

/// <summary>
/// The three graph gates over a target, a directory of YAML files or one
/// file, read as the Python validators read it: a directory's *.yaml files,
/// not recursively, in sorted order. Each gate returns its findings, errors and
/// warnings; a gate fails when it has an error.
/// </summary>
internal static class GraphGates
{
    private static readonly Lazy<Shapes> ClaimShapes = new(() => Shapes.For(CanonKind.Claim));
    private static readonly Lazy<Shapes> DecisionShapes = new(() => Shapes.For(CanonKind.Decision));
    private static readonly Lazy<Shapes> ReleaseShapes = new(() => Shapes.For(CanonKind.Release));
    private static readonly string[] Live = ["projected", "reported", "established"];

    /// <summary>Every rule code the graph gates can report: the shapes' and the code-level ones.</summary>
    public static IReadOnlyCollection<string> AllCodes() =>
        [.. ClaimShapes.Value.Codes, .. DecisionShapes.Value.Codes, .. ReleaseShapes.Value.Codes,
         "CLAIM-SINGLE-LIMB", "REL-NOT-MAPPING", "REL-NO-CANON", "LOAD-YAML", "LOAD-NOT-MAPPING", "LOAD-JSONLD"];

    public static IReadOnlyList<(string Path, string Text)> Files(string root, string target)
    {
        string full = Path.Combine(root, target);
        IEnumerable<string> paths = Directory.Exists(full)
            ? Directory.GetFiles(full, "*.yaml").OrderBy(p => p, StringComparer.Ordinal)
            : File.Exists(full) ? [full] : [];
        return paths.Select(p => (Path.GetRelativePath(root, p).Replace('\\', '/'), File.ReadAllText(p))).ToList();
    }

    public static (List<Finding> Findings, CanonGraph.Load Load) Claims(string root, string target)
    {
        CanonGraph.Load load = CanonGraph.Read(CanonKind.Claim, Files(root, target), []);
        List<Finding> findings = [.. load.Findings, .. ClaimShapes.Value.Validate(load)];
        foreach (CanonGraph.Source source in load.Sources)
        {
            if (IsInteger(source.Json["format"], 1) && Text(source.Json["status"]) is { } status && Live.Contains(status))
            {
                int limbs = SingleLimb.Count(source.Json["statement"]);
                if (limbs > 0)
                {
                    findings.Add(new Finding(source.Path, "CLAIM-SINGLE-LIMB", true,
                        $"statement joins ~{limbs + 1} limbs (rule 1: one proposition per claim). Candidate for adjudication, not a verdict"));
                }
            }
        }

        return (findings, load);
    }

    public static (List<Finding> Findings, CanonGraph.Load Load) Decisions(string root, string target)
    {
        CanonGraph.Load load = CanonGraph.Read(CanonKind.Decision, Files(root, target), []);
        return ([.. load.Findings, .. DecisionShapes.Value.Validate(load)], load);
    }

    /// <summary>The descriptors' validation, resolving basis against the canon directories' file stems in root, as Python does.</summary>
    public static (List<Finding> Findings, CanonGraph.Load Load) Releases(string root, string target, CanonConfig config)
    {
        List<string> stems = config.CanonDirectories
            .Select(d => Path.Combine(root, d))
            .Where(Directory.Exists)
            .SelectMany(d => Directory.GetFiles(d, "*.yaml"))
            .Select(Path.GetFileNameWithoutExtension)
            .OfType<string>()
            .ToList();
        CanonGraph.Load load = CanonGraph.Read(CanonKind.Release, Files(root, target), stems);
        List<Finding> findings = [.. load.Findings, .. ReleaseShapes.Value.Validate(load)];
        if (stems.Count == 0)
        {
            findings.Add(new Finding("*", "REL-NO-CANON", false, $"no claims or decisions found under {string.Join(" or ", config.CanonDirectories)}; cannot resolve basis"));
        }

        return (findings, load);
    }

    public static bool IsInteger(JsonNode? node, long expected) =>
        node is JsonValue value && value.TryGetValue(out long number) && number == expected;

    public static string? Text(JsonNode? node) =>
        node is JsonValue value && value.TryGetValue(out string? text) ? text : null;
}
