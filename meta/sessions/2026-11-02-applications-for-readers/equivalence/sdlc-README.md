# Equivalence — `applications/sdlc/README.md`

Old text: `e5a332d:applications/sdlc/README.md`. New text: same path.

| # | Old: section and rule, in brief | New: document and section | Note |
|---|---|---|---|
| 1 | The framework denominated in software delivery; the engineering projection; Conservation of Specification Demand is the general principle's name when the actor builds software | Opening; "How the general framework reads in software" | same |
| 2 | "Nothing here is deprecated. The reframing is a promotion" | — | removed: history (the v4 reframing) |
| 3 | Upstream basis block; `ddd:ref` markers `term:floor`, `DDD-frame-01`, `term:seam-identity` | `ddd:doc` block; markers kept beside the mapping table; "Where this comes from" | same |
| 4 | Mapping table, general → software (seven rows) | "How the general framework reads in software" | same; `core/NN` locations moved to the basis table |
| 5 | The design docs predate `core/`; correct as engineering guidance; foundational justification lives in `core/` | "Not settled yet", earlier design documents | same |
| 6 | The four v3 design documents are not in the tree; removed at `219ad6c` under `docs/`; restoring them is an open decision; listed as the record of v3 | "Not settled yet", earlier design documents | same; the per-document descriptions removed as history, recoverable at `e5a332d` |
| 7 | what · "moved 2026-10-28, not yet ratified" | "Where to start" table | corrected: stale status (PR #42 merged) |
| 8 | how · "`[PROPOSED]`, unruled"; with its vocabulary and worked decisions | "Where to start" table; vocabulary now `how-reference.md` | corrected: stale status (PR #41 merged); see the Gate 2 report on how.md's own unsettled points |
| 9 | production-as-ground: pre-production predicates close over substitute ground; DORA's keys instrument the gap; three tiers | "Where to start" table | same, described by the reader's task |
| 10 | Note: the historical documents say "law" and lean on the pre-review framing; restoring them is the restoring session's work; `core/` wins | "Not settled yet", earlier design documents | same |
| 11 | This README and production-as-ground are what the projection carries; product-cli is the reference implementation | "Where to start"; "Tooling" | same, updated to the current file set |
| 12 | Which role gets which decision: a model may own a decision iff its acceptance predicate closes over digital ground; else a person selected for competence on open predicates; autonomy is bounded by closure | "Three things", first | same |
| 13 | The orchestration layer is a seam, priced: cheap to specify, expensive per run, a bottleneck, the poisonable centre; harvesting recurring coordination into encoded rules with checks makes it cheaper over time | "Three things", second | same |
| 14 | Verification of third-party and environment ground is on a schedule, not build-triggered; unreachable source is Unknown, never a pass | "Three things", third | same |
| 15 | product-cli: authoring layer; owns features, ADRs, test criteria, dependencies; builds the derived graph; curated bundles; audits; serves the engineering graph; the harness is designed against `04-implementation.md` | "Tooling" | same |
| 16 | — | "Two worked examples, and why" | added per `DDD-dec-95` |
| 17 | — | "Where to start" rows for `what-reference.md`, `how-reference.md`, `how-examples/` | added: the new file set |
