# Plan — the authority profile, 2026-11-02

**Status: approved in Round 1 (2026-11-02), with rulings (`rulings.md`). Renumbered by R-14:
every id below from 77 moves to 85 onward (77 → 85, 78 → 86, 79–83 → 87–91). The text is left as
approved; the table at the end of Part 4 gives the ids as filed.** Originally: proposed, waiting for approval. Nothing below is written until Emil rules. Questions 1
to 7 are the charter's, each with the charter's proposal and Claude's answer. Q-8 to Q-10 and F-1
to F-3 come from the arrival findings in `bootstrap.md`. Where a ruling differs from an answer
here, the ruling governs, and `rulings.md` records it verbatim.

Register: **Agree** means Claude's answer is the charter's proposal. **Amend** means the
proposal stands with an addition or a narrowing, and the departure goes into the decisions
appendix. Every answer is Claude's until ruled.

---

## Part 1 — readings of ruled material (not reopened; flagged)

**F-1. The three required fields.** *Reading:* under the profile, a decision `D@v` is in force
only through an **acceptance record**. That is a `dpp/1` record whose `basedOn` pins `D@v` (so its
signature covers `D@v`'s hash) and the grant it is made under. It must carry a `signature`. Its
`by` is the charter's `acceptedBy` and its `at` is `acceptedAt`. This is `how.md` D-6, as the
examples already do it. `dpp/1` A-10 removed `acceptedBy` and `acceptedAt`, and §3.7 forbids
inventing undotted members, so no record carries them by name. "A signature by a human holder over
the version hash" holds transitively: the holder signs the acceptance's canonical form, and that
form contains the pin. `UNVERIFIED — Emil review`: that this reading meets the ruling.

**F-2. Hashed dotted members, not `extensions` — a proposed departure.** Every authority field (a
grant's grantee, scope and parent; an acceptance's grant, scope result and baseline; a waiver's
question and expiry; a key binding's key) goes in the **hashed** dotted member
`dk.decision-driven-design.authority`. That is where `how-vocabulary.md` already puts them.
`extensions` holds only what may change without a new version and confers nothing: display
names, and a copy of the record's log position for readers that lack the log. *Reason:*
`extensions` is outside the pin and the signature (`dpp-1.md` §3.7, §11.3). A grant whose scope
lives there can be widened after the grantor signs, and every pin and signature still verifies.
That breaks the ruling that acceptance is a *signature* over what is accepted. The charter's
wording would hold if "extensions" means "the protocol's extension mechanism" (dotted members
being the hashed half of it). Rule which.

**F-3. `[D2.11]`.** Its text is not in Hafeok/writ at `6737ac9`. The plan cites `[D2.5]`
("whose header carries the writer's clock and is covered by the header hash") and `[D2.3]` for
the clock rule, and cites `[D2.11]` only as Emil states it. If `[D2.11]` says more than that,
state it and the profile will carry it.

---

## Part 2 — the charter's questions

### Q-1. Grant acceptance — **Agree, with two signatures named; genesis is the exception**

- A grant is a decision of its **grantor**, signed by the grantor under the grant it delegates
  from. That signature is the grantor's act. It is not a separate acceptance, because the grantor
  is the holder who decides. This is Writ's "accepted by a holder whose own grant covers the
  authority graph" (`[D2]`; `bootstrap.md` finding 5).
- A grant is **live** only from the position of the grantee's signed **grant acceptance**, a
  record pinning the grant's hash. Authority is never imposed. Until then the grant confers
  nothing, and an acceptance made under it is refused.
- **The genesis is the one exception: founded, not accepted.** The founding record is the
  holder's own signed act, naming themselves. A separate acceptance would be the same person's
  signature twice over the same content. A **transfer** is not founding. The successor signs a
  grant acceptance of the transfer, as ruled, and the new genesis is live only from that position.
- A **fallback** grant is a grant, so its fallback holder accepts it like any other.

### Q-2. Revocation — **Agree, amended: closing is not revoking; supersession of a grant is not revocation**

- A grant is revoked by a decision of its grantor, or of any holder above it in its chain, signed
  under that holder's grant. Acceptances already made under it stay valid: each was valid at its
  own position (G2 reads "a grant live at its own position"). From the revocation's position, no
  new acceptance, review, waiver or grant may be made under it.
- **The chain below falls with it, from the revocation's position (agree).** Every grant
  delegating from a revoked grant, directly or through a chain, is not live from that position.
  Acceptances already made under those grants also stand. Nothing re-parents silently: a holder
  above re-grants if the delegate should keep authority.
- **Amendment, transfer.** Grants delegate from the **genesis decision** (its `id`), not from one
  holder's version of it. A transfer supersedes the genesis record and closes the prior holder's
  grant. That close is not a revocation, and nothing delegated from the genesis falls. Otherwise
  every transfer would void every grant in the product (`bootstrap.md` finding 7).
- **Amendment, supersession of a grant.** A grant is narrowed or widened by a superseding version,
  signed by its grantor and re-accepted by the grantee. Its delegates keep delegating from the
  grant's `id`. Their effective scope at any position is the intersection along the chain live at
  that position (Q-8). Narrowing a grant therefore narrows its chain from that position, without
  revoking anything.
- **Addition: revoking an acceptance.** The charter does not raise this, but the ledger had it and
  a product needs it. An acceptance may be revoked by its signer, or by a holder above the grant
  it was made under. The decision stops being in force from that position, and the acceptance
  stays in the log. This is distinct from supersession, which replaces the decision. Rule whether
  to include it.

### Q-3. Keys — **Agree, amended: "namespace" is the product; the first key is vouched for by the grantor**

- **Namespace = product.** A key binding is per product, and nothing in one product's authority
  has effect in another. "Force is local" applies to keys too. This is the ledger's ruling 47
  direction, adopted here on its own reason, not as precedent.
- A holder binds **one or more** keys by a signed **key-binding** record. **Rotation** is a new
  binding plus a close, signed by the key it closes. A **closed** key never signs again in that
  product. A key is bound to **one holder** in a product, ever. Verification of an acceptance
  uses the binding live at **its** position: rotation never invalidates history.
- **The first key — D7 generalised (proposed departure from "keep D7").** The genesis holder's
  first key is self-bound in the founding (D7 as it was). Every other holder's first key is bound
  by the **grantor**, inside the grant record, so the person who delegates vouches for the key.
  The ledger had the genesis holder vouch for every first key. Under delegation that would make
  the genesis holder vouch for people they never granted. Further keys, rotations and closes are
  the holder's own acts. A close may also be filed by any holder above in the chain, which is D7's
  "or the genesis holder's", generalised the same way.
- **Compromise — proposed addition.** A close may state a `since` position earlier than its own.
  Acceptances signed by that key at positions in `[since, close)` stay valid at their positions,
  so replay holds (G6). From the close's position, the decisions they put in force are reported
  "needs re-acceptance" and lose force until re-accepted. No acceptance is rewritten. Rule whether
  to include it. The alternative is to leave compromise to a revocation of each acceptance.

### Q-4. Review — **Agree**

A review is a rejection or a request for change. It is signed under a grant that could have
accepted the same version at that position: the same scope evaluation, recorded. It has no force,
stays in the log, and does not block a later acceptance. Writ may surface it. A signed comment by
anyone else is not a review under this profile.

### Q-5. "Human" — **Amend: positive attribution record; `attributedTo` refuses, it does not classify**

The proposal's "a machine is any identity with an `attributedTo`" does not work as stated.
`attributedTo` is a member of a record, not a property of an identity. A human assistant filing
for their manager would be classed a machine by it. So:

- A **machine identity** is one named by a signed **attribution record**: identity *M* is
  software, and human *H* is responsible for it. Any holder may file one for an identity in their
  product. *M* is a machine from that position, in that product, for good. No record un-names a
  machine.
- **Independently, a record whose `by` carries an `attributedTo` is never an acceptance, review,
  grant, waiver or key binding.** It is refused and recorded, whoever `by` is. This makes "no
  configuration makes it possible" hold structurally, not by lookup.
- **A grant to an identity is the grantor's attestation that it is one person.** A grant to a
  machine-named identity is refused. A **team identity** (a list, a group mailbox, a role
  account) is not a holder. A holder is one person, and a team is several grants (agree).
- **Weakest point.** No protocol can prove a key is held by a person. The profile makes the claim
  attributable, with the grantor accountable for it, and makes a later attribution decisive. It
  does not make it true. Acceptances by an identity made before it was named a machine stand at
  their positions, and are reported "needs re-acceptance" from the naming (the same mechanism as
  Q-3's compromise). `UNVERIFIED — Emil review`.

### Q-6. Positions and clocks — **Agree; non-positioned systems claim `dpp/1` conformance only**

- The profile requires a **positioned log**: a total order of positions, each with a header that
  carries the writer's clock and the hashes of the records landed at it, chained to the previous
  header and covered by the header hash (`[D2.5]`, `[D2.3]`; F-3).
- **Every time-dependent evaluation reads header clocks only:** grant liveness, unavailability
  windows, key validity, waiver expiry and session leases. A record's own `at` is the author's
  claim (`dpp-1.md` §11.4) and is never read for force. The profile requires an authority record's
  `at` to fall on its position's header date, and a record where it does not is refused.
- **Waiver expiry** is a header-clock instant. A waiver is live at *p* iff *p*'s header clock is
  before the instant. This is not Writ `[D2.3]`'s "review-by is a position" (`bootstrap.md`
  finding 4). A waiver's meaning is "for two weeks", which a position cannot say, so Claude
  proposes Writ follow the profile. Rule which.
- **A non-positioned system cannot claim the profile (agree).** It can claim `dpp/1` conformance.
  A positioned log can also claim Writ's *provenance-conformant* class. The charter's "provenance
  only" is read as one of those two. An ADR directory is the first and not the second.

### Q-7. Conformance — **Agree, one class, with the property list stated in the profile**

One class, **authority-conformant**, the name Writ `[D2.5]` already uses. It is claimed by a
positioned log that implements the profile and passes the suite. The profile states the suite as
a numbered **property list**: each property is a predicate over a generated history of grants,
grant acceptances, revocations, transfers, unavailabilities, key bindings, attributions,
acceptances, reviews, baselines, landings and waivers, each at a position with a header clock.
The draft list:

| # | Property | Mirrors |
|---|---|---|
| A1 | A decision is in force at *p* iff, for every scope it touches, it has an acceptance live at *p*, signed by a human holder, under a grant live and covering it at the acceptance's own position | G2, multi-scope rule |
| A2 | No machine-named identity, and no record carrying `attributedTo`, produces an acceptance, review, grant, waiver or key binding. Every attempt appears as a recorded refusal | G3 |
| A3 | Every chain from a live grant ends at the product's one live genesis. No history has two live geneses | genesis definition |
| A4 | A grant is live only from its grantee's acceptance. The genesis is live from founding or from the successor's acceptance | Q-1 |
| A5 | After a grant's revocation at *r*, no act under it or under any grant below it is valid at any *p* ≥ *r*. Acts before *r* keep their validity | Q-2 |
| A6 | A transfer changes no grant's liveness except the prior holder's genesis | Q-2 |
| A7 | The scope result recorded with an acceptance is a function of the log up to the acceptance's position. No later graph change alters it | scope at signing |
| A8 | No signature verifies under a key closed at or before its position. Every signature verifies under the key bound to its signer at its position | Q-3 |
| A9 | A baseline never grows between two acceptances of the same decision | G11 |
| A10 | A waiver changes no decision, is live only before its expiry by header clock, and answers only an open question | waiver ruling |
| A11 | A fallback acts only while its primary is filed unavailable, and never transfers | genesis ruling |
| A12 | Every evaluation at *p* is a function of the log up to *p*, headers included, and replay as recorded reproduces it | G1, G6 |
| A13 | A `basedOn` reference into another product never satisfies A1 | force is local |

**What this PR ships of the suite:** the property list, and a stdlib-only reference evaluator
(`applications/sdlc/authority/evaluate.py`) that the example checker uses. The checker also runs
A1 to A13 over seeded, generated histories. That shows the list is consistent and executable
against one evaluator. It is not Writ's suite, and the profile says Writ's suite is the first
implementation of it (`[D2]` G2, G3). No property-testing library is used: none is installed, and
the checker must run on a stock Python.

---

## Part 3 — new questions

**Q-8. Delegation.** *Proposal:* a grant may delegate only if it says so (`mayDelegate`); the
genesis always may. A delegated grant's scope must be a subset of its grantor's, and this is
checked at the grant's signing. Its effective scope at any position is the intersection along its
chain at that position (Q-2). *Why:* without the flag, every product owner can silently create
more acceptors. Without the subset rule, a chain escalates. Alternative: every grant may delegate,
subset only.

**Q-9. Where the worked example lives.** *Proposal (A):* in the How examples' test product, acme
shop, as its authority history, added and never edited. The stand-ins (`bootstrap.md` finding 8)
stay as history. New records: key bindings; `GRANT-what@2` and `GRANT-how@3` with class scopes;
grant acceptances; re-acceptances of the six How decisions and `WHAT-found@1` under the profile;
the multi-scope decision; the revocation, rotation and waiver. A fixture log gives every record a
position, with header clocks and chained header hashes. *Why A:* the How's "in force" half
(`how.md` §11.2) and the What's (`what.md` §7.2) can then be shown on decisions that exist. And
`DDD-dec-72`'s re-pin assumes an acceptance of the moved What means something. *Cost:* the
multi-scope decision creates a What element, so the What graph changes. That is `what@4`, with
`vectors.json` recomputed and `what/check.py` green. `vectors-varve.json` (M-12) is keyed to
`what@2` and is unaffected. *Alternative (B):* a separate small product in
`applications/sdlc/authority/example/`, with acme's migration as a successor item.

**Q-10. M-1's two other items.** *Proposal:* the **violation-description field** (`DDD-dec-52`)
stays where `how-vocabulary.md` put it, `…authority.violation`. The profile owns it in one
section: the field's shape, and that it confers no force. **Attestations** (`what.md` §3.2.3) are
**out of scope** here and stay a successor item. An attestation is a signed ground reading, not
an act of authority. Its only authority question is who may sign one, and that is a grant scope
the profile already expresses.

---

## Part 4 — the work, once ruled

One PR. Each step is its own commit with a `Basis:` line. Validators, the `dpp/1` suite, and both
checkers run before each commit.

| # | Deliverable | Files | Basis |
|---|---|---|---|
| 0 | Rulings verbatim; `DDD-dec-77`: the charter's already-ruled list (as `DDD-dec-54` recorded the How charter's); `DDD-dec-78`: Q-1 to Q-10 and F-1 to F-3 as ruled | `rulings.md`; `core/decisions/DDD-dec-77.yaml`, `-78.yaml` | `DDD-dec-46`, `-47`, `-54`, `-64` |
| 1 | `applications/sdlc/authority.md`. §1 scope and non-goals. §2 the genesis grant (verbatim, then founding, transfer, unavailability, fallback, loss). §3 grants: scope, delegation, grant acceptance, supersession, revocation. §4 acceptance of decisions: the acceptance record, the multi-scope rule, scope at signing, baselines, waivers, reviews, revoking an acceptance. §5 identities and keys: human, machine, attribution, team, bindings, rotation, close, compromise. §6 positions and clocks. §7 the violation-description field (Q-10). §8 conformance and the property list. Appendix A, decisions: every departure from the charter's proposal, with reasons. Appendix B, the ledger's authority sections and where each went (kept, generalised, dropped) | `applications/sdlc/authority.md` | `DDD-dec-78` |
| 2 | The vocabulary: one term per record kind (`sdlc:Genesis`, `sdlc:Transfer`, `sdlc:Grant`, `sdlc:GrantAcceptance`, `sdlc:Revocation`, `sdlc:Unavailability`, `sdlc:Availability`, `sdlc:KeyBinding`, `sdlc:Attribution`, `sdlc:Acceptance`, `sdlc:AcceptanceRevocation`, `sdlc:Review`, `sdlc:Waiver`, `sdlc:Refusal`, plus `sdlc:Scope`, `sdlc:baseline` and the header), each mapped to its `dpp/1` shape. It is a table in `how-vocabulary.md`'s form, and replaces that file's two "the profile's" rows by pointers | `applications/sdlc/authority-vocabulary.md`; two rows of `how-vocabulary.md` | `DDD-dec-78` |
| 3 | The reference evaluator, and the property run over generated histories | `applications/sdlc/authority/evaluate.py`, `authority/properties.py` | `DDD-dec-78` |
| 4 | The worked example, per Q-9's ruling. Product, genesis, two delegated scopes; the multi-scope decision shown not in force after one acceptance and in force after both; one revocation with its chain falling; one key rotation with an old acceptance still verifying; one waiver on the `RESID` Azure open question, live at one position and expired at a later one by header clock; one machine acceptance refused and recorded. `build.py` gains the records, and still refuses to change any published version. `check.py` replaces its stand-in step 4 with the evaluator, and states what it shows and what it does not | `how-examples/` (or `authority/example/` under B); `what@4` and `vectors.json` under A | `DDD-dec-78`; `DDD-dec-55` ruling 4 |
| 5 | Pointers from `what.md` §1.2, §5.1 and §7.2, and `how.md` §1.1, §1.2 (precondition 3) and §9.4 D-6, to the profile, by a dated update note. The ruled text is left as written | those files | `DDD-dec-78` |
| 6 | Supersessions, one decision each, in `DDD-dec-73`'s form (carried text, then what is stated more precisely). `DDD-dec-79` supersedes `-46`: transfer as a close that is not a revocation, the successor's acceptance, fallback limits. `DDD-dec-80` supersedes `-47`: F-1's mapping. `DDD-dec-81` supersedes `-54`: ruling 4's terms now defined. `DDD-dec-82` supersedes `-64`: P-7 stated as the profile's §3 and §4, P-1 to P-6 carried. `DDD-dec-83` supersedes `-72`: "sequenced after the authority profile's pull request" is discharged by this PR, and the rest is carried unchanged, `[PROPOSED]` items included | `core/decisions/DDD-dec-79…83.yaml` | each the decision it supersedes, and `DDD-dec-78` |
| 7 | Session record: the where-it-landed table; successor items (product-cli's re-pin, now unblocked; Writ's suite; Writ `[D2.3]` if Q-6 is ruled as proposed; attestations; acme's migration under B); the sessions README row | `rulings.md`, `successor-items.md`, `meta/sessions/README.md` | — |

**R-14 (2026-11-02):** filed as `DDD-dec-85` (step 0, the charter), `-86` (step 0, Round 1),
`-87` to `-91` (step 6, superseding `-46`, `-47`, `-54`, `-64`, `-72` in that order). The plan's ids
`DDD-dec-77` to `-83` were provisional, and are rechecked against every branch before each is
filed (`bootstrap.md`: 74 to 76 are held by an unmerged branch). Test keys are throwaway and
generated per build, as in the How examples. No real key is used.

**What the example will show, and what it will not.** It will show that the profile's rules
execute as written over one hand-built history, with outcomes predicted before the run. It will
not show that the profile is right, and it will not show that any real log implements it.

**Weakest point of the plan.** Q-9 (A) puts the profile's example into an estate whose pins and
vectors other work relies on (`what@N`, M-12, product-cli's re-pin target). Every change there is
by new version, and `build.py`'s refusal to change a published record is the guard. If that guard
is not trusted, choose B.
