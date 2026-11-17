# Proposals, second form — after R-2, R-3 and R-4

The three definitions as they stand after Emil's rulings of 2026-11-17. This file supersedes `proposals.md`, which is kept as written. Nothing here is filed.

| # | Definition | Ruled so far | Still to rule |
|---|---|---|---|
| D-1 | **The act map** is the record of one ruled decomposition under one declaration of ground axes. It holds act sites, the composite acts above and below them, the dependencies between them, and the index of determinables | Layers are composite acts and nothing else (E-2). The index is of determinables (R-3) | Nodes are sites. "Top act". Whether the index is part of the map |
| D-2 | **A second act map** exists when, and only when, a second declaration of ground axes exists | Nothing | The whole rule |
| D-3 | **A process** is a human understanding of work, scoped to an area of expertise. Its translation into the model is a view of an act map: the acts between one unresolved determinable and the determinate that discharge produces | North is the unresolved determinable; the discharge act is the other end (R-2). A process is a human concept, and this is its best translation (R-4) | The wording. Whether the view leaves out earlier readings |

Arguments below that Emil has not confirmed are `UNVERIFIED — Emil review`.

## D-1 — the act map

**Definition.** The act map is the record of one ruled decomposition of work into acts, read under one declaration of ground axes. It holds four things:

| Part | What it is | Source |
|---|---|---|
| Act sites | One site per address: a ground position on the declared axes and a layer path. The occupant is not part of it | `DDD-ground-06` |
| Layers | Composite acts above an act and below it. There is no other kind of layer. A top act is a composite act with none above it | `DDD-ground-06`; `core/09` §1; E-2 |
| Dependencies | Site B depends on site A when a state change an occurrence at A produced is in the ground reading of an occurrence at B. A directed graph | `DDD-address-01` |
| The index of determinables | Every determinable that makes demand arrive, with the act where it enters and the act where its determinate lands. Each is marked taken up, which makes it a decision anchored to acts, or not taken up, which makes it a candidate escape | `DDD-frame-13`; `core/00` §4a; R-3 |

The map has no direction of its own beyond causal order. A view gives it one by naming a north: one determinable from the index (E-1, R-2).

Occurrences are not in the map. Each is recorded against one site, with its time index.

**Weakest point.** Two, of different kinds.
1. `DDD-address-02`'s region says "a tree of occurrences". This says the nodes are sites. Unchanged from `proposals.md`.
2. The index is new, and nothing in the repository has one. The lifecycle's six sources of pull are the nearest thing: each names an entry act and a discharge act, and none is marked taken up or not. So the fourth part is defined before it has been built once.

**Rests on.** `DDD-ground-06`, `DDD-address-01`, `DDD-address-02`, `DDD-frame-13` (all projected); `core/00` §4a; the `lc:` vocabulary (Round 28, R30); E-2 and R-3 of this session. "Top act" and "occurrences sit outside the map" rest on **no claim**.

**Falsifier.** Any of:
1. An act site that must sit within two composite acts for its governing set to be stated.
2. A dependency that can be stated between two occurrences and between no two sites.
3. A determinable that makes demand arrive and that cannot be given an entry act on the map. This limb also yields a finding: work the decomposition does not cover.

**What it breaks.** Limb 1: the layer path and `DDD-ground-06`'s "exactly one address". Limb 2: the split between map and occurrence record. Limb 3: the claim that the map shows the pull at all.

## D-2 — when a second act map exists

Unchanged from `proposals.md`, and not yet ruled.

**Rule.** A second act map exists when, and only when, a second declaration of ground axes exists. A second top act under the same declaration is a second tree in the same map. A view is not a second map.

**Weakest point.** Whether two pieces of work share a declaration is the mapper's decision. The rule names it and does not make it.

**Rests on.** `DDD-ground-06`'s region; `DDD-address-04`; the accepted T2a map (`DDD-dec-38`), which has three roots under one declaration. That the declaration is the boundary rests on **no filed claim or ruling**.

