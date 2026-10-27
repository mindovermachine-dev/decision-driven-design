# Rulings — the Product Framework What, 2026-10-27

Rulings given during the session, verbatim, recorded when given. `prompt.md` stays the arrival
charter; this file carries what came after it.

## Round 1 — recorded as `DDD-dec-41`

The verbatim message is in `prompt.md` ("Emil, message 2").

## Round 2 — recorded as `DDD-dec-42`

Ruling on `DDD-dec-41`'s flagged reading and its open items O-1 to O-6:

> ruling 3 accepted. 1. yes 2. they are retired 3. drop it 4. explain this to me? 5. it anchors
> to a what element, we should have decisions for each change of the what 6. agreed

| Item | Ruling |
|---|---|
| Ruling 3's reading | Accepted |
| O-1 Path | `applications/sdlc/` |
| O-2 How and Delivery | Retired |
| O-3 Two Pillars | Dropped |
| O-4 Preview profiles | Not ruled; explanation requested |
| O-5 Decisions in the What | Anchor to a What element; a decision for each change of the What |
| O-6 product-cli | Agreed: re-pin to the moved What |

## Round 3 — recorded as `DDD-dec-43`

Ruling on the weakest point Claude named for §14 (authoring scopes) in its O-4 explanation:

> we dont let tools change it, but we acknowledge that parts of the entire what lives else where
> and processes where we should be able to gather the information from those tools are a valid
> use case, but all must be signed and approved by a human principal

| Item | Ruling |
|---|---|
| O-4, §14 Authoring scopes | Tools never change the What; gathering from tools and processes is valid; everything gathered is signed and approved by a human principal |
| O-4, §§11–13 | Not ruled; Claude's proposal stands as `[PROPOSED]` |

## Round 4 — recorded as `DDD-dec-44`

Ruling on Claude's `[PROPOSED]` reading of §§11–13 and the place of §14:

> design system and content store are parts of the what - they are essiential to the
> implementation and you cant build it without it. and data conformance is something that be done
> by reading the what, its a value add on not something thats part of the framework. Authoring
> scopes must be a central part of the framework, who can change what, and who helds the genesis
> grant for a given product

| Item | Ruling |
|---|---|
| §11 Design system | Part of the What (Claude's proposal to retire it superseded) |
| §12 Content store | Part of the What (Claude's proposal to retire it superseded) |
| §13 Data conformance | Not part of the framework; a value add-on that reads the What |
| §14 Authoring scopes | Central to the framework: who can change what, and who holds the genesis grant |

## Round 5 — recorded as `DDD-dec-45` to `DDD-dec-50`

Rulings on the three items `DDD-dec-44` left open, and three more, delivered as an attached file. Verbatim:

> Rulings on the three open items, and three more (2026-10-27). File as DDD-dec-45 onward; check upstream for id collisions first.
>
> Open 1, §4.5 and §4.6 — ruled: the form moves in; the content is decisions. Reification and content resolution enter the What as obligations: that reify(AIO, context) → CIO exists; that every (AIO, context) pair a system can reach is covered or declared unreifiable; that every (content key, locale) pair resolves or is declared missing. The content of a rule (which CIO, which words) is not catalogue text in the What; it is a decision anchored to the What element it binds, per ruling 5. The catalogue is the set of accepted decisions. The framework ships obligations, never widgets or words.
>
> Open 2, genesis grant — ruled.
>
> Definition: The genesis grant is the root of change authority over one product. It is held by the human principal who brought the product into being. It is unscoped within the product and scoped to nothing outside it, and it is the only grant that delegates from no other. Every other grant over the product delegates from it, directly or through a chain; every decision that changes the product resolves, through its acceptance and the grant that acceptance was made under, to the genesis. A product with no genesis grant has no authority, and nothing in it is in force.
>
> Space: a product is the decision space. Its What and its realisation (the repositories) are two scopes within it, under one genesis; a repository with no What is a product whose What is empty.
>
> Transfer: by decision, never by edit. The holder signs a transfer naming the successor; the successor signs acceptance of the grant; the transfer supersedes the prior genesis record; the prior holder’s grant is closed, not deleted. Holder unavailability is filed unavailability with a fallback holder, who may act and may not transfer. Loss of the holder with no fallback cannot be repaired from inside: a new genesis founds a new product, and the old product’s decisions are imported by basedOn, which keeps provenance and records that authority was re-founded.
>
> Home: downstream, applications/sdlc/. Not actor-general: that layer has no concept of a space someone brought into being, so a genesis there would be the origin of nothing. The term is software’s.
>
> Consequence, to be stated with it: a Context& package is not part of a customer’s product and has no genesis in the customer’s space. Its decisions enter by import under the customer’s genesis, basedOn the package’s versions. The package is itself a product, with its own genesis held by Context&, whose What is its decisions and whose realisation is what it ships. What a package ships is the How, and the How is not yet specified; that is a later session, not this one.
>
> Open 3, “signed” — ruled. A What-changing decision is a protocol record. The protocol (three things: record, reference, resolver) does not define force. The authority profile, a separate document in applications/sdlc/ alongside the genesis grant, makes signature, acceptedBy and acceptedAt required for a decision to be in force and defines acceptance as a signature by a human holder under a grant delegating from the genesis. “Signed” means that and nothing weaker.
>
> Token — ruled: [dpp/1 | decprov/1]. This handoff says decprov/1; the protocol branch (claude/epic-hopper-qr18wj, PR pending) ships dpp/1 in records, system.json, the well-known path decision-provenance and the suite. One token. The losing session renames before merge; neither merges until they agree.
>
> Falsifier — reworded, not withdrawn. A step whose only What form is “a verdict was computed” is not evidence that the What is a lens. A verdict is a valuation: a function of the What and the ground at a position, never stored. The What’s form for such a step is the declaration that makes it computable (the violation description on the anchoring decision). Re-run the T2b mapping with that reading: a step fails the falsifier only if it has neither a What element nor a decision that declares it.
>
> Housekeeping. Project instructions re-pinned to upstream v5.15.2 and DDD 4004b49. product-cli re-pins to the moved What once PR #39 is ratified (ruling 6 stands).
>
> Record all of the above verbatim in rulings.md. Then charter the move session.
| Item | Decision |
|---|---|
| Open 1, §4.5 and §4.6: the form moves in, the content is decisions | `DDD-dec-45` |
| Open 2, the genesis grant: definition, space, transfer, home, consequence | `DDD-dec-46` |
| Open 3, "signed": the authority profile | `DDD-dec-47` |
| The protocol token: one token, the losing session renames | `DDD-dec-48` |
| The falsifier, reworded | `DDD-dec-49` |
| Housekeeping: re-pins | `DDD-dec-50` |
