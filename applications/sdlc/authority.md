# The authority profile — force over a product

**Status: written 2026-11-02 to the plan ruled in Round 1, with Appendix A ruled in Round 2 and
Q-11 and the fixtures' re-founding ruled in Round 3; not yet ratified (Emil merges #45).** This is the
profile the Decision Provenance Protocol leaves to its adopters (`dpp-1.md` §9.4). It says what
makes a decision in force in a product, who may make it so, and how that authority is founded,
delegated and transferred. The session is `meta/sessions/2026-11-02-authority-profile/`. The
charter's rulings are `DDD-dec-85`, Round 1's are `DDD-dec-86`, Round 2's are `DDD-dec-92`, and Round 3's are `DDD-dec-93`. Emil ratifies by merging.

**Register.** *Ruled* cites a decision. After Round 3 no `UNVERIFIED` mark remains and nothing is open. `UNVERIFIED — Emil review` marked a choice the writing had
to make that no ruling covers. Each such choice is also listed in Appendix A. Section numbers are
the ones `DDD-dec-86` cites.

**Companions.**
- The vocabulary is [`authority-vocabulary.md`](authority-vocabulary.md).
- The reference evaluator is [`authority/evaluate.py`](authority/evaluate.py).
- The property run is [`authority/properties.py`](authority/properties.py).
- The worked example is the acme shop product's authority history: [`how-examples/log/acme.json`](how-examples/log/acme.json) and its records, checked by
  [`how-examples/check.py`](how-examples/check.py) (§9).

**Who it binds.** Writ implements it. product-cli's draft log never claims it. A Context& package
is a product under it.

---

## 1. Scope

### 1.1 What this profile fixes

`dpp/1` fixes the record, the reference and the resolver, and defines no force. This profile adds
force for one kind of system: a **product**, the decision space someone brought into being.

- **In force at a position.** A decision is in force at a position of the product's log iff the
  conditions of §4.7 hold there. Nothing else confers force: no `status` value, no signature alone,
  and no reference from another system.
- **Authority.** Who may make a decision in force is a holder of a grant, founded at the genesis
  and delegated from it (§2, §3).
- **Identity and keys.** Who a holder is, and which keys sign for them (§5).
- **Time.** Every evaluation is a function of a positioned log and its header clocks (§6).

### 1.2 Not here

| Not here | Where it is |
|---|---|
| The record, the reference, the resolver, the hash law | `dpp/1` (`DDD-dec-62`) |
| What a How decision is, its kinds, anchoring, packages, import | [`how.md`](how.md) |
| What a What element is, its kinds, identity, What-versions | [`what.md`](what.md) |
| Verdicts, readings, the gate's verbs, positions as Writ writes them | Writ |
| The ratchet over code landings (a landing that shrinks a baseline) | Writ, G11. The profile states the rule (§4.3) and Writ enforces it |
| Attestations (`what.md` §3.2.3) | a successor item (Round 1, Q-10) |

### 1.3 Where the profile's fields live

*Ruled (Round 1, F-2):* "Anything a signature must cover (a grant's scope, a baseline, a waiver's
expiry, a key binding) is a top-level dotted member inside the canonical form, as how-vocabulary.md
does it. extensions is for what may change without a new version, and nothing authority-bearing
may."

- **One member.** Every field this profile defines is in the hashed dotted member
  `dk.decision-driven-design.authority`. Its `record` names the record kind (vocabulary §1).
- **Inside the hash and the signature.** It is in the canonical form, so it is pinned and it is
  signed (`dpp-1.md` §3.7, §11.3). It holds objects, arrays and strings only, so `"yes"` stands
  where a boolean would.
- **`extensions`.** A writer may put display aids there, such as a copy of a record's position for
  a reader without the log. No evaluation in this profile reads `extensions`.
- **`status`.** `dpp/1` lets `status` mean what the profile says (§3.4). Here it carries no force,
  and no evaluation reads it. Force is computed (§4.7).

### 1.4 The rulings this rests on

| Ruling | Decision |
|---|---|
| The genesis grant: definition, space, transfer, home | `DDD-dec-46`, restated by `DDD-dec-85` |
| "Signed": signature, acceptor and time, required for force | `DDD-dec-47`, read by Round 1, F-1 |
| Force comes from this profile: genesis, grants, scopes, acceptance, baseline, waiver | `DDD-dec-54` ruling 4 |
| Scopes over ontology classes; the multi-scope rule | `DDD-dec-64` P-7, Round 5 of the move |
| The charter's eight rulings | `DDD-dec-85` |
| F-1 to F-3, Q-1 to Q-10 | `DDD-dec-86` |

---

## 2. The genesis grant

### 2.1 Definition

*Ruled, verbatim (2026-10-27, `DDD-dec-46`):*

> The genesis grant is the root of change authority over one product. It is held by the human
> principal who brought the product into being. It is unscoped within the product and scoped to
> nothing outside it, and it is the only grant that delegates from no other. Every other grant
> over the product delegates from it, directly or through a chain; every decision that changes
> the product resolves, through its acceptance and the grant that acceptance was made under, to
> the genesis. A product with no genesis grant has no authority, and nothing in it is in force.

