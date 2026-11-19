# Proposals for G1

Six claims and one decision, written once with the rulings of both days in them. Three claims keep their ids and are amended before landing (2026-11-18 R-8): `DDD-address-06`, `-07` and `-08`. Three are new: `DDD-address-09` to `-11`. The decision keeps `DDD-dec-122`. Nothing here is filed. Every statement below is `[PROPOSED]` until Emil rules it.

Each proposal gives its weakest point first, then the statement, the falsifier, what it breaks and what it rests on. "Rests on" names filed claims, rulings or nothing. Ruling numbers are by day: "11-17 R-7" is R-7 of `meta/sessions/2026-11-17-act-map-and-process/rulings.md`, and "11-18 R-2" is R-2 of `meta/sessions/2026-11-18-pull-and-scope/rulings.md`.

| # | Id | What | Kind | Status proposed |
|---|---|---|---|---|
| P-1 | `DDD-address-06` | The act map, with its scope and its index | conceptual | projected |
| P-2 | `DDD-address-07` | When a second act map exists | normative | projected |
| P-3 | `DDD-address-08` | A process, and north | normative | projected |
| P-4 | `DDD-address-09` | The pull | conceptual | projected |
| P-5 | `DDD-address-10` | Kinds of demand as ground positions | conceptual | projected |
| P-6 | `DDD-address-11` | The four states | conceptual | projected |
| P-7 | `DDD-dec-122` | The decision that files them | decision | — |
| P-8 | — | The two statements of #80 that are stated, not ruled | — | — |

## P-1 — `DDD-address-06`, the act map, amended

**Weakest point.** The scope is declared before any act is mapped, as a set of decisions. The map's layers are composite acts, found only after. Nothing makes the scope's edge fall on composite acts. If it does not, a composite act straddles the edge, and its seam decisions are half inside and half world.

**Statement.** The act map is the record of one ruled decomposition of the work inside one declared scope into acts, read under one declaration of ground axes, and it holds the act sites at their addresses, the composite acts that layer them, the causal dependencies between them and the index of the determinables that make demand arrive in its scope.

**Region, in brief.**

| Part | What it is | Rests on |
|---|---|---|
| Scope | The map's first declaration: the decisions its holders take. Everything outside is world to the map, including other people's decisions. A decision outside reaches the map only as ground crossing its edge | 11-18 R-2 |
| Act sites | One site per address: a ground position on the declared axes and a layer path. The occupant is left out. Occurrences are recorded beside the map, each against exactly one site, with its time index | `DDD-ground-06`; `DDD-address-01`; 11-17 R-7 point 1 |
| Layers | Composite acts above an act and below it, and no other kind of layer | 11-17 E-2; `DDD-ground-06` |
| Dependencies | B depends on A when a state change an occurrence at A produced is in the ground reading of an occurrence at B. A directed graph, not a tree | `DDD-address-01` |
| The index of determinables | One row per determinable at or inside the edge: its outcomes, its entry act, the act where its determinate lands, its specified, observed and expected states (actual is never read), its kind as a ground position, and its rate of change. A row whose specified state cites a decision in force is taken up | 11-17 R-3, R-6, R-7 point 2; 11-18 R-1, R-4, R-5 |

The index's observed state is a pointer to the latest observation in the occurrence record, not a copy. The map stays structure. The record holds what changes.

**Falsifier.** Any of: an act site that must sit within two composite acts for its governing set to be stated; a dependency that can be stated between two occurrences and between no two sites; a determinable that makes demand arrive in the scope and can be given no entry act on the map; or a composite act that cannot be placed wholly inside or wholly outside the declared scope.

**Breaks.** The first three limbs break what they broke on 2026-11-17: the layer path, the split between map and record, and the claim that the map shows the pull. The fourth breaks scope as a declaration made before acts, and with it part 1 of the pull procedure.

**Rests on.** `DDD-ground-06`, `DDD-ground-05`, `DDD-frame-13` (upstream, projected); `DDD-address-01` (projected). 11-17 E-2, R-3, R-6, R-7; 11-18 R-1, R-2, R-4, R-5. The fourth falsifier limb and the observed pointer rest on **no ruling**.