**Falsifier.** A governing decision whose applicability predicate must cover occurrences in two maps, or two occurrences in two maps whose behaviour must be compared.

**What it breaks.** Checking a map on its own, and the two grains of `DDD-address-05`.

## D-3 — a process

**Definition.** A process is a human understanding of work being done. It is scoped and settled within an area of expertise, such as software, finance or HR. It is not an object of the model.

Its translation into the model is a view of an act map, fixed by one north:

| Part of the view | What it is | Source |
|---|---|---|
| North | One unresolved determinable: the cause, where demand originates. It exists whether or not anyone has taken it up | `DDD-frame-13`; `core/00` §4a; R-2 |
| The other end | The act at which discharge produces the determinate | `core/09` §7a; R-2 |
| The acts shown | The act sites on a dependency path from the determinable's entry act to that discharge act | `DDD-address-01` |
| Rank | Distance from north along dependencies | E-1 |

The translation is the passage from determinable to determinate (`core/00` §4a), read over a chain of acts. It may cross composite acts.

**Weakest point.** A process is settled inside one area of expertise, so there is no fact against which the translation can be wrong. It can only be more or less useful to the people who hold the process. The falsifier below is therefore a test of utility, as `DDD-address-02`'s is, and weaker than a test of fact.

**What this settles without a new ruling.**
- **Round 9.** "The SDLC is a subprocess under the PDLC" is software's own word for its work. Its ruled reading in the model, a composite act within the PDLC, stands (`DDD-dec-114`). Nothing is superseded.
- **The lifecycle.** The six sources of pull are six norths. The SDLC is a composite act that several views pass through.
- **Mantle.** "A composite act that holds acts directly" is another translation of the same human concept, made for display. Whether Mantle keeps it is ruled in Mantle's project.

**Rests on.** R-2 and R-4 of this session; `DDD-frame-13`; `core/00` §4a; `core/09` §7a; `DDD-address-01`. "Process" has no filed term, here or upstream.

**Falsifier.** Either:
1. A process its holders recognise that has no north: no determinable in the world starts it. Work that starts only because an earlier decision scheduled it is the candidate. The holding note `meta/holding-note-addendum-determinables.md` Q36 (upstream, not ratified) calls that ledger-pull.
2. A view that the holders of the process do not recognise as their process, in a second mapped case.

**What it breaks.** Step 1b's use of "a process" as its unit, and the promotion condition of `DDD-flow-01` to `-04` ("a second process").

## Where to file — proposed, not ruled

| What | Where | Form |
|---|---|---|
| The rulings of this session | `core/decisions/DDD-dec-122.yaml` | One decision. `basedOn` the claims below, `DDD-ground-06`, `DDD-frame-13`, `DDD-address-01`, `DDD-dec-114`, `-38` |
| D-1, the act map | `core/claims/DDD-address-06.yaml` | Conceptual, projected. Test: T2b |
| D-2, a second act map | `core/claims/DDD-address-07.yaml` | Normative, projected |
| D-3, a process | `core/claims/DDD-address-08.yaml` | Normative, projected |
| Pointers | `method/01-map-and-index-acts.md`, "Artefact out"; `method/01b-map-the-flow-of-demand.md`, first use of "process" | One cited sentence each |

Not proposed: the term registry, the `lc:` vocabulary, upstream, and any change to the lifecycle's acts or sources of pull.

## What the rulings would leave open

