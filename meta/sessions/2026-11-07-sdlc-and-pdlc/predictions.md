# Predictions — the SDLC and PDLC applications, 2026-11-07

Written before each operation runs. The outcome is appended under each prediction afterwards and
never edited into it.

Not predicted: the reads made at arrival (every branch of both repositories, the upstream tag,
shallow clones of Varve and takt, the Claude Code Action docs and the Scrum Guide). They changed
nothing. **One miss.** The baseline `python3 scripts/ci.py` at the charter commit (`182465a`)
was run before this file existed, so nothing was written down for it. Its result was "all gates
passed", with 92 decision files on the branch (a miscount, see P-1's outcome). It is recorded here as observed, not as a
prediction held.

## P-1 — `DDD-dec-114` and `DDD-dec-115` filed

Prediction: `python3 scripts/validate-claims.py core/decisions/ --decisions` exits 0, valid at 94
(92 + 2). Every `basedOn` entry resolves:
- `DDD-dec-42`, `-52`, `-85`, `-87`, `-108`, `-109`, `-111`, `-112` and `-114` as local decision
  files;
- `DDD-address-01` as a local claim (arrival finding A-1);
- `DDD-frame-01`, `DDD-frame-02` and `DDD-ground-06` as pins already held at `v5.15.2`.

No `basis-resolves` flag fires. `validate-core-order.py` is unchanged: the pin file is not
touched, so it reports 81 pins resolved, 0 basis-loss, 0 content-drift and 1 shadowed id, the
count it printed at baseline.

Falsifier: the validator refuses either file, the count is not 94, any basis flag fires, or the
pin report moves.

**Outcome.** The validator exits 0 with "valid: 93 decisions, ids unique, format rules
satisfied". No basis flag fired. The pin report is unchanged: "81 pins resolved against the
pinned ref, 0 basis-loss, 0 content-drift, 1 shadowed id(s)".

**The count limb failed.** The validator counted 93, not the predicted 94, and the cause is the
prediction's base. The 92 came from `ls core/decisions | wc -l`, which also counts
`core/decisions/README.md`. The branch held 91 decision files at `182465a`
(`git ls-tree 182465a core/decisions/`), and 91 + 2 = 93. The same miscount is in the preamble's
"92 decision files", which is annotated in place (it is an observation, not a prediction). The other limbs held: both files are valid, every
basis resolved, and the pins did not move. Lesson: count with the validator, not with `ls`.

## P-2 — the lifecycle graph's first check run (`applications/pdlc/graph/check.py`)

Prediction: closure passes, with every `lc:` term used defined and sourced. The PDLC and SDLC act
maps, merged as one map, conform. The illustrative pool and delivery conform. All 12 planted
defects are caught, each by the shape that names its rule. Exit 0. Written before the first run,
which is the first test of shapes written in this session. A first-run failure in the SPARQL
constraints, the layer-path shape above all, would not surprise me.

Falsifier: any FAIL line.

**Outcome.** As predicted. Closure ok, map conforms, example conforms, 12 of 12 plants caught,
exit 0. The expected first-run failure did not come, so a passing shape was checked for
vacuity. A build act given the path "PDLC ▸ SDLC ▸ accept" was caught by the layer-path shape
("agrees with lc:within"). That defect is now plant 13. Re-run: 13 of 13, exit 0.

## P-3 — the occurrence record's first check run (`applications/sdlc/acts/check.py`)

Prediction: the illustrative record of issue #101 (7 occurrences), merged with the act map,
conforms to the map's shapes and the record's. All 7 plants are caught. Exit 0. The record's
SHAs are placeholders (`000…0001` to `000…0004`), not commits of any repository.

Falsifier: any FAIL line.

**Outcome.** As predicted: the record conforms, 7 of 7 plants caught, exit 0.

## P-4 — every gate, with the specs and READMEs in place (`python3 scripts/ci.py`)

Prediction: "all gates passed". Decisions valid at 93. The pin report is unchanged (81 pins, 0
basis-loss, 0 content-drift, 1 shadowed id). The `ddd:ref` markers in the two new specs name
only ids already pinned (`DDD-frame-01`, `DDD-frame-02`, `DDD-ground-06`, `term:answerability`,
`term:liability`, `term:seam-identity`), so no W5 fires for an unpinned reference. No gate reads
`applications/pdlc/` or `applications/sdlc/acts/` (S-3), so their files cannot fail a gate. The
two `lc:` checkers are run separately and pass, as in P-2 and P-3 (13 and 7 plants).

Falsifier: any gate red, a W5 or W6 on the new markers, or either checker failing.

**Outcome.** As predicted. `scripts/ci.py`: "all gates passed", exit 0. Decisions valid at 93.
Pins: 81 resolved, 0 basis-loss, 0 content-drift, 1 shadowed id. No W5 or W6. Both `lc:`
checkers: "all checks passed". Not predicted, and not new: `validate-claims.py core/claims/`
reports its 6 standing single-limb warnings over 31 claims, the same as at `main`. No claim file
was touched.

