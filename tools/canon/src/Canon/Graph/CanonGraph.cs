// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Text.Json.Nodes;
using System.Text.RegularExpressions;
using Canon.Configuration;
using Canon.Infrastructure;
using Varve.JsonLd;
using Varve.Rdf;
using YamlDotNet.Core;
using YamlDotNet.RepresentationModel;

namespace Canon.Graph;

/// <summary>What a set of files is read as: the class each node gets.</summary>
internal enum CanonKind
{
    /// <summary>A claim, core/claims/.</summary>
    Claim,

    /// <summary>A decision, core/decisions/.</summary>
    Decision,

    /// <summary>A release descriptor, releases/.</summary>
    Release,
}

/// <summary>
/// The mapping from the YAML files to RDF (DESIGN.md §5.2; DDD-dec-107). The
/// files are not changed. Each file is read as YAML, typed as PyYAML types it
/// (YamlJson), and expanded as JSON-LD under canon.context.jsonld, which is
/// passed to the processor from outside (JsonLdOptions.ExpandContext). canon
/// adds to each file's JSON, before expansion:
///   @type            canon:Claim, canon:Decision or canon:Release
///   canon:names      the IRI https://decision-driven-design.dk/id/X of the id
///                    (a release: its version), when it is a plain IRI
///                    segment (DDD-dec-107). The file itself is a blank node:
///                    two files never merge into one node, even with one id.
///                    (They did, at first, and the parallel run caught it:
///                    tools/canon/parallel-run.md, D-02.)
///   canon:sourcePath the repository-relative path
///   canon:fileStem   the file name without .yaml
///   canon:nullKey    each key whose value is null, which JSON-LD would drop
///   canon:basisScalar a release's basis when it is not a list (Python tells
///                    the two apart; RDF cannot)
/// Blank nodes are relabelled per file, so two files never share one.
/// This is the only place, with Shapes, that references Varve.
/// </summary>
internal static partial class CanonGraph
{
    public const string Namespace = "https://decision-driven-design.dk/ns/canon/1#";
    public const string IdBase = "https://decision-driven-design.dk/id/";

    private static readonly byte[] Context = Resource("canon.context.jsonld");

    /// <summary>A file read into the graph: its path, its JSON, and its YAML id or version as the Python validators read them.</summary>
    internal sealed record Source(string Path, JsonObject Json);

    internal sealed class Load(InMemoryDataset data, IReadOnlyDictionary<string, string> files, IReadOnlyList<Finding> findings, IReadOnlyList<Source> sources)
    {
        public InMemoryDataset Data { get; } = data;

        /// <summary>A subject's key (KeyOf) to the file it came from.</summary>
        public IReadOnlyDictionary<string, string> Files { get; } = files;

        /// <summary>Findings made before RDF: a file that does not parse, or is not a mapping.</summary>
        public IReadOnlyList<Finding> Findings { get; } = findings;

        public IReadOnlyList<Source> Sources { get; } = sources;
    }

    /// <summary>
    /// What a reference may resolve to, added to the graph as data: canon file
    /// stems (canon:CanonFile, canon:fileStem), upstream pins (canon:UpstreamPin,
    /// canon:pinId), local terms (canon:LocalTerm, canon:termId), and the
    /// (decision, entry) pairs recorded as unresolved (canon:RecordedUnresolved,
    /// canon:decisionId, canon:entry; DDD-dec-111).
    /// </summary>
    internal sealed record Resolution(
        IReadOnlyCollection<string> Stems,
        IReadOnlyCollection<string> Pins,
        IReadOnlyCollection<string> Terms,
        IReadOnlyCollection<(string Decision, string Entry)> Recorded)
    {
        public static Resolution None { get; } = new([], [], [], []);
    }

    /// <summary>Reads the files into one dataset, with the resolution's stub nodes.</summary>
    public static Load Read(CanonKind kind, IReadOnlyList<(string Path, string Text)> files, IEnumerable<string> canonStems) =>
        Read(kind, files, new Resolution(canonStems.ToList(), [], [], []));

