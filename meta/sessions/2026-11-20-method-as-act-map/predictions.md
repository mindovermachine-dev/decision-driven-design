# Predictions

Each prediction is written and committed before its operation runs. The result is recorded against it afterwards, and a miss is kept as a miss.

## Operation 1 — the survey (deliverable 1)

Read at `1ecf914` (`main`). The survey covers `method/`, `README.md`, `applications/`, `core/`, `releases/`, `CHANGELOG.md`, `spec/`, `scripts/`, `tools/` and `.github/`. Session records under `meta/sessions/` are history and are counted separately, not row by row. Nothing outside `meta/sessions/2026-11-20-method-as-act-map/` changes in this operation.

| # | Prediction | Result |
|---|---|---|
| P-1.1 | "Ten steps" (or "all ten steps") is said in at least four places: `method/README.md`, `DDD-dec-82`, `README.md` and at least one release descriptor or `CHANGELOG.md` section || Held. Six places: `method/README.md:3, 7, 39`, `DDD-dec-82` (statement and resolution), `README.md:43`, `GOVERNANCE.md:117, 181`, `releases/v0.5.0.yaml:40` and `CHANGELOG.md:73` |
| P-1.2 | At least one document under the rewritten `applications/` names a method step by number || Held. `pdlc.md` names steps 1, 7 and 10 (lines 46-50, 275, 345, 571, 682); `sdlc.md:88` and `what.md:53` name step 1; the PDLC graph data names step 1b's parts |
| P-1.3 | The tooling (`scripts/`, `tools/`, `.github/`) names a step by number or counts ten steps in at least one place || **Missed.** No script, check, workflow or `canon` code reads a step number or the count. The only tooling that assumes numbered steps is the field-report issue template ("step N"), and the only executable text naming a step is the PDLC checker's "1b" in messages. The prediction expected code coupled to the numbers, and there is none |
| P-1.4 | No claim statement under `core/claims/` names a method step by number. At least one claim region, test or note does (`DDD-address-09`'s test names step 1's five-part procedure; its region names method step 5) || Held. No statement. Regions, tests, breaks and notes of `DDD-address-06`, `-08`, `-09`, `-10`, `DDD-flow-01` and `-04` do |
| P-1.5 | Every ruled text that states step 1's register says "ruled for test". None says "reported" || Held. `DDD-dec-74` and `DDD-dec-122` (resolutions) and the cut descriptor `v0.5.0` say "ruled for test". None says reported |
| P-1.6 | At least one filed claim's region says a pull is found at the edge first. That wording is in tension with the 2026-11-19 move order (place an act, then trace back), and changing it is a change to a claim, which #88 puts out of scope for the statement only || Held, with something not foreseen: `DDD-address-09`'s own notes (line 53) flag the line as Claude's `UNVERIFIED` reading of 2026-11-18 E-4. So the region holds an unverified reading, not a ruling (survey F-2) |
| P-1.7 | The survey has between 80 and 200 rows || Held. 96 rows |

## Operation 2 — the readings as questions, and the proposals (deliverable 2)

Written before `proposals.md`. Nothing under `core/`, `method/`, `applications/` or `README.md` changes in this operation.

| # | Prediction | Result |
|---|---|---|
| P-2.1 | Each of the nine lines of steps 2 to 10 maps onto at least one field of the issue's second group. None needs a field outside that list || Held. Lines 2 to 10 map one to one onto B-1 to B-9, each a field in the issue's list (`proposals.md`, P-2) |
| P-2.2 | At least two of the nine lines hold something that is not a field of one act or one decision: a property of the map as a whole, or of the record beside it || Held. Lines 8 and 9 are records beside the map (derivation, occurrences); 6 and 7 are the occupancy record; 10 is partly the record. Put to Emil as Q-3 |
| P-2.3 | A trace back run on the lifecycle data, in the SDLC scope from "plan the realisation" (o1b), reaches the edge on at least two readings, and meets at least one act whose ground readings the data does not declare, so the trace cannot run on from it || **Half held.** The second limb held: "frame own-ground work" (oG) declares no reading but an earlier deployment, so the trace stops at a finding. The first limb reached the edge cleanly on one reading only (the owed verdict, oC). The second edge, the framed issue (o1), is at the edge only for occurrences whose locus is What, because o1 is held by the locus's owner. The prediction did not foresee an act inside for some occurrences and outside for others. It became P-3's weakest point and step 3 of its procedure |
| P-2.4 | The first group needs more than the two fields the issue names: at least whether the act is inside the scope, which is the scope's to say and not the act's || Held. A-1, "inside the scope", is added (P-2) |
| P-2.5 | At least one proposal conflicts with a ruling recorded only in an open issue's text, not filed: #82's six-move core process, accepted 2026-11-18 at 13:22 || Held. K-1: #82's six-move process finds pulls before acts. Put to Emil as Q-5 |
| P-2.6 | `DDD-dec-124` is still free by file on every branch of both repositories when the proposals are written || Held. Re-checked before writing: no `DDD-dec-124` to `-129` file on any branch of either repository, no mention of `-125` to `-129`, and no `DDD-dec-12x` upstream on any branch or tag |
| P-2.7 | `python3 scripts/ci.py` passes after the proposals are committed || Held |

## Operation 3 — file DDD-dec-124 and change `method/` on the G1 rulings (deliverable 3)

Written after the G1 rulings were recorded (`rulings.md`) and before any file under `core/` or `method/` changes. The clone was unshallowed first (see P-3.4).

| # | Prediction | Result |
|---|---|---|
| P-3.1 | `DDD-dec-124` passes `validate-claims.py --decisions` on the first run, with every `basedOn` id resolving || Held. `valid: 103 decisions, ids unique, format rules satisfied` on the first run |
| P-3.2 | Under `method/`, the diff against `1ecf914` is additions only, plus one new file (`make-an-act-map.md`). No existing line is changed or deleted. `DDD-address-09` gains lines in `notes` only || Held. Against `1ecf914`, `method/`, `core/claims/` and `README.md` show 404 lines added and 0 deleted; `DDD-address-09` changes in one hunk, at the end of `notes` |
| P-3.3 | The worked example, run on the lifecycle data in the How owner's scope from "plan the realisation" (o1b): the owed verdict (oC) is the edge, with #103's pull; the own-ground issue (oG) is placed and its trace stops at a finding, because its readings are not described; the framed issue (o1) varies inside and outside on the change-locus axis, which the data declares, so the ruling makes two act sites where the data holds one, and that is a finding for the lifecycle data || Held, in all three limbs (`make-an-act-map.md`, worked example) |
| P-3.4 | `canon issue-refs --basis` on the unshallowed clone checks Refs on every commit of the branch and Basis on exactly the commits that touch `core/` || Held. `issue-refs: ok. 9 commits in 1ecf91415d82..44be60251c17; Refs checked on 9, Basis on 1`. The one commit touching `core/` is `44be602` |
| P-3.5 | The canon tests and `check --compare` pass unchanged, and `ci.py` passes || Held. 66 tests succeeded, 0 failed; `compare: every case agrees`; `canon check: all gates passed`; `ci.py`: `all gates passed` |
| P-3.6 | On the pull request, `agent review` reads "Not approved" and says nothing else; `pipeline (devcontainer)` passes | |
| P-3.7 | `method/README.md`'s first 20 lines name the four moves and the register of each || Held. Lines 3 to 10 hold the four moves, each with its register |
