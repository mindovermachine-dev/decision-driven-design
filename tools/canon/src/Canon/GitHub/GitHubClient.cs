// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

using System;
using System.Collections.Generic;
using System.Net;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Text.Json.Nodes;
using Canon.Infrastructure;

namespace Canon.GitHub;

/// <summary>
/// The two GitHub REST calls canon makes: list a repository's releases, and
/// create one. The base URL is a parameter (CANON_GITHUB_API, default
/// https://api.github.com), which is how the tests reach a real HTTP server
/// speaking the same shape. The token is GH_TOKEN; it is sent as a header and
/// never written anywhere.
/// </summary>
internal sealed class GitHubClient : IDisposable
{
    public const string DefaultApi = "https://api.github.com";

    private readonly HttpClient http;
    private readonly string repository;
    private readonly bool hasToken;

    public GitHubClient(Uri api, string repository, string? token)
    {
        this.repository = repository;
        hasToken = token is not null;
        http = new HttpClient { BaseAddress = new Uri(api.ToString().TrimEnd('/') + "/"), Timeout = TimeSpan.FromSeconds(30) };
        http.DefaultRequestHeaders.UserAgent.Add(new ProductInfoHeaderValue("canon", "0.1.0"));
        http.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/vnd.github+json"));
        http.DefaultRequestHeaders.Add("X-GitHub-Api-Version", "2022-11-28");
        if (token is not null)
        {
            http.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", token);
        }
    }

    public bool HasToken => hasToken;

    /// <summary>
    /// The release whose tag or name is <paramref name="tag"/>, drafts included
    /// when the token can see them. Listed rather than fetched by tag, because
    /// the by-tag endpoint does not return drafts, and a draft Release is one of
    /// the places a version can already exist.
    /// </summary>
    public JsonObject? FindRelease(string tag)
    {
        for (int page = 1; page <= 100; page++)
        {
            using HttpResponseMessage response = Send(HttpMethod.Get, $"repos/{repository}/releases?per_page=100&page={page}", null);
            if (response.StatusCode != HttpStatusCode.OK)
            {
                throw new CanonException($"GitHub: listing releases of {repository} answered {(int)response.StatusCode}");
            }

            if (JsonNode.Parse(response.Content.ReadAsStringAsync().Result) is not JsonArray releases || releases.Count == 0)
            {
                return null;
            }

            foreach (JsonNode? node in releases)
            {
                if (node is JsonObject release
                    && (release["tag_name"]?.GetValue<string>() == tag || release["name"]?.GetValue<string>() == tag))
                {
                    return release;
                }
            }
        }

        throw new CanonException($"GitHub: more than 10000 releases in {repository}; refusing to guess");
    }

    public JsonObject CreateRelease(string tag, string name, string body, bool prerelease)
    {
        JsonObject request = new()
        {
            ["tag_name"] = tag,
            ["name"] = name,
            ["body"] = body,
            ["draft"] = false,
            ["prerelease"] = prerelease,
        };

        using HttpResponseMessage response = Send(HttpMethod.Post, $"repos/{repository}/releases", request.ToJsonString());
        string text = response.Content.ReadAsStringAsync().Result;
        return response.StatusCode == HttpStatusCode.Created && JsonNode.Parse(text) is JsonObject created
            ? created
            : throw new CanonException($"GitHub: creating the release {tag} answered {(int)response.StatusCode}");
    }

    private HttpResponseMessage Send(HttpMethod method, string path, string? json)
    {
        using HttpRequestMessage request = new(method, path);
        if (json is not null)
        {
            request.Content = new StringContent(json, Encoding.UTF8, "application/json");
        }

        try
        {
            return http.Send(request);
        }
        catch (HttpRequestException exception)
        {
            throw new CanonException($"GitHub could not be reached: {exception.Message}", exception);
        }
        catch (System.Threading.Tasks.TaskCanceledException exception)
        {
            throw new CanonException($"GitHub did not answer in time: {exception.Message}", exception);
        }
    }

    public void Dispose() => http.Dispose();

    /// <summary>owner/name from a remote URL (https or ssh), or null.</summary>
    public static string? RepositoryFromRemote(string url)
    {
        string trimmed = url.Trim();
        int at = trimmed.IndexOf("github.com", StringComparison.OrdinalIgnoreCase);
        if (at < 0)
        {
            return null;
        }

        string rest = trimmed[(at + "github.com".Length)..].TrimStart(':', '/');
        if (rest.EndsWith(".git", StringComparison.Ordinal))
        {
            rest = rest[..^4];
        }

        string[] parts = rest.Split('/', StringSplitOptions.RemoveEmptyEntries);
        return parts.Length >= 2 ? parts[0] + "/" + parts[1] : null;
    }

    internal static IReadOnlyList<string> Describe(JsonObject release) =>
    [
        $"tag {release["tag_name"]?.GetValue<string>() ?? "?"}",
        release["draft"]?.GetValue<bool>() == true ? "draft" : "published",
    ];
}
