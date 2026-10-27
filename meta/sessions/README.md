# meta/sessions/

Session arrival records. One directory per session, named `YYYY-MM-DD-<slug>/`, holding the
**prompt** and its **bootstrap** as committed *before* the session ran.

**Why this exists.** Five sessions arrived without a durable record of what they were asked to do:
the prompt lived only in the invocation, so a session's own charter could not be cited, diffed, or
checked against what the session actually did. `DDD-dec-17` records those five arrival failures.
Committing the prompt first makes the charter a repo object — quotable at every gate, and auditable
afterwards against the commits the session produced.

**The convention.** Before a session begins work:

1. `meta/sessions/YYYY-MM-DD-<slug>/prompt.md` — the session prompt, verbatim.
2. `meta/sessions/YYYY-MM-DD-<slug>/bootstrap.md` — the invocation message and the session's
   parameters (branch, base commits, gates, principal).

Both land in the session's first commit, on the session's branch, before any canon is touched.

A session's own scope is thereby fixed at arrival rather than reconstructed at close. Where a
session's later work exceeds the committed prompt, the excess is visible as excess.

**Index.**

| Session | Type |
|---|---|
| `2026-08-17-freight/` | Interactive canon curation — the accumulated small-items list (batches A–G) |
| `2026-08-18-wave3/` | Interactive canon curation — the principle-layer filings (batches W/H/Q, map P) |
| `2026-08-18-track-1-determination/` | Projection authoring — the determination learning track, ten rungs, two repositories |
| `2026-08-19-measure-discharge/` | Interactive paper drafting — the measure note's discharge section (items M-1…M-5) |
| `2026-08-20-paper-a/` | Interactive paper drafting — Paper A, the framework's statement paper (P-1…P-5) |
| `2026-08-21-floor-lineage/` | Interactive canon curation — the floor's definition placement and lineage (F-1…F-4) |
| `2026-08-23-phase1a/` | Interactive canon curation — Phase 1a: the discharge partition and `DDD-measure-06` (R-1…R-4) |
| `2026-08-24-ground-audit/` | Interactive audit — Phase 1b: the ground audit (D-1…D-4); changed nothing. Output: `meta/ground-audit-2026-08-24.md` |
| `2026-08-25-item4/` | Interactive canon curation — item 4: status, kind, the validator and the appendix (I-1…I-4) |
| `2026-08-27-ground-migration/` | Interactive canon curation with an execution phase — item 5: the ground migration, on the ground audit's rulings (G1…G6) |
| `2026-08-30-paper-a-revision/` | Interactive paper revision — Paper A answers its external review, advances its pin to `v5.12.0`, and carries W1 (R-1…R-6) |
| `2026-08-31-ground-migration-exec/` | Interactive canon curation with an execution phase — the ground migration executed upstream; the two-W6 firing predicted for the next pin advance (G1…G6) |
| `2026-09-01-primer/` | Interactive drafting — the primer at `projections/primer/`, generated where it can be, pinned always (gates 1–4) |
| `2026-09-02-pre-transfer/` | Interactive canon curation — publication readiness before transfer: the accountability arity, the front pages, the pin advance to `v5.13.0`, the readiness report (I-1…I-4) |
| `2026-09-27-act-address/` | Interactive design with a pre-registered dry run — the act address: candidate D under test, the layer path and causal time index, occurrence uniqueness (R-1…R-8). **Arrival retroactive**: no prompt was committed before the session ran (`arrival-retroactive.md`, the `DDD-dec-17` precedent); the hashed pre-registration bounds the test, not the design work |
| `2026-09-27-act-address-landing/` | Interactive canon curation — lands the act address session in both repositories: `DDD-ground-06`, `term:act-address` and `DDD-dec-37` upstream; `DDD-address-01…05` and `DDD-dec-38` here; the pin advance staged with its firing predicted (gates 0–4) |
| `2026-10-26-housekeeping/` | Housekeeping on Emil's blanket ruling — the Track 1 banners struck in both repositories, the release-head guard (S-1), the `repo:` URL (S-7), upstream PR #3 closed (S-10), the six org/sim review flags ruled, F-3 recorded, and the pin advance to `v5.15.2` staged with its firing predicted |
| `2026-10-27-product-framework-what/` | Rulings recorded — the Product Framework's What moves into this repository as the opinionated specification of a software application; How and Delivery stay out; decisions to be added into the What; a system is ground and tolerance (`DDD-dec-41`); How and Delivery retired, Two Pillars dropped, a decision for each change of the What (`DDD-dec-42`). Nothing moved yet: O-4 open |
