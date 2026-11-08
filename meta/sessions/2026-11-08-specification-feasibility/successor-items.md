# Successor items — specification feasibility, 2026-11-08

Work this session's decisions require and did not do. Each is its own session, and each is a
proposal until Emil rules on it.

| # | Item | Rests on | Where |
|---|---|---|---|
| S-1 | The What: a ground-sourced bounded context (its source, its edition, its `basedOn` vetting); the admission element within a system; the admission check over Deciders, Projectors and Views; the permission check, with `Unknown` on an unresolved reference | DDD-dec-116 F-8 to F-12 | `what.md` §3.1, §3.7, a new section; `what/ontology.ttl`, `what/shapes.ttl`; an example graph. A new edition, not an edit of edition 1 (DDD-dec-113 E-6: read-forever) |
| S-2 | The three loose-coupling conditions as How kinds, with a worked example of each | DDD-dec-116 F-2 | `how.md` §4, `how-examples/` |
| S-3 | product-cli: the unvetted state of a pinned What change, the vetting decision, staleness by pin, projected against reported | DDD-dec-116 F-3, F-4, F-6 | `applications/sdlc/product-cli/product-definition.md`, then the product-cli repository |
| S-4 | product-cli's grants and roles; mark `[D1.11]` superseded by DDD-dec-117 in §1, W10 and §8 | DDD-dec-117 | `product-definition.md`; the product-cli repository (from `rust-final`'s ledger and scope code, as input only) |
| S-5 | The authority profile: scopes over decision kinds; roles as named, evaluated scopes; amend Appendix B's roles row with a pointer to DDD-dec-117 | DDD-dec-117 | `authority.md` §3.1, Appendix B; `authority-vocabulary.md`; `What` §5.1 |
| S-6 | Answer O-1: whose What holds a ground-sourced context when the source belongs to no product (DDD-dec-113 Q-C2) | rulings.md O-1 | a ruling |
| S-7 | Answer O-2: whether owners and roles come from the Decision-Driven Organisations grant map | rulings.md O-2 | a ruling; `applications/organizations/` |
| S-8 | Sequence S-1 with the unlanded `2026-11-07-sdlc-and-pdlc` branch | findings.md F-d | — |
