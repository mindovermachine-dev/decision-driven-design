# Proposals for G1 — the method is making an act map

Deliverable 2 of #88. Written 2026-11-20 on `main` at `1ecf914`, after the survey (`survey.md`). Nothing here is filed, and nothing under `core/`, `method/`, `applications/` or `README.md` has changed.

Everything below is Claude's, `UNVERIFIED — Emil review`, except where a ruling is quoted. The issue's "Read as" and "Not ruled" lists are Claude's, so nothing here builds on them as rulings: Part A puts them to Emil as questions.

The two rulings this rests on, from #88, verbatim:

> **2026-11-19, 13:54.** "The method now is all proposed and the method as i envision it now is to create an act map. And that process is 1. scope the act map 2. place an act or decision 3. follow the determinable back to the edge and note the pull. 4. do it again untill all maps you can find or think of is mapped and your pull sources are identified."
>
> **2026-11-19, 13:57.** "The method should be updated as well. and steps 2 to 10 is recorded in the acts and decisions. We need to help people then describe the act fully or else they cant find the pull"

## Part A. The readings, as questions

Each can be answered in a line. The recommended answer comes first.

| # | Question | Recommended | What it settles |
|---|---|---|---|
| Q-1 | **Register.** Is every part of the method `[PROPOSED]`, step 1 included, so that step 1 leaves "ruled for test"? | Yes. "The method now is all proposed" (13:54) reads this way | Moves step 1's register. That is a MINOR release under `DDD-dec-82`, and it supersedes in part `DDD-dec-122`'s "step 1 stays ruled for test" (survey F-4). The claims stay projected; T2b still tests them (P-7) |
| Q-2 | **Order.** Scope stays first (2026-11-18 R-2, filed in `DDD-dec-122`). After it, the practitioner places an act or decision they can see, and the pull is found by tracing back from it. Does this supersede the order of parts 2 to 5 of step 1's first part (edge determinables, states and gaps before any act)? | Yes, parts 2 to 5 only. Part 1, scope, stands | What is superseded. **Note (survey F-1):** the issue says this supersedes "the ruling of 2026-11-18 that mapping starts with north". The record holds "start with North" as E-2, "Direction given … Not ruled". So no ruling about north is superseded. R-2 (scope first) is the filed ruling, and it stands |
| Q-3 | **Steps 2 to 10.** They stop being steps. Each becomes something recorded on an act or a decision, **or in a record keyed by act site** (the occupancy, derivation and occurrence records beside the map). Is "recorded in the acts and decisions" meant to include those records? | Yes. Four of the nine (6, 7, 8, 9) already attach beside the map, and 10 partly, under `DDD-dec-122` (Q-9) | Whether the act description (P-2) holds all of steps 2 to 10, or only six of them |
| Q-4 | **Move 4.** "do it again untill all maps you can find or think of is mapped". Did you mean maps, acts, or both? | Both: every act and decision inside the scope, then each further scope (P-6) | What move 4 repeats. Asked in the planning project and not answered |
| Q-5 | **#82's core process.** On 2026-11-18 at 13:22 you accepted a core process of six moves, in #82's text and not filed: declare the scope, find the pulls, map the acts, read the states, name the gaps, treat each gap as a pull. Its order finds pulls before acts. Do the four moves of 2026-11-19 supersede that order? | Yes, for the order of making a map. #82's moves 4 to 6 (read the states, name the gaps, treat each gap as a pull) stay #82's, as the verification of a map, not as part of making it (P-5) | What #82 starts from. It waits on this answer |
| Q-6 | **"Describe the act fully."** Does "fully" mean every field of P-2's two groups, or the fewest that let the trace run, with the rest filled as the work proceeds? | The fewest first (group A), the rest when known (group B). A field left empty is itself visible | Whether move 2 can finish before steps 2 to 10's content is known |

## Part B. The proposals

Each names its weakest point first, then the proposal, what it rests on, its falsifier and what it breaks.

### P-1. The four moves, as one card

