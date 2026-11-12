---
name: product-definition
slot: source
status: trial
schema: 1
tracking: mindovermachine-dev/decision-driven-design#75
read-from: applications/sdlc/product-cli/product-definition.md
read-at: 84aa4665b4b0392ef4bb08ac042e42ae9fc6d12c
read-blob: 8019dc03ce2e4083bcfafbe8b6625f7fae901b24
covers: [introduction, chapter 1, chapter 5]
---

<!--
TRIAL. This file defines nothing. The definition is product-definition.md, unchanged and in
force (D1.24). This file tests the source convention of issue #75.

Schema 1 [PROPOSED], after Emil's direction of 2026-11-12: a source has the shape of any written
document. It is a headline, an introduction, and chapters with headlines, in order. Chapters hold
sections with headlines, in order. Anything further is built on top of that shape.

  #    the document's headline
  ##   a chapter's headline, numbered in reading order
  ###  a section's headline, led by its identifier
  **Introduction.**  the introduction of the document or of a chapter
  - **ID** text {field: value | field: value}   one statement, one proposition

Order is content: a document is read from the top, and later parts build on earlier ones.
An introduction says what the part beneath it is for.
Fields built on top so far: basis (rulings), depends-on (statements), refs (as the definition
writes them, unchecked), note (flags for review).

The wording is the definition's. Sentences are split and pronouns resolved. Nothing is added.
W1 to W12 and D1.n are the definition's identifiers. All other identifiers are minted here.
-->

# Product: product definition

**Introduction.**

- **I0.1** This is the definition of the rewritten product-cli.
- **I0.2** The rewritten product-cli replaces the Rust workspace of the same name.
- **I0.3** The definition is written outside-in: the promise first, the implementation last.
- **I0.4** Chapters 1 to 6 are the product.
- **I0.5** Chapter 7 is how the product happens to be built, and may change without the product changing.

## 1. The promise

**Introduction.**

- **P0.1** The product is a machine-checkable statement of what a product does, with an executable oracle for its behaviour, exported as one graph that someone else can sign.
- **P0.2** Four consequences follow from the promise and are the whole product.
- **P0.3** Everything below the promise is how.

### P1 The What is authored in conversation, and every step of it is a decision.

- **P1.1** An agent proposes. {basis: D1.10}
- **P1.2** The author watches the graph, its findings and its open questions change live. {basis: D1.10}
- **P1.3** The author adopts or rejects each proposal. {basis: D1.10}
- **P1.4** Each adoption is a `dpp/1` decision record with its reason. {basis: D1.10 | refs: dpp/1}
- **P1.5** Specification moves at the speed of the conversation. {basis: D1.10 | depends-on: P1.4}
- **P1.6** Every element of the What traces to the person who adopted it. {basis: D1.10 | depends-on: P1.4}

### P2 The What is a graph with shapes, never prose with diagrams.

- **P2.1** Anything that cannot be stated as a node, an edge or a shape is not yet specified.
- **P2.2** The tool says that such a thing is not yet specified, rather than accepting it.

### P3 Behaviour is executable before any code exists.

- **P3.1** A Decider and a Projector are simulated sound and complete against scenarios drawn from the flows.
- **P3.2** The same scenarios later judge realised code through a wire protocol the tool implements.

### P4 The tool puts nothing in force and decides nothing about realisation.

- **P4.1** The tool records the author's decisions over the What as `dpp/1` records. {basis: D1.11 | refs: dpp/1}
- **P4.2** By the tool's profile, those records carry no force. {basis: D1.11}
- **P4.3** The tool produces a canonical document. {basis: D1.11 | note: UNVERIFIED — Emil review. The definition places the D1.11 marker before P4.1. Whether the ruling extends to P4.3 and P4.4 is read from position, not stated.}
- **P4.4** What the canonical document is held against, who accepts it under which grant, and from which position it is in force, belong to Writ. {basis: D1.11 | note: UNVERIFIED — Emil review. Same question of extent as P4.3.}

## 5. The guarantees

**Introduction.**

- **W0.1** Each guarantee is a property test over generated What graphs and scenarios.
- **W0.2** The suite of property tests is public.
- **W0.3** Every test observes bytes, in the draft log or in an export, never the return value of the verb that produced them.
- **W0.4** W1 and W5 are the edition's violations. {basis: D1.19 | refs: DDD-dec-113}
- **W0.5** W3 and W4 are the edition's warnings. {basis: D1.19 | refs: DDD-dec-113}
- **W0.6** The checks themselves are the edition's shapes, not code in this tool. {basis: D1.19}

### W1 Shape before storage.

- **W1.1** No change set enters the draft log if it carries a violation.
- **W1.2** A failed write leaves the log unchanged.

### W2 Derived, not declared.

- **W2.1** A Decider's signature (the commands it handles, the events it may emit, the state it evolves) is computed from the graph.
- **W2.2** A Projector's signature (the events it folds, the fields it may produce) is computed from the graph.
- **W2.3** An authored signature, or logic, that disagrees with the computed signature is refused.

### W3 Coverage.

