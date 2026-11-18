# The pull statement and the five-step procedure

A pull is a gap between two of four states of a determinable, read inside a declared scope. The four states are specified, actual, observed and expected. **The four states are credited to GitHub user pjarnhus** (2026-11-18 R-6). Only their four names are his. The mapping to canon, and everything below, is ours.

The procedure finds the pulls of a scope before any act inside it is mapped. It has five parts, in this order: scope, the determinables at the edge, the three readable states, the gaps, and the trace to an entry act. Its output is one pull statement per pull. Step 1 then maps acts from the entry acts the statements name.

**Register: `[PROPOSED]`.** Nothing here is filed. Each part names the ruling it rests on. Where a part rests on no ruling, it says so.

**Weakest point.** "Actual" is never read directly (`term:outcome`: "the world renders outcomes, never verdicts"). So the gap between specified and actual, which is the bug, is only ever read through observed. A practitioner who has not observed a deviation cannot find it with this procedure. The procedure finds pulls someone has seen or expects. It cannot find the ones nobody has seen.

## The five parts

| # | Part | The question, in plain words | Rests on |
|---|---|---|---|
| 1 | **Scope** | Whose decisions are we mapping? Everything else is the world | 2026-11-18 R-2: scope is the first declaration of a map. Everything outside it is world, including other people's decisions |
| 2 | **The determinables at the edge** | What comes into the work and what goes out? For each, what could turn out more than one way? | 2026-11-18 R-1: two or more outcomes that cannot all hold together. Looking at the edge first is E-4 ("they also inspect a system and look at the input and output"), read by Claude, `UNVERIFIED — Emil review` |
| 3 | **The three readable states** | What was decided? What has someone seen? What does each person who bears it expect? | 2026-11-18 R-5, the mapping to canon. That "actual" is not readable is an open point of #80 |
| 4 | **The gaps** | Which two states disagree? | 2026-11-18 R-5: a pull is a gap between two of the four states. The table of gaps is Claude's (see below) |
| 5 | **The trace to an entry act** | Follow the gap back. Stop where someone outside the scope would have to answer. Which act inside the scope takes it in? | 2026-11-18 R-2: the trace back from a request stops where the answer lies outside the scope |

## The pull statement

One statement per pull. Every field has a check that passes or fails. "Mechanical" means a reader can check it against the statement alone. "Judgement" means the check needs someone who knows the work.

| # | Field | What it holds | Check: it passes when | Kind of check | Part |
|---|---|---|---|---|---|
| F-1 | Scope | The name of the scope, and the decisions inside it: those the map's holders take | Every decision the statement names is marked inside or outside, and none is marked both | Mechanical | 1 |
| F-2 | Edge crossing | What crosses the edge, in or out, with the side that produces it and the side that reads it | Exactly one side is inside the scope | Mechanical | 1, 2 |
| F-3 | Determinable | The dimension that can turn out more than one way, named in words | It is about something that crosses the edge in F-2 | Mechanical | 2 |
| F-4 | Outcomes | Two or more outcomes of F-3 | There are at least two, and no two can hold together at the grain the statement names | Judgement | 2 |
| F-5 | Specified | The governing decision in force that covers F-3, cited, with its holder marked inside or outside; or "none" | A citation that resolves to a decision, or the word "none" | Mechanical | 3 |
| F-6 | Observed | What someone inside the scope has seen, by whom and in which record; or "not observed" | The observer is inside the scope. A sighting made outside is written as an edge crossing in F-2, not here | Mechanical | 3 |
| F-7 | Expected | One row per holder: who bears the outcome, and the outcome they expect | Each row names its holder. Two holders who disagree are both kept | Mechanical | 3 |
| F-8 | Actual | Always "not read" | The field says "not read". Anything else fails: a reading is F-6 | Mechanical | 3 |
| F-9 | Gap | The two states that disagree, as a row of the gap table | Both states are filled, or the row allows "none". A gap with actual in it is marked "suspected" | Mechanical | 4 |
| F-10 | Kind | The position on a declared ground axis that the pull pulls from, naming the axis | The axis is named and the position is one of its values. Where the item came from is not used | Mechanical once the axis is declared. Declaring the axis is judgement | 4 |
| F-11 | Rate of change | How often time makes F-3 unresolved again, with a unit, or "no unit known" | It is stated, with a unit or the words "no unit known" | Mechanical | 4 |
| F-12 | Trace and stop | The chain followed back from the gap, and the point where it stops because the answer lies outside the scope | Every link but the last is inside the scope. The last is outside and is named as world, or the chain ends inside at the cause | Judgement | 5 |
| F-13 | Entry act | The first act inside the scope that reads the pull | It is inside the scope, and the trace in F-12 reaches it | Mechanical | 5 |

