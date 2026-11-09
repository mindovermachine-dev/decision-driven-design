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

## P-9 — CI on the continuation's head

Prediction: `pipeline (devcontainer)` succeeds on `eb8102c`, as `scripts/ci.py` did locally (P-8).

**Outcome.** Run 42411491433: completed, success. The commit after it changes only
`landing.md` and this file, which no gate reads. CI is predicted green on it too.

## Round 26 (2026-11-08)

Not predicted: the arrival reads (the branch at `0dfe59a`, unmoved; `main` at `1ab1de0`; a grep for
"flow time" and for the How-owner option). They changed nothing. The rulings commit touches only
`meta/sessions/`.

## P-10 — the pool example fixed, the own-ground plant added, "flow time" marked

Planned edits:
- remove `ex:opt4` (the How owner's "manual cache purge" option) from `example-pool.ttl`;
- move it to the own-ground entry as issue #104 in `applications/sdlc/acts/example-record.ttl`:
  one o4 occurrence, `lc:demandKind lc:OwnGroundDemand`, with no o13, so no DORA query sees it;
- give `lc:OptionShape` a constraint that an option's `lc:demandKind`, if stated, is
  `lc:NewDemand`;
- add the plant "an own-ground item in the option pool";
- mark "flow time" `[PROPOSED]`, `UNVERIFIED — Emil review` at each of its 4 places in the specs
  and graph data (`pdlc.md` §1, `sdlc.md` §13 and §18, `dora/lead-time.rq`), and add it to
  `pdlc.md` §15.

Prediction, PDLC checker (`applications/pdlc/graph/check.py`):
- closure ok;
- map and example conform, the example with 4 options;
- **18 of 18** plants caught (17 + 1). No existing plant uses `ex:opt4`: the decline plants attach
  new exits to `ex:opt5`.

Prediction, SDLC checker (`applications/sdlc/acts/check.py`):
- the record conforms with 14 occurrences;
- **10 of 10** record plants, plus the DORA unit plant (11 "plant caught" lines, unchanged);
- the four DORA values unchanged: 17520 s, 2 per week, 0.5, 21600 s. #104 has no o13, so it
  enters no query.

The pool's worked metrics become:
- proposed: When 3 of 4, What 1 of 4, How 0;
- pulled: 2, When's share 1/2;
- closed: 3 (2 pulled, 1 expired), so the decline rate is 0/3 and the expiry rate 1/3.

The example then has no declined option. That shape is still exercised by the two decline plants.

Falsifier: any FAIL line, a plant count other than 18 and 11, or a DORA value that moves.

**Outcome.** As predicted.
- PDLC: closure ok, map and example conform, **18 of 18** plants caught. The new plant is caught
  by its own message, "Only new demand enters the option pool", which nothing else carries.
- SDLC: the record conforms with **14** occurrences. **11** "plant caught" lines (10 record plants
  and the DORA unit plant). DORA unchanged: 17520 s over 2, 2 per week over 2, 0.5 over 2, 21600 s
  over 1.
- Both exit 0.

## P-11 — every gate, after Round 26 (`python3 scripts/ci.py`)

Prediction: "all gates passed". 93 decisions (none touched). Pins 81, 0 basis-loss, 0
content-drift, 1 shadowed. No gate reads the files changed. Falsifier: any gate red.

**Outcome.** As predicted: "all gates passed", exit 0. 93 decisions. Pins 81, 0, 0, 1 shadowed.

## P-12 — CI on Round 26's head

Prediction: green on `b79e334`, as P-11 was locally. **Outcome.** Run completed, success. The
commit after it changes only `landing.md` and this file, which no gate reads. CI is predicted green
on it too.

## Round 27 (2026-11-09)

Not predicted: the arrival read (the branch at `f3b5eba`, unmoved; `main` at `1ab1de0`) and the
fetch of the Kanban Guide. Neither changed anything.

## P-13 — "flow time" ruled (Round 27)

Planned edits:
- `DDD-dec-114`, amended in place (Round 21): the statement gains one sentence defining flow time
  as the forecast's interval, o2b to o13, for new demand, landed dark. A new resolution section
  P-14 says it is based on the Kanban cycle time, with the Kanban Guide's wording quoted, and
  states the two differences. The notes record the amendment. The basis is unchanged: the Kanban
  Guide is an external source, not a graph node, so it goes in the resolution as a citation. A
  basedOn entry for it would not resolve (`DDD-dec-111`).
- `pdlc.md` §1: the proposed-term marks come off and the Kanban lineage goes in. §15: O-9 is
  ruled.
- `sdlc.md` §13 and §18, and `dora/lead-time.rq`: the marks come off.

Prediction:
- `validate-claims.py --decisions`: valid at 93, with no basis flag.
- Pins unchanged: 81, 0, 0, 1 shadowed.
- `scripts/ci.py`: "all gates passed".
- Both `lc:` checkers unchanged: PDLC 18 of 18, SDLC 11, the DORA values the same. No graph data
  changes except a comment in `lead-time.rq`.
- After the edit, `grep "flow time"` finds no `UNVERIFIED` or `[PROPOSED]` next to the term in
  the specs or the query.

Falsifier: any of these fails, or a mark remains.

**Outcome.** As predicted.
- 93 decisions valid, with no basis flag.
- Pins 81, 0, 0, 1 shadowed.
- "all gates passed", exit 0.
- PDLC 18 plants caught. SDLC 11, with the DORA values unchanged.
- No proposed-term mark remains on "flow time". The one grep hit left is `dora/lead-time.rq`'s own
  `[PROPOSED]`, which is the query's register, not the term's.

The first pass left the O-9 row's old text in place, so the row read as ruled and unruled at
once. It was rewritten as closed before this run. The Kanban Guide read is v2025.5 (May 2025):
cycle time is "The elapsed time between when a work item started and when a work item finished",
and the guide names "Cycle Time could be Flow Time" itself.

## P-14 — CI on Round 27's head

Prediction: green on `9b24f26`. **Outcome.** Run 42588904271: completed, success. The next commit
changes only `landing.md` and this file. CI is predicted green on it too.

## Round 28 (2026-11-09)

Not predicted: the arrival read (the branch at `7c36e8d`, `main` at `1ab1de0`). It changed nothing.

## P-15 — Round 28 applied

Planned edits:
- `DDD-dec-114` gains P-15 (the PDLC proposals ruled), and `DDD-dec-115` gains S-11 (the SDLC
  proposals ruled, R5's toggle service with PROV, R6, R1). Both statements gain one sentence.
  Their notes mark R11 and R13 to R15 as ruled. No basedOn change, since PROV is an external
  standard and is cited, not listed.
- The specs' registers change from "unruled" to "ruled by Round 28, except R4".
- The ruled items' marks come off. The open-item tables are updated.
- `sdlc.md` §7 gets the toggle service with PROV.
- Graph data:
  - a new act **oS** "propose a scope or assurance cut" (When owner), with o1 reading it
    (`lc:readsEarlier`);
  - `lc:ToggleOn` aligned to PROV in the ontology (`rdfs:subClassOf prov:Activity`; `lc:decidedBy`
    and `lc:readsVerdict` as sub-properties of `prov:wasAssociatedWith` and `prov:used`);
  - `lc:ToggleOnShape` requires `prov:startedAtTime` (when the feature was released);
  - the example's `ex:on101` gets one;
  - one new plant, "a release with no PROV time".
- The R16 to R18 marks come off the ontology.

Prediction:
- PDLC checker: closure ok (oS's terms are existing `lc:` terms; `prov:` terms are outside
  `lc:`, so closure does not judge them). The map conforms with oS. **19 of 19** plants caught.
- SDLC checker unchanged: 11, with the same DORA values.
- 93 decisions valid; pins 81, 0, 0, 1 shadowed; `scripts/ci.py` "all gates passed".
- After the edit, the only `UNVERIFIED` left in the two specs are R4's, the register lines'
  definition of what stays Claude's exposition, and the new PROV reading.

Falsifier: any FAIL, a count other than 19 and 11, or a gate red.

**Outcome.** As predicted in every count.
- PDLC: closure ok, map conforms with oS, **19 of 19** plants caught.
- SDLC: **11**, with the DORA values unchanged.
- 93 decisions valid; pins 81, 0, 0, 1 shadowed; "all gates passed", exit 0.
- The only `UNVERIFIED` left in the two specs is the new PROV reading (`sdlc.md` §7, and the
  register line that names it). The `[PROPOSED]` marks left in `pdlc.md` refer to method steps 7
  and 10 in `method/`, which are not this session's.

**One deviation from the plan.** `lc:decidedBy` was not made a sub-property of
`prov:wasAssociatedWith`, because exits and classifications also use it and are not releases. The
mapping is stated for releases in `lc:ToggleOn`'s comment instead.

**Two follow-ups after the first pass.**
- A blanket replacement marked the two invented example files "ruled". They now say "invented
  data, not a ruling".
- Three stale section references in graph headers were corrected (`pdlc.md` §9 to §11, §8 to §10;
  `sdlc.md` §4 to §3).

## Round 29 (2026-11-09)

Not predicted: the arrival read (the branch at `f391e06`, green, run 42591798992) and an
analytic computation done to set this prediction. Neither changed anything.

## P-16 — probabilistic forecasting (Round 29)

Planned edits:
- `DDD-dec-114`: the statement's forecast sentence and P-14's sketch become probabilistic
  forecasting. P-16 is added. The made line names Round 29.
- `pdlc.md` §1: the forecast section. §14 falsifier 3 becomes calibration plus the spread. O-4 is
  reworded: the percentiles, threshold and sample stay open.
- `sdlc.md` §18: the spread joins the How owner's answerability.
- Graph data:
  - `lc:Forecast` and its shape: rank, best, median, worst in days, their percentiles, trials, the
    sample days, and a spread equal to worst minus best;
  - `applications/pdlc/graph/forecast.py`: a seeded Monte Carlo over the daily new-demand
    throughput read from the SDLC's example record;
  - the PDLC checker computes a forecast for rank 2 and validates it;
  - two plants (median later than worst; fewer than 1000 trials).

Prediction:
- **The sample.** The example record's window, 2026-11-02 to 2026-11-09, has 7 days and one
  new-demand landing (#101's o13 on 2026-11-05). #103 is owed and does not count. So the daily
  throughput is [0, 0, 0, 1, 0, 0, 0], p = 1/7.
- **The values.** For rank 2, the days until two landings follow a negative binomial. Its exact
  15th, 50th and 85th percentiles are **5, 12 and 23 days**, computed before the simulation ran.
  The Monte Carlo (10,000 trials, seeded) comes out within ±2 days of each. Spread ≈ 18.
- **The checker** asserts that band against the analytic values.
- **Counts:** PDLC closure ok, **21 of 21** plants; SDLC unchanged at 11; 93 decisions valid; pins
  81, 0, 0, 1 shadowed; "all gates passed".

Falsifier: the simulation lands outside ±2 days of the analytic percentiles, a count differs, or a
gate is red.

**Outcome.** As predicted, and more exactly than predicted.
- The sample is [0, 0, 0, 1, 0, 0, 0].
- The Monte Carlo (10,000 trials, seed 2026) gives best 5, median 12 and worst 23 days for rank 2:
  **equal** to the exact percentiles, inside the ±2 band. Spread 18.
- The forecast conforms. PDLC: closure ok, **21 of 21** plants. SDLC: 11.
- 93 decisions valid; pins 81, 0, 0, 1 shadowed; "all gates passed", exit 0.

## P-17 — CI on Round 29's head

Prediction: green on `6b4e5e2`. **Outcome.** Completed, success. The next commit changes only
`landing.md` and this file. CI is predicted green on it too.

## Round 30 (2026-11-09)

Not predicted: the arrival read (the branch at `c6230e6`, unmoved, clean). It changed nothing.

## P-18 — "PROV" as traceability; O-4 ruled (Round 30)

Planned edits:
- **Graph data.** No `prov:` term anywhere in `applications/pdlc/graph/` or
  `applications/sdlc/acts/`:
  - `lc:ToggleOn` loses `rdfs:subClassOf prov:Activity`, and `lc:readsVerdict` loses
    `rdfs:subPropertyOf prov:used`;
  - a new `lc:releasedAt` replaces `prov:startedAtTime`, in the ontology, the shape, the example
    and the plants;
  - the shape requires the four traceability facts (who, what, when, on what verdict);
  - the forecast percentiles' comments and `forecast.py` say "ruled" instead of "proposed".
- **`DDD-dec-115`:** the statement and S-11's R5 now say traceability, and drop the PROV-O
  reading.
- **`DDD-dec-114`:** P-16 gets O-4's ruled numbers.
- **Specs:** `pdlc.md` §1, falsifier 3, O-4 and the register; `sdlc.md` §7 and the register; the
  READMEs.

Prediction:
- PDLC: closure ok (`lc:releasedAt` defined and sourced), map and example conform, **21 of 21**
  plants. The release plant is renamed and now caught by the traceability message. The forecast
  is unchanged (5, 12, 23).
- SDLC: 11.
- 93 decisions; pins 81, 0, 0, 1 shadowed; "all gates passed".
- `grep -rn "prov:"` over the two graph directories finds nothing.
- `UNVERIFIED` appears nowhere in `pdlc.md` or `sdlc.md`.

Falsifier: any of these fails.

**Outcome.** As predicted.
- PDLC: closure ok, map and example conform, **21 of 21** plants. The forecast is unchanged (5, 12,
  23).
- SDLC: 11.
- 93 decisions; pins 81, 0, 0, 1 shadowed; "all gates passed", exit 0.
- No `prov:` term in either graph directory, and no `UNVERIFIED` in `pdlc.md` or `sdlc.md`.

**One slip, caught before commit.** The first rewrite of `lc:ToggleOn` cut four following
definitions. The checker's closure step failed, naming them (`lc:toggle`, `lc:ready`,
`lc:readsVerdict`, `lc:userSideShare`). They were restored from `HEAD`, and the diff against
`HEAD` shows only the intended changes. The new release-without-verdict requirement is covered by
the existing "toggle turned on without a verdict" plant, so the plant count did not move.

## P-19 — CI on Round 30's head

Prediction: green on `015a365`. **Outcome.** Completed, success. The next commit changes only
`landing.md` and this file. CI is predicted green on it too.
