# Successor items — ready to try, 2026-11-02

Open at the end of G2. Each waits on the gate named.

| Id | Item | Waits on |
|---|---|---|
| R-1 | The applicability table (`applicability.md`), including the licence question and the two scoped deviations | G3 |
| R-2 | `GOVERNANCE.md`, `AGENTS.md`, `.github/repo-standard.yaml`, the devcontainer, `scripts/ci.py`, the boards | G3 |
| R-3 | The root clean-up and the move of `validate-core-order.py`, as one decision | G3 |
| R-4 | The worked example. Emil asked "could Varve work?" Claude's answer is in the reply that delivered G2 | G4 |
| R-5 | The practitioner README, `why.md`, `method/` step cards, and the quick start | G3, G4 |
| R-6 | The SemVer mapping, the first version, and the fate of the 4.x CHANGELOG headings | G6 |
| R-7 | The `validate-core-order.py .` defect named in the README. Not reproduced or filed in this session | R-3 |
| R-8 | Project instructions are stale on two points: `main` is at `1d0f40c`, not `4004b49`, and `DDD-dec-62` replaced `decprov/1` with `dpp/1`. The pin, v5.15.2, still holds | Emil (project instructions live outside the repository) |

## Update — 2026-11-02, end of G3 execution (add-only)

The table above is left as written. Status as of this update:

| Id | Status |
|---|---|
| R-1 | Ruled in Round 2; filed as `DDD-dec-78`, `DDD-dec-79`, `DDD-dec-81` |
| R-2 | Written: `GOVERNANCE.md`, `AGENTS.md`, `.github/repo-standard.yaml`, `.devcontainer/`, `scripts/ci.py`, fixtures. The boards wait on Emil (A-4) |
| R-3 | Done: `DDD-dec-80`, root move landed |
| R-4 | Ruled: `DDD-dec-77` |
| R-5 | Next, G5, after Emil's review of G3 |
| R-6 | Ruled: `DDD-dec-82`. The CHANGELOG heading and the v0.5.0 descriptor follow G5 |
| R-7 | Reproduced after the move, through both the shim and `scripts/validate-core-order.py .`: exit 1, 4 E13 errors on `core/14-maturation.md` and `core/16-calibration-ledger.md`. Cause, from reading the code: in upstream-only mode (`.` has no numbered docs), `check_upstream` gets no `local_ids`, so this repository's own `term:maturity` and `term:calibration-ledger` embeds read as unpinned upstream ids. Not fixed and not filed; the fix belongs with an issue |
| R-8 | Partly moot: `CLAUDE.md` now imports `AGENTS.md`. The project instructions outside the repository are still Emil's |

New items:

| Id | Item | Waits on |
|---|---|---|
| R-9 | GitHub reports the licence as `NOASSERTION` while `LICENSE.md` sits beside `LICENSE` (P-8). Renaming it to `LICENSING.md` or moving it to `docs/licensing.md` makes detection report MPL-2.0 (tested with licensee 10.1.0) | Emil |
| R-10 | The release-head guard (`DDD-dec-39`) is implemented upstream (`scripts/check-release-head.py`, `spec/release-format.md`) and not in this repository. The v0.5.0 descriptor (G6) needs either a port or a stated manual check | G6 proposal |
| R-11 | Item 6: commits carrying `Refs #N`, enforced in `scripts/ci.py` once the first session has done it by hand. This session has no issue | Emil: open one, or rule that the PR serves |
| R-12 | The root shim `validate-core-order.py` is removed in the first release after v0.5.0 (`DDD-dec-80`) | v0.5.x |

### Emil's admin acts — listed, not attempted

| Id | Act | Where |
|---|---|---|
| A-1 | Set the organisation's `Maturity` property for this repository from `Exploring` to `Experimental` | Organisation settings → custom properties |
| A-2 | Turn on Discussions | Repository settings → Features |
| A-3 | Apply `.github/repo-standard.yaml`: the description, topics, Discussions and the `Signed Commits` ruleset. Review the description and topics first; they are flagged `UNVERIFIED` | `repo-standard` apply, as Varve does |
| A-4 | Create the two boards: Roadmap (one card per method step, 1 to 10) and Work (WIP limit 2 in *In progress*) | Projects |

## Update — 2026-11-02, end of G5 and G6 (add-only)

| Id | Status |
|---|---|
| R-5 | Done: README, `why.md`, `method/`, quick start (G5) |
| R-6 | Done as proposed: the CHANGELOG heading and `releases/v0.5.0.yaml`, unratified (G6) |
| R-7 | Still open: `validate-core-order.py .` misreads local ids. Not fixed, not filed |
| R-9 | Done: `LICENSING.md`; GitHub reports MPL-2.0 at the branch ref |
| R-10 | Done: `DDD-dec-84`; the guard is ported and is a `ci.py` gate |
| R-11 | Issue #44 opened; commits carry `Refs #44` from `c57c4de`. Enforcement in `ci.py` follows later |
| R-12 | Open: the root shim goes in the first release after v0.5.0 |

New items:

| Id | Item | Waits on |
|---|---|---|
| R-13 | **Ratify v0.5.0.** Fill `ratified_head` in `releases/v0.5.0.yaml` with the head Emil ratifies, normally the commit before the descriptor. Until then the `releases` gate is red by design. A ruled change after that point means a new descriptor commit naming the new head (spec §4 rule 7) | Emil |
| R-14 | **Decision-id overlap.** The authority-profile session (`claude/bold-franklin-i7b16g`, plan at `50b463b`) names `DDD-dec-77` to `83` provisionally, read before this branch filed 77 to 82. This branch skipped 83 and took 84. That session's recheck will see 77 to 82 and 84 taken | Emil; that session's recheck |
| R-15 | **Port the release workflow.** Tag and GitHub Release from the descriptor on merge, as upstream's `release.yml`. Until then Emil cuts `v0.5.0` by hand at the merged head, after `main`'s CI has run the guard there (`DDD-dec-84`) | A later session |
| R-16 | **The junior-engineer test** of the quick start: the example's falsifier | Emil |
| R-17 | Step 1's card leaves "Cost and relocation" and the principal's role unfiled, and its exit check is a flagged reading of `DDD-ground-06`. Filling them is a ruling | Emil |

Emil's admin acts, still open and not attempted: A-1 Maturity → Experimental, A-2 Discussions on,
A-3 apply `.github/repo-standard.yaml`, A-4 the two boards.
