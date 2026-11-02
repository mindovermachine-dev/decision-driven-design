# Independent equivalence check (M-3)

Three fresh agents, none of which wrote the text, compared each old document at `e5a332d` with its
rewrite. They were given the old and new texts and the allowed removals, and nothing else. Every
finding is listed with its disposition. "Fixed" means the new text was changed to restore the old
rule; "kept" means the finding was examined and the new text left as it is, with the reason.

## The What pair — 21 findings, 8 example statements

| # | Finding | Disposition |
|---|---|---|
| 1 | Lost: "A system is not a coordinate of any act" | Fixed |
| 2 | Lost: work units, seams and verification as a process retired; the gate is Writ | Fixed; `DDD-dec-54` added to the basis |
| 3 | Lost (borderline): Two Pillars dropped; canon consumed by pin | Kept out of the body: history. `DDD-dec-42` in the basis table |
| 4 | Lost: the `pf:` namespace ends; `pf:` catalogue classes not carried | Fixed, in the reference's "Encoding" |
| 5 | Lost: a UI step is What "owned by product and design" | Fixed |
| 6 | Lost: "The rate is a What-side signal, and stays one" | Fixed |
| 7 | Weakened: "one or more" domains and systems | Fixed |
| 8 | Weakened: "if and only if" became "only if" | Fixed |
| 9 | Weakened: a journey is a "product-level, derived composition: a declared path" | Fixed |
| 10 | Changed: "declared ground, over which decisions are made"; step 1 reads "addresses" | Fixed |
| 11 | Changed: "would disagree" became "may differ" | Fixed |
| 12 | Changed: "monotonically" became "steadily" | Fixed |
| 13 | Changed: "not a check this tool requires" | Fixed: "not a check the What's own checker requires", in both documents |
| 14 | Changed: a catalogue is in a "package" | Fixed: "a package: a product of its own" |
| 15 | Changed: outside-scope routes "to a sanctioned author" | Fixed in substance: "routed to a sanctioned source, and through it to a person who can accept it". The old text's own §5.2 renamed authoring tools to sources under `DDD-dec-43`; "author" survives as the accepting person |
| 16 | Decided point marked unsettled: "in force" cannot be claimed until the authority profile exists | Fixed: stated as decided, and removed from "Not settled yet" |
| 17 | Decided allocation marked unsettled: how attestations are held is the profile's | Fixed: removed from "Not settled yet" |
| 18 | New: "the graph's name is not hashed" | Kept: ruled, `DDD-dec-73`, now cited for it |
| 19 | New: genesis "held by the person who brought the product into being" | Fixed: "or by whoever it has since been transferred to"; basis `DDD-dec-46` |
| 20 | New: delegation "directly or through others" | Kept, reworded to `DDD-dec-46`'s "directly or through a chain" |
| 21 | Widened: the open question on adopter-registered AIOs | Kept: the old text itself identified it with how.md's open question, which is about What kinds in general |
| W1 | Wrong: "staff refund them" | Fixed: customers ask for refunds; staff see every order |
| W2 | Wrong: a change to "refund within paid" anchors to `Order` | Fixed: it anchors to the invariant |
| W3 | Wrong: `Cancel order` anchors to the `Ordering` domain | Fixed: the `Ordering` bounded context |
| W4 | Incomplete: `Order` has three invariants | Fixed |
| W5 | Wrong: Acme Shop targets iOS and Android | Fixed: a general illustration, with a note that `shop-bff` targets the web only |
| W6 | "44 elements" is 45 with the product node | Fixed: "44 elements under the product node" |
| W7, W8 | Verifiable from the How records, not the What file | Kept: correct |

## The five small documents — 27 findings

| Finding | Disposition |
|---|---|
| F1.1, F1.2, F1.3 `applications/README.md`: "states it again" contradicted "not a restatement"; the self-prescribed structure lost; the actor framing lost | Fixed |
| F1.4 the "agentic design framework" characterisation | Fixed |
| F1.5 "every document lists unsettled points" was untrue | Fixed: "a document that has any lists them" |
| F2.1 org-03 falsifier "or" became "and" | Fixed. Serious: it made the claim harder to refute |
| F2.2 the org-01 summary read as praising presenting guesses as facts | Fixed |
| F2.3 summaries stated predictions as facts | Fixed: each summary now opens "The prediction:" |
| F2.4 "status floors" weakened to marking | Fixed |
| F2.5 "manifests" glossed without basis | Fixed: glossed by the manifest definition in `projections/README.md` |
| F2.6 "most organisations" | Fixed: "organisations" |
| F2.7 the reversal-cost comparison lost | Fixed |
| F2.8 "and nothing records it" added | Fixed: removed |
| F2.9 headings stronger than the claims | Fixed |
| F2.10 the promotion criterion lost "core-like" and "repository" | Fixed |
| F2.11 "session-authored" | Fixed in the basis table |
| F3.1 `sdlc/README.md`: a definition of the principle without its canonical limits | Fixed: removed. Serious |
| F3.2 "poisonable centre" became "can poison" | Fixed. Serious |
| F3.3 product-cli's "reference implementation" status lost | Fixed |
| F3.4 the assessment of the removed design documents lost | Fixed |
| F3.5 mapping-table wording drift | Fixed |
| F3.6 shortened index descriptions | Kept: each is stated in the target document |
| F3.7 two new statements | Kept: both supported by `how.md` |
| F4.1 `how-examples/README.md`: "test stand-in for the unwritten profile" became "the checker does not yet implement" | Fixed. Serious |
| F4.2 "Kind 2" lost from the residency anchor | Fixed |
| F4.3 the 21/15 breakdown lost | Fixed: the earlier breakdown stated; two records added since |
| F4.4 "discards them" lost | Fixed |
| F4.5 three additions | Kept: each verified against `check.py` and the records |
| F4.6 wording drift (`@1`, "edition") | Fixed |
| F5.1 `production-as-ground.md`: "reported, partially" and "is real" lost | Fixed |
| F5.2 "is not accepted" stronger than "should not be treated as settled" | Fixed |
| F5.3 "a guide, not a proof" | Fixed: the old wording |

## The How pair

Pending at this commit.

## What this says about the rewrite

The checks found 48 points across the two sets, and 5 the small-documents check called serious.
Almost all are the same failure: a rule restated in plainer words lost a qualifier ("if and only
if", "or", "poisonable", "core-like") or gained one. Plain prose made these slips easy to write;
the independent check made them easy to find. The equivalence tables written alongside the rewrite
marked every one of these rows "same". They are not evidence of equivalence by themselves.
