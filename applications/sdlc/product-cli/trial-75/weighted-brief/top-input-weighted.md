# Top input

## Relevance (a reader)

# Audience: authoriser

**Trial, `[PROPOSED]`.**

| | |
|---|---|
| Who | The person who authorises the work. They decide whether it is funded, continued or stopped. |
| Already knows | The business. That a tool called product-cli exists and is being rewritten. |
| Does not know | The terms of the definition. They have not read it. |
| Needs | What the product is for. What it commits to, in a form someone could hold it to. What it refuses to do, and who holds that authority instead. Where a person stays in control of what an agent produces. |
| Does not need | Mechanisms, formats, field-level rules, or how a check is carried out. |

## The document's introduction (C0)

Draft 4, 2026-11-03 (Draft 3, 2026-10-30; Draft 2, 2026-10-30; Draft 1, 2026-10-21). Written outside-in: the promise first, the implementation last. Chapters 1 to 6 are the product; chapter 7 is how it happens to be built and may change without the product changing.

This is the definition of the rewritten product-cli. It replaces the Rust workspace of the same name. `[D1.24]` (2026-11-03) It lives here, in decision-driven-design beside the What it implements; the tool, its ADRs and its tests live in `mindovermachine-dev/product-cli` (chapter 7). What carries over is listed in chapter 8; everything else is new, and "it was like that before" is not a reason for anything in this document.

Rulings are marked `[D1.n]` with their date where they land.
- **Drafts 2 and 3.** Draft 2 adds D1.2 to D1.9. Draft 3 adds D1.10 to D1.15, ruled with ADR-0010, ADR-0011 and ADR-0012; they rest on `dpp/1` (specification 1.0, draft of 2026-10-27, decision-driven-design `spec/decision-provenance/dpp-1.md`).
- **Draft 4** adds D1.16 to D1.25, ruled on 2026-11-03. D1.16 to D1.23 come from the gate checks of 2026-11-02 (A1 to A8); D1.24 supersedes D1.23, and D1.25 adds step 0 to the order of work. The checks were run against decision-driven-design `c7424ad`, Varve `c0a776b`, Writ `6737ac9` and the Rust tool `70395df`.
- **Superseded rulings** keep their number, with the ruling that replaces them named in place. The text below states the ruling in force.

## Chapters

### C1 — 1. The promise

**Budget: 75 words.**

The canon's own text of this chapter:

A machine-checkable statement of what a product does, with an executable oracle for its behaviour, exported as one graph that someone else can sign.

Four consequences follow and are the whole product:

- `[D1.10]` (2026-10-30) **The What is authored in conversation, and every step of it is a decision.** An agent proposes; the author watches the graph, its findings and its open questions change live, and adopts or rejects each proposal. Each adoption is a `dpp/1` decision record with its reason, so specification moves at the speed of the conversation and every element of the What traces to the person who adopted it.
- **The What is a graph with shapes, never prose with diagrams.** Anything that cannot be stated as a node, an edge or a shape is not yet specified, and the tool says so rather than accepting it.
- **Behaviour is executable before any code exists.** A Decider and a Projector are simulated sound and complete against scenarios drawn from the flows. The same scenarios later judge realised code through a wire protocol the tool implements.
- **The tool puts nothing in force and decides nothing about realisation.** `[D1.11]` (2026-10-30) It records the author's decisions over the What as `dpp/1` records, which by its profile carry no force. It produces a canonical document. What that document is held against, who accepts it under which grant, and from which position it is in force, belong to Writ.

Everything below is how.

### C2 — 2. Who it is for

**Budget: 25 words.**

Shared summary: It is for three roles on one surface: an author, an agent, and a realiser who needs an oracle to realise against. The author models the product and adopts or rejects the agent's proposals, the agent writes only proposals, and the realiser runs the behavioural-conformance runner against realised code. Neither author nor realiser edits the other's artefact.

### C3 — 3. The surface

**Budget: 40 words.**

Shared summaries of its sections:

- C3.1 (Commands): The verbs capture, validate and export What nodes, derive and simulate Deciders and Projectors, run scenarios and conformance, manage open questions and proposals, and serve the workbench and the agent surface. Every export, the canonical one included, is written by an exporter over the canonical graph.
- C3.2 (The draft log): The working copy is a positioned log of its own, where every verb is a commit and `diff` and undo are reads over it. Draft positions are local to the author and are not Writ positions; the export is a document, not a position.
- C3.3 (Proposals and decisions): Every change that reaches the draft log's head is a decision record: an agent's write is a proposal beside the head, which the author adopts or rejects, while the author's CLI write has no proposal step. `accepted` means adopted into the author's draft, carrying no force, permission or grant.
- C3.4 (The workbench): `product view` serves a live, local view of the draft log, updating on every new position whoever wrote it, and shows the What at the head, the session, pending proposals, findings and open questions. Its only writes are adopt and reject, through the same verbs as the CLI.
- C3.5 (Adopting on the fly): Adoption costs one action wherever the author is: in the workbench, at the CLI, or by elicitation in the conversation, with a `ref` to the proposal as its default `why`. Rejection asks for a short reason, which is returned to the agent as the outcome of its proposal.
- C3.6 (MCP): MCP offers the same verbs over stdio or HTTP in a phase-gated session: structure, then behaviour, then surface. Every agent write creates a proposal and requires a reason, and the agent surface has no adopt, reject, land, grant or signing; adoption is the author's.

