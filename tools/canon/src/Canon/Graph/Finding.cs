// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

namespace Canon.Graph;

/// <summary>
/// One finding of a gate: the file it is about (the repository-relative path,
/// or "*" for a finding about the set, such as a duplicate id), the rule code
/// (DESIGN.md §5.4), whether it is a warning, and the message.
/// </summary>
internal sealed record Finding(string File, string Code, bool Warning, string Message)
{
    public override string ToString() => $"{File}: [{Code}]{(Warning ? " (warning)" : "")} {Message}";
}
