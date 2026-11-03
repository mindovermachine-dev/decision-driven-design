# Successor items — the canon CLI, 2026-11-02

What this session leaves open at the end of Gate 1. Each row names who or what closes it.

| # | Item | Closes it |
|---|---|---|
| S-1 | **Gate 1 review.** `DDD-dec-100` to `DDD-dec-102` and `tools/canon/DESIGN.md`, with questions Q-1 to Q-7 in DESIGN.md §11 | **Emil** |
| S-2 | **The root shim is due for removal.** `validate-core-order.py` at the root was kept "for one release" (`DDD-dec-80`), and `v0.5.0` is cut (tag at `e5a332d`). Not removed here, because G1 changes no scripts | A later commit, on `DDD-dec-80` |
| S-3 | **`CHANGELOG.md` is stale.** At `e5a332d` it heads v0.5.0 "Ready to try (proposed)" and says "Proposed, not cut", but the tag exists. Found while designing `canon changelog` (DESIGN.md §4.5). Not edited here | Emil's ruling on Q-4, then `canon changelog`, or a hand fix before it |
| S-4 | **R-7 stays open in Python.** `validate-core-order.py .` gives four false E13s (P-4). DESIGN.md §4.7 removes the cause in `canon pins`. The Python checker is not fixed in this session; whether to fix it before retirement is open | Gate 3, or a fix in `scripts/` on its own issue |
| S-5 | **The ratification act under `canon land`** (Q-2) needs a decision and a ruleset change in `.github/repo-standard.yaml` before `land` is used | Emil, at Gate 2 |
| S-6 | **Decision-id headroom.** This session holds `DDD-dec-100` to `DDD-dec-102`. `DDD-dec-94` to `99` are left to the live authority-profile session (`claude/bold-franklin-i7b16g`) (Q-7) | Emil; that session's next id check |
| S-7 | **Gates 2 to 4** as the charter sets them: repository operations with tests; the shapes and `canon check` in parallel; a retiring decision per validator | Later sessions, after Emil's review |

## After Round 1 (2026-11-02)

Add-only. The table above stands as written at the end of Gate 1.

