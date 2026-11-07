# The PDLC — the product lifecycle

**Register: `[PROPOSED]`, unruled.** This specification is the exposition of `DDD-dec-114`. It
has two layers:
- **What the decision files.** The decision files Emil's rulings of 2026-11-06 and 2026-11-07,
  Rounds 3 to 15 (verbatim in
  [`meta/sessions/2026-11-07-sdlc-and-pdlc/rulings.md`](../../meta/sessions/2026-11-07-sdlc-and-pdlc/rulings.md)).
- **What this text adds.** The text adds Claude's construction: the tables, the shapes, the
  metrics, the checks and the falsifiers. None of it is ruled. Where a sentence states a ruling,
  the round is named. Everything else is Claude's, `UNVERIFIED — Emil review`.

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

---

## 0. The weakest point

**The owners are this projection's, not canon's.** Canon names no owner roles. The What, When and
How owners are a placement of responsibility argued from upstream core/05 §5 and mapped onto
method step 7 (complete accountability), which is itself `[PROPOSED]` and has nothing filed
beyond one line (see [`method/07`](../../method/07-complete-accountability.md)). If the
placement rule fails, the three owners fall with it. It fails when a boundary decision cannot be
split into one owner's act and another's ground (§3).

The second weakness is empirical. Nothing here has run. The forecast (§1), the option metrics
(§8) and the seam's price (§11) are computations over a record that does not exist yet. The SDLC
starts writing it from edition 1 (`DDD-dec-115`).

## 1. The stance: delivery does not decide when

*Ruled (Round 6, wording approved by Round 14):* "Delivery does not decide when. The How owner's
duty is to take approved work to production as fast as the quality constraints allow. The
cadence that results is the forecast everyone else plans against."

- **The How owner's duty.** The shortest lead time within the assurance the What owner set
  (§5). Assurance is not the How owner's to lower (Round 6: "What owner (Recommended)").
- **The forecast is computed, not promised.** An issue's expected delivery follows from two
  things:
  - its position in the When owner's order (the rank recorded at o2a);
  - the measured throughput, read from the SDLC's occurrence record (`DDD-dec-115` S-6).
- **The measures.** The measures are DORA's four keys, as
  [`production-as-ground.md`](../sdlc/production-as-ground.md) §2 reads them: deployment
  frequency, change lead time, change failure rate and failed-deployment recovery time.

**The computation, `[PROPOSED]`.**
- **Inputs.** Throughput λ is changes reaching o13 per week, over the last N weeks. Lead time L
  runs from o2b to o13, and its distribution comes from the record.
- **The estimate.** An issue at rank k, not yet allocated, has an expected landing date of about
  now + k/λ + median(L). A forecast is a distribution: resample λ and L from the record.
- **When it changes.** The forecast changes when the order changes (a When decision), when λ
  changes (the How owner's performance), or when assurance changes (a What decision that moves
  L). Nothing else moves it.
- **Delivery and landing.** Delivery is o16, which is the When owner's own act. The forecast is
  for landing, dark, and o16 can follow as soon as the ready-for-users verdict is in.

**This departs from how many organisations operate.** In many organisations the delivery process
is expected to move dates: a team is asked to "pull in" a feature, and the date becomes a target
the delivery side negotiates. Here the delivery side has nothing to negotiate. Its only lever is
lead time, and it is already obliged to minimise it. A date is held by changing the order (When),
or by cutting scope or assurance (both What). It is never held by pushing the How owner (§3, rule
1). Emil, Round 6: "many have the idea that delivery can have an impact on when something is
delivered. But its the how owners responsibility to have approved work go production as fast as
possible within the quality constraints."

## 2. The three owners

Each owner is a **scope under the product's genesis grant** (authority.md §2–3, `DDD-dec-87`,
`DDD-dec-85`): a grant held by one person, delegating from the genesis, accepted by its holder.
The genesis holder may hold any of the three.

