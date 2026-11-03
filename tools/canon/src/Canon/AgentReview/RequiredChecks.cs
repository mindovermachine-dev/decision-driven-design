// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using YamlDotNet.Core;
using YamlDotNet.RepresentationModel;

namespace Canon.AgentReview;

/// <summary>
/// The status checks the default branch's rulesets require, read from
/// .github/repo-standard.yaml (DDD-dec-108): each context with the app
/// (integration id) it is pinned to, if any. canon reads main's copy, as
/// Varve's agent-review.cs reads the pin from main's file.
/// </summary>
internal static class RequiredChecks
{
    public const string DefaultPath = ".github/repo-standard.yaml";

    /// <summary>Every required context on a ruleset that covers ~DEFAULT_BRANCH, with its pinned app.</summary>
    public static IReadOnlyDictionary<string, long?> OnTrunk(string? yaml)
    {
        Dictionary<string, long?> checks = new(StringComparer.Ordinal);
        if (string.IsNullOrWhiteSpace(yaml))
        {
            return checks;
        }

        YamlStream stream = [];
        try
        {
            stream.Load(new StringReader(yaml));
        }
        catch (YamlException)
        {
            return checks;
        }

        if (stream.Documents.Count == 0
            || stream.Documents[0].RootNode is not YamlMappingNode root
            || !root.Children.TryGetValue(new YamlScalarNode("rulesets"), out YamlNode? rulesets)
            || rulesets is not YamlSequenceNode list)
        {
            return checks;
        }

        foreach (YamlNode node in list)
        {
            if (node is not YamlMappingNode ruleset
                || Scalar(ruleset, "target") != "branch"
                || Scalar(ruleset, "enforcement") != "active"
                || !Includes(ruleset, "~DEFAULT_BRANCH")
                || Child(ruleset, "rules") is not YamlSequenceNode rules)
            {
                continue;
            }

            foreach (YamlNode r in rules)
            {
                if (r is not YamlMappingNode rule || Scalar(rule, "type") != "required_status_checks"
                    || Child(rule, "parameters") is not YamlMappingNode parameters
                    || Child(parameters, "required_status_checks") is not YamlSequenceNode required)
                {
                    continue;
                }

                foreach (YamlNode c in required)
                {
                    if (c is YamlMappingNode check && Scalar(check, "context") is { } context)
                    {
                        checks[context] = long.TryParse(Scalar(check, "integration_id"), NumberStyles.None, CultureInfo.InvariantCulture, out long id)
                            ? id
                            : null;
                    }
                }
            }
        }

        return checks;
    }

    private static bool Includes(YamlMappingNode ruleset, string pattern) =>
        Child(ruleset, "conditions") is YamlMappingNode conditions
        && Child(conditions, "ref_name") is YamlMappingNode refName
        && Child(refName, "include") is YamlSequenceNode include
        && include.Children.Contains(new YamlScalarNode(pattern));

    private static YamlNode? Child(YamlMappingNode mapping, string key) =>
        mapping.Children.TryGetValue(new YamlScalarNode(key), out YamlNode? value) ? value : null;

    private static string? Scalar(YamlMappingNode mapping, string key) =>
        Child(mapping, key) is YamlScalarNode scalar ? scalar.Value : null;
}