A product is the decision space. Its What and its realisation are scopes within it, under one
genesis. A package is a product with an empty What and its own genesis. In another product it is
provenance, never authority (`DDD-dec-85`).

### 2.2 Founding

*Ruled (Round 1, Q-1): the genesis is founded, not accepted.*

- **The founding record** is a `genesis` record. Its `by` and `holder` are the founder, and it
  names the product IRI P (`DDD-dec-63` §1). Its `basedOn` is empty, so it delegates from nothing.
- **Self-bound key.** It carries `firstKey`, and it is signed by that key. The founding is
  therefore also the holder's first key binding (§5.3; the ledger's D7, as it fits).
- **No acceptance.** A separate acceptance would be the same person's signature twice over the
  same content.
- **One per product.** A second founding in the same log is refused. The genesis's `id` names the
  genesis decision for the life of the product.

### 2.3 Transfer

*Ruled (`DDD-dec-46`; Round 1, Q-1, Q-2).* A transfer is a decision, never an edit.

1. **The holder signs.** The holder signs a new version of the genesis decision. It supersedes the
   version in force and names the successor as `holder`. If the successor has no key in the
   product, it also carries the successor's `firstKey`, so the transferring holder vouches for it.
2. **The successor accepts.** The successor signs a grant acceptance of that version (§3.3).
   Until then the transfer is pending, and the prior holder still holds.
3. **The prior grant closes.** On the successor's acceptance, the prior holder's genesis is closed,
   not deleted. *Ruled (Q-2): closing is not a revocation.* Every grant delegates from the genesis
   decision's `id`, not from a holder's version, so nothing delegated from the genesis falls at a
   transfer.
4. **Only the holder transfers.** A fallback may not transfer (§2.4).

### 2.4 Unavailability and fallback

*Ruled (`DDD-dec-46`):* "Holder unavailability is filed unavailability with a fallback holder, who
may act and may not transfer."

- **A fallback is a grant.** It carries `fallbackOf` naming its primary. It is granted by the
  primary's holder and delegates from the primary. Its scope is the primary's at every position,
  so it carries none of its own. Like any grant, it is live only from its holder's acceptance
  (§3.3). *Ruled (Round 2, A-6):* "any grant may have a fallback, and a fallback delegates from
  its primary".
- **Unavailability.** It is a signed record naming the grant, with `from` and an optional `until`,
  both header-clock times (§6.2). The holder files it, or a holder above them in the chain does.
  The holder ends it early with an availability record.
- **When a fallback may act.** Only while its primary is unavailable at the header clock of the
  act's position. It may then do whatever the primary may: accept, review, waive, delegate if the
  primary may.
- **What a fallback may not do.** It may not transfer the genesis.
- **The primary while unavailable.** A primary filed unavailable does not act. Its grant stays live,
  and so do its delegates.

### 2.5 Loss

*Ruled (`DDD-dec-46`):* "Loss of the holder with no fallback cannot be repaired from inside: a new
genesis founds a new product, and the old product's decisions are imported by basedOn, which keeps
provenance and records that authority was re-founded."

**Key loss is not holder loss.** *Ruled (Round 3, Q-11):* "A genesis holder who loses a key still
holds the genesis. What is needed is a new key binding, and the one party the holder pre-authorised
is the fallback." A-9 for the genesis reads: "by a new key binding vouched by a fallback; absent any
fallback, by the new-product path". Round 2's "by transfer" is withdrawn.

- **The vouch.** The holder of a live fallback of the genesis signs a `key-binding` with
  `act: "vouch"`, naming the genesis holder and the new key, under their fallback grant (`under`).
  It is the same vouching a grantor gives a new holder's first key (§5.3), applied upward, because
  the genesis has no grantor. It does not wait for the holder to be filed unavailable: the holder
  is present and keyless, not absent.
- **The binding.** The genesis holder signs a `key-binding` with `act: "add"`, signed by the new
  key itself. It names and pins the vouch, and may close the lost keys (`closes`). The key is live
  from that position.
- **No transfer.** The fallback still may not transfer.
- **No path.** Only when the holder and every fallback have lost their keys is there no path. That
  is the ruled new-product case above.

### 2.6 Adopting the profile

A product whose records predate any positioned log adopts the profile by founding its log. The
founding is that log's first position. Earlier records are held as `dpp/1` records and carry
provenance. They confer no force until they are landed in the log and accepted under it. The acme
shop example does this (§9). Its stand-ins were signed by keys that no longer exist, so its
founding names the same holder and P under a new key, superseding the stand-in genesis for
provenance.

**Test fixtures, re-founded once.** *Ruled (Round 2, A-5; widened in Round 3, P-9):*
- **The once.** Every test product in this repository whose stand-in records were signed by
  discarded keys is re-founded once. The founding is under a key kept with the fixture, with the
  same holder and the same product IRI. Its record states that it is a test-fixture re-founding,
  not a transfer.
- **Which they were.** acme shop by `GEN@3`, and the vendor package by `GEN@2`. These are the last
  re-foundings.
