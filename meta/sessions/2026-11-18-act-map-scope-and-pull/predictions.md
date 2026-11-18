# Predictions

Each prediction is written and committed before its operation runs. The result is recorded against it afterwards, and a miss is kept as a miss.

## Operation 1 — copy the two session directories from `47cf4cc` (deliverable 1)

| # | Prediction | Result |
|---|---|---|
| P-1.1 | Eleven files are added: eight under `2026-11-17-act-map-and-process/` and three under `2026-11-18-pull-and-scope/`. No other path changes | Held. Eleven files added, eight and three, in commit `e1e2491`; no other path |
| P-1.2 | Every copied file is byte-identical to its blob at `47cf4cc` (`git diff 47cf4cc HEAD --` over the two directories is empty) | Held. `git diff --cached 47cf4cc` over the two directories was empty before the commit |
| P-1.3 | `survey.md` is among them and says it covers 109 lines in 38 files read at `84aa466` | Held. Its line 11 reads "Read at `84aa466` (`main`)"; its opening says 109 lines in 38 files |
| P-1.4 | No file under `core/`, `method/` or `meta/sessions/README.md` changes | Held |
| P-1.5 | `python3 scripts/ci.py` passes after the copy, as it does on `main` | Held, after a local setup step. The first run failed the `what` and `how` gates because `rdflib`, `pyoxigraph` and `pyld` were not installed in the container. Installed from `scripts/requirements.txt`; the second run passed every gate. Not a branch fault |

## Operation 2 — draft deliverables 2 to 5 for G1

Written before any of the four drafts. Nothing under `core/`, `method/` or `applications/` changes in this operation.

| # | Prediction | Result |
|---|---|---|
| P-2.1 | Every field of the pull statement gets a check that passes or fails on the worked example. At least one check is a judgement, not mechanical || Held. Thirteen fields, each with a check. F-4 and F-12 are judgement, and F-10 is judgement in declaring its axis |
| P-2.2 | With the How as the scope, the owed item's trace stops at the edge: the classification is outside the scope, so the entry act inside the scope is not the entry act `DDD-flow-03` names for the PDLC || Held. Under the How, #103 enters at plan the realisation; under the PDLC, at the classification (`pull-procedure.md`, W-1) |
| P-2.3 | "Actual" cannot be filled for any determinable in the worked example || Held, for all three items |
| P-2.4 | The own-ground item fits no gap on the product's determinables. It fits only once a determinable of the arrangement itself is named || Held. #104 fits "expected, with nothing specified" only on the arrangement's determinable (W-3) |
| P-2.5 | At least one desk check against a junior engineer's first contact fails on vocabulary: a word the procedure uses without defining it || Held. Part 1 fails on the owner names. Part 4 also fails, without the axis: a failure the prediction did not foresee |
| P-2.6 | All nine "Value made visible" rows of steps 2 to 10 can be filled from the draft line each card already quotes. None has to say it cannot be. At least two steps attach beside the map, not in it || Held. All nine rows filled from the quoted line. Four steps attach beside the map (6, 7, 8, 9) |
| P-2.7 | Six claims are proposed: `DDD-address-06` to `-08` amended and `-09` to `-11` new. `DDD-dec-122` is amended and no new decision id is needed || Held |
| P-2.8 | The proposals surface at least one conflict between a ruling of 2026-11-17 and one of 2026-11-18 that only Emil can settle || Held. 11-17 R-7 point 3 against 11-18 R-2 and R-3, on what individuates a map (`proposals.md`, P-2) |
| P-2.9 | `python3 scripts/ci.py` passes after the drafts are committed || Held |
