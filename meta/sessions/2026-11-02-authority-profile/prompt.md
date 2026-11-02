# Prompt — the authority profile, 2026-11-02

The session's charter, verbatim, as Emil gave it. Per `DDD-dec-20`, committed before any canon
edit so the session's scope is fixed at arrival.

---

Charter: the authority profile (`applications/sdlc/authority.md`)
The Decision Provenance Protocol (`dpp/1`, merged) fixes the record, the reference and the resolver and defines no force. This session writes the profile that defines force for a product: what makes a decision in force, who may make it so, and how that authority is founded, delegated and transferred. Writ implements it; product-cli’s draft log never claims it; a Context& package is a product under it. Branch from `main` after confirming #42 is in.
Read first. `spec/decision-provenance/dpp-1.md`; `applications/sdlc/what.md` §5 (authoring scopes) and §2; `how.md` §3 and §5; `rulings.md` of the What-move session (the genesis definition of 2026-10-27, Round 5’s multi-scope rule); `DDD-dec-46`, `-54`, `-63`, `-64`, `-73`; the former ledger protocol’s authority sections in product-cli (`ledger/spec/ledger-protocol.md` §5.4–5.7, roles, grants, unavailability, key bindings) as input to read, not authority. Produce the plan and wait for approval before writing.
Already ruled; do not reopen:

* The genesis grant, verbatim from 2026-10-27: root of change authority over one product; held by the human who brought the product into being; unscoped within the product, scoped to nothing outside it; delegates from nothing; every other grant delegates from it; every change resolves to it; a product with no genesis has no authority. Transfer by decision (holder signs, successor accepts, prior closed not deleted); unavailability with a fallback who may act and not transfer; loss without fallback is a new product with `basedOn` import.
* A product is the decision space; its What and its realisation are scopes within it; a package is a product with an empty What and its own genesis, provenance and never authority in another product.
* Scope: a set of ontology classes, optionally narrowed to one element’s `within*` subtree; derived kinds in no scope; a decision touching kinds in more than one scope needs a valid acceptance under each, from the same or different holders, in force only when all are live.
* A machine identity never accepts, reviews, grants or waives; no configuration makes it possible; the attempt is refused and recorded.
* The protocol’s optional `signature`, `acceptedBy`, `acceptedAt` are required under this profile for a decision to be in force; acceptance is a signature by a human holder over the version hash under a grant live at that position.
* Baseline on an acceptance; landings only shrink it; only a fresh acceptance grows it. Waiver: a signed, expiring answer to an open question that changes no decision.
* Scope is evaluated at signing and the result recorded; a later change to the graph does not re-evaluate it.
* Force is local; `basedOn` carries provenance only.

Questions to rule, with the proposal’s answer stated:

1. Grant acceptance. Proposal: a grant is in force only when the grantee has signed acceptance of it (the ledger’s `gacc`), so authority is never imposed. Say whether the genesis is the one exception (it is founded, not accepted).
2. Revocation. Proposal: a grant is revoked by a decision of its grantor or any holder above it in the chain; revocation does not invalidate acceptances already made under the grant (they were valid at their position); it prevents new ones. Say whether a revoked chain below a revoked grant falls with it (proposal: yes, from the revocation’s position).
3. Keys. Proposal: a holder binds one or more signing keys per namespace by a signed record; rotation is a new binding plus a close; a closed key never signs again; a key belongs to one holder; verification of an old acceptance uses the key bound at its position. Keep the ledger’s D7 reading where it fits.
4. Review. Proposal: a review (rejection or request for change) is signed under the same grant that could have accepted, has no force, and stays in the log.
5. What “human” means. Proposal: an identity in the protocol’s scheme that no attribution record names as a machine; a machine is any identity with an `attributedTo`. Say what a team identity is (proposal: not a holder; a holder is one person; teams are expressed by several grants).
6. Positions and clocks. Proposal: the profile requires a positioned log whose header clock is covered by the header hash (Writ’s `[D2.3]`, `[D2.11]`), and every time-dependent evaluation (lease, waiver expiry, key validity) uses header clocks only. Say whether a non-positioned system can claim the profile (proposal: no; it can claim provenance only).
7. Conformance. Proposal: one class, “authority-conformant”, claimed by a system that implements all of the above and passes a suite; the suite is property tests over generated grant, acceptance, revocation and key histories, mirroring Writ’s G2 and G3 so Writ’s suite is the first implementation of it.

Deliverables:

* `applications/sdlc/authority.md`: scope; the genesis grant; grants, scope, delegation, acceptance of grants, revocation; acceptance of decisions, baselines, waivers, reviews; keys and identities; positions and clocks; conformance with the suite’s property list; a decisions appendix recording every departure from the proposal with reasons.
* Vocabulary terms under `sdlc:` for every record kind above, each mapped to a `dpp/1` record shape using `extensions` for what the protocol does not define.
* A worked example: one product with a genesis, two delegated scopes (What; How and code), one multi-scope decision accepted under both, one revocation, one key rotation, one waiver that expires, checked by the existing checker extended for authority.
* Supersession of whatever in `DDD-dec-46`, `-54`, `-64` this document now states more precisely; `DDD-dec-72` (product-cli’s re-pin) is unblocked by this PR and says so.
* Session record under `meta/sessions/`; ids from the next free after checking `main`; `Basis:` lines; validators and both checkers passing; nothing merged. Emil ratifies by merging.

Discipline. Claude proposes; Emil rules; record rulings verbatim. Change ruled material by supersession. The ledger protocol is input; “it was like that in the ledger” is not a reason. No model identifiers in any record.
