// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

using System.Linq;
using System.Text.Json.Nodes;
using System.Text.RegularExpressions;

namespace Canon.Graph;

/// <summary>
/// Rule 1's proxy, ported from scripts/validate-claims.py's single_limb: the
/// semicolons left in a live claim's statement once whitespace is collapsed,
/// parentheticals are removed (innermost first, until none are left) and a
/// leading "RETIRED — " is dropped. A text heuristic for a human to read,
/// never a constraint, so it is code and always a warning. Retired claims are
/// exempt, as there.
/// </summary>
internal static partial class SingleLimb
{
    public static int Count(JsonNode? statement)
    {
        string text = statement switch
        {
            null => "",
            JsonValue value when value.TryGetValue(out string? scalar) => scalar,
            JsonArray array => string.Join(", ", array.Select(e => e?.ToString() ?? "None")),
            _ => statement.ToString(),
        };

        string s = string.Join(' ', Whitespace().Split(text.Trim()).Where(p => p.Length > 0));
        string previous;
        do
        {
            previous = s;
            s = Parenthetical().Replace(s, " ");
        }
        while (previous != s);

        s = Retired().Replace(s, "");
        return s.Count(c => c == ';');
    }

    [GeneratedRegex(@"\s+")]
    private static partial Regex Whitespace();

    [GeneratedRegex(@"\([^()]*\)")]
    private static partial Regex Parenthetical();

    [GeneratedRegex(@"^RETIRED — ")]
    private static partial Regex Retired();
}
