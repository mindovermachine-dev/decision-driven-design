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