**Notes it carries.** First drafted on 2026-11-17 on a branch that did not land, and amended on the rulings of 2026-11-18 (11-18 R-8). The 2026-11-17 text is on the archive branch at `47cf4cc`.

## P-2 — `DDD-address-07`, when a second act map exists, amended

**Weakest point.** **The two days' rulings conflict, and only Emil can settle it.** 11-17 R-7 point 3 rules that a second act map exists "when, and only when, a second declaration of ground axes exists". 11-18 R-2 rules scope the first declaration of a map, and R-3 speaks of a narrow scope's map and a wider map. The SDLC and the PDLC share one declaration of axes (`DDD-dec-115`). So under the 2026-11-17 wording, a map with the How as its scope and the PDLC's map are one map. Under R-3 they are two.

**Two options.**

| | Option A (recommended) | Option B |
|---|---|---|
| Statement | A second act map exists when, and only when, a second declaration exists: a second scope, or a second declaration of ground axes over one scope | As 2026-11-17: when, and only when, a second declaration of ground axes exists. A narrower scope under the same axes is a scope declared within the one map |
| R-3 reads as | Two maps: the narrow one and the wider one. The narrow scope's pull appears in the wider map as a dependency, and as a seam only where the wider map declares the narrow scope | One map, with nested scopes. "A wider map" means the map seen at its wider scope |
| What it supersedes | The wording of 11-17 R-7 point 3 | Nothing. But "everything outside the scope is world" then holds of a scope, not of a map |
| The lifecycle | Unchanged. `pdlc.md` §11's "one map, validated together" is one map with the PDLC as its scope, and the How declared within it | Unchanged |
| Weakest point of its own | It supersedes a ruled sentence | 11-18 R-2 calls scope "the first declaration of a map", which B demotes to a declaration within one |

**Region, in brief, under A.** Two act sites belong to one map exactly when they are inside one declared scope and their positions are read on the same declared axes, under one ruled decomposition. A part of a map, such as the acts within one composite act, is not a map. A view is not a map. A wider map may declare a narrower scope within it. A pull of the narrower scope then shows as a seam at its edge. Where the wider map does not declare it, the pull shows as a dependency only (11-18 R-3).

**Falsifier.** Unchanged in form: a governing decision whose applicability predicate must cover occurrences in two maps, or two occurrences in two maps whose behaviour must be compared to answer a question the work poses. Under A it adds: two maps of nested scopes whose shared acts carry different addresses.

**Breaks.** Checking a map on its own (`applications/pdlc/graph/check.py`); the two grains of `DDD-address-05`; under A, any reading of the PDLC and the SDLC as one map that is then given two scopes.

**Rests on.** 11-17 R-7 point 3; 11-18 R-2 and R-3; `DDD-ground-06`'s region; `DDD-address-04`; `DDD-dec-38` (the T2a map, three top acts under one declaration). That scope individuates a map rests on **no ruling** under either option until Emil rules Q-2.

## P-3 — `DDD-address-08`, a process and north, amended

**Weakest point.** "Unresolved" is now read as "two of the determinable's states disagree". A determinable can be unresolved with no gap anyone can read: actual differs from observed and nobody has looked. Such a north exists and no view can be fixed by it until someone observes.

**Statement.** A process is a human understanding of work, scoped within an area of expertise and not an object of the model, and its translation into the model is a named view of one act map, fixed by one or more norths and optionally bounded by composite acts inside the map's scope, where a north is a determinable in the map's index that is unresolved: the determinable of a pull.

