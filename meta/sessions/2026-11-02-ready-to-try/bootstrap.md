# Bootstrap — ready to try, 2026-11-02

Filled in at arrival and committed with `prompt.md` as the session's first commit.

| Parameter | Value |
|---|---|
| Invocation | Interactive. Emil asked how the repository can present like Varve; Claude proposed three layers and four rulings; Emil ruled three and asked a question on the fourth. `prompt.md` carries the exchange verbatim |
| Principal | Emil (sole ratifier; ratifies by merging the pull request) |
| Upstream repo | github.com/mindovermachine-dev/actor-indexed-determination (read only in this session) |
| Upstream pin | `v5.15.2` (`graph/upstream.yaml`), unchanged by this session |
| Downstream repo | github.com/mindovermachine-dev/decision-driven-design |
| Downstream base | `1d0f40c` — head of `main` at arrival, in sync with `origin/main` |
| Downstream branch | `claude/ready-to-try-2026-11-02` |
| Reference | `Hafeok/varve` at its default branch on 2026-11-02, read for comparison; the organisation's stewardship standard as published in `mindovermachine-dev/.github` (`profile/README.md`, HEAD `2f4982a`) |
| Model | Claude Opus 5.5 |

## Gates

| Gate | What | Who |
|---|---|---|
| G0 | This charter committed before any other change | Claude |
| G1 | Rulings 1, 3 and 4 recorded as decisions, verbatim, when given | Claude, on Emil's ruling |
| G2 | Layer 1 hygiene that needs no further ruling, landed as commits on this branch | Claude; Emil reviews |
| G3 | The standard's applicability table ruled: which items apply, how, and which deviations are stated | **Emil** |
| G4 | The worked example ruled (Emil asked: could Varve work?) | **Emil** |
| G5 | Layer 2: README, `why.md`, `method/` step cards, quick start; built on G3 and G4 | Claude; Emil reviews |
| G6 | Layer 3: the version scheme's mapping ruled, the first release under it proposed as a descriptor | **Emil** |

The session stops at G3, G4 and G6. Nothing past a gate is written before the gate is ruled.

## Scope at arrival

In scope: Layers 1 to 3 as proposed in the charter, under the rulings. Out of scope: any change
to canon content (claims, terms, decisions already filed, the What, the How). A link fix or a
moved file is not a canon change; a rewritten sentence in ruled material is, and is not done.

## Decision ids

Checked across every branch of both repositories at arrival. Upstream holds up to `DDD-dec-39`.
Downstream `main` holds up to `DDD-dec-62`. The open branch `claude/stoic-einstein-v3y8w9` (the
Product Framework What move, last commit 2026-11-02 08:28 UTC) holds `DDD-dec-63`…`DDD-dec-73`.
No branch holds `DDD-dec-74` or above. This session takes `DDD-dec-74` onward. The move session
is still live; the claim is recorded here, in each decision's notes, and in the pull request, the
`DDD-dec-62` precedent.

## Session record

| File | What |
|---|---|
| `prompt.md` | The charter, verbatim |
| `rulings.md` | Every ruling, verbatim, in the round it was given |
| `applicability.md` | G3: the stewardship standard, item by item, as it applies here `[PROPOSED]` |
| `predictions.md` | What each operation is predicted to do, written before it runs |
| `successor-items.md` | What this session leaves open |
