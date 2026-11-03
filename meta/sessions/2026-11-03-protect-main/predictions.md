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

**P-5 — held.** On `a792949`, the branch's head at the first push, one check run:
`pipeline (devcontainer)`, `completed`, `success`, app id 15368. The `trunk` ruleset's
`integration_id` matches the app that posts the check. This outcome is recorded in a commit after
`a792949`, so the head to land is that later commit, once its own run is green (issue #51).

## After the landing — 2026-11-03

Add-only. Emil landed `458d05b` with `canon land` and applied `.github/repo-standard.yaml`
(`landing.md`, "Outcome"). Read against `landing.md`'s expectations, written before the landing:

- **The plan's expectation** (four rulesets created; the description, topics and Discussions
  changed): **held** by the end state. The four rulesets are active and the repository settings
  match the file. Emil applied the settings first, then the rulesets.
- **Check 1** (rules on `main`: `deletion`, `non_fast_forward`, `required_signatures`,
  `required_status_checks`): **held**, read live.
- **Check 2** (a direct push to `main` refused with GH013, naming `pipeline (devcontainer)`, even
  for the admin): **held**. Emil's signed empty commit `d270e4b` was refused with "Required
  status check "pipeline (devcontainer)" is expected." `main` is still at `458d05b`. The
  `trunk` ruleset is in force, and it has no bypass for the admin role.
- **P-5's consequence** (`integration_id: 15368` matches the app that posts the check, so a
  landing is possible): **held**. `458d05b` reached `main` under `canon land`. The landing was
  made before the rulesets were applied, so it was not itself gated by `trunk`. The first
  landing under the ruleset will be the first test that `canon land --main` passes `trunk`.

## Round 2 — 2026-11-03

Add-only. **The expectation left open above** (the first landing under the ruleset tests that
`canon land --main` passes `trunk`): **held**. `320fccb` reached `main` by `canon land --main`
after the rulesets were applied, with `pipeline (devcontainer)` green on it from app 15368
(`landing.md`, "The second landing").

### Round 2 predictions, written before each operation

**P-6 — `DDD-dec-109` and `DDD-dec-110` filed.** `validate-claims.py core/decisions/
--decisions` exits 0, valid at 88 (86 on `main` plus two). Every `basedOn` id resolves.
Falsifier: a refusal, or a count other than 88.

**P-7 — canon builds and its existing tests pass unchanged.** After `agent-review` is added and
`land` gains its check, `dotnet build` has no warnings (warnings are errors), and the 32 tests
present at `320fccb` pass with no edit to any of them. `land` asks GitHub nothing when `main`'s
`.github/repo-standard.yaml` pins no `agent review`, and the existing land tests have no such
file. Falsifier: a build error, or an existing test that fails or needs an edit.

**P-8 — the new tests, tamper cases included, pass.** Each new test is run and passes. Then, to
show it can fail, the session breaks the rule it guards, once each, and watches it go red. The
three ruled tamper cases are a session-authored comment, a check from another app, and an
approval of an older head. For each, the rule is disabled in a scratch edit that is never
committed. Falsifier: a new test red against the real code, or a tamper test still green with its
rule disabled.

**P-9 — the repository's gates stay green.** `scripts/ci.py`, `canon changelog --check` and
`canon issue-refs --basis` (from a full, not shallow, clone) pass at the branch's head.
Falsifier: any of them fails.

**P-10 — CI on the pushed head.** `pipeline (devcontainer)` concludes `success`, from app 15368.
No check named `agent review` appears on the head. `.github/workflows/agent-review.yml` is new on
this branch, so it does not exist on `main`, and `pull_request_target` and `issue_comment` run
only `main`'s copy. Nothing on this branch can post that check. Falsifier: the pipeline fails, or
an `agent review` check appears.

### Round 2 outcomes

**P-6 — held.** At `b9536e3`, valid at 88, exit 0. Every `basedOn` id resolves.

**P-7 — held.** `dotnet build canon.slnx -c Release`: no warnings, with warnings as errors. The
32 tests present at `320fccb` pass with no edit to any of them. One compile error on the first
build (CS0136, a reused local name in `AgentReviewCommand.cs`) was fixed before any test ran.

**P-8 — held.** 61 tests: the 32 old ones and 29 new, all green. Each ruled tamper case was then
broken once, in a scratch copy of the repository under the session's scratchpad, never in the
working tree:
- the session-comment rule disabled (a comment made through an app counts): red on
  `ASessionAuthoredCommentDoesNotCount` and `ACommentThroughAnyOtherAppDoesNotCount`, and on
  nothing else;
- `canon land` ignoring the app id: red on `ASuccessFromAnotherAppDoesNotCount` alone;
- any approved SHA counting, not only a prefix of the head: red on
  `AnApprovalOfAnEarlierHeadDoesNotCount` alone.

**P-9 — held.** At `c933e08`: `scripts/ci.py` passes every gate, and `canon changelog --check`
passes. `canon issue-refs --basis`: "5 commits in 320fccb9dc90..c933e0879999; Refs checked on 5,
Basis on 1".

**P-10 — held.** On `b73cc7f`, one check run: `pipeline (devcontainer)`, `completed`, `success`,
app 15368. No `agent review` check appeared. The head to land is the commit that records this,
once its own run is green (issue #51).

**Not predicted: the merge of `main`.** `main` moved from `320fccb` to `afba50f` (canon Gate 3,
and the contributing session) while Round 2 was being built. `dacec94` was green, but it could no
longer be fast-forwarded onto. The merge was made without a prediction, and is recorded here
instead. It had three conflicts: `Cli.cs`, `meta/sessions/README.md` and `CONTRIBUTING.md`, each
resolved by hand as the merge commit states. After it: `scripts/ci.py` passed, 66 canon tests
passed, `changelog --check` passed, and `check --compare` reported that every case agrees. The
canon session filed its S-20 decision as `DDD-dec-111` after seeing 109 and 110 here, so the ids
do not collide.

**P-11 — the merged head in CI.** `pipeline (devcontainer)` concludes `success` from app 15368 on
the head that records this, and no `agent review` check appears. Falsifier: either fails.

**P-11 — held.** On `0190521`: `pipeline (devcontainer)`, `success`, app 15368, and no
`agent review` check. By then `main` had moved again, to `e70ab63` (the product-cli definition).
That second merge (`55c2be8`) was clean and not predicted. Afterwards, every gate passed locally:
`ci.py`, 66 tests, `check --compare`, `issue-refs --basis` and `changelog --check`.

**P-12 — the head to land.** On the commit that records this, `pipeline (devcontainer)`
concludes `success` from app 15368, and no `agent review` check appears. Falsifier: either fails.
