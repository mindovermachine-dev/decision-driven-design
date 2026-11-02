// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

using System;
using System.Collections.Generic;
using System.IO;
using System.Runtime.CompilerServices;
using Canon.Infrastructure;

namespace Canon.Tests;

/// <summary>
/// Real repositories in a temporary directory: a bare repository as origin,
/// reached over the local transport, and working clones of it. Nothing is
/// faked; every git call is git.
/// </summary>
internal sealed class Sandbox : IDisposable
{
    private static readonly string GlobalConfig = Path.Combine(Path.GetTempPath(), "canon-tests-gitconfig-" + Environment.ProcessId);

    public Sandbox()
    {
        Directory = Path.Combine(Path.GetTempPath(), "canon-test-" + Guid.NewGuid().ToString("N")[..12]);
        System.IO.Directory.CreateDirectory(Directory);
        Remote = Path.Combine(Directory, "origin.git");
        Run(Directory, "init", "--quiet", "--bare", "--initial-branch=main", Remote);
        Work = Clone("work");
    }

    /// <summary>
    /// Isolates every git the tests start, canon's own included, from the
    /// machine's configuration: no system file, and a global file of the
    /// tests' own. Process-wide and set once, before any test runs.
    /// </summary>
    [ModuleInitializer]
    internal static void IsolateGit()
    {
        File.WriteAllText(GlobalConfig, """
            [user]
                name = Canon Test
                email = canon-test@example.invalid
            [init]
                defaultBranch = main
            [commit]
                gpgsign = false
            [tag]
                gpgsign = false
            [advice]
                detachedHead = false
            """);
        // Configuration passed in the environment outranks every file, so a
        // signing key the machine injects this way (GIT_CONFIG_COUNT with
        // KEY_n and VALUE_n) would sign the tests' tags with a real key.
        // Cleared, with the author and committer overrides, so the tests'
        // identity and keys are their own.
        foreach (System.Collections.DictionaryEntry entry in Environment.GetEnvironmentVariables())
        {
            string name = (string)entry.Key;
            if (name.StartsWith("GIT_CONFIG_", StringComparison.Ordinal)
                || name.StartsWith("GIT_AUTHOR_", StringComparison.Ordinal)
                || name.StartsWith("GIT_COMMITTER_", StringComparison.Ordinal))
            {
                Environment.SetEnvironmentVariable(name, null);
            }
        }

        Environment.SetEnvironmentVariable("GIT_CONFIG_NOSYSTEM", "1");
        Environment.SetEnvironmentVariable("GIT_CONFIG_GLOBAL", GlobalConfig);
        Environment.SetEnvironmentVariable("GIT_TERMINAL_PROMPT", "0");
    }

    public string Directory { get; }

    public string Remote { get; }

    public string Work { get; }

    public string Clone(string name)
    {
        string path = Path.Combine(Directory, name);
        Run(Directory, "clone", "--quiet", Remote, path);
        return path;
    }

    public static string Run(string where, params string[] arguments)
    {
        ProcessResult result = Processes.Run("git", where, arguments);
        return result.Exit == 0
            ? result.Output.Trim()
            : throw new InvalidOperationException($"git {string.Join(' ', arguments)} in {where}: {result.Error}");
    }

    public static bool Try(string where, params string[] arguments) =>
        Processes.Run("git", where, arguments).Exit == 0;

    public string Git(params string[] arguments) => Run(Work, arguments);

    public void Write(string path, string text, string? repository = null)
    {
        string full = Path.Combine(repository ?? Work, path);
        System.IO.Directory.CreateDirectory(Path.GetDirectoryName(full)!);
        File.WriteAllText(full, text);
    }

    public string Read(string path, string? repository = null) =>
        File.ReadAllText(Path.Combine(repository ?? Work, path));

    public string Commit(string message, string? repository = null)
    {
        string where = repository ?? Work;
        Run(where, "add", "-A");
        Run(where, "commit", "--quiet", "--allow-empty", "-m", message);
        return Run(where, "rev-parse", "HEAD");
    }

    /// <summary>An ed25519 key made with ssh-keygen, set as this clone's signing key.</summary>
    public string UseSigningKey(string? repository = null)
    {
        string where = repository ?? Work;
        string key = Path.Combine(Directory, "signing-key-" + Guid.NewGuid().ToString("N")[..8]);
        ProcessResult made = Processes.Run("ssh-keygen", Directory, ["-q", "-t", "ed25519", "-N", "", "-C", "canon-test", "-f", key]);
        if (made.Exit != 0)
        {
            throw new InvalidOperationException("ssh-keygen: " + made.Error);
        }

        Run(where, "config", "gpg.format", "ssh");
        Run(where, "config", "user.signingkey", key);
        return key;
    }

    public (int Exit, string Out, string Err) Canon(IReadOnlyDictionary<string, string> environment, params string[] arguments) =>
        CanonIn(Work, environment, arguments);

    public static (int Exit, string Out, string Err) CanonIn(string where, IReadOnlyDictionary<string, string> environment, params string[] arguments)
    {
        using StringWriter output = new();
        using StringWriter error = new();
        int exit = Cli.Run(arguments, output, error, where, environment);
        return (exit, output.ToString(), error.ToString());
    }

    public void Dispose()
    {
        try
        {
            foreach (string file in System.IO.Directory.EnumerateFiles(Directory, "*", SearchOption.AllDirectories))
            {
                File.SetAttributes(file, FileAttributes.Normal);
            }

            System.IO.Directory.Delete(Directory, recursive: true);
        }
        catch (IOException)
        {
            // A leftover temp directory is not a test failure.
        }
    }
}
