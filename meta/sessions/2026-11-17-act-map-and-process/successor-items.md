# Successor items — the act map and a process, 2026-11-17

Nine items stay open after `DDD-dec-122`. None is ruled. O-6 and O-7 become new issues (R-7, point 6).

| # | Item | Where it shows | For |
|---|---|---|---|
| O-1 | `DDD-address-02`'s region says the act map is "a tree of occurrences". `DDD-address-06` says its nodes are act sites and the tree is containment. The region is superseded, annotated or left | `core/claims/DDD-address-02.yaml:8`; `method/01-map-and-index-acts.md:62` | Emil |
| O-2 | The second top act, changes to the SDLC itself, has no graph data. One sentence about it contradicts `DDD-ground-06`: "the same addresses with a different layer path" | `applications/sdlc/sdlc.md:451`, `:455` | Emil |
| O-3 | Four places call the SDLC's part of the lifecycle map "the act map" | `survey.md`, S-10 | A prose pass, after PR #73 |
| O-4 | A later o5 reads an earlier o6, and o6 reads o5. The data leaves the first edge out | `applications/sdlc/sdlc.md:106`; `applications/sdlc/acts/acts.ttl:88` | Emil |
| O-5 | New demand declares oC as an entry act. No dependency leads from oC towards o16 for new demand | `applications/pdlc/graph/demand-flow.ttl`; `rulings.md`, evidence | Emil |
| O-6 | **New issue.** The lifecycle has no index of determinables. Its six sources of pull are not marked taken up or not, and carry no rate of change | `applications/pdlc/graph/demand-flow.ttl` | Emil opens the issue |
| O-7 | **New issue.** Which method step builds the index: step 1, or step 3, which is not filed. The rate of change has no unit and no measure, and step 4's tick rate is not filed either | `method/01-map-and-index-acts.md`; `method/03-surface-decisions.md` | Emil opens the issue |
| O-8 | PR #73 rewrites prose under `applications/`. The survey's line numbers are `main`'s at `84aa466` | `survey.md` | Whoever lands second |
| O-9 | Carry R-2, R-4 and R-5 to Mantle's planning project. Mantle's ruling of 2026-11-17 is a view with a bound and no north | `DDD-address-08`, notes | Emil |