**Weakest point.** The step card's nine fields come from the method draft, which is `[PROPOSED]`, not from a ruling. Filling nine fields for "do it again" invents content the ruling did not give. And one card for four moves leaves `DDD-dec-82`'s unit, "a step card added or a step's register moves", with one card where it counted ten.

**Proposal.** One card, `method/make-an-act-map.md`, `[PROPOSED]`. The four moves are its sections. Each move has the nine fields, "Value made visible" first. One card, because the ruling gives one thing ("create an act map") with four moves, and four cards would read as four steps again.

| Field | Move 1. Scope the act map | Move 2. Place an act or decision | Move 3. Follow the determinable back to the edge and note the pull | Move 4. Do it again |
|---|---|---|---|---|
| **Value made visible** | What is yours to decide, and what is world. Where every trace will stop | One act or decision, described fully enough to find its pull. A field you cannot fill shows now, not in production | Why the act happens at all: its pull, the entry act, and which part of the chain is yours | Your pull sources: every pull at the edge, the acts each one enters, and where your edge is a dependency in a wider map |
| Step | Move 1 of 4 | Move 2 of 4 | Move 3 of 4 | Move 4 of 4 |
| Decision discharged | The scope: the decisions the map's holders take without asking anyone. The ground axes, and the axis kinds are read on. Commitment level not filed | That this act is inside the scope, and its address | For each ground reading: inside, edge or unknown. Where the trace stops | Whether to place another act, widen to another scope, or stop |
| Ground in | The people doing the work and the decisions they take | Move 1's scope and axes. An act or decision the practitioner can see: a request, an issue, a command, a review | The placed act's description (P-2, group A) | The map so far and its findings |
| Act | List the decisions. Mark each inside or outside, once. Declare the axes, starting from "built or not built" for kinds. By the holders, with whoever rules the decomposition | Fill the act description, group A at least (P-2) | The trace procedure (P-3) | Moves 2 and 3 for every act the trace placed and every act or decision seen in the scope. Then the edge pass (P-4). Then a further scope (P-6) |
| Artefact out | The scope list and the declared axes, as graph data | An act site at its address, with its description. Or a decision anchored at an act site through its applicability predicate | Dependencies between act sites. A pull statement for each reading that reaches the edge. Rows in the index of determinables. Findings for unknown sources | The act map of `DDD-address-06`, with its index. One map per scope and declaration of axes (`DDD-address-07`) |
| Cost and relocation | Deciding the scope makes everything outside it ground that crosses the edge. Seams appear only where scopes are declared (2026-11-18 R-3) | Describing costs effort now. Demand moves from discovery in production to the description | A reading with no known source becomes a finding, not a guess | Grows with each act and scope. A nested scope's pull shows in the wider map as a dependency |
| Exit check | Every decision named is marked inside or outside, once. Mechanical on the list; whether the list is complete is a judgement | Group A filled, each field passing its check. The occupant is not in the address | Every reading of the act ends at a placed act inside, at the edge with a pull statement, or at a finding | P-5 |
| Principal | Whoever rules the decomposition. The method names no role for it (`DDD-ground-06` region) | The same | The same | The same |

**Rests on.** The moves and their order: the ruling of 13:54. One card: none. The fields: the method draft, `[PROPOSED]`. "Value made visible" first: none (the issue's instruction; the draft's purpose line puts value first). Move 1's content: 2026-11-18 R-2, `DDD-address-06`, `-07`, `-10`. Move 3's stop: R-2 and `DDD-address-09`'s statement.

