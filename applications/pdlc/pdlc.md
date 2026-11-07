# The PDLC — the product lifecycle

**Register: `[PROPOSED]`, unruled.** This specification is the exposition of `DDD-dec-114`. It
has two layers:
- **What the decision files.** The decision files Emil's rulings of 2026-11-06 and 2026-11-07,
  Rounds 3 to 22 (verbatim in
  [`meta/sessions/2026-11-07-sdlc-and-pdlc/rulings.md`](../../meta/sessions/2026-11-07-sdlc-and-pdlc/rulings.md)).
  Rounds 16 to 22 entered by amendment before landing (Round 21).
- **What this text adds.** The text adds Claude's construction: the tables, the shapes, the
  metrics, the checks, the proposed What elements and the falsifiers. None of it is ruled. Where
  a sentence states a ruling, the round is named. Everything else is Claude's, `UNVERIFIED — Emil
  review`.

Where this text and `DDD-dec-114` disagree, the decision governs, and the text is wrong.

**Upstream basis.** The coordinates, the address and the accountability argument are canon in
`actor-indexed-determination`, pinned in [`graph/upstream.yaml`](../../graph/upstream.yaml) at
`v5.15.2`:

<!-- ddd:ref id=DDD-frame-01 -->
<!-- ddd:ref id=DDD-frame-02 -->
<!-- ddd:ref id=DDD-ground-06 -->
<!-- ddd:ref id=term:answerability -->
<!-- ddd:ref id=term:liability -->
<!-- ddd:ref id=term:seam-identity -->
<!-- ddd:ref id=term:capability -->

---

## 0. The weakest point

**The owners are this projection's, not canon's.** Canon names no owner roles. The What, When and
How owners are a placement of responsibility argued from upstream core/05 §5 and mapped onto
method step 7 (complete accountability). That step is itself `[PROPOSED]`, with nothing filed
beyond one line ([`method/07`](../../method/07-complete-accountability.md)). If the placement
rule fails, the three owners fall with it. It fails when a boundary decision cannot be split into
one owner's act and another's ground (§6).

**The second weakness: two proposed What elements.** The PDLC leans on two What elements that do
not exist yet: the product-assurance declaration and the observation need (§4, §5). Until the
What's schema carries them (successor items), product assurance and observability needs live in
prose. The How owner's capability to instrument well is then the only thing that makes the
evidence come back. That capability is a classification pin, and Round 16 names it as the
backstop, not the guard.

**The third weakness is empirical.** Nothing here has run. The forecast (§1), the option metrics
(§10), the meter (§3) and the seam's price (§13) are computations over a record that does not
exist yet. The SDLC starts writing it from edition 1 (`DDD-dec-115`).

## 1. The stance: delivery does not decide when

*Ruled (Round 6, wording approved by Round 14; refined by Round 19):* "Delivery does not decide
when. The How owner's duty is to take approved work to production as fast as the quality
constraints allow. The cadence that results is the forecast everyone else plans against."

- **The quality constraints** are the What, its ground and tolerance, and the **product
  assurance** (Round 19). Both are the What owner's.
- **Implementation assurance is the How owner's own** (Round 19, §4). Lowering it is the How
  owner's choice, guarded by outcomes read across seams (Rounds 19, 20).
- **The How owner's duty.** The shortest lead time within the What and the product assurance.
- **The forecast is computed, not promised.** An issue's expected delivery follows from two
  things:
  - its position in the When owner's order (the rank recorded at o2a);
  - the measured throughput, read from the SDLC's occurrence record (`DDD-dec-115` S-6).
- **The measures.** The measures are DORA's four keys, as
  [`production-as-ground.md`](../sdlc/production-as-ground.md) §2 reads them. They are the How
  owner's answerability (Round 20; [`../sdlc/sdlc.md`](../sdlc/sdlc.md) §18).

**The computation, `[PROPOSED]`.**
- **Inputs.** Throughput λ is new-demand changes reaching o13 per week, over the last N weeks.
  Flow time F runs from o2b to o13 for new demand, from the record. F is not DORA's lead time,
  which starts at the first commit.
- **The estimate.** An issue at rank k, not yet allocated, has an expected landing date of about
  now + k/λ + median(F). A forecast is a distribution: resample λ and F from the record.
- **Capacity is shared.** Owed and own-ground work (§9) share the How owner's capacity. They
  show in the forecast only as a lower λ for new demand, which is the only form in which the
  When owner sees them (Round 22).
- **When it changes.** The forecast changes when the order changes (a When decision), when λ or F
  change (the How owner's performance), or when product assurance changes (a What decision).
- **Delivery and landing.** Delivery is o16, the When owner's own act. The forecast is for
  landing, dark.

**This departs from how many organisations operate.** In many organisations the delivery process
is expected to move dates: a team is asked to "pull in" a feature, and the date becomes a target
the delivery side negotiates. Here the delivery side has nothing to negotiate. Its only lever is
lead time, and it is already obliged to minimise it. A date is held by changing the order (When),
or by cutting scope or product assurance (both What). It is never held by pushing the How owner
(§6, rule 1). Emil, Round 6: "many have the idea that delivery can have an impact on when
something is delivered. But its the how owners responsibility to have approved work go
production as fast as possible within the quality constraints."

## 2. The three owners

Each owner is a **scope under the product's genesis grant** (authority.md §2–3, `DDD-dec-87`,
`DDD-dec-85`): a grant held by one person, delegating from the genesis, accepted by its holder.
The genesis holder may hold any of the three. Each owner may be several holders, one per scope.
For the What owner, `what.md` §5.1 already divides the What into scopes over element kinds. "The
What owner" means the holder of the scope that covers the element in question.

| Owner | Owns | Acts it holds | Ruled by |
|---|---|---|---|
| **What owner** | The What: everything the How needs in order to implement (§3), including the acceptance relation and tolerance, its observability needs, and **product assurance** on the use act (§4). The mix between the software's share and the users' share. Its own evidence of the product in use (§5) | o1 (What and assurance loci), oC (classify a reported defect, §9), oR (ready for users), oU (holds the allocation of the acts of use) | Rounds 6, 7, 10, 16–19, 22 |
| **When owner** | The order of all **new** demand, and when each change reaches users. It is the business, where new demand enters, and the go-to-market owner | o2a (release for work: pull, decline, expire), o16 (turn a toggle on), a date promised outside (outside the arrangement) | Rounds 5, 10, 11, 22 |
| **How owner** | The SDLC: the process of getting approved changes to production. **Implementation assurance** (§4). The order of **owed** and **own-ground** demand (§9). Telemetry of the product in use, which it adds (§5) | o1 (How locus), oG (frame own-ground work), every SDLC act from o1b to o13 ([`../sdlc/sdlc.md`](../sdlc/sdlc.md)) | Rounds 5, 8, 16, 19, 20, 22 |

**The When owner is the go-to-market owner** (Round 10). Relative importance is judged by when a
feature will have the best market impact. That is why ordering new demand belongs to the When
owner, and why the When owner is also the biggest contributor to the option pool (Round 11).

**The How owner understands digital product development** (Round 16). In canon terms that is a
capability requirement on the occupant of the How scope: pinning by classification, the loosest
of `core/04`'s pinning resolutions. §5 says how the encoded observation needs lower the
dependence on it.

**Ground.** *Ruled (Round 14):* "Their ground is their own to control, but the seams between them
supplies some to each". Each owner controls its own ground. Ground that crosses a seam is
supplied by its producer and is read-only for the receiver.

### 2.1 The seam table, checked against the act map

The prompt asks that every row be an output of one owner's act and appear in the ground reading
of another owner's act. Rows 1 to 8 are Round 14's table, not ruled. The telemetry row is Round
16's, ruled. The last two are Claude's additions from Round 22. The act map is
[`graph/acts.ttl`](graph/acts.ttl) with [`../sdlc/acts/acts.ttl`](../sdlc/acts/acts.ttl).

| From → To | Ground supplied | Produced by | Read by | Check |
|---|---|---|---|---|
| When → What | A pulled option (a need) | o2a (When) | o1 (dependency "the pulled option") | **Holds** |
| When → What | A scope-cut proposal | **No act** | The What owner's What-locus o1 | **Gap.** No act on the map produces it. It cannot be an option, because an option is never a What change (Round 11). Open item O-3 |
| What → When | Each element's outcome and acceptance | Earlier o1s (What) | o2a (`lc:readsEarlier m:o1`) | **Holds** (fixed in the first session) |
| What → When | The ready-for-users verdict | oR (What) | o16 (dependency) | **Holds** |
| What → How | The What, the product assurance | o1 (What and assurance loci) | o1b (dependency, new demand), and the How owner's implementation-assurance decisions | **Holds** |
| When → How | A released issue, in order | o2a (the pull and its rank) | o2b (dependency, `lc:forKind lc:NewDemand`) | **Holds, for new demand only** (Round 22). Owed and own-ground issues cross no When → How seam |
| How → When | The record: cadence, lead time, change failure rate | The dispatcher's occurrence records, o3 to o13 | o2a (`lc:readsEarlier m:o13`); the forecast | **Holds** |
| How → What | The change in production, dark, with its verdicts | o13, with o9 and o10's verdicts | oR (dependency) | **Holds** |
| **How → What** | **Telemetry of the product in use** (Round 16, ruled) | o13 deploys the instrumentation. oU, occupied by the software, emits the data | oR (presence, for each observation need: `lc:checksObservation`); oC and later o1s (`lc:readsEarlier m:oU`): the What owner's evidence for superseding the What (method step 10) | **Holds.** Presence is checked before ready-for-users (§5). The data is read after delivery |
| What → How | A classification verdict: owed (Round 22) | oC (What) | o1b (dependency, `lc:forKind lc:OwedDemand`) | **Holds** |
| What → When | A classification verdict: new (Round 22) | oC (What) | o2a, through the option the What owner proposes at o0 | **Holds, indirectly.** A defect classified new becomes an option. The When owner reads it as an option, never as a defect |

**Finding F-2: the order of o1 and o2a** (first session). Round 11's ruled reading has the When
owner pull an option at o2a, which the What owner then frames at o1. The map follows it: o0 → o2a
→ o1 → o1b → o2b, for new demand.

**Falsifier: a piece of ground two owners both need to write.** Two candidates, both resolved by
splitting what each owner writes:
- **The issue thread.** The issue body is the framing, written only under o1's scope (or oG's,
  for own-ground). The realisation plan is a separate section or comment, under the How scope.
- **A toggle.** Its existence and default are the How owner's. Its on state is the When owner's.

## 3. The What owner's output

*Ruled (Round 18):* "its more than the needs it's everything the how needs in order to implement
including the assurance". At o1 the What owner frames the full ground and tolerance for the How's
acts. [`what.md`](../sdlc/what.md) §1.1 puts it this way: "the What as a whole is the software's
declared ground, over which decisions are made, and the tolerance each act must meet." The table
reads each part against `what.md` at `1ab1de0`.

| `what.md` | The What owner declares | What the How gets from it |
|---|---|---|
| §3.0 Product and boundary | The product node, its purpose, its systems and journeys, product-wide demands and targets | What is being built, where it ends, and which systems it spans: the boundary of every How decision |
| §3.1 Domain model | Bounded contexts, entities, value objects, relations, invariants, reference data | The data the code holds, in the business's language, with the invariants it must never break |
| §3.2 Event model | Commands, events, views; UI steps, interaction objects, context of use, accessibility criteria, the page graph; the system | The behaviour to realise, step by step, screen by screen, for each context of use |
| §3.3 Deciders | `decide` and `evolve`: the business rules as acceptance and rejection | The executable behaviour: what each command does, and what it refuses. These are the conformance cases for o9 |
| §3.4 Projectors | The read models and the events they are built from | What each view shows and how it is derived |
| §3.5 Named-algorithm primitives | The algorithm or standard, its I/O contract, its oracle | Computations specified by reference, testable against the oracle |
| §3.6 Quality demands | Runtime bounds and architectural constraints, located | The non-functional, made checkable: the bounds to instrument (a contract over telemetry facts) and the constraints to build to |
| §3.7 Subjects and authorization | Subject kinds and their claims: who may act in the product | The authorization to implement, separate from authority over the product |
| §4.1 Declared targets | Platform contexts, interaction classes, design-system and content-store editions | The targets the How realises against |
| §4.2 Obligations | Reification exists, reification coverage, content coverage | The pairs that must be covered or declared missing |
| **Observation need** `[PROPOSED]` (§5) | Where in the product the evidence of use comes from, what data is needed, and which acceptance or outcome it evidences (Round 17) | The telemetry to add, as a declared requirement, with its presence checked before ready-for-users |
| **Product-assurance declaration** `[PROPOSED]` (§4) | How sure we must be that users perform the designed act, located and inherited downward (Rounds 18, 19) | The level of evidence the observation needs must reach, and the user-side share the What owner adds. Not the How's checks: those are implementation assurance (Round 19) |

**The meter.** *Ruled (Round 18):* "Yes (Recommended)". The What-locus share of o6 directions is
the PDLC's meter of whether the What gave the How everything it needed. Every o6 occurrence
records the locus of the decision it supplied (`lc:suppliedLocus`, [`../sdlc/sdlc.md`](../sdlc/sdlc.md)
§13). The meter is the count of o6 with `lc:suppliedLocus lc:What`, divided by all o6, per issue
and per What element. It is read across the How → What seam. A What-locus direction is a
decision the What owed and did not give, supplied late at human price. A falling share means the
What is getting more complete.

## 4. Two assurances

*Ruled (Round 19):* "Assurance is the feature so its how sure can we be that our users does the
act we designed. Not how sure are we the feature is implemented correctly that is the Assurance
that the how must own". Assurance is a coordinate of each act's `DDD-frame-01` tuple, so there
are two, on two acts.

| | Product assurance | Implementation assurance |
|---|---|---|
| **On the act** | oU, the use act, occupied by users and software | The How's acts: build, accept, land (o4 to o13) |
| **Asks** | How sure can we be that users do the act we designed? | How sure are we that the feature is implemented correctly against the What? |
| **Owner** | What owner | How owner |
| **Met by** | The software, and the user-side share: training, guidance, procedure (Round 7) | Mechanical checks (o9), o10's depth, independence of acceptance (Round 13) |
| **Evidenced by** | Observation needs and evidence in use (Rounds 16, 17) | The gates' verdicts, then change failure rate and the ready-for-users verdicts |
| **Judged at** | oR, ready for users | o9 to o11, and afterwards by the outcomes |
| **Declared in** | The What, as a product-assurance declaration `[PROPOSED]` | A How decision, per What element or per act ([`../sdlc/sdlc.md`](../sdlc/sdlc.md) §5) |

**Product assurance decides two things:** which observation needs the What must carry, and how
much user-side share is required. A high level needs strong evidence that users perform the act,
and may need training as well as software. The ready-for-users verdict judges whether both are
there.

**The product-assurance declaration, `[PROPOSED]`.** A What element, located like a §3.6 demand:
within the product, a system, a flow, a step, a Decider or a Projector. It is inherited downward,
so an element without its own declaration takes its nearest ancestor's. It states how sure we must
be that users perform the designed act. Two levels are proposed as a start, `UNVERIFIED — Emil
review`:
- **observed**: the act's completion is observed in use;
- **evidenced**: the act's completion is observed, and the acceptance it serves is evidenced by
  an outcome measure.

The declaration is not an o9 check list, an o10 depth or an independence rule. Round 19 corrects
Round 18 on exactly this point: those belong to implementation assurance.

**The guard on implementation assurance.** *Ruled (Round 19):* "Outcomes, read across seams
(Recommended)". *Ruled (Round 20):* "And if they don't thats fine - then it was properly not
giving any value."
- **Lowered verification shows** as change failure rate and failed ready-for-users verdicts. Both
  are in the record the What and When owners read, and the How owner answers for them.
- **If lowering moves neither,** the verification removed gave no value. The How owner may keep
  tuning implementation assurance down until the outcomes move.
- **A withdrawn falsifier.** In Round 19, Claude proposed the falsifier "implementation assurance
  falls, and neither measure moves". Emil ruled it wrong in Round 20, and it is withdrawn. Its
  replacement, also Claude's and `[PROPOSED]`, is §14, falsifier 4.

## 5. Evidence in use and observation needs

*Ruled (Round 16):* "I agree the telemetry is the hows to add and the rest is the what to gather.
Which is why you need a how owner that understands digital product development".

| Evidence of the product in use | Whose | How it reaches the What owner |
|---|---|---|
| Telemetry of the product in use | How owner's to add | Across the How → What seam, read-only, beside the change in production (§2.1) |
| User research, support signals, training outcomes, and all other evidence | What owner's own ground | Its own gathering. No seam |

The What owner judges product acceptance (oR) and supersedes the What from this evidence (method
step 10, `[PROPOSED]`). Without the Round 16 row, nothing brought the product in use back to it.

**Observation needs.** *Ruled (Round 17):* "what people needs to add their observability needs to
the specification so its clear where in the product they get their data and what data they
need". The form below is Claude's proposal, `[PROPOSED]`:
- **A located What element.** An observation need is located like a §3.6 demand: the product, a
  system, a flow, a step, a Decider or a Projector.
- **What it declares.** The data needed, and the acceptance or outcome it evidences.
- **Not a quality demand.** It has no bound, so it is not a third kind of quality demand. §3.6
  admits exactly two: "a quality demand is one of exactly two kinds". It is its own element kind.
- **Its How side** is a contract over `telemetry` facts, anchored to the need. That is the
  pattern how.md's H-9 gives a runtime bound's measurement wiring (`DDD-dec-60`, superseded by
  `DDD-dec-70` with the telemetry facts unchanged).
- **Checked for presence before ready-for-users.** The verdict records, per need, whether the
  telemetry exists (`lc:checksObservation`), and a ready verdict with any need unmet is refused
  (`lc:ReadyNeedsTelemetryShape`).
- **Its own decision.** Adding it changes the What's schema (`ontology.ttl`, `shapes.ttl`), which
  goes by its own decision (successor items).

**The capability pin and the guard** (Round 16, Claude's reading, `[PROPOSED]`).
- **The pin.** "A How owner that understands digital product development" is, in canon terms,
  pinning by classification: an occupant selected for a capability envelope (`core/04`,
  `term:capability`). It is the loosest pin, and the costliest to rely on alone.
- **The encoded needs are the guard.** With each What element naming the evidence of success it
  needs, the How owner's instrumenting is a declared requirement, checked mechanically before
  ready-for-users.
- **The pin is the backstop.** It catches what the needs did not foresee.

## 6. The placement rule

*Ruled (Round 10):* "Adopt it (Recommended)". Responsibility is placed **per decision, not per
role**. For each boundary decision exactly one owner holds the act, with control and liability.
Another owner's verdict enters it only as read-only ground.

**The argument, from upstream core/05 §5.**
- **Separable.** Accountability decomposes into answerability, liability and control, which
  "come apart in practice and must not be fused".
- **The failure mode.** "A party can be answerable and liable with no control — unfair, and
  ineffective; a party with control can shed liability through organisational design."
- **What the rule does.** Placing each boundary decision with one owner gives control and
  liability to the same party, decision by decision.

| Boundary decision | Act | Owner (control and liability) | Ground it reads (read-only) |
|---|---|---|---|
| What the product must do: acceptance and tolerance | o1, What locus | What owner | A pulled option (When); evidence in use (own, and telemetry from How) |
| Product assurance, and the mix between software and users | o1, assurance locus | What owner | The stakes in the What; failed ready-for-users verdicts |
| Implementation assurance | A How decision (o1b, or How-locus o1) | How owner | The What and the product assurance (What); its own DORA keys |
| Ready for users | oR | What owner | The change in production, dark, with its verdicts, and telemetry presence (How) |
| Owed or new, for a reported defect | oC | What owner | The report; the What in force; telemetry (How) |
| The order of all new demand | o2a | When owner | The What elements and their declared acceptance (What); the cadence (How) |
| The order of owed and own-ground demand | Inside the SDLC (o2b) | How owner | The classification verdict (What); its own record |
| Turning a change on | o16 | When owner | The ready-for-users verdict (What) |
| A date promised outside | Outside the arrangement | When owner | The forecast, computed from the record (How) |
| Cutting scope to meet a date | o1, What locus | What owner | The When owner's proposal (When) |

**The three rules** (Round 10):
1. **The When owner may propose a What change but never make one.** A date is held by cutting
   scope or product assurance (both the What owner's) or by changing the order, never by pushing
   the How owner.
2. **The What owner declares readiness but never picks the date.**
3. **A dispute escalates to the genesis grant holder.** Escalation "routes a determination to an
   accountability-bearing actor — not merely to a more capable one" (core/05 §5).

**Relative importance** (Round 10). The What owner declares each element's outcome and acceptance.
The When owner judges importance by when a feature will have the best market impact.

**Answerability, per owner.** For the How owner, answerability is the DORA keys (Round 20). For
the What owner, it is the meter (§3) and the ready-for-users verdicts against what users then do
(§5). For the When owner, it is the option metrics (§10) and the market outcome of its order.

**Mapped to method step 7, `[PROPOSED]`.** Step 7's one filed line reads: "Attribution,
principal, authority, stake, remediation per allocation." For each row of the table:
- **Attribution.** The act's record, signed under the owner's scope (authority.md §4.1).
- **Principal.** The scope's holder.
- **Authority.** The grant.
- **Stake.** The outcome it bears on.
- **Remediation.** Supersession by a later decision under the same scope, or escalation.

Canon names no owner roles. This mapping is Claude's.

**Falsifier.** A boundary decision that cannot be split into one owner's act and another's
ground. It is then jointly owned, it belongs to the genesis grant holder, and the rule has failed
for it.

## 7. The four loci

*Ruled (Round 4):* "Yes, four values (Recommended)". An issue declares its locus: the coordinate
of DDD-frame-01's tuple ⟨task, ground, acceptance relation, tolerance, arrangement, assurance⟩
that the change moves. *Ruled (Round 3):* it is declared on the issue, and the dispatcher refuses
an issue without one.

| Locus | Coordinates moved | Acceptance path |
|---|---|---|
| **What** | Acceptance relation, tolerance | The occupant drafts a decision anchored to the What element it changes. The What owner accepts it. Tools never change the What (`DDD-dec-42` O-5) |
| **Assurance** | **Product** assurance (Round 19) | The What owner accepts it. It sets the observation needs and the user-side share required (§4). A change to implementation assurance is **How**-locus |
| **Ground** | Ground | Each owner's own ground is controlled by that owner. A ground-locus issue declares whose ground it changes, and that owner accepts it. Ground crossing a seam is supplied by its producer and read-only for the receiver (Round 14) |
| **How** | Arrangement: How decisions and the code realising them, one locus (Round 3); implementation assurance (Round 19) | Handed to the SDLC (o1b onward), accepted at o10 by a holder of Approve for the How scope. A change to the SDLC arrangement itself is How one layer up ([`../sdlc/sdlc.md`](../sdlc/sdlc.md) §10) |

**Locus and kind are different axes.** The locus says which coordinate a change moves. The demand
kind (§9) says why the work exists. An owed issue is usually How-locus: the software is brought
back to the What. An own-ground issue is How-locus or ground-locus (the How owner's ground). A
new-demand issue may be any locus.

**Why planning is not a locus.** Planning moves no coordinate (Round 4). Time in canon is the
causal time index (`DDD-address-01`).
- **Derived order** comes from the causal index.
- **Chosen order** is the When owner's decision for new demand, recorded at o2a as the rank, and
  the How owner's for owed and own-ground demand (Round 22).

The coordinate **task** is not a locus value. Claude reads it, `UNVERIFIED — Emil review`, as
what the issue itself names.

## 8. Priority is a When decision

*Ruled (Round 12):* "this also solves the classic problem of a product owner, owning the priority
which is inherently wrong. That's a when decision". Round 22 sharpens it: the When owner orders
new demand, and the How owner orders owed and own-ground work (§9).

**The Scrum Guide's own wording** (the 2020 Scrum Guide, November 2020, the current edition,
[scrumguides.org/scrum-guide.html](https://scrumguides.org/scrum-guide.html), read 2026-11-07):

> "The Product Owner is also accountable for effective Product Backlog management, which
> includes:"

and the third of its four items is

> "Ordering Product Backlog items; and,"

The same guide says "The Product Owner is one person, not a committee." It also says "The
Product Owner may do the above work or may delegate the responsibility to others." and
"Regardless, the Product Owner remains accountable." It defines the backlog as "an emergent,
ordered list of what is needed to improve the product."

**The departure.**
- **Two decisions in one role.** The classic product owner holds a What decision (creating the
  items) and a When decision (ordering them) at once.
- **Ground they do not hold.** Priority is importance relative to the queue and the market window.
  That ground is the When owner's (Round 10).
- **Liability without control.** A product owner who sets priority bears liability without
  control for its market outcome (core/05 §5).
- **Three kinds of demand in one list.** The backlog also orders all three kinds of demand in
  one list (§9).

**One person may hold both scopes.** *Ruled (Round 12):* "Yes, acts kept apart (Recommended)".
Each act is recorded under its own scope. With no second party, the genesis grant holder reviews.

**Falsifier.** An organisation where the same person holds both scopes and the record cannot tell
their When decisions from their What decisions.

## 9. Sources of pull: three kinds of demand

*Ruled (Round 22):* "determination pull will come from different sources … Which is why bugs or
technical debt is hard to put into the classic backlog". The kinds: "Adopt (Recommended)". The
classifier: "What owner (Recommended)".

| Kind | Is | Detected by | Ordered by | Through the pool? |
|---|---|---|---|---|
| **New** | A need not yet in the What: new acts, new acceptance | The market, via the When owner (o0); or the What owner, from evidence in use or a change in its ground | When owner (o2a), framed by the What owner (o1) | **Yes** |
| **Owed** | A decision already in the What that the software does not meet. The demand was allocated, but at the act nobody decided it (an escape) | The record, the gates, users, telemetry | How owner. It is restored, and measured as time to restore | **No** |
| **Own-ground** | Work on the How owner's own ground: technical debt, the arrangement, dependencies, platform | The How owner's own record (DORA trends) | How owner, justified by the DORA keys | **No** |

**Sources, by kind.**

| Source | Kind | Enters at | Ordered by | Pool |
|---|---|---|---|---|
| A market need (a customer segment cannot do something it will pay for) | New | o0, by the When owner | When | Yes |
| Users can't do the designed act: evidence in use shows the act is not performed (product assurance not met) | New, a What change: a different design, or a user-side share (Round 7) | o0, by the What owner | When | Yes |
| The software deviates from the What: a defect against a Decider, a bound or an invariant in force | Owed, by the What owner's classification (oC) | o1b, without o2a | How | No |
| A reported defect the What owner finds is the What being wrong, not the software | New, by the classification (oC) | o0, by the What owner | When | Yes |
| Technical debt, the arrangement, the How owner's ground (a dependency's CVE, a platform end of life, a slow pipeline) | Own-ground | oG, by the How owner | How | No |
| Regulation, or another change in the What owner's ground | New: the What must change | o0, by the What owner | When | Yes |

**Why the classic backlog struggles.** It mixes three kinds of demand under one orderer, who holds
the ground for one of them.
- **New demand** is judged on market ground: when will this have the best impact?
- **Owed demand** is judged on the What in force: the software owes it, and every day it stays
  unmet is time to restore.
- **Own-ground demand** is judged on the How's record: does it lower lead time, change failure
  rate or recovery time?

A single orderer weighs a bug against a feature on market ground. The bug was never a market
question, so it loses or wins by accident. Technical debt cannot be argued on market ground at
all, so it waits until it shows as an incident, and then it arrives as owed demand. Separating
the kinds gives each its own orderer, with the ground to judge it.

**The classification verdict (oC).** It is the What owner's act. A reported defect is owed if the
software breaks the What in force, and new if the What must change. Only the What owner holds the
What in force, so the classification is its verdict, read by the How owner (an owed verdict enters
the SDLC at o1b) and by the When owner (a new verdict becomes an option). In the shapes,
`lc:ClassificationShape` refuses a classification by any other owner, or one that is neither owed
nor new.

**What the When owner sees.** It sees owed and own-ground work only as its effect on cadence: a
lower throughput for new demand (§1).

**The guard, from both sides** (Round 20's guard applied to own-ground work):
- **Too little own-ground work** shows as rising change failure rate, lead time and time to
  restore.
- **Too much** shows as falling cadence with no DORA improvement.

The How owner answers for both, with the DORA keys.

**The flow, redrawn with every entry point.** A stream in causal order. Each line is a state
change.

```
NEW DEMAND
  o0   propose an option ............... When owner (market), or What owner (evidence, regulation, a "new" verdict)
  o2a  release for work ................ When owner orders
  o1   frame the issue, declare locus .. locus owner
        │
