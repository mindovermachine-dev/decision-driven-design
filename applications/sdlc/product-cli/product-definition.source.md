---
name: product-definition
slot: source
status: trial
schema: 0
tracking: mindovermachine-dev/decision-driven-design#75
read-from: applications/sdlc/product-cli/product-definition.md
read-at: 84aa4665b4b0392ef4bb08ac042e42ae9fc6d12c
read-blob: 8019dc03ce2e4083bcfafbe8b6625f7fae901b24
covers: [chapter 1, chapter 5]
---

# Product definition: source statements (trial)

**This file is a trial and defines nothing.** The definition is `product-definition.md`, which is unchanged and in force (`D1.24`). This file tests whether that definition can be held as ID'd statements, from which other files are derived (issue #75).

How to read it:

- Each fenced block is YAML. Each entry is one statement.
- The wording is the definition's. Sentences are split and pronouns resolved. Nothing is added.
- `W1` to `W12` and `D1.n` are the definition's own identifiers. Every other identifier is minted here and is `[PROPOSED]`.
- `refs` are carried as the definition writes them. They were not checked against their targets.
- Schema 0 is `[PROPOSED]`. It is separate from claim format version 1 (`spec/claim-format.md`), by Emil's ruling of 2026-11-11.

## Schema 0

| Field | Meaning |
|---|---|
| `id` | Stable identifier. Never reused. |
| `kind` | `promise`, `guarantee` or `ruling` in this trial. |
| `title` | The name of a group. Present on group entries only. |
| `text` | One proposition. |
| `basis` | The rulings the statement rests on. |
| `follows-from` | The statements this one is a consequence of. It is not independent of them. |
| `refs` | References outside this definition, as written there. |
| `note` | Anything flagged for review. |

## Rulings cited

A ruling is not a statement. Its content is the statements that cite it in `basis`. This block holds only what the definition says about the ruling itself.

```yaml
- {id: D1.4,  kind: ruling, date: 2026-10-30, amended-by: [D1.18, D1.21]}
- {id: D1.10, kind: ruling, date: 2026-10-30}
- {id: D1.11, kind: ruling, date: 2026-10-30}
- {id: D1.12, kind: ruling, date: 2026-10-30}
- {id: D1.17, kind: ruling, date: 2026-11-03, supersedes: [D1.14]}
- {id: D1.18, kind: ruling, date: 2026-11-03}
- {id: D1.19, kind: ruling, date: 2026-11-03}
```

## Chapter 1. The promise

```yaml
- id: P0
  kind: promise
  title: The promise
- id: P0.1
  kind: promise
  text: >-
    The product is a machine-checkable statement of what a product does, with an executable
    oracle for its behaviour, exported as one graph that someone else can sign.
- id: P0.2
  kind: promise
  text: Four consequences follow from the promise and are the whole product.

- id: P1
  kind: promise
  title: The What is authored in conversation, and every step of it is a decision.
  basis: [D1.10]
- id: P1.1
  kind: promise
  text: An agent proposes.
  basis: [D1.10]
- id: P1.2
  kind: promise
  text: The author watches the graph, its findings and its open questions change live.
  basis: [D1.10]
- id: P1.3
  kind: promise
  text: The author adopts or rejects each proposal.
  basis: [D1.10]
- id: P1.4
  kind: promise
  text: Each adoption is a `dpp/1` decision record with its reason.
  basis: [D1.10]
  refs: [dpp/1]
- id: P1.5
  kind: promise
  text: Specification moves at the speed of the conversation.
  basis: [D1.10]
  follows-from: [P1.4]
- id: P1.6
  kind: promise
  text: Every element of the What traces to the person who adopted it.
  basis: [D1.10]
  follows-from: [P1.4]

- id: P2
  kind: promise
  title: The What is a graph with shapes, never prose with diagrams.
- id: P2.1
  kind: promise
  text: Anything that cannot be stated as a node, an edge or a shape is not yet specified.
- id: P2.2
  kind: promise
  text: The tool says that such a thing is not yet specified, rather than accepting it.

- id: P3
  kind: promise
  title: Behaviour is executable before any code exists.
- id: P3.1
  kind: promise
  text: >-
    A Decider and a Projector are simulated sound and complete against scenarios drawn from
    the flows.
- id: P3.2
  kind: promise
  text: >-
    The same scenarios later judge realised code through a wire protocol the tool implements.

- id: P4
  kind: promise
  title: The tool puts nothing in force and decides nothing about realisation.
- id: P4.1
  kind: promise
  text: The tool records the author's decisions over the What as `dpp/1` records.
  basis: [D1.11]
  refs: [dpp/1]
- id: P4.2
  kind: promise
  text: By the tool's profile, those records carry no force.
  basis: [D1.11]
- id: P4.3
  kind: promise
  text: The tool produces a canonical document.
  basis: [D1.11]
  note: >-
    UNVERIFIED — Emil review. The definition places the D1.11 marker before P4.1. Whether the
    ruling extends to P4.3 and P4.4 is read from position, not stated.
- id: P4.4
  kind: promise
  text: >-
    What the canonical document is held against, who accepts it under which grant, and from
    which position it is in force, belong to Writ.
  basis: [D1.11]
  note: UNVERIFIED — Emil review. Same question of extent as P4.3.
```

