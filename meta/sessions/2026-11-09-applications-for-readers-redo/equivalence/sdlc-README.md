# Equivalence — `applications/sdlc/README.md`

Old: `84aa466`. New: this session's working tree.

| # | Old: rule, in brief | New: section | Note |
|---|---|---|---|
| 1 | The agentic/DAG design framework constituted the whole of DDD through v3; in v4 it is the engineering projection; CSD is what CDD is called when the actor builds software | opening | same |
| 2 | "Nothing here is deprecated. The reframing is a promotion: what looked like the framework was always one projection of it." | opening | same, verbatim |
| 3 | Upstream basis; three `ddd:ref` markers | opening | same; markers unchanged |
| 4 | The seven-row mapping table, core/ to software | How the general framework reads in software | same, verbatim |
| 5 | The design docs predate `core/`; they remain correct as engineering guidance; foundational justification now lives in `core/`, more generally and carefully | The four v3 design documents | same |
| 6 | The four v3 documents are not in the tree; removed at `219ad6c` under `docs/`; not re-landed; "restoring them is an open decision that has not been taken"; listed as record, not links | The four v3 design documents; Not settled yet | same; register `open` in words: *(open)* |
| 7 | The four descriptions, including the autonomy-levels note (per-role autonomy is the actor model's pinning resolution, `core/04`; ceiling set by closure, `core/03`) | The four v3 design documents, items 1 to 4 | same |
| 8 | what.md: "moved 2026-10-28, not yet ratified"; description; identity form | The documents here, `what.md` row | fact corrected: ratified by the merge of #42 (each decision names the PR's acceptance as the ratification act). Its one `[OPEN]` point stated as *(open)* |
| 9 | how.md: "`[PROPOSED]`, unruled"; description | `how.md` row | register: `[PROPOSED]` -> ruled, by `DDD-dec-55`–`61` (merged in #41) and `DDD-dec-119` (Round 2). The `[OPEN]` adopter-kinds point and the IRI reading kept unsettled |
| 10 | production-as-ground: description (three clauses) | `production-as-ground.md` row | same; register from its own status line ("reported, partially") added |
| 11 | sdlc.md: ruled by Round 28 (`DDD-dec-115`); description | `sdlc.md` row | same; "with the DORA computations over that record" added from `sdlc.md` and `acts/dora/` |
| 12 | (not listed) authority.md, authority-vocabulary.md, authority/, product-cli/, acts/ | The documents here | added: the directive asks for every document in `sdlc/`. authority.md: ruled, ratified by the merge of #45 |
| 13 | The What is owned in the PDLC and read here as ground (`DDD-dec-114`, Round 8); stays where `DDD-dec-42` placed it; the SDLC never writes it | after the table | same; ids to the table |
| 14 | Note: the v3 documents were written before the v4 register ("law" vs "principle"; pre-review immune framing); if restored, reconciliation is the restoring session's work; `core/` wins | The four v3 design documents, last paragraph | same |
| 15 | "Until then, this README and `production-as-ground.md` are what the SDLC projection carries here" | removed; closing note says why | fact corrected: what.md, how.md, authority.md and sdlc.md have landed, so the sentence is false |
| 16 | The reference implementation is product-cli | Reference implementation | same |
| 17 | `core/03`: a decision can be owned by a model **iff** its acceptance predicate closes over digital ground; otherwise an actor selected for competence on open predicates; autonomy bounded by closure | Where the projection sharpens the design | same; "iff" written "if and only if" (#48 trap: its version said "when") |
| 18 | `core/06` prices the orchestration layer: cheap to specify, expensive per run, a bottleneck, "the poisonable centre"; the compound move; cheaper over time | same section | same; "poisonable" kept (#48 trap F3.2) |
| 19 | Verification of third-party and environment ground: not optional, not build-triggered; truth moves on their clock; on a schedule; unreachable is `Unknown`, never a pass | same section | same |
| 20 | product-cli: owns features, ADRs, test criteria, dependencies; builds the derived graph; curated bundles; audits; serves the engineering graph; harness designed against `04-implementation.md` | Reference implementation | same |
| 21 | The Rust tool is the reference until retirement; frozen at `rust-final`; the rewrite implements the What alone, `what.md` and its §6 wire, records decisions as `dpp/1` records that carry no force; defined in `product-cli/product-definition.md`; code, ADRs, tests in product-cli's repository | Reference implementation | same |
| 22 | (new) the `sdlc:` namespace IRI reading | `how.md` and `authority.md` rows; Not settled yet | added: carried from the two vocabularies, which mark it `UNVERIFIED`; stated as *(Claude's reading, not yet confirmed by Emil)* |