### C5 — 5. The guarantees

**Budget: 60 words.**

The canon's own text of this chapter:

Each is a property test over generated What graphs and scenarios, and the suite is public. Every test observes bytes, in the draft log or in an export, never the return value of the verb that produced them.

`[D1.19]` (2026-11-03) W1 and W5 are the edition's violations. W3 and W4 are its warnings (`DDD-dec-113`). The checks themselves are the edition's shapes, not code in this tool.

- **W1. Shape before storage.** No change set enters the draft log if it carries a violation. A failed write leaves the log unchanged.
- **W2. Derived, not declared.** A Decider's signature (the commands it handles, the events it may emit, the state it evolves) and a Projector's (the events it folds, the fields it may produce) are computed from the graph. An authored signature, or logic, that disagrees is refused.
- **W3. Coverage.** Each gap below is a finding, never a silent pass:
  - every command targeting an aggregate is handled by its Decider;
  - every event a Projector's View projects is folded by it;
  - every (command, subject kind) pair, from a step's `sdlc:offeredTo` or a trigger's `sdlc:subject`, has a scenario showing acceptance or a reachable rejection;
  - every View a step surfaces has a scope rule for every subject kind the step is offered to, or is public;
  - `[D1.4]` (2026-10-30, amended by D1.18) `[D1.18]` (2026-11-03) every automated or external trigger acts as a subject kind (`sdlc:subject`). A user trigger's subject comes from the step's `sdlc:offeredTo` (`what.md` §3.7).
- **W4. Justification.** Orphans are findings:
  - every aggregate field is read by some Decider;
  - every projected field is consumed by some step;
  - every claim is read by some Decider or compared by a scope key;
  - every Decider has a reachable rejection.
- **W5. Type boundary.** Each of these is refused at write, not reported later:
  - a UI step references only AIOs, never concrete controls;
  - `[D1.4]` (2026-10-30, amended by D1.18) a trigger's `sdlc:subject`, when present, names a subject kind whose nature matches the trigger's `source`. An absent subject is accepted, and reported under W3 when the trigger is automated or external. A What without subjects therefore exports byte-identically;
  - a journey crosses systems only through a Translation.
- **W6. Simulation before realisation.** Every Decider and Projector with scenarios is simulated sound and complete before an export is marked ready. A What with a failing scenario exports, but says so in its What-version record.
- **W7. Canonical export.** Two exports of the same draft position are byte-identical, on every platform, graph and logic artefacts alike. Canonicalisation happens once, before any exporter runs. Every derived export is a deterministic function of the canonical graph and artefacts, and its record names that graph's canonical hash.
- **W8. Round-trip.** Importing a canonical export yields a draft whose export is byte-identical to the input, graph and artefacts.
- **W9. Phase order.** An agent session cannot author a node before the nodes it derives from exist. The gate is the session transport, not advice in a prompt.
- **W10. Nothing in force, nothing landed.** `[D1.11]` (2026-10-30) The tool holds no key and no grant, puts nothing in force, knows no Writ position, and writes to no log but its own draft log. Its decision records carry no force by its profile. Exporters produce documents only.
- **W11. Decision-provenance conformant.** `[D1.12]` (2026-10-30) The draft log is a conformant system under `dpp/1` §8, at specification 1.0, checked by the `dpp/1` conformance suite (Appendix C):
  - every record it exposes is conformant (§3.6), has a non-empty `why`, and has `system` equal to the draft log's identifier;
  - no hashed content changes under a published triple, and no version is reused (§3.8);
  - records it no longer holds answer "not held" (§6.8).

  The export's What-version record rests on every decision in force (D1.17). A Writ decision that lands the export, by naming it in its `basedOn`, therefore reaches each author decision and each agent proposal by the walk of `dpp/1` §7 alone.
- **W12. Nothing an agent wrote is in the What unless a person adopted it.** `[D1.12]` (2026-10-30) Every change at the head of the draft log is attached to a decision record whose `by` is the author: either an adoption of a proposal, or the author's own write. A proposal never reaches the head on its own, and the agent surface has no verb that adopts.

### C8 — 8. Boundaries and decisions taken

**Budget: 40 words.**

Shared summary: The scope is the What alone: the How, work units, features, releases and code generation are not in it. What carries over from the Rust workspace is the name and verb names, `what.md`, the wire-protocol schemas, the self-hosted What as the first fixture, and the conformance suite. The tool records decisions and never puts one in force; the draft log and Writ's log are two `dpp/1` systems joined only by `basedOn` references.

