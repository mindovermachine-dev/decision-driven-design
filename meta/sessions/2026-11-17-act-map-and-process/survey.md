# Survey — every use of "act map"

"Act map" stands on 109 lines in 38 files. The repository uses the word in three ways that do not agree, and it defines none of them.

| Question | What the uses say |
|---|---|
| One or many? | **One per mapped case.** No line has two maps of one case. The repository holds three cases, each with its own map: the dry run's T2a, the quick start's Varve slice, and the product lifecycle. Four lines name the SDLC's part of the lifecycle map as "the SDLC's act map", against seven that say the two files are one map |
| Tree or graph? | **Both, over different relations.** Containment is a tree: 11 lines, and the data enforces it. Dependency is a graph: 13 lines, and the data has acts with two and three incoming dependencies. Ten more lines read the map as a table with rows |
| Nodes? | **The claim says occurrences. The data says act sites.** `DDD-address-02` and step 1's card say "a tree of occurrences". `lc:Act` is "an act site of the map: one address, possibly many occurrences", and occurrences live in a separate record |

Read at `84aa466` (`main`), with canon at `v5.15.2`. The search was `grep -rnIiE "act[- ]maps?\b|actmap|act_map"` over the working tree, excluding `.git` and this session's directory.

## Findings

| # | Finding | Where |
|---|---|---|
| S-1 | **Only one filed sentence says what the act map is, and it is in a region, not a statement.** `DDD-address-02`'s region says the claim "governs the act map (a tree of occurrences)". Step 1's card repeats it. No claim, decision or term defines the act map | `core/claims/DDD-address-02.yaml:8`; `method/01-map-and-index-acts.md:62` |
| S-2 | **Containment is a tree in the data.** Every act sits within exactly one composite act (`lc:ActShape`, `lc:within`, at most one). The lifecycle map has one root, `m:PDLC` | `applications/pdlc/graph/shapes.ttl:29`; `applications/pdlc/graph/acts.ttl:17` |
| S-3 | **Dependency is not a tree in the data.** o1b has three incoming dependencies, scoped by kind. o2b and o12 have two each. `lc:readsEarlier` adds loops across issues: o2a reads earlier o13s | `applications/sdlc/acts/acts.ttl`; `applications/pdlc/graph/ontology.ttl:113` |
| S-4 | **The stream has a loop between act sites that the data leaves out.** The prose has o5 read "o4 (then o6)" and o6 read o5's report. The data gives o5 a dependency on o4 only. The loop is between occurrences: a later o5 reads an earlier o6. "Within an issue, dependencies are acyclic" therefore holds over occurrences, and over sites only because the edge is omitted | `applications/sdlc/sdlc.md:95`, `:106`, `:107`; `applications/sdlc/acts/acts.ttl:88` |
| S-5 | **Nodes are act sites in the data and occurrences in the claim.** `lc:Act` is a site with many occurrences. The occurrence record is a second artefact, merged with the map for checking. The quick start's rows are called occurrences and then used as sites ("if you run o3 again tomorrow, the new occurrence has o3's address") | `applications/pdlc/graph/ontology.ttl:33`; `applications/sdlc/acts/check.py:10`; `method/quick-start.md:77`, `:101` |
| S-6 | **Each case's map has its own declared ground axes.** T2a declares four. The quick start declares three. The lifecycle declares three (`DDD-dec-115`: "the act map's three axes"). No map uses two declarations, and no declaration serves two maps | `meta/sessions/2026-09-27-act-address/results-act-address-dry-run.md:31`; `method/quick-start.md:63`; `core/decisions/DDD-dec-115.yaml:5` |
| S-7 | **One map already holds several roots.** T2a's layer paths start at three different composite acts: delivery pipeline, operations, runtime. Emil accepted that map (act address landing, GATE 1 ruling 7; `DDD-dec-38`) | `meta/sessions/2026-09-27-act-address/results-act-address-dry-run.md:35` to `:37` |
| S-8 | **"Top act" is used and not filed.** `sdlc.md` names "the second top act: changes to the SDLC itself", and has o11 read changes "produced in other top acts". The second top act has no graph data: `m:PDLC` is the only root. Nothing says whether it belongs to the lifecycle map or to a second map | `applications/sdlc/sdlc.md:124`, `:451` |
| S-9 | **A sentence in `sdlc.md` §10 contradicts `DDD-ground-06`.** "Its acts sit at the same addresses with a different layer path." The layer path is part of the address, so two acts with different layer paths never share an address. They can share a ground position, which is coincidence (`DDD-address-04`). Flagged, not harmonised (`AGENTS.md`) | `applications/sdlc/sdlc.md:455` |
| S-10 | **A part is named as a map in four places.** "The SDLC's act map", "its act map", "the act map, o1b to o13". Each sits beside a sentence saying the two files are one map | `applications/sdlc/acts/acts.ttl:5`; `applications/sdlc/README.md:68`; `applications/sdlc/sdlc.md:89` |
| S-11 | **"Process" is used and not filed.** Canon at `v5.15.2` has no term for it. Downstream, Emil's Round 9 sentence "the SDLC is a subprocess under the PDLC" was ruled to read "the SDLC is a composite act within the PDLC". Step 1b uses the word 24 times without saying what one is, and its four claims wait on "a second process" | `core/decisions/DDD-dec-114.yaml:18`; `method/01b-map-the-flow-of-demand.md`; `core/claims/DDD-flow-01.yaml:73` |
| S-12 | **The SDLC holds no act directly.** Its members are four composite acts: frame, build, accept, land and run. Every SDLC act sits within one of those. The PDLC holds eight acts directly, and the SDLC | `applications/sdlc/acts/acts.ttl:126` to `:130` |

