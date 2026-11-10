# Predictions — map the flow of demand, 2026-11-08

Each prediction was stated before its operation ran, then checked. Recorded in order.

| # | Operation | Predicted | Observed | Held |
|---|---|---|---|---|
| 1 | Item 0: read `applications/pdlc/graph/example-pool.ttl` at `2f575f3` | No How-owner option; the cache purge recorded as #104 at oG | Four options (When, What, When, When); line 33 records the removal | Yes |
| 2 | Item 2: scan every branch of both repositories for decision ids | Highest file `DDD-dec-117`; upstream `DDD-dec-39`; `118` free | As predicted. `DDD-dec-118` to `120` appear only as range mentions | Yes |
| 3 | `validate-claims.py core/claims/` after `DDD-flow-01` to `-04` | 0 errors; no single-limb warning on the new claims (no semicolons in their statements); the six existing warnings unchanged | 35 claims, 0 errors, 6 warnings, all pre-existing (`DDD-cost-18`, `-24`, `-27`, `DDD-org-02` to `-04`) | Yes |
| 4 | First `scripts/ci.py` run in this container | All gates pass | `what` and `how` failed: `rdflib`, `pyoxigraph`, `pyld` not installed. After `pip install -r scripts/requirements.txt`: all gates passed | **No.** A container miss, not a repository one: the dependencies were absent. The prediction did not check them first |
| 5 | `validate-claims.py core/decisions/ --decisions` after `DDD-dec-118` | Valid; every `basedOn` resolves (local files and pinned ids) | 96 decisions valid | Yes |
| 6 | First `applications/pdlc/graph/check.py` run with the flow graph | `flow` conforms; the five new plants caught; existing results unchanged | As predicted, but the entry-outside-detection note fired on five sources: four at o0, which is held by `AnyOwner`, a false positive of the query | **Partly.** The checks held; the reading needed `AnyOwner` excluded. After the fix, one note: `software-deviates` at oC, the `DDD-flow-03` tension |
| 7 | Final gates before push: `scripts/ci.py`, `check.py`, and canon as CI runs it (tests, `changelog --check`, `issue-refs --basis`, `check --compare`) | All pass; `issue-refs` sees `Refs #67` on every commit | All passed: 66 canon tests; `issue-refs` ok on 6 commits (after unshallowing the clone, which it needs); `check --compare` agrees on every case. CI run 42694897190 on `63bc5c5`: success | Yes |
| 8 | Round 26: branch state at arrival (2026-11-10) | Clean tree at `8186d0b`, equal to origin; `main` at `2f575f3` | As predicted | Yes |
| 9 | Survey of "detect" in the card, pdlc.md, the graph data, the claims and the decision | Hits in `DDD-flow-03`, the card's claim row, owed paragraph and sources table, `lc:detectedOn`, check.py's note; pdlc.md §9's column | As predicted, plus `DDD-dec-118` (two lines) and pdlc.md §10 ("the new demand it detects"). Both pdlc.md uses are sighting-sense | Yes, with two more hits |
| 10 | Round 26 copied into rulings.md | The quoted block is identical to the message | Identical | Yes |
| 11 | `validate-claims.py core/claims/` after rewording `DDD-flow-03` | 0 errors; the six existing warnings, none new (no semicolon in the statement) | As predicted | Yes |
| 12 | `check.py` after sighting and entry in the graph data | `flow` conforms; five old flow plants and two new ones caught; the old note replaced by one reading, `software-deviates` along the telemetry seam | As predicted | Yes |
| 13 | A plant for `lc:SeamShape` (a seam produced at an act the supplier does not hold) | Caught | Caught | Yes |
| 14 | `validate-claims.py core/decisions/ --decisions` after `DDD-dec-118`'s Round 26 lines | Valid, 96 | Valid, 96 | Yes |
| 15 | Final gates before push (Round 26): `scripts/ci.py`, `check.py`, canon as CI runs it | All pass; `issue-refs` on 10 commits | All passed: 66 canon tests, changelog, `issue-refs` ok on 10 commits (Basis on 3), `check --compare` agrees. CI on the pushed head is reported in the session, not recorded here, so the approved head is the one CI ran | Yes |