- **The next test product** is founded under kept test keys from the start and needs no ruling.
- **Why it holds.** It is acceptable only because the keys are now kept for each fixture's life
  (§9), which ends the cause. Outside test fixtures there is no re-founding: a real founder keeps
  their key, and loss is §2.5.

---

## 3. Grants

### 3.1 Scope

*Ruled (`DDD-dec-85`; `DDD-dec-64` P-7).* A **scope** is a set of ontology classes, optionally
narrowed to one element's `sdlc:within*` subtree.

- **The record.** `scope` is `{classes, within?, withinPath?}`. `classes` is a non-empty list of
  class names (`sdlc:Field`, `sdlc:Binding`). `within` is an element IRI. `withinPath` is that
  element's `within*` chain up to the product node, read from the graph when the grant is signed.
- **Derived kinds are in no scope.** A grant naming one is refused. In sdlc edition 1 the derived
  element kind is `sdlc:Journey` ("a product-level, derived composition", `what/ontology.ttl`).
- **The genesis is unscoped.** It covers every class and every element in the product.
- **What a scope may name.**
  - What element kinds: every class within `sdlc:WhatElement`.
  - The How's decision and record classes: `sdlc:Constraint`, `sdlc:Binding`, `sdlc:Contract`,
    `sdlc:TargetDeclaration`, `sdlc:Exclusion`, `sdlc:Import`, `sdlc:Retention`.
  - The code the How governs: `sdlc:Component`, `sdlc:CodeElement`.
- **Grants choose.** A grant need not name everything, and what it leaves out is the grantor's
  choice. The acme What grant leaves out the product node, so changes to it are the genesis's (§9).

### 3.2 Delegation

*Ruled (Round 1, Q-8):* "A grant delegates only if it says so, and only a subset of its own scope."

- **A grant is a decision of its grantor.** Its `by` acts under the grant named as `parent`, which
  they hold, live and available. The grant pins that parent's version in `basedOn`, and is signed
  by a key bound to the grantor (§5.3).
- **Only if it says so.** The parent must carry `mayDelegate: "yes"`. The genesis always may. A
  fallback delegates exactly as its primary may.
- **Only a subset.** The new scope's classes are a subset of the parent's effective classes.
  If the parent's scope has a subtree, the new scope has one inside it: the parent's `within`
  appears in the new `withinPath`. This is checked when the grant is signed, and the result is
  fixed (scope at signing).
- **Effective scope.** At any position it is the intersection along the chain live there, with the
  innermost subtree.
- **Self-grants.** A holder does not grant to themself.
- **Grants to machines.** A grant to an identity named a machine is refused (§5.1).

### 3.3 Grant acceptance

*Ruled (Round 1, Q-1):* a grant is live only from its grantee's signed acceptance. Authority is
never imposed.

- **The record.** A `grant-acceptance` names and pins the grant version. Its `by` is the grantee.
- **Its key.** If the grantee has no key in the product, it is signed by the `firstKey` the grant
  vouched for, and that key opens for the grantee at this position (§5.3). Otherwise it is signed
  by a key of theirs already bound.
- **The same rule covers** a transfer's new genesis (§2.3) and a fallback grant (§2.4).

### 3.4 Supersession of a grant

- **A new version.** A grant is changed by a new version of the same `id`, signed by the same
  grantor under the same parent, superseding the live version. It is live from the grantee's
  acceptance of it. Until then the earlier version stays live.
- **Its delegates.** Delegates keep delegating from the grant's `id`. A narrowed grant narrows its
  chain from that position, through the intersection rule (§3.2), and revokes nothing.

### 3.5 Revocation

*Ruled (Round 1, Q-2).*

- **Who.** A grant is revoked by a `revocation` record from its grantor, or from any holder above
  it in the chain, made under that holder's grant (`under`). The genesis is never revoked. It is
  transferred (§2.3).
- **From when.** From the revocation's position, nothing may be done under the grant: no
  acceptance, review, waiver or grant.
- **The chain below falls.** Every grant delegating from it, directly or through a chain, is not
  live from the same position.
- **What stands.** Acts made under the grant before the revocation stay valid. Each was valid at its
  own position (G2, "a grant live at its own position"). The decisions they put in force stay in
  force. Nothing re-parents silently: a holder above re-grants if a delegate should keep authority.

---

## 4. Acceptance of decisions

### 4.1 The acceptance record

*Ruled (`DDD-dec-47`; Round 1, F-1):* "An acceptance is its own signed record whose by and at are
the acceptor and the time, and which pins the decision's version hash."

An `acceptance` record:

- **Who.** Its `by` is the acceptor, and its `at` is when they accepted. These are Draft 3's
  `acceptedBy` and `acceptedAt`, which `dpp-1.md` A-10 removed as fields.
- **What.** It names the decisions it accepts (`accepts`) and pins each in `basedOn`. Its
  `signature` covers its canonical form, so it covers each pin, so it covers the accepted
  version's hash.
- **Under what.** It names and pins the grant version it is made under (`grant`). That grant is
  held by `by`, live and available at the acceptance's position. A fallback acceptance names the
  fallback grant (§2.4).
