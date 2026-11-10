# Bootstrap — release v0.7.0, 2026-11-10

Filled in at arrival and committed with `prompt.md` as the session's first commit.

| Parameter | Value |
|---|---|
| Invocation | Interactive. Emil's rulings and his refused `canon release v0.7.0` run are verbatim in `prompt.md` |
| Principal | Emil (sole ratifier; ratifies by landing the branch, then cuts the release) |
| Issue | [#69](https://github.com/mindovermachine-dev/decision-driven-design/issues/69). Every commit of the session carries `Refs #69` |
| Upstream pin | `v5.15.2` (`graph/upstream.yaml`), unchanged by this session |
| Downstream base | `87db443` (`87db443b86712ddc0f678ffc3e2cb3e8ea066e05`), the head of `main` at arrival. **`main` has not moved** from the `87db443` the prompt names |
| Downstream branch | `claude/clever-brown-h3ewei`, from `main` at `87db443` |
| Last release | `v0.6.0`, tag on `1ab1de0` (#59) |
| Model | Claude Opus 5.5 |

## Gates

| Gate | What | Who |
|---|---|---|
| G0 | This charter committed before any other change | Claude |
| G1 | The version confirmed from the rules; commit 1, `releases/v0.7.0.yaml` and its `CHANGELOG.md` section from `canon changelog` (the head Emil ratifies); commit 2, `canon ratify v0.7.0`; `scripts/ci.py` and canon's checks green; pushed, pull request opened, CI green | Claude; **stops for Emil** |
| G2 | Confirm `prerelease: true`; land the branch (`canon land`); then, from `main`, `canon release v0.7.0 --plan` and `canon release v0.7.0` | **Emil** |

## The range at arrival

`git log v0.6.0..main` holds 38 commits. They came from five pull requests, all landed:

| PR | What | Decisions and claims |
|---|---|---|
| #64 | The PDLC and the SDLC as applications | `DDD-dec-114`, `DDD-dec-115` |
| #65 | product-cli's definition brought up to sdlc edition 1 | none new (basis `DDD-dec-113`, `-73`, `-72`) |
| #66 | `sdlc.md` §19: O-8 and O-9, open items only | none new (basis `DDD-dec-115`) |
| #63 | Specification feasibility; grants and roles | `DDD-dec-116`, `DDD-dec-117` |
| #68 | Method step 1b, map the flow of demand | `DDD-dec-118`; `DDD-flow-01` to `-04` |

#67 is an issue (the demand-flow session's), not a pull request.

## Scope

In scope: `releases/v0.7.0.yaml`, the `CHANGELOG.md` section that `canon changelog` generates from
it, this session record, and the session's row in `meta/sessions/README.md`. That row and the
record go in before commit 1. The release-head guard allows only the descriptor after the ratified
head (rule 7).

Out of scope: every claim, decision, step card and specification; landing; `canon release`.
