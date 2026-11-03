// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Text.Json.Nodes;
using System.Threading;
using System.Web;

namespace Canon.Tests;

/// <summary>
/// A real HTTP/1.1 server on 127.0.0.1 speaking the shapes of GitHub's REST
/// API canon uses: GET and POST /repos/{o}/{r}/releases; and for agent review
/// (DDD-dec-109), a pull request, its commits and conversation comments, the
/// pull requests and check runs of a commit, and POST or PATCH of a check run,
/// attributed to the app whose token made the call (<see cref="TokenApps"/>),
/// as GitHub attributes it. It is the one stand-in in the tests, at the one
/// boundary canon cannot reproduce locally (DESIGN.md §3.4). It holds state and
/// answers requests; it asserts nothing about how it is called.
///
/// It listens on port 0, so the operating system assigns the port while the
/// socket is bound and no two servers can race for one. Each connection
/// carries one request and is closed after the response.
/// </summary>
internal sealed class GitHubServer : IDisposable
{
    private readonly TcpListener listener = new(IPAddress.Loopback, 0);
    private readonly Thread thread;

    public GitHubServer(string repository)
    {
        Repository = repository;
        listener.Start();
        Url = $"http://127.0.0.1:{((IPEndPoint)listener.LocalEndpoint).Port}";
        thread = new Thread(Serve) { IsBackground = true };
        thread.Start();
    }

    public string Repository { get; }

    public string Url { get; }

    /// <summary>The releases the repository has, as GitHub returns them.</summary>
    public ConcurrentQueue<JsonObject> Releases { get; } = new();

    /// <summary>Every request's method, path and authorization header, in order.</summary>
    public ConcurrentQueue<(string Method, string Path, string? Authorization)> Requests { get; } = new();

    /// <summary>Pull requests by number, as GET pulls/{n} returns them.</summary>
    public ConcurrentDictionary<int, JsonObject> Pulls { get; } = new();

    /// <summary>Each pull request's commits, as GET pulls/{n}/commits returns them.</summary>
    public ConcurrentDictionary<int, JsonArray> PullCommits { get; } = new();

    /// <summary>Each pull request's conversation comments, as GET issues/{n}/comments returns them.</summary>
    public ConcurrentDictionary<int, JsonArray> Comments { get; } = new();

    /// <summary>Every check run on any commit, as GitHub holds them.</summary>
    public ConcurrentQueue<JsonObject> CheckRuns { get; } = new();

    /// <summary>The app each bearer token belongs to: a run it posts is that app's.</summary>
    public ConcurrentDictionary<string, long> TokenApps { get; } = new();

    private int nextRun = 1000;

    public void AddPullRequest(int number, string head, params (string Message, string Email)[] commits)
    {
        Pulls[number] = new JsonObject
        {
            ["number"] = number,
            ["head"] = new JsonObject { ["sha"] = head },
            ["user"] = new JsonObject { ["login"] = "Hafeok", ["id"] = 2194785 },
        };
        JsonArray list = [];
        foreach ((string message, string email) in commits)
        {
            list.Add(new JsonObject
            {
                ["sha"] = head,
                ["commit"] = new JsonObject { ["message"] = message, ["author"] = new JsonObject { ["email"] = email } },
                ["parents"] = new JsonArray(new JsonObject { ["sha"] = "0000000000000000000000000000000000000000" }),
            });
        }

        PullCommits[number] = list;
        Comments.TryAdd(number, []);
    }

    /// <summary>A conversation comment; <paramref name="app"/> is the app GitHub records as having made it.</summary>
    public void AddComment(int number, string login, long account, string body, long? app = null, bool edited = false)
    {
        Comments.GetOrAdd(number, _ => []).Add(new JsonObject
        {
            ["id"] = Interlocked.Increment(ref nextRun),
            ["user"] = new JsonObject { ["login"] = login, ["id"] = account },
            ["body"] = body,
            ["created_at"] = "2026-11-03T10:00:00Z",
            ["updated_at"] = edited ? "2026-11-03T10:05:00Z" : "2026-11-03T10:00:00Z",
            ["performed_via_github_app"] = app is long id ? new JsonObject { ["id"] = id, ["slug"] = "app-" + id.ToString(CultureInfo.InvariantCulture) } : null,
        });
    }