- **Signed.** It is signed by a key bound to `by` at that position (§5.3).
- **By a human.** It does not carry `attributedTo`, and its `by` is not named a machine (§5.1).
- **Of local decisions.** Every decision it accepts is landed in this log, in this system. A
  reference to another system's record is provenance and is never accepted (§4.7).

### 4.2 What a decision touches, and the multi-scope rule

- **Scope at signing.** *Ruled (`DDD-dec-85`):* "Scope is evaluated at signing and the result
  recorded; a later change to the graph does not re-evaluate it."
- **What an acceptance records.** For each decision it accepts, it records in `touches` the items
  that decision touches. Each item is `{class, element, path}`: the class, the element, and the
  element's `within*` path as the graph had it at signing.
- **What a decision touches.** *Ruled (Round 2, A-11):* "'touches' means every element the
  decision creates, changes or retires, per the scope wording" (what.md §5.1). It is ruled as
  proposed, and is read so that a How decision is the one element it creates:
  - a What change touches each element it creates, changes or retires, with that element's kind;
  - a How decision touches the class of its kind (`sdlc:Constraint`, `sdlc:Binding`,
    `sdlc:Contract`) at its anchor;
  - a target declaration, exclusion, import or retention touches its record class at its anchor;
  - a decision may touch several, as `CUR@1` does (§9).
- **Covering.** A grant covers an item if the item's class is in its effective classes, the class
  is not derived, and the grant's subtree, if any, is on the item's path. An acceptance covers the
  items its grant covers, and covers at least one, or it is refused.
- **The multi-scope rule.** *Ruled (`DDD-dec-64` P-7; `DDD-dec-85`):* "a decision touching kinds in
  more than one scope needs a valid acceptance under each, from the same or different holders, in
  force only when all are live." Here: a decision's items must all be covered by live acceptances,
  together. Acceptances of one decision must record the same items. A later one that records
  different items is refused.

### 4.3 Baselines

*Ruled (`DDD-dec-85`):* "Baseline on an acceptance; landings only shrink it; only a fresh
acceptance grows it."

- **The entries.** A `baseline` is a list of entries on an acceptance. Each entry is
  `{decision, subject, target}`: the decision accepted, the element violating it, and the target.
  This is `how.md` D-6's (decision, element, target).
- **Under the signature.** The baseline is signed with the acceptance.
- **Only by acceptance.** Only an acceptance carries one. Only a fresh acceptance of the decision
  grows it.
- **Landings shrink it.** A landing that removes a baselined violation records the smaller baseline
  at its position, without a signature (Writ `[D2]`; G11).
- **What it marks.** A baseline entry marks debt. A boundary is an exclusion decision, never a
  baseline entry (`how.md` §8.2).

### 4.4 Waivers

*Ruled (`DDD-dec-85`):* "a signed, expiring answer to an open question that changes no decision."

- **The record.** A `waiver` names the question: `{decision, target, provenance}`, an open question
  in Writ's sense (`how.md` §9.3). It carries the grant it is made under, `expires` and `touches`.
- **Who may waive.** It is signed under a grant that could accept the decision (§4.2), by a human
  (§5.1).
- **When it expires.** *Ruled (Round 1, Q-6):* "expiry is a header-clock time, and Writ follows."
  A waiver is live at a position iff that position's header clock is before `expires`. It must
  expire after the clock of the position it lands at.
- **What it changes.** No decision, and nothing in force. The gate reports the question as waived
  while the waiver is live, and open after.
- **What it never covers.** A violation, or a coverage gap (`how.md` §8.2).

### 4.5 Reviews

*Ruled (Round 1, Q-4).*

- **What it is.** A `review` is a rejection (`"reject"`) or a request for change
  (`"request-change"`) of a landed decision version, which it pins.
- **Who may review.** It is signed under a grant that could have accepted that version at that
  position (the same covering rule), by a human.
- **What it does.** It has no force, stays in the log, and does not block a later acceptance. A
  signed comment by anyone else is not a review under this profile.

### 4.6 Revoking an acceptance

*Ruled (Round 1, Q-2):* "an acceptance may be revoked." An `acceptance-revocation`:

- **Who.** It is signed by the acceptance's own signer, or by a holder of a grant above the grant
  the acceptance was made under (`under`).
- **Its effect.** From its position the acceptance is not live, so a decision that needed it is not
  in force. The acceptance stays in the log.
- **Not supersession.** Supersession replaces a decision. Revocation withdraws an acceptance and
  leaves the decision unaccepted.

### 4.7 In force

A decision D is **in force at position p** iff:

1. it is landed in the product's log at or before p;
2. every item its acceptances record (§4.2) is covered by acceptances of D that are valid at their
   own positions, at or before p, and not revoked by p, and none of them is reported as needing
   re-acceptance by p (§5.1, §5.3);
3. no decision in force at p supersedes it.

**Force is local.** *Ruled (`DDD-dec-85`):* "Force is local; `basedOn` carries provenance only."
- **Other systems.** A record in another system, a package's included, is never in force here.
- **Imports.** A decision here that rests on one is in force only under acceptances here. An
  import is that (`how.md` §7).
- **Signatures elsewhere.** A signature in another system confers nothing here.

---

## 5. Identities and keys

