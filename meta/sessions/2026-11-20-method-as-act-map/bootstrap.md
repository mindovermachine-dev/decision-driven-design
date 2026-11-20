# Bootstrap — the method as making an act map, 2026-11-20

Filled in at arrival, 2026-11-20 at 10:21 UTC, and committed with `prompt.md` as the session's first commit.

| Parameter | Value |
|---|---|
| Invocation | A Claude Code session started by Emil. His message is below, verbatim. `prompt.md` is the body of issue #88, verbatim, as his message asks |
| Principal | Emil. He rules each reading and each proposal at G1, and at G2. Merging is his |
| Issue | [#88](https://github.com/mindovermachine-dev/decision-driven-design/issues/88), read in full at arrival. It had no comments. Every commit of this session carries `Refs #88` |
| Downstream base | `main` at `1ecf914` (the merge of #73), exactly the commit the message names, not later. `origin/main` was fetched at arrival and read `1ecf914` |
| Downstream branch | `claude/upbeat-gauss-5yb7sh`, new, from `main` at `1ecf914` |
| Upstream repo | github.com/mindovermachine-dev/actor-indexed-determination, read only |
| Upstream pin | `v5.15.2` in `graph/upstream.yaml`, tag at `084bce7`. Upstream `main` is also at `084bce7`. Unchanged by this session |
| Upstream fetched | Cloned at arrival with every branch (27) and tag (18). Canon is read at `v5.15.2` only |
| Toolchain | `dotnet` SDK 10.0.404 (the exact version `tools/canon` needs) and `python3` are installed, so the whole `validate` workflow can be run locally |
| Held | #74 (the method plugin, head `d80a102` on `claude/confident-goldberg-c0y0ia`) holds `DDD-dec-121`. Its files are not touched |
| Waiting on G1 | #81 (the What and product-cli) and #82 (the states and gaps). The G1 report says what each needs from the rulings |

## Scope of this session

Deliverables 1 and 2 only. Then stop at G1 and report. Deliverables 3 and 4 wait for the G1 rulings and a later instruction.

## Gates

| Gate | What | Who |
|---|---|---|
| G0 | `prompt.md` and this file committed before any other change | Claude |
| G1 | Deliverable 1, the survey, and deliverable 2, the proposals. The readings the issue marks `UNVERIFIED` are put first, as questions answerable in a line each. Each proposal names its weakest point first, with a falsifier and what it breaks. Draft issues, if any, are in the report, not opened. **Stop for Emil** | Claude; Emil rules |
| G2 | Deliverables 3 and 4, on the G1 rulings | Not this session's until instructed |
| Merge | Landing the branch | Emil |

## Decision and claim ids

Checked at arrival across every branch of both repositories: 67 remote branches downstream, and 27 branches and 18 tags upstream. By file and by any mention in any file.

| Id | Where it appears |
|---|---|
| Highest decision file on `main` | `DDD-dec-123` (the one-landing waiver of the `agent review` check) |
| `DDD-dec-121` | A file on `claude/confident-goldberg-c0y0ia` only (#74). Held; not this session's |
| `DDD-dec-124` | No file on any branch. One mention, on `main` and five other branches: `meta/sessions/2026-11-18-canon-lock-file/findings.md:313`, as the alternative id in question W-1, which was not taken (`DDD-dec-123` was filed) |
| `DDD-dec-125` onwards | No file and no mention on any branch of either repository |
| Highest upstream | `DDD-dec-39`, on any branch or tag |
| `DDD-address-01` to `-11` | Files on `main`. No `DDD-address-12` or higher anywhere |
| `DDD-address-*` upstream | None |

So a new decision would take `DDD-dec-124`, with its one stray mention named at G1, or `DDD-dec-125` if Emil prefers an id with no mention. The check is run again before filing.

## Deviations

| # | Deviation | Why |
|---|---|---|
| V-1 | `prompt.md` is the issue body, not the session message | Emil's message says so. The message is kept below so the session's own instructions are on record |
| V-2 | The model is not recorded here | The session's operating rules keep model identifiers out of files pushed to the repository |
| V-3 | `predictions.md` is not in this first commit | The message says to commit `prompt.md` and this file first. Predictions are written before each later operation |

## The session message, verbatim

> Work issue #88 in mindovermachine-dev/decision-driven-design. Read AGENTS.md and
> meta/way-of-working.md first. main is at 1ecf914 or later; say which in bootstrap.md.
>
> Before anything else, commit prompt.md (the issue body, verbatim) and bootstrap.md under
> meta/sessions/2026-11-20-method-as-act-map/, on a new branch from main. Write predictions
> before each operation and score them after.
>
> Work deliverables 1 and 2 only, then stop at G1 and report. At G1 I rule each reading the
> issue marks UNVERIFIED and each proposal. Put the readings to me first, as questions I can
> answer in a line each. Name the weakest point of each proposal first, and give each a
> falsifier and what it breaks.
>
> What has changed since the issue was written on 2026-11-19:
> - #73 landed. applications/ is rewritten for readers, and DDD-dec-94, -95, -119 and -120 are
>   on main. Include the rewritten applications/ documents in the survey.
> - #81 (the What and product-cli) and #82 (the states and gaps) now wait on this issue's G1.
>   Say at G1 what each of them needs from my rulings.
> - #74 (the method plugin) is held until the release that follows this issue. It holds
>   DDD-dec-121. Do not touch its files.
>
> Rules that have bitten earlier sessions:
> - Fetch the live repository and canon at the pin before you cite any id. Never cite from
>   memory.
> - The issue's "Read as" and "Not ruled" lists are Claude's, not mine. Do not build on them
>   as rulings.
> - Change ruled material by supersession, never by rewriting. T2b's pre-registration is fixed.
> - Record my rulings verbatim when I give them, not at close.
> - Every commit carries Refs #88. A commit that changes core/ carries a Basis line.
> - The gate is the whole validate workflow, not scripts/ci.py alone: ci.py, then in tools/canon
>   the tests, changelog --check, issue-refs --basis and check --compare. canon needs .NET SDK
>   10.0.404 exactly. Report the workflow run on your pushed head, and both required checks by
>   their check names: pipeline (devcontainer) and agent review.
> - agent review reads "Not approved" until I comment by hand. That is expected. Report
>   anything else it says.
> - Check that any decision or claim id you propose is free on every branch of both
>   repositories. The highest decision on main is DDD-dec-123.
> - Do not open issues. Draft them in your gate report.
> - Write the credited GitHub user as pjarnhus, with no @.