| Owner | Owns | Acts it holds | Ruled by |
|---|---|---|---|
| **What owner** | The What: what the product must do, its acceptance relation and tolerance. The assurance locus. The mix between the software's share and the users' share of the product's acceptance | o1 for What- and assurance-locus issues, oR (ready for users), oU (holds the allocation of the acts of use) | Rounds 6, 7, 10 |
| **When owner** | The order of all proposed changes, and when each reaches users. It is the business, where demand enters, and the go-to-market owner | o2a (release for work: pull, decline, expire), o16 (turn a toggle on), a date promised outside (outside the arrangement) | Rounds 5, 10, 11 |
| **How owner** | The SDLC: the process of getting approved changes to production | o1 for How-locus issues, and every SDLC act, o1b to o13 ([`../sdlc/sdlc.md`](../sdlc/sdlc.md)) | Rounds 5, 8 |

**The When owner is the go-to-market owner** (Round 10). Relative importance is judged by when a
feature will have the best market impact. That is why ordering belongs to the When owner, and why
the When owner is also the biggest contributor to the option pool (Round 11).

**Ground.** *Ruled (Round 14):* "Their ground is their own to control, but the seams between them
supplies some to each". Each owner controls its own ground. Ground that crosses a seam is
supplied by its producer and is read-only for the receiver.

### 2.1 Round 14's seam table, checked against the act map

The prompt asks that every row be an output of one owner's act and appear in the ground reading
of another owner's act. The act map is [`graph/acts.ttl`](graph/acts.ttl) with
[`../sdlc/acts/acts.ttl`](../sdlc/acts/acts.ttl).

| From → To | Ground supplied | Produced by | Read by | Check |
|---|---|---|---|---|
| When → What | A pulled option (a need) | o2a (When) | o1 (dependency "the pulled option") | **Holds** |
| When → What | A scope-cut proposal | **No act** | The What owner's What-locus o1 | **Gap.** No act on the map produces it. It cannot be an option, because an option is never a What change (Round 11). It needs its own act: "propose a scope or assurance cut", held by the When owner and read by the What owner. Not added to the map; open item O-3 |
| What → When | Each element's outcome and acceptance | Earlier o1s (What) | o2a (`lc:readsEarlier m:o1`) | **Holds, after a fix.** The map first had o2a read only the record. Added in this session |
| What → When | The ready-for-users verdict | oR (What) | o16 (dependency) | **Holds** |
| What → How | The What, the assurance | o1 (What and assurance loci) | o1b (dependency), and o10 through the assurance level (`../sdlc/sdlc.md` §5) | **Holds** |
| When → How | A released issue, in order | o2a (the pull and its rank) | o2b (dependency "the release for work") | **Holds**, with finding F-2 below |
| How → When | The record: cadence, lead time, change failure rate | The dispatcher's occurrence records, o3 to o13 | o2a (`lc:readsEarlier m:o13`); the forecast | **Holds** |
| How → What | The change in production, dark, with its verdicts | o13, with o9 and o10's verdicts | oR (dependency) | **Holds** |

**Finding F-2: the order of o1 and o2a.** The act map Round 2 was ruled on has o1 (write the
issue) before o2a (release for work). Round 11's ruled reading has the When owner pull an option
at o2a, and the What owner then turn the pulled option into What decisions at o1. The map here
follows Round 11: o0 → o2a → o1 → o1b → o2b. The "released issue" that crosses the seam is
therefore o2a's pull together with o1's framing, and o2b reads both, through o1b. This is
Claude's reading, `UNVERIFIED — Emil review`.

