# Predictions — method plugin, 2026-11-08

Each prediction was made before its operation ran. Outcomes as observed.

| # | Operation | Prediction | Outcome |
|---|---|---|---|
| 1 | `git ls-remote --tags origin v0.7.0` | The tag exists (the release session cut it) | **Held.** `72f8f13` (annotated), which peels to `84aa466` = `main` |
| 2 | Open the issue | It is #71 (#69 was the release issue, so its PR is #70) | **Missed.** #72. #70 and #71 were already taken |
| 3 | `python3 scripts/ci.py` on `84aa466` | All gates pass | **Missed, then held.** `what` and `how` failed because rdflib, pyoxigraph and pyld were not installed. After `pip install -r scripts/requirements.txt`, all gates passed |
| 4 | `plugins/ddd-method/check.py`, first run | Passes | **Missed.** One shared 8-word run with `method/README.md`: the skill restated the README's definition of "Value made visible". Reworded, and it passed. The check caught exactly what it exists to catch |
| 5 | `claude plugin validate` on the plugin and on the marketplace root | Both pass | **Held.** Both exit 0, and the root also passes with `--strict`. One plugin-directory warning (no icon) and one piece of advice (the README has no install line), neither of which changes the verdict |
| 6 | Install from the local marketplace in a scratch `HOME` | Install id `ddd-method@decision-driven-design`, version `0.7.0`; the skill is listed as `ddd-method:run` | **Held.** `claude plugin details` lists skill `run` (about 144 tokens always on). A headless session's init event lists `ddd-method:run` in both `skills` and `slash_commands` |
| 7 | `check.py` with planted defects (an id; a sentence from step 1's card; version `0.6.0`) | Each is refused | **Held.** Three FAILs, then 0 failures after the plants were restored |
| 8 | Smoke eval `proposed-as-ruled`, 1 run, `--allow-tools "Bash(git *)"` | 3 of 3 graders pass | **Missed, informatively.** 0.75. The model's only Bash call began with `cd` and was denied. It then stopped, refused to treat the step as ruled, and declined to name the register without reading it, which is what the skill says to do. The grant was too narrow, not the skill |
| 9 | Same, with `--allow-tools Bash Write` (Bash still inside the eval's OS sandbox, with no network) | 3 of 3 | **Held.** 1.00 |
| 10 | The full suite, 4 cases × 3 runs × 2 arms | Every case passes with the plugin. Without it, `unreachable` and `proposed-as-ruled` score lowest | **Missed in part.** `proposed-as-ruled` and `demand-flow-start` passed at 1.00. `step-1-small` (0.50) and `unreachable` (0.56) failed. `unreachable` failed on a rubric that counted generic field names as card content; corrected, it scored 1.00 with the plugin and 0.33 without. `step-1-small` stays below 1.0 (`findings.md` §Evals) |

## Round 28 (2026-11-11)

| # | Operation | Prediction | Outcome |
|---|---|---|---|
| 11 | Re-read the branch, origin and `main` | The branch is at `7700558` locally and on origin, and `main` has not moved | **Held.** `main` = `84aa466`. 60 origin branches (59 at arrival) |
| 12 | Highest decision id on every origin branch | `DDD-dec-120`, on `claude/zealous-ptolemy-3txf8k` | **Held.** `-119` and `-120` exist only there, and no branch mentions a higher id. This round takes `DDD-dec-121` |
| 13 | Round 28 copied into `rulings.md` | Byte-exact apart from the quote markers | **Held.** Verified by stripping the markers and comparing |
| 14 | `validate-claims.py core/decisions/ --decisions` with `DDD-dec-121` | Accepts it first time | **Held.** 97 decisions, all valid |
| 15 | The F-9 edit to `README.md` | The diff touches one line | **Held.** Only line 8 changed |
| 16 | `scripts/ci.py`; canon's `dotnet test`, `changelog --check` and `check --compare`, as CI runs them | All pass | **Held.** All gates pass. Canon: 66 tests, the changelog is the projection, every compare case agrees |
| 17 | `claude plugin validate --strict` on the plugin and the marketplace; `canon issue-refs --basis` after the commit | All pass | **Held.** Both `--strict` validations pass. `issue-refs --basis` first failed because the local clone was shallow and lacked its configured starting commits. After unshallowing, as CI checks out with full history: "ok. 5 commits in 84aa4665b4b0..6f75bba833db; Refs checked on 5, Basis on 1" |

## Round 29 (2026-11-19)

| # | Operation | Prediction | Outcome |
|---|---|---|---|
| 18 | Round 29 copied into `rulings.md` | Byte-exact apart from the quote markers | **Held** |
| 19 | Fetch `main` | `dc8b737`, with `DDD-address-06` to `-11`, `DDD-dec-122`, and `method/01` to `10` changed | **Held**, plus #86 (`DDD-dec-123`, `tools/canon/`). No new release |
| 20 | `check.py`'s thinness check against `main`'s `method/` | Still no shared 8-word run | **Held** |
| 21 | `git merge-tree origin/main HEAD` | One conflict, `meta/sessions/README.md` | **Held** |
| 22 | `DDD-dec-121` on every branch of both repositories | Only on this branch; upstream's highest is `DDD-dec-39` | **Held for files, missed for mentions.** Five branches mention it, each as an id record attributing it to #74. The highest downstream is now `DDD-dec-123` |
| 23 | The whole validate workflow, locally, on this branch's head | Passes, as before the round, since only records change | **Held.** `scripts/ci.py`: all gates. Canon: 66 tests, `changelog --check`, `issue-refs --basis` (6 commits from `dc8b737`, Refs on 6, Basis on 1) and `check --compare` (every case agrees) |

## Round 30 (2026-11-19)

| # | Operation | Prediction | Outcome |
|---|---|---|---|
| 24 | Round 30 copied into `rulings.md` | Byte-exact | **Held** |
| 25 | Rebase onto `main` | Each of the three commits that touch the index row conflicts there, and nothing else conflicts | **Held.** `main` had moved to `54dcb95` (#87). Seven commits replayed and signed |
| 26 | `DDD-dec-121` amended, then `validate-claims.py --decisions` | Valid | **Held.** 99 decisions |
| 27 | `check.py` after the `SKILL.md` edits, against `main`'s cards | Thinness still passes | **Held** |
| 28 | `check.py` with the pin check extended to the evals and both READMEs | Passes | **Missed.** It caught `#v0.7.1` and `0.8.0` left in the plugin README. Fixed. A planted `v0.8.0` in a grader was refused |
| 29 | The whole validate workflow on the new head | Passes | **Held, after a fix to the environment.** `scripts/ci.py`: all gates. Both `claude plugin validate --strict` runs pass. Canon first could not run: after the rebase `global.json` pins SDK `10.0.404` (#86), and this container had `10.0.403`. With `10.0.404` installed beside it (outside the repository): 66 tests, `changelog --check`, `issue-refs --basis` (8 commits from `54dcb95`, Refs on 8, Basis on 2) and `check --compare` (every case agrees) |

## Round 31 (2026-11-19)

| # | Operation | Prediction | Outcome |
|---|---|---|---|
| 30 | The tree before the round | Clean at `6657942`, as on origin | **Held** |
| 31 | Round 31 copied into `rulings.md` | Byte-exact | **Held** |
| 32 | The whole validate workflow on the record-only head | Passes, since only records change | **Held.** `scripts/ci.py`: all gates. Both `claude plugin validate --strict` runs pass. Canon, on SDK `10.0.404`: 66 tests, `changelog --check`, `issue-refs --basis` (9 commits from `54dcb95`, Refs on 9) and `check --compare` (every case agrees) |

## Round 32 (2026-11-24): predictions for the gate report, written before checking

| # | Operation | Prediction | Outcome |
|---|---|---|---|
| 33 | Round 32 copied into `rulings.md` | Byte-exact | **Held** |
| 34 | `git merge-tree origin/main HEAD` (47 commits) | Conflicts in `meta/sessions/README.md` and in the root `README.md`: #89 rewrote its status table and the front door, and this branch changed line 8 and added the plugin section | **Missed.** No conflict at all, not even in `meta/sessions/README.md`: `merge-tree` is clean, and a trial rebase in a throwaway worktree replays every commit with no stop. What remains is in the meaning, not the text: line 8 would say `v0.7.0` (`main` still says `v0.5.0`), and the plugin section says "step cards" |
| 35 | `check.py`'s thinness check against `method/` at `v0.8.0`, including the live card | Still no shared 8-word run, and no id | **Held** |
| 36 | The first line of each not-live card at `v0.8.0` | All eleven (01, 01b, 02 to 10) say they are not live and name the live card, in one pattern a skill can key on generically | **Held.** Each opens `> **Not live.** This card is superseded by [Make an act map](make-an-act-map.md), the live card (`DDD-dec-124`` |
| 37 | The files the live card links to at `v0.8.0`, by relative link | About ten to fifteen, spread over `method/`, `applications/`, `core/`, `graph/` and `meta/sessions/`, so a fixed three trees would miss reads | **Missed in part.** Nine link targets: `method/README.md`, `01-map-and-index-acts.md` (the pull statement's form), `../graph/upstream.yaml`, `../core/claims/`, and five under `../applications/`. None is under `meta/sessions/`: rulings are cited by name ("2026-11-18 R-2"), not linked. A fixed three directories would still miss `applications/` |
| 38 | `SKILL.md` at `d80a102` naming "step" as its unit | §2 to §5 assume numbered steps and a step argument. Most of the procedure must be rewritten, and the Round 30 rules survive only in substance | **Held.** §2 to §5, the README and three of four eval cases are built on numbered steps |

## Round 33 (2026-11-24): the build

| # | Operation | Prediction | Outcome |
|---|---|---|---|
| 39 | Round 33 copied into `rulings.md` | Byte-exact. Amendment 4 is a placeholder ("[yes, … / no]"), so it is recorded and not applied | **Held** |
| 40 | The rewritten `SKILL.md` against `method/` at `v0.8.0` | No shared 8-word run, no id, no named quick start, no mapping of old steps | **Held** |
| 41 | `pin_trees.py show v0.8.0` | More than three directories: `method/`, `core/`, `graph/` and `applications/` | **Held.** 23 paths, five of them under `applications/` |
| 42 | Eval `move-as-ruled` | With ≈ 1.00; without ≈ 0.75 (refuses, but does not read at the pin) | **Held** in run 3: 1.00 / 0.75 |
| 43 | Eval `unreachable` | With ≈ 1.00; without low (rebuilds the method from memory) | **Held** in run 3: 1.00 / 0.44 |
| 44 | Eval `not-live-card` | With high. Without also high: plain Claude reads the working tree, whose first line says "Not live". The plugin's gain is reading at the pin | **Missed.** The baseline was 0.00 in run 1 and 0.17 in run 2, on clones of an unrebased branch with no "Not live" line, and 0.50 in run 3, on the rebased head. The plugin itself read past the notice in run 2 (S-1) |
| 45 | Eval `act-map-small` | The weakest. Failures on `pull-statement` and `trace-endings`, with or without the plugin, as on step 1 at `v0.7.0` | **Held in part.** Run 3: 0.81 / 0.63. `pull-statement` failed in every run with the plugin, for a reason in the grader (E-1). `trace-endings` passed |

## Round 34 (2026-11-24)

| # | Operation | Prediction | Outcome |
|---|---|---|---|
| 46 | Round 34 copied into `rulings.md` | Byte-exact | **Held** |
| 47 | The rule line on the not-live cards at `v0.8.0` | The first `---` | **Held.** Line 7 on 1b's card and on 6's |
| 48 | Re-run `not-live-card` (3 runs per arm) | With ≈ 1.00, now relaying 1b's superseding section and saying it does. Without ≈ 0.5 | **Held in part.** 0.94 / 0.44. The 0.06 is a grader miss on a quoted shell variable |
| 49 | Re-run `act-map-small` (3 runs per arm) | With rises to ≈ 0.9 to 0.95, as `pull-statement` passes on gaps marked missing with a reason. Without stays ≈ 0.6 to 0.8. `act-description` stays noisy on long files | **Missed in part.** 0.85 / 0.56. `pull-statement` still failed in 2 of 3 runs with the plugin: a kind left empty, and a reason given only as a comment |