    /// <summary>A check run on a commit, as if <paramref name="app"/> had posted it.</summary>
    public void AddCheckRun(string head, string name, long app, string conclusion)
    {
        CheckRuns.Enqueue(new JsonObject
        {
            ["id"] = Interlocked.Increment(ref nextRun),
            ["name"] = name,
            ["head_sha"] = head,
            ["status"] = "completed",
            ["conclusion"] = conclusion,
            ["app"] = new JsonObject { ["id"] = app },
        });
    }

    public void AddRelease(string tag, bool draft)
    {
        Releases.Enqueue(new JsonObject
        {
            ["tag_name"] = tag,
            ["name"] = tag,
            ["draft"] = draft,
            ["prerelease"] = false,
        });
    }

    /// <summary>A URL on which nothing listens: GitHub unreachable. Port 1 is never bound by these tests.</summary>
    public static string Unreachable() => "http://127.0.0.1:1";

    public IReadOnlyDictionary<string, string> Environment(string token = "test-token") =>
        new Dictionary<string, string> { ["CANON_GITHUB_API"] = Url, ["GH_TOKEN"] = token };

    private void Serve()
    {
        while (true)
        {
            TcpClient client;
            try
            {
                client = listener.AcceptTcpClient();
            }
            catch (SocketException)
            {
                return;
            }
            catch (ObjectDisposedException)
            {
                return;
            }
            catch (InvalidOperationException)
            {
                // Stopped between the loop's turns: Dispose ran.
                return;
            }

            using (client)
            {
                Handle(client.GetStream());
            }
        }
    }

    private void Handle(NetworkStream stream)
    {
        using StreamReader reader = new(stream, Encoding.ASCII, leaveOpen: true);
        string[] requestLine = (reader.ReadLine() ?? "").Split(' ');
        if (requestLine.Length < 2)
        {
            return;
        }

        string method = requestLine[0];
        string target = requestLine[1];
        string? authorization = null;
        int length = 0;
        for (string? line = reader.ReadLine(); !string.IsNullOrEmpty(line); line = reader.ReadLine())
        {
            int colon = line.IndexOf(':', StringComparison.Ordinal);
            string name = line[..colon].Trim();
            string value = line[(colon + 1)..].Trim();
            if (name.Equals("Authorization", StringComparison.OrdinalIgnoreCase))
            {
                authorization = value;
            }
            else if (name.Equals("Content-Length", StringComparison.OrdinalIgnoreCase))
            {
                length = int.Parse(value, CultureInfo.InvariantCulture);
            }
        }

        char[] body = new char[length];
        int read = 0;
        while (read < length)
        {
            int n = reader.Read(body, read, length - read);
            if (n == 0)
            {
                break;
            }

            read += n;
        }

        Requests.Enqueue((method, target, authorization));
        int query = target.IndexOf('?', StringComparison.Ordinal);
        string path = query < 0 ? target : target[..query];
        string page = query < 0 ? "1" : HttpUtility.ParseQueryString(target[(query + 1)..])["page"] ?? "1";
        string releases = $"/repos/{Repository}/releases";

        string query_ = query < 0 ? "" : target[(query + 1)..];
        (int status, string json) = (method, path == releases) switch
        {
            ("GET", true) => (200, Page(page)),
            ("POST", true) => Create(new string(body, 0, read)),
            _ when path.StartsWith($"/repos/{Repository}/", StringComparison.Ordinal)
                => Route(method, path[$"/repos/{Repository}/".Length..], page, query_, new string(body, 0, read), authorization),
            _ => (404, """{"message":"Not Found"}"""),
        };

        byte[] bytes = Encoding.UTF8.GetBytes(json);
        string head = $"HTTP/1.1 {status} {status switch { 404 => "Not Found", 403 => "Forbidden", 201 => "Created", _ => "OK" }}\r\n"
            + "Content-Type: application/json\r\n"
            + $"Content-Length: {bytes.Length}\r\n"
            + "Connection: close\r\n\r\n";
        stream.Write(Encoding.ASCII.GetBytes(head));
        stream.Write(bytes);
        stream.Flush();
    }

