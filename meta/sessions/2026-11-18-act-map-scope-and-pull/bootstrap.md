# Bootstrap — the act map, scope and pull, 2026-11-18

Filled in at arrival, 2026-11-18 at 08:51 UTC (09:51 Europe/Berlin), and committed with `prompt.md` as the session's first commit.

| Parameter | Value |
|---|---|
| Invocation | A Claude Code session started by Emil. `prompt.md` is the prompt, verbatim |
| Principal | Emil. He rules each proposal at G1 and G2, and merging is his |
| Issue | [#80](https://github.com/mindovermachine-dev/decision-driven-design/issues/80), the charter, read in full at arrival. It had no comments. Every commit of this session carries `Refs #80` on its own line |
| Downstream base | `84aa466`, head of `main` at arrival |
| Downstream branch | `claude/act-map-scope-and-pull-2026-11-18`, from `main` at `84aa466` |
| Archive branch | `claude/pull-and-scope-2026-11-18`, head `47cf4cc`, as the prompt says. A source to copy from. Not merged, not rebased, not pushed to, not deleted |
| Old branch | `claude/act-map-and-process-2026-11-17`, head `66bc21f`, still on the remote. Every commit on it is contained in the archive branch (checked with `git merge-base --is-ancestor`). Its deletion is Emil's (2026-11-18 R-7), not this session's |
| Upstream repo | github.com/mindovermachine-dev/actor-indexed-determination, read only |
| Upstream pin | `v5.15.2` in `graph/upstream.yaml`, tag at `084bce7`. Upstream `main` is also at `084bce7`. Unchanged by this session |
| Upstream fetched | Cloned at arrival with every branch and tag. Canon is read at `v5.15.2` only |

## Gates

| Gate | What | Who |
|---|---|---|
| G0 | `prompt.md` and this file committed before any other change | Claude |
| D-1 | The two session directories copied from `47cf4cc` as they stand, in one commit naming the source commit | Claude |
| G1 | Deliverables 2 to 5: the pull statement and the five-step procedure with one worked example tested against a junior engineer's first contact; the proposed claims; what each of steps 2 to 10 adds to the act map; the effect on T2b's pre-registration, on step 1b's kinds and on `DDD-address-02`'s region. **Stop for Emil**, who rules each proposal and where it is filed | Claude; Emil rules |
| G2 | Deliverable 6, on the G1 rulings only: claims filed, cards changed by supersession. The whole `validate` workflow run locally before every push, and the workflow run on each pushed commit reported. A pull request against `main`, naming the head to ratify. **Stop for Emil** | Claude; Emil rules |
| Merge | Landing the branch | Emil |

## Decision and claim ids

Checked at arrival across every branch of both repositories: 63 remote branches downstream and 28 upstream, with every upstream tag.

| Id | Where it appears |
|---|---|
| `DDD-dec-122` | Files on the archive branch and the old branch only. Nowhere on `main` |
| `DDD-dec-121` | `claude/confident-goldberg-c0y0ia` |
| `DDD-dec-119`, `-120` | `claude/zealous-ptolemy-3txf8k` |
| Highest on `main` | `DDD-dec-118` |
| Highest upstream | `DDD-dec-39`, on any branch or tag |
| `DDD-address-06` to `-08` | Files on the archive branch and the old branch only |
| `DDD-address-09` onwards | No file on any branch of either repository. The only mention is the text of 2026-11-18 R-8 on the archive branch |
| `DDD-address-*` upstream | None |

So `DDD-dec-122` and `DDD-address-06` to `-08` are this issue's by 2026-11-18 R-8, and new claims start at `DDD-address-09`. A new decision, if one is ruled, would take `DDD-dec-123`. The check is run again before filing.

## Deviations

| # | Deviation | Why |
|---|---|---|
| V-1 | The session environment named a different development branch. The branch is the one the prompt names | The prompt is Emil's explicit instruction |
| V-2 | The model is not recorded here, unlike earlier bootstraps | The session's operating rules keep model identifiers out of files pushed to the repository |
| V-3 | `predictions.md` is not in this first commit | The prompt says to commit `prompt.md` and this file first. Predictions are written before each later operation |

## Known before work starts

- The `Agent review` check fails on `main` on a build error in `tools/canon` (`NU1004`: the lock file expects `Microsoft.NET.ILLink.Tasks` 10.0.14 and the runner resolves 10.0.15). This branch does not cause it and does not fix it. It is reported at each push.
- The local toolchain has `dotnet` 10.0.404 and `python3`, so the whole `validate` workflow can be run locally.
