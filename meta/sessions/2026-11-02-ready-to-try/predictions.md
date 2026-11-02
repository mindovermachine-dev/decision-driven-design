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

## P-3 — G2, front-page links

Prediction: after the edit, no README outside `meta/` and `core/decisions/` links to
`github.com/Hafeok/actor-indexed-determination` or `github.com/Hafeok/product-cli`, and every
rewritten link resolves (anonymous `git ls-remote` on each repository). Ruled records keep their
historical URLs; they are not rewritten.

## P-4 — G2, community files

Prediction: adding `SECURITY.md`, `CODE_OF_CONDUCT.md`, issue templates and a PR template changes
no validator result. They touch no watched path except `.github/`, which the workflow does not
watch, so CI does not run for them alone.
