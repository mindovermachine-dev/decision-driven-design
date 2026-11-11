# The SDLC projection — the framework, denominated in software delivery

<!-- ddd:doc
reader: architects, developers and product owners applying Decision-Driven Design to a software product, and tool builders implementing it
act: find the document for their task, know how settled each one is, and see how the general framework reads in software
pin: v5.15.2
basis: [term:floor, DDD-frame-01, term:seam-identity, DDD-dec-41, DDD-dec-42, DDD-dec-64, DDD-dec-55, DDD-dec-119, DDD-dec-85, DDD-dec-86, DDD-dec-113, DDD-dec-114, DDD-dec-115, DDD-dec-95]
status: current
supersedes: 84aa466:applications/sdlc/README.md
-->

This folder is the **engineering projection** of the general principle. The agentic/DAG design
framework constituted the whole of Decision-Driven Design through v3. In v4 it takes its proper
place: *Conservation of Specification Demand* is what *Conservation of Determination Demand* is
called when the actor is building software.

Nothing here is deprecated. The reframing is a promotion: what looked like the framework was always
*one projection* of it.

**Upstream basis.** This document builds on the principle repository's canon
(`actor-indexed-determination`). The `core/NN` references below resolve there, pinned at a version
and a status in `graph/upstream.yaml`:

<!-- ddd:ref id=term:floor -->
<!-- ddd:ref id=DDD-frame-01 -->
<!-- ddd:ref id=term:seam-identity -->

## The documents here

