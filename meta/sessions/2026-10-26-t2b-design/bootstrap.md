
## Supplement at GATE 0 — the Varve bases (2026-10-26, after the arrival commit)

This section supersedes the two **[OPEN]** rows for the Varve bases and arrival gaps 1 and 3
above. Those lines stay as written; this section records what replaced them.

Emil supplied the owner at GATE 0: `Hafeok`. Both repositories are public and were cloned
read-only. Nothing in either was written.

| Parameter | Value |
|---|---|
| Varve repo | github.com/Hafeok/varve |
| Varve base | `8b0d435` (`8b0d43538e4a4fdfeb11b27ca54ad9e8a86f5de3`) — head of `main` at arrival, 2026-10-26 12:12 UTC; tag `v0.1.0-preview.14` points at it |
| varve-demo repo | github.com/Hafeok/varve-demo |
| varve-demo base | `47b941a` (`47b941a2a0c65541fc0e6bb711f7320e98f838bf`) — head of the default branch `claude/festive-keller-huyqzn` at arrival |
| varve-demo `main` | `5755988` — the initial commit only. All 30 commits of record sit on the unmerged default branch |
| Push access | Confirmed: the session branch was pushed to downstream origin. Arrival gap 3 is closed |

Two observations, reported at GATE 1 item 4 and not ruled here:
- varve-demo's last two commits (`f8ba707`, `47b941a`) are dated 2026-10-26, the day of the
  ruling. From their messages they accept ADRs 0001 to 0009 and file a session record. They are
  decision acts, not step builds.
- The base is a branch head, not `main`. Which ref the test runs against is for GATE 3 to state.