## The list

"One per mapped case" marks a line that names a map belonging to one case or one run of step 1. "One" marks a line that says "the act map" inside one case. "Not implied" means the line names the map and says nothing of its shape.

### In force: claims, decisions, the method, the applications

| File and line | One or many | Tree or graph | What the line says |
|---|---|---|---|
| `applications/README.md:7` | one | tree: containment | nesting is "a relation in the act map" |
| `applications/pdlc/README.md:21` | one | not implied | "the PDLC's acts on the act map": the PDLC has acts on it, not a map of its own |
| `applications/pdlc/README.md:29` | one | tree: containment | nesting is a relation in the map |
| `applications/pdlc/graph/acts.ttl:5` | one, held in two files | not implied | "the PDLC's acts on the act map"; "the two files are one map" |
| `applications/pdlc/graph/check.py:1` | one, held in two files | not implied | "the act map (PDLC and SDLC)" |
| `applications/pdlc/graph/check.py:138` | one | graph: dependency edges | "follows an edge of the act map" |
| `applications/pdlc/graph/check.py:155` | one | table: rows | "a seam is a row of the act map" |
| `applications/pdlc/graph/demand-flow.ttl:11` | one, held in two files | not implied | names both acts.ttl files |
| `applications/pdlc/graph/ontology.ttl:11` | one | tree and graph | the form: composite acts, act sites, causal dependencies |
| `applications/pdlc/graph/ontology.ttl:33` | one | not implied | "an act site of the map": the nodes are sites, not occurrences |
| `applications/pdlc/graph/ontology.ttl:54` | one | not implied | dct:source names "the act map" of Round 2 as where a term comes from |
| `applications/pdlc/graph/ontology.ttl:62` | one | not implied | dct:source names "the act map" of Round 2 as where a term comes from |
| `applications/pdlc/graph/ontology.ttl:64` | one | not implied | dct:source names "the act map" of Round 2 as where a term comes from |
| `applications/pdlc/graph/ontology.ttl:66` | one | not implied | dct:source names "the act map" of Round 2 as where a term comes from |
| `applications/pdlc/graph/ontology.ttl:69` | one | not implied | dct:source names "the act map" of Round 2 as where a term comes from |
| `applications/pdlc/graph/ontology.ttl:70` | one | not implied | dct:source names "the act map" of Round 2 as where a term comes from |
| `applications/pdlc/graph/ontology.ttl:71` | one | not implied | dct:source names "the act map" of Round 2 as where a term comes from |
| `applications/pdlc/graph/ontology.ttl:72` | one | not implied | dct:source names "the act map" of Round 2 as where a term comes from |
| `applications/pdlc/graph/ontology.ttl:73` | one | not implied | dct:source names "the act map" of Round 2 as where a term comes from |
| `applications/pdlc/graph/ontology.ttl:92` | one | not implied | dct:source names "the act map" of Round 2 as where a term comes from |
| `applications/pdlc/graph/ontology.ttl:93` | one | not implied | dct:source names "the act map" of Round 2 as where a term comes from |
| `applications/pdlc/graph/ontology.ttl:94` | one | not implied | dct:source names "the act map" of Round 2 as where a term comes from |
| `applications/pdlc/graph/ontology.ttl:106` | one | not implied | dct:source names "the act map" of Round 2 as where a term comes from |
| `applications/pdlc/graph/ontology.ttl:114` | one | not implied | dct:source names "the act map" of Round 2 as where a term comes from |
| `applications/pdlc/graph/ontology.ttl:124` | one | not implied | dct:source names "the act map" of Round 2 as where a term comes from |
| `applications/pdlc/graph/ontology.ttl:125` | one | not implied | dct:source names "the act map" of Round 2 as where a term comes from |
| `applications/pdlc/graph/ontology.ttl:195` | one | not implied | dct:source names "the act map" of Round 2 as where a term comes from |
| `applications/pdlc/graph/shapes.ttl:8` | one | not implied |  |
| `applications/pdlc/graph/shapes.ttl:252` | one | not implied |  |
| `applications/pdlc/graph/shapes.ttl:367` | one | graph: dependency edges | an edge is a dependency or an earlier reading |
| `applications/pdlc/graph/shapes.ttl:393` | one | table: rows | "a seam is a row of the act map"; the row is a producing act and a reading act joined by a dependency |
| `applications/pdlc/pdlc.md:152` | one | table: rows | the seam table is checked against it |
| `applications/pdlc/pdlc.md:156` | one, held in two files | not implied | names both acts.ttl files |
| `applications/pdlc/pdlc.md:566` | one | not implied | "the PDLC's acts on the act map" |
| `applications/pdlc/pdlc.md:568` | one, held in two files | not implied | "one map, validated together"; "the form of method step 1" |
| `applications/sdlc/README.md:68` | a part named as a map | not implied | "its act map": the SDLC's own |
| `applications/sdlc/acts/acts.ttl:5` | a part named as a map | not implied | "the SDLC's act map"; four lines later "the two files are one map" |
| `applications/sdlc/acts/acts.ttl:13` | one | tree: containment | "the act map's layers, read as composite acts" |
| `applications/sdlc/acts/check.py:1` | one | not implied | "the lifecycle act map" |
| `applications/sdlc/acts/check.py:6` | one | not implied |  |
| `applications/sdlc/acts/check.py:10` | one | not implied | the occurrence record is merged with the map: the map holds sites, not occurrences |
| `applications/sdlc/acts/shapes.ttl:16` | one | not implied |  |
| `applications/sdlc/sdlc.md:89` | a part named as a map | not implied | heading "The act map, o1b to o13"; the body says "one map" |
| `applications/sdlc/sdlc.md:118` | one | graph: dependency edges | readings from the causal index |
| `applications/sdlc/sdlc.md:665` | one | graph: dependency edges | dependencies scoped by kind |
| `applications/sdlc/sdlc.md:762` | one | not implied | another product's sessions would be "mapped onto the act map": one map that adopters share |
| `core/claims/DDD-address-02.yaml:8` | one | tree: containment | "a tree of occurrences"; the only claim that says what the map is |
| `core/claims/DDD-flow-03.yaml:14` | one, held in two files | not implied | names both acts.ttl files |
| `core/claims/DDD-flow-03.yaml:22` | one | tree and graph | traced on the map; the seam table has rows read at an act |
| `core/decisions/DDD-dec-114.yaml:20` | one | tree: containment | nesting is "a relation in the act map" |
| `core/decisions/DDD-dec-114.yaml:128` | one | table: rows | a seam listing is checked against it |
| `core/decisions/DDD-dec-115.yaml:5` | one | not implied | the map has three axes: one axis declaration |
| `core/decisions/DDD-dec-115.yaml:124` | one | not implied | "the act map's graph data" |
| `core/decisions/DDD-dec-115.yaml:185` | one | graph: dependency edges | readings from the causal index |
| `core/decisions/DDD-dec-38.yaml:55` | one per mapped case | not implied | "the T2a act map" |
| `method/01-map-and-index-acts.md:62` | one | tree: containment | "a tree of occurrences" |
| `method/01-map-and-index-acts.md:82` | one per mapped case | not implied | "this step's act map" |
| `method/01b-map-the-flow-of-demand.md:24` | one | graph: dependency edges | demand is traced across it |
| `method/01b-map-the-flow-of-demand.md:41` | one per mapped case | not implied | step 1's output |
| `method/01b-map-the-flow-of-demand.md:57` | one | graph: dependency edges | "along edges of the act map" |
| `method/01b-map-the-flow-of-demand.md:97` | one per mapped case | not implied | "your act map" |
| `method/01b-map-the-flow-of-demand.md:132` | one per mapped case | not implied | ground in |
| `method/01b-map-the-flow-of-demand.md:134` | one | not implied | graph data sits beside it |
| `method/01b-map-the-flow-of-demand.md:145` | one, held in two files | not implied | names both acts.ttl files |
| `method/01b-map-the-flow-of-demand.md:249` | one per mapped case | not implied |  |
| `method/quick-start.md:75` | one per mapped case | table: rows | a table, one row per occurrence, with the layer path as a column |