## P-5 — CI on the pushed head

Prediction: `pipeline (devcontainer)` succeeds on `9759c6b`, the same gates as P-4 in the
devcontainer.

**Outcome.** Run 286 (`validate`, event push): completed, success.

A follow-up commit corrects `landing.md`, which said the head is named in a closing report on
#61. No such report was posted, since the session was not asked to comment. The commit changes
two Markdown files under `meta/sessions/`, which no gate reads, so CI is predicted green on it as
well.

## Continuation (Rounds 16 to 22)

Not predicted: the reads at arrival (the branch head, `main`, `what.md` §3.0 to §5.1, how.md's H-9
row, `DDD-dec-60` and `-70`). They changed nothing. The charter commit (`5ac00e6`) and the
rulings commit (`6e8306c`) touch only `meta/sessions/`, which no gate reads.

## P-6 — `DDD-dec-114` and `DDD-dec-115` amended in place (Round 21)

Prediction: `validate-claims.py core/decisions/ --decisions` exits 0, still **93** decisions
(amended, not added). `DDD-dec-114`'s `basedOn` gains `DDD-dec-70`, which holds the H-9 telemetry
contract pattern (it supersedes `DDD-dec-60`, which the prompt cites), and `DDD-dec-64`, which
rules the What's structure that the output table reads. `DDD-dec-115` gains nothing new. Every
entry resolves: the new ones as local files, and the upstream ones as the three existing pins.
The pin report is unchanged: 81 pins, 0 basis-loss, 0 content-drift, 1 shadowed id. No pin is
added, because no new upstream id is cited.

Falsifier: the validator refuses either file, the count moves, a basis flag fires, or the pin
report moves.

**Outcome.** As predicted. "valid: 93 decisions, ids unique, format rules satisfied". No basis
flag fired. Pins: 81 resolved, 0 basis-loss, 0 content-drift, 1 shadowed id. `DDD-dec-114`'s
basedOn gained `DDD-dec-64` and `DDD-dec-70`. `DDD-dec-115`'s is unchanged.

## P-7 — the lifecycle graph, amended for Rounds 16 to 22

**A miss first.** After adding oC, oG and the `lc:forKind` dependencies, I ran
`applications/pdlc/graph/check.py` before writing a prediction for that change. It printed "all
checks passed", 13 of 13 plants caught. The run is recorded here as observed, not as a held
prediction.

Prediction, for both checkers after the remaining edits (the example classification and the
telemetry check, four new PDLC plants, the record's demand kind, issue #103 restoring #101, the
DORA queries and the reading shape):
- `applications/pdlc/graph/check.py`: closure ok, so every new `lc:` term is defined and sourced.
  The map conforms with oC, oG and the kind-scoped dependencies. The example conforms. **17 of 17**
  plants caught. Exit 0.
- `applications/sdlc/acts/check.py`: the record conforms with 13 occurrences. **10 of 10** plants
  caught. The DORA keys compute to the hand-worked values: lead time 17520 seconds (the median of
  17040 and 18000), deployment frequency 2 per week, change failure rate 0.5, time to restore 21600
  seconds. The four readings conform. The bad-unit plant is caught. Exit 0.

The likeliest failure is in the DORA arithmetic: rdflib's datetime and decimal handling, or the
median of two Decimals.

Falsifier: any FAIL line, or any computed value other than those four.

**Outcome.** As predicted, in every part.
- PDLC: closure ok, map and example conform, 17 of 17 plants caught.
- SDLC: the record conforms, 10 of 10 plants caught, and the bad-unit plant caught (11 "plant
  caught" lines).
- DORA: lead time 17520 s over 2, deployment frequency 2 per week over 2, change failure rate 0.5
  over 2, time to restore 21600 s over 1.
- The readings conform. Exit 0 for both.

The expected arithmetic failure did not come.

## P-8 — every gate, after the spec amendments (`python3 scripts/ci.py`)

Prediction: "all gates passed". Decisions valid at 93. Pins unchanged (81, 0, 0, 1 shadowed).
`pdlc.md` gains one `ddd:ref`, `term:capability`, which is pinned at `v5.15.2`, so no W5 fires.
No gate reads `applications/pdlc/` or `applications/sdlc/acts/`. Both `lc:` checkers pass as in
P-7 (17 plants; 10 plus 1, and the four DORA values). No claim changed, so `core/claims/` reports
its 6 standing warnings.

Falsifier: any gate red, a W5 or W6, or a checker failing.

**Outcome.** As predicted. `scripts/ci.py`: "all gates passed", exit 0. 93 decisions. Pins 81, 0,
0, 1 shadowed, and no W or E lines. Both checkers: "all checks passed". A misdirected batch
before this run (the shell sat in the session folder) wrote nothing and ran nothing. It is noted
here because its prediction text was rewritten and resent.
