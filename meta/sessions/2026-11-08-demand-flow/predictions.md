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
| 7 | Final `scripts/ci.py` before push | All gates pass | See the push commit's record in `findings.md` | — |
