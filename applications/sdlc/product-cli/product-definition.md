# Product: product definition

Draft 4, 2026-11-03 (Draft 3, 2026-10-30; Draft 2, 2026-10-30; Draft 1, 2026-10-21). Written outside-in: the promise first, the implementation last. Chapters 1 to 6 are the product; chapter 7 is how it happens to be built and may change without the product changing.

This is the definition of the rewritten product-cli. It replaces the Rust workspace of the same name. `[D1.24]` (2026-11-03) It lives here, in decision-driven-design beside the What it implements; the tool, its ADRs and its tests live in `mindovermachine-dev/product-cli` (chapter 7). What carries over is listed in chapter 8; everything else is new, and "it was like that before" is not a reason for anything in this document.

Rulings are marked `[D1.n]` with their date where they land.
- **Drafts 2 and 3.** Draft 2 adds D1.2 to D1.9. Draft 3 adds D1.10 to D1.15, ruled with ADR-0010, ADR-0011 and ADR-0012; they rest on `dpp/1` (specification 1.0, draft of 2026-10-27, decision-driven-design `spec/decision-provenance/dpp-1.md`).
- **Draft 4** adds D1.16 to D1.25, ruled on 2026-11-03. D1.16 to D1.23 come from the gate checks of 2026-11-02 (A1 to A8); D1.24 supersedes D1.23, and D1.25 adds step 0 to the order of work. The checks were run against decision-driven-design `c7424ad`, Varve `c0a776b`, Writ `6737ac9` and the Rust tool `70395df`.
- **Superseded rulings** keep their number, with the ruling that replaces them named in place. The text below states the ruling in force.

## 1. The promise

A machine-checkable statement of what a product does, with an executable oracle for its behaviour, exported as one graph that someone else can sign.

Four consequences follow and are the whole product:

- `[D1.10]` (2026-10-30) **The What is authored in conversation, and every step of it is a decision.** An agent proposes; the author watches the graph, its findings and its open questions change live, and adopts or rejects each proposal. Each adoption is a `dpp/1` decision record with its reason, so specification moves at the speed of the conversation and every element of the What traces to the person who adopted it.
- **The What is a graph with shapes, never prose with diagrams.** Anything that cannot be stated as a node, an edge or a shape is not yet specified, and the tool says so rather than accepting it.
- **Behaviour is executable before any code exists.** A Decider and a Projector are simulated sound and complete against scenarios drawn from the flows. The same scenarios later judge realised code through a wire protocol the tool implements.
- **The tool puts nothing in force and decides nothing about realisation.** `[D1.11]` (2026-10-30) It records the author's decisions over the What as `dpp/1` records, which by its profile carry no force. It produces a canonical document. What that document is held against, who accepts it under which grant, and from which position it is in force, belong to Writ.

Everything below is how.

## 2. Who it is for

A product owner, a designer or an agent authoring what a product does, and an engineer who needs an oracle to realise against. Three roles, one surface.

| Role | Does | Through |
|---|---|---|
| Author (product owner, designer) | names the product, its domains and systems; models entities, events, commands, Views, UI steps, flows, journeys, subjects, quality demands; answers open questions; adopts or rejects the agent's proposals | the workbench, the CLI, or an agent session driving the same verbs |
| Agent | proposes What from an interview or a document, within a phase-gated session, writing only proposals through the tool's verbs | the MCP server |
| Realiser (engineer, or a build agent under Writ) | derives Decider and Projector signatures, reads scenarios, runs the behavioural-conformance runner against realised code | the CLI and the wire protocol |

**The author's day.** The author talks to an agent with the workbench open beside the conversation. The agent proposes; each proposal appears on the graph with its reason and its findings; the author adopts or rejects it. A flow is sketched. The tool refuses a UI step that names a dropdown or a View over an event nobody emits, and reports a command whose Decider does not yet handle it as a finding to answer. The Decider's signature is derived and its logic authored. Scenarios run. The export is handed to Writ.

**The realiser's day.** Read the accepted What at a position through Writ, build, run the runner, land.

Neither edits the other's artefact.

## 3. The surface

### Commands

Every verb takes `--product <name>`; a repository holds one or more products under `.product/products/<name>/`.