**Falsifier.** A practitioner performs a move and cannot name the value it gave them (the draft's default). Or a junior engineer with the card alone cannot say which move they are in.

**What it breaks.** The README's step table and its "ten steps" (survey, `method/README.md:3`, `README.md:27-44`). `DDD-dec-82`'s unit (survey F-3). The roadmap of one card per step (`GOVERNANCE.md:181`). The field-report template's "step N". #74's plugin. All for deliverable 4, not changed here.

### P-2. The act description

**Weakest point.** Group A's third field, where each reading comes from, presupposes the practitioner can see the source. Often the source is a person's judgement, with no act on any map. Then the field reads "unknown", and the trace stops at a finding rather than a pull. Second: steps 3 and 7 describe decisions and allocations, and steps 8 to 10 describe records beside the map, so "on the act" is true only if Q-3 is answered yes.

**Proposal.** Two groups. Group A is the fewest fields that let the trace run. Group B is what steps 2 to 10 held. A decision is described by the rows marked "decision".

**Group A — for the trace**

| # | Field | Of | Value when filled | Check | Rests on |
|---|---|---|---|---|---|
| A-1 | Inside the scope: which of the scope's decisions this act takes | Act | You know the act is yours, so a trace through it continues | It names a decision on move 1's list | 2026-11-18 R-2; `DDD-address-06` (scope) |
| A-2 | The determinable it resolves, with two or more outcomes that cannot all hold together | Act, decision | What the act settles, and so what could pull it | Two or more outcomes; no two hold together (a judgement) | `DDD-frame-13` (pinned, projected); 2026-11-18 R-1; `DDD-address-09` |
| A-3 | Each ground reading, and where it comes from: an act inside (name it) or what crosses the edge (name it), or "unknown" | Act | The trace's next hop for every reading | Every reading has one of the three | `DDD-address-01` (B depends on A iff a state change A produced is in B's ground reading); `DDD-ground-02` (pinned, projected): undeclared source coverage is a finding, and "Unknown is never a pass" |
| A-4 | Its address: position on the declared axes and its layer path, with the occupant left out | Act | The act has one place on the map, so it is placed once | One address per act site; no occupant in it | `DDD-ground-06` (pinned, projected) |

A-1 is not in the issue's list. The trace cannot decide "inside or outside" without it, and it is the scope's to say, not the act's.

**Group B — what steps 2 to 10 held**

| # | Field | From step | Of | Value when filled | Rests on |
|---|---|---|---|---|---|
| B-1 | The authority at this act's layer | 2 | Act (its layer) | An act whose layer has no authority shows as unowned | Draft line 2, `[PROPOSED]`; `DDD-dec-122` Q-9 row, `[PROPOSED]` |
| B-2 | The decisions anchored here, each with its applicability predicate. A determinable governance took up | 3 | Act, decision | The backlog is visible. A decision with no act site is a candidate escape | `DDD-ground-01` (pinned, projected); `DDD-address-06` (index); draft line 3 |
| B-3 | For each ground reading: provenance (controlled, observed, inferred, institutional, missing) and tick rate. For the determinable: its rate of change | 4 | Act | Missing ground found before build | Draft line 4, `[PROPOSED]`; `DDD-address-06` (rate of change); `DDD-ground-02` |
| B-4 | The acceptance predicate; which closure senses hold for the arrangement allocated; the assurance set from stakes | 5 | Act | Where a verdict can be a mechanical check and where it needs a person | Upstream `term:closure` (pinned, settled); `DDD-dec-122` K-2. Open: closure is classified before the arrangement is allocated (K-2) |
| B-5 | The occupant: actor or arrangement, source, commitment level, assurance mechanism. Beside the address, never in it | 6 | Act (occupancy record) | Where demand sits and who carries it | `DDD-ground-06`; draft line 6 |
| B-6 | Attribution, principal, authority, stake, remediation | 7 | Decision, allocation | An auditable answer to the compliance question | Upstream `term:accountability` and its parts (pinned, settled); `DDD-frame-08` (pinned); `DDD-flow-04` for the PDLC |
| B-7 | The components it pulls | 8 | Act (derivation record) | From an act, its components; from a component, every act that pulls it | `DDD-address-02`, `-03` |
| B-8 | Its occurrences, each with its time index | 9 | Act site (occurrence record) | Evidence, not assertion | `DDD-address-01`; `DDD-address-06` (occurrences beside the map) |
| B-9 | The observed state: a pointer to the latest observation. Behaviour at the two grains | 10 | Determinable, act site | Escape seen as it happens; the pulls a supersession opens | `DDD-address-11`, `-05`, `-06` |

**A decision**, described: A-2 (the determinable it takes up, its outcomes as alternatives), B-2 (its predicate and the act sites it governs), B-6 (its principal), and its commitment level. Rests on `DDD-ground-01` and the decision ontology in `meta/way-of-working.md` §4.

