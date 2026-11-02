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
/// A real HTTP/1.1 server on 127.0.0.1 speaking the two shapes of GitHub's
/// REST API canon uses: GET /repos/{o}/{r}/releases (paged) and POST
/// /repos/{o}/{r}/releases. It is the one stand-in in the tests, at the one
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

        (int status, string json) = (method, path == releases) switch
        {
            ("GET", true) => (200, Page(page)),
            ("POST", true) => Create(new string(body, 0, read)),
            _ => (404, """{"message":"Not Found"}"""),
        };

        byte[] bytes = Encoding.UTF8.GetBytes(json);
        string head = $"HTTP/1.1 {status} {(status == 404 ? "Not Found" : status == 201 ? "Created" : "OK")}\r\n"
            + "Content-Type: application/json\r\n"
            + $"Content-Length: {bytes.Length}\r\n"
            + "Connection: close\r\n\r\n";
        stream.Write(Encoding.ASCII.GetBytes(head));
        stream.Write(bytes);
        stream.Flush();
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
