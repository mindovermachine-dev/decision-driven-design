# Audience-top input

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

## Chapters, with the shared summaries of their leaves

### C1 — 1. The promise

- C1: The promise is a machine-checkable statement of what a product does, with an executable oracle for its behaviour, exported as one graph that someone else can sign. The What is authored in conversation, where an agent proposes and the author adopts or rejects, and is a graph with shapes, never prose, with behaviour executable before code exists. The tool puts nothing in force and decides nothing about realisation; acceptance and force belong to Writ.

### C2 — 2. Who it is for

- C2: It is for three roles on one surface: an author, an agent, and a realiser who needs an oracle to realise against. The author models the product and adopts or rejects the agent's proposals, the agent writes only proposals, and the realiser runs the behavioural-conformance runner against realised code. Neither author nor realiser edits the other's artefact.

### C3 — 3. The surface

- C3.1 (Commands): The verbs capture, validate and export What nodes, derive and simulate Deciders and Projectors, run scenarios and conformance, manage open questions and proposals, and serve the workbench and the agent surface. Every export, the canonical one included, is written by an exporter over the canonical graph.
- C3.2 (The draft log): The working copy is a positioned log of its own, where every verb is a commit and `diff` and undo are reads over it. Draft positions are local to the author and are not Writ positions; the export is a document, not a position.
- C3.3 (Proposals and decisions): Every change that reaches the draft log's head is a decision record: an agent's write is a proposal beside the head, which the author adopts or rejects, while the author's CLI write has no proposal step. `accepted` means adopted into the author's draft, carrying no force, permission or grant.
- C3.4 (The workbench): `product view` serves a live, local view of the draft log, updating on every new position whoever wrote it, and shows the What at the head, the session, pending proposals, findings and open questions. Its only writes are adopt and reject, through the same verbs as the CLI.
- C3.5 (Adopting on the fly): Adoption costs one action wherever the author is: in the workbench, at the CLI, or by elicitation in the conversation, with a `ref` to the proposal as its default `why`. Rejection asks for a short reason, which is returned to the agent as the outcome of its proposal.
- C3.6 (MCP): MCP offers the same verbs over stdio or HTTP in a phase-gated session: structure, then behaviour, then surface. Every agent write creates a proposal and requires a reason, and the agent surface has no adopt, reject, land, grant or signing; adoption is the author's.

### C4 — 4. The formats

Chapter introduction (C4): Every format has a specification page and a conformance suite before any implementation, and is under a read-forever rule from the first release.

Section numbers in this chapter and the next are `applications/sdlc/what.md`'s. The mapping from the old Framework sections is `what.md`'s appendix.

- C4.1 (The vocabulary (`sdlc:`)): The vocabulary is `sdlc:`, owned by decision-driven-design; this tool implements it and owns nothing of it, and `pf:` is retired. It is versioned by edition: an export states its edition, a later edition never changes the meaning of an earlier one, and migration is a new export.
- C4.2 (Shapes): The shapes and rules live with the vocabulary, versioned by the same edition, and are one artefact in two roles: the author's feedback in this tool and Writ's enumerated decisions. The binary embeds the edition's files, and the build fails if they do not hash to the pin.
- C4.3 (The canonical export): The canonical export is the graph document, the RDFC-1.0 canonical N-Quads serialisation of the What graph at one draft position, plus the logic artefacts its digests name; the graph document is the only one Writ lands. Two exports of the same draft position are byte-identical, graph and artefacts alike.
- C4.4 (The What-version record): Every export carries its manifest as a What-version `dpp/1` record, which is JSON, not RDF. It holds the ruled shape, a `basedOn` that pins every decision in force at the version, this tool's dotted member, and unhashed `extensions`.
- C4.5 (Decision records and the profile): The draft log exposes its decision records through the `dpp/1` file binding, so a reader with the repository can walk them without the tool. This tool publishes a profile, a format under read-forever, stating that no record of this system binds anyone and requiring no signatures.
- C4.6 (Exports): Every export is a deterministic function of the canonical graph and its logic artefacts; the canonical writer's format is the one Writ lands, and every other export is derived and not landable. A derived format is under read-forever only when it has a specification page and a conformance suite.
- C4.7 (Scenarios and the wire protocol): A scenario is an `sdlc:Scenario` element; this tool owns its authoring and reporting form, and the graph form is the vocabulary's. The wire protocol is the JSON request and response shapes a runner reads on stdin and answers on stdout; its schemas are decision-driven-design's, and this tool implements them.
- C4.8 (Decider and Projector logic): The logic is an authored artefact held by digest, not part of the graph's triples; the graph holds the derived signature, and the simulator refuses logic that disagrees with it. The logic media type is this tool's format, a closed expression grammar, specified with its suite before the Decider slice.

### C5 — 5. The guarantees

- C5: Each guarantee is a property test over generated What graphs and scenarios, in a public suite, and every test observes bytes, never a verb's return value. They cover shape before storage, derived signatures, coverage, justification, type boundary, simulation before realisation, canonical export, round-trip, phase order and decision-provenance conformance. The tool holds no key and puts nothing in force, and nothing an agent wrote is in the What unless a person adopted it.

### C6 — 6. The contracts between parts

- C6: The contracts between parts are five small interfaces, each expressed over the vocabulary: the draft store, the shape engine, the simulator, the runner protocol and the authoring session. Exporting and the workbench are not contracts; the workbench reads the draft store and the shape engine, and writes only through the authoring session. Nothing in the tool references Writ, and Writ references the vocabulary by IRI and edition, never this tool's code.

### C7 — 7. Implementation

- C7: This chapter may change without chapters 1 to 6 changing. The tool is one Native AOT binary hosting the CLI, MCP and the workbench, with Varve embedded as the draft store; the definition lives in decision-driven-design, the tool in `mindovermachine-dev/product-cli`, and the Rust workspace is frozen by tag. Acceptance goes through a one-time lift, with two fixtures that round-trip byte-identically, and the order of work ends by retiring the Rust binary.

### C8 — 8. Boundaries and decisions taken

- C8: The scope is the What alone: the How, work units, features, releases and code generation are not in it. What carries over from the Rust workspace is the name and verb names, `what.md`, the wire-protocol schemas, the self-hosted What as the first fixture, and the conformance suite. The tool records decisions and never puts one in force; the draft log and Writ's log are two `dpp/1` systems joined only by `basedOn` references.

### CX — Cross-repository dependencies

- CX: The cross-repository dependencies list what each ruling needs from decision-driven-design, Writ, Varve and product-cli, and the state of each need. Most are met, including the tagged `sdlc:` edition 1, the validation regime, RDFC-1.0 and SHACL in Varve, the `rust-final` tag and slice 0. Still open are Writ landing canonical N-Quads as the What document and Writ's embedded log and `land`; product-cli's element-hash vectors are to deliver at step 2.