**Rests on.** The two-group split and the choice of group A: the ruling of 13:57 ("describe the act fully or else they cant find the pull") and none beyond it. Each field: the row's own column.

**Falsifier.** An act with group A filled whose pull the trace cannot find. Or a pull found only by using a group B field: then group A is not enough.

**What it breaks.** The step cards as the unit of the method. The occupancy, derivation and occurrence records stay where `DDD-dec-122` put them, beside the map.

### P-3. The trace back, for a junior engineer

**Weakest point.** The scope is a list of decisions, and the trace walks acts. An act held by different owners on different occurrences sits inside for some and outside for others. In the lifecycle data, "frame the issue" (o1) is held by "the locus's owner", so in the SDLC scope it is inside when the locus is How and outside when it is What. The procedure has to say what to do then.

**Proposal.** Written for someone at first contact.

1. Take the act you placed. Write down everything it reads before it can decide (group A, A-3).
2. For each thing it reads, ask: **who made this the way it is?**
   - **Someone inside the scope, by an act.** Write: "this act depends on that act, because it reads …". If that act is not on the map yet, place it next (move 2).
   - **Someone or something outside the scope**: another team's decision, a customer, a regulator, time passing. **This is the edge.** Write a pull statement for it (the form on step 1's card stands). Stop following this reading.
   - **You do not know.** Write it down as a finding: "reads … from an unknown source". Do not guess. Ask the people who do the work.
3. If the act is held inside for some occurrences and outside for others, write it twice: once as inside, once as at the edge, and record the split as a finding for move 1.
4. If the act you would place next is already on the map, write the dependency and do not place it again. Dependencies between act sites may loop.
5. The act is traced when every reading ends in one of the three. Go on to the next act you placed.

**A sketch, read from the lifecycle data, not run.** Scope: the SDLC. Start at "plan the realisation on the issue" (o1b), `applications/sdlc/acts/acts.ttl`. It reads three things:

| Reading, from the data | Who made it so | Result |
|---|---|---|
| "the framed issue, its locus declared" (o1) | The locus's owner. Inside when the locus is How, outside when it is What | Step 3: written twice; a finding for move 1 |
| "the What owner's verdict: owed" (oC) | The What owner, outside the SDLC | The edge. A pull statement: owed demand |
| "the How owner's own-ground issue" (oG) | The How owner, inside | Place oG next |

At oG, "frame own-ground work on an issue", the data declares no reading except an earlier deployment (`lc:readsEarlier m:o13`). Nothing says what the How owner read to decide there was own-ground work. The trace stops at a finding: the act is not described fully enough to find its pull. That is the ruling of 13:57, met on the repository's own data.

**Rests on.** 2026-11-18 R-2 (the stop). `DDD-address-01` (the dependency). `DDD-address-06` (loops over sites). `DDD-address-09`'s statement. `DDD-ground-02` ("Unknown is never a pass"). The instruction to test against a junior engineer's first contact: the method draft, `[PROPOSED]`. The sketch: Claude's reading of the data, `UNVERIFIED`.

**Falsifier.** `DDD-address-09`'s own: two practitioners on one scope and record name different entry acts. And: a junior engineer cannot sort a reading into the three cases.

**What it breaks.** The five-part order on step 1's card (parts 2 to 5). `DDD-address-09`'s test, which names "the five-part procedure of step 1" (P-9).

### P-4. The edge pass

**Weakest point.** It brings back, inside move 4, the edge-first order the ruling of 13:54 replaced. It rests on no ruling.

**Proposal.** Add it to move 4, not as a fifth move. Once the trace has run, list each state that crosses the edge, in or out. For each, ask: **who outside the scope is waiting on it, and what do they expect?** An expected state that no act inside reads is "expected, with nothing specified": demand that nothing answers. Write a pull statement for it, with "none" as its entry act.

