// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

using System;

namespace Canon.Infrastructure;

/// <summary>
/// canon could not run: a tool is missing, git failed where it must not, a
/// file could not be read. Mapped to exit code 2. A refusal is not an
/// exception; commands return <see cref="Exit.Refused"/> for that.
/// </summary>
internal sealed class CanonException : Exception
{
    public CanonException(string message)
        : base(message)
    {
    }

    public CanonException(string message, Exception inner)
        : base(message, inner)
    {
    }

    public CanonException()
    {
    }
}