### 5.1 Human, machine, attribution

*Ruled (`DDD-dec-85`; Round 1, Q-5).*

- **Machine.** A machine identity is one named by a signed `attribution` record: identity M is
  software, and human H is responsible for it.
  - Any holder of a live grant may file one.
  - M is a machine from that position, in this product, for good. No record un-names a machine.
  - Grants held by M are not live from that position.
  - Acceptances M signed before it was named stand at their positions. From the naming they are
    reported as needing re-acceptance, and do not count for force.
- **`attributedTo`.** A record carrying `attributedTo` is never an act of authority. It is refused
  and recorded as an acceptance, review, grant, waiver, key binding, or any other record of §1 of
  the vocabulary. This holds whoever its `by` is. No configuration makes it otherwise.
- **Recorded.** A refused attempt is recorded in the header of the position it was attempted at,
  with its reason (§6.1).
- **Human.** An identity in the protocol's scheme that no attribution names as a machine.
- **A grant is an attestation.** A grant to an identity is the grantor's attestation that it is one
  person.
- **Weakest point.** No protocol can prove that a key is held by a person. The profile makes the
  claim attributable, with the grantor accountable for it, and makes a later attribution decisive.
  It does not make the claim true.

### 5.2 Teams

*Ruled (Round 1, Q-5).* A team identity (a list, a group mailbox, a role account) is not a holder.
A holder is one person. A team is expressed as several grants.

### 5.3 Keys

*Ruled (Round 1, Q-3).*

**Bindings.**
- **Per product.** Keys are bound per product, and nothing in one product's key bindings has effect
  in another.
- **One holder.** A key belongs to one holder in a product, ever.
- **Several keys.** A holder may have several keys live.
- **Verification.** An act is verified against the binding live at the act's position. Rotation
  never invalidates history.

**The first key.**
- **The genesis holder's** is self-bound in the founding (§2.2).
- **Every other holder's** is vouched for by their grantor, as `firstKey` in the grant. It opens at
  the grantee's acceptance, which it signs (§3.3).
- **A transfer** vouches for the successor's the same way (§2.3).

**The `key-binding` record.** It has three acts, and a fourth for the genesis alone (§2.5):
- **`add`.** It binds a further key. It is signed by a live key of the holder. If the holder has no
  live key, a holder above them in the chain binds it, under their grant (ruled, Round 2, A-9;
  for the genesis, §2.5).
- **`rotate`.** It binds a new key and closes an old one at the same position. It is signed by the
  key it closes.
- **`close`.** It is signed by the holder, or by a holder above them, under their grant. A closed
  key never signs again in the product, and is never bound again.
- **`vouch`.** Only for the genesis holder, by the holder of a live fallback of the genesis,
  naming the holder and the new key. It opens nothing. The holder's `add` that pins it, signed by
  the new key, opens it (§2.5; Round 3, Q-11).

**Compromise: `since`.** A `close` may carry `since`, a position at or before its own.
- **What stands.** Acceptances signed by that key from `since` stay valid at their positions, so
  replay holds (G6).
- **What changes.** From the close's position they are reported as needing re-acceptance, and stop
  counting for force until another acceptance covers the decision.
- **Nothing is rewritten.**

**Order within a position.** The records a header lists are judged in that order (§6.1). An act
listed before a close in the same position was signed while the key was live.

---

## 6. Positions and clocks

### 6.1 The positioned log

*Ruled (Round 1, Q-6).* The profile requires a positioned log. Each header carries:

- `position`, consecutive from `"1"`;
- `clock`, the writer's clock, an RFC 3339 UTC time;
- `previous`, the hash of the previous header (absent on the first);
- `records`: each record landed at this position, as `{ref, hash}`, in the order judged;
- `refused`: each attempt refused here, as `{ref, hash, reason}`;
- `hash`, the hash law of `dpp-1.md` §5 over the header without `hash`.

