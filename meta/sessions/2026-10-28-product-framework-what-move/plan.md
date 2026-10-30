# Plan — the Product Framework What move, 2026-10-28

**Status: approved in Round 1 (2026-10-28) and carried out; the record of where each step landed is
in `rulings.md`.** The text below is the plan as approved, left as written. The questions are
ruled; their answers are in `rulings.md`, and where a ruling differs from the proposed answer the
ruling governs (Q-3, Q-5). Questions Q-1 to Q-7 come from the arrival
findings in `bootstrap.md`; each has the answer Claude proposes.

## Gate 0 — the identity form (this commit)

`DDD-dec-63`, filed unruled. Stop for a ruling. On the ruling, record it verbatim in
`rulings.md` and rewrite `DDD-dec-63` to it before anything else moves.

## Then one PR, in this order

Each step is its own commit with a `Basis:` line, and validators run before each.

| # | Deliverable | Files | Basis |
|---|---|---|---|
| 1 | The ontology and shapes for the §3 subset, under `sdlc:`, in the ruled identity form. The §4–§7 classes are kept as IRIs with an `sdlc:notAuthored` marker. `sdlc-nt/1` hash vectors and a small checker ship with them. This step comes first because `what.md` cites terms that must exist | `applications/sdlc/what/ontology.ttl`, `what/shapes.ttl`, `what/vectors.json`, `what/check.py` | `DDD-dec-63`, `DDD-dec-51` |
| 2 | `what.md`: §3 and §6.3.1 rewritten against the rulings. Covers actors, declared targets, reification and content coverage as obligations, and authoring scopes as grants over element kinds. One worked example runs through it: the How test product's `acme-shop`, extended, never Phoenix | `applications/sdlc/what.md` | `DDD-dec-41`…`DDD-dec-47`, `DDD-dec-57`, `DDD-dec-63` |
| 3 | Supersessions of `DDD-dec-55` to `DDD-dec-61`, anchored to the real identifiers. The How examples' What graph and records get new versions, nothing is edited, and the checker stays green | `DDD-dec-64`… (one per superseded decision); `how-examples/what/`, `records/`, `build.py`, `check.py` | `DDD-dec-55` ruling 4, `DDD-dec-63` |
| 4 | product-cli's re-pin recorded as a decision: its definition names `what.md` at a tag and the sdlc edition, and its v1.9.1 copy is retired | one decision; the edit in product-cli is an act on that repository (Q-6) | `DDD-dec-42` O-6, `DDD-dec-50` |
| 5 | The falsifier run and reported, the session record, and the sessions README row | `falsifier-t2b.md`, `rulings.md`, `meta/sessions/README.md` | `DDD-dec-49`, `DDD-dec-52` |

Step 2's dispositions, so the shape is reviewable now:

| Source | Lands as |
|---|---|
| §3 intro, §3.0, §3.0.1 product, journeys | moves. "Direction (§7.3)" is struck from product-wide concerns, since Delivery is retired |
| §3.1 domain model | structure and reference data move. The production-data paragraphs and the three data-conformance callouts are §13 material, so they are cut to one pointer saying data conformance is an add-on that reads the What (`DDD-dec-44`) |
| §3.2–§3.2.4 events, patterns, UI steps, AIOs, accessibility, page graph | move. Everything that said "the How's reification rules (§4.5)" becomes the reification obligation (`DDD-dec-45`), whose content is binding decisions (`DDD-dec-57`). The "slice = work unit (§5)" callout loses its §5 half. The intent-reliance rate stays, as a What-side signal |
| §3.2.5 system | moves. Target platform contexts, design-system and content-store targets, and locales become the What's target declarations (`DDD-dec-57`). "Deployment identity is How" stays as a pointer to `how.md` |
| §3.3, §3.4 Decider, Projector | move. Their "realisation constraint" callouts become pointers to the binding `PURE` in `how.md` |
| §3.5 named-algorithm primitives | moves, retitled. "Polanyi floor" is not carried as a title, because "floor" is a canon term (risk 1 of the earlier charter) |
| §3.6 quality demands | moves. Kind 2's "binds to the How" becomes "a contract anchors to it" (`how.md` §4.2) |
| §3.7 actors | moves from `55c9281` (Q-1), with the word settled (Q-5) |
| §6.3.1 wire protocol | moves, with the actor block if §3.7 is taken from `55c9281`. The four schemas come with it. `how.md` Appendix B's "not carried" row gets a correcting pointer citing the charter |
| §14 authoring scopes | rewritten as grants over What element kinds, instantiating the genesis grant. Tools are gathering sources whose material enters only as signed decisions (`DDD-dec-43`). The enforcement oracle and the completeness join stay |
| §9, §10 | §9 as cut by `DDD-dec-51` goes into the ontology (step 1), with `anchorsTo` and `supersedes` added. §10 becomes one conformance level: described and in force |

## Questions for Emil

| # | Question | Claude proposes |
|---|---|---|
| Q-1 | §3.7 is not in `c895652`. Which source for actors? | `55c9281` (v1.11.0, the October branch on top of `c895652`), cited as such for §3.7 and its threads through §3.2.0, §3.2.1, §3.3, §3.4 and §6.3.1. Not `adc0220`: that branch also carries Blueprint, DeployableUnit and §7.4 deploy permission, which are How and Delivery |
| Q-2 | The ontology and shapes are in product-cli, in two divergent copies. Which is the source? | `schema/` at product-cli `70395df` (the 399-line ontology), cut to the §3 subset. The `spec/schema/` copy is reported as divergent and not used |
| Q-3 | §4–§7 classes "kept as IRIs": at `pf:` or re-minted under `sdlc:`? | Kept at their `pf:` IRIs (`https://productframework.org/ns#`), declared in the moved ontology as not authored by any tool. Re-minting them under `sdlc:` would put retired classes beside the How vocabulary's live terms, and Writ's decisions already reference the `pf:` IRIs. The §3 classes are minted under `sdlc:`, with `owl:equivalentClass` to their `pf:` IRIs for migration. `UNVERIFIED — Emil review`: who controls `productframework.org` is not known here |
| Q-4 | The genesis grant and the authority profile: in this PR or their own? | Their own PR, after this one. This PR uses them by the definitions ruled in `DDD-dec-46` and `DDD-dec-47`, and the examples keep their test stand-ins. If Emil wants them here, they become step 0 and stop for their own ruling |
| Q-5 | "Actor" collides with the canon term. What is §3.7's word? | `sdlc:ActorKind` kept, defined as "a principal of the specified product", with a note that it is not canon's actor. The alternative is "principal kind", which collides less and matches §3.7's own definition |
| Q-6 | Item 4 is an edit in product-cli, outside this repository | This PR records the re-pin as a decision with the exact target (tag, edition). The edit in product-cli is a separate PR there, only with Emil's go-ahead. Writ's D2.4 sentence ("product-cli owns the `pf:` vocabulary") likewise needs amending in Hafeok/writ |
| Q-7 | Mapping the T2b slice reads varve-demo before T2b's pre-registration is sealed | Map it using only the documents the T2b charter already lets its own session read (varve-demo's README, `docs/spec/script.md`, `docs/adr/`, `docs/decisions/`), and record that the mapping was made before sealing. Or defer the falsifier until T2b is sealed. Claude recommends deferring: a mapping made now is a reading of the slice that the T2b test is meant to make first |

## What this plan does not do

- No How beyond step 3's supersessions.
- No change to `core/claims/` and no pin advance.
- No write to any other repository.
- Nothing merged. Before any merge the PR head is checked against the ratified head.
