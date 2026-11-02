// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

namespace Canon;

/// <summary>Exit codes, as Varve's eng/ scripts use them.</summary>
internal static class Exit
{
    /// <summary>Conformant, or done.</summary>
    public const int Ok = 0;

    /// <summary>Refused: a check found a violation, or a precondition failed.</summary>
    public const int Refused = 1;

    /// <summary>Could not run.</summary>
    public const int CouldNotRun = 2;
}