- **W3.0** Each coverage gap is a finding, never a silent pass.
- **W3.1** Every command targeting an aggregate is handled by its Decider.
- **W3.2** Every event a Projector's View projects is folded by it.
- **W3.3** Every (command, subject kind) pair, from a step's `sdlc:offeredTo` or a trigger's `sdlc:subject`, has a scenario showing acceptance or a reachable rejection.
- **W3.4** Every View a step surfaces has a scope rule for every subject kind the step is offered to, or is public.
- **W3.5** Every automated or external trigger acts as a subject kind (`sdlc:subject`). {basis: D1.4, D1.18}
- **W3.6** A user trigger's subject comes from the step's `sdlc:offeredTo`. {basis: D1.4, D1.18 | refs: what.md §3.7}

### W4 Justification.

- **W4.0** Orphans are findings.
- **W4.1** Every aggregate field is read by some Decider.
- **W4.2** Every projected field is consumed by some step.
- **W4.3** Every claim is read by some Decider or compared by a scope key.
- **W4.4** Every Decider has a reachable rejection.

### W5 Type boundary.

- **W5.0** Each type-boundary breach is refused at write, not reported later.
- **W5.1** A UI step references only AIOs, never concrete controls.
- **W5.2** A trigger's `sdlc:subject`, when present, names a subject kind whose nature matches the trigger's `source`. {basis: D1.4, D1.18}
- **W5.3** An absent subject on a trigger is accepted. {basis: D1.4, D1.18}
- **W5.4** An absent subject is reported under W3 when the trigger is automated or external. {basis: D1.4, D1.18}
- **W5.5** A What without subjects exports byte-identically. {basis: D1.4, D1.18 | depends-on: W5.3}
- **W5.6** A journey crosses systems only through a Translation.

### W6 Simulation before realisation.

- **W6.1** Every Decider and Projector with scenarios is simulated sound and complete before an export is marked ready.
- **W6.2** A What with a failing scenario exports, but says so in its What-version record.

### W7 Canonical export.

- **W7.1** Two exports of the same draft position are byte-identical, on every platform, graph and logic artefacts alike.
- **W7.2** Canonicalisation happens once, before any exporter runs.
- **W7.3** Every derived export is a deterministic function of the canonical graph and artefacts.
- **W7.4** The record of every derived export names the canonical graph's canonical hash.

### W8 Round-trip.

- **W8.1** Importing a canonical export yields a draft whose export is byte-identical to the input, graph and artefacts.

### W9 Phase order.

- **W9.1** An agent session cannot author a node before the nodes it derives from exist.
- **W9.2** The gate is the session transport, not advice in a prompt.

### W10 Nothing in force, nothing landed.

- **W10.1** The tool holds no key and no grant. {basis: D1.11}
- **W10.2** The tool puts nothing in force. {basis: D1.11}
- **W10.3** The tool knows no Writ position. {basis: D1.11}
- **W10.4** The tool writes to no log but its own draft log. {basis: D1.11}
- **W10.5** The tool's decision records carry no force by its profile. {basis: D1.11}
- **W10.6** Exporters produce documents only. {basis: D1.11}

### W11 Decision-provenance conformant.

- **W11.1** The draft log is a conformant system under `dpp/1` §8, at specification 1.0. {basis: D1.12 | refs: dpp/1 §8}
- **W11.2** The draft log's conformance is checked by the `dpp/1` conformance suite. {basis: D1.12 | refs: dpp/1 Appendix C}
- **W11.3** Every record the draft log exposes is conformant. {basis: D1.12 | refs: dpp/1 §3.6}
- **W11.4** Every record the draft log exposes has a non-empty `why`. {basis: D1.12}
- **W11.5** Every record the draft log exposes has `system` equal to the draft log's identifier. {basis: D1.12}
- **W11.6** No hashed content changes under a published triple. {basis: D1.12 | refs: dpp/1 §3.8}
- **W11.7** No version is reused. {basis: D1.12 | refs: dpp/1 §3.8}
- **W11.8** Records the draft log no longer holds answer "not held". {basis: D1.12 | refs: dpp/1 §6.8}
- **W11.9** The export's What-version record rests on every decision in force. {basis: D1.12, D1.17}
- **W11.10** A Writ decision that lands the export, by naming it in its `basedOn`, reaches each author decision and each agent proposal by the walk of `dpp/1` §7 alone. {basis: D1.12 | depends-on: W11.9 | refs: dpp/1 §7}

### W12 Nothing an agent wrote is in the What unless a person adopted it.

- **W12.1** Every change at the head of the draft log is attached to a decision record whose `by` is the author. {basis: D1.12}
- **W12.2** That decision record is either an adoption of a proposal, or the author's own write. {basis: D1.12}
- **W12.3** A proposal never reaches the head on its own. {basis: D1.12}
- **W12.4** The agent surface has no verb that adopts. {basis: D1.12}

## Appendix. Rulings cited

A ruling is not a statement. Its content is the statements that name it in `basis`.

| Ruling | Date | Relation |
|---|---|---|
| D1.4 | 2026-10-30 | amended by D1.18 and D1.21 |
| D1.10 | 2026-10-30 | |
| D1.11 | 2026-10-30 | |
| D1.12 | 2026-10-30 | |
| D1.17 | 2026-11-03 | supersedes D1.14 |
| D1.18 | 2026-11-03 | |
| D1.19 | 2026-11-03 | |