## Chapter 5. The guarantees

```yaml
- id: W0
  kind: guarantee
  title: What holds for every guarantee
- id: W0.1
  kind: guarantee
  text: Each guarantee is a property test over generated What graphs and scenarios.
- id: W0.2
  kind: guarantee
  text: The suite of property tests is public.
- id: W0.3
  kind: guarantee
  text: >-
    Every test observes bytes, in the draft log or in an export, never the return value of
    the verb that produced them.
- id: W0.4
  kind: guarantee
  text: W1 and W5 are the edition's violations.
  basis: [D1.19]
  refs: [DDD-dec-113]
- id: W0.5
  kind: guarantee
  text: W3 and W4 are the edition's warnings.
  basis: [D1.19]
  refs: [DDD-dec-113]
- id: W0.6
  kind: guarantee
  text: The checks themselves are the edition's shapes, not code in this tool.
  basis: [D1.19]

- id: W1
  kind: guarantee
  title: Shape before storage.
- id: W1.1
  kind: guarantee
  text: No change set enters the draft log if it carries a violation.
- id: W1.2
  kind: guarantee
  text: A failed write leaves the log unchanged.

- id: W2
  kind: guarantee
  title: Derived, not declared.
- id: W2.1
  kind: guarantee
  text: >-
    A Decider's signature (the commands it handles, the events it may emit, the state it
    evolves) is computed from the graph.
- id: W2.2
  kind: guarantee
  text: >-
    A Projector's signature (the events it folds, the fields it may produce) is computed from
    the graph.
- id: W2.3
  kind: guarantee
  text: An authored signature, or logic, that disagrees with the computed signature is refused.

- id: W3
  kind: guarantee
  title: Coverage.
- id: W3.0
  kind: guarantee
  text: Each coverage gap is a finding, never a silent pass.
- id: W3.1
  kind: guarantee
  text: Every command targeting an aggregate is handled by its Decider.
- id: W3.2
  kind: guarantee
  text: Every event a Projector's View projects is folded by it.
- id: W3.3
  kind: guarantee
  text: >-
    Every (command, subject kind) pair, from a step's `sdlc:offeredTo` or a trigger's
    `sdlc:subject`, has a scenario showing acceptance or a reachable rejection.
- id: W3.4
  kind: guarantee
  text: >-
    Every View a step surfaces has a scope rule for every subject kind the step is offered
    to, or is public.
- id: W3.5
  kind: guarantee
  text: Every automated or external trigger acts as a subject kind (`sdlc:subject`).
  basis: [D1.4, D1.18]
- id: W3.6
  kind: guarantee
  text: A user trigger's subject comes from the step's `sdlc:offeredTo`.
  basis: [D1.4, D1.18]
  refs: [what.md §3.7]

- id: W4
  kind: guarantee
  title: Justification.
- id: W4.0
  kind: guarantee
  text: Orphans are findings.
- id: W4.1
  kind: guarantee
  text: Every aggregate field is read by some Decider.
- id: W4.2
  kind: guarantee
  text: Every projected field is consumed by some step.
- id: W4.3
  kind: guarantee
  text: Every claim is read by some Decider or compared by a scope key.
- id: W4.4
  kind: guarantee
  text: Every Decider has a reachable rejection.

- id: W5
  kind: guarantee
  title: Type boundary.
- id: W5.0
  kind: guarantee
  text: Each type-boundary breach is refused at write, not reported later.
- id: W5.1
  kind: guarantee
  text: A UI step references only AIOs, never concrete controls.
- id: W5.2
  kind: guarantee
  text: >-
    A trigger's `sdlc:subject`, when present, names a subject kind whose nature matches the
    trigger's `source`.
  basis: [D1.4, D1.18]
- id: W5.3
  kind: guarantee
  text: An absent subject on a trigger is accepted.
  basis: [D1.4, D1.18]
- id: W5.4
  kind: guarantee
  text: An absent subject is reported under W3 when the trigger is automated or external.
  basis: [D1.4, D1.18]
- id: W5.5
  kind: guarantee
  text: A What without subjects exports byte-identically.
  basis: [D1.4, D1.18]
  follows-from: [W5.3]
- id: W5.6
  kind: guarantee
  text: A journey crosses systems only through a Translation.

- id: W6
  kind: guarantee
  title: Simulation before realisation.
- id: W6.1
  kind: guarantee
  text: >-
    Every Decider and Projector with scenarios is simulated sound and complete before an
    export is marked ready.
- id: W6.2
  kind: guarantee
  text: A What with a failing scenario exports, but says so in its What-version record.

- id: W7
  kind: guarantee
  title: Canonical export.
- id: W7.1
  kind: guarantee
  text: >-
    Two exports of the same draft position are byte-identical, on every platform, graph and
    logic artefacts alike.
- id: W7.2
  kind: guarantee
  text: Canonicalisation happens once, before any exporter runs.
- id: W7.3
  kind: guarantee
  text: Every derived export is a deterministic function of the canonical graph and artefacts.
- id: W7.4
  kind: guarantee
  text: The record of every derived export names the canonical graph's canonical hash.

- id: W8
  kind: guarantee
  title: Round-trip.
- id: W8.1
  kind: guarantee
  text: >-
    Importing a canonical export yields a draft whose export is byte-identical to the input,
    graph and artefacts.

- id: W9
  kind: guarantee
  title: Phase order.
- id: W9.1
  kind: guarantee
  text: An agent session cannot author a node before the nodes it derives from exist.
- id: W9.2
  kind: guarantee
  text: The gate is the session transport, not advice in a prompt.

- id: W10
  kind: guarantee
  title: Nothing in force, nothing landed.
  basis: [D1.11]
- id: W10.1
  kind: guarantee
  text: The tool holds no key and no grant.
  basis: [D1.11]
- id: W10.2
  kind: guarantee
  text: The tool puts nothing in force.
  basis: [D1.11]
- id: W10.3
  kind: guarantee
  text: The tool knows no Writ position.
  basis: [D1.11]
- id: W10.4
  kind: guarantee
  text: The tool writes to no log but its own draft log.
  basis: [D1.11]
- id: W10.5
  kind: guarantee
  text: The tool's decision records carry no force by its profile.
  basis: [D1.11]
- id: W10.6
  kind: guarantee
  text: Exporters produce documents only.
  basis: [D1.11]

- id: W11
  kind: guarantee
  title: Decision-provenance conformant.
  basis: [D1.12]
- id: W11.1
  kind: guarantee
  text: The draft log is a conformant system under `dpp/1` §8, at specification 1.0.
  basis: [D1.12]
  refs: [dpp/1 §8]
- id: W11.2
  kind: guarantee
  text: The draft log's conformance is checked by the `dpp/1` conformance suite.
  basis: [D1.12]
  refs: [dpp/1 Appendix C]
- id: W11.3
  kind: guarantee
  text: Every record the draft log exposes is conformant.
  basis: [D1.12]
  refs: [dpp/1 §3.6]
- id: W11.4
  kind: guarantee
  text: Every record the draft log exposes has a non-empty `why`.
  basis: [D1.12]
- id: W11.5
  kind: guarantee
  text: Every record the draft log exposes has `system` equal to the draft log's identifier.
  basis: [D1.12]
- id: W11.6
  kind: guarantee
  text: No hashed content changes under a published triple.
  basis: [D1.12]
  refs: [dpp/1 §3.8]
- id: W11.7
  kind: guarantee
  text: No version is reused.
  basis: [D1.12]
  refs: [dpp/1 §3.8]
- id: W11.8
  kind: guarantee
  text: Records the draft log no longer holds answer "not held".
  basis: [D1.12]
  refs: [dpp/1 §6.8]
- id: W11.9
  kind: guarantee
  text: The export's What-version record rests on every decision in force.
  basis: [D1.12, D1.17]
- id: W11.10
  kind: guarantee
  text: >-
    A Writ decision that lands the export, by naming it in its `basedOn`, reaches each author
    decision and each agent proposal by the walk of `dpp/1` §7 alone.
  basis: [D1.12]
  follows-from: [W11.9]
  refs: [dpp/1 §7]

- id: W12
  kind: guarantee
  title: Nothing an agent wrote is in the What unless a person adopted it.
  basis: [D1.12]
- id: W12.1
  kind: guarantee
  text: >-
    Every change at the head of the draft log is attached to a decision record whose `by` is
    the author.
  basis: [D1.12]
- id: W12.2
  kind: guarantee
  text: That decision record is either an adoption of a proposal, or the author's own write.
  basis: [D1.12]
- id: W12.3
  kind: guarantee
  text: A proposal never reaches the head on its own.
  basis: [D1.12]
- id: W12.4
  kind: guarantee
  text: The agent surface has no verb that adopts.
  basis: [D1.12]
```