    private (int, string) Route(string method, string path, string page, string query, string body, string? authorization)
    {
        const string NotFound = """{"message":"Not Found"}""";
        string[] parts = path.TrimStart('/').Split('/');
        int number = parts.Length > 1 && int.TryParse(parts[1], NumberStyles.None, CultureInfo.InvariantCulture, out int n) ? n : -1;
        switch (method, parts)
        {
            case ("GET", ["pulls", _]):
                return Pulls.TryGetValue(number, out JsonObject? pull) ? (200, pull.ToJsonString()) : (404, NotFound);
            case ("GET", ["pulls", _, "commits"]):
                return (200, PageOf(PullCommits.TryGetValue(number, out JsonArray? commits) ? commits : [], page));
            case ("GET", ["issues", _, "comments"]):
                return (200, PageOf(Comments.TryGetValue(number, out JsonArray? comments) ? comments : [], page));
            case ("GET", ["commits", string sha, "pulls"]):
                JsonArray heads = [];
                foreach (JsonObject candidate in Pulls.Values)
                {
                    if (candidate["head"]?["sha"]?.GetValue<string>() == sha)
                    {
                        heads.Add(candidate.DeepClone());
                    }
                }

                return (200, PageOf(heads, page));
            case ("GET", ["commits", string sha, "check-runs"]):
                string? name = HttpUtility.ParseQueryString(query)["check_name"];
                JsonArray runs = [];
                foreach (JsonObject run in CheckRuns)
                {
                    if (run["head_sha"]?.GetValue<string>() == sha && (name is null || run["name"]?.GetValue<string>() == name))
                    {
                        runs.Add(run.DeepClone());
                    }
                }

                return (200, new JsonObject { ["total_count"] = runs.Count, ["check_runs"] = runs }.ToJsonString());
            case ("POST", ["check-runs"]):
                JsonObject created = (JsonObject)JsonNode.Parse(body)!;
                created["id"] = Interlocked.Increment(ref nextRun);
                created["app"] = new JsonObject { ["id"] = AppOf(authorization) };
                CheckRuns.Enqueue(created);
                return (201, created.ToJsonString());
            case ("PATCH", ["check-runs", _]):
                foreach (JsonObject run in CheckRuns)
                {
                    if (run["id"]?.GetValue<int>() == number)
                    {
                        // An app can update only its own check run, as on GitHub.
                        if (run["app"]?["id"]?.GetValue<long>() != AppOf(authorization))
                        {
                            return (403, """{"message":"Forbidden"}""");
                        }

                        foreach ((string key, JsonNode? value) in (JsonObject)JsonNode.Parse(body)!)
                        {
                            run[key] = value?.DeepClone();
                        }

                        return (200, run.ToJsonString());
                    }
                }

                return (404, NotFound);
            default:
                return (404, NotFound);
        }
    }

    private long AppOf(string? authorization) =>
        authorization is not null && authorization.StartsWith("Bearer ", StringComparison.Ordinal)
            && TokenApps.TryGetValue(authorization["Bearer ".Length..], out long app) ? app : 0;

    private static string PageOf(JsonArray items, string page)
    {
        JsonArray body = [];
        if (page == "1")
        {
            foreach (JsonNode? item in items)
            {
                body.Add(item?.DeepClone());
            }
        }

        return body.ToJsonString();
    }

    private string Page(string page)
    {
        JsonArray body = [];
        if (page == "1")
        {
            foreach (JsonObject release in Releases)
            {
                body.Add(release.DeepClone());
            }
        }

        return body.ToJsonString();
    }

    private (int, string) Create(string json)
    {
        JsonObject created = (JsonObject)JsonNode.Parse(json)!;
        Releases.Enqueue(created);
        return (201, created.ToJsonString());
    }

    public void Dispose()
    {
        listener.Stop();
        listener.Dispose();
        thread.Join(TimeSpan.FromSeconds(5));
    }
}
