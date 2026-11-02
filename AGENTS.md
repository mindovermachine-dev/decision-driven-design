# AGENTS.md

Guidance for agents working in the `decision-driven-design` repository. This file is the
tool-neutral entry (`DDD-dec-81`, item 7); `CLAUDE.md` and any other tool's instruction file point
here rather than repeating it.

## What this repo is

**This repository is the software projection (split per `DDD-dec-04`).** The actor-general
theory — the numbered core documents and the canonical term graph — is **canon in the principle
repository** (`actor-indexed-determination`, pinned at the tag named in `graph/upstream.yaml`,
which is authoritative), not here. Do not add or edit core
theory documents in this repo; canon changes are issues and PRs against the principle repo.
This repo holds the software apparatus, the SDLC and organisation-design projections, the graph
tool's claims (`core/claims/`: `org`, `tool`, `sim`), and the program's decisions
(`core/decisions/`). Shared claims are consumed by pin, not copy — `graph/upstream.yaml`, checked
by `scripts/validate-core-order.py` against a shallow clone of the pinned ref.

The framework is a **claim graph**, not a set of documents. Files are a storage format; the
graph is the object. Read `meta/way-of-working.md` — it governs the repo and every project that
projects from it, and where it and older material disagree, it wins. It defines the three layers
(framework, program in `meta/`, projections), the status vocabulary, and the correction loop
**repo → program → projection → repo**.

Then, before changing any claim or converting any prose:

- `spec/claim-format.md` — the claim schema (format version 1) and its validation rules.
- `meta/conversion-protocol.md` and `.claude/skills/claim-conversion/` — how `core/` prose
  becomes claim files under `core/claims/`.
- `meta/graph-tool-ontology.md` — the claim/decision ontology; the load-bearing edge is
  `decision --basedOn--> claim`.

## Working on canon

**The repo is ground truth, always.** Verify against the live repo before landing anything in
`core/`; never carry a claim's statement, status, or evidence on the confidence of prose, and
where evidence is executable, verify against a fresh run of the asset. Computations that back a
reported claim live in `core/assets/` and must reproduce — a claim whose computation fails
demotes until fixed.

- **Canon authority lives in the claim files.** For a converted document, `core/claims/*.yaml`
  governs; the prose is its exposition. Prose that contradicts its claim is a bug in the prose —
  flag it in the claim's `notes:`, do not silently harmonise.
- **Never present an identity holding as evidence for the framework.** State which is arithmetic
  and which is a modelling claim, always (`meta/way-of-working.md` §6).
- **Flag, don't guess.** Reasoning not confirmed by canon or a named principal is marked
  (`UNVERIFIED — Emil review`), never asserted. Surfacing these is half the point of the work.
- **Validate before commit.** `python3 scripts/validate-claims.py core/claims/` and, for
  decisions, `python3 scripts/validate-claims.py core/decisions/ --decisions` must pass.
  `python3 scripts/ci.py` runs every gate in order (claims, decisions, core order and pins, the
  What, the How examples, the checker fixtures) and is what CI runs; it must pass before a push.
  Its dependencies are in `scripts/requirements.txt`, or use the devcontainer.

## Cite claim IDs in commit messages

**Every commit that changes canon must cite the claim or decision IDs it rests on**, as a
`Basis:` line in the commit message (e.g. `Basis: DDD-tool-01; DDD-dec-03`), and name the
claim IDs it touches. This is not bookkeeping: it is `DDD-agent-01` applied to this repo's own
agents. That claim holds that long-running agent drift is **escaped decisions caused by basis
loss** — context decay removes claim nodes from the agent's ground, so later edits revert to
model priors with no `basedOn` edge to the declared claims. The remedy is **basis as query, not
context residue**: fetch the governing claim from `core/claims/` and cite it, rather than
trusting that it is still carried in context. An edit to `core/` whose commit message names no
basis is, by this repo's own ontology, a candidate escaped decision about the framework itself.

Retired claims are never deleted — they stay in the graph with the correction that killed them
(`core/claims/DDD-measure-08.yaml` is the exemplar). IDs are never reused; renumbering is
forbidden.
