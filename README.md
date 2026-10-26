# Decision-Driven Design

<!-- ddd:charter
reader: anyone arriving at the repository
act: orient, by finding what this repository holds and where to start
opener: ddd:doc
authority: none
exempt: [LICENSE.md, CHANGELOG.md, CLAUDE.md]
-->

**Charter.** Root documents are for anyone arriving. Their act is to orient. The licence, the changelog and the agent guidance keep their own formats. Every document in this repository opens with its reader and act; `spec/doc-format.md` says how.

**The software projection of the Conservation Principle of Determination Demand** — a theory of where
determinations come from, what they cost, and which actor should make each one.

> **This repository was split (`DDD-dec-04`).** The actor-general theory now lives in the principle
> repository, [`actor-indexed-determination`](https://github.com/Hafeok/actor-indexed-determination)
> (split at tag `v5.0.0`, pin now advanced — see `graph/upstream.yaml`); *decision-driven-design* is
> its **software projection** and keeps the name. Core canon is consumed by pin, not copy — see [`graph/upstream.yaml`](graph/upstream.yaml). Falsification
> of a core claim is an issue for the principle repo; software apparatus and domain projections are
> issues here. What remains in this repository: the tool contracts and apparatus, the SDLC and
> organisation-design projections, the graph tool's claims and the program's decisions.

The framework is a **claim graph**: every claim it makes is a node with a status, evidence, and a
falsifier, stored as data and validated against a versioned schema. It remains deliberately **smaller
and better-attributed** than v3 — and says exactly which of its claims are `established` (argued
internally and unchallenged; four claims, all formal — not external validation), `reported` (at
least one reproducing computation), or still `projected` (a declared falsifier nobody has met).

---

## Start here: the one idea

Four classical results govern how work is allocated in engineered systems — Brooks's essential
complexity, Tesler's conservation of complexity, Ashby's requisite variety, Meyer's contracts. Each
quantifies over an **actor**: the thing that makes a determination against some ground. **Each of
them holds that actor largely fixed.** They had little reason to vary it — for the whole history of
these results there were two kinds of determiner, a person or a program, and the gap between them
was a light switch, not a spectrum.

A third kind now exists: **non-deterministic, yet with a distribution that can be frozen by binding.**
Decision-Driven Design is what you get when you **make the actor an explicit parameter** those
results hold largely fixed. The framework indexes their allocation questions to the arrangement; its
contribution is stated against those literatures, not against their absence.

Two claims follow, and they are the framework's core contribution — both **projected**: argued,
with declared falsifiers nobody has met:

1. **The irreducible floor of a task is a property of its *acceptance predicate*, not of the task.**
   Zero where you can check the answer; non-zero where you cannot; and *whether you can* is, in
   general, undecidable. *(`DDD-floor-02`, **projected**)* → [`core/03-the-floor.md`](https://github.com/Hafeok/actor-indexed-determination/blob/main/core/03-the-floor.md)

2. **Selection intensity is inversely proportional to acceptance-predicate closure.** *Training* is
   what you do when you can check the work. *Selection* is what you do when you cannot — you check the
   worker instead. This is falsifiable across professions. *(`DDD-hyp-05`, **projected**)*
   → [`core/04-actors.md`](https://github.com/Hafeok/actor-indexed-determination/blob/main/core/04-actors.md)

And, new in 4.1: a measure for the closing region. The chain-rule identity is arithmetic
(`DDD-measure-02`, **established**, formal); the identification of specification demand with the
Shannon entropy of the verdict is a modelling claim (`DDD-measure-01`, **projected**) — the
identity holding is not evidence for the identification
([`core/09`](https://github.com/Hafeok/actor-indexed-determination/blob/main/core/09-the-measure.md)). The measure is defined exactly where the predicate closes,
and is undefined at the floor.

And a prediction: **model actors outperform human actors exactly where the acceptance predicate
closes, and underperform exactly where it does not — the gap tracks *closure*, not *difficulty*.**

---

## What this is, and is not

**It is** a two-primitive theory (decisions, and the ground they are determined against), an
allocation lens (four stores: encoded, mechanically checked, judged, escaped), and an actor model
(pinning resolution, the floor-in-the-predicate, seam composition).

**It is not** a new physical law. The conservation claim is **Tesler's Law of Conservation of
Complexity, generalised** — denominated in decisions, with a fourth store (the *escaped* one Tesler
lacked) and an assurance-level bound. It has **no measurable unit**, so it is a **principle**, not a
law, and the repository says so throughout. See [`core/01-the-principle.md`](https://github.com/Hafeok/actor-indexed-determination/blob/main/core/01-the-principle.md)
and, for the full record of what was corrected and why,
[`meta/lineage-and-limits.md`](https://github.com/Hafeok/actor-indexed-determination/blob/main/meta/lineage-and-limits.md).

We publish the review and the retreats as first-class documents. A framework that states what it
cannot support is worth more than one that overclaims.

---

## Reading order

### Core — the theory (upstream)

The actor-general theory — `00` primitives through `13` delivery, the canonical term graph, and the
reproduction assets — is **canon in the principle repository**,
[`actor-indexed-determination`](https://github.com/Hafeok/actor-indexed-determination), at the tag
pinned in [`graph/upstream.yaml`](graph/upstream.yaml), which is authoritative for the version.
It is not duplicated here. This repository pins the specific claims it depends on in
[`graph/upstream.yaml`](graph/upstream.yaml); read the theory in the principle repo's `core/`.

The load-bearing, falsifiable claims — the floor is in the acceptance predicate (`DDD-floor-02`,
projected), selection intensity tracks predicate closure (`DDD-hyp-05`, projected), demand is the
Shannon entropy of the verdict (`DDD-measure-01`, projected), overflow ∩ open is the mechanism of
capacity-generated escape (`DDD-floor-01`, reported) — all live upstream. Falsification of any of them is an issue against the principle repo, not this one.

### Apparatus — the mechanisms

Operational results that fall out of the core. Read as needed.

| Document | What it gives you |
|---|---|
| [`apparatus/encode-verify.md`](apparatus/encode-verify.md) | *Encode ground you control; verify ground you don't* — and verify on a schedule |
| [`apparatus/closure-principle.md`](apparatus/closure-principle.md) | *An actor's own output is not ground* — poisoned ground, and why Terraform can delete your database |
| [`apparatus/adversarial-ground.md`](apparatus/adversarial-ground.md) | The attack surface of an actor is its ground, not its logic — across three fields |
| [`apparatus/the-skill-floor.md`](apparatus/the-skill-floor.md) | A skill without a per-invocation verifier is floor-exposed by construction |
| [`apparatus/prefix-stability.md`](apparatus/prefix-stability.md) | A prefix is a dependency chain: Martin's SDP, the optimal ordering, and cache invalidation as a specification audit |
| [`apparatus/tool-surfaces.md`](apparatus/tool-surfaces.md) | Tools reallocate demand: exporters, resolvers, verifiers — and why class depends on the task, not the tool |
| [`apparatus/tool-contract.md`](apparatus/tool-contract.md) | What a tool must declare for a DDD-native local agent; why the harness binds tools and the model never picks them |

### Applications — the projections

The framework, denominated in a domain.

| Document | Domain |
|---|---|
| [`applications/sdlc/`](applications/sdlc/) | Software delivery. What the tree carries today: the section README and `production-as-ground.md`. The four v3 design documents live in this repository's git history, not in the tree — see the section README for what they were and where they sit |
| [`applications/sdlc/production-as-ground.md`](applications/sdlc/production-as-ground.md) | Production is the only real ground; DORA read as demand; which feedback loops are waste |

### The graph — claims and decisions as data

The framework as nodes. Files are storage; the graph is the object.

| Path | What it is |
|---|---|
| [`core/claims/`](core/claims/) | One YAML node per claim (`DDD-<area>-<nn>`), with status, evidence, and falsifier. Canon authority for a converted claim lives here, not in its prose |
| [`core/decisions/`](core/decisions/) | Decision nodes (`DDD-dec-NN`); the load-bearing edge is `decision --basedOn--> claim` |
| [`spec/claim-format.md`](spec/claim-format.md) | The claim schema (format version 1) and its validation rules |
| [`scripts/validate-claims.py`](scripts/validate-claims.py) | Validates `core/claims/` and `core/decisions/` against the spec |
| [`validate-core-order.py`](validate-core-order.py) | Validates docs, embeds and the cross-repo pins. **Canonical invocation: `python3 validate-core-order.py core/`** — run against the repository root (`.`) it misreads this repository's own registry ids and reports spurious E13 errors on a clean tree; a fix for that mode is tracked, the `core/` invocation is authoritative |

### Meta — the honesty layer and the program

| Document | What it is |
|---|---|
| [`meta/way-of-working.md`](meta/way-of-working.md) | How work on the framework is structured: the graph model, projections, the correction loop. Governs the repo |
| [`meta/conversion-protocol.md`](meta/conversion-protocol.md) | How `core/` prose becomes claim files |
| [`meta/graph-tool-ontology.md`](meta/graph-tool-ontology.md) · [`meta/graph-tool-mvp.md`](meta/graph-tool-mvp.md) | The claim/decision ontology and the tool's MVP sketch |
| `meta/lineage-and-limits.md` (upstream) | Full attribution, corrections, retreats, and the open falsification debts — canon in the principle repo |
| [`meta/consolidated-state.md`](meta/consolidated-state.md) | Projection-local status (org, outreach, product); shared claims resolve upstream |
| [`graph/upstream.yaml`](graph/upstream.yaml) | The cross-repo pins: every upstream id this repo depends on, at a version and a status |

Danish glossary of core terms: in the principle repo (`i18n/ordliste-dansk.md`).

---

## What changed from v3

v3 was the agentic-design framework: decisions as the unit of work, a DAG of roles, artifacts with
schemas, backed by [`product-cli`](https://github.com/Hafeok/product-cli). Its reframing as the
**engineering projection** of the general principle stands — that is what it always was. Its four
design documents, however, are **not in this tree**: they were removed at the v4 restructuring and
survive in git history; restoring them is an open decision that has not been taken. What the
projection carries in the tree today is [`applications/sdlc/`](applications/sdlc/)'s README,
`production-as-ground.md`, and the reference implementation. What v4 adds is the layer *beneath*
it: the theory that explains why the DAG design works, and the actor model that says which node
each determination belongs to.

The register also changed. Following external review:

- **"Law" → "Principle."** No physical-law status without a measurable quantity (which we do not have;
  Ashby did, and even he refused the term).
- **Conservation** holds as an accounting identity *within a fixed decomposition* — re-decomposing
  *relocates* demand into the seam (a cleaner split pre-pays more into the interface contract; the
  total is invariant), so the decomposition is the highest-leverage decision. → [`core/09`](https://github.com/Hafeok/actor-indexed-determination/blob/main/core/09-the-measure.md) §4, `DDD-measure-03`.
- **The immune-system "licensing" argument** is demoted to a suggestive parallel with known
  disanalogies; **CRISPR** is the accurate compound-platform instance.
- **The zero-floor postulate** is retreated to **the floor-in-the-predicate** result, which is
  sharper and survives the theoretical limits (Rice, inevitable model error, collective tacit
  knowledge).

Full record: [`meta/lineage-and-limits.md`](https://github.com/Hafeok/actor-indexed-determination/blob/main/meta/lineage-and-limits.md).

---

## Status

This is a working specification under active revision. The strongest claims — the floor-in-the-
predicate, and *selection intensity tracks predicate closure* — are **falsifiable**, and the
conditions are stated in the documents. Live status is now in the graph: every claim carries a
status (`established` / `reported` / `projected` / `retired`) in [`core/claims/`](core/claims/).
The counting-procedure debt — a measure of governing-decision demand — is **addressed for closing
predicates** by the measure: the conservation identity is arithmetic (`DDD-measure-02`,
established) and the identification of demand with verdict entropy is a modelling claim
(`DDD-measure-01`, **projected**); off closing predicates it is marked as a **boundary, not an
open debt**. The framework books its remaining debts openly ([`meta/`](meta/)).

Reference implementation: [`product-cli`](https://github.com/Hafeok/product-cli) (the authoring layer
for the SDLC projection).

## Standing on

Tesler (conservation of complexity) · Ashby (requisite variety) · Brooks (essential complexity) ·
Meyer & Hoare (contracts) · Saltzer, Reed & Clark (end-to-end) · Kalman (observability) · Polanyi &
Collins (tacit knowledge) · Rice (undecidability) · Edelman & Gally (degeneracy). Full attribution in
[`meta/lineage-and-limits.md`](https://github.com/Hafeok/actor-indexed-determination/blob/main/meta/lineage-and-limits.md).

## License

Spec text: **CC BY 4.0**. Any code and schemas: **Apache-2.0**.
