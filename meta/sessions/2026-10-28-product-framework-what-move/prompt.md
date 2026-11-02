# Prompt — the Product Framework What move, 2026-10-28

The session's charter, verbatim, as Emil gave it. Per `DDD-dec-20`, committed before any canon
edit so the session's scope is fixed at arrival. It supersedes, as this session's charter, the
unmerged move charter at `claude/product-framework-move-2026-10-27` (`38a84d8`), which was
Claude's drafting and never ran.

---

Charter: move the What into `applications/sdlc/` and settle its identity form
PR #39 recorded the rulings for the move (`DDD-dec-41` to `DDD-dec-53`, plus the rulings of 2026-10-27 filed under the How branch and merged in #41) but moved no text. This session does the move. `main` is the base; branch from it after confirming #41 is in.
Read first. `meta/sessions/2026-10-27-product-framework-what/` in full, including `rulings.md`. `applications/sdlc/how.md`, `how-vocabulary.md` and `DDD-dec-54` to `DDD-dec-62`. The source: github.com/Hafeok/product-framework at `c895652` (v1.10.0), `docs/product-framework.md`. Then produce the plan below and wait for approval before moving a line.
Already ruled; do not reopen: only the What moves (§3 and the §6.3.1 wire protocol); How and Delivery are retired; home is `applications/sdlc/`; Two Pillars conformance is dropped; every decision anchors to a What element or to the product; tools never change the What and everything gathered is signed by a human principal; the design system and content store are targets declared by the What, their catalogues are packages, and the AIO-to-CIO and key-to-string bindings are How decisions; data conformance (§13) is not framework; authoring scopes (§14) are central and instantiate the genesis grant over a product; the genesis grant and the authority profile are defined in `applications/sdlc/`, not upstream; reification and content obligations move in as obligations, their content as decisions; the protocol token is `dpp/1`.
The identity form is the first deliverable, and nothing else is written until it is ruled. Propose how a What element is identified: the IRI scheme under the product's namespace, what is stable across renames (the element's identity must survive a rename so Writ's baselines do), how a version of the What is identified (the graph content hash plus the authored Decider and Projector logic, as §7.3.1 had it, or something better), and how a `dpp/1` record for a What-version references the elements it contains. Put the proposal in a decision, file it unruled, and stop for a ruling.
Then, in one PR:

1. Move §3 and §6.3.1 into `applications/sdlc/what.md`, rewritten against the rulings: no How, no Delivery, no Two Pillars; actors (§3.7) included; the design system and content store as declared targets; reification and content coverage as obligations on the What; authoring scopes as the instantiation of grants over What element kinds. Quote the source where its text is right; do not copy sections the rulings retired.
2. Move the ontology and the shapes for the §3 subset, under the sdlc namespace and the ruled identity form. The §4 to §7 classes are kept as IRIs the How references, marked as not authored by any tool.
3. Supersede `DDD-dec-55` to `DDD-dec-61` with versions anchored to the real identifiers, per ruling 4 of 2026-10-28. Until this step is done those decisions bind the How test product only; after it, the How examples are rebuilt against the landed What and the checker must stay green.
4. Record product-cli's re-pin (ruling 6): the tool's definition names the moved What and the sdlc edition; the v1.9.1 copy it holds is retired.
5. Session record under `meta/sessions/2026-10-28-product-framework-what-move/`; every ruling verbatim; decisions numbered from 63 (`DDD-dec-62` is taken by the token ruling, merged in #41); `Basis:` lines; validators passing; the How checker passing; nothing merged. Emil ratifies by merging.

Falsifier to carry. Map the T2b slice using only What constructs under the reworded reading: a step fails only if it has neither a What element nor a decision that declares it; a verdict is a valuation and is expected to have no stored What form. Report the result either way.
Discipline. Claude proposes; Emil rules; record rulings when given. Change ruled material by supersession, never by rewriting. Check the PR head against the ratified head before any merge. Commits carry `Basis:` and the session trailer, no model identifiers in any record.
