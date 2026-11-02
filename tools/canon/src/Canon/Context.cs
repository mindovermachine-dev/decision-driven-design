// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

using System.Collections.Generic;
using System.IO;
using Canon.Configuration;
using Canon.Infrastructure;

namespace Canon;

/// <summary>
/// What a command runs against: the repository, its declaration, where to
/// write, and the environment it was given. Tests construct a real one over a
/// real repository; nothing here is faked.
/// </summary>
internal sealed class Context(
    string root,
    CanonConfig config,
    TextWriter output,
    TextWriter error,
    IReadOnlyDictionary<string, string> environment)
{
    public string Root { get; } = root;

    public CanonConfig Config { get; } = config;

    public TextWriter Out { get; } = output;

    public TextWriter Err { get; } = error;

    public IReadOnlyDictionary<string, string> Environment { get; } = environment;

    public Git Git { get; } = new(root);

    public string? Env(string name) =>
        Environment.TryGetValue(name, out string? value) && value.Length > 0 ? value : null;
}