**What changes from 2026-11-17.** Three things, each from a ruling of 2026-11-18.
- "Whether or not governance has taken it up" now means the governance inside the scope (#80, "State at opening"). A decision outside the scope is world, so a north may be taken up outside and still be a north of the map.
- A north is the determinable of a pull (P-4). The view runs from each north's entry act to the act where its determinate lands, both inside the scope.
- The bound lies inside the scope. A view cannot reach outside its map.

Unchanged from 2026-11-17: a north is a cause, not a decision; the discharge act is the other end; time sets a determinable's rate of change, which is what creates demand; a view leaves out earlier readings; in tooling a process is a saved view, never a node.

**Falsifier.** A view that the holders of a process do not recognise as their process; or a process whose holders can name no determinable it answers, once the calendar is set aside; or a process its holders recognise whose work answers no gap between any two states.

**Breaks.** Step 1b's use of "a process" as its unit; the promotion condition of `DDD-flow-01` to `-04` ("a second process"); under the third limb, the identification of north with a pull's determinable.

**Rests on.** 11-17 E-1, R-2, R-4, R-5, R-6, R-7 point 4; 11-18 R-2, R-5; `DDD-frame-13`; `DDD-address-01`; `DDD-ground-06`. That north is the determinable of a pull rests on **no ruling**: it is Claude's joining of 11-17 R-2 and 11-18 R-5, `UNVERIFIED — Emil review`.

## P-4 — `DDD-address-09`, the pull, new

**Weakest point.** The fourth gap, actual against observed, can never be inspected (`term:outcome`). So the most common deviation in software, the one nobody has seen, is a pull this claim names and its procedure cannot find.

**Statement.** A pull is a gap between two of the four states of a determinable (`DDD-address-11`), read inside a map's declared scope, where the determinable has two or more outcomes that cannot all hold together, and a pull is placed by a trace back from the request that stops where the answer lies outside the scope.

**Region, in brief.** Wherever a map's scope is declared. A pull is found at the edge first: what crosses into the scope and out of it (11-18 E-4, Claude's reading). Its entry act is the first act inside the scope that reads it. Under a different scope the same determinable may show a different gap and a different entry act (`pull-procedure.md`, W-1 and W-2).

**Falsifier.** A request inside a declared scope that its holders recognise as demand and that shows no gap between any two states of any determinable at or inside the edge; or two practitioners who, given the same scope and the same record, independently write statements for one pull that name different entry acts.

**Test.** Reproducibility, which is what Emil asked for at 11-18 E-3 ("so that it can be reproduced by practicitioners"): two practitioners run the five parts on one scope without conferring, and their statements are compared field by field.

**Breaks.** Step 1 starting from scope and north (P-8, S-2); `DDD-address-08`'s north as a pull's determinable; the pull procedure.

**Rests on.** 11-18 R-1, R-2, R-5; `DDD-frame-13` ("determination demand is thereby a measure over unresolved determinables"); `term:outcome`. The edge-first search rests on 11-18 E-4, which is not a ruling.

## P-5 — `DDD-address-10`, kinds of demand as ground positions, new

**Weakest point.** No map in the repository has declared the axis kinds are read on. The worked example declares two for exposition: realisation (not built, built) and whose determinable (the product's, the arrangement's). The second is needed only to place own-ground demand, and rests on no ruling.

**Statement.** A kind of demand is a position on a declared ground axis, so kinds differ by the ground a demand pulls from and not by where it came from, and two demand items at one position are of one kind whatever their source.

**Falsifier.** Two demand items at one ground position that must be ordered by different owners to be ordered on the ground they need; or one item whose kind changes with who reported it while its ground position is unchanged.

**Breaks.** Step 1b's part 6 as written, which classifies each source of pull; the "sources by kind" tables of `pdlc.md` §9 and step 1b, read as classification by source. Not `DDD-flow-01`: its three kinds are already tested relative to the decisions in force, which is a ground reading.

**Rests on.** 11-18 R-4; `DDD-ground-06` (positions on declared axes); consistent with `DDD-flow-01`. The second axis rests on **no ruling** (Q-4).

## P-6 — `DDD-address-11`, the four states, new

**Weakest point.** The mapping is built from four words (11-18, "The four states"). pjarnhus's own definitions are not known and may differ. "Expected" is not one state: each holder who bears the outcome has one.

