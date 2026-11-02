// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

using System.Collections.Generic;
using System.Text.RegularExpressions;
using Canon.Configuration;
using YamlDotNet.RepresentationModel;

namespace Canon.Releases;

/// <summary>
/// A release descriptor, releases/&lt;version&gt;.yaml (spec/release-format.md).
/// Read as text values; validation here is structural, enough for canon's
/// operations to refuse a descriptor they cannot act on. The full rules are
/// the releases gate's (scripts/validate-releases.py until Gate 3).
/// </summary>
internal sealed partial record Descriptor(
    string Path,
    string? Format,
    string? Version,
    string? Title,
    string? Date,
    string? Commit,
    string? RatifiedHead,
    bool Prerelease,
    IReadOnlyList<string> Basis,
    string? Summary)
{
    public static Descriptor Parse(string path, string text)
    {
        YamlMappingNode yaml = Yaml.LoadMapping(text, path);
        return new Descriptor(
            path,
            Yaml.Scalar(yaml, "format"),
            Yaml.Scalar(yaml, "version"),
            Yaml.Scalar(yaml, "title"),
            Yaml.Scalar(yaml, "date"),
            Yaml.Scalar(yaml, "commit"),
            Yaml.Scalar(yaml, "ratified_head"),
            Yaml.Scalar(yaml, "prerelease") == "true",
            Yaml.Sequence(yaml, "basis") ?? [],
            Yaml.Scalar(yaml, "summary"));
    }

    /// <summary>What is wrong with it for a release operation; empty when nothing is.</summary>
    public IReadOnlyList<string> Problems(string expectedVersion)
    {
        List<string> problems = [];
        if (Format is not ("1" or "2"))
        {
            problems.Add($"format missing or unsupported: {Format ?? "(none)"}");
        }

        if (Version is null || !VersionPattern().IsMatch(Version))
        {
            problems.Add($"version missing or not v<major>.<minor>.<patch>: {Version ?? "(none)"}");
        }
        else if (Version != expectedVersion)
        {
            problems.Add($"version {Version} disagrees with the file name ({expectedVersion})");
        }

        if (string.IsNullOrWhiteSpace(Title) || Title.Contains('\n', System.StringComparison.Ordinal))
        {
            problems.Add("title missing or not one line");
        }

        if (Basis.Count == 0)
        {
            problems.Add("basis missing or empty");
        }

        if (string.IsNullOrWhiteSpace(Summary))
        {
            problems.Add("summary missing");
        }

        if (Commit is not null && !ShaPattern().IsMatch(Commit))
        {
            problems.Add($"commit is not a hex sha of 7-40 characters: {Commit}");
        }

        if (Format == "2" && (RatifiedHead is null || !ShaPattern().IsMatch(RatifiedHead)))
        {
            problems.Add($"ratified_head missing or not a hex sha of 7-40 characters: {RatifiedHead ?? "(none)"}");
        }

        return problems;
    }

    [GeneratedRegex(@"\Av[0-9]+\.[0-9]+\.[0-9]+\z")]
    internal static partial Regex VersionPattern();

    [GeneratedRegex(@"\A[0-9a-f]{7,40}\z")]
    internal static partial Regex ShaPattern();
}
