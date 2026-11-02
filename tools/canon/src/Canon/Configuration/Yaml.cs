// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using Canon.Infrastructure;
using YamlDotNet.Core;
using YamlDotNet.RepresentationModel;

namespace Canon.Configuration;

/// <summary>
/// YAML through the representation model only: no reflection, no type
/// binding, and so no surprise from a scalar YAML reads as a date or a number.
/// Every value comes back as the text the file holds.
/// </summary>
internal static class Yaml
{
    public static YamlMappingNode LoadMapping(string text, string where)
    {
        YamlStream stream = [];
        try
        {
            stream.Load(new StringReader(text));
        }
        catch (YamlException exception)
        {
            throw new CanonException($"{where}: not valid YAML: {exception.Message}", exception);
        }

        return stream.Documents.Count == 1 && stream.Documents[0].RootNode is YamlMappingNode mapping
            ? mapping
            : throw new CanonException($"{where}: not a YAML mapping");
    }

    public static string? Scalar(YamlMappingNode mapping, string key) =>
        mapping.Children.TryGetValue(new YamlScalarNode(key), out YamlNode? node) && node is YamlScalarNode scalar
            ? scalar.Value
            : null;

    public static YamlMappingNode? Mapping(YamlMappingNode mapping, string key) =>
        mapping.Children.TryGetValue(new YamlScalarNode(key), out YamlNode? node) ? node as YamlMappingNode : null;

    public static IReadOnlyList<string>? Sequence(YamlMappingNode mapping, string key)
    {
        if (!mapping.Children.TryGetValue(new YamlScalarNode(key), out YamlNode? node))
        {
            return null;
        }

        return node is YamlSequenceNode sequence
            ? sequence.Children.OfType<YamlScalarNode>().Select(s => s.Value ?? "").ToList()
            : Array.Empty<string>();
    }

    public static bool Has(YamlMappingNode mapping, string key) =>
        mapping.Children.ContainsKey(new YamlScalarNode(key));
}