    /// <summary>Reads the files into one dataset, with the resolution's stub nodes.</summary>
    public static Load Read(CanonKind kind, IReadOnlyList<(string Path, string Text)> files, Resolution resolution)
    {
        InMemoryDatasetBuilder builder = new();
        Dictionary<string, string> owners = new(StringComparer.Ordinal);
        List<Finding> findings = [];
        List<Source> sources = [];
        RdfTerm sourcePath = Iri(Namespace + "sourcePath");

        for (int index = 0; index < files.Count; index++)
        {
            (string path, string text) = files[index];
            JsonObject? json = Json(kind, path, text, findings);
            if (json is null)
            {
                continue;
            }

            sources.Add(new Source(path, json));
            byte[] document = Encoding.UTF8.GetBytes(json.ToJsonString());
            string prefix = $"f{index}x";
            JsonLdOptions options = new()
            {
                BaseIri = Encoding.UTF8.GetBytes(IdBase),
                ExpandContext = Context,
            };

            JsonLdResult result = JsonLdParser.Parse(
                document,
                (in QuadView quad) =>
                {
                    RdfTerm subject = Relabel(quad.Subject.Materialise(), prefix);
                    RdfTerm predicate = quad.Predicate.Materialise();
                    RdfTerm obj = Relabel(quad.Object.Materialise(), prefix);
                    builder.Add(subject, predicate, obj, default);
                    if (predicate.Equals(sourcePath))
                    {
                        owners[KeyOf(subject)] = path;
                    }
                },
                in options);

            if (!result.Succeeded)
            {
                findings.Add(new Finding(path, "LOAD-JSONLD", false, $"the JSON-LD mapping failed: {result.Error?.Code} {result.Error?.Message}"));
            }
        }

        RdfTerm type = Iri("http://www.w3.org/1999/02/22-rdf-syntax-ns#type");
        int stub = 0;
        void Stub(string cls, params (string Property, string Value)[] values)
        {
            RdfTerm node = RdfTerm.BlankNode(Encoding.UTF8.GetBytes($"stub{stub++}"));
            builder.Add(node, type, Iri(Namespace + cls), default);
            foreach ((string property, string value) in values)
            {
                builder.Add(node, Iri(Namespace + property), RdfTerm.Literal(Encoding.UTF8.GetBytes(value)), default);
            }
        }

        foreach (string stem in resolution.Stems)
        {
            Stub("CanonFile", ("fileStem", stem));
        }

        foreach (string pin in resolution.Pins)
        {
            Stub("UpstreamPin", ("pinId", pin));
        }

        foreach (string term in resolution.Terms)
        {
            Stub("LocalTerm", ("termId", term));
        }

        foreach ((string decision, string entry) in resolution.Recorded)
        {
            Stub("RecordedUnresolved", ("decisionId", decision), ("entry", entry));
        }

        return new Load(builder.ToDataset(), owners, findings, sources);
    }

    /// <summary>The file's JSON, with canon's additions; null (and a finding) when it cannot be read.</summary>
    private static JsonObject? Json(CanonKind kind, string path, string text, List<Finding> findings)
    {
        YamlStream stream = [];
        try
        {
            stream.Load(new StringReader(text));
        }
        catch (YamlException exception)
        {
            findings.Add(new Finding(path, "LOAD-YAML", false, "not valid YAML: " + exception.Message));
            return null;
        }

        if (stream.Documents.Count != 1 || stream.Documents[0].RootNode is not YamlMappingNode root)
        {
            findings.Add(new Finding(path, kind == CanonKind.Release ? "REL-NOT-MAPPING" : "LOAD-NOT-MAPPING", false, "descriptor is not a YAML mapping"));
            return null;
        }

        JsonObject json = (JsonObject)YamlJson.Convert(root)!;
        JsonArray nulls = [];
        foreach ((string key, JsonNode? value) in json.ToList())
        {
            if (value is null)
            {
                nulls.Add((JsonNode)JsonValue.Create(key));
            }
        }

        if (kind == CanonKind.Release && json["basis"] is { } basis and not JsonArray)
        {
            json.Remove("basis");
            json["canon:basisScalar"] = basis;
        }

        string stem = System.IO.Path.GetFileNameWithoutExtension(path);
        string? identity = kind == CanonKind.Release ? Text(json["version"]) : Text(json["id"]);
        if (identity is not null && PlainSegment().IsMatch(identity))
        {
            json["canon:names"] = new JsonObject { ["@id"] = identity };
        }

        json["@type"] = "canon:" + kind;
        json["canon:sourcePath"] = path;
        json["canon:fileStem"] = stem;
        if (nulls.Count > 0)
        {
            json["canon:nullKey"] = nulls;
        }

        return json;
    }

    public static string KeyOf(RdfTerm term) =>
        $"{(int)term.Kind}|{Encoding.UTF8.GetString(term.Lexical)}";

    public static RdfTerm Iri(string iri) => RdfTerm.Iri(Encoding.UTF8.GetBytes(iri));

    public static RdfTerm Relabel(RdfTerm term, string prefix) =>
        term.Kind == RdfTermKind.BlankNode
            ? RdfTerm.BlankNode(Encoding.UTF8.GetBytes(prefix + Encoding.UTF8.GetString(term.Lexical)))
            : term;

    private static string? Text(JsonNode? node) =>
        node is JsonValue value && value.TryGetValue(out string? text) ? text : null;

    internal static byte[] Resource(string name)
    {
        using Stream stream = Assembly.GetExecutingAssembly().GetManifestResourceStream("Canon.Shapes." + name)
            ?? throw new CanonException($"canon's resource {name} is missing from the build");
        using MemoryStream copy = new();
        stream.CopyTo(copy);
        return copy.ToArray();
    }

    [GeneratedRegex(@"\A[A-Za-z0-9._~-]+\z")]
    private static partial Regex PlainSegment();
}
