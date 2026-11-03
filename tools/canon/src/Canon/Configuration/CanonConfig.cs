// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

using System;
using System.Collections.Generic;
using System.IO;
using YamlDotNet.RepresentationModel;

namespace Canon.Configuration;

/// <summary>
/// The repository's declaration, canon.yaml at its root (DESIGN.md §3.3).
/// With no file, this repository's layout is the default, so canon runs in a
/// repository that has not declared itself, and nothing about this
/// repository is compiled into any other default.
/// </summary>
internal sealed record CanonConfig
{
    public const string FileName = "canon.yaml";

    public string Remote { get; init; } = "origin";

    public string Trunk { get; init; } = "main";

    /// <summary>owner/name on GitHub; null means: work it out from the remote's URL.</summary>
    public string? GitHub { get; init; }

    public string Releases { get; init; } = "releases";

    public string ChangelogPath { get; init; } = "CHANGELOG.md";

    /// <summary>The first heading line of the frozen tail (DDD-dec-104).</summary>
    public string? ChangelogTailFrom { get; init; }

    /// <summary>SHA-256 of the frozen tail's bytes, lower-case hex.</summary>
    public string? ChangelogTailSha256 { get; init; }

    /// <summary>The first commit the Refs #N rule covers; null means every commit in the range.</summary>
    public string? RefsFrom { get; init; }

    public IReadOnlyList<string> ExemptAuthors { get; init; } = [];

    public IReadOnlyList<string> BasisPaths { get; init; } = ["core/"];

    /// <summary>The first commit the Basis: rule covers (DDD-dec-105: 99d0a0f).</summary>
    public string? BasisFrom { get; init; }

    /// <summary>The first commit whose Basis: ids must resolve (DDD-dec-105).</summary>
    public string? BasisResolveFrom { get; init; }

    public IReadOnlyList<string> CanonDirectories { get; init; } = ["core/claims", "core/decisions"];

    public string Pins { get; init; } = "graph/upstream.yaml";

    /// <summary>The projection's own term registry; a basedOn may name one of its terms (DDD-dec-111).</summary>
    public string LocalTerms { get; init; } = "core/graph/terms.yaml";

    /// <summary>The basedOn entries of filed decisions recorded as unresolved (DDD-dec-111).</summary>
    public string UnresolvedBasis { get; init; } = "graph/unresolved-basis.yaml";

    /// <summary>The shared fixtures both implementations read (DESIGN.md §8.2).</summary>
    public string Fixtures { get; init; } = "scripts/fixtures";

    /// <summary>The Python claim and decision validator, for canon check --compare.</summary>
    public string PythonClaims { get; init; } = "scripts/validate-claims.py";

    /// <summary>The Python release validator, for canon check --compare.</summary>
    public string PythonReleases { get; init; } = "scripts/validate-releases.py";

    /// <summary>The command every gate runs under; until Gate 3 it is scripts/ci.py.</summary>
    public IReadOnlyList<string> Gates { get; init; } = ["python3", "scripts/ci.py"];

    public static CanonConfig Load(string root)
    {
        string path = Path.Combine(root, FileName);
        string text = File.Exists(path) ? File.ReadAllText(path) : "";
        if (string.IsNullOrWhiteSpace(text))
        {
            return new CanonConfig();
        }

        YamlMappingNode yaml = Yaml.LoadMapping(text, FileName);
        CanonConfig defaults = new();
        YamlMappingNode? changelog = Yaml.Mapping(yaml, "changelog");
        YamlMappingNode? refs = Yaml.Mapping(yaml, "issue-refs");
        YamlMappingNode? basis = Yaml.Mapping(yaml, "basis");

        return new CanonConfig
        {
            Remote = Yaml.Scalar(yaml, "remote") ?? defaults.Remote,
            Trunk = Yaml.Scalar(yaml, "trunk") ?? defaults.Trunk,
            GitHub = Yaml.Scalar(yaml, "github"),
            Releases = Yaml.Scalar(yaml, "releases") ?? defaults.Releases,
            ChangelogPath = (changelog is null ? null : Yaml.Scalar(changelog, "path")) ?? defaults.ChangelogPath,
            ChangelogTailFrom = changelog is null ? null : Yaml.Scalar(changelog, "tail-from"),
            ChangelogTailSha256 = changelog is null ? null : Yaml.Scalar(changelog, "tail-sha256"),
            RefsFrom = refs is null ? null : Yaml.Scalar(refs, "from"),
            ExemptAuthors = (refs is null ? null : Yaml.Sequence(refs, "exempt-authors")) ?? defaults.ExemptAuthors,
            BasisPaths = (basis is null ? null : Yaml.Sequence(basis, "paths")) ?? defaults.BasisPaths,
            BasisFrom = basis is null ? null : Yaml.Scalar(basis, "from"),
            BasisResolveFrom = basis is null ? null : Yaml.Scalar(basis, "resolve-from"),
            CanonDirectories = (basis is null ? null : Yaml.Sequence(basis, "canon")) ?? defaults.CanonDirectories,
            Pins = (basis is null ? null : Yaml.Scalar(basis, "pins")) ?? defaults.Pins,
            Gates = Yaml.Sequence(yaml, "gates") is { Count: > 0 } gates ? gates : defaults.Gates,
            Fixtures = Yaml.Scalar(yaml, "fixtures") ?? defaults.Fixtures,
        };
    }

    public string DescriptorPath(string version) => $"{Releases.TrimEnd('/')}/{version}.yaml";
}