| Verb | What it does |
|---|---|
| `product init [--demo]` | scaffolds `.product/`, opens the draft log, seeds the worked example |
| `product product new\|list\|show` | the product root (§3.0): name, purpose, owned domains and systems |
| `product domain new <kind> <id> …` | captures a What node of one of the kinds listed below; refuses a change set with a violation (W1) |
| `product domain show\|list\|rm` | inspects or removes nodes and their links |
| `product domain validate [--strict]` | `[D1.19]` (2026-11-03) violations; with `--strict`, also the warning findings of chapter 5 (W3, W4) |
| `product domain export [--canonical] [--format <name\|IRI>]` | the What, written by an exporter over the canonical graph. The default and `--canonical` give the canonical document, which is what Writ lands. `--format` selects another registered exporter. An unknown format, or an edition the exporter does not support, is refused with a diagnostic and no output. `--list-formats` prints each registered format: name, IRI, media type, supported editions, stability |
| `product decider derive\|validate\|simulate <aggregate>` | derives a Decider's signature from the event model, checks the authored logic against it, runs its scenarios |
| `product projector derive\|validate\|simulate <view>` | the read-model peer |
| `product primitive new\|validate <id>` | a named-algorithm primitive: reference, I/O contract, oracle pairs (§3.5) |
| `product scenario new\|list\|run` | a given/when/then over events, a command (with a subject) and expected events or state; drawn from flows or authored |
| `product conformance run <runner>` | drives a realised implementation through the wire protocol (§6) with the product's scenarios and reports outcomes |
| `product question new\|list\|answer` | open questions as authored nodes: what the graph cannot yet decide, which nodes they concern, what they block |
| `product diff [<p> <q>] [--export <file>]` | what changed between two draft positions, or between the draft and a given export |
| `product proposal list\|show\|adopt\|reject\|review` | `[D1.12]` (2026-10-30) the agent's pending proposals; `adopt` and `reject` write the author's decision record, with its reason (below). `[D1.15]` (2026-10-30) `adopt` takes one or more numbers or ids, or `--all`; `review` steps through pending proposals one at a time (below) |
| `product view [--port <n>]` | `[D1.13]` (2026-10-30) the workbench: a live view of the draft log on localhost (below) |
| `product mcp [--http]` | the agent surface, same verbs, phase-gated (below); with `--http`, also starts the workbench |

**Node kinds for `domain new`:** `entity`, `value-object`, `relation`, `invariant`, `context`, `mapping`, `reference-data`, `event`, `command`, `view`, `trigger`, `ui-step`, `flow`, `system`, `journey`, `subject-kind`, `quality-demand`. `[D1.8]` (2026-10-30) `subject-kind` replaces `actor-kind`, following chapter 8's term.

> **Open.** Some kinds are in the vocabulary but have no `domain new` kind:
> - AIO, context of use, page graph and application root;
> - WCAG criterion and attestation;
> - `sdlc:DeclaredTarget` (`what.md` §4.1);
> - `sdlc:Interaction`, `sdlc:Field`, `sdlc:StateAnnotation` and `sdlc:ContentKey`, which are elements by `DDD-dec-64` P-3.
>
> Either they gain kinds, or the definition names the verb through which they are authored.

`[D1.2]` (2026-10-27) Exporting goes through one seam: every export, the canonical one included, is written by an exporter over the canonical graph (§4, "Exports").

### The draft log

The working copy is a positioned log of its own (Varve, embedded, kept in Git). Every verb is a commit; `diff`, undo and "what changed in this session" are reads over it. Draft positions are local to the author and are not Writ positions. The export is a document, not a position: Writ computes its own delta when it lands it.

### Proposals and decisions

`[D1.12]` (2026-10-30) The draft log is a `dpp/1` conformant system (`dpp/1` §8). Every change that reaches its head is a decision record (`dpp/1` §3) with a non-empty `why`.

- **The agent proposes.** An agent's write is a proposal: a change set, shape-checked (W1) and phase-gated (W9) when submitted, held beside the head and not in it.
  - Its record has `status: proposed`, `by` the agent's identity (`dpp/1` §3.4: software is `by`, never a person), `attributedTo` the author, and the agent's reason in `why`.
  - An agent may submit two or three proposals as alternatives to one another.
- **The author adopts or rejects.**
  - Adoption is a new version of the proposal's decision: `by` the author, `status: accepted`, `why` the author's reason or a `ref` to the proposal, and the change set pinned. The change set is shape-checked again against the head it lands on.
  - Rejection is a new version with `status: withdrawn` and its reason.
  - Adopting one alternative withdraws its siblings, each with a `why` referring to the adopted one.
- **The author writes directly.** A CLI write by the author is a decision record with `by` the author and `status: accepted`, with no proposal step.
- **What the statuses mean** is fixed by this tool's profile (`dpp/1` §9.4, chapter 4): `accepted` means adopted into this author's draft. It carries no force, permission or grant, and no reader may infer any (`dpp/1` §3.4).

### The workbench

`[D1.13]` (2026-10-30) `product view` serves a live, local view of the draft log in a browser. It follows the draft log rather than any one writer, so it updates on every new position whoever wrote it: the CLI, an agent over stdio MCP, or an agent over HTTP MCP. It shows:

- the structure, behaviour and surface of the What at the head;
- the session: the current phase, what the last decision changed, and who decided it (agent proposal or author);
- pending proposals with their reasons, findings and alternatives, each with adopt and reject;
- findings (W3, W4) and open questions, as what to answer next.

Its only writes are adopt and reject, and they go through the same verbs as the CLI, so W1, W9 and W12 have one enforcement point. It binds to localhost.

### Adopting on the fly

`[D1.15]` (2026-10-30) Adoption is the author's most frequent act, so it costs one action wherever the author is.