| Option | What it is | For | Against |
|---|---|---|---|
| **A (recommended)** | The edge pass, inside move 4 | Finds demand no act answers, which a trace from acts cannot reach. Keeps four moves | It is Claude's. It brings edge-first back by another door |
| B | No edge pass. Unanswered demand is found when someone files a request, which is an act | Nothing added | A need nobody has taken up stays unseen until someone acts on it |
| C | A fifth move | Clear | Changes the ruled four moves |

**Rests on.** None ruled. Supported by `DDD-address-11` (expected, per holder), by 2026-11-18 E-4 (a statement, not a ruling), and by `DDD-address-09`'s region line, which is Claude's unverified reading of E-4 (survey F-2).

**Falsifier.** In a worked example, the edge pass finds no pull the trace did not. Or the holders outside the scope cannot be listed.

**What it breaks.** Nothing filed. Under option C, the ruled four.

### P-5. When the loop ends

**Weakest point.** "Until all maps you can find or think of is mapped" has no bound. Any stop is a principal's judgement. A mechanical check can show that the trace closed. It cannot show the map is complete: an address is blind to axes nobody declared (`DDD-ground-06`).

**Proposal.** For one map, move 4 ends when:

1. every placed act has every reading ended at an act inside, the edge, or a finding (P-3);
2. the edge pass has asked every crossing state (P-4, if ruled);
3. the principal accepts the findings as they stand, or opens a further scope.

**#82's gaps are not move 4's exit check.** They are the check of a map once the work runs. At design time there is no record, so only "specified against expected" can be read, as #82's own text says. Recommended: the exit above for making the map, and #82's grid as the verification of the map, filed by #82.

**Rests on.** None ruled. #82's grid is accepted (2026-11-18, 13:22) but not filed.

**Falsifier.** A map that passes the exit, and whose holders, shown it, name an act or a pull it misses.

**What it breaks.** #82's deliverable 2, which places its process "as step 1's exit check, and as the content of steps 9 and 10". Neither exists as a step after Q-1 and Q-3.

### P-6. What move 4 means

**Weakest point.** Emil's word is "maps". The reading adds acts. It is unanswered (Q-4).

**Proposal.** Three nested loops:

1. **Inside one map:** every act the trace placed gets moves 2 and 3. That is already in P-3, step 2.
2. **Inside one map, acts no trace reached:** every act or decision seen in the scope that no trace reached is placed and traced. If its trace finds a pull, that is a further pull source. If it reads nothing and nothing reads it, it is a finding: a dead act, or a map missing a dependency.
3. **Further scopes:** a pull at this map's edge, followed past the edge, is a dependency in a wider map (2026-11-18 R-3; `DDD-address-07`). Each scope the practitioner can map is a further map, with moves 1 to 4.

**Rests on.** The ruling of 13:54 ("do it again"). R-3. `DDD-address-07`. Loop 2's finding: none.

**Falsifier.** A nested scope's pull that cannot be shown as a dependency in the wider map (a limb of `DDD-address-07`'s falsifier).

**What it breaks.** Nothing filed.

### P-7. What T2b tests

**Weakest point.** T2b was the test that would move step 1 to reported (`DDD-dec-74`: it "stands or falls on T2b"). Once step 1 is `[PROPOSED]`, no part of the method's register waits on T2b. Reading the pre-registration's "its act map is itself produced by method step 1" as "produced by making an act map" can look like rewriting by reading.

**Proposal.** The pre-registration (`prereg-act-coordinates.md`, revision 3) is fixed and is not edited. Its predictions (§5) and falsifiers (§6) are about the address, the layer path, the time index and reuse: `DDD-ground-06`, `DDD-address-01` to `-05`. None is about the step's register. So:

| | What T2b does |
|---|---|
| Tests, unchanged | Every prediction in §5 and every falsifier in §6, on a map made by the four moves |
| Moves | The claims, from projected to reported if they survive. Not the method's register: a move becomes ruled only by a ruling |
| Reads under supersession | "its act map is itself produced by method step 1" (§4): produced by making an act map, at the card's commit (T-6 already asks for the commit). As `effects.md` of 2026-11-18 read R-6's "tree of occurrences" |
| Registered again, for the unsealed `prereg-t2b.md` | T-2 superseded: P-3's trace is run from each placed act and every reading is recorded as inside, edge or unknown. New T-7: group A is filled for every act, and any pull that needed a group B field is recorded. New T-8: the edge pass, if P-4 is ruled. T-1, T-3 to T-6 stand |

