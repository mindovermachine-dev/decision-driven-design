# Bootstrap — the act map and a process, 2026-11-17

| Parameter | Value |
|---|---|
| Invocation | Interactive. Emil gave the issue text as one message in the claude.ai project conversation. `prompt.md` carries it verbatim |
| Principal | Emil (sole ratifier; ratifies by landing the branch) |
| Issue | None found on GitHub at arrival. The newest issue is #77, and none carries this title. The issue text exists only in the conversation and in `prompt.md`. Commits carry no `Refs` line until Emil names a number |
| Upstream repo | github.com/mindovermachine-dev/actor-indexed-determination, read only, at tag `v5.15.2` (`084bce7`) |
| Upstream pin | `v5.15.2` (`graph/upstream.yaml`, line 133), unchanged by this session |
| Downstream repo | github.com/mindovermachine-dev/decision-driven-design |
| Downstream base | `84aa466`, head of `main` at arrival |
| Downstream branch | `claude/act-map-and-process-2026-11-17` |
| Parallel work | PR #73 (`claude/zealous-ptolemy-3txf8k`, `applications/` for readers, `DDD-dec-94`, `-95`, `-119`) and PR #74 (`claude/confident-goldberg-c0y0ia`, the method plugin, `DDD-dec-121`). Both are open and unlanded. #73 rewrites prose under `applications/`, where this session's survey reads line numbers |
| Model | Claude Fable 5.2 |

## Gates

| Gate | What | Who |
|---|---|---|
| G0 | This charter committed before any other change | Claude |
| G1 | Deliverables 1 and 2: `survey.md` and `proposals.md`. Nothing is filed | Claude; **stops for Emil**, who rules each definition and where it is filed |
| G2 | Deliverable 3: the definitions filed as ruled; `python3 scripts/ci.py` passes; pushed | Claude; **stops for Emil** |
| Merge | Land the branch | **Emil** |

## Scope at arrival

In scope: the survey, the proposals, and after G1 the filings Emil rules.

Out of scope, from the issue: changing any act; new processes such as budget or employment; Mantle; canon in the principle repository.

## Decision ids

Checked across every branch of both repositories at arrival (2026-11-17, 15:40 UTC).

- **Upstream** (27 remote branches): the highest decision id is `DDD-dec-39`.
- **Downstream** (every `origin/*` branch): the highest decision file on `main` is `DDD-dec-118`. `DDD-dec-119` is on PR #73's branch. `DDD-dec-120` and `DDD-dec-121` are on PR #74's branch. No branch mentions an id above `DDD-dec-121`.

The next free decision id is **`DDD-dec-122`**. Nothing is filed before G1.

The highest claim id in the address area is `DDD-address-05`.

## Deviations at arrival

- **Reading before the charter.** The ground files were read, and the search for "act map" was run, before this charter was committed. Nothing was written. Recorded here because the convention puts the charter first.
- **Project instructions are stale on the head.** They name `main` at `4004b49`. `main` is at `84aa466`. The upstream pin they name, `v5.15.2`, is still the pin.

## Read at arrival

- `AGENTS.md`; `meta/way-of-working.md`; `meta/sessions/README.md`.
- `method/01-map-and-index-acts.md`; `method/quick-start.md` §3 and §4; `method/01b-map-the-flow-of-demand.md` (the lines that name the act map or a process).
- `core/claims/DDD-address-01.yaml`, `-02`, `-04`; `core/decisions/DDD-dec-114.yaml`, `-118`.
- `applications/pdlc/pdlc.md` §11 and §13; `applications/sdlc/sdlc.md` §3 and §10; `applications/pdlc/graph/ontology.ttl`, `shapes.ttl`, `acts.ttl`; `applications/sdlc/acts/acts.ttl`.
- `meta/sessions/2026-09-27-act-address/` (`rulings.md`, `prereg-act-coordinates.md`, `results-act-address-dry-run.md`).
- Upstream at `v5.15.2`: `core/claims/DDD-ground-06.yaml`; `term:act` and `term:act-address` in `core/graph/terms.yaml`; `core/14-indexed-determination.md` §5.