- **Adoption needs no typing.** By default an adoption's `why` is a `ref` to the proposal, pinned in `basedOn` (`dpp/1` §3.4): "adopted for the reason the proposal gives". The author types a reason only to add one.
- **Rejection needs one line, and the agent reads it.** `dpp/1` requires a non-empty `why`, so rejection asks for a short reason, with a few one-press reasons offered (out of scope, wrong, duplicate, not yet). The reason is returned to the agent as the outcome of its proposal, so a rejection is also the instruction for the next proposal.
- **The workbench.**
  - Each pending proposal is a card beside the graph. The change it would make is drawn on the graph in place: added, changed and removed elements marked. The card shows its reason and the findings it would add or close.
  - Keyboard: next and previous proposal, adopt, reject, and choose among alternatives. Adopting one alternative withdraws its siblings in the same action.
  - A selection, or everything pending in the current phase, can be adopted in one action after a confirmation that states the count. Each proposal still gets its own record.
  - A proposal that no longer holds against the head is marked stale, with adopt disabled and the failing shape shown.
- **The CLI.**
  - `product proposal list` numbers the pending proposals.
  - `product proposal adopt 3 5` or `adopt --all` adopts by number. `--why` adds a reason.
  - `product proposal review` steps through them one at a time, showing each change set and its reason, with single-key adopt, reject, skip and quit, in the manner of `git add -p`.
- **In the conversation.** Where the MCP client supports elicitation, the agent may ask the author to adopt its proposals inline. The tool, not the model, sends the elicitation request, and the author's answer goes from the client to the tool without passing through the model, so the adoption's `by` is the author. Where the client does not support elicitation, the agent points the author to the workbench or to `review`. The profile records that an adoption made by elicitation trusts the client to have shown the request to the author.

### MCP

The same verbs, over stdio or HTTP, in a phase-gated session: structure (§3.0, §3.1), then behaviour (§3.2 to §3.5), then surface (§3.2.1 to §3.2.4), because each derives from the one before.

- Read verbs from an earlier phase stay callable; writes lock to their phase.
- Every write verb of an agent session creates a proposal, and requires a reason.
- Open questions are phase-free and gate advancing.
- There is no adopt, no reject, no land, no grant and no signing on the agent surface: adoption is the author's, in the workbench, at the CLI, or by elicitation answered by the author (D1.15). An agent session ends with an export, which is handed to Writ by whoever holds a grant there.

## 4. The formats

Every format has a specification page and a conformance suite before any implementation, and is under a read-forever rule from the first release.

Section numbers in this chapter and the next are `applications/sdlc/what.md`'s. The mapping from the old Framework sections is `what.md`'s appendix.

### The vocabulary (`sdlc:`)

`[D1.1]` (2026-10-28) The vocabulary is `sdlc:`, owned by decision-driven-design (`applications/sdlc/`), where the What now lives; this tool implements it and owns nothing of it. `pf:` is retired. Element identity is the ruled form of `DDD-dec-63`: a stable product IRI P, flat element IRIs `P/what/<ULID>` with names as labels, RDFC-1.0 as the canonical form, a What-version as a `dpp/1` record. The §4 to §7 classes are not carried.

The content is the What subset of the Product Framework:
- product, domain, system, bounded context;
- entity, value object, field, relation, invariant, context mapping, reference data;
- event, command, View with its state space, trigger with its subject kind;
- UI step and interaction, AIO, context of use, page graph and application root;
- WCAG criterion and attestation;
- flow, journey;
- Decider, Projector, scenario, named-algorithm primitive;
- quality demand, subject kind and claim, scope rule, declared target;
- open question.

`[D1.18]` (2026-11-03) **Terms.** This definition and every specification page cite the vocabulary's own terms: `sdlc:subject` on a trigger, `sdlc:keyedBy` on a Projector, `sdlc:wireName` and `sdlc:within`. CLI flags may use other names. Earlier drafts' `acts_as` and `keyed_by` read as these terms.

The vocabulary is versioned by edition. An export states its edition. A later edition never changes the meaning of an earlier one; migration is a new export.

### Shapes

`[D1.9]` (2026-10-30, amended by D1.20) The shapes and rules live with the vocabulary, in decision-driven-design (`applications/sdlc/`), versioned by the same edition. The content:

- SHACL shapes for every node kind (the per-node checks);
- SPARQL rules for the graph-level checks (chapter 5).

They are the author's feedback in this tool and, at the same edition, Writ's enumerated decisions over the same graph. One artefact, two roles; never two copies.

`[D1.20]` (2026-11-03) **How the edition is carried.** The edition is pinned by `(versionIRI, hash)`, as `DDD-dec-72` rules: `owl:versionIRI` and the sha256 over `ontology.ttl` then `shapes.ttl`, the bytes as tagged.
- The binary embeds both files byte for byte, because the version IRI does not dereference to them and the binary runs offline.
- The build fails if the embedded bytes do not hash to the pin.
- There is no edited copy, no second source and no runtime fetch.

The one hash law (D1.3) governs What graph content. The edition itself is pinned as files.