| # | Item |
|---|---|
| O-1 | `DDD-address-02`'s region says "a tree of occurrences" |
| O-2 | `sdlc.md` §10: the second top act has no graph data, and one sentence contradicts `DDD-ground-06` (S-8, S-9) |
| O-3 | Four places call the SDLC's part "the act map" (S-10) |
| O-4 | The o5 and o6 loop is left out of the data (S-4) |
| O-5 | New demand declares oC as an entry act, and no dependency leads from oC towards o16 for new demand (`rulings.md`, evidence) |
| O-6 | The lifecycle has no index of determinables. Its six sources of pull are not marked taken up or not. Building the index changes the lifecycle data, which this issue puts out of scope |
| O-7 | Which step builds the index: step 1, or step 3, which is not filed |
| O-8 | PR #73 rewrites prose under `applications/`. The survey's line numbers are `main`'s at `84aa466` |
| O-9 | Carry R-2 and R-4 to Mantle's planning project |

## For G1

1. D-1: are the map's nodes act sites, with occurrences recorded beside it?
2. D-1: is the index of determinables a part of the act map?
3. D-2: is the rule ruled as written?
4. D-3: is the wording ruled as written? Does a view leave out earlier readings (`lc:readsEarlier`), so that rank is strict?
5. Filing: one decision and three claims in the address area?
6. Scope: definitions only in this session, with O-6 and O-7 as new issues?
7. Is there a GitHub issue number for the commits?

## Amendments

Added after the file was first committed. The sections above are left as written.

### A-1 — D-3 after R-5 and E-5

**Definition, as amended.** A process is a human understanding of work being done, scoped and settled within an area of expertise. It is not an object of the model. Its translation into the model is a **named view** of an act map, fixed by:

| Part | What it is | How many |
|---|---|---|
| Norths | Unresolved determinables: the causes the work answers | One or more |
| Bound | Composite acts the view is limited to | None, one or more |

The view shows the act sites on a dependency path from each north's entry act to the act where its determinate lands, inside the bound where one is given.

**Why two parts.** People name a process by where the work happens and who holds it, and by why it happens. The model keeps those apart: the first is composite acts, the second is norths. The SDLC is a bound with the norths that end at its discharge act. The PDLC is one bound with six norths.

**In tooling.** A process is a saved view with a name. It is never a node, so no decision can be anchored to it.

**Falsifier, as amended.** Limb 1 of D-3 ("a process with no north", with calendar-started work as the candidate) is withdrawn on E-5: time makes a determinable unresolved again, so calendar-started work has a north. What remains:

1. A view that the holders of the process do not recognise as their process, in a second mapped case.
2. A process whose holders cannot name any determinable it answers, after the calendar is set aside.

**Weakest point, added.** If time is the cause of every determination, then "time" cannot tell one north from another. What tells them apart is which determinable time moves, and how fast. So north stays the determinable, and a north's rate of change is a property the index may need. Nothing filed says so.

**Rests on.** R-2, R-4, R-5 and E-5 of this session; `DDD-frame-13`; `core/00` §4a; `DDD-address-01`; `DDD-ground-06` for the bound.

**Effect on Mantle.** "A composite act that holds acts directly" is a view with a bound and no north. It is a case of this definition, not a rival to it. Whether Mantle keeps it is ruled there (O-9).

### A-2 — D-1 after R-6

**The index of determinables, as amended.** Each determinable in the index carries a fourth property beside its entry act, its discharge act and whether it is taken up: its **rate of change**, the rate at which time makes it unresolved again. That rate is what creates demand (R-6).

**What it gives.** A north's rate of change says how often the work recurs. The lifecycle writes this on acts, as free text (`lc:recurs "per issue"`, `"per event"`). On R-6 it is a property of the cause first, and the acts inherit it.

**Weakest point.** No filed claim carries a rate of change for a determinable. The method's step 4, which is `[PROPOSED]` and not filed, speaks of declaring ground with its tick rate. So this property is defined here before it has a unit or a way to measure it.

**Falsifier.** A determinable whose demand recurs at a rate that its own rate of change does not explain, for example work that recurs because an act upstream failed and not because the world moved. That is owed demand in the lifecycle, and it may need a rate of its own.

**Rests on.** R-6 and E-5 of this session; `DDD-frame-13`. On no filed claim for the rate itself.
