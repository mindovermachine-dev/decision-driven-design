// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

using System.Collections.Generic;
using System.ComponentModel;
using System.Diagnostics;
using System.Threading.Tasks;

namespace Canon.Infrastructure;

/// <summary>The outcome of a child process: its exit code and both streams.</summary>
internal sealed record ProcessResult(int Exit, string Output, string Error);

/// <summary>
/// Runs child processes with an argument list, never a shell string, so no
/// argument is ever re-parsed. Exit 127 means the program could not be started.
/// </summary>
internal static class Processes
{
    public const int NotFound = 127;

    public static ProcessResult Run(
        string file,
        string workingDirectory,
        IEnumerable<string> arguments,
        IReadOnlyDictionary<string, string>? environment = null)
    {
        ProcessStartInfo start = new()
        {
            FileName = file,
            WorkingDirectory = workingDirectory,
            RedirectStandardOutput = true,
            RedirectStandardError = true,
            RedirectStandardInput = true,
            UseShellExecute = false,
        };

        foreach (string argument in arguments)
        {
            start.ArgumentList.Add(argument);
        }

        if (environment is not null)
        {
            foreach (KeyValuePair<string, string> pair in environment)
            {
                start.Environment[pair.Key] = pair.Value;
            }
        }

        try
        {
            using Process process = Process.Start(start)
                ?? throw new CanonException($"could not start {file}");
            process.StandardInput.Close();
            Task<string> error = process.StandardError.ReadToEndAsync();
            string output = process.StandardOutput.ReadToEnd();
            process.WaitForExit();
            return new ProcessResult(process.ExitCode, output, error.Result);
        }
        catch (Win32Exception)
        {
            return new ProcessResult(NotFound, "", $"{file}: not found");
        }
    }
}