**Rests on.** The fixed pre-registration. `DDD-dec-122` (Q-10, the T-items). The precedent of 2026-11-18's `effects.md`.

**Falsifier.** A prediction in §5 that cannot be evaluated on a map made by the four moves. The likeliest: the layer prediction, if the moves place acts without composite acts.

**What it breaks.** `DDD-dec-74`'s "stands or falls on T2b", as the state at its ruling. The README's "waits on T2b" (survey). `DDD-address-09`'s test (P-9).

### P-8. Where `method/01`, `01b` and `02` to `10` go

**Weakest point.** Twelve card files stay in `method/`, and one is live. Their "Next" links still chain step to step. A reader who lands on `02` from a link may take it as a live step.

**Proposal.** No file is deleted, moved or reworded. Moving them would break every link to them, in `README.md`, `applications/pdlc/pdlc.md` and the session records.

| File | What happens | Where its content goes |
|---|---|---|
| `method/make-an-act-map.md` | New. The live card (P-1) with the act description (P-2) and the trace (P-3) | — |
| `method/README.md` | A superseding section at the top: the method is making an act map, four moves, each `[PROPOSED]`. The old table stays below it, headed "As it stood at v0.7.0" | — |
| `01-map-and-index-acts.md` | A superseding section at the top, naming the new card | Scope, part 1: move 1. Parts 2 to 5: moves 2 and 3. The pull statement and gaps table: kept and cited by move 3. Address and time index: A-4 and B-8 |
| `01b-map-the-flow-of-demand.md` | A superseding section | Owners per decision and seams: B-1, B-6, and the scope of move 1 (an owner is a scope, `DDD-dec-117`). Tracing an item end to end: moves 3 and 4. Kinds: the declared kind axis, move 1, and the index. Sighting against entry: the pull statement. `DDD-flow-01` to `-04` stand |
| `02` to `10` | A superseding section on each: no longer a step; its line is field B-1 to B-9 | B-1 to B-9 |
| `quick-start.md` | Unchanged here. A draft issue at deliverable 4 | — |

**Rests on.** Supersession, never rewriting (`AGENTS.md`; the method draft). The ruling of 13:57. `DDD-dec-118` placed 1b as "a step of the method" (survey): that ruling is superseded in part by P-9's decision.

**Falsifier.** A reader of `method/README.md` alone cannot name the four moves and the register of each (the issue's exit for deliverable 3).

**What it breaks.** `applications/pdlc/pdlc.md`'s "method step 7" and "step 10" (survey), the PDLC graph data's "method step 1b, part 5/6", `DDD-flow-04`'s breaks field, and the plugin. All for deliverable 4.

### P-9. The decision that files this

**Weakest point.** One decision carries a register move, a supersession in part of two decisions and a new card. Splitting it would leave one of them unfiled for a time. And `DDD-dec-124` has one stray mention (survey; `bootstrap.md`).

**Proposal.** One decision, **`DDD-dec-124`**, principal Emil:

- The method is making an act map, in four moves, each `[PROPOSED]` (13:54).
- Step 1 leaves "ruled for test" (Q-1). This supersedes in part `DDD-dec-122` ("step 1 stays ruled for test" and the order of parts 2 to 5).
- Steps 2 to 10 are recorded as the act description's group B (13:57; Q-3).
- `DDD-dec-118`'s "a step of the method, placed after step 1" is superseded in part: 1b's content goes as P-8 says. Its other rulings stand.
- `supersedes:` none, because no earlier decision is wholly replaced, as `DDD-dec-122` did. `basedOn:` `DDD-dec-122`, `-118`, `-74`, `-82`, `DDD-address-01`, `-06`, `-07`, `-09`, `-11`, `DDD-ground-01`, `-02`, `-05`, `-06`, `DDD-frame-13`.
- A `notes` entry appended to `DDD-address-09`, as `DDD-address-02` got one under `DDD-dec-122`: its region's "found at the edge first" (Claude's unverified reading of E-4) and its test's "five-part procedure of step 1" are read under `DDD-dec-124`. No statement, region or test is reworded.

