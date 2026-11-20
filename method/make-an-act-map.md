# Make an act map

**Register: `[PROPOSED]`, every part of it.** The method is one thing: making an act map. It has
four moves, and each is `[PROPOSED]`: written down, not ruled as tested. The moves and their order
are Emil's ruling of 2026-11-19; that steps 2 to 10 are recorded on the acts and decisions is his
ruling of the same day; both are filed as `DDD-dec-124`. The claims the moves rest on are
**projected**: argued, with falsifiers nobody has met. Try it; do not rely on it.

> 1. **Scope the act map.**
> 2. **Place an act or decision.**
> 3. **Follow the determinable back to the edge and note the pull.**
> 4. **Do it again**, until every map you can find or think of is mapped and your pull sources
>    are identified.

Emil's words, 2026-11-19: "We need to help people then describe the act fully or else they cant
find the pull". The act description below is how.

**Weakest point.** Move 3 needs to know where each thing an act reads comes from. Often the
source is a person's judgement that no map holds. Then the trace stops at a finding, not at a
pull, and the map shows a hole where the reason for the work should be.

This card replaces the ten numbered steps. The old cards stay in this directory, as written, each
marked not live ([`README.md`](README.md)).

## The four moves

Each move is given in the step card's nine fields, "Value made visible" first. The fields are the
method draft's (`[PROPOSED]`). Where a field rests on a claim or a ruling, it is named.

| Field | 1. Scope the act map | 2. Place an act or decision | 3. Follow the determinable back to the edge and note the pull | 4. Do it again |
|---|---|---|---|---|
| **Value made visible** | What is yours to decide, and what is world. Where every trace will stop | One act or decision, described fully enough to find its pull. A field you cannot fill shows now, not in production | Why the act happens at all: its pull, the act that takes it in, and which part of the chain is yours | Your pull sources: every pull at the edge, the acts it enters, the demand no act answers, and where your edge is a dependency in a wider map |
| Step | Move 1 of 4 | Move 2 of 4 | Move 3 of 4 | Move 4 of 4 |
| Decision discharged | The scope: the decisions the map's holders take without asking anyone else. The ground axes, and the axis kinds of demand are read on | That this act is inside the scope, and its address | For each thing the act reads: produced inside, at the edge, or unknown. Where the trace stops | Whether to place another act, widen to another scope, or stop |
| Ground in | The people doing the work and the decisions they take | Move 1's scope and axes. An act or decision you can see: a request, an issue, a command, a review | The placed act's description, group A | The map so far and its findings |
| Act | List the decisions. Mark each inside or outside, once. Declare the ground axes. Declare the kind axis, starting from **built or not built**. Done by the holders, with whoever rules the decomposition | Fill group A of the act description. Fill group B where you know it | The trace (below) | Moves 2 and 3 for every act the trace placed, and for every act or decision in the scope that no trace reached. Then the edge pass. Then a further scope |
| Artefact out | The scope list and the declared axes, as graph data | An act site at its address, with its description. Or a decision anchored at an act site through its applicability predicate | Dependencies between act sites. A pull statement for each reading that reaches the edge. Rows in the index of determinables. Findings | The act map of `DDD-address-06` with its index. One map per scope and declaration of axes (`DDD-address-07`) |
| Cost and relocation | Everything outside the scope becomes ground that crosses the edge. Seams appear only where scopes are declared | Describing costs effort now. Demand moves from discovery in production to the description | A reading with no known source becomes a finding, not a guess | Grows with each act and scope |
| Exit check | Every decision named is marked inside or outside, once. Mechanical on the list; whether the list is complete is a judgement | Group A filled, each field passing its check. The occupant is not in the address | Every reading of the act ends at a placed act inside, at the edge with a pull statement, or at a finding | See "When to stop". **The stop is the principal's judgement** |
| Principal | Whoever rules the decomposition. The method names no role for it (`DDD-ground-06` region) | The same | The same | The same |
| Rests on | 2026-11-18 R-2 ("scope must be the first"); `DDD-address-06`, `-07`, `-10` | 2026-11-19 rulings; `DDD-ground-06`; `DDD-ground-01` | 2026-11-18 R-2 (the stop); `DDD-address-01`; `DDD-address-09`'s statement | 2026-11-19 ruling; G1 Q-4 ("both"); 2026-11-18 R-3; `DDD-address-07` |

