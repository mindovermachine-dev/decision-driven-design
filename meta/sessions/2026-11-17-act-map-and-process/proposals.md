# Proposals — the act map, a second act map, a process

Three definitions, `[PROPOSED]`. Nothing here is filed. Emil rules each one, and where it is filed, at G1.

| # | Proposal | Rests on | Weakest point |
|---|---|---|---|
| D-1 | **The act map** is the record of one ruled decomposition under one declaration of ground axes. It holds act sites. It has two relations: containment, which is a tree under each top act, and causal dependency, which is a directed graph | `DDD-ground-06`; `DDD-address-01`; `DDD-address-02`; the `lc:` vocabulary (Round 28, R30) | It says "sites" where `DDD-address-02`'s region says "occurrences" |
| D-2 | **A second act map** exists when, and only when, a second declaration of ground axes exists. A second top act under the same declaration is a second tree in the same map | `DDD-ground-06`'s region; `DDD-address-04`; the accepted T2a map | Whether two pieces of work share a declaration is the mapper's decision. The rule names the decision. It does not make it |
| D-3 | **A process** is a composite act. Mantle's ruling is its limiting case, with depth fixed at one | `DDD-dec-114` (Round 9, ruled reading); `DDD-ground-06` | It adds a second word for a filed term and no new content |

Every argument below that Emil has not confirmed is `UNVERIFIED — Emil review`. That is all of them.

## D-1 — the act map

**Definition.** The act map is the record of one ruled decomposition of work into acts, read under one declaration of ground axes. It holds:

| Part | What it is | Shape | Source |
|---|---|---|---|
| Act sites | One site per full address: a ground position on the declared axes and a layer path. The occupant is not part of it | Nodes | `DDD-ground-06` |
| Containment | Each act site and each composite act sits within at most one composite act. A composite act within none is a **top act** | A tree under each top act. A forest when there is more than one top act | `DDD-ground-06` (the layer path); `DDD-address-02` (no act is shared) |
| Dependency | Site B depends on site A when a state change an occurrence at A produced is in the ground reading of an occurrence at B | A directed graph. Not a tree | `DDD-address-01` |

Occurrences are not in the map. Each occurrence is recorded against exactly one site, with its time index. The record of occurrences is a second artefact.

**Weakest point.** `DDD-address-02`'s region and step 1's card say "a tree of occurrences". This definition says the nodes are sites. The claim's statement is untouched: every occurrence is still its own act, and no act has two parents. But a ruled region is being read more narrowly than it is written, and ruled material changes by supersession. If Emil holds that the map's nodes are occurrences, then the lifecycle's `acts.ttl` is not an act map, because `lc:Act` is a site (S-5).

**Why "tree or graph" has two answers.** The survey finds 11 lines that need a tree and 13 that need a graph. They are about different relations. "A tree of occurrences" (R-6) rules out one act under two parents. "Follows an edge of the act map" (`lc:` shapes) walks dependencies. Neither can be given up: the layer path needs the tree, and step 1b and the fan-out query need the graph.

**Rests on.**
- `DDD-ground-06` (upstream, projected): the address, the layer path, and "addresses are relative to a ruled decomposition".
- `DDD-address-01` (projected): dependency over ground readings.
- `DDD-address-02` (projected): every occurrence is its own act.
- The `lc:` vocabulary, ruled by Round 28 (R30): `lc:Act` as a site, `lc:within`, `lc:dependency`.
- "Top act" rests on **none**. It is used in `sdlc.md` §3 and §10 and is not filed (S-8). This definition would file it.
- That occurrences sit outside the map rests on the `lc:` data and on **no claim**.

**Falsifier.** Any of:
1. An act site that must sit within two composite acts for its governing set to be stated.
2. A dependency that can be stated between two occurrences and between no two sites.
3. A question about the work that the sites and the occurrence record together cannot answer, and a single tree of occurrences can.

