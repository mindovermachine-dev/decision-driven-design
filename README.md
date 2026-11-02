# Decision-Driven Design

**A method for designing software by its decisions:** map the acts the work consists of, place
each decision where it is resolved, and say which actor, whether person, program or model, makes
each one and who answers for it. This repository is the method's software projection: the step
cards, the claims they rest on, and the decisions that rule them.

> **Ready to try, not ready to use (`DDD-dec-74`).** Only step 1 of ten is ruled, and it is ruled
> *for test*: the claims it rests on are projected, and the independent case that tests them has
> not run. Steps 2 to 10 are `[PROPOSED]`. Try step 1, tell us what happened, and do not rely on
> any of it yet.

**Weakest point.** No step of the method has been exercised on a case outside the framework. Every
example here, including the quick start, was written inside it.

## What it gives you

What step 1 gives you today, and the canon behind it:

- **An address for every act.** Each act occurrence gets a position on declared ground axes plus
  its layer path, with the actor left out. Decisions and actors then have a place to be anchored,
  and every later artefact has an address to attach to (`DDD-ground-06`;
  [step 1](method/01-map-and-index-acts.md)).
- **A causal order instead of timestamps.** Occurrences are ordered by which state changes are in
  whose ground reading, so you can see which acts actually depend on which (`DDD-address-01`).
- **Reuse kept out of identity.** Every occurrence is its own act, and shared code is a
  derivation edge from many occurrences to one component. That is what later lets a change to a
  shared component show its fan-out (`DDD-address-02`, `DDD-address-03`).

All three are **projected**: argued, with falsifiers stated, not yet tested.

## Where it is the wrong tool

- **You need a method that has been shown to work.** None of this one has been, yet. Every step is
  projected or `[PROPOSED]` (`DDD-dec-74`).
- **You can only read the work back from existing code.** Step 1 maps forward from the domain and
  the request, never back from code. Code reuse is not evidence of what the acts are
  (`DDD-address-02`; [step 1](method/01-map-and-index-acts.md)).
- **You cannot say what the ground is.** An address is blind to every axis nobody declared. If the
  ground cannot be declared, the map will look complete and will not be (`DDD-ground-06`).
- **Nobody can rule.** Addresses are relative to a *ruled* decomposition. Without a principal who
  rules it, there is nothing for the map to be relative to (`DDD-ground-06`).

## Status, step by step

| # | Step | Register |
|---|---|---|
| 1 | [Map and index acts](method/01-map-and-index-acts.md) | **Ruled for test.** Claims projected; waits on T2b, the first independent application case |
| 2 | [Anchor authority](method/02-anchor-authority.md) | `[PROPOSED]` |
| 3 | [Surface decisions](method/03-surface-decisions.md) | `[PROPOSED]` |
| 4 | [Declare ground](method/04-declare-ground.md) | `[PROPOSED]` |
| 5 | [Classify closure and set assurance](method/05-classify-closure-and-set-assurance.md) | `[PROPOSED]` |
| 6 | [Allocate](method/06-allocate.md) | `[PROPOSED]` |
| 7 | [Complete accountability](method/07-complete-accountability.md) | `[PROPOSED]` |
| 8 | [Derive forward](method/08-derive-forward.md) | `[PROPOSED]` |
| 9 | [Execute and record](method/09-execute-and-record.md) | `[PROPOSED]` |
| 10 | [Observe and supersede](method/10-observe-and-supersede.md) | `[PROPOSED]` |

The version is the method's (`DDD-dec-75`). It stays below 1.0 until all ten steps are ruled.
A step added or moving register is a MINOR release (`DDD-dec-82`).

## Quick start

[`method/quick-start.md`](method/quick-start.md) runs step 1 on the HTTP slice of Varve's own quick
start, at Varve's release `v0.1.0-preview.15`. The slice is five requests: write a name, delete
it, read now, read as of the first commit, list the commits. You map them into five act
occurrences, give each an address, and order them causally. The as-of read turns out to depend on
the write alone, although it runs after the delete.

Varve is the **subject** of the design, not a dependency. The example is **exposition, not
evidence**. It is falsified by the junior-engineer test: someone at first contact performs the step
and cannot name the value it gave them. Running that test is Emil's act, and it has not been run.

## The repository

| Path | What it is |
|---|---|
| [`method/`](method/) | The step cards and the quick start |
| [`why.md`](why.md) | The theory: where determinations come from, what they cost, and which actor should make each one |
| [`core/claims/`](core/claims/) · [`core/decisions/`](core/decisions/) | The claim graph and the decisions that rule it. A claim file governs its prose |
| [`graph/upstream.yaml`](graph/upstream.yaml) | The actor-general claims this projection pins from the principle repository, [`actor-indexed-determination`](https://github.com/mindovermachine-dev/actor-indexed-determination) |
| [`applications/sdlc/`](applications/sdlc/) | The software-delivery projection: the What, the How and their worked examples |
| [`apparatus/`](apparatus/) | Operational results: encode and verify, the closure principle, tool surfaces |
| [`spec/`](spec/) | The claim format, the release format, the Decision Provenance Protocol |
| [`meta/`](meta/) | The way of working, and every session's record |
| [`scripts/ci.py`](scripts/ci.py) | Every gate, from one entry point. `python3 scripts/ci.py` is what CI runs |

## Community

| | |
|---|---|
| Contributing | [CONTRIBUTING.md](CONTRIBUTING.md) |
| Governance | [GOVERNANCE.md](GOVERNANCE.md) |
| Security | [SECURITY.md](SECURITY.md) |
| Conduct | [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) |
| Licensing | [LICENSING.md](LICENSING.md) |
| Changes | [CHANGELOG.md](CHANGELOG.md) |
| Agents | [AGENTS.md](AGENTS.md) |

Falsifying a core, actor-general claim is an issue for the
[principle repository](https://github.com/mindovermachine-dev/actor-indexed-determination). Trying
the method is an issue here, with the field-report template.

## How this project is run

Decision-Driven Design is run to the **Mind Over Machine open-source stewardship standard**, as it
applies to a specification repository (`DDD-dec-76`). [GOVERNANCE.md](GOVERNANCE.md) states the three
departures and why. **It is developed with AI assistance under Emil's rulings.** Every session leaves
a record in [`meta/sessions/`](meta/sessions/), and every decision is a file with its basis.

## Licence

Specification text is **CC BY-SA 4.0**. Code and schemas are **[MPL-2.0](LICENSE)** (`DDD-dec-79`).
See also [`NOTICE`](NOTICE) and [`LICENSING.md`](LICENSING.md). Releases up to `v0.4.0` remain
available under their earlier licences, as `LICENSING.md` states.
