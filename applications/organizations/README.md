# Organisation design — four predictions to test

<!-- ddd:doc
reader: people who design or run organisations, deciding whether the framework predicts anything about how theirs works
act: read the four organisation-design claims and the observation that would refute each, so they can test them
pin: v5.15.2
basis: [DDD-org-01@projected, DDD-org-02@projected, DDD-org-03@projected, DDD-org-04@projected, DDD-dec-05, DDD-dec-40]
status: current
supersedes: 84aa466:applications/organizations/README.md
-->

Use this if you design or run an organisation and want to know what Decision-Driven Design
predicts about it. Organisation design is a **directory**, not a repository: four claims, and no
documents of its own yet. Promotion to a repository requires core-like documents and an identified
external checker, and not before.

**How settled this is.** All four claims are **projected**: predictions that have not been
tested, not findings. They were ratified as projected, and each was written in a session
(session-authored). They rest on principle-layer claims pinned upstream. Nothing here is canon.

Below are the claims exactly as they stand in their claim files: each statement and its
falsifier, word for word, with no new prose.

## 1. Graph discipline predicts organisational outcomes

*Projected.*

> Graph discipline — status floors at the consumer boundary, manifests, correction flow to a single canon — predicts organisational outcomes: pivot cost, trust damage from shipping projected claims as established, decision-review latency after thesis change.

**It is wrong if:**

> Organisations measurably differing in graph discipline show no difference in pivot cost or correction latency after size and sector controls.

## 2. The Stable Dependency Principle, with status

*Projected.*

> The Stable Dependency Principle, statused: decisions whose reversal cost exceeds what their basis claims' hazard can absorb (high commitment level on low-status claims) concentrate pivot cost and produce incident-discovered cascades; organisations cannot see these violations because their assumption layer carries no status field.

**It is wrong if:**

> Decisions flagged by fragility (hazard × afferent decisions × reversal cost) generate no more rework or incident findings than unflagged decisions of equal size.

## 3. Priority as a governed decision

*Projected.*

> Priority as a governed decision: backlogs ordered by decisions basedOn statused value-claims — with claim priority set by value of information and decision priority by cost of delay, reversal cost, and basis readiness — churn less and predict delivered value better than intuition-ordered backlogs; roadmap churn is the cascade from silently demoted value-claims.

**It is wrong if:**

> Teams with statused value-claims and explicit basedOn priority show no less roadmap churn or no better value prediction than matched intuition-ordered teams; or churn events do not trace to value-claim status changes on audit.

## 4. Institutional discipline across industries, retrodicted

*Projected.*

> Cross-domain retrodiction: the intensity of an industry's institutionalised graph discipline — permits, licensure, stage-gates, mandatory inspection — is predicted by reversal cost and feedback latency. Construction and manufacturing evolved formal status floors because irreversibility forced them; software's informality is explained by cheap retries, and its formalisation pressure rises with consequence and with agent-generated code collapsing generation cost while verification cost stands.

**It is wrong if:**

> Industries matched on reversal cost and feedback latency showing grossly different discipline intensity, or discipline intensity tracking regulation-historical accident better than the two parameters after controls.

## Where this comes from

| Section | Rests on |
|---|---|
| A directory, not a repository; the promotion criterion | `DDD-dec-05` |
| How settled this is | `DDD-dec-40` (2026-10-26): each claim ratified as projected, its claim file its exposition. Each claim file's notes say "Session-authored" |
| 1 | `core/claims/DDD-org-01.yaml` |
| 2 | `core/claims/DDD-org-02.yaml` (credit: Martin's Stable Dependency Principle) |
| 3 | `core/claims/DDD-org-03.yaml` (credits: Reinertsen; Bezos's Type 1/Type 2 doors) |
| 4 | `core/claims/DDD-org-04.yaml` |
| Rests on principle-layer claims | `graph/upstream.yaml` |

The earlier text of this page said the claims were "flagged `UNVERIFIED — Emil review` in their
claim files". They are not: `DDD-dec-40` ratified all four as projected on 2026-10-26, and the
claim files carry no such flag. The earlier text is at
`84aa466:applications/organizations/README.md`.