The header hash covers the clock, the previous header and every pin. That is the
provenance-conformant log of Writ `[D2.5]` ("whose header carries the writer's clock and is
covered by the header hash"), with the profile's records in it.

### 6.2 Clocks

*Ruled (Round 1, Q-6, F-3).*

- **Header clocks only.** Every time-dependent evaluation reads the header clock of the position
  being evaluated, never a process clock: grant liveness, unavailability windows, key validity,
  waiver expiry, session leases.
- **A record's own `at`** is its author's claim (`dpp-1.md` §11.4). It is never read for force. An
  act of authority whose `at` differs from its header's clock is refused (ruled, Round 2, A-8). The
  comparison is at the precision `at` carries: a date-only `at` must be the clock's date, and an
  `at` with a time must be the clock.
- **`[D2.11]`, as Emil states it (Round 1, F-3):**
  - Header clocks are monotone by the writer's clamp: ts = max(clock, head). A backwards
    wall-clock step yields equal timestamps, never a refusal. The evaluator therefore accepts equal
    clocks and refuses only a clock that steps back.
  - As-recorded replay is a fixture import through a writer whose injected clock returns each
    recorded timestamp in turn, never a re-stamped log.
  - G6 is re-evaluation of the recorded log, served as-of.
  - The stamped instant is the staging instant under group commit.
- **Why a time and not a position.** "A position does not advance on a quiet product, so a
  position-based expiry never fires exactly where a waiver most needs to; a header-clock time is
  deterministic because the clock is in the log ([D2.3])." Writ's definition is amended to match
  (Emil's act).

### 6.3 Systems without positions

A system without a positioned log cannot claim this profile. It can claim `dpp/1` conformance.
With a positioned log and no authority records, it can also claim Writ's *provenance-conformant*
class. product-cli's draft log is that, and never more (charter).

---

## 7. The violation-description field

*Ruled (Round 1, Q-10; `DDD-dec-52`).* The profile covers the violation description, the field
`DDD-dec-52` names on a decision.

- **Where it lives.** `dk.decision-driven-design.authority.violation` is
  `{language, binds, text}`.
- **Its form.** `language` is `"sparql-1.1-select"`. `text` returns one row per violation
  (`?subject`, `?reason`). `binds` lists the variables the evaluator binds (`anchor`, `target`)
  (`how-vocabulary.md`).
- **It confers no force.** A decision is in force or not by §4.7, whatever its violation
  description finds.
- **What it is for.** It is the declaration that makes a verdict computable. The verdict is
  computed, never stored (`DDD-dec-52`).
- **No description.** A decision without one is allowed, and is idle where nothing rests on it
  (`how.md` §4.3).

---

## 8. Conformance

### 8.1 One class

*Ruled (Round 1, Q-7).*
- **The class.** One class, **authority-conformant**, the name Writ `[D2.5]` uses.
- **Who claims it.** A positioned log (§6) whose records follow §2 to §5, and whose
  implementation satisfies the property list (§8.2) over generated histories.
- **The claim.** It names this profile and the suite it ran.
- **Writ's suite is its first implementation** (G2, G3).

### 8.2 The property list

Each property is a predicate over a history: acts at positions with header clocks, and the
evaluation of that history.

| # | Property | Mirrors |
|---|---|---|
| A1 | A decision is in force at p only if every item it touches is covered by acceptances valid at their own positions, at or before p, not revoked, not needing re-acceptance, each signed by a human holder under a grant live at its position | G2; the multi-scope rule |
| A2 | No identity named a machine, and no record carrying `attributedTo`, produces a valid act of authority. Every such attempt is judged, and so recorded | G3 |
| A3 | Every live grant's chain runs through live grants to the product's one genesis, and every delegated scope is within its grantor's | genesis definition; Q-8 |
| A4 | No grant other than the genesis is live before a valid acceptance of it by its grantee | Q-1 |
| A5 | After a grant's revocation at r, neither it nor any grant below it is live at any p ≥ r, and no act under them after r is valid | Q-2 |
| A6 | A transfer's completion changes no grant's liveness | Q-2 |
| A7 | An acceptance's recorded scope result never changes after its position | scope at signing |
| A8 | Every valid act is signed by a key bound to its signer, and no key signs after its close | Q-3 |
| A9 | A baseline is carried only by a valid acceptance, on a decision it accepts. That landings only shrink it is Writ's G11 over code, and is not checked here | the baseline ruling |
| A10 | Waivers change nothing in force, and a waiver is live only before its expiry by header clock | the waiver ruling; Q-6 |
| A11 | A fallback acts only while its primary is filed unavailable at the act, and never transfers | `DDD-dec-46` |
| A12 | Evaluating the same log again, or a prefix of it as-of, gives the same judgements and the same state at every position | G1, G6 |
| A13 | An acceptance of a record in another system is never valid | force is local |

### 8.3 The reference evaluator and the property run

[`authority/evaluate.py`](authority/evaluate.py) is §2 to §6 as code, in the standard library only.
[`authority/properties.py`](authority/properties.py) generates seeded histories and checks A1 to
A13 against it:

- **The histories.** 1,000 of them. Four in five are random acts, many of them deliberately wrong.
  One in five is scripted with random timing to reach fallbacks, transfers, a revoked middle grant
  and a late machine naming.
- **The output.** It prints how many acts of each kind were valid and how many were refused. It
  fails if a kind is never valid.
- **Mutations.** Eight mutations of the evaluator were run by hand on 2026-11-02, each removing
  one rule. Each was caught by the property it targets:
  - the `attributedTo` refusal (A2);
  - the machine refusal (A2);
  - chain liveness (A3, A5);
  - waiver expiry (A10);
  - acceptance revocation (A1);
  - the subset rule (A3);
  - key binding (A8);
  - the local-system rule (A13).

**Not Writ's suite.** It shows that the list is consistent and executable against one evaluator.
It does not show that any other implementation holds it, or that the generator reaches every
case.

---

## 9. The worked example: acme shop, under the profile

The How examples' test product, extended (Round 1, Q-9). Records are added, never edited. The log
is [`how-examples/log/acme.json`](how-examples/log/acme.json): 16 positions, hand-built, with no
writer behind it. Every key is a throwaway test key.

| p | Header clock | Landed | What it shows |
|---|---|---|---|
| 1 | 2026-11-02 09:00 | `GEN@3`, `ATTR-agent@1` | the founding, self-bound (§2.2, §2.6); the proposing agent named a machine (§5.1) |
| 2 | 09:10 | the founding What decision and the six How records the stand-ins had accepted; `GRANT-what@2` (every authored What kind), `GRANT-how@3` (How and code, may delegate) | two delegated scopes, each vouching for its grantee's first key |
| 3 | 09:20 | `GACC-what@1`, `GACC-how@1` | grants live only from acceptance (§3.3) |
| 4 | 09:30 | `ACC-what@2`; `ACC-1@3` with a five-entry baseline. **Refused:** `ACC-agent@1` | re-acceptance under the profile; baseline (§4.3); a machine's acceptance refused and recorded |
| 5 | 10:00 | `CUR@1`; `ACC-cur-what@1` (owner) | `CUR@1` creates the field `currency` and changes Place order (What kinds), and binds it (a How kind). Accepted under one scope only, it is **not** in force |
| 6 | 10:30 | `ACC-cur-how@1` (architect); `what@4` | accepted under both scopes by two holders: in force (§4.2); `what@4` names the new graph |
| 7–9 | 11:00–11:20 | `GRANT-lead@1` (bindings within Ordering), its acceptance, `GRANT-ctr@1` (bindings within Place order), its acceptance, `CURFMT@1` | delegation two levels down, each a subset (§3.2) |
| 10 | 11:30 | `ACC-curfmt@1` (contractor) | an acceptance deep in the chain |
| 11 | 2026-11-03 09:00 | `REVK-lead@1` | the lead's grant revoked; the contractor's falls with it; `CURFMT@1` stays in force (§3.5) |
| 12 | 09:30 | `CURFMT@2` (the agent's proposal). **Refused:** `ACC-curfmt@2` | an act under a fallen chain, refused and recorded |
| 13 | 2026-11-04 09:00 | `KEY-architect@1` | rotation: `ACC-1@3`, signed at p4 by the closed key, still verifies (§5.3) |
| 14 | 09:30 | `WAIV-resid@1`, expiring 2026-11-11T00:00Z | a waiver on the open question `RESID`, azure, `deployment-observed`: live here |
| 15 | 2026-11-12 09:00 | `REV-curfmt@1` | a review with no force (§4.5); the waiver has expired by header clock, and the question is open again |
| 16 | 2026-11-13 09:00 | `SCN@1`; `ACC-scn-what@1` (owner); `what@5` | added for sdlc edition 1 (`DDD-dec-113`, E-5): a What change touching only What kinds, in force on one acceptance; `what@5` names the new graph and the completed edition |

**What `how-examples/check.py` verifies against the What graph** (rdflib):

- every recorded scope item's class and `within*` path, 66 items;
- every grant's subtree path;
- that `CUR@1`'s delta is exactly what@3's graph before and what@4's after: one element created,
  one changed, nothing retired;
- that `SCN@1`'s delta is exactly what@4's graph before and what@5's after: one element created,
  four changed, nothing retired;
- that every violation the verdicts report is in `ACC-1@3`'s baseline;
- that the waived question is an open question.

**What it shows, and what it does not.** It shows the profile's rules executing as written over
one hand-built history, with each outcome predicted before the run. It does not show that the
profile is right, or that any real log implements it.

- **The verdicts' date.** They are computed as of the readings (2026-10-28). A gate evaluating at
  p15's clock would find every reading older than `RESID`'s P1D, and would report every `RESID`
  verdict as an open question. The checker says so.
- **The keys.** *Ruled (Round 2, P-6):* "keep the test keys for the fixture's life".
  - They are in [`how-examples/test-keys/`](how-examples/test-keys/), declared there as the test
    holders' test keys, never used outside the fixture.
  - They are rotated only by a new founding that says so in its record.
  - The 25 records of 2026-11-02 were rebuilt once, before ratification, so that their keys are
    these (session `rulings.md`, Round 2).
  - The vendor package's re-founding key, `vendor-holder-p`, is kept there too (Round 3, P-9).

---

## Appendix A — Decisions: every departure from the charter's proposal

The charter's answers, and Round 1's rulings on them, are `DDD-dec-86`. A ruled departure is
listed with its ruling. Round 2 (`DDD-dec-92`) ruled every reading Round 1 left open, all as
proposed. Round 3 (`DDD-dec-93`) replaced A-9's genesis clause (Q-11) and widened A-5 (P-9).

| # | The proposal said | This profile says | Reason | State |
|---|---|---|---|---|
| A-1 | what the protocol does not define goes in `extensions` | every authority field is in the hashed dotted member | `extensions` is outside the pin and the signature (`dpp-1.md` §3.7, §11.3) | ruled, F-2 |
| A-2 | `acceptedBy` and `acceptedAt` are required | they are the acceptance record's `by` and `at` | `dpp-1.md` A-10 removed them as fields | ruled, F-1 |
| A-3 | revocation of a grant, its chain falling | also: the close at a transfer is not a revocation, a grant's supersession is not one, and an acceptance may be revoked | without the first, every transfer voids every grant | ruled, Q-2 |
| A-4 | keys per namespace; D7 where it fits | namespace is the product; the grantor vouches for the first key; `since` on a close | under delegation D7 would have the genesis holder vouch for people they never granted | ruled, Q-3 |
| A-5 | (not raised) | each test product is re-founded once under a kept key, with the same holder and IRI, as a test-fixture re-founding: acme by `GEN@3`, the vendor by `GEN@2`; the next test product needs no ruling | the stand-ins' keys were discarded after their builds, so no act under them can be signed. In a real product the founder keeps their key | ruled, Round 2; widened to every test product in Round 3 (P-9) |
| A-6 | fallback for the genesis | any grant may have a fallback, granted by its primary's holder and delegating from the primary, with the primary's scope; it may do what the primary may, delegation included, except transfer | "may act" read as everything its primary may; one rule for every grant | ruled, Round 2 |
| A-7 | (not raised) | records a header lists are judged in that order | several acts at one position (a close and an act signed by the closing key) need an order. The header's order is in the hash | ruled, Round 2 |
| A-8 | (not raised) | an act of authority whose `at` differs from its header's clock is refused | `at` is never read for force, but a record that disagrees with its own position is not an act anyone should rely on | ruled, Round 2: "an act whose at differs from its header's clock is refused" |
| A-9 | (not raised) | a holder with no live key gets one bound by a holder above. For the genesis, "by a new key binding vouched by a fallback; absent any fallback, by the new-product path" (§2.5) | the first-key rule, applied again; the genesis has no one above | ruled, Round 2; the genesis clause ruled in Round 3 (Q-11), "by transfer" withdrawn |
| A-10 | a machine is any identity with an `attributedTo` | a machine is named by an attribution record; `attributedTo` refuses, it does not classify | `attributedTo` is a record member, not an identity property | ruled, Q-5 |
| A-11 | (not raised) | what a decision touches (§4.2): a What change, its elements' kinds; a How decision, its kind's class at its anchor; other How records, their record class | the multi-scope rule needs a computable "touches" | ruled, Round 2, with the scope wording (§4.2) |
| A-12 | (not raised) | in sdlc edition 1 the derived element kind is `sdlc:Journey` | the ontology's own comment ("derived composition"). `sdlc:State` is a projection's state space, not an element kind | ruled, Round 2 |
| A-13 | thirteen properties | thirteen. The subset rule (Q-8) is part of A3, and A9 checks what the profile holds, leaving the ratchet over landings to G11 | the mutation run found no property checking the subset rule | ruled, Round 2: "as written" |
| A-14 | a refusal is recorded | in the header of its position, with its reason, not as a record of its own | a refusal is the log's act, not an authority act; the header's hash covers it | ruled, Round 2: it matches Writ's "written to the log with the agent as cause" |
| A-15 | (not raised) | `status` carries no force | `dpp-1.md` §3.4 leaves its meaning to the profile, and force is computed | ruled, Round 2 |

---

## Appendix B — the ledger protocol's authority sections, and where each went

Input, read at product-cli `70395df`, `ledger/spec/ledger-protocol.md`. "It was like that in the
ledger" is not a reason for anything here (charter). Each row says why it was kept, changed or
dropped.

| Ledger | Here | Why |
|---|---|---|
| Roles and the closed claim vocabulary (§5.6, LP-6.1) | dropped. A grant carries a scope of ontology classes, and the act kinds are the record kinds | scopes are ruled as classes (P-7). A role is a name for a scope nobody evaluates |
| `grant` with `order: primary \| fallback-N` and `limits` | a fallback is a grant with `fallbackOf` (§2.4); no ranks and no limits | the ruling gives a fallback one limit, no transfer |
| `gacc`, the grant acceptance (LP-6.3) | kept (§3.3) | ruled, Q-1 |
| `genesis: true` with `external_ref` | the genesis record, founded and self-bound (§2.2) | the product IRI P is in the record. A contract reference is the founder's business |
| Unavailability and availability (§5.6) | kept (§2.4), with header-clock times | ruled |
| Revocation of a grant or an acceptance (`rev:`) | kept, as two record kinds (§3.5, §4.6) | ruled, Q-2 |
| Key bindings: add, rotate, revoke; D7 (§4.10–4.11) | add, rotate, close; first key by the grantor; `since` (§5.3) | ruled, Q-3 |
| A close ends the key across namespaces (LP-4.39); ruling 47, per namespace | per product (§5.3) | force is local |
| Re-acceptance after a closed key (LP-4.13) | "needs re-acceptance", from `since` (§5.3) | ruled with Q-3 |
| Namespace policy, `accept_role`, schemes, `require_sk` (§5.6, §6.3) | dropped | "configuration is a decision or does not exist" (Writ); the scope is the policy |
| Decision classes and their floors (§6.4) | dropped. What a decision touches decides who may accept it (§4.2) | the class requirement table was never implemented, and scopes over classes do its work |
| `allowed_signers` derived from bindings (§4.9) | not carried. The reference evaluator derives key windows from the log | a derived file is an implementation's |
| Writer-behavioural refusals (LP-6.14: non-interactive, agent identity, software key) | the machine rule (§5.1) is structural; hardware keys are not required | "no configuration makes it possible" is a property of records, checkable from the log |
