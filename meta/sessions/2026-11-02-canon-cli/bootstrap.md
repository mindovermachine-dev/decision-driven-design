# Bootstrap — the canon CLI, 2026-11-02

Filled in at arrival and committed with `prompt.md` as the session's first commit.

| Parameter | Value |
|---|---|
| Invocation | Interactive. Emil's rulings were given through the claude.ai question dialog and handed to this Claude Code session as its prompt. `prompt.md` carries them verbatim |
| Principal | Emil (sole ratifier; ratifies by merging the pull request) |
| Issue | [#46](https://github.com/mindovermachine-dev/decision-driven-design/issues/46). Every commit of the session carries `Refs #46` |
| Upstream repo | github.com/mindovermachine-dev/actor-indexed-determination (read only in this session) |
| Upstream pin | `v5.15.2` (`graph/upstream.yaml`), unchanged by this session |
| Downstream repo | github.com/mindovermachine-dev/decision-driven-design |
| Downstream base | `e5a332d` — head of `main` at arrival, and the commit tagged `v0.5.0` |
| Downstream branch | `claude/nifty-carson-e3x9t2` (assigned by the harness) |
| Reference | `Hafeok/varve`, read for its conventions; `Varve` on nuget.org, read live |
| Signing | `Claude (Emil) <claude+emil@okkels-klein.dk>`, key `SHA256:xDu5EyJd05ROum1g+8Aj1Up3MjE6RbHnI70/xNHljDY` |
| Model | Claude Opus 5.5 |

## Gates

| Gate | What | Who |
|---|---|---|
| G0 | This charter committed before any other change | Claude |
| G1 | The rulings filed as decisions; `tools/canon/DESIGN.md`; predictions before each operation. No code | Claude; **stops for Emil's review** |
| G2 | canon's repo operations (`land`, `release`, `ratify`, `changelog`, `issue-refs`) with tests | Claude, after Emil's review |
| G3 | The shapes, and `canon check` in parallel with the Python gates | Claude, after Emil's review |
| G4 | A decision retiring each Python validator, after full agreement | **Emil** |

The session stops at the end of G1. Nothing past G1 is written before Emil's review.

## Scope at arrival

In scope: the decisions filing the five rulings, `tools/canon/DESIGN.md`, this session record,
and the session's row in `meta/sessions/README.md`. Out of scope at G1: any C# code, any change
to `scripts/`, CI or the devcontainer (designed, not made), and any change to canon content
(claims, terms, the What, the How, decisions already filed).

## Decision ids

Checked across every branch of both repositories at arrival (2026-11-02, 12:58 UTC).

- **Upstream** (`actor-indexed-determination`, 27 branches): the highest id on any branch is
  `DDD-dec-39` (`main`, `claude/release-head-guard`).
- **Downstream `main`** (`e5a332d`): `DDD-dec-01` to `DDD-dec-84`, with `DDD-dec-83` never used
  (ready-to-try, amendment 4). `DDD-dec-901` is a validator fixture, not a decision.
- **`claude/bold-franklin-i7b16g`** (the authority-profile session, head `e120251`, 12:55 UTC):
  `DDD-dec-85` to `DDD-dec-93`. The session is live and filing round by round.
- No other branch holds an id above `DDD-dec-84`.

This session takes **`DDD-dec-100` onward**. `DDD-dec-94` to `DDD-dec-99` are left as headroom for
the live authority-profile session, so that its next rounds do not collide with this one; any of
them it does not use stay unused, and the gap is not a defect (the amendment 4 precedent). The
claim is recorded here, in each decision's notes, and in the pull request.
`UNVERIFIED — Emil review`: the headroom of six is Claude's choice, not a ruling.

## Session record

| File | What |
|---|---|
| `prompt.md` | The charter, verbatim |
| `predictions.md` | What each operation is predicted to do, written before it runs |
| `successor-items.md` | What this session leaves open |
