// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

using System;
using System.Globalization;
using System.Numerics;
using System.Text.Json.Nodes;
using System.Text.RegularExpressions;
using YamlDotNet.Core;
using YamlDotNet.RepresentationModel;

namespace Canon.Graph;

/// <summary>
/// YAML to JSON, typing plain scalars as PyYAML's safe_load does (YAML 1.1's
/// resolver), because the Python validators judge the values PyYAML produces
/// and the parallel run compares verdicts (DDD-dec-102). A quoted scalar is
/// always a string. A plain one is, in PyYAML's order: null, bool (including
/// yes/no/on/off), int (decimal, 0b, 0x, a leading 0 for octal, sexagesimal,
/// with underscores), float, else a string. Dates are left as written: the
/// only date PyYAML's implicit resolver accepts without a time is
/// yyyy-mm-dd with two-digit month and day, whose str() is the text itself.
/// (2026-1-2 is a string to PyYAML; canon first read it as a date, which the
/// parallel run caught: tools/canon/parallel-run.md, D-01.) Full timestamps
/// stay strings: no rule here reads one as a time.
/// </summary>
internal static partial class YamlJson
{
    /// <summary>The JSON value of a node; JSON null for a YAML null.</summary>
    public static JsonNode? Convert(YamlNode node) => node switch
    {
        YamlMappingNode mapping => Mapping(mapping),
        YamlSequenceNode sequence => Sequence(sequence),
        YamlScalarNode scalar => Scalar(scalar),
        _ => null,
    };

    private static JsonObject Mapping(YamlMappingNode mapping)
    {
        JsonObject result = [];
        foreach ((YamlNode key, YamlNode value) in mapping.Children)
        {
            string name = key is YamlScalarNode k ? k.Value ?? "" : key.ToString();
            result[name] = Convert(value);
        }

        return result;
    }

    private static JsonArray Sequence(YamlSequenceNode sequence)
    {
        JsonArray result = [];
        foreach (YamlNode item in sequence.Children)
        {
            result.Add(Convert(item));
        }

        return result;
    }

    private static JsonNode? Scalar(YamlScalarNode scalar)
    {
        string text = scalar.Value ?? "";
        if (scalar.Style is not (ScalarStyle.Plain or ScalarStyle.Any) || scalar.Tag.ToString() == "tag:yaml.org,2002:str")
        {
            return JsonValue.Create(text);
        }

        if (NullPattern().IsMatch(text))
        {
            return null;
        }

        if (TruePattern().IsMatch(text))
        {
            return JsonValue.Create(true);
        }

        if (FalsePattern().IsMatch(text))
        {
            return JsonValue.Create(false);
        }

        if (Integer(text) is { } integer)
        {
            return integer >= long.MinValue && integer <= long.MaxValue
                ? JsonValue.Create((long)integer)
                : JsonNode.Parse(integer.ToString(CultureInfo.InvariantCulture));
        }

        if (FloatPattern().IsMatch(text) && double.TryParse(text.Replace("_", "", StringComparison.Ordinal), NumberStyles.Float, CultureInfo.InvariantCulture, out double number) && double.IsFinite(number))
        {
            return JsonValue.Create(number);
        }

        return JsonValue.Create(text);
    }

    /// <summary>YAML 1.1's int, as PyYAML resolves and constructs it.</summary>
    private static BigInteger? Integer(string text)
    {
        if (!IntPattern().IsMatch(text))
        {
            return null;
        }

        string value = text.Replace("_", "", StringComparison.Ordinal);
        int sign = 1;
        if (value.StartsWith('-'))
        {
            sign = -1;
            value = value[1..];
        }
        else if (value.StartsWith('+'))
        {
            value = value[1..];
        }

        BigInteger result;
        if (value == "0")
        {
            result = BigInteger.Zero;
        }
        else if (value.StartsWith("0b", StringComparison.Ordinal))
        {
            result = Radix(value[2..], 2);
        }
        else if (value.StartsWith("0x", StringComparison.Ordinal))
        {
            result = Radix(value[2..], 16);
        }
        else if (value.StartsWith('0'))
        {
            result = Radix(value[1..], 8);
        }
        else if (value.Contains(':', StringComparison.Ordinal))
        {
            result = BigInteger.Zero;
            foreach (string part in value.Split(':'))
            {
                result = (result * 60) + BigInteger.Parse(part, CultureInfo.InvariantCulture);
            }
        }
        else
        {
            result = BigInteger.Parse(value, CultureInfo.InvariantCulture);
        }

        return sign * result;
    }

    private static BigInteger Radix(string digits, int radix)
    {
        BigInteger result = BigInteger.Zero;
        foreach (char c in digits)
        {
            result = (result * radix) + System.Convert.ToInt32(c.ToString(), 16);
        }

        return result;
    }

    [GeneratedRegex(@"\A(~|null|Null|NULL|)\z")]
    private static partial Regex NullPattern();

    [GeneratedRegex(@"\A(yes|Yes|YES|true|True|TRUE|on|On|ON)\z")]
    private static partial Regex TruePattern();

    [GeneratedRegex(@"\A(no|No|NO|false|False|FALSE|off|Off|OFF)\z")]
    private static partial Regex FalsePattern();

    [GeneratedRegex(@"\A([-+]?0b[0-1_]+|[-+]?0[0-7_]+|[-+]?(0|[1-9][0-9_]*)|[-+]?0x[0-9a-fA-F_]+|[-+]?[1-9][0-9_]*(:[0-5]?[0-9])+)\z")]
    private static partial Regex IntPattern();

    [GeneratedRegex(@"\A([-+]?([0-9][0-9_]*)?\.[0-9.]*([eE][-+][0-9]+)?)\z")]
    private static partial Regex FloatPattern();
}