**Pressure case already in the repository.** S-4: a later o5 reads an earlier o6, and o6 reads o5. Between sites that is a loop. The data omits one edge to keep sites acyclic. Limb 2 does not fire, because the dependency can be stated between sites. But "dependencies are acyclic" is true of occurrences and not of sites, and the definition must not claim otherwise.

**What it breaks.** If limb 1 fires: `lc:ActShape`, the uniqueness of the layer path, and `DDD-ground-06`'s "exactly one address". If limb 2 or 3 fires: the split between map and record, and with it the lifecycle graph data and Mantle's reading of it.

## D-2 — when a second act map exists

**Rule.** A second act map exists when, and only when, a second declaration of ground axes exists. Two act sites belong to one map exactly when their ground positions are read on the same declared axes, under the same ruled decomposition.

| Case | One map or two | Why |
|---|---|---|
| The PDLC's acts and the SDLC's acts, in two files | One | One declaration: surface read, change locus, authority read (`DDD-dec-115`) |
| A second top act under the same axes, such as changes to the SDLC itself (`sdlc.md` §10) | One, with two trees | Same declaration. T2a already has three roots in one accepted map (S-7) |
| The quick start's Varve slice and the lifecycle | Two | Different declarations |
| The same work, decomposed a second way | One at a time | Re-decomposition supersedes (`DDD-ground-06`'s region). The old map is history |
| A part of a map, such as o1b to o13 | Not a map | It is the acts within one composite act of the map (S-10) |

**Why the axes decide.** An address is a position on declared axes. Coincidence is equality of ground positions (`DDD-address-04`). Applicability predicates range over positions (`DDD-ground-01`). None of the three is defined between two declarations. So the boundary of a map is the boundary of what can be compared and governed together. Between two maps only one relation remains: an act in one reads state that an act in the other produced.

**Weakest point.** Whether two pieces of work share a declaration is decided by whoever rules the decomposition. Any two maps can be made one by declaring the union of their axes. Then some acts never read some axes, which is the held T2b test item F-1: "an act that never reads an axis … is coverage, not a position". So the rule says what a second map is and what it costs. It does not say when to make one.

**The alternative, for the ruling.** One map per top act. It is simpler to state, and it matches "the SDLC's act map" in four places. It fails on the accepted T2a map, which has three roots (S-7). It would also make the changes to the SDLC a second map whose acts are compared with the first at every o11, across a boundary where comparison is not defined.

**Rests on.**
- `DDD-ground-06`'s region: axes are declared, and addresses are relative to a ruled decomposition.
- `DDD-address-04`: coincidence at ground position.
- Act address landing, GATE 1 ruling 7 (`DDD-dec-38`): the T2a map accepted.
- `DDD-dec-115`: the lifecycle map's three axes.
- That the axis declaration is the boundary rests on **no filed claim or ruling**. It is this session's reading of S-6.

**Falsifier.** Either:
1. A governing decision whose applicability predicate must cover occurrences in two maps.
2. Two occurrences in two maps whose behaviour must be compared (`DDD-address-05`) to answer a question the work poses.

Each shows a split that loses governance. The second application case will test it: an organisation mapped beside the PDLC either shares the PDLC's axes or does not.

**What it breaks.** Checking a map on its own (`check.py`). The two grains of `DDD-address-05`, which assume one address space. Any tool that points from one map at acts in another.

## D-3 — a process

**Definition.** A process is a composite act. A subprocess is a composite act within another. A process's acts are the act sites whose layer paths pass through it.

**Mantle's ruling as the limiting case.** "A process is a composite act that holds acts directly" is this definition with depth fixed at one: the members shown are the acts one step below. Mantle's view may keep it. This repository cannot adopt it as written:

| Composite act | Holds acts directly | A process under Mantle's ruling | Called a process in this repository |
|---|---|---|---|
| PDLC | Yes: o0, o2a, oS, o1, oC, oR, o16, oU | Yes | Yes (`DDD-dec-118`; step 1b) |
| SDLC | **No.** It holds frame, build, accept, land and run | **No** | **Yes.** Round 9: "the SDLC is a subprocess under the PDLC". Round 5: "the process of getting changes to production" (`DDD-dec-114`) |
| frame, build, accept, land and run | Yes | Yes | No. They are "stages" (`acts.ttl`) |

Adopting the ruling as written would un-name the SDLC as a process, or require moving its acts, which is out of scope.

**Weakest point.** The definition adds nothing canon lacks. "Process" becomes a reader's word for "composite act". If Emil means more by a process (owners, declared kinds of demand, an entry and a discharge), this definition is too weak, and step 1b is where the stronger one would come from. I found no ruling that asks for more.

**The alternative, for the ruling.** A process is a composite act that declares kinds of demand, with an entry act and a discharge act for each (step 1b's unit). It separates the PDLC from "frame". It rests on `DDD-dec-118` and on four projected claims with one process as their whole evidence, so it would define a general word from one case.

**Rests on.**
- `DDD-dec-114`: Round 9, with the reading ruled in Round 14, already equates a subprocess with a composite act within another.
- `DDD-ground-06` and `term:act-address`: composite acts and the layer path.
- "Process" itself rests on **no filed claim or term**, here or upstream.
- Mantle's ruling is taken from the issue text. This session has not read Mantle's planning project.

**Falsifier.** A use of "process" in this repository, or in a mapped case, that names something no composite act can be: work with no containing act, or a flow that crosses two top acts and belongs to neither.

**What it breaks.** Step 1b's wording ("each process declares its own kinds of demand") and the promotion condition of `DDD-flow-01` to `-04` ("a second process"), which would then have no defined subject.

## Where to file — proposed

| What | Where | Form |
|---|---|---|
| The rulings of G1 | `core/decisions/DDD-dec-122.yaml` | One decision, `basedOn` the claims below and `DDD-dec-114`, `-115`, `-38` |
| D-1, the act map, with "top act" | `core/claims/DDD-address-06.yaml` | Conceptual, projected. Test: T2b |
| D-2, a second act map | `core/claims/DDD-address-07.yaml` | Normative, projected, as `DDD-address-02` is: a governing choice about representation |
| D-3, a process | `core/claims/DDD-address-08.yaml` | Normative, projected |
| Pointers | `method/01-map-and-index-acts.md`, "Artefact out" row; `method/01b-map-the-flow-of-demand.md`, first use of "process" | One cited sentence each |

Not proposed:
- **The term registry.** `core/graph/terms.yaml` holds terms established by numbered core documents. None of the three is.
- **The `lc:` vocabulary.** It is ruled, and an `lc:Process` class would add a second name for `lc:CompositeAct`.
- **Upstream.** Out of scope. The act map is diachronic, so it files downstream by `DDD-dec-09`'s charter in any case.

## What the rulings would leave open

| # | Item | From |
|---|---|---|
| O-1 | `DDD-address-02`'s region says "a tree of occurrences". If D-1 is ruled, the region is superseded or annotated, not rewritten | D-1 |
| O-2 | `sdlc.md` §10: the second top act has no graph data, and "the same addresses with a different layer path" contradicts `DDD-ground-06` | S-8, S-9 |
| O-3 | Four places call the SDLC's part "the act map" | S-10 |
| O-4 | The o5 and o6 loop is left out of the data | S-4 |
| O-5 | PR #73 rewrites prose under `applications/`. The survey's line numbers are `main`'s at `84aa466` | `bootstrap.md` |

## For G1

1. D-1: are the map's nodes act sites, with occurrences in a record beside it?
2. D-1: is "top act" filed, as a composite act within no other?
3. D-2: does the axis declaration bound a map, or does each top act have its own?
4. D-3: is a process any composite act, with Mantle's ruling as the depth-one view?
5. Filing: one decision and three claims in the address area, or another form?
6. Is there a GitHub issue number for the commits?