| Document | For | How settled it is |
|---|---|---|
| [`what.md`](what.md), with its [ontology, shapes, examples and checker](what/) | The opinionated specification of what a software application is and does: domains, behaviour, screens, who may act, and the behavioural-conformance wire. Moved here from the Product Framework (its §3, and the §6.3.1 wire protocol), in the ruled identity form | Ruled, and ratified by the merge of the move. One point is *(open)*: whether an adopter may register abstract interaction objects, which is the How's open question |
| [`how.md`](how.md), with its [vocabulary](how-vocabulary.md) and [worked decisions](how-examples/) | The How as decisions: constraint, binding and contract, anchored in the What, held by Writ, shipped as packages and imported by `basedOn` | Ruled. What the How left "not ruled separately" until its merge was ratified by that merge. One point is *(open)*: whether adopters may register What kinds. Three of its readings are *(Claude's reading, not yet confirmed by Emil)*: the baseline's ratchet semantics and an earlier decision's consequence for declared gaps (both §8.2), and the vocabulary's namespace IRI, under which nothing is served yet. |
| [`authority.md`](authority.md), with its [vocabulary](authority-vocabulary.md) and [reference evaluator](authority/) | The authority profile: what makes a decision in force in a product, who may make it so, and how that authority is founded, delegated and transferred | Ruled, and ratified by the merge of its pull request. Its vocabulary shares the namespace reading above *(Claude's reading, not yet confirmed by Emil)* |
| [`sdlc.md`](sdlc.md), with its [act map, record shape and checker](acts/) | The SDLC as an arrangement: the How owner's, from a released issue to production, dark behind a toggle. Issues drive agent sessions started by a label (Claude Code Action first); takt's `ready/<N>` shape with Varve's force and no squash; Varve's identity map ported; every occurrence recorded as graph data from edition 1, with the DORA computations over that record | Ruled |
| [`production-as-ground.md`](production-as-ground.md) | Pre-production predicates close over substitute ground; DORA's four keys instrument the encode/verify gap; the three tiers of feedback loop and which are eliminable | Reported, partially: a retrodiction against DORA's published findings, not a statistical test |
| [`product-cli/product-definition.md`](product-cli/product-definition.md) | The definition of the rewritten product-cli, the tool that implements the What | A product definition in drafts, with its rulings dated where they land |

**The What is owned in the PDLC and read here as ground** ([`../pdlc/`](../pdlc/README.md)). It
stays in this directory, where it was placed, and the SDLC never writes it.

## How the general framework reads in software

| In `core/` (general) | Here (software) |
|---|---|
| Determination | a decision in the SDLC — a feature choice, an ADR, a test criterion |
| Ground | the repo, the schemas, the live environment, the source of truth |
| The four stores | encoded constraint · CI check · human/model judgment · the unhandled case |
| Actor (`04`) | a role in the DAG — human, model, or program, pinned accordingly |
| Seam demand (`06`) | the interface contract between roles; the orchestration layer |
| Encode/verify (`apparatus`) | pinning controlled ground; verifying third-party APIs and live env |
| Floor-in-the-predicate (`03`) | which decisions a model can own (closing predicate) vs. which need a human |

## Where the projection sharpens the design

Three places where `core/` gives the SDLC framework something it did not have before:

**Which role gets which decision** is no longer a matter of taste. `core/03` says a decision can be
owned by a model if and only if its acceptance predicate closes over digital ground. Otherwise it
needs an actor selected for competence on open predicates (a senior, a domain expert). *Autonomy is
bounded by closure.*

**The orchestration layer is a seam**, and `core/06` prices it: an orchestrator is cheap to specify
and expensive per run, a bottleneck, and the poisonable centre of the system. The compound move,
harvesting recurring coordination decisions into encoded rules with a check on each, is how a
DDD-shaped system gets cheaper over time instead of paying full judgment cost on every run.

**Verification of third-party and environment ground** is not optional and not build-triggered.
[`apparatus/encode-verify.md`](../../apparatus/encode-verify.md) says why: their truth moves on their
clock, so the check must run on a schedule, and an unreachable source is `Unknown`, never a pass.

## Reference implementation

**[`product-cli`](https://github.com/mindovermachine-dev/product-cli)** is the reference
implementation: the authoring layer for this projection. It owns features, ADRs, test criteria and
dependencies; builds the derived graph; assembles curated bundles; runs audits; and serves the
engineering graph. The companion orchestration harness is designed against the patterns in
`04-implementation.md` (one of the v3 design documents below).

That describes the Rust tool, which is the reference until its retirement. It is frozen at the tag
`rust-final`. Its rewrite implements the What alone, `what.md` and its §6 wire protocol, and records
the author's decisions over it as `dpp/1` records that carry no force. The rewrite is defined here,
beside the What it implements: [`product-cli/product-definition.md`](product-cli/product-definition.md).
Its code, ADRs and tests stay in the product-cli repository.

## The four v3 design documents

**They are not in this tree.** They were removed at the v4 restructuring (commit `219ad6c`, under
their former `docs/` paths) and have not been re-landed. Restoring them is a decision that has not
been taken *(open)*. They are listed here as the record of what the v3 framework comprised,
recoverable from this repository's git history, and not as links. They predate the `core/` layer.
They remain correct as *engineering guidance*; where they reach for a foundational justification,
that justification now lives in `core/`, stated more generally and more carefully.

1. **`01-foundations.md`** *(history: `docs/01-foundations.md`)*: LLMs as knowledge forecasters;
   work as a chain of context-conditioned decisions; value actions as the terminus; roles and
   artifacts; the DAG, not the pipeline. *Start here for the software framing.*
2. **`02-entity-reference.md`** *(history: `docs/02-entity-reference.md`)*: the vocabulary made
   precise: processes, decisions, actions, interpretations, roles, artifacts, sessions, schemas,
   bundles, audits, the orchestration system, per-role autonomy.
3. **`03-autonomy-levels.md`** *(history: `docs/03-autonomy-levels.md`)*: the 0–5 autonomy ladder,
   why autonomy is per-role not per-system, and why this structure is what makes Levels 4–5
   reachable. *Now with a sharper foundation: per-role autonomy is exactly the actor model's pinning
   resolution (`core/04`), and the ceiling on a role's autonomy is set by the closure of its
   acceptance predicate (`core/03`).*
4. **`04-implementation.md`** *(history: `docs/04-implementation.md`)*: the build architecture:
   Rust + Oxigraph, curated SPARQL for bundle assembly, the event substrate, the worker contract,
   emergent decisions during action, the meta-loop, the model catalog.

The four were written before the v4 register: they say "law" where `core/` now says "principle",
and lean on the pre-review immune framing. If they are ever restored to the tree, that
reconciliation is the restoring session's work, and the `core/` layer wins wherever they conflict.

## Not settled yet

- **The four v3 design documents** *(open)*: whether to restore them. Restoring them would put the
  v3 engineering guidance back in the tree, reconciled to the v4 register.
- **The `sdlc:` namespace IRI** *(Claude's reading, not yet confirmed by Emil)*: no IRI under
  `/ns/sdlc` is served or registered yet, and the choice is Emil's. Both vocabularies use it.
- **Whether an adopter may register What kinds** *(open)*, including abstract interaction objects:
  `what.md` and `how.md` both point to it. Deciding it would say whether such a kind is a
  vocabulary change in this repository or something an adopter can add.
- **Per document.** Each document above lists its own open points under its own "Not settled yet".

## Where this comes from

| Section | Rests on |
|---|---|
| The engineering projection; the mapping table; where the projection sharpens the design | Upstream canon at the pin: `term:floor` (`core/03`), `DDD-frame-01`, `term:seam-identity` (`core/06`), actors (`core/04`); `apparatus/encode-verify.md` |
| `what.md`, ruled and ratified | `DDD-dec-41` (the move), `DDD-dec-42` (placed in this directory), `DDD-dec-63` (identity form), `DDD-dec-64` (the move's own choices); ratified by the merge of PR #42 (`2b6e4a7`), each decision naming the pull request's acceptance as the ratification act |
| `how.md`, ruled | `DDD-dec-55` to `-61`, superseded on the same terms by `DDD-dec-65` to `-71`; ratified by the merge of PR #41 (`1d0f40c`); `DDD-dec-119` (Round 2 of `meta/sessions/2026-11-09-applications-for-readers-redo/`): the parts "not ruled separately" were ratified by that merge. The earlier text of this page called `how.md` "`[PROPOSED]`, unruled"; that was stale |
| `authority.md`, ruled | `DDD-dec-85`, `-86`, `-92`, `-93`; ratified by the merge of PR #45 (2026-11-02) |
| The `sdlc:` namespace IRI, a reading | `how-vocabulary.md` and `authority-vocabulary.md`, each marking it `UNVERIFIED — Emil review` |
| `sdlc.md`, ruled | `DDD-dec-115` (S-11: Round 28 ruled its proposals; Round 30 entered by amendment) |
| `production-as-ground.md` | its own status line, "reported, partially" |
| `product-cli/product-definition.md` | its own drafts and rulings; sdlc edition 1, `DDD-dec-113` |
| The What owned in the PDLC, read here as ground | `DDD-dec-114`, Round 8 ("Stays, read as ground"); `DDD-dec-42` placed it here |
| Reference implementation | product-cli; the rewrite's definition in `product-cli/product-definition.md` |
| The four v3 design documents | Removed at commit `219ad6c`, former paths `docs/01-foundations.md` to `docs/04-implementation.md` |
| How this page is written | `DDD-dec-94`, `DDD-dec-95` |

The earlier text of this page said that, until the v3 documents are restored, "this README and
`production-as-ground.md` are what the SDLC projection carries here". That stopped being true when
`what.md`, `how.md`, `authority.md` and `sdlc.md` landed, and the sentence is removed. The earlier
text is at `84aa466:applications/sdlc/README.md`.
