# migration/ — repo split execution bundle

Everything the kickoff prompt requires, landed on the execution branch. Contents:

| File | Role |
|---|---|
| `core-contracts.md` | The core reorder: per-doc ddd:contract blocks, reorder map, "what old 00 loses" ledger |
| `validate-core-order.py` | Ordering + transclusion checker. Reads `core/graph/*.yaml` registries AND per-claim `core/claims/*.yaml` files carrying `canonical_md` (format 2) |
| `graph/terms.yaml` | Seed term registry — extend to every `establishes` entry during step 4 |
| `spec-addendum-claim-format-2.md` | Additive claim-format bump enabling claims as embed sources; all format-1 claims valid unchanged |
| `decisions/DDD-dec-04..06.yaml` | The split decisions, drafted in the live decision format with real basis ids. **Filed into `core/decisions/` 2026-08-03 on Emil's explicit authorisation** ("accept and continue", repo split execution session) |

Gates before execution (both verified by the agent, neither performable by it):
1. DDD-dec-04..06 present in `core/decisions/` — **MET 2026-08-03**
2. Measure note shipped, recorded in CHANGELOG or consolidated-state (per DDD-dec-06) —
   **SUPERSEDED** by DDD-dec-07 (Emil, sequencing revision): the split may execute
   immediately; DDD-dec-06's naming resolution stands

## Resolved judgment calls (⚑ ledger)

All eight ⚑ items accepted by Emil (2026-08-03, repo split execution session). Record
them as resolved in the migration report at execution.

From the package and kickoff:
1. **core/09 register fix** — fix in place: *specification demand* → *determination
   demand* throughout, one parenthetical noting the projection term at first occurrence.
2. **Git history** — fresh init for the principle repo; provenance note in README citing
   this repo and the commit branched from.
3. **Principle repo name** — `actor-indexed-determination`; settled by DDD-dec-06.
4. **`i18n/ordliste-dansk.md`** — moves whole to the principle repo; DDD-relevant subset
   regenerated later only if wanted.

From `core-contracts.md`:
5. **00 minimal actor/arrangement** — as written; admission test + composition phrase
   only, full theory (pinning resolution, selection, training) stays in 04.
6. **`assurance` split across 01/05** — `assurance` (the level) established in 01,
   `assurance-tower` in 05; two term keys, two homes.
7. **Closure-sense fix** — old 00 line 160 "closes the encoded store" rephrased to
   "fills the encoded store" wherever that sentence lands (licensed by the kickoff's
   edit list).
8. **Ensemble theory in 11** — the `capacity` dependency on 10 pins it after 10; it does
   not move to 06.

Corrections vs the v1 package: pin examples now use live ids (`DDD-floor-01`,
`DDD-measure-01`, `term:closure`); decision YAML uses the repo's actual schema
(question/resolution/commitmentLevel/basis/assurance/principal/made/reviewTrigger);
claims embed from `core/claims/` per-claim files, not a parallel registry.
The placement table and pinning semantics (E12/E13/W5) in `repo-split-package.md` §2–3
stand, with ids read as corrected here.