| # | Status or item | Closes it |
|---|---|---|
| S-1 | **Done.** Gate 1 reviewed. Round 1 ruled Q-1, Q-3 to Q-7 (`DDD-dec-103` to `DDD-dec-107`, bootstrap amendment 1). Q-2 needed no ruling | — |
| S-3 | Ruled by `DDD-dec-104`. Fixed by the first run of `canon changelog` at Gate 2 | Gate 2 |
| S-6 | **Done.** Q-7 confirmed the headroom | — |
| S-8 | **Cite the protection decision.** Emil's ruling on `main`'s protection (Varve's set, `pipeline (devcontainer)` required, no bypass, `land/**`, `v*` tags restricted to Emil) is filed by another session. DESIGN.md §4.2 says `DDD-dec-<pending>` until its id is known | This session, once the id is known |
| S-9 | **A cut descriptor was edited.** `releases/v0.5.0.yaml` on `main` had `ratified_head` changed in `023c2c4` and `c7424ad`, after `v0.5.0` was tagged at `e5a332d`, against `spec/release-format.md` rule 6. Restore it to its blob at the tag, or rule an exception. canon's immutability check (DESIGN.md §4.5) waits on this | **Emil** |

## After Gate 2 (2026-11-02)

Add-only.

| # | Status or item | Closes it |
|---|---|---|
| S-3 | **Done.** `CHANGELOG.md` is the projection (P-10) | — |
| S-8 | **Still open.** No branch holds the protection decision at the end of Gate 2 | This session, once its id is known |
| S-9 | **Done on `main`** by `288471f` (the descriptor restored to its state at the tag), and `ci.py` now refuses an edited cut descriptor (`e8fde2a`) | — |
| S-10 | **The changelog renders no cut status**, which departs from one line of `DDD-dec-104`'s resolution ("whether it is cut"). Rendering it makes the projection change when a tag is pushed, so `CHANGELOG.md` would go stale on every release. Rule it: supersede that line, or keep it and accept a follow-up commit after every cut | **Emil** |
| S-11 | **Release order under `DDD-dec-104`.** The ratified head must carry the descriptor and its changelog section, and only the `ratified_head` line may follow. `canon ratify` defaults to `HEAD`. This differs from v0.5.0's process, whose head preceded the descriptor. No rule changes, but the release procedure should say so | Emil to confirm; then the release procedure |
| S-12 | **The Refs start commit** is `6aad807` (`canon.yaml`), Claude's measured choice | Emil |
| S-13 | **P-13** (CI green with the .NET feature) is tested on push, not here | The PR's CI run |
| S-14 | Gates 3 and 4: shapes, `canon check`, `canon pins` (R-7), the parallel run, retirement | Later, after review |

## After Round 2 (2026-11-03)

Add-only.

| # | Status or item | Closes it |
|---|---|---|
| S-10 | **Ruled.** `DDD-dec-104`, amendment in `notes:` (2026-11-03) | — |
| S-11 | **Ruled.** `spec/release-format.md`, port note item 4; `GOVERNANCE.md`, "Releases". Rule 7 is unchanged | — |
| S-12 | **Ruled.** `6aad807` (`canon.yaml`) | — |
| S-8 | **Still open.** No branch holds the protection decision at the 2026-11-03 check | This session or Gate 3, once its id is known |
| S-15 | **Landing PR #47** by fast-forward: Emil's act (`canon land 47`, then `canon land 47 --main`). Gate 3 starts from `main` after it | **Emil** |

## After the landing (2026-11-03)

Add-only.

| # | Status or item | Closes it |
|---|---|---|
| S-9 | **Closed.** `releases/v0.5.0.yaml` was restored on `main` in `288471f`, and is byte-identical at `5ccdf41` to its blob at the tag `e5a332d`. `DDD-dec-104`'s notes gain a dated line saying so | — |
| S-15 | **Done.** Emil landed PR #47 by `canon land 47` and `canon land 47 --main`; `main` is `5ccdf41` | — |
| S-8 | **Still open.** The protection session takes `DDD-dec-108`. Cite it in DESIGN.md §4.2 once it is filed | This session, once `DDD-dec-108` exists |

## At the end of Gate 3 (2026-11-03)

Add-only.

| # | Status or item | Closes it |
|---|---|---|
| S-14 | Gate 3 built: the shapes, `canon check`, the parallel run (47 cases agree; ledger `tools/canon/parallel-run.md`) | Emil's review, then landing |
| S-16 | **Agreement B** (`DDD-dec-103`): a full re-run of `canon check --compare` after the Varve pin moves past `0.1.0-preview.15`. Each retirement then names both versions | After the next Varve release |
| S-17 | **Gate 4**: one decision per validator retiring it from `scripts/ci.py`, after S-16; `ci.py` itself last | Emil |
| S-18 | **The What's shapes** in `canon check` (DESIGN.md §5.5): `applications/sdlc/what/shapes.ttl` through Varve, and the hash vectors through `Varve.Rdf`'s RDFC-1.0, compared with `what/check.py` | A later gate |
| S-19 | **`canon pins`** (DESIGN.md §4.7; R-7) and the `core-order` gate | A later gate |
| S-20 | **Resolving `basedOn`.** Python does not resolve a decision's `basedOn`, so canon does not either (parity). Making it a rule would be a new decision | Emil, if wanted |
| S-8 | **Still open.** `DDD-dec-108` (the protection decision) is not on any branch at the end of Gate 3 | This session, once it exists |
| S-8 | **Closed.** `DDD-dec-108` (the protection decision) is filed on `claude/sharp-davinci-89xeil` (`458d05b`), and DESIGN.md §4.2 cites it, saying it was not yet landed when cited | — |

## Round 4 (2026-11-03)

Add-only.

| # | Status or item | Closes it |
|---|---|---|
| S-20 | **Ruled: yes, as its own decision.** Both validators gain basedOn resolution together, with fixtures; upstream ids resolve through `graph/upstream.yaml`. Implemented after #53 lands, on a new branch from `main`; filed decisions that would fail are reported, not edited | This session, after #53 lands |
| S-8 | `DDD-dec-108` has landed on `main` (`c06b359`, landed with `458d05b`); DESIGN.md §4.2 now says so | — |

## S-20 built (2026-11-03)

Add-only.

| # | Status or item | Closes it |
|---|---|---|
| S-20 | **Built.** `DDD-dec-111`; the rule in `validate-claims.py` and canon's decision shapes; two refuse fixtures; the ledger's own count. Waits on review and landing | Emil |
| S-21 | **The 14 recorded entries** (`graph/unresolved-basis.yaml`): 12 decisions whose `basedOn` names an upstream decision (`DDD-dec-09`, `-15`, `-17`, `-26`, `-37`, `-39`) or an upstream term (`term:presumed-discharge`) that is not pinned. Options: pin the upstream ids in `graph/upstream.yaml` (a pin advance, a decision), after which the entries leave the record; or rule them acceptable as recorded | **Emil** |
| S-22 | **Two readings in `DDD-dec-111`'s notes**: local terms resolve, and the rule is an error with a record rather than a warning | **Emil** |
| S-23 | **Landing order.** `claude/sharp-davinci-89xeil` (agent review, `DDD-dec-109`, `-110`) also changes `tools/canon/`. Whichever lands second merges `main` in first | Whichever session lands second |

## Round 5 (2026-11-03)

Add-only.

| # | Status or item | Closes it |
|---|---|---|
| S-22 | **Ruled: both readings confirmed.** Add-only note in `DDD-dec-111` | — |
| S-21 | **Ruled: pin them at `v5.15.2`.** A decision of its own, after #55 lands, on a new branch from `main` | This session, step 2 |
| S-23 | **Ruled: #55 lands first**; the agent-review branch merges `main` afterwards | Emil's landing order |
