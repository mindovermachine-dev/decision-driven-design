// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

using System;
using System.Collections;
using System.Collections.Generic;
using Canon;

Dictionary<string, string> environment = [];
foreach (DictionaryEntry entry in Environment.GetEnvironmentVariables())
{
    environment[(string)entry.Key] = (string?)entry.Value ?? "";
}

return Cli.Run(args, Console.Out, Console.Error, Environment.CurrentDirectory, environment);
