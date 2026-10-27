# Prompt — the Product Framework move, chartered 2026-10-27

Chartered by Emil's instruction "Then charter the move session" (Round 5 of
`meta/sessions/2026-10-27-product-framework-what/rulings.md`). Written by Claude from the rulings
`DDD-dec-41` to `DDD-dec-50`. Committed before the session works, per `DDD-dec-20`.

**This charter is Claude's drafting, not Emil's words.** Emil ruled what moves and on what terms.
The gate structure, the inventory and the predictions below are Claude's proposal for how to
carry those rulings out. Emil may amend the charter before the session arrives; an amendment is
committed here before any gate runs.

## Precondition

The session does not start until PR #39 is ratified (merged). Every ruling it executes lives in
that PR. Before Gate 0 closes, check the merge against the ratified head named in #39.

## Purpose

Move the Product Framework's What (github.com/Hafeok/product-framework, v1.10.0 at `c895652`)
into `applications/sdlc/` as the opinionated specification of what a software application is and
does — its ground and tolerance (`DDD-dec-41`, `DDD-dec-42`) — with decisions anchored to What
elements, the genesis grant and authority profile alongside it, and the framework's own
constructs replaced by pinned canon where canon already states them.

## Rulings this session executes

| Ruling | Decision |
|---|---|
| Only the What moves; How (§§4–7) and Delivery retired | `DDD-dec-41`, `DDD-dec-42` |
| Home `applications/sdlc/`; Two Pillars conformance dropped | `DDD-dec-42` |
| A system is ground and tolerance, not an address coordinate | `DDD-dec-41`, `DDD-dec-42` |
| Every decision anchors to a What element; every change of the What is a decision | `DDD-dec-42` |
| Tools never change the What; gathered material is signed and approved by a human principal | `DDD-dec-43` |
| Design system and content store are What; data conformance is an add-on outside the framework; authoring scopes are central | `DDD-dec-44` |
| Reification and content resolution enter as obligations; their content is decisions; the framework ships no widgets or words | `DDD-dec-45` |
| The genesis grant: definition, space, transfer, home, packages | `DDD-dec-46` |
| The authority profile: force, acceptance, "signed" | `DDD-dec-47` |
| §9 cut down, §10 one level, the store is Varve | `DDD-dec-51` |
| Verdicts: declaration and ground reading recorded; "violation description" a record field | `DDD-dec-52` |

## Out of scope

- Any How, including what a package ships (`DDD-dec-46`: a later session).
- The protocol rename (`DDD-dec-53`): the protocol branch's act, not this session's.
- T2b and the reworded falsifier (`DDD-dec-49`): its own session.
- product-cli's re-pin (`DDD-dec-50`): after this session lands.
- Data conformance (§13): an add-on, not moved.
- Any change to canon upstream.

## Gates

Stop at every gate. Write each gate's prediction before its operations.

**Gate 0 — arrival.** PR #39 merged at its ratified head; `graph/upstream.yaml` still pins
v5.15.2 (if not, read canon at the new pin and say so); next free decision id checked across both
repositories and every open branch; `bootstrap.md` completed and committed with this file.

**Gate 1 — the inventory.** A table, one row per Product Framework section, each marked *moves*,
*moves as obligation*, *replaced by canon pin*, *retired* or *out*, with the decision that
governs it. Prediction, committed before the inventory is written:

| PF section | Predicted disposition | Governing |
|---|---|---|
| §1 Purpose | Rewritten for the What only | `DDD-dec-42` |
| §2 The split; §2.1 authoring order | Steps 1–5 of the funnel move; step 6 (the How) retired; the split becomes What / realisation under one genesis | `DDD-dec-42`, `DDD-dec-46` |
| §2.2 Allocation reading | Replaced by canon pin | `DDD-dec-42` |
| §3 The What (§3.0–§3.6) | Moves | `DDD-dec-42` |
| §§4–7 How, work units, verification, Delivery | Retired, except §4.5 and §4.6 | `DDD-dec-42` |
| §4.5, §4.6 Reification, content resolution | Move as obligations | `DDD-dec-45` |
| §8 Two Pillars | Retired | `DDD-dec-42` |
| §9 Encoding and the derivation contract | Moves cut down: one graph, stable element identity, derivation edges within the What, RDF + SHACL reference; How edges dropped; anchors-to and supersedes added | `DDD-dec-51` |
| §10 Conformance rules | Regenerated, not moved: one level, described and in force | `DDD-dec-51` |
| §11, §12 Design system, content store | Move as obligations; catalogues are accepted decisions | `DDD-dec-44`, `DDD-dec-45` |
| §13 Data conformance | Out (add-on) | `DDD-dec-44` |
| §14 Authoring scopes | Moves, central; reframed as gathering scope plus delegated authority | `DDD-dec-43`, `DDD-dec-44`, `DDD-dec-46` |

The gate stops for Emil's ruling on any prediction the inventory overturns.

**Gate 2 — authority.** Draft, under `applications/sdlc/`, the genesis grant (term definition per
`DDD-dec-46`) and the authority profile (per `DDD-dec-47`), each with its falsifier and what it
breaks. The authority profile defines the "violation description" field (`DDD-dec-52`). Records use
the token decprov/1 (`DDD-dec-53`), and only once the protocol branch has renamed and merged. The gate stops for Emil's ruling on both texts and on where downstream terms register.

**Gate 3 — the What.** Write the moved What under `applications/sdlc/`: §3 restated for the
What only, the obligations of `DDD-dec-45`, authoring scopes per gate 2, the decision-anchoring
model of `DDD-dec-42`, and pinned `ddd:ref`s wherever canon states the construct. One sustained
worked example through every section, tested against a junior engineer's first contact. The
gate stops for Emil's review.

**Gate 4 — the retirement in the Hafeok repository.** A notice in
github.com/Hafeok/product-framework that §§4–8 are retired and the What has moved, pointing here.
An act on another repository: proposed as its own pull request there, only with Emil's
go-ahead at this gate.

## Risks named at chartering — Claude, UNVERIFIED — Emil review

1. **"Floor" collides.** PF §3.5 titles named-algorithm primitives "the Polanyi floor". Canon
   registers its own floor term. Gate 3 uses the canon term exactly as registered or renames the
   PF construct; it does not carry the PF title over.
2. **The worked example.** The Product Framework ships `examples/checkout/`, including
   design-system and content-store manifests that are instances. Under `DDD-dec-45` the framework
   ships no instances, so the example's manifests become example decisions, not framework text.
   Phoenix stays downstream-only and is never the example.
3. **§9 is load-bearing.** Ruled to move (`DDD-dec-51`). Stable element identities are what
   decisions anchor to; Gate 3 fixes their form before any decision is written against them.
4. **Verdicts.** Ruled (`DDD-dec-52`): record the declaration and the ground reading. Gate 3
   writes no construct that stores a verdict.

## Amendments before arrival

| Date | Amendment | Basis |
|---|---|---|
| 2026-10-27 | §9 and §10 predictions filled from the ruling; Gate 1 no longer stops for them; Gate 2 carries the violation-description field and the decprov/1 token; risks 3 and 4 updated | `DDD-dec-51`, `DDD-dec-52`, `DDD-dec-53` |