OWED DEMAND                              │
  oU   the product in use ─┐             │
  oC   classify a defect ──┴─ owed ──────┤   What owner's verdict (a "new" verdict goes to o0)
                                         │
OWN-GROUND DEMAND                        │
  oG   frame own-ground work ────────────┤   How owner, from its own record
                                         ▼
  o1b  plan the realisation ... o2b allocate ... o3 … o13 deploy, dark      the SDLC; How owner orders owed and own-ground
        │
  oR   ready for users ................. What owner (new demand with a toggle)
  o16  turn the toggle on .............. When owner
  oU   use the product ................. software and users → telemetry (How) and evidence (What) → oC, o0, o1
```

An owed fix restores behaviour the What already promised. It is usually not behind a new toggle,
and needs no o16. Its o13 records which earlier deployment it restores (`lc:restores`), which feeds
change failure rate and time to restore ([`../sdlc/sdlc.md`](../sdlc/sdlc.md) §18).

**Falsifiers** (Round 22, proposed with the adopted kinds; `[PROPOSED]`):
- an item that cannot be classified as new, owed or own-ground;
- an implementation bug that needs the When owner's ordering to get fixed.

## 10. The pull system and the option pool

*Ruled (Round 11, reading approved by Round 14; Round 22):* the When owner is the business, and
new demand enters the product there. The PDLC is a pull system for new demand: new work moves only
when the When owner pulls an option from the pool (o2a). The SDLC never pushes new demand. Owed and
own-ground demand do not go through the pool (§9).

**o0 propose an option.** Any owner may propose, and the When owner is the biggest contributor.
The What owner contributes specification gaps, user feedback, regulation, and defects it
classifies as new. Round 11's reading had the How owner contribute arrangement changes and
technical debt. Under Round 22 those are own-ground demand and bypass the pool, so the How owner
contributes only the new demand it detects.

**What an option is.** *Ruled (Round 11):* "Yes, outcomes only (Recommended)".
- **An outcome or need.** An option states who cannot do what, and by when it matters.
- **Never a What change.** The What owner turns a pulled option into What decisions at o1.

**How an option leaves.** *Ruled (Round 11):* "Yes, recorded (Recommended)". Every option leaves
by a recorded When-owner decision:

| Exit | Record |
|---|---|
| **Pulled** (o2a) | The issue it became, and its rank |
| **Declined** | With a reason |
| **Expired** | When its market window passed, and not before |

**The record shape (SHACL).** The shape is in [`graph/shapes.ttl`](graph/shapes.ttl) (`lc:OptionShape`,
`lc:ExitShape`, `lc:DeclinedShape`, `lc:PulledShape`, `lc:ExpiredShape`). An option carries:
- its contributor;
- the outcome stated (`lc:need`);
- its market window (`lc:mattersBy`);
- when it was proposed;
- at most one exit, decided by the When owner.

An option naming a What element it changes is refused. Run
`python3 applications/pdlc/graph/check.py`.

**Metrics from the record:**

| Metric | Computation |
|---|---|
| Option age | For open options, now − `proposedAt`. For closed ones, `decidedAt` − `proposedAt` |
| Contributor share of proposed options | Options by `contributor` / all |
| Contributor share of pulled options | Pulled by `contributor` / all pulled |
| Decline rate | Declined / closed |
| Expiry rate | Expired / closed |

**Worked over the illustrative pool** ([`graph/example-pool.ttl`](graph/example-pool.ttl), which is
invented): five options; the When owner proposed three, the What owner one and the How owner one.
Two were pulled, one declined, one expired, one is open. The When owner's share is 3/5 of proposed
and 1/2 of pulled. The decline rate is 1/4 and the expiry rate 1/4. Under Round 22, the How
owner's option (a manual cache purge on every deploy) would no longer be an option: it is
own-ground work. The example keeps it as it stood, and records this here.

**Falsifiers.**
- An option reaches o1 already phrased as a What change the What owner did not make.
- An option leaves the pool with no recorded decision.

## 11. The PDLC's acts on the act map

The act map is the form of method step 1. It is graph data in [`graph/acts.ttl`](graph/acts.ttl),
with the SDLC's acts in [`../sdlc/acts/acts.ttl`](../sdlc/acts/acts.ttl): one map, validated
together.
- **The PDLC's acts:** o0, o2a, o1, oC, oR, o16, oU.
- **On the SDLC side:** oG, own-ground framing, is the How owner's entry point.
- **Kind-scoped dependencies.** o1b depends on o1 (new), oC (owed) or oG (own-ground), by
  `lc:forKind`. o2b reads o2a for new demand only.

The ids o14 and o15 are not reused.

## 12. Release toggles, from the PDLC's side

*Ruled (Round 5):* "Release toggles (Recommended)". *Ruled (Round 10):* "Yes, as a constraint
(Recommended)".

- **Turning a toggle on (o16) is the When owner's act.**
- **o16 reads the What owner's ready-for-users verdict (oR).** The verdict covers the software's
  share and the user-side share. Since Rounds 16 and 17, it also covers the presence of the
  telemetry each observation need asks for.
- **The constraint.** Turning on an unready toggle is refused (`lc:ToggleOnShape`). A verdict
  that is ready while an observation need's telemetry is absent is refused
  (`lc:ReadyNeedsTelemetryShape`).
- **Creating and retiring a toggle are the How owner's**, inside the SDLC
  ([`../sdlc/sdlc.md`](../sdlc/sdlc.md) §7).

## 13. The seam to the SDLC

*Ruled (Round 9, reading approved by Round 14):* the SDLC is a composite act within the PDLC.
Every SDLC occurrence's layer path begins PDLC ▸ SDLC.

| Direction | What crosses | Where |
|---|---|---|
| Into the SDLC | A released issue (new demand) | o2a → o2b, framed at o1 |
| Into the SDLC | An owed issue | oC → o1b (the What owner's classification) |
| Into the SDLC | The What, and the product assurance | Read as ground, never written by the SDLC |
| Out of the SDLC | Production state, dark | o13 → oR → o16 |
| Out of the SDLC | Telemetry of the product in use | o13's instrumentation, oU's data → oR (presence), oC, o1 |
| Out of the SDLC | The record, with the DORA keys | The occurrence record (`DDD-dec-115` S-6, S-10) |

Own-ground issues start inside the SDLC (oG) and cross no seam on the way in.

**Nothing else crosses.** No calendar input enters the SDLC. The SDLC is given an order for new
demand and a product assurance, and returns a cadence and its DORA keys.

**The seam's price** (upstream core/06, |D_comp| = |D_single| + |S|). Splitting the lifecycle
manufactures seam demand S. Paying it down is one-time specification work:
- the issue's form (locus, kind, acceptance criteria);
- the What, complete for the How (§3), with its observation needs and product assurance;
- the record's shape.

"Skip it and S does not disappear, it escapes."
- **Mechanism at the seam, not actor.** No orchestrating actor stands at this seam: records cross
  it. That buys scale with no poisonable centre, paid for with rigidity.
- **Where the escape shows.** In o6 directions that supply a What decision.
- **The price, measured** by the meter (§3): the What-locus share of o6.

## 14. Falsifiers

1. **A behaviour change that moves no coordinate.** An issue's change alters behaviour but moves
   no coordinate.
2. **A change that needs a "when".** A change that can only be stated with a "when" in it.
3. **Forecast error out of band.** Forecast error beyond a band Emil sets (O-4).
4. **Blind outcome measures.** An escape reaches users that neither change failure rate nor the
   ready-for-users verdicts record. Then the outcome measures are blind, and the guard on
   implementation assurance fails. `[PROPOSED]`, Claude's (Round 20). It replaces "the How owner
   can shorten lead time by lowering assurance", which Round 19's split made wrong: the How owner
   may lower implementation assurance, and is guarded by outcomes.
5. **Users reached before o16.** A landed change reaches users before o16.
6. **An unrecorded user-side share.** A feature meets its software acceptance, is turned on, and
   fails its product acceptance for want of a user-side share nothing recorded.
7. **A toggle turned on without a verdict.** A toggle is turned on without a ready-for-users
   verdict, and nothing refused it.
8. **A calendar input across the seam.** A calendar input has to cross the seam for the SDLC to
   work.
9. **Evidence by no route.** A What element is superseded on evidence that reached the What owner
   through no recorded seam and was not its own gathering. Then a route for evidence of the
   product in use is missing from §5.
10. **A complete-looking What that fails.** A How ships with no What-locus directions and fails
    product acceptance. Then the meter (§3) reads the What as complete when it was not: zero o6
    What-share does not mean the What gave the How everything.
11. **An unclassifiable item.** An item cannot be classified as new, owed or own-ground (§9).
12. **A bug that waits on the When owner.** An implementation bug needs the When owner's ordering
    to get fixed (§9).

The falsifiers of §2.1 (ground two owners must write), §6 (a decision that cannot be split), §8
(When and What decisions indistinguishable) and §10 (an option phrased as a What change, an option
leaving with no record) are part of this list.

## 15. Open items

| # | Item | Closes it |
|---|---|---|
| O-1 | Whether `applications/sdlc/` should one day nest under `applications/pdlc/`. That would be a supersession of `DDD-dec-42`'s placement | Emil |
| O-2 | How `applications/organizations/` relates. `DDD-org-03` ("priority as a governed decision") orders backlogs by decisions based on statused value-claims. Under §8 and §9 those are When decisions over new demand only | Emil |
| O-3 | The scope-cut proposal has no act on the map (§2.1) | Emil |
| O-4 | The forecast error band (§14, falsifier 3) | Emil |
| O-5 | F-2: o2a before o1 | Emil |
| O-6 | Record kinds for the When owner's acts (o2a, o16, an option's exit) and for the classification (oC) in the authority profile | A successor session |
| O-7 | The product-assurance levels (§4): two are proposed | Emil |
| O-8 | The observation need and the product-assurance declaration as What elements: the What schema, by their own decisions (successor items) | Emil, then a successor session |
