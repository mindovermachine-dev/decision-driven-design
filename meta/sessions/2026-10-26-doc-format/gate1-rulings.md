# GATE 1 rulings — doc format

Given by Emil on 2026-10-26, on `gate1-survey.md`. Recorded when given.

| # | Question | Ruling |
|---|---|---|
| 1 | Canon under pre-session ruling 1: reading A (both repositories' `core/`) or B (upstream only) | **A.** Canon is upstream `core/` and this repository's `core/`: documents 13–17, `claims/`, `decisions/` and `graph/`. |
| 2 | The disposition table (survey item 3) | **As recommended.** The table stands as ruled. The promotions are registered in `promotions.md`, with IDs that held bases can cite. |
| 3 | Retention of the old text | **As recommended.** A reformatted document replaces its old text in place, and names it in a `supersedes: <commit>:<path>` field. |
| 4 | May `basis` name a held result? | **As recommended.** `basis` may name `held:<session-dir>/<item-id>`. The check reports held bases as their own warning class. |
| 5 | Should GATE 2 propose a change to `CLAUDE.md`'s sentence on core documents? | **Yes.** Proposed at GATE 2, not made. |

## Consequences for GATE 2

- Pre-session ruling 1 now reads: **only canon carries authority, and canon is both repositories' `core/`.** Every other folder exists for a named reader doing a named act.
- `core/13`–`17` keep `ddd:contract` and the canon format. They are outside the `ddd:doc` check.
- "Promote" means filing claims in the canon that fits: upstream if actor-general, `core/claims/` here if software-specific.