F-11 is the rate of change of 2026-11-17 R-6, carried here because the index holds it. Whether a determinable is taken up by governance is read from F-5: a decision in force means taken up.

## The gap table

`[PROPOSED]`. Claude's table from the 2026-11-18 record, carried unchanged. R-5 rules the mapping of the four states. Whether it also rules this table is a question for G1 (Q-6 in `proposals.md`).

| Gap | What it is | Readable? |
|---|---|---|
| Expected, with nothing specified | A need nobody has taken up: a feature | Yes |
| Specified, with nothing actual | An approved change not yet built | Only as specified with nothing observed |
| Specified against actual | A deviation: a bug, which needs an implementation to exist | Only as specified against observed |
| Actual against observed | A deviation nobody has seen, or an alarm with nothing behind it | No. It can be suspected, never inspected |
| Expected against specified | The specification is wrong | Yes |

Two pairs are not in the table: observed against expected, and specified against observed read as itself. The worked example uses the second as the readable form of "specified against actual". That reading is Claude's, `UNVERIFIED — Emil review`.

## Worked example: the acme shop, with the How as the scope

The acme shop is the invented, illustrative record of [`applications/pdlc/`](../../../applications/pdlc/). The scope is the one Emil gave as his example in 2026-11-18 R-2: the How, "which is essentially the SDLC". The example is carried through all five parts. One item, issue #103, is followed in full. Two more, #101 and #104, are carried beside it, because kinds can only be told apart by comparison.

### Part 1 — scope

| Field | Value |
|---|---|
| F-1 Scope | **The How.** Inside: the decisions the How owner holds, about how the shop's software is planned, built, accepted, landed and run (pdlc.md §2, §13) |
| Outside, as world | The When owner's decisions: what is released for work, in which order, and when a toggle goes on. The What owner's decisions: what the software must do, its acceptance, and whether a defect is a bug. Customers' decisions |

| F-2 Edge crossing | Produced by | Read by | Source |
|---|---|---|---|
| In: a released issue (new demand) | When owner, outside | How owner, inside | pdlc.md §13 |
| In: an owed issue, with the classification verdict | What owner, outside | How owner, inside | pdlc.md §13 |
| In: the What and its product assurance | What owner, outside | How owner, inside | pdlc.md §13 |
| Out: production state, dark | How owner, inside | What owner, outside | pdlc.md §13 |
| Out: telemetry of the product in use | How owner's instrumentation, inside | What owner, outside. The How owner reads it too | pdlc.md §13; `DDD-flow-03` (sighting) |
| Out: the record, with the DORA keys | How owner, inside | When owner, outside | pdlc.md §13 |

Check F-1 passes: every decision named is marked once. Check F-2 passes: each row has one side inside.

### Part 2 — the determinables at the edge

| Item | F-3 Determinable | Crosses at | F-4 Outcomes | Check F-4 |
|---|---|---|---|---|
| #103 | Whether reorder respects the stock invariant | In: the What (the invariant); out: telemetry (the basket) | (a) reorder never adds an out-of-stock line; (b) reorder adds an out-of-stock line | Passes. (a) and (b) cannot both hold for one basket |
| #101 | Whether a returning customer can reorder in one step | In: a released issue | (a) in one step; (b) only by building the basket again | Passes |
| #104 | Whether a deploy needs a manual cache purge | Out: the record (each deploy) | (a) no manual step; (b) a manual purge on every deploy | Passes |

A rejected candidate shows the check failing. "The shop's quality" names no outcomes that exclude each other, so it is not a determinable and gets no statement.

### Part 3 — the three readable states

| Item | F-5 Specified | F-6 Observed | F-7 Expected | F-8 Actual |
|---|---|---|---|---|
| #103 | The Place order Decider's stock invariant (example-pool.ttl, the report on #103). Holder: What owner, **outside** | The out-of-stock line in a basket, on the How owner's telemetry (demand-flow.ttl, `t103`) | Customers: (a). What owner: (a) | Not read |
| #101 | The What decision framed at o1 for the issue. Holder: What owner, **outside** | Not observed: nothing built yet | Customers, through the When owner's market need: (a) | Not read |
| #104 | None found in the record | A manual purge on every deploy, in the How owner's own record | How owner: (a) | Not read |

Checks pass for all three rows. #104's "none" is a finding about the record, not a failure: nobody decided that deploys need a purge. It is how the arrangement came to be.

### Part 4 — the gaps

The kind is read on one declared axis, which the worked example declares here. It is Claude's, for exposition, built from Emil's ruling that "ground for a feature is by necessity that it hasnt been implemented and a bug must have been implemented" (R-4). `UNVERIFIED — Emil review`.

| Axis | Values | Why it is an axis |
|---|---|---|
| Realisation of the determinable in the scope | not built · built | R-4: a feature and a bug cannot share ground, because one has not been implemented and the other has |
| Whose determinable | the product's · the arrangement's | Without it #104 has no place (see the finding below) |

