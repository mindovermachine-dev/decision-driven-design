# Prompt — the Product Framework How, 2026-10-27

The session's charter, verbatim, as Emil gave it. Per `DDD-dec-20`, committed before any canon
edit so the session's scope is fixed at arrival.

---

Charter: the How, as decisions (2026-10-27)
The What has moved into `applications/sdlc/` (PR #39, `DDD-dec-41` to `DDD-dec-44`, plus the rulings of 2026-10-27 on reification and content obligations, the genesis grant over a product, the authority profile, and the protocol token). The How (§4 to §6 of the old Product Framework) and Delivery (§7) were retired by `DDD-dec-41`. This session specifies the How anew, in `applications/sdlc/`, as the thing the old sections were describing from the outside.
The thesis to test, not to assume. The How is not a description of a realisation. It is a set of decisions: each anchored to a What element or to the product, accepted under the product’s genesis, held against code and deployments by a gate, shipped as a package by a vendor, and imported into another product by `basedOn` under that product’s genesis. What Context& ships is the How. If this thesis fails against the material below, say where and propose what replaces it.
Already ruled; do not reopen:

* A How decision anchors to exactly one What element or to the product. Anchoring to the product is the degenerate case an empty What forces (a repository with no What is a product whose What is empty), not a loophole.
* Every change to the What or the How is a decision; tools never change either; everything gathered is signed by a human principal.
* A package is a product with its own genesis, held by the vendor. In another product’s space it is provenance, never authority: its decisions enter by import, `basedOn` the package’s versions, and are in force only under the importing product’s acceptances.
* Force comes from the authority profile (genesis, grants, scopes, acceptance, baseline, waiver). The How does not redefine any of it.
* The gate is Writ. The How states what Writ enforces; it does not restate Writ’s verbs, positions, partitions or guarantees.
* The protocol token is whichever was ruled on 2026-10-27; records use it.

Proposal to evaluate: three kinds of How decision.

1. Constraint: a decision with a violation description over code facts (layers, references, visibility, public API, names, banned APIs, secrets). The old layout model (§4.3) is a constraint with a particular evaluator and allowlist semantics; “no orphans” is the baseline reading, where everything not covered is a violation until a decision covers it.
2. Realisation: a decision binding a What element to a shape in a target (a Decider to a pure core; a Command to a canonical route; an AIO in a context to a CIO; a content key in a locale to a string). This collapses the old §4.2’s “pure core”, §4.4, §4.5, §4.6 and §5.2 into one kind. A target is a language or a design system or a content store, each with a named realisation vocabulary and projector or reporter edition.
3. Contract: a decision over a deployable unit rather than over code (application contract, infrastructure and runtime contract, deployment identity, data residency, the §3.6 Kind-2 architectural demands). Facts come from a reporter over the deployment, not a projector over the repository.

Determine whether a fourth kind is needed (the old §4.1 “principle” licensed by a “top decision” is the candidate; the proposal says it is a decision that other decisions are `basedOn`, not a kind) and whether any of the three should split.
Questions to rule, with the proposal’s answer stated so you can disagree:

* What a package contains. Proposal: decisions; realisation vocabularies; projector and reporter editions named by the decisions; nothing else. Analyzers and code that make decisions checkable ship with the package but are its realisation, not its content. Does a package carry a What of its own? Proposal: only the element kinds it binds to, never instances.
* Specified once, realised per target. Proposal: every decision is stated in the How vocabulary with no language in it, and every language-specific shape is a realisation under a named vocabulary edition; C# is the first target and the second must be expressible without touching a decision. Check this against the layer rule, the pure-core rule and the REST projection: write each once and show two targets.
* Realisation coverage. The old §4.5 required a reification for every (AIO, context) pair a system can reach. Proposal: generalise to every kind: for every What element of a kind a package binds, in every target the product declares, a realisation exists or a declared gap exists, and the gate reports the gap. Is “declared gap” a waiver, a baseline entry, or a third thing? Proposal: a baseline entry on the realisation decision, so it shrinks under the ratchet.
* Supersession across the import. When a package supersedes a decision, what does the importing product see, and what must it do? Proposal: `explain` shows “rests on superseded version”; nothing is forced; re-import is a landing plus acceptance under the importer’s genesis. State whether a package may declare a version as withdrawn (unsafe to rest on) and what that obliges.
* Contracts and reporters. Which facts about a deployment are the gate allowed to rely on, with what provenance, and what is an open question rather than a violation when a reporter is absent?
* What the How says about generation. The old §5.2 generated verification shells from the oracle. Proposal: out of scope for this session; generation is an open question in Writ’s definition (“can realisations generate as well as check”) and is decided by evidence later. Confirm or argue it in.

Deliverables:

* `applications/sdlc/how.md`: scope and non-goals; the kinds with their anchors, facts, provenance and evaluators; the package; import and supersession; coverage and gaps; conformance (what a product claims when it says its How is specified); a decisions appendix recording every departure from the proposal with reasons.
* The How vocabulary as a list of terms with definitions, under the sdlc namespace, each mapped to a protocol record shape.
* Three worked decisions, one per kind, each written once and shown realised in two targets, with the What element or product it anchors to, and its acceptance under a test genesis.
* A session record under `meta/sessions/` as for the What session; decisions numbered from the next free id after checking upstream; `Basis:` lines; validators passing; nothing merged (Emil ratifies).

Discipline: Claude proposes; Emil rules; record rulings verbatim when given. Change ruled material by supersession. The old §4 to §7 text is input to read and may be quoted; it is not authority, and “it was like that in v1.10” is not a reason.
