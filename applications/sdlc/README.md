# The SDLC Projection

**The framework, denominated in software delivery.** This is the agentic/DAG design framework that
constituted the whole of Decision-Driven Design through v3. In v4 it takes its proper place: the
**engineering projection** of the general principle — *Conservation of Specification Demand*, which is
what *Conservation of Determination Demand* is called when the actor is building software.

Nothing here is deprecated. The reframing is a promotion: what looked like the framework was always
*one projection* of it.

---

**Upstream basis.** This document is part of the software projection; it builds on the
principle repo's canon (`actor-indexed-determination`). The `core/NN` references below resolve
there, pinned at a version and a status in `graph/upstream.yaml`:

<!-- ddd:ref id=term:floor -->
<!-- ddd:ref id=DDD-frame-01 -->
<!-- ddd:ref id=term:seam-identity -->

## How this relates to `core/`

| In `core/` (general) | Here (software) |
|---|---|
| Determination | a decision in the SDLC — a feature choice, an ADR, a test criterion |
| Ground | the repo, the schemas, the live environment, the source of truth |
| The four stores | encoded constraint · CI check · human/model judgment · the unhandled case |
| Actor (`04`) | a role in the DAG — human, model, or program, pinned accordingly |
| Seam demand (`06`) | the interface contract between roles; the orchestration layer |
| Encode/verify (`apparatus`) | pinning controlled ground; verifying third-party APIs and live env |
| Floor-in-the-predicate (`03`) | which decisions a model can own (closing predicate) vs. which need a human |

The design docs below predate the `core/` layer. They remain correct as *engineering guidance*; where
they reach for a foundational justification, that justification now lives in `core/`, stated more
generally and more carefully.

---

## The design documents

**The four v3 design documents are not in this tree.** They were removed at the v4 restructuring
(commit `219ad6c`, under their former `docs/` paths) and have not been re-landed; restoring them is
an open decision that has not been taken. They are listed here as the record of what the v3
framework comprised — recoverable from this repository's git history — not as links:

1. **`01-foundations.md`** *(history: `docs/01-foundations.md`)* — LLMs as knowledge forecasters; work as a chain of
   context-conditioned decisions; value actions as the terminus; roles and artifacts; the DAG, not the
   pipeline. *Start here for the software framing.*

2. **`02-entity-reference.md`** *(history: `docs/02-entity-reference.md`)* — the vocabulary made precise: processes,
   decisions, actions, interpretations, roles, artifacts, sessions, schemas, bundles, audits, the
   orchestration system, per-role autonomy.

3. **`03-autonomy-levels.md`** *(history: `docs/03-autonomy-levels.md`)* — the 0–5 autonomy ladder, why autonomy is
   per-role not per-system, and why this structure is what makes Levels 4–5 reachable. *Now with a
   sharper foundation: per-role autonomy is exactly the actor model's pinning resolution (`core/04`),
   and the ceiling on a role's autonomy is set by the closure of its acceptance predicate (`core/03`).*

4. **`04-implementation.md`** *(history: `docs/04-implementation.md`)* — the build architecture: Rust + Oxigraph, curated
   SPARQL for bundle assembly, the event substrate, the worker contract, emergent decisions during
   action, the meta-loop, the model catalog.

Written against v4:

- **[what](what.md)** · moved 2026-10-28, not yet ratified — the opinionated specification of what a software application is and does (Product Framework §3 and §6.3.1, moved by `DDD-dec-41`…), in the identity form of `DDD-dec-63`; with its [ontology, shapes, example and checker](what/)
- **[how](how.md)** · `[PROPOSED]`, unruled — the How as decisions: constraint, binding and contract, anchored in the What, held by Writ, shipped as packages and imported by `basedOn`; with its [vocabulary](how-vocabulary.md) and [worked decisions](how-examples/)
- **production-as-ground** · pre-production predicates close over substitute ground; DORA's four keys instrument the encode/verify gap; the three tiers of feedback loop and which are eliminable

> **Note.** The four historical documents were written before the v4 register (they say "law"
> where `core/` now says "principle," and lean on the pre-review immune framing). If they are ever
> restored to the tree, that reconciliation is the restoring session's work, and the `core/` layer
> wins wherever they conflict. Until then, this README and `production-as-ground.md` are what the
> SDLC projection carries here; the reference implementation is
> [`product-cli`](https://github.com/Hafeok/product-cli).

---

## Where the projection sharpens the design

Three places where `core/` gives the SDLC framework something it did not have before:

**Which role gets which decision** is no longer a matter of taste. `core/03` says a decision can be
owned by a model iff its acceptance predicate closes over digital ground; otherwise it needs an actor
selected for competence on open predicates (a senior, a domain expert). *Autonomy is bounded by
closure.*

**The orchestration layer is a seam**, and `core/06` prices it: an orchestrator is cheap to specify
and expensive per run, a bottleneck, and the poisonable centre of the system. The compound move —
harvesting recurring coordination decisions into encoded rules, with a check on each — is how a
DDD-shaped system gets cheaper over time instead of paying full judgment cost on every run.

**Verification of third-party and environment ground** is not optional and not build-triggered.
`apparatus/encode-verify.md` says why: their truth moves on their clock, so the check must run on a
schedule, and an unreachable source is `Unknown`, never a pass.

---

## Reference implementation

**[`product-cli`](https://github.com/Hafeok/product-cli)** — the authoring layer for this projection:
owns features, ADRs, test criteria, dependencies; builds the derived graph; assembles curated bundles;
runs audits; serves the engineering graph. The companion orchestration harness is designed against the
patterns in `04-implementation.md`.