| Item | F-9 Gap | Readable as | F-10 Kind: position | F-11 Rate of change |
|---|---|---|---|---|
| #103 | Specified against actual: a bug | Specified against observed | product · built | Per reorder of a basket holding an item since sold out. Unit: reorders |
| #101 | Specified, with nothing actual: an approved change not yet built | Specified, with nothing observed | product · not built | Set by the market. No unit known |
| #104 | Expected, with nothing specified | As itself | arrangement · built | Per deploy. Unit: deploys |

Read in the lifecycle's words, #103 is owed, #101 is new and #104 is own-ground. The positions tell them apart without asking who reported them. That is R-4.

### Part 5 — the trace to an entry act

| Item | F-12 Trace back from the request, and where it stops | F-13 Entry act |
|---|---|---|
| #103 | The request to fix reorder ← the owed verdict: is the out-of-stock line a bug, or is the What wrong? That answer is the What owner's. **Stop: outside the scope.** The verdict arrives across the edge as ground | Plan the realisation (o1b in the acme map), which reads the owed verdict |
| #101 | The released issue ← the When owner's order and the What owner's framing. **Stop: outside** | Plan the realisation (o1b), which reads the framing |
| #104 | The request to remove the purge ← the How owner's own record of deploys. The record is inside. The chain ends inside, at the cause | Frame own-ground work (oG) |

**The same item under a wider scope.** With the PDLC as the scope, the What owner's classification is inside. #103's trace then runs on past it, to the product in use and the customer's basket, and stops at the customer, who is world. The entry act becomes oC, the classification, which is what `DDD-flow-03` names. The What → How seam is visible in that map only because the PDLC map declares the How as a scope within it. That is R-3: "if we started with the PDLC we wouldnt see the seam in the how because it wouldnt exist" read the other way round.

## Desk check against a junior engineer's first contact

Claude's desk check, `UNVERIFIED — Emil review`. It is a reading of this page, not a run. Running the junior-engineer test is Emil's act, as it is for the quick start.

| Part | What the junior engineer must do | Passes at first contact? | What fails, and the fix proposed |
|---|---|---|---|
| 1 | List the decisions their own team makes | **Fails as written.** "The How owner", "the What owner" and "the When owner" are lifecycle words | Ask "which decisions can your team make without asking anyone?" and list them. The owner names follow |
| 2 | Name what crosses into and out of the team's work, and two outcomes for each | Passes. "Name two ways it could turn out that cannot both be true" needs no canon word | Keep the word "determinable" out of the question and in the field name |
| 3 | Find the decision in force; say what they have seen; ask who bears it | Partly. Specified needs to know where decisions are written down. A junior engineer in a team without a written What fails here | Allow "none written" as a value. That is a finding, as #104's is |
| 3 | Write "not read" under actual | Passes mechanically, and confuses. Why would a field always say the same thing? | One sentence: "you only ever see what someone observed; the world itself is not a reading" |
| 4 | Pick the row of the gap table | Passes mechanically | — |
| 4 | Read the kind off the axis | **Fails without the axis.** The junior engineer cannot invent "realisation" | The procedure must give the axis, or step 1 must declare it first. This is Q-4 in `proposals.md` |
| 5 | Follow the chain back and stop at the first answer outside the team | Passes when part 1 passed. Fails with it | Same fix as part 1 |

## Findings

| # | Finding | Status |
|---|---|---|
| W-1 | The entry act depends on the scope. Under the How, #103 enters at plan the realisation. Under the PDLC it enters at the classification. `DDD-flow-03` is scoped to the PDLC and is not contradicted | Claude's reading, `UNVERIFIED — Emil review` |
| W-2 | The same determinable shows a different gap under a different scope. Under the PDLC, #101 is first "expected, with nothing specified" at the option pool. Under the How it is "specified, with nothing actual". Its position, product · not built, is the same under both | Claude's reading, `UNVERIFIED — Emil review` |
| W-3 | Own-ground demand finds a place among the gaps once the determinable is the arrangement's, not the product's. #104 is "expected, with nothing specified" on the arrangement. A dependency's CVE would be "specified against actual" on the arrangement. So own-ground differs from new and owed by whose determinable it is, not by its gap. This answers an open point of #80 with a proposal, not a ruling. #104 also shows a combination the PDLC's kinds do not name: built, with nothing specified. The arrangement behaves a way nobody decided | `[PROPOSED]`, `UNVERIFIED — Emil review` |
| W-4 | The kind needs a declared axis before part 4, and the procedure runs before step 1 declares axes. So the procedure declares at least the axis kinds are read on | `[OPEN]`, Q-4 |
| W-5 | The rate of change has a unit for two items and none for the market need | Carried from `successor-items.md` O-7 of 2026-11-17: no unit and no measure |