`[D1.19]` (2026-11-03) **The validation regime and the severities** are the edition's (ruled in `DDD-dec-113`, E-1 and E-2; `what.md` §7.2):
- **The data graph** is the What graph merged with the edition's `ontology.ttl`. Validation uses SHACL Core class semantics (`rdf:type/rdfs:subClassOf*` over that merged graph) with SHACL-SPARQL, and no RDFS or OWL entailment.
- **The ontology** is never part of a What graph's hash or of an export.
- **`sh:Violation`** refuses at write (W1, W5).
- **`sh:Warning`** is a finding (W3, W4). It is reported, never refused.

A requirement added to an edition after an example is pinned enters as `sh:Warning`, and may become a violation only in a later edition (`DDD-dec-113`, E-2).

If the edition keeps pattern conformance (`what.md` §3.2.0, every command traces to a trigger) a violation, then `domain new command` takes its trigger in the same change set, and an agent proposes them together.

### The canonical export

`[D1.3]` (2026-10-30, amended by D1.16) **The canonical document.** The landable graph document is the RDFC-1.0 canonical N-Quads serialisation of the What graph at one draft position, in the default graph, under the hash law of `DDD-dec-73`. It is the only graph document Writ lands. Writ must accept it as such; that is a change requested in Writ (Writ #22), not made here.

`[D1.16]` (2026-11-03, superseding the logic clause of D1.3 and the whole of D1.7) **What the export contains.**
- **The graph.** One graph: the What nodes, with every Decider and Projector carrying `sdlc:logic` (a `sha256:` digest) and `sdlc:logicMediaType`, as `DDD-dec-63` §6 rules.
- **The logic artefacts.** The authored logic itself, one file per digest, in the logic media type (below).

The canonical export is the graph document plus the artefacts its digests name. A digest in the graph with no artefact beside it is a malformed export. The graph hash and the element hashes cover the logic through the digests.

`[D1.5]` (2026-10-30) **Determinism.** Two exports of the same draft position are byte-identical, graph and artefacts alike. Element IRIs are minted when a node is first written, so two authors who independently author the same What hold different IRIs and export different bytes. Identity comes from the draft log, not from content.

**Element hashes.** Each element's hash is taken over its description, canonicalised on its own (`DDD-dec-63` §4, `what.md` §2.3). The description rule is `sdlc:`-specific, so it is implemented here over Varve's canonicaliser and never put into Varve. Its vectors over decision-driven-design's examples are offered there as a further cross-check. M-12's second implementation stays Varve's published vectors (`DDD-dec-73`).

### The What-version record

`[D1.14]` (2026-10-30) is superseded by D1.17.

`[D1.17]` (2026-11-03) Every export carries its manifest as a What-version `dpp/1` record. It is JSON, per `dpp/1` §3, not RDF; the PROV-O rendering of `dpp/1` §10 is non-normative and lossy. It has four parts.

- **The ruled shape.** It is `DDD-dec-63` §6's record, written unchanged:
  - `id` is `what`; `version` is a sequence this system chooses, never the graph hash;
  - `supersedes` is the previous What-version;
  - the dotted member `dk.decision-driven-design.sdlc` holds `record: "what-version"`, `product` (P), `edition {versionIRI, hash}`, `canon: "rdfc-1.0"`, `graphHash`, and `elements`, an array of `{iri, hash}` sorted by IRI.

  The protocol members are this system's: `system` is the draft log's identifier, `by` the author who exported, and `why` the reason for the export.
- **`basedOn`.** It pins every decision in force at the version: every adoption and every direct author write. A `dpp/1` §7 walk from any export therefore reaches every author decision and agent proposal behind it. At roughly 150 bytes per reference, this stays well under `dpp/1` §3.1's 1 MiB recommendation for several thousand decisions. A What past that size is a question for a later draft, not a reason to change the shape now.
- **This tool's dotted member** (`dpp/1` §3.7), named by a reverse domain name this project controls. It holds:
  - the format IRI of the canonical export;
  - the simulation status (W6);
  - the logic artefacts, as `{digest, mediaType}`, sorted by digest.

  Its values are strings, objects and arrays only, as the hash law requires.
- **`extensions` (unhashed).** These hold the draft position, its Varve header hash and the session identifier. `dpp/1` defines no positions, sessions or clocks other than `at` (§1.3), so these are this tool's, and change nothing about the decision.

### Decision records and the profile

`[D1.12]` (2026-10-30) The draft log exposes its decision records through the `dpp/1` file binding (§6.6), at `.product/products/<name>/decisions/`, so a reader with the repository can walk them without the tool. The record shapes are `dpp/1`'s.

This tool publishes a profile (`dpp/1` §9.4), and names it in its descriptor. It states:

- what `proposed`, `accepted` and `withdrawn` mean (chapter 3, "Proposals and decisions");
- that no record of this system binds anyone, and that a `basedOn` edge from another system into it carries provenance and never force;
- the dotted members and `extensions` it writes;
- the identity schemes in `by`: the author's (from configuration, as a URI), and the agent's, which is self-declared by the MCP client and unauthenticated (`dpp/1` §11.4).

The profile is a format under read-forever like the others. It requires no signatures: they are optional in `dpp/1` (§11.3), and the tool holds no key (W10).

### Exports

`[D1.2]` (2026-10-27, amended by D1.16) Every export is a deterministic function of the canonical graph and its logic artefacts. The canonical graph is the pinned edition plus the RDFC-labelled, sorted triple set. Exporters receive only these. They read neither the draft log nor node-record internals.

**Canonical and derived.** The canonical writer is the first exporter; its format IRI is the one Writ lands. Every other export is derived:

- deterministic from the same canonical graph and artefacts;
- not landable;
- its `dpp/1` record names the canonical content hash it was derived from (`prov:wasDerivedFrom`).

**Stability.** A derived format is under read-forever only when it has a specification page and a conformance suite. At first release: sorted Turtle, with a fixed prefix set and subjects and predicates sorted, for human review and diffs.

**Scope.** An exporter describes the What. Output that is executable, or that is parameterised by a realisation target, is code generation and is out of scope.

### Scenarios and the wire protocol

**Scenarios.** A scenario is an `sdlc:Scenario` element within its Decider or Projector (`what.md` §3.3). It has three parts:

- `given`: prior events;
- `when`: a command with its subject (`sdlc:asSubject`), or an event for a Projector;
- `then`: expected events with their payloads, or a rejection naming its invariant; or expected read-model state.

The scenario format this tool owns is the authoring and reporting form of those elements. The graph form is the vocabulary's.

**The wire protocol (`what.md` §6).** The JSON request and response shapes a runner reads on stdin and answers on stdout, over the wire scalar alphabet (boolean, 64-bit integer, string). Its four schemas are decision-driven-design's (`what/conformance/`), under `https://decision-driven-design.dk/ns/sdlc/conformance/1/`, and this tool implements them. Every name on the wire is a wire name, never a key or a label. Running the protocol against code under Writ is Writ's reporter.

### Decider and Projector logic

`[D1.7]` (2026-10-30) is superseded by D1.16.

`[D1.16]` (2026-11-03) **The logic is an authored artefact held by digest** (`DDD-dec-63` §6). It is not RDF and not part of the graph's triples; the graph carries its digest and media type.

The signature is in the graph and is derived:
- `sdlc:decidesFor`, `sdlc:handles`, `sdlc:reads` and `sdlc:rejects` for a Decider;
- `sdlc:projectsFor`, `sdlc:folds` and `sdlc:keyedBy` for a Projector.

W2, W3 and W4 read only these edges. The logic file must agree with them, and the simulator refuses logic that does not.

**The logic media type** is this tool's format, specified with its suite before the Decider slice. It is a closed expression grammar over:
- the Decider's state;
- the command's payload;
- the command's subject and its claims;
- for a Projector, the view state and the event.

It covers decide rules (rejections by invariant wire name, with their conditions, and emissions) and evolve and fold assignments. Every value is a wire scalar; set-valued claims are the one list position (`what.md` §3.3). A named-algorithm primitive is the only escape for what rules cannot express (§3.5). Logic the simulator cannot evaluate is not a Decider; it is prose.

decision-driven-design's example logic (`what/examples/logic/*.yaml`, `application/yaml`) is the first input the grammar must read. Whether the media type is that YAML with a fixed expression grammar, or a successor that reads it, is the logic specification's decision.

## 5. The guarantees

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

## 6. The contracts between parts

Five interfaces, each small, each expressed over the vocabulary. Exporting is not a contract: exporters are functions of the canonical-export format and add no seam over the vocabulary.

| Contract | In | Out | First implementation |
|---|---|---|---|
| **Draft store** | commits of What nodes and logic artefacts | positions, as-of reads, diffs | Varve, embedded, file backend in Git |
| **Shape engine** | a graph, and the embedded shapes and ontology of an edition | violations and warnings by node and shape | Varve's `Varve.Shacl` with `Varve.Shacl.Sparql`, under the regime of D1.19 |
| **Simulator** | a Decider or Projector, its logic artefact, scenarios | outcomes per scenario, derived signature, coverage and justification findings | an evaluator for the logic media type over the wire scalar alphabet |
| **Runner protocol** | scenarios | requests on stdin; outcomes judged by exact ordered-emit and full-state equality from stdout | `what.md` §6's JSON shapes; a C# reference runner |
| **Authoring session** | a product, a phase, an actor (agent or author) | the verbs permitted in that phase to that actor: proposals for an agent, adoption and direct writes for the author | MCP over stdio and HTTP; the workbench and the CLI for the author |

The workbench is not a contract: it reads the draft store and the shape engine, and writes only through the authoring session.

Nothing in the tool references Writ. Writ references the vocabulary by IRI and edition, never this tool's code.

## 7. Implementation

This chapter may change without chapters 1 to 6 changing.

| Part | Built from | Why |
|---|---|---|
| Draft store | Varve, embedded | positions and diffs over the draft for free; one RDF stack in the ecosystem |
| Shapes and rules | the edition's files, embedded and hash-checked at build (D1.20), evaluated by Varve's SHACL and SHACL-SPARQL | the same bytes Writ evaluates, so the author's check and the gate cannot disagree |
| Canonical form | Varve's `RdfCanonicaliser` (RDFC-1.0) | checked on 2026-11-02 to reproduce decision-driven-design's published graph hashes, and the lift input's hash, byte for byte |
| Element hashes | this tool, over Varve's canonicaliser | the description rule is `sdlc:`'s, not Varve's |
| Node kinds | one C# record per kind, with a source generator emitting the RDF writer, the parser, the kind registry and the shape binding (ADR-0005) | the Rust version kept five hand-maintained parallel enumerations and failed silently when one was missed |
| Exporters | one interface over the canonical graph and artefacts, registered at compile time | Native AOT forbids runtime plugins; canonicalisation in one place |
| Decision records | `dpp/1` records over the file binding, hashed by the `dpp/1` hash law (§5) | the draft log is walkable by any `dpp/1` reader, with no tool |
| Workbench | a Blazor WebAssembly client, embedded in the binary and served by it | all C#, no Node; Blazor Server is not Native AOT compatible, static files and minimal APIs are |
| Hosts | one Native AOT binary: CLI, MCP and the workbench | one process; no shared or hosted server, only local hosts; the draft log is per author |

**Constraints.** 100% managed .NET, Native AOT and trimming compatible, Varve's constraints 1 to 5, every third-party package needs an ADR. Fixed layers, dependencies downward, public API baselines, every rule an analyzer that fails the build.

`[D1.23]` (2026-11-03) is superseded by D1.24. It put the rewrite in a new repository.

`[D1.24]` (2026-11-03) **Where it lives.**
- **The definition** lives in decision-driven-design, at `applications/sdlc/product-cli/product-definition.md`. A change to it is a pull request there, ratified by merge. Outside-in therefore crosses two repositories: a definition change merges here before any product-cli change that relies on it, and the product-cli change cites the commit.
- **The tool**, its ADRs, its tests and its release descriptors live in `mindovermachine-dev/product-cli`, which `Hafeok/product-cli` redirects to. There is no new repository.
- **The Rust workspace is frozen by tag.** The tag is `rust-final`, at `70395df`.
  - The first rewrite pull request removes the Rust tree from `main`, `.decisions/` included. From then on, `main` holds the rewrite alone: one toolchain, one CI and one `AGENTS.md`.
  - Everything the rewrite reads from the Rust tool is read at the tag, and nothing at the tag changes. That covers the lift input, the framework CLI scenarios, the behaviour the old crates are read for, and the `.decisions/` ledger that `writ import` reads once.
  - The Rust binary keeps working from its published releases.
- **The Rust tool's open issues** are closed as not carried, or re-filed against the rewrite, when the Rust tree leaves `main`.
- **Retirement** means that the acceptance below holds, the lift tool is deleted, and no further Rust release is made. The tag stays.

`[D1.4]` (2026-10-30, amended by D1.21) **Acceptance.** The Rust tool's export of its self-hosted What is in `pf:` and cannot be byte-identical to an `sdlc:` export. Acceptance therefore goes through a one-time lift.

`[D1.21]` (2026-11-03) **The lift.**
1. **The frozen input.** It is pinned by RDFC-1.0 graph hash, not by bytes, because the Rust tool's Turtle is not byte-stable across builds: its re-export at `70395df` differs in bytes from the committed `.product/products/product-cli/product-cli.ttl` and is isomorphic to it.
   - Repository and commit: `mindovermachine-dev/product-cli` at `70395df`, tagged `rust-final` (D1.24).
   - Command: `product domain export --product product-cli`. The Rust tool has no `--canonical`.
   - Size: 1,412 triples and 289 subjects, of which 32 are blank nodes.
   - Graph hash: `sha256:ad855b900abd76bdc8a26d91ce995e267856dad8c47d15e1ee509f41c5d07e06`. pyoxigraph and Varve agree on it.
2. **The lift map,** frozen, versioned and committed, never regenerated:
   - **Terms.** Every `pf:` class and predicate in the input is either mapped to an `sdlc:` term or dropped by name with a reason.
     - The How kinds are dropped: `ReificationRule`, `Cio`, design-system style and tokens, `versionedAs` and `targetsPlatform`.
     - The ownership edges become `sdlc:within` (`DDD-dec-64` P-2): `inContext`, `ownsDomain`, `ownsSystem`, `systemOf`, `journeyOf` and `boundedBy`.
   - **IRI subjects.** Each gets one minted `P/what/<ULID>`, with the old name as `rdfs:label`. The product IRI P is stated in the lift ADR.
   - **Blank nodes.** All 32 become elements (P-3), each keyed by (owning subject IRI, predicate, its own description, sorted). The key is unique over the frozen input.
     - The 15 `pf:hasAttribute` nodes become `sdlc:Field` elements: `attrName` becomes `rdfs:label`, and `attrType` becomes `sdlc:fieldType`.
     - The 7 `pf:offers` and 10 `pf:surfaces` nodes become `sdlc:Interaction` elements within their UI step.
   - **Stored, not minted.** The ULIDs and the adopted wire names are stored in the map, each wire name with the reference to the review that adopted it. Lifting again therefore reproduces the golden bytes.
   - **Wire names are authored, not carried.** The input has none. The lift ADR states the rule that proposes one for every kind that requires one (`what.md` §6, R-1, R-2), and review adopts each.
3. **Two fixtures.**
   - **The golden fixture.** The lift produces the new tool's canonical export of the self-hosted What. It imports through W1 and carries no violation under its edition. It is reviewed and committed. Lifting again with the same map is checked to reproduce the golden bytes, once, and the result is recorded. The self-hosted What holds no Decider, Projector, scenario, subject kind or scope rule, so this fixture fixes structure and surface only.
   - **The behaviour fixture.** decision-driven-design's `what/examples/acme-shop-5.ttl` and its logic artefacts, at `v0.6.0`, imported through W1. It carries no findings under the edition. Its published element and graph hashes (`vectors-5.json`) are part of the test. *Amended 2026-11-06 (decision-driven-design `DDD-dec-113`, E-5):* it was `acme-shop-4.ttl` and `vectors-4.json`. That graph is pinned by `CUR@1` and `what@4`, and lacks the (Place order, Customer) scenario and the E-7 descriptions; `acme-shop-5.ttl` is it plus both.
4. **Acceptance.**
   - Both fixtures round-trip byte-identically (W7, W8).
   - The conformance suite passes: the framework CLI scenarios, and the seed round-trip property.
   - The lift is a repository tool, not a product verb. It is deleted when the Rust binary is retired.

**Order of work:**

0. `[D1.25]` (2026-11-03) Slice 0, the repository skeleton (ADR-0002, ADR-0003, ADR-0004):
   - the eight layer projects, each with its public API baseline and a test that the layering analyzer refuses an upward reference;
   - the Native AOT publish of the host on every supported runtime in CI, with a smoke test of the published binary;
   - the package register: Varve, the analyzers, and the test-only packages.

   It needs no `sdlc:` edition, so it does not wait for step 1's upstream.
1. Pin the `sdlc:` edition and its shapes; the lift ADR and the lift map. Edition 1 shipped in decision-driven-design `v0.6.0` (`DDD-dec-113`).
2. The canonical graph, element hashes and the exporters (canonical N-Quads with artefacts, sorted Turtle), with their conformance suites; the What-version record; the logic media type's specification page and suite.
3. The lift and both fixtures.
4. Nodes and `validate`, each write a `dpp/1` record (W11).
5. `[D1.13]` (2026-10-30) The authoring loop: proposals and adoption, MCP with the structure phase, and the workbench. From here the main use is dogfooded.
6. Deciders, Projectors and the simulator, with the behaviour phase.
7. Scenarios and the runner protocol.
8. Open questions, and the surface phase.
9. Retire the Rust binary.

## 8. Boundaries and decisions taken

- **Scope.** The What alone: `what.md` (Product Framework §3) and its §6 wire protocol (the old §6.3.1).
  - **Not in it:**
    - the How: contracts, layout model, reification, design-system and content-store catalogues;
    - work units or seams;
    - features, releases, delivery targets or `done`.

    Those are decisions and valuations held in Writ over this tool's export.
  - **Declared targets are in it.** A system's design system and content store, declared as `sdlc:DeclaredTarget` at an edition (`what.md` §4.1, `DDD-dec-57`), are What. Their catalogues are packages; the bindings are Writ's.
  - The framework document stays whole as an open standard; this tool implements one part of it and says which.
- **Licence.** Apache-2.0, from the commit after `rust-final` that replaced the licence (`59553ee`, merged at `53bd547`). MIT governs everything at `rust-final` and before it, and the Rust tool's releases.
- **What carries over from the Rust workspace.**
  - **Carried:**
    - the name and the verb names;
    - `what.md` and its §6;
    - the wire-protocol JSON schemas, as moved into decision-driven-design;
    - the self-hosted What, through the D1.21 lift, as the first fixture;
    - the framework CLI scenarios and the seed round-trip property, as the conformance suite.
  - `[D1.9]` (2026-10-30) `schema/ontology/product-framework.ttl` and `schema/shapes/` are input to `sdlc:` in decision-driven-design and are not carried into this repository.
  - **Not carried:** `ddd`, `spec`, `eval`, `ledger`, codegen, the build seam, `how`, `feature`, `build`, `seam`, `preview`, `target`, `deployable-unit`, `design-system`, `scope`, and the React explorer.
- **No authority, ever.** `[D1.11]` (2026-10-30) The tool records decisions; it never puts one in force. It holds no key and no grant, offers no acceptance under a grant, and knows no Writ position. `dpp/1` leaves authority to profiles (§1.3, §9.4), and this tool's profile claims none. The ledger that lived in the Rust repository is Writ's authority graph now; `writ import` reads the old `.decisions/` once.
- **Two systems, one protocol.** The draft log and Writ's log are two `dpp/1` systems. The draft log holds the author's decisions over the What; Writ's log holds what is in force. They share no position, grant or key; they are joined only by `basedOn` references with pins, which carry provenance and never force. The tool never learns about Writ positions or grants; the moment it does, the boundary has leaked.
- **Decision-driven, like Writ.** The tool holds no key, but the project does.
  - `[D1.22]` (2026-11-03, amending the Draft 3 clause "governed by an embedded `writ` from its first commit") Writ has no implementation yet: its embedded log arrives with Writ #7, and `land` with #8.
  - **Until #7,** this repository's ADRs are files under `docs/decisions/`, under the interim rule of Writ ADR 0008: ADR-level discipline is kept by review, and `main` is fast-forwarded only at an approved, checked head.
  - **From #7,** `writ import` reads them once, with a baseline, and the repository is governed by its embedded `writ`.
  - **From #8,** code lands through `writ land`.

  This is the path Writ takes for its own ADRs.
- **Subjects are What (`what.md` §3.7, adopted from the unmerged v1.11.0 by ruling, 2026-10-28; the term is `SubjectKind`, since "actor" is canon's and "principal" is authority's).**
  - Subject kinds have a nature (human, process, external) and claims.
  - A trigger's `sdlc:subject` sits beside its unchanged `source`, nature matching source, so a What without subjects exports byte-identically.
  - The subject is a fourth argument of `decide`, beside `when` on the wire, never a payload field.
  - Steps offer commands to subject kinds (`sdlc:offeredTo`).
  - A View scope is one rule per subject kind; an absent rule means the kind sees nothing.
  - `sdlc:keyedBy` on the Projector makes scoping a keyed fold at the seam, not a filter over a shared one.
  - Authentication, and with it provider coverage, belongs to the How.
  - Authority within the product stays separate from authority over the specification, which is why Writ's grants are not `sdlc:`.
  - The checks this tool needs that `what.md` §3.7 still marks `[OPEN]` are the subject half of W3 and claim justification. They are in edition 1 as warning shapes (`DDD-dec-113`, E-4), and are built here only by importing that edition.
- **Not in scope.** Code generation of any kind, including verification shells; delivery practice; any model inside a check. The proposer that turns an interview into nodes is an agent driving the verbs, outside the tool, and its output is judged by the same shapes as a human's.

## Cross-repository dependencies

As of 2026-11-06.

| Ruling | Needs | Where | State |
|---|---|---|---|
| D1.19 | the validation regime, and violations separated from warnings | decision-driven-design #49 | **met**: ruled in `DDD-dec-113` (E-1, E-2), landed by mindovermachine-dev/decision-driven-design#59 |
| D1.19, W3, W4 | the five §3.4 and §3.7 shapes not yet in `shapes.ttl` | decision-driven-design #50 | **met**: `DDD-dec-113` (E-4) |
| D1.1, D1.20 | `sdlc:` edition 1 tagged; until then its file hash moves | decision-driven-design | **met**: `v0.6.0`, tag object `bb47a720832c77f6a53c82b90388cd4a2c5c23bf` on `1ab1de005eb60ce2ea019e9942cd52b790aab0e7`, edition hash `sha256:a2006d9da588586bbf7ac19b3eec4861ff5a1aec0006a61784e9e0d842672f29` |
| D1.3, D1.17 | Writ lands canonical N-Quads as the What document, and holds the guest graph under `sdlc:` instead of `pf:` | Writ #22 | open |
| D1.22 | the embedded log (#7) and `land` (#8) | Writ | open |
| element hashes | product-cli's element-hash vectors, offered as a cross-check beside Varve's (`DDD-dec-73`, `DDD-dec-113` E-3) | decision-driven-design (M-12) | to deliver at step 2 |
| D1.3 | RDFC-1.0 in Varve | Varve | **met**: `RdfCanonicaliser` reproduces decision-driven-design's graph hashes |
| D1.19 | SHACL Core with SHACL-SPARQL, AOT-compatible | Varve | **met**: `Varve.Shacl` and `Varve.Shacl.Sparql` agree with pyshacl on both examples |
| D1.1 | `DDD-dec-63` on `main`, and the What half of `sdlc:` published | decision-driven-design | **met** |
| D1.17 | the What-version record's dotted member | decision-driven-design | **met**: fixed by `DDD-dec-63` §6 |
| D1.7 | an RDF form of the logic | decision-driven-design | **withdrawn** with D1.7 (D1.16) |
| D1.24 | the tag `rust-final` at `70395df` | product-cli | **met**: tag object `d0cf1f1ec40eb55c271b8d4dadfefcd260c03312` |
| D1.24 | the Rust tree removed from `main` | product-cli | **met**: mindovermachine-dev/product-cli#166, merged at `53bd54758ba71f7a810f91ddf3a6c83d5e653145` |
| D1.25 | slice 0, the repository skeleton | product-cli | **met**: `4ce90e9` |
| — | `applications/sdlc/README.md` points to the Rust product-cli as the reference implementation | decision-driven-design | amended with this definition's arrival; the Rust tool is the reference until retirement |
