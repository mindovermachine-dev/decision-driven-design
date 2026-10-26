# Bootstrap — housekeeping session, 2026-10-26

Filled in at arrival and committed with `prompt.md` as the session's first commit.

| Parameter | Value |
|---|---|
| Invocation | Interactive. Emil asked for a rundown, the proposed list, and recommendations, then ruled "agreed on all execute it". `prompt.md` carries the exchange verbatim |
| Principal | Emil (sole ratifier; ratifies by merging the two pull requests) |
| Upstream repo | github.com/mindovermachine-dev/actor-indexed-determination |
| Upstream base | `1cb3819` — head of `main` at arrival; tag `v5.15.1` points at it |
| Upstream branch | `claude/release-head-guard` |
| Downstream repo | github.com/mindovermachine-dev/decision-driven-design |
| Downstream base | `baec167` — head of `main` at arrival, in sync with `origin/main` |
| Downstream branch | `claude/housekeeping-2026-10-26` |
| Model | Claude Fable 5.1 |
| Gates | None formal. Emil ruled on the charter as a whole; each item lands as its own commit, and the two pull requests are the ratification acts |

## Scope at arrival

In scope, from the charter: items 1 to 5 and 8 in full; item 6 for the six org and sim flags.
Deferred by the charter's own sequencing: item 7 (T2b, its own session, after the pin advance to
v5.15.2 completes) and item 6's three address flags (they wait on S-3 and S-4, which are canon
authoring, not housekeeping). S-5 (the Danish glossary rulings) is not taken: ruling Danish terms
is Emil's act, and no release in this session needs it.

Decision ids: 39 is the next free id across both repositories (upstream holds up to 37, downstream
38). The upstream guard ruling takes 39; the downstream session decision takes 40.

## Session record

| File | What |
|---|---|
| `prompt.md` | The charter, verbatim |
| `pin-advance-prediction.md` | The firing predicted before the ref moved (`dbabbce`) |
| `successor-items.md` | S-1, S-7, S-10 closed; S-2..S-6, S-8, S-9 carried; H-1..H-3 new |
| `core/decisions/DDD-dec-40.yaml` | The ruling, and the open bump |
| Upstream PR #26 | `DDD-dec-39`, the guard, the banners, `v5.15.2` proposed |
