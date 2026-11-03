# Decision-Driven Design

**A method for designing software by its decisions:** map the acts the work consists of, place
each decision where it is resolved, and say which actor, whether person, program or model, makes
each one and who answers for it. This repository is the method's software projection: the step
cards, the claims they rest on, and the decisions that rule them.

**v0.5.0 is a preview: ready to try, not ready to use (`DDD-dec-74`).** The register of each
reason below is stated beside it, and the [status table](#status-step-by-step) gives each step's.

## Why use it

| You get | Canon | Register |
|---|---|---|
| **An address for every decision.** Every act occurrence gets an address: its position on the ground axes you declared, plus the chain of acts it sits in. Decisions anchor to those addresses through applicability predicates, so a decision that matches no address shows up as a candidate escape instead of hiding | `DDD-ground-06`, `DDD-ground-01` | Projected |
| **The fan-out of a change, before you make it.** A change to a shared component is an escaped decision at every occurrence the change's own decision does not cover. The map lists those occurrences for the person making the change | `DDD-address-02`, `DDD-address-03` | Projected |
| **Which acts depend on which.** Occurrences are ordered by the state changes in each one's reading, not by timestamps. An act depends on another only if it reads what the other changed | `DDD-address-01` | Projected |
| **The right actor for each determination.** Whether a person, a program or a model should make a determination depends on how its result can be checked, and on the arrangement around it, not on the task alone. Change the arrangement and what cannot be discharged moves | `DDD-floor-02` | Projected |
| **Where to invest in checking.** Where results cannot be checked quickly and objectively, you end up relying on choosing the worker instead. The method shows which work that is before you hand it to a model | `DDD-hyp-05` | Projected |
| **One way escapes happen.** Work beyond an actor's capacity escapes where the decisions it sheds carry no verifier; overflow alone produces retries, not escapes. This is sufficient for escape, not the only cause, and it has been reproduced on toy actors so far | `DDD-floor-01` | **Reported** (toy actors) |
| **Agents that drift less.** Long-running agent drift is decisions made with no basis. Grounding an agent in an external claim graph, with a basis cited per decision, is claimed to reduce drift compared with carrying instructions in context. This repository is run that way | `DDD-agent-01` | Projected |
| **Decisions with provenance.** Every decision is a file with its principal, its basis and what it supersedes. Records signed under `dpp/1` can be verified by another system | `DDD-dec-62`, [`spec/decision-provenance/`](spec/decision-provenance/) | Ruled |

What step 1 gives you today, worked through on a real system, is in the
[quick start](#quick-start).

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

## Where it is the wrong tool

- **You can only read the work back from existing code.** Step 1 maps forward from the domain and
  the request, never back from code. Code reuse is not evidence of what the acts are
  (`DDD-address-02`; [step 1](method/01-map-and-index-acts.md)).
- **You cannot say what the ground is.** An address is blind to every axis nobody declared. If the
  ground cannot be declared, the map will look complete and will not be (`DDD-ground-06`).
- **Nobody can rule.** Addresses are relative to a *ruled* decomposition. Without a principal who
  rules it, there is nothing for the map to be relative to (`DDD-ground-06`).
- **You need a method that has been shown to work.** None of this one has been, yet. No step has
  been exercised on a case outside the framework; every example here, including the quick start,
  was written inside it. Every step is projected or `[PROPOSED]` (`DDD-dec-74`), and step 1 waits
  on its first independent application case.

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