No new claim is proposed. "Group A is enough to find the pull" could be a claim, but it rests on no evidence. It stays `[PROPOSED]` on the card until a case tests it.

**Ids.** Checked 2026-11-20 on 67 branches downstream and 27 branches and 18 tags upstream. `DDD-dec-124`: no file anywhere; one mention, on `main`, as the alternative not taken in `meta/sessions/2026-11-18-canon-lock-file/findings.md:313`. `DDD-dec-125` onwards: no file and no mention. `DDD-dec-121` is #74's and is not used. If you prefer an id with no mention: `DDD-dec-125`.

**Falsifier.** After filing, a ruled or front-door line still states step 1 "ruled for test" as current (the survey's F-4 list), or `validate` refuses the decision.

**What it breaks.** `DDD-dec-82`'s "all ten steps" (survey F-3), which is deliverable 4, not changed here.

## Part C. Conflicts found

| # | Conflict | Where | Held for |
|---|---|---|---|
| K-1 | The four moves start from an act. #82's six-move core process, accepted 2026-11-18 at 13:22 and not filed, finds pulls before acts | #82's text; the ruling of 13:54 | Q-5 |
| K-2 | `DDD-dec-118` ruled 1b "a step of the method, placed after step 1". Under the four moves there are no steps | `DDD-dec-118` statement | Q-1, Q-3, P-9 |
| K-3 | `DDD-address-09`'s region says a pull is found at the edge first, and its test names the five-part procedure. Its own notes flag the region line as unverified | `DDD-address-09.yaml:8, 31, 53` | P-9 |
| K-4 | `DDD-dec-82`'s statement counts ten steps for 1.0 | `DDD-dec-82` statement | Deliverable 4 |
| K-5 | "Start with north" is cited by the issue as a ruling of 2026-11-18. The record holds it as a direction, not ruled | `2026-11-18-pull-and-scope/rulings.md`, E-2 | Q-2 |

## Part D. What #81 and #82 need from the rulings

| Issue | Needs | Why |
|---|---|---|
| #81, the What and product-cli | **Q-2** and **Q-5**: whether the order is the four moves (scope, act, trace, pull) or its own outcome line (scope, demand, acts) | Its outcome line and product-cli's phase order (W9) follow whichever order is ruled. #81 says it follows #88's G1 |
| | **P-2**, group A | The What's kinds map onto it: a field is the determinable (A-2), a View is a ground reading (A-3), a trigger is the edge. #81's pull kind (`about`, `arisesFrom`, `heldBy`) is A-2 and A-3 seen from the edge |
| | **P-3** and **P-4** | #81's finding 2 (the What checks the chain backwards) is P-3's trace. Its findings 7a, 8 and 9 (a pull with no ground; an axis position with nothing on it; a scope with no entry) are what an edge pass finds |
| | **Q-1** | #81 cites the method. Everything it cites is then `[PROPOSED]` |
| #82, the states and gaps | **Q-5** | Whether its six-move core process stands, or is superseded in order by the four moves |
| | **P-5** | Whether its gaps are move 4's exit check (recommended: no, they verify a running map) |
| | **Q-3** and **P-8** | #82 places its process as "step 1's exit check" and "the content of steps 9 and 10". Neither is a step after these rulings. Its X-1 and X-2 stand as they are |

## Part E. Draft issues

Deliverable 4's list is for G2. One side finding is drafted now, because it is not #88's.

**Draft: "README.md names v0.5.0 as the current preview".** `README.md:8` reads "**v0.5.0 is a preview: ready to try, not ready to use (`DDD-dec-74`)**". The tags `v0.6.0` and `v0.7.0` exist. Outcome: the front door names the current release, or no release. Ground: `README.md`, `releases/`, `DDD-dec-74`. Out of scope: the registers. A PATCH under `DDD-dec-82`.
