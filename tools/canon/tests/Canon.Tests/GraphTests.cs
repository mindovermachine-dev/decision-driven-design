// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.Json;
using System.Text.Json.Nodes;
using Canon.Checks;
using Canon.Configuration;
using Canon.Graph;
using Canon.Infrastructure;
using Xunit;
using YamlDotNet.RepresentationModel;

namespace Canon.Tests;

/// <summary>
/// The graph gates (Gate 3), against real inputs: this repository itself, the
/// Python validators themselves, and PyYAML itself. Nothing is restated as an
/// expected value that one of those can answer.
/// </summary>
public sealed class GraphTests
{
    private static readonly Dictionary<string, string> NoEnvironment = [];

    /// <summary>The repository these tests are built from: the directory above the test binary that holds canon.yaml.</summary>
    private static string Repository()
    {
        for (DirectoryInfo? d = new(AppContext.BaseDirectory); d is not null; d = d.Parent)
        {
            if (File.Exists(Path.Combine(d.FullName, "canon.yaml")) && Directory.Exists(Path.Combine(d.FullName, "scripts")))
            {
                return d.FullName;
            }
        }

        throw new InvalidOperationException("the repository root (canon.yaml) is not above " + AppContext.BaseDirectory);
    }

    [Fact]
    public void EveryShapeSetLoadsInVarve()
    {
        Assert.Contains("CLAIM-FALSIFIER", GraphGates.AllCodes());
        Assert.Contains("DEC-BASEDON", GraphGates.AllCodes());
        Assert.Contains("REL-BASIS-UNRESOLVED", GraphGates.AllCodes());
    }

    /// <summary>The parallel run itself, on this repository: every fixture and the live tree agree with the Python validators.</summary>
    [Fact]
    public void CanonAgreesWithThePythonValidatorsOnEveryFixtureAndTheLiveTree()
    {
        var result = Sandbox.CanonIn(Repository(), NoEnvironment, "check", "claims", "decisions", "fixtures", "--compare");

        ReleaseRepository.Expect(result, 0);
        Assert.Contains("compare: every case agrees", result.Out, StringComparison.Ordinal);
        Assert.DoesNotContain(" NO", result.Out, StringComparison.Ordinal);
    }

    /// <summary>
    /// YAML 1.1 as PyYAML's safe_load types it, scalar by scalar, with PyYAML
    /// as the oracle. 2026-1-2 is here because canon first got it wrong
    /// (parallel-run.md, D-01).
    /// </summary>
    [Fact]
    public void PlainScalarsAreTypedAsPyYamlTypesThem()
    {
        string[] scalars =
        [
            "1", "\"1\"", "'1'", "0", "0123456", "0x1F", "0b101", "1_000", "-7", "+3", "190:20:30",
            "1.5", "-0.25", ".5", "yes", "No", "on", "OFF", "true", "False", "~", "null", "",
            "2026-11-03", "2026-1-2", "4801fee", "DDD-dec-84", "v0.5.0", "'a: b'", "1e10",
        ];
        string yaml = string.Join("\n", scalars.Select((s, i) => $"k{i}: {s}")) + "\n";

        ProcessResult python = Processes.Run("python3", Path.GetTempPath(),
            ["-c", "import sys, json, yaml; print(json.dumps(yaml.safe_load(sys.argv[1]), default=str, sort_keys=True))", yaml]);
        Assert.True(python.Exit == 0, python.Error);

        YamlStream stream = [];
        stream.Load(new StringReader(yaml));
        JsonNode canon = YamlJson.Convert(stream.Documents[0].RootNode)!;

        JsonObject expected = JsonNode.Parse(python.Output)!.AsObject();
        foreach ((string key, JsonNode? want) in expected)
        {
            string scalar = scalars[int.Parse(key[1..], System.Globalization.CultureInfo.InvariantCulture)];
            JsonNode? got = canon[key];
            Assert.True(JsonNode.DeepEquals(want, got) || NumericallyEqual(want, got),
                $"scalar {scalar}: PyYAML gives {want?.ToJsonString() ?? "null"}, canon gives {got?.ToJsonString() ?? "null"}");
        }
    }

    [Fact]
    public void ARepeatedClaimIdIsOneFindingAboutTheSetAsInPython() =>
        Repeated("claims", "CLAIM-DUPLICATE-ID", decisions: false, """
            format: 1
            id: DDD-fixture-77
            kind: empirical
            statement: Fixture.
            status: projected
            region: here
            falsifier: none
            changed: v0
            """);

    [Fact]
    public void ARepeatedDecisionIdIsOneFindingAboutTheSetAsInPython() =>
        Repeated("decisions", "DEC-DUPLICATE-ID", decisions: true, """
            id: DDD-dec-977
            principal: Fixture
            made: never
            resolution: accept
            basedOn: [DDD-fixture-01]
            """);

    private static void Repeated(string directory, string code, bool decisions, string text)
    {
        using Sandbox sandbox = new();
        sandbox.Write($"{directory}/a.yaml", text);
        sandbox.Write($"{directory}/b.yaml", text);

        List<Finding> canon = decisions
            ? GraphGates.Decisions(sandbox.Work, directory).Findings
            : GraphGates.Claims(sandbox.Work, directory).Findings;
        List<string> arguments = [Path.Combine(Repository(), "scripts/validate-claims.py"), Path.Combine(sandbox.Work, directory)];
        if (decisions)
        {
            arguments.Add("--decisions");
        }

        ProcessResult python = Processes.Run("python3", sandbox.Work, arguments);

        Finding finding = Assert.Single(canon);
        Assert.Equal(("*", code), (finding.File, finding.Code));
        Assert.Equal(1, python.Exit);
        Assert.Single(python.Error.Split('\n'), l => l.Contains("global: duplicate ids", StringComparison.Ordinal));
    }

    private static bool NumericallyEqual(JsonNode? a, JsonNode? b) =>
        a is JsonValue x && b is JsonValue y
        && x.GetValueKind() == JsonValueKind.Number && y.GetValueKind() == JsonValueKind.Number
        && Math.Abs(x.GetValue<double>() - y.GetValue<double>()) < 1e-12;
}
