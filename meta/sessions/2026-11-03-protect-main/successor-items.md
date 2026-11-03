# Successor items — protect main, 2026-11-03

What this session leaves open. Each row names who or what closes it.

| # | Item | Closes it |
|---|---|---|
| S-1 | **Land and apply.** Land the branch with `canon land`, then apply `.github/repo-standard.yaml` and run the three checks (`landing.md`) | **Emil** |
| S-2 | **The Signed Commits bypass list** (F-1): whether Integration 1236702 is this organisation's Claude app, and whether it, or the admin role entry, stays | **Emil**, by a ruling; a decision superseding nothing, adding to `DDD-dec-81` and `DDD-dec-108` |
| S-3 | **canon in a shallow clone.** `canon issue-refs --basis` reported `Basis on 0` and exited 0 when `basis.from` (`99d0a0f`) was not in the clone's history, so the Basis rule silently covered nothing. A checker that cannot see its start commit should say so (DESIGN.md §6.3's own lesson). CI is unaffected (`fetch-depth: 0`) | The canon CLI session (Gate 3) |
| S-4 | **Cite `DDD-dec-108`** in `tools/canon/DESIGN.md` §4.2, which says `DDD-dec-<pending>` (the canon CLI session's S-8) | The canon CLI session, once this lands |
| S-5 | **F-2 and F-3.** Whether sessions are excluded from `land/` and `v*` (check 3), and whether pull-request merges are turned off | **Emil** |

## After Round 2 (2026-11-03)

Add-only. The table above stands as written.

| # | Status | Closes it |
|---|---|---|
| S-1 | **Closed.** Landed (`458d05b`, then `320fccb`), applied, checks 1 and 2 held (`landing.md`) | Done by Emil |
| S-2 | **Ruled: "Remove it"** (`rulings.md`, Round 2). Integration 1236702 leaves the Signed Commits bypass list; the admin role stays the only bypass. Filed in this round | This round (`DDD-dec-110`) |
| S-5 | **Answered by evidence; check 3 not run.** Every push comes from Hafeok (the last 9 pushes, Emil's check), so a session's push to `land/` would be accepted. This confirms F-2. Agent review closes it (Round 2) | This round (`DDD-dec-109`) |
