# Successor items — the canon CLI, 2026-11-02

What this session leaves open at the end of Gate 1. Each row names who or what closes it.

| # | Item | Closes it |
|---|---|---|
| S-1 | **Gate 1 review.** `DDD-dec-100` to `DDD-dec-102` and `tools/canon/DESIGN.md`, with questions Q-1 to Q-7 in DESIGN.md §11 | **Emil** |
| S-2 | **The root shim is due for removal.** `validate-core-order.py` at the root was kept "for one release" (`DDD-dec-80`), and `v0.5.0` is cut (tag at `e5a332d`). Not removed here, because G1 changes no scripts | A later commit, on `DDD-dec-80` |
| S-3 | **`CHANGELOG.md` is stale.** At `e5a332d` it heads v0.5.0 "Ready to try (proposed)" and says "Proposed, not cut", but the tag exists. Found while designing `canon changelog` (DESIGN.md §4.5). Not edited here | Emil's ruling on Q-4, then `canon changelog`, or a hand fix before it |
| S-4 | **R-7 stays open in Python.** `validate-core-order.py .` gives four false E13s (P-4). DESIGN.md §4.7 removes the cause in `canon pins`. The Python checker is not fixed in this session; whether to fix it before retirement is open | Gate 3, or a fix in `scripts/` on its own issue |
| S-5 | **The ratification act under `canon land`** (Q-2) needs a decision and a ruleset change in `.github/repo-standard.yaml` before `land` is used | Emil, at Gate 2 |
| S-6 | **Decision-id headroom.** This session holds `DDD-dec-100` to `DDD-dec-102`. `DDD-dec-94` to `99` are left to the live authority-profile session (`claude/bold-franklin-i7b16g`) (Q-7) | Emil; that session's next id check |
| S-7 | **Gates 2 to 4** as the charter sets them: repository operations with tests; the shapes and `canon check` in parallel; a retiring decision per validator | Later sessions, after Emil's review |

## After Round 1 (2026-11-02)

Add-only. The table above stands as written at the end of Gate 1.

| # | Status or item | Closes it |
|---|---|---|
| S-1 | **Done.** Gate 1 reviewed. Round 1 ruled Q-1, Q-3 to Q-7 (`DDD-dec-103` to `DDD-dec-107`, bootstrap amendment 1). Q-2 needed no ruling | — |
| S-3 | Ruled by `DDD-dec-104`. Fixed by the first run of `canon changelog` at Gate 2 | Gate 2 |
| S-6 | **Done.** Q-7 confirmed the headroom | — |
| S-8 | **Cite the protection decision.** Emil's ruling on `main`'s protection (Varve's set, `pipeline (devcontainer)` required, no bypass, `land/**`, `v*` tags restricted to Emil) is filed by another session. DESIGN.md §4.2 says `DDD-dec-<pending>` until its id is known | This session, once the id is known |
| S-9 | **A cut descriptor was edited.** `releases/v0.5.0.yaml` on `main` had `ratified_head` changed in `023c2c4` and `c7424ad`, after `v0.5.0` was tagged at `e5a332d`, against `spec/release-format.md` rule 6. Restore it to its blob at the tag, or rule an exception. canon's immutability check (DESIGN.md §4.5) waits on this | **Emil** |