## The act description

Two groups. **Group A** is the fewest fields that let the trace run. Fill it in move 2. **Group B**
is what steps 2 to 10 held. Fill it when you know it, and leave a field empty when you do not: an
empty field is itself something the map shows (G1 Q-6).

### Group A — for the trace

| # | Field | Of | Value when filled | Check | Rests on |
|---|---|---|---|---|---|
| A-1 | **Inside the scope**: which of the scope's decisions this act takes | Act | You know the act is yours, so a trace through it continues | It names a decision on move 1's list | 2026-11-18 R-2; `DDD-address-06` |
| A-2 | **The determinable** it resolves, with two or more outcomes that cannot all hold together | Act, decision | What the act settles, and so what could pull it | Two or more outcomes; no two hold together (a judgement) | `DDD-frame-13`; 2026-11-18 R-1; `DDD-address-09` |
| A-3 | **Each ground reading**, and where it comes from: an act inside (name it), something crossing the edge (name it), or "unknown" | Act | The trace's next hop, for every reading | Every reading has one of the three | `DDD-address-01`; `DDD-ground-02` ("Unknown is never a pass") |
| A-4 | **The address**: position on the declared axes and the layer path, with the occupant left out | Act | The act has one place on the map, so it is placed once | One address per act site; no occupant in it | `DDD-ground-06` |

### Group B — what steps 2 to 10 held

Some of these sit on the act. Some sit in a record kept per act site beside the map: who occupies
it, what it pulls, and its occurrences (`DDD-address-06`; G1 Q-3).

| # | Field | Held by | Of | Value when filled | Rests on |
|---|---|---|---|---|---|
| B-1 | The authority at this act's layer | Old step 2 | Act (its layer) | An act whose layer has no authority shows as unowned | Method draft, `[PROPOSED]` |
| B-2 | The decisions anchored here, each with its applicability predicate | Old step 3 | Act, decision | The backlog is visible. A decision with no act site is a candidate escape | `DDD-ground-01`; `DDD-address-06` (the index) |
| B-3 | For each reading: provenance (controlled, observed, inferred, institutional, missing) and tick rate. For the determinable: its rate of change | Old step 4 | Act | Missing ground is found before build | Method draft; `DDD-address-06`; `DDD-ground-02` |
| B-4 | The acceptance predicate, which closure senses hold for the arrangement allocated, and the assurance set from stakes | Old step 5 | Act | Where a verdict can be a mechanical check and where it needs a person | Upstream `term:closure`. Open: closure is classified before the arrangement is allocated (`DDD-dec-122`, K-2) |
| B-5 | The occupant: actor or arrangement, source, commitment level, assurance mechanism | Old step 6 | Occupancy record | Where demand sits and who carries it | `DDD-ground-06`: the occupant is never in the address |
| B-6 | Attribution, principal, authority, stake, remediation | Old step 7 | Decision, allocation | An auditable answer to the compliance question | Upstream `term:accountability`; `DDD-frame-08`; `DDD-flow-04` (PDLC) |
| B-7 | The components it pulls | Old step 8 | Derivation record | From an act, its components. From a component, every act that pulls it | `DDD-address-02`, `-03` |
| B-8 | Its occurrences, each with its time index | Old step 9 | Occurrence record | Evidence, not assertion | `DDD-address-01` |
| B-9 | The observed state, as a pointer to the latest observation, and behaviour at the two grains | Old step 10 | Determinable, act site | Escape seen as it happens, and the pulls a supersession opens | `DDD-address-05`, `-11` |

