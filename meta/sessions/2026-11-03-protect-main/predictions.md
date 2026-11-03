# Predictions — protect main, 2026-11-03

Written before each operation runs. The outcome is appended under each prediction afterwards and
never edited into it.

Not predicted: the reads made at arrival (every branch of both repositories, `main`'s head check
runs and author, the repository's rulesets and events, a shallow clone of `Hafeok/varve`). They
changed nothing. The charter commit (`03ab5a8`) was made before this file, as the arrival
convention requires (`DDD-dec-20`).

## P-1 — baseline at the charter commit (`03ab5a8`)

Prediction: once `scripts/requirements.txt` is installed (this container has no rdflib at
arrival), `python3 scripts/ci.py` exits 0 with every gate passing. Decisions valid at 85 (the
number of `DDD-dec-*.yaml` files on `main`). The only change since `5ccdf41` is two Markdown files
under `meta/sessions/`, which no gate reads. Falsifier: any gate red, or a decision count other
than 85.

## P-2 — `DDD-dec-108` filed

Prediction: `validate-claims.py core/decisions/ --decisions` exits 0, valid at 86. Every
`basedOn` id (`DDD-dec-78`, `-81`, `-84`, `-101`) resolves to a local file. Claims and pins are
unchanged from P-1. Falsifier: the validator refuses the file, or the count is not 86.

## P-3 — `.github/repo-standard.yaml` with four rulesets

Prediction: the file parses as YAML (PyYAML `safe_load`). It has exactly four rulesets, named
`Signed Commits`, `trunk`, `land` and `Release Tags`. `trunk` has `bypass_actors: []` and exactly
one required status check, `pipeline (devcontainer)`, with `integration_id: 15368`. `land` and
`Release Tags` each have exactly one bypass actor, `User 2194785`. `Signed Commits` is
byte-identical to `5ccdf41` below its comment block. No gate reads the file, so `scripts/ci.py`
is unchanged from P-2. Falsifier: a parse error, or any of those counts or values differs.

## P-4 — `GOVERNANCE.md`, the README rows and the session record

Prediction: Markdown only, so `scripts/ci.py` passes exactly as at P-2. `canon issue-refs
--basis` passes in CI over the branch's range: every commit carries `Refs #51`, and the commit
that adds `DDD-dec-108` under `core/` carries a `Basis:` line. Falsifier: any gate's result
differs from P-2, or `issue-refs` refuses a commit.

## P-5 — CI on the pushed head

Prediction: the `validate` workflow's one job, `pipeline (devcontainer)`, concludes `success` on
the branch's head, with its check run from app id 15368 (the id `trunk` names). Falsifier: the job
fails, or its app id is not 15368. If the app id differs, the `trunk` ruleset would never be
satisfied and nothing could land, so that falsifier blocks the landing.

## Outcomes

Appended after the runs. The predictions above are not edited.

**P-1 — held.** After `pip install -r scripts/requirements.txt`, `python3 scripts/ci.py` exited 0
at `03ab5a8`, with all seven gates `ok`. `validate-claims.py core/decisions/ --decisions`: valid
at 85.

**P-2 — held.** At `c06b359`: valid at 86, exit 0, read directly. Every `basedOn` id resolves.
The decision's notes were amended once before the push (the two paths the trunk ruleset does not
close), and the change was folded into the same commit by a fixup, so `DDD-dec-108` lands as one
commit.

**P-3 — held.** At `dab0656`: `yaml.safe_load` parses the file. Four rulesets, in the order
`Signed Commits`, `trunk`, `land`, `Release Tags`. `trunk`: `bypass_actors: []`, one check,
`{context: pipeline (devcontainer), integration_id: 15368}`. `land` (branch) and `Release Tags`
(tag): one bypass actor each, `User 2194785`. `Signed Commits` and `repository:` compare equal to
`5ccdf41`. The diff to the header comment is the two citations of `DDD-dec-108` and "ruleset"
made plural. The declaration was also read against the schema of Varve's `repo-standard`
(`tools/repo-standard/src/RepoStandard/Declaration/DeclarationSchema.cs`): `name`, `target`
(`branch` or `tag`) and `enforcement` are present on each ruleset. Its `rules` and `conditions`
pass through unchecked, so GitHub validates them at apply. Running `repo-standard plan` was not
possible: building Varve's tool from the clone was refused by this session's permissions.

**P-4 — held, with a finding.** `scripts/ci.py` exited 0 at `61a3f6a`, as at P-2. Locally,
`canon issue-refs --basis` first reported `Refs checked on 4, Basis on 0`. The clone was
shallow, so `99d0a0f` (`basis.from`) was not an ancestor of anything and the Basis rule silently
covered no commit. After `git fetch --unshallow`: `Refs checked on 4, Basis on 1`, ok. CI checks
out with `fetch-depth: 0`, so CI is not affected. The finding is S-3 below. `canon changelog
--check`: ok.
