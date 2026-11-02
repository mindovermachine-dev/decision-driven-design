# Decision-Driven Design for organisations — four predictions to test

<!-- ddd:doc
reader: people who design or run organisations, deciding whether the framework says anything about how theirs works
act: understand the four predictions the framework makes about organisations, and how each would be shown wrong
pin: v5.15.2
basis: [DDD-org-01@projected, DDD-org-02@projected, DDD-org-03@projected, DDD-org-04@projected, DDD-dec-05, DDD-dec-40]
status: current
supersedes: e5a332d:applications/organizations/README.md
-->

Use this if you design or run an organisation and want to know what Decision-Driven Design
predicts about it. There is no method here yet, only four predictions. Each is stated with the
observation that would show it wrong, so you can test it against what you see.

**How settled this is.** All four are argued and none has been tested. Treat them as hypotheses
worth checking, not as findings. This folder holds no documents of its own beyond this page. It
becomes a fuller application only when it has its own documents and someone outside the project
who can check them.

The four use one idea throughout. An organisation's working assumptions, priorities and decisions
form a graph: decisions rest on claims, and claims can be more or less established. **Graph
discipline** is how well an organisation keeps that graph honest. It marks how established each
claim is at the point where someone relies on it. It records what each decision rests on, and it
sends corrections back to one source of truth.

## 1. Graph discipline predicts how expensive change is

<!-- ddd:ref id=DDD-org-01 -->

Organisations that keep their decision graph honest change course more cheaply. They lose less
trust by presenting a guess as a fact, and they review decisions faster after a core assumption
changes.

> Graph discipline — status floors at the consumer boundary, manifests, correction flow to a
> single canon — predicts organisational outcomes: pivot cost, trust damage from shipping
> projected claims as established, decision-review latency after thesis change.

**It is wrong if** organisations that measurably differ in graph discipline show no difference in
pivot cost or correction latency, once size and sector are controlled for.

## 2. Hard-to-reverse decisions on weak assumptions are where the cost hides

<!-- ddd:ref id=DDD-org-02 -->

A decision that is expensive to reverse, resting on an assumption nobody has established, is
fragile. Such decisions are where the cost of a change of direction piles up, and where incidents
reveal cascades. Most organisations cannot see them, because they record no status for their
assumptions.

> The Stable Dependency Principle, statused: decisions whose reversal cost exceeds what their basis
> claims' hazard can absorb (high commitment level on low-status claims) concentrate pivot cost and
> produce incident-discovered cascades; organisations cannot see these violations because their
> assumption layer carries no status field.

**It is wrong if** decisions flagged as fragile (how weak their assumptions are, times how many
decisions depend on them, times reversal cost) cause no more rework or incident findings than
unflagged decisions of the same size.

## 3. Priority is a decision, and should rest on stated value

<!-- ddd:ref id=DDD-org-03 -->

A backlog ordered by decisions that rest on stated, statused claims about value churns less and
predicts delivered value better than one ordered by intuition. Claims are prioritised by what
learning their truth is worth. Decisions are prioritised by cost of delay, cost of reversal and
how ready their basis is. Roadmap churn is what happens when a claim about value is quietly
downgraded and nothing records it.

> Priority as a governed decision: backlogs ordered by decisions basedOn statused value-claims —
> with claim priority set by value of information and decision priority by cost of delay, reversal
> cost, and basis readiness — churn less and predict delivered value better than intuition-ordered
> backlogs; roadmap churn is the cascade from silently demoted value-claims.

**It is wrong if** teams that do this show no less roadmap churn and no better value prediction
than matched teams that order by intuition. It is also wrong if, on audit, churn events do not
trace back to changes in the status of value claims.

## 4. Industries formalise in proportion to reversal cost and feedback delay

<!-- ddd:ref id=DDD-org-04 -->

Permits, licensing, stage gates and mandatory inspection are graph discipline built into an
industry. How much of it an industry has is predicted by how costly its mistakes are to reverse
and how slowly it learns of them. Construction and manufacturing formalised because their
mistakes are irreversible. Software stayed informal because retries are cheap. The pressure on
software to formalise rises with the stakes, and with agents making code cheap to generate while
checking it stays expensive.

> Cross-domain retrodiction: the intensity of an industry's institutionalised graph discipline —
> permits, licensure, stage-gates, mandatory inspection — is predicted by reversal cost and
> feedback latency. Construction and manufacturing evolved formal status floors because
> irreversibility forced them; software's informality is explained by cheap retries, and its
> formalisation pressure rises with consequence and with agent-generated code collapsing generation
> cost while verification cost stands.

**It is wrong if** industries matched on reversal cost and feedback delay differ grossly in how
formal they are. It is also wrong if, after controls, formality follows the accidents of regulatory
history better than it follows those two factors.

## Where this comes from

The quoted statements are the claims exactly as they stand in their claim files, which govern.
The plain-language summaries above each one are explanation only.

| Section | Rests on |
|---|---|
| 1 | `DDD-org-01`, projected |
| 2 | `DDD-org-02`, projected |
| 3 | `DDD-org-03`, projected |
| 4 | `DDD-org-04`, projected |
| A folder, not a repository, until it has its own documents and an external checker | `DDD-dec-05` |
| The claims ratified as projected, the claim file as their exposition | `DDD-dec-40` |

The claims rest in turn on principle-layer claims pinned in `graph/upstream.yaml`. The earlier
text of this page is at `e5a332d`.