**Falsifier: a piece of ground two owners both need to write.** Two candidates, both resolved
by splitting what each owner writes:
- **The issue thread.** o1 (the locus's owner) frames the issue. o1b (How) plans the realisation
  on it. o6 directs the session on it. Proposed: the issue body is the framing and is written
  only under o1's scope. The realisation plan is a separate section or comment, written under
  the How scope. A How-owner edit to the framing is refused (an extension, `../sdlc/sdlc.md`
  §11).
- **A toggle.** A toggle's existence and its default are the How owner's. Its on state is the
  When owner's. They are two pieces of ground. The falsifier fires only if one of them has to be
  written by both.

## 3. The placement rule

*Ruled (Round 10):* "Adopt it (Recommended)". Responsibility is placed **per decision, not per
role**. For each boundary decision exactly one owner holds the act, with control and liability.
Another owner's verdict enters it only as read-only ground.

**The argument, from upstream core/05 §5.**
- **Separable.** Accountability decomposes into answerability, liability and control, which
  "come apart in practice and must not be fused".
- **The failure mode.** "A party can be answerable and liable with no control — unfair, and
  ineffective; a party with control can shed liability through organisational design."
- **What the rule does.** Placing each boundary decision with one owner gives control and
  liability to the same party, decision by decision. The other owner's verdict is ground. It
  informs the act but does not share control of it, so it does not share liability either.

| Boundary decision | Act | Owner (control and liability) | Ground it reads (read-only) |
|---|---|---|---|
| What the product must do: acceptance and tolerance | o1, What locus | What owner | A pulled option (When) |
| Assurance, and the mix between software and users | o1, assurance locus | What owner | The stakes in the What; the record's change failure rate (How) |
| Ready for users | oR | What owner | The change in production, dark, with its verdicts (How) |
| The order of all proposed changes | o2a | When owner | The What elements and their declared acceptance (What); the cadence (How) |
| Turning a change on | o16 | When owner | The ready-for-users verdict (What) |
| A date promised outside | Outside the arrangement | When owner | The forecast, computed from the record (How) |
| Cutting scope to meet a date | o1, What locus | What owner | The When owner's proposal (When) |

**The three rules** (Round 10):
1. **The When owner may propose a What change but never make one.** A date is held by cutting
   scope or assurance, both the What owner's, or by changing the order, never by pushing the
   How owner.
2. **The What owner declares readiness but never picks the date.**
3. **A dispute escalates to the genesis grant holder.** Escalation "routes a determination to an
   accountability-bearing actor — not merely to a more capable one" (core/05 §5).

**Relative importance** (Round 10). The What owner declares each element's outcome and acceptance.
The When owner judges importance by when a feature will have the best market impact.

**Mapped to method step 7, `[PROPOSED]`.** Step 7's one filed line reads: "Attribution,
principal, authority, stake, remediation per allocation." For each row of the table above:
- **Attribution.** The act's record, signed under the owner's scope (authority.md §4.1).
- **Principal.** The holder of that scope.
- **Authority.** The scope grant, delegating from the genesis.
- **Stake.** The outcome the decision bears on: the product's acceptance for the What owner, its
  market impact for the When owner, lead time within assurance for the How owner.
- **Remediation.** Supersession by a later decision under the same scope, or escalation to the
  genesis holder.

Canon names no owner roles. This mapping is Claude's, and step 7 is unruled.

**Falsifier.** A boundary decision that cannot be split into one owner's act and another's
ground. It is then jointly owned, it belongs to the genesis grant holder, and the rule has failed
for that decision. A recurring class of such decisions would falsify the three-owner split.

## 4. The four loci

*Ruled (Round 4):* "Yes, four values (Recommended)". An issue declares its locus: the coordinate
of DDD-frame-01's tuple ⟨task, ground, acceptance relation, tolerance, arrangement, assurance⟩
that the change moves. *Ruled (Round 3):* it is declared on the issue, and the dispatcher refuses
an issue without one.

| Locus | Coordinates moved | Acceptance path |
|---|---|---|
| **What** | Acceptance relation, tolerance | The occupant drafts a decision anchored to the What element it changes. The What owner accepts it. Tools never change the What (`DDD-dec-42` O-5: every change of the What is made by a decision) |
| **Assurance** | Assurance | The What owner accepts it. It sets the depth of o10 inside the SDLC: the independence the acceptance needs, and what o9 must verify ([`../sdlc/sdlc.md`](../sdlc/sdlc.md) §5) |
| **Ground** | Ground | Each owner's own ground is controlled by that owner. A ground-locus issue declares whose ground it changes, and that owner accepts it. Ground crossing a seam is supplied by its producer and read-only for the receiver (Round 14) |
| **How** | Arrangement: How decisions and the code realising them, one locus (Round 3) | Handed to the SDLC (o1b onward), accepted at o10 by a holder of Approve for the How scope. A change to the SDLC arrangement itself is How one layer up ([`../sdlc/sdlc.md`](../sdlc/sdlc.md) §10) |

**Why planning is not a locus.** Planning moves no coordinate (Round 4). Time in canon is the
causal time index (`DDD-address-01`): B comes after A when a state change A produced is in B's
ground reading. So planning splits in two.
- **Derived order.** Order computed from dependencies is not a decision. The causal index gives
  it.
- **Chosen order.** Order chosen among causally independent occurrences is a decision, and it
  moves no coordinate. It is the When owner's, recorded at o2a as the pulled option's rank.

The coordinate **task** is not one of the four values. Claude's reading, `UNVERIFIED — Emil
review` (`DDD-dec-114` notes): the task is what the issue itself names, so a change of task is a
new option, not a locus of an existing issue.

## 5. Assurance, and the user-side share

*Ruled (Round 7, reading approved by Round 14):* the acts of using the product are occupied
partly by the software and partly by its users. The What owner can meet the product's acceptance
by allocating demand to either:
- **into the implementation**, which is the How owner's share;
- **into the users**, through training, guidance or procedure.

Only the What owner sees the whole demand. So the What owner sets assurance and chooses the mix,
and the How owner sees only the software's share.

On the act map this is **oU**, one address occupied by two kinds of actor: the software and the
user. The occupant is not part of the address (`DDD-ground-06`), so the address is the same
whoever occupies it, and the two shares can be compared at it. The user-side share now has an
address, and so has a place to record what was allocated to it (the ready-for-users verdict's
`lc:userSideShare`).

## 6. Priority is a When decision

*Ruled (Round 12):* "this also solves the classic problem of a product owner, owning the priority
which is inherently wrong. That's a when decision".

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
- **Two decisions in one role.** The classic product owner holds a What decision (what the
  product does: "Creating and clearly communicating Product Backlog items") and a When decision
  (ordering them) at once.
- **Ground they do not hold.** Priority is importance relative to the queue and to the market
  window. That is ground only the When owner, as go-to-market, holds (Round 10). A product owner
  who sets it judges from ground they do not hold.
- **Liability without control.** They are accountable for the market outcome of an order whose
  market ground is not theirs. That is the configuration core/05 §5 calls unfair and ineffective.

Here the What owner owns the items and the When owner owns their order.

**One person may hold both scopes.** *Ruled (Round 12):* "Yes, acts kept apart (Recommended)".
The split is between decisions, not people.
- **Each act under its own scope.** Each act is recorded under its own scope, so a When decision
  made by the person who is also the What owner is still visible as a When decision.
- **Review with no second party.** With no second party, a dispute has nobody to dispute it, so
  the genesis grant holder reviews.

**Falsifier.** An organisation where the same person holds both scopes and the record cannot tell
their When decisions from their What decisions. Then "acts kept apart" is not achievable in
practice, and the split is a split of people after all.

## 7. The pull system

*Ruled (Round 11, reading approved by Round 14):* the When owner is the business, and demand
enters the product there.
- **The pull.** The PDLC is a pull system: work moves only when the When owner pulls an option
  from the pool (o2a).
- **No push.** The SDLC never pushes. Its cadence flows back as the forecast (§1).

## 8. The option pool

**o0 propose an option.** Any owner may propose. The When owner is the biggest contributor. The
What owner proposes specification gaps and user feedback. The How owner proposes arrangement
changes and technical debt (Round 11).

**What an option is.** *Ruled (Round 11):* "Yes, outcomes only (Recommended)".
- **An outcome or need.** An option states who cannot do what, and by when it matters.
- **Never a What change.** The What owner turns a pulled option into What decisions at o1. This
  keeps the placement rule at the door: the business owns which needs, and when; the What owner
  owns what the product does.

**How an option leaves.** *Ruled (Round 11):* "Yes, recorded (Recommended)". Every option leaves
the pool by a recorded When-owner decision:

| Exit | Record |
|---|---|
| **Pulled** (o2a) | The issue it became, and its rank in the order |
| **Declined** | With a reason |
| **Expired** | When its market window passed, and not before |

An option sitting in the pool forever is a decision not to do it, made by nobody. So there is no
silent backlog, and option age and contributor share come from the record.

**The record shape (SHACL).** The shape is in [`graph/shapes.ttl`](graph/shapes.ttl) (`lc:OptionShape`,
`lc:ExitShape`, `lc:DeclinedShape`, `lc:PulledShape`, `lc:ExpiredShape`), and the terms are in
[`graph/ontology.ttl`](graph/ontology.ttl). An option carries:
- its contributor (`lc:contributor`: the What, When or How owner);
- the outcome stated (`lc:need`);
- its market window (`lc:mattersBy`, a date);
- when it was proposed (`lc:proposedAt`);
- at most one exit decision (`lc:exit`), which must be `lc:decidedBy lc:WhenOwner`.

An option that names a What element it changes (`lc:changesWhatElement`) is refused. An
expiry dated inside the window is refused. Run `python3 applications/pdlc/graph/check.py`.

**Metrics from the record.** All are computed from the options and their exits, none stored:

| Metric | Computation |
|---|---|
| Option age | For open options, now − `proposedAt`. For closed ones, `decidedAt` − `proposedAt` |
| Contributor share of proposed options | Options by `contributor` / all options |
| Contributor share of pulled options | Pulled options by `contributor` / all pulled options |
| Decline rate | Declined / closed |
| Expiry rate | Expired / closed. A high rate means the When owner is letting windows pass rather than deciding |

**Worked over the illustrative pool** ([`graph/example-pool.ttl`](graph/example-pool.ttl), which is
invented): five options; the When owner proposed three, the What owner one and the How owner
one. Two were pulled (one from the When owner, one from the What owner), one declined (How), one
expired (When), and one is open. The When owner's share is 3/5 of proposed and 1/2 of pulled.
The decline rate is 1/4 and the expiry rate 1/4.

**Falsifiers.**
- An option reaches o1 already phrased as a What change the What owner did not make.
- An option leaves the pool with no recorded decision.

## 9. The PDLC's acts on the act map

The act map is the form of method step 1: addresses on declared axes plus a layer path, a causal
time index, and the occupant kept out of the address. It is written as graph data in
[`graph/acts.ttl`](graph/acts.ttl), with the SDLC's acts in
[`../sdlc/acts/acts.ttl`](../sdlc/acts/acts.ttl): one map, validated together. The axes are the
SDLC's (Round 2, accepted for now), plus two surface values and one authority value the PDLC's
acts need: the option pool, the product in use, and an owner's scope grant. Those three values
are Claude's, `UNVERIFIED — Emil review`.

The stream, in causal order. Each line is a state change, and each act follows the acts whose
changes are in its ground reading. The SDLC's acts are summarised in one line.

```
o0   propose an option              → an option in the pool            any owner (mostly When)
o2a  release for work               → option pulled, with its rank     When owner   reads: o0; earlier o1s, earlier o13s (record)
o1   frame the issue, declare locus → an issue, framed                 locus owner  reads: o2a
     ── the SDLC, o1b … o13 (../sdlc/sdlc.md) ─────────────────────────────────────────────
     → the change in production, dark, with its verdicts               How owner    reads: o2a, o1
oR   ready for users                → a verdict over software + users  What owner   reads: o13
o16  turn the toggle on             → the toggle, on                   When owner   reads: oR
oU   use the product                → the acts of use                  software or user; held by What owner
```

The ids o14 and o15 are not reused (Round 2 retired o14; o15 was in the map Round 2 was ruled
on).

## 10. Release toggles, from the PDLC's side

*Ruled (Round 5):* "Release toggles (Recommended)". A change lands dark behind a toggle, which is
the How owner's process. *Ruled (Round 10):* "Yes, as a constraint (Recommended)".

- **Turning a toggle on (o16) is the When owner's act.**
- **o16 reads the What owner's ready-for-users verdict (oR).** The verdict covers the software's
  share and the user-side share.
- **The constraint.** Turning on an unready toggle is refused. In the shapes, `lc:ToggleOnShape`
  refuses an `lc:ToggleOn` with no `lc:readsVerdict` to an `lc:ReadyForUsers` for the same toggle
  with `lc:ready true`. Planted defects cover a missing verdict, an unready verdict, a verdict
  given by the When owner, and a toggle turned on by the What owner.
- **Creating and retiring a toggle are the How owner's**, inside the SDLC
  ([`../sdlc/sdlc.md`](../sdlc/sdlc.md) §7).

The ready-for-users verdict is computed, not stored (`DDD-dec-49`, `DDD-dec-52`). What is recorded
is the declaration it was computed from and the ground reading it read. This is Claude's
reading, `UNVERIFIED — Emil review` (`DDD-dec-114` notes).

## 11. The seam to the SDLC

*Ruled (Round 9, reading approved by Round 14):* the SDLC is a composite act within the PDLC.
Every SDLC occurrence's layer path begins PDLC ▸ SDLC, and the seam of Round 8 is the boundary of
that composite act. `lc:SdlcWithinPdlcShape` enforces the layer path.

| Direction | What crosses | Where |
|---|---|---|
| Into the SDLC | A released issue | o2a → o2b, framed at o1 (F-2) |
| Into the SDLC | The What | Read as ground, never written by the SDLC |
| Into the SDLC | The assurance | It sets o10's depth |
| Out of the SDLC | Production state, dark | o13 → oR → o16 |
| Out of the SDLC | The record | The occurrence record (`DDD-dec-115` S-6) |

**Nothing else crosses.** In particular, no calendar input enters the SDLC. The SDLC is never
told a date. It is given an order (the rank) and an assurance, and it returns a cadence.

**The seam's price** (upstream core/06, the seam-demand identity |D_comp| = |D_single| + |S|).
Splitting the product lifecycle into the PDLC and the SDLC manufactures seam demand S: the
decisions about how the two coordinate. They did not exist when one owner did everything. Paying
S down is one-time specification work:
- the issue's form (a declared locus and acceptance criteria in criterion form);
- the What as ground;
- the assurance levels;
- the record's shape.

Core/06: "skip it and S does not disappear, it escapes."

- **Mechanism at the seam, not actor.** No orchestrating actor stands at this seam. It is crossed
  by records: the issue, the What graph, the assurance, the occurrence record. Core/06 says what
  that buys: scale with no poisonable centre, paid for with rigidity. A situation the records do
  not anticipate escapes.
- **Where the escape shows.** It shows as late decisions supplied across the seam at human
  price, above all an o6 direction that supplies a What decision. That means the specification
  was incomplete upstream, in the PDLC ([`../sdlc/sdlc.md`](../sdlc/sdlc.md) §14).
- **The price, measured.** The share of o6 occurrences whose `lc:suppliedLocus` is What. Each is
  seam demand that the one-time specification did not pay and that a human paid per run. A
  falling share means the seam is getting cheaper.

## 12. Falsifiers

Each of these, if observed, falsifies part of this specification:

1. **A behaviour change that moves no coordinate.** An issue's change alters behaviour but moves
   no coordinate: the four loci do not cover it.
2. **A change that needs a "when".** A change that can only be stated with a "when" in it: then
   time is a coordinate after all, and planning is not outside.
3. **Forecast error out of band.** Forecast error beyond a band Emil sets. The band is not set:
   open item O-4.
4. **Lead time bought with assurance.** The How owner can shorten lead time by lowering assurance:
   the assurance ruling has a gap.
5. **Users reached before o16.** A landed change reaches users before o16: dark is not dark.
6. **An unrecorded user-side share.** A feature meets its software acceptance, is turned on, and
   fails its product acceptance for want of a user-side share that nothing recorded.
7. **A toggle turned on without a verdict.** A toggle is turned on without a ready-for-users
   verdict, and nothing refused it.
8. **A calendar input across the seam.** A calendar input has to cross the seam for the SDLC to
   work.

The falsifiers of §2.1 (ground two owners must write), §3 (a decision that cannot be split), §6
(When and What decisions indistinguishable in the record) and §8 (an option phrased as a What
change, an option leaving with no record) are part of this list.

## 13. Open items

| # | Item | Closes it |
|---|---|---|
| O-1 | Whether `applications/sdlc/` should one day nest under `applications/pdlc/`. That would be a supersession of `DDD-dec-42`'s placement, and it is not done here | Emil |
| O-2 | How `applications/organizations/` relates. `DDD-org-03` ("priority as a governed decision") is the nearest claim: it orders backlogs by decisions based on statused value-claims. Claude's reading, `UNVERIFIED — Emil review`: those are When decisions under this split, and the claim's falsifier is a measure of the When owner's order | Emil |
| O-3 | The scope-cut proposal has no act on the map (§2.1). Proposed: an act "propose a scope or assurance cut", held by the When owner and read by the What owner's o1 | Emil |
| O-4 | The forecast error band (§12, falsifier 3) | Emil |
| O-5 | F-2: o2a before o1 (§2.1) | Emil |
| O-6 | Record kinds for the When owner's acts (o2a, o16, an option's exit) in the authority profile, which today defines acceptances, grants, reviews and waivers | A successor session |