### Release notes

| File and line | One or many | Tree or graph | What the line says |
|---|---|---|---|
| `CHANGELOG.md:15` | one per mapped case | graph: dependency edges | demand is traced across it |
| `CHANGELOG.md:25` | one per mapped case | not implied | each specification carries its own |
| `releases/v0.7.0.yaml:41` | one per mapped case | graph: dependency edges | copy of CHANGELOG.md:15 |
| `releases/v0.7.0.yaml:51` | one per mapped case | not implied | copy of CHANGELOG.md:25 |

### Session records (history, never edited)

| File and line | One or many | Tree or graph | What the line says |
|---|---|---|---|
| `meta/sessions/2026-09-27-act-address-landing/gate1-rulings.md:15` | one per mapped case | not implied | the T2a map is accepted |
| `meta/sessions/2026-09-27-act-address-landing/gate1-survey.md:145` | one per mapped case | not implied |  |
| `meta/sessions/2026-09-27-act-address-landing/gate1-survey.md:148` | one per mapped case | not implied | axes and five occurrences |
| `meta/sessions/2026-09-27-act-address-landing/gate1-survey.md:174` | one per mapped case | not implied |  |
| `meta/sessions/2026-09-27-act-address-landing/prompt.md:48` | one per mapped case | not implied |  |
| `meta/sessions/2026-09-27-act-address/prereg-act-coordinates.md:26` | one | tree: containment | R-6: "a tree of occurrences" |
| `meta/sessions/2026-09-27-act-address/prereg-act-coordinates.md:77` | one | tree: containment | "a tree of unique occurrences" |
| `meta/sessions/2026-09-27-act-address/prereg-act-coordinates.md:108` | one per mapped case | not implied | "its act map": the first independent case has its own |
| `meta/sessions/2026-09-27-act-address/results-act-address-dry-run.md:7` | many (plural) | not implied | "the act maps below": one per case |
| `meta/sessions/2026-09-27-act-address/results-act-address-dry-run.md:11` | one per mapped case | not implied | the map depends on the axes the mapper declared |
| `meta/sessions/2026-09-27-act-address/results-act-address-dry-run.md:31` | one per mapped case | table: rows | a table of occurrences under its own four declared axes; its layer paths start at three different roots |
| `meta/sessions/2026-09-27-act-address/results-act-address-dry-run.md:70` | one per mapped case | not implied |  |
| `meta/sessions/2026-09-27-act-address/rulings.md:27` | one per mapped case | not implied | "the T2a act map's axis declarations" |
| `meta/sessions/2026-11-02-ready-to-try/predictions.md:378` | one per mapped case | not implied | the quick start's map |
| `meta/sessions/2026-11-02-ready-to-try/predictions.md:421` | one per mapped case | table: rows | the quick start's map, counted in rows |
| `meta/sessions/2026-11-07-sdlc-and-pdlc/findings.md:10` | one | graph: dependency edges | an order between two acts |
| `meta/sessions/2026-11-07-sdlc-and-pdlc/findings.md:19` | one | graph: dependency edges | causal-index readings |
| `meta/sessions/2026-11-07-sdlc-and-pdlc/predictions.md:57` | one | not implied | a record is merged with the map: the map holds sites, not occurrences |
| `meta/sessions/2026-11-07-sdlc-and-pdlc/prompt-2.md:208` | one | table: rows | a row is checked against the map |
| `meta/sessions/2026-11-07-sdlc-and-pdlc/prompt-2.md:240` | one | not implied | "the act map, the occurrence record": two things |
| `meta/sessions/2026-11-07-sdlc-and-pdlc/prompt.md:35` | one | not implied |  |
| `meta/sessions/2026-11-07-sdlc-and-pdlc/prompt.md:197` | one | tree: containment | nesting is "a relation in the act map" |
| `meta/sessions/2026-11-07-sdlc-and-pdlc/prompt.md:314` | one | not implied | the o1 to o15 map |
| `meta/sessions/2026-11-07-sdlc-and-pdlc/prompt.md:373` | one | not implied | "the act map's form" |
| `meta/sessions/2026-11-07-sdlc-and-pdlc/prompt.md:438` | one | table: rows | seam rows are checked against it |
| `meta/sessions/2026-11-07-sdlc-and-pdlc/prompt.md:478` | one | not implied | "the PDLC's acts on the act map" |
| `meta/sessions/2026-11-07-sdlc-and-pdlc/prompt.md:498` | one | not implied |  |
| `meta/sessions/2026-11-07-sdlc-and-pdlc/prompt.md:504` | a part named as a map | not implied | "the act map for o1b to o13" |
| `meta/sessions/2026-11-07-sdlc-and-pdlc/rulings.md:39` | one | not implied |  |
| `meta/sessions/2026-11-07-sdlc-and-pdlc/rulings.md:201` | one | tree: containment | nesting is "a relation in the act map" |
| `meta/sessions/2026-11-07-sdlc-and-pdlc/rulings.md:576` | one | graph: dependency edges | causal-index readings |
| `meta/sessions/2026-11-07-sdlc-and-pdlc/rulings.md:710` | one | tree: containment | R-9, the ruled reading |
| `meta/sessions/2026-11-07-sdlc-and-pdlc/rulings.md:717` | one | graph: dependency edges | causal-index readings |
| `meta/sessions/2026-11-07-sdlc-and-pdlc/rulings.md:719` | one | table: rows | the seam table is checked against it |
| `meta/sessions/2026-11-07-sdlc-and-pdlc/rulings.md:739` | one | not implied | the o1 to o15 map, verbatim |
| `meta/sessions/2026-11-08-demand-flow/findings.md:41` | one | not implied |  |
| `meta/sessions/2026-11-08-demand-flow/successor-items.md:14` | one | not implied |  |
| `meta/sessions/README.md:53` | one | not implied | "the lc: act map" |
| `meta/sessions/README.md:55` | one | not implied |  |
