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

## Amendment 1 — 2026-11-02: Round 1; main merged; ids re-checked; Q-7

Add-only. Nothing above this heading is edited.

- **Q-7 ruled** (Round 1, `rulings.md`): "94–99 left to the authority-profile session; this
  session took 100–102". The headroom is no longer Claude's choice alone. The `UNVERIFIED` flag
  above stands as history.
- **Base.** `main` moved from `e5a332d` to `c7424ad` (the authority profile, PR #45, merged). The
  branch took it by a signed merge, not a rebase, so the hashes cited so far still hold. There
  were no conflicts.
- **Decision ids**, re-checked on every branch of both repositories after the merge. Upstream
  (27 branches) holds up to `DDD-dec-39`. `main` holds up to `DDD-dec-93`.
  `claude/applications-for-readers-2026-11-02` (`fa99917`) holds `DDD-dec-94` and `95`. This
  branch holds `100` to `102`. No branch holds `96` to `99` or anything above `102`. Emil's
  round says the protection decision "will take the next free id". Its branch was not visible at
  the check. This session takes **`DDD-dec-103` onward** for Round 1, so the two cannot collide
  whichever id that decision takes.
- **Found at the check, not acted on.** `main` changed `releases/v0.5.0.yaml` twice after
  `v0.5.0` was tagged at `e5a332d`. `023c2c4` and `c7424ad` set `ratified_head` to `02298d3`,
  then `7aa3fb0`, and both are later than the tagged commit. A cut descriptor is immutable
  (`spec/release-format.md` rule 6). The tag still points at `e5a332d`. This is S-9.

## Amendment 2 — 2026-11-02: Gate 2's scope; main merged again

Add-only. Nothing above this heading is edited.

- **Scope.** Round 1 opened Gate 2. In scope: `tools/canon/` (source, tests, build files),
  `canon.yaml` at the root, `CHANGELOG.md` rewritten as the projection (`DDD-dec-104`), and the
  .NET SDK added to `.devcontainer/devcontainer.json` and `.github/workflows/validate.yml`
  (DESIGN.md §9). Still out of scope: `scripts/` (unchanged) and any canon content. The session
  stops at the end of Gate 2.
- **Base.** `main` moved to `e8fde2a` (S-9 corrected; `ci.py` decides "cut" from origin). Taken
  by a signed merge (`78ccb60`) with no conflicts.
- **Pull request.** [#47](https://github.com/mindovermachine-dev/decision-driven-design/pull/47),
  draft, in Varve's PR form. Ratification is Emil's landing by fast-forward after CI is green.

## Amendment 3 — 2026-11-03: Gate 2 landed; Gate 3 starts from main

Add-only. Nothing above this heading is edited.

- **Base.** `main` at `5ccdf41`, where Emil landed PR #47 by `canon land`. The session's
  branch, `claude/nifty-carson-e3x9t2` (fixed by the harness), held exactly `5ccdf41` after the
  landing. Its pull request is merged, so the branch restarts from `main` under the same name.
  Gate 3's work starts there and goes to a new pull request.
- **Decision ids**, re-checked on 2026-11-03 on every branch of both repositories. Upstream (27
  branches) holds up to `DDD-dec-39`. `main` holds up to `DDD-dec-107`. No branch holds
  `DDD-dec-108` or above yet. On Emil's word, the protection session takes `DDD-dec-108`, and
  this session takes **`DDD-dec-109` onward**.
- **Scope.** Gate 3 as DESIGN.md §5 and §8 design it: the shapes for claims, decisions and
  releases, the JSON-LD context, `canon check` with `--compare`, CI running it beside
  `scripts/ci.py`, and a ledger of every fixture's two verdicts. Out of scope: the What's shapes
  (DESIGN.md §5.5, after these), `canon pins` (R-7), and any retirement (Gate 4). The session
  stops at the end of Gate 3.
- **Protection.** If Emil applies the protection rulesets during the session, branch pushes are
  unaffected. Only `land/**` and `main` are restricted, to Emil.

## Amendment 4 — 2026-11-03: Gate 3 landed; S-20 starts from main

Add-only. Nothing above this heading is edited.

- **Base.** Emil landed PR #53, and `main` is `6ad604f`, reached by fast-forward with no merge
  commit. The session's branch restarts from it under the same name (its pull request is
  merged). S-20 goes to a new pull request.
- **Decision ids**, re-checked on 2026-11-03 at 09:16 UTC on every branch of both
  repositories. Upstream (27 branches) holds up to `DDD-dec-39`. `main` holds up to
  `DDD-dec-108`. `claude/sharp-davinci-89xeil`, the protection session's agent-review round,
  holds `DDD-dec-109` and `DDD-dec-110` and has not landed. This session filed nothing in
  `109`/`110`, so nothing collides, though the session was told "109 onward" and that
  session's bootstrap names this one as taking 109. **S-20 takes `DDD-dec-111`**, the next
  free id.
- **Scope.** S-20 only: the decision; the rule in `scripts/validate-claims.py` and in canon's
  decision shapes, in one change; refuse fixtures; the history scan; the ledger entry. Out of
  scope: editing any filed decision.
