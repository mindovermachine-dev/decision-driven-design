# Decision-Driven Design for software

<!-- ddd:doc
reader: architects, developers and product owners who want to apply the framework to a software product
act: find the document for their task, in the order they will need them
pin: v5.15.2
basis: [term:floor, DDD-frame-01, term:seam-identity, DDD-dec-41, DDD-dec-42, DDD-dec-55, DDD-dec-74, DDD-dec-77, DDD-dec-95]
status: current
supersedes: e5a332d:applications/sdlc/README.md
-->

This folder applies Decision-Driven Design to building software. It gives you one place to say
what a product is and does, one place to say how it is built, and a way to change both under
control: every change is a signed decision by someone allowed to make it.

**How settled this is.** The What and the How are decided, except for points each document marks.
None of it has yet been tried on a real product beyond the worked example. Try it; do not rely on
it yet.

## Where to start

| You want to | Read |
|---|---|
| Say what your product is and does: domains, behaviour, screens, who may act | [`what.md`](what.md) |
| Decide how it is built and deployed, or reuse a vendor's decisions | [`how.md`](how.md) |
| See both working end to end, and run the checker | [`how-examples/`](how-examples/) |
| Decide where your team should verify changes, or read the DORA metrics through the framework | [`production-as-ground.md`](production-as-ground.md) |
| Build a tool that reads, writes, checks or hashes a What | [`what-reference.md`](what-reference.md), and the vocabulary, shapes and checker in [`what/`](what/) |
| Build a tool for How decisions, or the gate that holds them | [`how-reference.md`](how-reference.md) |

Read `what.md` before `how.md`. The How is written against a settled What.

## Two worked examples, and why

The documents here use **Acme Shop**, a small test web shop with one domain and two systems. It
has a complete What, signed decision records for its What and How, and a checker that runs them.

The method's quick start ([`../../method/quick-start.md`](../../method/quick-start.md)) uses
**Varve**, a real open-source system with a short public quick start, to practise mapping acts.

So a reader moving from the method into the What switches examples. Writing Varve's What, so that
one example carries the whole method, is planned but not done *(not settled yet)*.

## How the general framework reads in software

The framework's principle is stated once, in general terms, in the principle repository. In
software it is called the **conservation of specification demand**: for a task at a stated
assurance level, the decisions the task needs are fixed, and every one of them gets made, by
someone, at some price. The words of the general framework read like this here:

| In the general framework | In software |
|---|---|
| A determination | a decision in the work: a feature choice, an architecture decision, a test criterion |
| Ground | what the work reads: the repository, the schemas, the live environment, the source of truth |
| The four places a decision can live | an encoded constraint; a mechanical check; a person's or model's judgment; nobody's (the unhandled case) |
| An actor | a role in the work: a person, a model or a program, each pinned in its own way |
| Seam demand | the contract between roles, and the orchestration that connects them |
| Encoding and verifying | pinning the ground you control; verifying third-party APIs and the live environment |
| Which decisions close | which decisions a model can own, and which need a person |

<!-- ddd:ref id=term:floor -->
<!-- ddd:ref id=DDD-frame-01 -->
<!-- ddd:ref id=term:seam-identity -->

## Three things the framework changes in practice

**Who gets which decision is not a matter of taste.** A model can own a decision when the test of
whether it was decided right can be checked over digital ground. Otherwise it needs a person chosen
for judgment on open questions: a senior engineer, a domain expert. How much autonomy a role can
have is bounded by how far its decisions close.

**Orchestration is a seam, and it has a price.** An orchestrator is cheap to specify and expensive
on every run. It is a bottleneck, and the one place that can poison the whole system. A system
designed this way gets cheaper over time by turning recurring coordination decisions into encoded
rules, each with a check, instead of paying for judgment on every run.

**Third-party and environment ground must be verified on a schedule.** Their truth changes on their
own clock, not on your build. So their checks run on a schedule, and a source you cannot reach is
*unknown*, never a pass ([`../../apparatus/encode-verify.md`](../../apparatus/encode-verify.md)).

## Tooling

[`product-cli`](https://github.com/mindovermachine-dev/product-cli) is the authoring tool for this
application. It manages features, architecture decisions, test criteria and dependencies, builds
the graph, assembles bundles, runs audits and serves the engineering graph. Its companion
orchestration harness is designed against the patterns of the earlier implementation document
(below). Writ, the gate that holds How decisions, is defined but not yet built
([`how.md`](how.md)).

## Not settled yet

- **One example for the whole method.** Varve's What is not written yet (above).
- **The earlier design documents.** Before version 4, this folder had four design documents:
  foundations, an entity reference, autonomy levels and an implementation architecture. They were
  removed at the version 4 restructuring and are recoverable from history at `219ad6c`, under their
  former `docs/` paths. Whether to restore them is not decided. They predate the current register,
  so restoring them would mean reconciling them with canon, which wins wherever they conflict.

## Where this comes from

| Section | Rests on |
|---|---|
| How settled this is | `DDD-dec-74` (ready to try: ruled for test, projected, not reported) |
| What and How | `DDD-dec-41`, `DDD-dec-42` (the What moved here); `DDD-dec-55` and its successors (the How) |
| Two worked examples | `DDD-dec-77` (Varve is the method's example); `DDD-dec-95` (Acme Shop stays for the What and How; Varve's What an open item) |
| How the general framework reads in software | Upstream canon: `term:floor` (`core/03`), `DDD-frame-01`, `term:seam-identity` (`core/06`), actors (`core/04`); `apparatus/encode-verify.md` |
| Three things the framework changes | Closure bounds autonomy (`core/03`); seams are priced (`core/06`); verification on a schedule (`apparatus/encode-verify.md`) |
| The earlier design documents | Removed at commit `219ad6c`; their former paths `docs/01-foundations.md` to `docs/04-implementation.md` |

Upstream references resolve in the principle repository at the pin in `graph/upstream.yaml`. The
earlier text of this page is at `e5a332d`. That text still described the What as "not yet
ratified" and the How as "unruled"; both had landed.
