// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Canon.Infrastructure;
using Varve.Rdf;
using Varve.Shacl;
using Varve.Shacl.Model;
using Varve.Shacl.Sparql;
using Varve.Sparql.Evaluation;
using Varve.Turtle;

namespace Canon.Graph;

/// <summary>
/// The shapes of one kind (common.ttl plus claim, decision or release
/// .shapes.ttl), loaded once into Varve.Shacl with SHACL-SPARQL as an
/// extension, and the validation of a canon graph against them. A result's
/// rule code is the canon:rule of its source shape; every rule is a node
/// shape whose constraint is sh:node, sh:or or sh:sparql, so the source shape
/// is always the rule.
/// </summary>
internal sealed class Shapes
{
    private static readonly ShaclOptions Options = new()
    {
        Extensions = [SparqlConstraints.Extension(new EvaluationOptions())],
    };

    private readonly ShapesGraph graph;
    private readonly Dictionary<string, string> codes;

    private Shapes(ShapesGraph graph, Dictionary<string, string> codes)
    {
        this.graph = graph;
        this.codes = codes;
    }

    /// <summary>Every rule code these shapes carry.</summary>
    public IReadOnlyCollection<string> Codes => codes.Values.Distinct(StringComparer.Ordinal).ToList();

    public static Shapes For(CanonKind kind)
    {
        string file = kind switch
        {
            CanonKind.Claim => "claim.shapes.ttl",
            CanonKind.Decision => "decision.shapes.ttl",
            _ => "release.shapes.ttl",
        };

        InMemoryDatasetBuilder builder = new();
        Dictionary<string, string> codes = new(StringComparer.Ordinal);
        RdfTerm rule = CanonGraph.Iri(CanonGraph.Namespace + "rule");
        // Each resource is parsed on its own, and every parse labels its blank
        // nodes from _:g0, so the labels are prefixed per resource: merged
        // unprefixed, two files' lists would share nodes and be ill-formed.
        string[] resources = ["common.ttl", file];
        for (int index = 0; index < resources.Length; index++)
        {
            string name = resources[index];
            string prefix = $"r{index}x";
            ParseResult parsed = TurtleParser.Parse(
                CanonGraph.Resource(name),
                (in QuadView quad) =>
                {
                    RdfTerm s = CanonGraph.Relabel(quad.Subject.Materialise(), prefix);
                    RdfTerm p = quad.Predicate.Materialise();
                    RdfTerm o = CanonGraph.Relabel(quad.Object.Materialise(), prefix);
                    builder.Add(s, p, o, default);
                    if (p.Equals(rule))
                    {
                        codes[CanonGraph.KeyOf(s)] = Encoding.UTF8.GetString(o.Lexical);
                    }
                },
                new TurtleOptions { Syntax = RdfSyntax.Turtle });
            if (!parsed.Succeeded)
            {
                throw new CanonException($"{name} does not parse as Turtle: {parsed.FirstError}");
            }
        }

        ShapesLoad load = ShapesGraph.Load(builder.ToDataset(), GraphPattern.DefaultGraph, Options, default);
        return load.Shapes is { } loaded
            ? new Shapes(loaded, codes)
            : throw new CanonException($"{file} does not load as SHACL: " + string.Join("; ", load.Problems.Select(p => $"{p.Kind} {p.Message}")));
    }

    /// <summary>Validates the graph; one finding per result, in the report's order.</summary>
    public IReadOnlyList<Finding> Validate(CanonGraph.Load load)
    {
        ValidationOutcome outcome = ShaclValidator.Validate(graph, load.Data, GraphPattern.DefaultGraph, Options, default);
        if (!outcome.Succeeded)
        {
            throw new CanonException("SHACL validation could not run: " + string.Join("; ", outcome.Problems.Select(p => $"{p.Kind} {p.Message}")));
        }

        List<Finding> findings = [];
        HashSet<string> duplicates = new(StringComparer.Ordinal);
        foreach (ShaclResult result in outcome.Report!.Results)
        {
            string code = codes.TryGetValue(CanonGraph.KeyOf(result.SourceShape), out string? found) ? found : "SHAPE-" + Encoding.UTF8.GetString(result.SourceShape.Lexical);
            string file = code.EndsWith("DUPLICATE-ID", StringComparison.Ordinal) || code.EndsWith("DUPLICATE-VERSION", StringComparison.Ordinal)
                ? "*"
                : load.Files.TryGetValue(CanonGraph.KeyOf(result.FocusNode), out string? path) ? path : "?";
            string message = result.Messages.Count > 0 ? Encoding.UTF8.GetString(result.Messages[0].Lexical) : code;
            if (result.Value is { Kind: RdfTermKind.Literal } value && code is "REL-BASIS-ENTRY" or "REL-BASIS-UNRESOLVED")
            {
                message += ": " + Encoding.UTF8.GetString(value.Lexical);
            }

            // A repeated id is one finding about the set, as Python reports it
            // ("duplicate ids: [...]" once), not one per file that carries it.
            if (file == "*" && !duplicates.Add(code))
            {
                continue;
            }

            bool warning = Encoding.UTF8.GetString(result.Severity.Lexical).EndsWith("#Warning", StringComparison.Ordinal);
            findings.Add(new Finding(file, code, warning, message));
        }

        return findings;
    }
}
