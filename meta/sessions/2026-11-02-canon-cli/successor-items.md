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