**Statement.** A determinable is read in four states inside a scope — specified, the governing decisions in force over it; actual, the outcome, the determinate as it lands in the world; observed, the verdict, the same determinate as assessed by a declared predicate; and expected, the tolerance held by each holder who bears the outcome — and actual is never read directly.

**Credits** (the claim format's `credits` field, as `DDD-frame-13` uses it). The four state names, specified, actual, observed and expected, are GitHub user pjarnhus's, from unpublished work on four states of an implementation (11-18 R-6). The mapping of each to canon is ours, made from the names.

**Falsifier.** A demand item whose gap cannot be stated without a fifth state; or a determinable outside software for which one of the four cannot be given any meaning.

**Breaks.** `DDD-address-09`, which defines a pull over these states; the gap table; the index's state columns in `DDD-address-06`.

**Rests on.** 11-18 R-5 and R-6; upstream `term:outcome`, `term:verdict`, `term:tolerance`, `term:governing-decision` (settled). "Never read directly" rests on `term:outcome` ("the world renders outcomes, never verdicts") and on an open point of #80.

## P-7 — `DDD-dec-122`, amended

One decision, Emil principal, recording the rulings of both days and the G1 rulings of this session in his words. It files the six claims, and the card changes Emil rules at G1. Proposed relations:

| Relation | To | Why |
|---|---|---|
| Adds to | `DDD-dec-114` | Round 9's "the SDLC is a subprocess under the PDLC" keeps its ruled reading. In `DDD-address-08`'s terms the SDLC is a bound, and in `DDD-address-06`'s it may be declared a scope |
| Amends | `DDD-dec-118` | Its option text "Acts first, then how demand arrives" is amended if step 1 starts from scope and pull (S-2). Its "classify each source of pull" is amended by `DDD-address-10`. Its other rulings stand |
| Supersedes | Nothing by the `supersedes` field. Under P-2 option A, the wording of 11-17 R-7 point 3 | A decision's `supersedes` names a whole decision. Neither earlier decision is wholly replaced |

`basedOn`: the six claims; `DDD-ground-05`, `DDD-ground-06`, `DDD-ground-01`, `DDD-frame-13` upstream; `DDD-address-01`, `-02`, `-04`; `DDD-flow-01`, `-03`; `DDD-dec-114`, `-118`, `-38`.

Its notes say it was first drafted on 2026-11-17 on a branch that did not land and was amended on the rulings of 2026-11-18, and they supersede 11-17 R-7 point 7 ("no issue number on the commits"), as the 2026-11-18 record's first correction already says.

## P-8 — the two statements that are stated, not ruled

#80 lists them as stated and not ruled. They are proposed here and are not ground.

| # | Statement in #80 | Proposed reading | Falsifier | Rests on |
|---|---|---|---|---|
| S-1 | "The act map is the central modelling artefact for every application" | Central as an index every later artefact attaches to, not as a container that holds them. `steps-and-the-map.md` is the evidence: each of steps 2 to 10 attaches to a part of the map or to a record beside it | An artefact a later step produces that has no part of the map, and no record beside it, to attach to | 11-18 E-1, not ruled |
| S-2 | "Step 1 starts from north" | Step 1 starts from scope, then north. Scope comes first because 11-18 R-2 says "scope must be the first else we cant place the pull". North is found by the five-part procedure, before any act is mapped | A pull statement whose entry act cannot be found until acts are mapped | 11-18 E-2, not ruled; `DDD-ground-05` (declaring the determinable space precedes determination over it) |

**Where the procedure is filed (S-2).**

| | Option A (recommended) | Option B |
|---|---|---|
| Form | The five parts become the first part of step 1's card, by a superseding section, marked `[PROPOSED]` inside a card ruled for test | A card of its own before step 1, `[PROPOSED]`, numbered when N-1 is ruled |
| For it | It is what Emil stated at 11-18 E-2, and it keeps one step for one map | Step 1's ruled form is untouched, and its register is not mixed |
| Against it | One card carries two registers | Step 1b's numbering problem doubles |
| T2b | Its act map is produced by step 1 with the new first part. See `effects.md` | T2b runs step 1 unchanged. The pull procedure is tested separately |

## G1 questions

| # | Question |
|---|---|
| Q-1 | P-1: is `DDD-address-06` ruled as amended, with the index carrying the three readable states and the observed state as a pointer into the record? |
| Q-2 | P-2: option A or option B for `DDD-address-07`? Under A, the wording of 11-17 R-7 point 3 is superseded |
| Q-3 | P-3: is `DDD-address-08` ruled as amended, with north as the determinable of a pull? |
| Q-4 | P-5: does each map declare the axis its kinds are read on, or does the method give one? Is "whose determinable" ruled as the place of own-ground demand (`pull-procedure.md`, W-3)? |
| Q-5 | P-4, P-5, P-6: are `DDD-address-09` to `-11` ruled as written, each conceptual and projected? |
| Q-6 | Does 11-18 R-5 rule the gap table as well as the mapping of the four states? If not, is it ruled now, and is "specified against observed" ruled as the readable form of "specified against actual"? |
| Q-7 | May a file under `core/claims/` carry pjarnhus's credit, given that his agreement is not recorded (an open point of #80)? If not, `DDD-address-11` carries "the four state names are not ours" with no name, and the credit stays in the session record |
| Q-8 | P-8: S-1 and S-2 as read? For S-2, option A or option B? |
| Q-9 | `steps-and-the-map.md`: are the nine "Value made visible" rows ruled as proposed? |
| Q-10 | `effects.md`: is the effect on T2b, on step 1b's kinds and on `DDD-address-02`'s region ruled as stated, and which of the three options for `DDD-address-02`? |
| Q-11 | Filing: the six claims under `core/claims/`, `DDD-dec-122` under `core/decisions/`, the card changes in `method/`, and this session's row in `meta/sessions/README.md`. Anything else, or anything not? |

## Amendments after G1

Appended on Emil's G1 rulings of 10:30 (`rulings.md`). The sections above are left as written, and where they differ, this section governs. These are the texts that will be filed once the held conflicts K-1 to K-3 are answered.

### G1-A1 — P-2, `DDD-address-07`, on C-1 and G1-Q2

**Statement, ruled (option A).** A second act map exists when, and only when, a second declaration exists: a second scope, or a second declaration of ground axes. Scope says what is world. Axes say what is comparable.

**Falsifier, corrected by C-1.** Two limbs, one per kind of boundary.
- Between maps with different declarations of ground axes: a governing decision whose applicability predicate must cover occurrences in both, or two occurrences in the two maps whose behaviour must be compared to answer a question the work poses.
- Between maps of nested scopes on the same axes: shared acts that carry different addresses in the two maps.

The first limb no longer fires on a PDLC decision covering an SDLC act, which is the case C-1 names.

### G1-A2 — P-3, `DDD-address-08`, on C-2. **Held: K-1**

The text C-2 asks for, to be filed once K-1 is answered: "… fixed by one or more norths and optionally bounded by composite acts inside the map's scope, where a north is the determinable of a pull, whether or not a gap is open on it now." A process keeps its north between occurrences: the determinable is to the gap as the act site is to the occurrence. The falsifier's third limb, "a process its holders recognise whose work answers no gap between any two states", reads "no gap at any time", not "no gap now".

### G1-A3 — P-4 and P-6, on G1-Q6 and G1-W

`DDD-address-09`'s region says: a pull is a gap between two of the four states; the gap table is examples; "specified against observed" is the readable stand-in for "specified against actual"; "found" means any holder observing an outcome outside their tolerance, which is "expected against observed", found from the expected side. Its weakest point keeps the unreadable gap between actual and observed. Whether it adds "a bug never found has no impact" is held at K-3.

`DDD-address-11`'s credits name pjarnhus, without an @, and its notes record that Emil told him and he agreed (G1-Q7).

### G1-A4 — P-5, on G1-Q4

`DDD-address-10`'s region says: each map declares the axis its kinds are read on, and the method offers "built or not built" as the starting point. "Whose determinable" is named in its notes as `[PROPOSED]`, with own-ground demand as its only evidence.
