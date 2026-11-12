# Top input

## Relevance (a reader)

# Audience: newcomer

**Trial, `[PROPOSED]`.** Written from Emil's reading of the first brief (2026-11-12): he wants it to say what the thing is and how it works, and does not care that it was rewritten.

| | |
|---|---|
| Who | Someone meeting the product for the first time. |
| Already knows | Software in general. Nothing about this product. |
| Needs | What it is. How it works: what goes into it, what it does with that, what comes out, and who or what uses the result. |
| Does not need | Its history: what it replaces, or that it was rewritten. Its status or drafts. Who authorises it. How it is built. |

## The document's introduction (C0)

Draft 4, 2026-11-03 (Draft 3, 2026-10-30; Draft 2, 2026-10-30; Draft 1, 2026-10-21). Written outside-in: the promise first, the implementation last. Chapters 1 to 6 are the product; chapter 7 is how it happens to be built and may change without the product changing.

This is the definition of the rewritten product-cli. It replaces the Rust workspace of the same name. `[D1.24]` (2026-11-03) It lives here, in decision-driven-design beside the What it implements; the tool, its ADRs and its tests live in `mindovermachine-dev/product-cli` (chapter 7). What carries over is listed in chapter 8; everything else is new, and "it was like that before" is not a reason for anything in this document.

Rulings are marked `[D1.n]` with their date where they land.
- **Drafts 2 and 3.** Draft 2 adds D1.2 to D1.9. Draft 3 adds D1.10 to D1.15, ruled with ADR-0010, ADR-0011 and ADR-0012; they rest on `dpp/1` (specification 1.0, draft of 2026-10-27, decision-driven-design `spec/decision-provenance/dpp-1.md`).
- **Draft 4** adds D1.16 to D1.25, ruled on 2026-11-03. D1.16 to D1.23 come from the gate checks of 2026-11-02 (A1 to A8); D1.24 supersedes D1.23, and D1.25 adds step 0 to the order of work. The checks were run against decision-driven-design `c7424ad`, Varve `c0a776b`, Writ `6737ac9` and the Rust tool `70395df`.
- **Superseded rulings** keep their number, with the ruling that replaces them named in place. The text below states the ruling in force.

## Chapters

### C1 — 1. The promise

**Budget: 70 words.**

The canon's own text of this chapter:

A machine-checkable statement of what a product does, with an executable oracle for its behaviour, exported as one graph that someone else can sign.

Four consequences follow and are the whole product:

- `[D1.10]` (2026-10-30) **The What is authored in conversation, and every step of it is a decision.** An agent proposes; the author watches the graph, its findings and its open questions change live, and adopts or rejects each proposal. Each adoption is a `dpp/1` decision record with its reason, so specification moves at the speed of the conversation and every element of the What traces to the person who adopted it.
- **The What is a graph with shapes, never prose with diagrams.** Anything that cannot be stated as a node, an edge or a shape is not yet specified, and the tool says so rather than accepting it.
- **Behaviour is executable before any code exists.** A Decider and a Projector are simulated sound and complete against scenarios drawn from the flows. The same scenarios later judge realised code through a wire protocol the tool implements.
- **The tool puts nothing in force and decides nothing about realisation.** `[D1.11]` (2026-10-30) It records the author's decisions over the What as `dpp/1` records, which by its profile carry no force. It produces a canonical document. What that document is held against, who accepts it under which grant, and from which position it is in force, belong to Writ.

Everything below is how.

### C2 — 2. Who it is for

**Budget: 35 words.**

Shared summary: It is for three roles on one surface: an author, an agent, and a realiser who needs an oracle to realise against. The author models the product and adopts or rejects the agent's proposals, the agent writes only proposals, and the realiser runs the behavioural-conformance runner against realised code. Neither author nor realiser edits the other's artefact.

### C3 — 3. The surface

**Budget: 60 words.**

The canon's own text of this chapter:

#### C3.1 — Commands

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

#### C3.2 — The draft log

The working copy is a positioned log of its own (Varve, embedded, kept in Git). Every verb is a commit; `diff`, undo and "what changed in this session" are reads over it. Draft positions are local to the author and are not Writ positions. The export is a document, not a position: Writ computes its own delta when it lands it.

#### C3.3 — Proposals and decisions

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

#### C3.4 — The workbench

`[D1.13]` (2026-10-30) `product view` serves a live, local view of the draft log in a browser. It follows the draft log rather than any one writer, so it updates on every new position whoever wrote it: the CLI, an agent over stdio MCP, or an agent over HTTP MCP. It shows:

- the structure, behaviour and surface of the What at the head;
- the session: the current phase, what the last decision changed, and who decided it (agent proposal or author);
- pending proposals with their reasons, findings and alternatives, each with adopt and reject;
- findings (W3, W4) and open questions, as what to answer next.

Its only writes are adopt and reject, and they go through the same verbs as the CLI, so W1, W9 and W12 have one enforcement point. It binds to localhost.

#### C3.5 — Adopting on the fly

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

#### C3.6 — MCP

The same verbs, over stdio or HTTP, in a phase-gated session: structure (§3.0, §3.1), then behaviour (§3.2 to §3.5), then surface (§3.2.1 to §3.2.4), because each derives from the one before.

- Read verbs from an earlier phase stay callable; writes lock to their phase.
- Every write verb of an agent session creates a proposal, and requires a reason.
- Open questions are phase-free and gate advancing.
- There is no adopt, no reject, no land, no grant and no signing on the agent surface: adoption is the author's, in the workbench, at the CLI, or by elicitation answered by the author (D1.15). An agent session ends with an export, which is handed to Writ by whoever holds a grant there.

### C4 — 4. The formats

**Budget: 40 words.**

Chapter introduction (C4): Every format has a specification page and a conformance suite before any implementation, and is under a read-forever rule from the first release.

Section numbers in this chapter and the next are `applications/sdlc/what.md`'s. The mapping from the old Framework sections is `what.md`'s appendix.

Shared summaries of its sections:

- C4.1 (The vocabulary (`sdlc:`)): The vocabulary is `sdlc:`, owned by decision-driven-design; this tool implements it and owns nothing of it, and `pf:` is retired. It is versioned by edition: an export states its edition, a later edition never changes the meaning of an earlier one, and migration is a new export.
- C4.2 (Shapes): The shapes and rules live with the vocabulary, versioned by the same edition, and are one artefact in two roles: the author's feedback in this tool and Writ's enumerated decisions. The binary embeds the edition's files, and the build fails if they do not hash to the pin.
- C4.3 (The canonical export): The canonical export is the graph document, the RDFC-1.0 canonical N-Quads serialisation of the What graph at one draft position, plus the logic artefacts its digests name; the graph document is the only one Writ lands. Two exports of the same draft position are byte-identical, graph and artefacts alike.
- C4.4 (The What-version record): Every export carries its manifest as a What-version `dpp/1` record, which is JSON, not RDF. It holds the ruled shape, a `basedOn` that pins every decision in force at the version, this tool's dotted member, and unhashed `extensions`.
- C4.5 (Decision records and the profile): The draft log exposes its decision records through the `dpp/1` file binding, so a reader with the repository can walk them without the tool. This tool publishes a profile, a format under read-forever, stating that no record of this system binds anyone and requiring no signatures.
- C4.6 (Exports): Every export is a deterministic function of the canonical graph and its logic artefacts; the canonical writer's format is the one Writ lands, and every other export is derived and not landable. A derived format is under read-forever only when it has a specification page and a conformance suite.
- C4.7 (Scenarios and the wire protocol): A scenario is an `sdlc:Scenario` element; this tool owns its authoring and reporting form, and the graph form is the vocabulary's. The wire protocol is the JSON request and response shapes a runner reads on stdin and answers on stdout; its schemas are decision-driven-design's, and this tool implements them.
- C4.8 (Decider and Projector logic): The logic is an authored artefact held by digest, not part of the graph's triples; the graph holds the derived signature, and the simulator refuses logic that disagrees with it. The logic media type is this tool's format, a closed expression grammar, specified with its suite before the Decider slice.

### C5 — 5. The guarantees

**Budget: 20 words.**

Shared summary: Each guarantee is a property test over generated What graphs and scenarios, in a public suite, and every test observes bytes, never a verb's return value. They cover shape before storage, derived signatures, coverage, justification, type boundary, simulation before realisation, canonical export, round-trip, phase order and decision-provenance conformance. The tool holds no key and puts nothing in force, and nothing an agent wrote is in the What unless a person adopted it.

### C8 — 8. Boundaries and decisions taken

**Budget: 15 words.**

Shared summary: The scope is the What alone: the How, work units, features, releases and code generation are not in it. What carries over from the Rust workspace is the name and verb names, `what.md`, the wire-protocol schemas, the self-hosted What as the first fixture, and the conformance suite. The tool records decisions and never puts one in force; the draft log and Writ's log are two `dpp/1` systems joined only by `basedOn` references.

