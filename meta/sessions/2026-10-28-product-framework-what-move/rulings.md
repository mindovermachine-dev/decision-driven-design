# Rulings — the Product Framework What move, 2026-10-28

Rulings given during the session, verbatim, recorded when given. `prompt.md` stays the arrival
charter; this file carries what came after it.

## The charter's own rulings

The list under "Already ruled; do not reopen" in `prompt.md`, verbatim there. Each restates a
decision already on `main` (`DDD-dec-41` to `DDD-dec-62`), except one: §6.3.1 moves with the What.
That reverses `how.md` Appendix B's "not carried" (`bootstrap.md`, finding 5).

## Round 1, 2026-10-28 — recorded in `DDD-dec-63` and the plan

Verbatim:

> Round 1, move session (2026-10-28).
> Identity form (`DDD-dec-63`) — ruled, with two changes.
>
> * P as the product IRI, stable across genesis transfer, and also the product node: ruled as proposed.
> * Flat element IRIs `P/what/<key>`, encoding neither kind nor position: ruled as proposed.
> * Keys are opaque. A key is a ULID minted at creation; the human name is `rdfs:label` and may change by decision. This removes the weakest point you named (a readable key that reads as the old name forever) and makes the rule simple: nothing in an identity carries meaning. Baselines and anchors become unreadable in raw form, and that is `explain`'s job to resolve, not the identifier's to avoid.
> * Rename, property change and move under the same IRI; kind change, split and merge as new elements with `sdlc:succeeds`; baselines not carried over: ruled as proposed.
> * No blank-node ban; the canonical form is RDFC-1.0. The decision protocol and Writ already name RDFC-1.0 as the reference canonical form for graph content; a second canonicalisation (`sdlc-nt/1`) would be a second hash law, and there is one. Element identities are IRIs and never blank nodes, which is what the ban was protecting; blank nodes inside an element's description (lists, ordered fields) are allowed and canonicalised by RDFC-1.0. Drop the "explicit positions everywhere" rewrite and the unchecked claim that every §3 construct survives it.
> * A What-version as a `dpp/1` record pinning the decisions in force and listing every element with its hash; Decider and Projector logic as a digest on its element; graph hash from the canonical graph: ruled as proposed, with RDFC-1.0 as the canonical form.
>
> Q-1 — ruled: take §3.7 from `55c9281`, and with it the changes that commit makes to §3.2.0, §3.2.1, §3.3, §3.4 and §6.3.1; those were the corrections accepted on 2026-10-21 (acts_as beside source, the actor as a fourth argument of `decide`, scope rules per kind, `keyed_by`). Note in the session record that v1.11.0 was never merged upstream and is adopted here by ruling.
> Q-2 — ruled: take the ontology and shapes from product-cli's `schema/`, the copy the Rust round-trip tests read. Record the diff between the two copies in the session record; reconcile nothing from the other.
> Q-3 — ruled: do not carry the §4–§7 classes at all. Not at `pf:` IRIs, not re-minted under `sdlc:`. The How now has its own vocabulary (`how-vocabulary.md`, three kinds); nothing references `pf:ReificationRule` or `pf:Feature` any more. The `pf:` namespace ends with this move. Writ's definition (which says `pf:` keeps those classes) is amended on my side today.
> Q-4 — ruled: own PR, sequenced after this one and before product-cli's re-pin, because an acceptance of a moved What means nothing until the authority profile exists.
> Q-5 — ruled: the What's term is `SubjectKind`, not `ActorKind`. "Actor" is canon's; "principal" is authority's; "subject" is what OIDC calls the authenticated identity whose claims these are, and the claims are the point. `acts_as` becomes `subject`. §3.7's prose follows.
> Q-6 — ruled as proposed: record the re-pin here; the edits in product-cli and Writ are separate acts in those repositories.
> Q-7 — ruled as proposed: defer the falsifier until T2b's pre-registration is sealed; record it as deferred, not dropped.
> Proceed on the plan once `DDD-dec-63` is revised to the above and filed as ruled.

### Where each ruling landed

| Ruling | Landed in | State |
|---|---|---|
| Identity form, six points | `DDD-dec-63`, rewritten to the ruling | ruled |
| RDFC-1.0, "the decision protocol and Writ already name RDFC-1.0" | `DDD-dec-63` | ruled. The stated premise was checked and is borne out only in part: Varve implements RDFC-1.0 (`Varve.Rdf.RdfCanonicaliser`; `dec:varve/ApplyConvergesDesiredState`), but `spec/decision-provenance/dpp-1.md` on `main` and Hafeok/writ's `docs/` at `6737ac9` do not name it. The ruling does not depend on the premise and stands; the finding is recorded in `DDD-dec-63`'s notes |
| Q-1 §3.7 from `55c9281` | `what.md` §3.7 and the threaded sections; `bootstrap.md` finding 1 | ruled. v1.11.0 was never merged in Hafeok/product-framework; it is adopted here by this ruling |
| Q-2 ontology and shapes from product-cli `schema/` | `applications/sdlc/what/`; the diff between the two copies in `schema-copies.md` | ruled |
| Q-3 no §4–§7 classes; `pf:` ends | the moved ontology carries none; it supersedes charter item 2's second sentence | ruled |
| Q-4 authority profile in its own PR | `plan.md`; successor item | ruled |
| Q-5 `SubjectKind`; `acts_as` becomes `subject` | `what.md` §3.7; the ontology | ruled |
| Q-6 re-pin recorded here | the re-pin decision | ruled |
| Q-7 falsifier deferred, not dropped | `falsifier-t2b.md` | ruled |

### Where the plan landed (after Round 1)

| Plan step | Landed | Commit |
|---|---|---|
| 1 ontology, shapes, example, hash law | `applications/sdlc/what/` (ontology, shapes, example, vectors, check, mint, conformance schemas); `schema-copies.md` | `ce08939` |
| 2 `what.md` | `applications/sdlc/what.md`; `DDD-dec-64` proposed (seven choices the rulings did not make); `how.md` Appendix B corrected by pointer | `0c94c32` |
| 3 supersession of `DDD-dec-55`…`61` | `DDD-dec-65`…`71`; 15 version 2 records; How checker 105 ok, 1 expected warning, 0 failures | `2c4f276` |
| 4 product-cli's re-pin | `DDD-dec-72`, with its target `[PROPOSED]` and the re-pin itself a successor item | `f25c302` |
| 5 falsifier, session record | `falsifier-t2b.md` (deferred, Q-7); `successor-items.md`; this table | this commit |

Charter item 2's second sentence ("The §4 to §7 classes are kept as IRIs the How references,
marked as not authored by any tool") is superseded by Round 1, Q-3. No §4–§7 class is carried.
