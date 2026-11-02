# Predictions — the canon CLI, 2026-11-02

Written before each operation runs. The outcome is appended under each prediction afterwards and
never edited into it.

Not predicted: the reads made at arrival, before this file existed (fetching every branch of both
repositories, `git ls-remote --tags`, nuget.org's package index, a shallow clone of `Hafeok/varve`).
They changed nothing. The first commit (the charter) was made before this file, as the arrival
convention requires (`DDD-dec-20`).

## P-1 — baseline at the charter commit (`6aad807`)

Prediction, from `main`'s state at `e5a332d` (the ready-to-try session's last recorded run):
`python3 scripts/ci.py` passes every gate. Claims valid at 31 with 6 warnings; decisions valid at
68; 74 pins resolved, 0 basis-loss; the `releases` gate reports `v0.5.0` as cut (tag present
locally) and does not re-guard it. Falsifier: any gate red on a tree whose only change since
`e5a332d` is two Markdown files under `meta/sessions/`.

## P-2 — G1, three decisions filed (`DDD-dec-100` to `DDD-dec-102`)

Prediction: `validate-claims.py core/decisions/ --decisions` is valid at 71 (68 + 3); claims and
pins unchanged from P-1; every `basedOn` id resolves to a local file. Falsifier: the validator
refuses one of the three, or the count is not 71. The exit code is read directly, not through a
pipe (the ready-to-try P-1 lesson).

## P-3 — G1, the design and the session record

Prediction: `tools/canon/DESIGN.md`, this file's outcomes, `successor-items.md` and the README
row change no gate's result: `scripts/ci.py` passes exactly as at P-2. `tools/` is new and no
gate reads it. Falsifier: any gate's output differs from P-2 other than by nothing.

Outcome for P-1 (appended): **refuted on the first run, by the environment, not the tree.** The
first run exited 1 with `what` and `how` failed: this container had no rdflib, so both checkers
skipped their RDF steps and reported the skip as a failure, as they should. After
`pip install -r scripts/requirements.txt` (rdflib 7.6.0, PyLD 3.3.0, pyshacl 0.40.2, pyoxigraph
0.5.13, PyYAML 6.0.3; Python 3.13.18, where CI uses 3.11), the second run exited 0: all seven
gates passed. Measured directly: claims valid at 31 with 6 warnings; decisions valid at 68; 74
pins resolved, 0 basis-loss, 0 content-drift, 1 shadowed id; `v0.5.0` points at `e5a332d` and is
skipped by the guard as cut. The prediction held for the tree. The lesson is for `canon check`'s
design: a checker that cannot run must say so as a failure, never a pass (DESIGN.md §6.3).

## P-4 — R-7 reproduced before it is designed around

Prediction, from the ready-to-try record (successor items, R-7):
`python3 scripts/validate-core-order.py .` exits 1 with 4 E13 errors on `core/14-maturation.md`
and `core/16-calibration-ledger.md`, while `python3 scripts/validate-core-order.py core/` exits 0.
Falsifier: a different count, different files, or exit 0.

Outcome for P-4 (appended): **held.** Exit 1; four E13 errors, three on `core/14-maturation.md`
(`term:maturation`, `term:waterline`, `term:maturity`) and one on `core/16-calibration-ledger.md`
(`term:calibration-ledger`). The ready-to-try record named two of the four ids as examples; the
count and files match. Cause, confirmed by reading `scripts/validate-core-order.py:368-385`: when
the argument holds no numbered documents, `main` takes the upstream-only branch and calls
`check_upstream` without `local_ids`, so this repository's own terms read as unpinned upstream
ids. `core/` takes the full branch and passes `local_ids=set(graph)` (line 522). The design for
`canon pins` removes the two modes (DESIGN.md §4.7).

Outcome for P-2 (appended): **held.** `validate-claims.py core/decisions/ --decisions` printed
"valid: 71 decisions, ids unique, format rules satisfied" and exited 0, read directly. Claims
exit 0, unchanged. Every `basedOn` id names a local file (`DDD-dec-04`, `-43`, `-51`, `-72`,
`-76`, `-81`, `-84`, `DDD-tool-01`, and the three among themselves).

Outcome for P-3 (appended): **held.** `scripts/ci.py` exited 0 with all seven gates passed;
decisions valid at 71; 74 pins resolved, 0 basis-loss, 0 content-drift, 1 shadowed id. Same as
P-2. No gate reads `tools/`.

## P-5 — Round 1, the Basis survey (tests D-8 early, by script, before canon exists)

Prediction: among non-merge commits reachable from `HEAD` that change anything under `core/`,
at least one after issue #44's first `Refs #44` commit has no `Basis:` line (D-8). Every commit
on this branch since `6aad807` that touches `core/` has one. Falsifier: none missing after #44.

Outcome for P-5 (appended): **refuted.** The survey ran on a shallow clone first (264 commits)
and was redone after `git fetch --unshallow` (389). Of 94 non-merge commits that change `core/`,
20 have no `Basis:` line. All 20 are dated 2026-07-26 or earlier, the newest is `35d68f6`, and all
predate `99d0a0f` (2026-07-28, "CLAUDE.md: … require claim-ID basis in commits"). Every one of the
71 since `99d0a0f` carries a `Basis:` line, so none is missing after #44. D-8 is refuted as
written. The rule has been kept by hand from the moment it was written, which is why `99d0a0f`
is proposed as the start commit.

## P-6 — Basis ids resolve at their own commit

Prediction: of the ids named on `Basis:` lines of those 71 commits, some do not resolve to a file
under `core/claims/` or `core/decisions/` at that commit. Causes: upstream ids that are pinned
(e.g. `DDD-ground-*`), and ids filed in the same commit's own tree, which resolve. At least one
id resolves neither locally nor in `graph/upstream.yaml` at that commit. Falsifier: every id
resolves one way or the other.

Outcome for P-6 (appended): **held.** Over the 71 commits, the `Basis:` lines name 338 ids,
counted once per commit. 254 resolve to a file under `core/claims/` or `core/decisions/` at their
own commit, and 72 to an id named in `graph/upstream.yaml` at that commit. 12 resolve to neither,
in 8 commits:

| Commit | Ids |
|---|---|
| `bd79609` | `DDD-dec-40` |
| `76d644e` | `DDD-ground-06`, `DDD-ground-01`, `DDD-dec-37` |
| `f6d432a` | `DDD-dec-26` |
| `b20cc56` | `DDD-dec-26` |
| `61dfafa` | `DDD-measure-12`, `DDD-measure-14` |
| `79bb532` | `DDD-dec-15` |
| `f4b392e` | `DDD-cost-11` |
| `70619c9` | `DDD-cost-02`, `DDD-cost-03` |

Most are upstream ids cited before they were pinned, or decisions filed upstream. They are not
errors to rewrite. They are why `DDD-dec-105` enforces resolution only from its own commit on.

## P-7 — Round 1 decisions filed (`DDD-dec-103` to `DDD-dec-107`)

Written before the validator ran, and appended late, in this same commit: the validator was run
on the five files before this prediction was written down. Prediction as it stood: valid at 85
(71 + main's `DDD-dec-85` to `93` + 5). Outcome: valid at 85, exit 0. Recorded as a lapse in
order, not a held prediction.
