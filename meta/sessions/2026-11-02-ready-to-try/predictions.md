# Predictions — ready to try, 2026-11-02

Written before each operation runs. The outcome is appended under each prediction afterwards and
never edited into it.

## Baseline at arrival (`1d0f40c`), measured

| Check | Result |
|---|---|
| `validate-claims.py core/claims/` | valid: 31 claims, 6 warnings (single-limb candidates) |
| `validate-claims.py core/decisions/ --decisions` | valid: 47 decisions |
| `validate-core-order.py core/` | 74 pins resolved, 0 basis-loss, 0 content-drift, 1 shadowed id; core OK |

## P-1 — G1, three decisions filed

Prediction: decisions valid at 50; claims and pins unchanged from the baseline.

Outcome: decisions valid at 50 after `basedOn` edges were added. The first commit attempt filed
the three decisions with no `basedOn` and the validator correctly refused them (exit 1, "escaped
decision"); Claude read the result through a pipe that hid the exit code and committed anyway,
then amended the unpushed commit. Correction recorded here — Claude. Nothing invalid was pushed.

## P-2 — G2, the CI pin step runs without a secret

The principle repository is public (anonymous `git ls-remote` succeeds on 2026-11-02). The pin
step skipped itself whenever `UPSTREAM_TOKEN` was absent, and its comment still called the
repository private.

Prediction: with the skip removed (the token is used if present, and not required), the step
runs on every push and pull request that touches the watched paths, forks included, and reports
what the baseline reports: 74 pins resolved, 0 basis-loss, 0 content-drift. Falsifier: the step
fails on a clean tree at this branch's head. What it breaks: the claim that the pins are checkable
by anyone, which the "ready to try" front door (`DDD-dec-74`) will rely on.

Outcome, local run without credentials: 74 pins resolved, 0 basis-loss, 0 content-drift, 1
shadowed id; exit 0. Held locally. The CI run on the pushed branch is the test proper and is
recorded in the pull request.

## P-3 — G2, front-page links

Prediction: after the edit, no README outside `meta/` and `core/decisions/` links to
`github.com/Hafeok/actor-indexed-determination` or `github.com/Hafeok/product-cli`, and every
rewritten link resolves (anonymous `git ls-remote` on each repository). Ruled records keep their
historical URLs; they are not rewritten.

Outcome: 0 such links remain in READMEs outside `meta/` and `core/decisions/`. Both rewritten
targets resolve anonymously. Held. `spec/claim-format.md` and `applications/sdlc/how.md` still
carry `Hafeok/` URLs and were left: they are ruled material, and a link in them changes by
supersession or by Emil's say-so, not by this session.

## P-4 — G2, community files

Prediction: adding `SECURITY.md`, `CODE_OF_CONDUCT.md`, issue templates and a PR template changes
no validator result. They touch no watched path except `.github/`, which the workflow does not
watch, so CI does not run for them alone.

Outcome: claims valid at 31 with the same 6 warnings, decisions valid at 50, pins as baseline.
Held.

## P-5 — after the move to Claude Code, the three validators re-run

Written 2026-11-02 at about 08:55 UTC, at `c221a41` (bootstrap amendment 1), before any of the
three runs in this session.

Re-signing changed no tree (bootstrap amendment 1), and amendment 1 touched only
`meta/sessions/`. Prediction: every result equals the G2 head's. Claims valid at 31 with the same
6 warnings. Decisions valid at 50. Pins: 74 resolved, 0 basis-loss, 0 content-drift, 1 shadowed
id, exit 0. The pin check runs against a fresh shallow clone of `v5.15.2`. Falsifier: any count,
warning or exit code differs. What it breaks: the claim that a re-sign leaves the record
unchanged, which bootstrap amendment 1 rests on.

Outcome, at `03cd154` (the prediction's commit): claims valid at 31 with the same 6 single-limb
warnings (`DDD-cost-18`, `-24`, `-27`; `DDD-org-02`, `-03`, `-04`), exit 0. Decisions valid at 50,
exit 0. Pins: 74 resolved, 0 basis-loss, 0 content-drift, 1 shadowed id; core OK, exit 0. The pin
check shallow-cloned the pinned ref afresh, with `DDD_UPSTREAM_DIR` unset. Every exit code was
read directly, not through a pipe (P-1's lesson). Held.

## G3 execution — predictions P-6 to P-13

All eight were written together on 2026-11-02, at `9f5fd0b`, before any of the operations ran.
Each outcome is appended under its prediction afterwards. Baseline at `9f5fd0b`: claims 31 valid
(6 warnings); decisions 67 valid; pins 74, 0 basis-loss, 0 content-drift, 1 shadowed; `what/check.py`
31 ok, 0 failures; `how-examples/check.py` 112 ok, 1 expected warning, 0 failures. All exit 0
with the checkers' dependencies installed.

### P-6 — `GOVERNANCE.md`

Prediction: no validator result changes. Every relative link in the file resolves to a path at
the branch head. The file states exactly three departures from the standard, each with its
decision: item 4 and item 5 (`DDD-dec-78`) and the signing exception (`DDD-dec-81`). Falsifier: a
dead relative link, or a departure stated without a decision id.

### P-7 — `AGENTS.md`, with `CLAUDE.md` pointing to it

Prediction: `AGENTS.md` carries `CLAUDE.md`'s instructions with no rule dropped. Its diff against
the old `CLAUDE.md` shows only the tool-neutral framing, the moved checker's path and the gates
entry point. `CLAUDE.md` becomes a pointer that imports `AGENTS.md` (`@AGENTS.md`), so Claude Code
still loads the instructions. No validator result changes. Falsifier: a heading or rule of the
old `CLAUDE.md` with no counterpart in `AGENTS.md`.

### P-8 — copyleft: `LICENSE`, `NOTICE`, `LICENSE.md`

Prediction: `LICENSE` is byte-identical to the MPL-2.0 text served at
`https://www.mozilla.org/media/MPL/2.0/index.txt` (sha256 `3f3d9e00…9d04`, the same bytes as
Varve's `LICENSE`). GitHub's licence detection, queried by API at this branch's ref, reports
`MPL-2.0` where it reports `NOASSERTION` today. No validator result changes. Falsifier: a hash
mismatch, or detection reporting anything other than `MPL-2.0` at the branch ref.

### P-9 — the root move (`DDD-dec-80`)

Prediction: git records every moved file as a 100% rename: the three reports, every file under
`migration/`, and `validate-core-order.py` to `scripts/`. The root shim and
`scripts/validate-core-order.py` give byte-identical output and the same exit code on `core/`
(exit 0, 74 pins) and on `.` (exit 1, the R-7 defect, 4 errors), so the shim hides nothing. No
file under `core/decisions/` or under another session's `meta/sessions/` record changes. Nothing
under `meta/history/` contributes a new E13 error, because the checker skips any path with a
`migration` part and the three reports carry no embeds. Falsifier: a rename below 100%, any
output difference between the shim and the script, or a ruled record in the diff.

### P-10 — `.github/repo-standard.yaml`

Prediction: the file parses as YAML. It declares the description, the topics, Discussions on
and the Signed Commits ruleset with Varve's two bypass actors. Every other feature flag stays at
its current value (issues, projects, wiki on), so applying the file changes only what DDD-dec-81
rules. Nothing is applied by this session. The public API still reports `has_discussions: false`
and the old description at the end of the session, because applying is Emil's act. Falsifier:
the file declares a setting that DDD-dec-81 did not rule, or any repository setting changes.

### P-11 — devcontainer

Prediction: `devcontainer.json` parses as JSON with comments. `scripts/requirements.txt` pins the
five checker dependencies at the versions that pass here. A clean Python 3.11 virtual
environment that installs only that file runs `scripts/ci.py` to exit 0. The image itself cannot
be built in this container, because no Docker daemon runs here. The test proper is CI's
`pipeline (devcontainer)` job on the pushed branch, which builds the image and runs the gates
inside it. Falsifier: the clean-venv run fails, or the CI job is red.

### P-12 — `scripts/ci.py` as the single entry point, called by CI

Prediction: `python3 scripts/ci.py` runs six gates in order: claims, decisions, core order and
pins, the What, the How examples, and fixtures. It exits 0 at the head and prints one line per
gate. It exits 1 if any gate fails. Demonstration: with one accept fixture broken on purpose in
a scratch copy, it exits 1 and names the fixtures gate. The workflow runs on every push and pull
request, with no path filter. Its only step after checkout is `scripts/ci.py` inside the
devcontainer. It references no secret: `UPSTREAM_TOKEN` is dropped, because a public clone needs
no token, and Varve keeps no Actions secrets in its repository. Falsifier: any gate red at the
head, a broken fixture not caught, or the workflow running anything besides `ci.py`.

### P-13 — validator fixtures, accept and refuse

Prediction: under `scripts/fixtures/`, each checker gets a tree it must accept and cases it must
refuse. `validate-claims.py` must refuse a projected claim with no falsifier, a claim with no
region, and an established claim with no derivation. `--decisions` must refuse a decision with
no `basedOn` and one with no principal. `validate-core-order.py` must refuse a forward edge (E4)
and a drifted embed (E6). Each accept tree exits 0, and each refuse case exits 1 and prints its
expected error code. The fixtures' prose carries no `ddd:embed` or `ddd:ref` of an upstream id,
so the repository-wide E13 scan is unchanged. Falsifier: an accept tree that fails, or a refuse
case that passes or fails for a different code.