**A decision** is described by A-2 (the determinable it takes up, with its outcomes as the
alternatives), B-2 (its applicability predicate and the act sites it governs), B-6 (its principal)
and its commitment level (`DDD-ground-01`; `meta/way-of-working.md` §4).

That group A is enough to find a pull is `[PROPOSED]`, not a claim. It is falsified by an act with
group A filled whose pull the trace cannot find, or by a pull found only through a group B field.

## The trace

For someone at first contact.

1. Take the act you placed. Write down everything it reads before it can decide (A-3).
2. For each thing it reads, ask: **who made this the way it is?**
   - **Someone inside the scope, by an act.** Write "this act depends on that act, because it
     reads …". If that act is not on the map yet, place it next (move 2).
   - **Someone or something outside the scope**: another team's decision, a customer, a
     regulator, time passing. **This is the edge.** Write a pull statement for it, in the form on
     [step 1's card](01-map-and-index-acts.md#the-pull-statement). Stop following this reading.
   - **You do not know.** Write it down as a finding: "reads … from an unknown source". Do not
     guess. Ask the people who do the work.
3. **Do not write an act twice.** If the act is inside the scope on some occurrences and outside
   on others, find the ground axis it varies on.
   - If that axis is declared, they are two act sites at two addresses, one inside and one outside
     (`DDD-address-02`, `DDD-ground-06`). Place the one that is inside. The other is at the edge.
   - If no declared axis separates them, record a finding for move 1: **an axis is missing.**
   - The axis is a ground axis, never who occupies the act. The occupant is not part of the
     address (`DDD-ground-06`; upstream `term:act-address`).
   - Declaring a missing axis is a second declaration of axes. Under `DDD-address-07` that makes
     a second map, which supersedes the first (`DDD-ground-06` region: re-decomposition
     supersedes). Where a wider map shares the act, split it there too, or the two maps give one
     act two addresses (a limb of `DDD-address-07`'s falsifier).
4. If the act you would place next is already on the map, write the dependency and do not place it
   again. Dependencies between act sites may loop (`DDD-address-06`).
5. The act is traced when every reading ends in one of the three. Go on to the next act you placed.

Step 3 is Emil's G1 ruling on P-3 (2026-11-20). Its last two bullets are Claude's reading of
canon at `v5.15.2`, checked as he asked. The first of them, that the axis is a ground axis and
never the occupant, Emil confirmed at G2. The second, on a second map and a wider map splitting
the act too, is not confirmed: `UNVERIFIED — Emil review`.

## The edge pass

Inside move 4, after the trace (G1 P-4, option A). List each state that crosses the edge, in or
out. For each, ask: **who outside the scope is waiting on it, and what do they expect?** An
expected state that no act inside reads is "expected, with nothing specified": demand that nothing
answers. Write a pull statement for it, with "none" as its entry act.

The edge pass rests on no ruling beyond G1 P-4. It is there because a trace that starts from acts
finds only the pulls that already have an act.

## When to stop

For one map, move 4 can stop when:

1. every placed act has every reading ended at an act inside, the edge, or a finding;
2. the edge pass has asked every state that crosses the edge;
3. the principal accepts the findings as they stand, or opens a further scope.

**The stop is the principal's judgement.** The checks show that the trace closed. They cannot show
the map is complete: an address is blind to axes nobody declared (`DDD-ground-06`).

"Do it again" covers three loops (G1 Q-4, "both"):

1. every act the trace placed gets moves 2 and 3;
2. every act or decision in the scope that no trace reached is placed and traced. If it reads
   nothing and nothing reads it, it is a finding: a dead act, or a missing dependency;
3. each further scope you can map gets moves 1 to 4. A pull at this map's edge, followed past it,
   is a dependency in the wider map (2026-11-18 R-3; `DDD-address-07`).

The four states and their gaps check a map once its work runs. That check is #82's, not this
card's (G1 Q-5).

## Worked example: the How owner's lifecycle

The acme shop of [`applications/pdlc/`](../applications/pdlc/) is invented. Its act map is the
lifecycle data in [`applications/sdlc/acts/acts.ttl`](../applications/sdlc/acts/acts.ttl) and
[`applications/pdlc/graph/acts.ttl`](../applications/pdlc/graph/acts.ttl). The example reads that
data and changes none of it. It is exposition, written by Claude inside the framework, not
evidence: `UNVERIFIED — Emil review`.

### Move 1. Scope

The scope is the decisions the How owner takes: how a change is planned, built, checked, landed
and deployed, and the order of owed and own-ground work
([`sdlc.md`](../applications/sdlc/sdlc.md) §5). Outside it, and so world to this map: what the
shop must do, and whether a defect is owed (the What owner's); which new work comes first and when
a feature is switched on (the When owner's).

The ground axes are the ones the data declares: the surface read, the change locus and the
authority read. Kinds are read on **built or not built**.

### Move 2. Place an act: "plan the realisation" (o1b)

Someone on the team can see an issue being planned. That act is o1b. Its group A:

| # | Field | o1b |
|---|---|---|
| A-1 | Inside the scope | Yes: how a change is planned |
| A-2 | Determinable and outcomes | How the issue's change will be realised: a complete plan on the issue, or an incomplete one, paid again later at "direct on the issue" (o6) (`sdlc.md` §4). The two cannot both hold |
| A-3 | Ground readings, with their source | The framed issue (o1); the What owner's verdict "owed" (oC); the How owner's own-ground issue (oG). One per kind of demand (`lc:forKind`) |
| A-4 | Address | Surface: issue · locus: declared · authority: none. Layer path PDLC ▸ SDLC ▸ frame |

### Move 3. Trace o1b back to the edge

| Reading | Who made it so | Result |
|---|---|---|
| "the What owner's verdict: owed" (oC) | The What owner, who is outside the scope | **The edge.** The pull is #103's: reorder adds an out-of-stock line, specified against observed. Its pull statement is the one on [step 1's card](01-map-and-index-acts.md#worked-example-in-brief), with o1b as its entry act |
| "the How owner's own-ground issue" (oG) | The How owner, inside | Place oG next |
| "the framed issue" (o1) | The owner of the issue's declared locus. Inside when the locus is How, outside when it is What | Step 3. The axis it varies on is the change locus, which the data declares. So these are two act sites: o1 at locus How (inside) and o1 at locus What (outside, at the edge). The data holds one site, at locus "declared". **Finding**: the lifecycle data should hold two sites. Splitting them is not this card's to do |

### Move 2 and 3 again: "frame own-ground work" (oG)

| # | Field | oG |
|---|---|---|
| A-1 | Inside the scope | Yes: the order of own-ground work |
| A-2 | Determinable and outcomes | Whether a piece of the How owner's own ground needs work now: framed as an issue, or not |
| A-3 | Ground readings, with their source | **Not described.** The data gives no dependency. It records only that oG reads earlier deployments (`lc:readsEarlier m:o13`), with no "because" |
| A-4 | Address | Surface: issue · locus: How · authority: owner's scope. Layer path PDLC ▸ SDLC ▸ frame |

The trace cannot run. Nothing on the map says what the How owner read to decide there was
own-ground work, so oG's pull cannot be found. It stops at a **finding**: "oG reads … from an
unknown source". This is the ruling of 2026-11-19 met on the repository's own data: the act is not
described fully enough to find its pull.

The prose knows more than the map. `sdlc.md` §5 says own-ground work arrives from "the How owner's
own record: DORA trends, a dependency advisory, the arrangement, the platform". Written into A-3,
those would let the trace run. The DORA trends are read from the occurrence record of deployments
(inside). A dependency advisory comes from whoever publishes it (the edge). That move is the
practitioner's, asked of the people who do the work. It is not made here.

### One act described fully: o1b

Group A is above. Group B, from the lifecycle documents:

| # | Field | o1b | Source |
|---|---|---|---|
| B-1 | Authority at its layer | The How owner, who owns the SDLC | `DDD-dec-114` |
| B-2 | Decisions anchored, with predicate | Which How decisions and components the change touches, and in what steps. Applies to every issue that enters the SDLC, of any kind (Claude's reading of the three `lc:forKind` dependencies) | `sdlc.md` §4 |
| B-3 | Provenance and tick rate | The owed verdict and the framed issue: institutional, another owner's decision, one per issue. The own-ground issue: not declared. The determinable changes once per issue | `sdlc.md` §5; the data |
| B-4 | Closure and assurance | Human or model judgement, written on the issue. No act accepts the plan before work starts; "approve" (o10) accepts only the result. Open as O-8 | `sdlc.md` §4 and its O-8 |
| B-5 | Occupant | Human or model, in the occupancy record. Not in the address | `acts.ttl` (`lc:occupantLens`) |
| B-6 | Accountability | The How owner answers for owed work by time to restore. Stake and remediation: not filed | `sdlc.md` §5 and §18 |
| B-7 | Components it pulls | Not recorded. Empty, and visible as empty | — |
| B-8 | Occurrences | None in the example record. Empty, and visible as empty | `example-record.ttl` |
| B-9 | Observed | None. Its only observation would be the plan on the issue | — |

### Move 4. Do it again

- **Loop 1.** The trace placed oG and stopped there. Nothing more to place from o1b.
- **Loop 2.** Acts in the scope that no trace from o1b reached: "allocate the occupant" (o2b) to
  "deploy, dark" (o13). Each is placed and traced the same way. Not carried out here.
- **The edge pass.** Among what crosses the edge: the change in production, read by the What owner
  at "ready for users" (oR); the classification verdict, read by o1b. Each has an act inside that
  reads or produces it, in the lifecycle as written ([`pdlc.md`](../applications/pdlc/pdlc.md)
  §2.1). This pass finds no demand without an act. It looked only at what the seam table lists.
- **Loop 3.** The wider scope is the whole lifecycle, the PDLC. There, #103's pull is not at the
  edge: it enters at the classification act (oC), as `DDD-flow-03` says. In the wider map the How
  owner's edge is a dependency.
- **The stop.** Two findings stand: o1 is one site where the ruling makes two, and oG's readings
  are not described. Whether to stop is the principal's judgement.

## The canon it rests on

Read at the pinned tag `v5.15.2`. The claim files govern. Where this card and a claim disagree,
the card is wrong.

| Claim | Status | Where |
|---|---|---|
| `DDD-ground-06`, `DDD-ground-01`, `DDD-ground-02`, `DDD-ground-05`, `DDD-frame-13`, `DDD-frame-08` | projected | upstream, pinned in [`graph/upstream.yaml`](../graph/upstream.yaml) |
| `DDD-address-01` to `-11` | projected | [`core/claims/`](../core/claims/) |
| `DDD-flow-01` to `-04` | projected, PDLC only | [`core/claims/`](../core/claims/) |

## What would break it

- **A move.** The method draft's default, `[PROPOSED]`: a practitioner performs the move and
  cannot name the value it gave them. A junior engineer with this card alone cannot say which
  move they are in.
- **The act description.** An act with group A filled whose pull the trace cannot find.
- **The trace.** `DDD-address-09`'s falsifier: two practitioners on one scope and record name
  different entry acts.
- **The edge pass.** A worked case where it finds no pull the trace did not.
- **The stop.** A map that passes it, whose holders, shown it, name an act or a pull it misses.

**What this card does not move.** Every claim stays projected. The first independent case, T2b,
still tests the address claims, on a map made with this card (G1 P-7). No move becomes ruled
without a ruling.

[All of the method](README.md)
