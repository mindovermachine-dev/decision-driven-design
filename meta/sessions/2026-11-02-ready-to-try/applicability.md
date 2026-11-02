# Applicability — the stewardship standard as it applies here (G3) `[PROPOSED]`

`DDD-dec-76` adopts the Mind Over Machine stewardship standard in full, as it applies to this
repository. This table proposes how each item applies. Nothing here is ruled. Every row is
`UNVERIFIED — Emil review` until G3.

Source: `mindovermachine-dev/.github`, `profile/README.md`, HEAD `2f4982a`, section "Open Source
stewardship". Varve's `GOVERNANCE.md` is the precedent for form.

## Weakest point first

Two items collide with how this repository already works, and neither can be settled by
hygiene.

- **Item 5, non-blocking reviews.** The standard reviews releases, not merges. Here, merging is
  the principal's ratification act, so every merge is a blocking review. Proposal: keep that for
  anything that files, supersedes or ratifies a decision, and state it as a deviation. Treat such
  a merge as this repository's counterpart of a release review. Allow editorial changes (links,
  typos, community files) to reach `main` without a ratification act.
- **Item 4, trunk-based development.** Sessions run on branches for days across gates (the What
  move's branch has been open since 2026-10-28). Proposal: state it as a deviation, scoped to
  canon sessions. A session branch lives only as long as its gates, and anything not behind a
  gate lands on the trunk.

## The fourteen items

| # | Item | Applies? | How, here |
|---|---|---|---|
| 1 | Semantic Versioning | Yes | The method's version (`DDD-dec-75`). The SemVer mapping is G6 |
| 2 | Containerised development | Yes | A devcontainer with Python 3.11, PyYAML, git and `ssh-keygen`. That is everything the checkers and the How examples need |
| 3 | Containerised pipelines, runnable locally | Yes | One entry point, `scripts/ci.py`, that runs every gate in order. The workflow calls it and nothing else, mirroring Varve's `eng/ci.cs` |
| 4 | Trunk-based development | **Deviation, scoped** | See the weakest point |
| 5 | Non-blocking reviews | **Deviation, scoped** | See the weakest point |
| 6 | Full traceability | Yes, adapted | AI sessions are already recorded in `meta/sessions/` (prompt, bootstrap, rulings). Missing: commits tied to issues. Proposal: every session gets an issue, and its commits carry `Refs #N`. Enforce it in `scripts/ci.py` once the first session has done it by hand |
| 7 | Agentic AI ready | Yes | `CLAUDE.md` and `.claude/skills/claim-conversion` exist. Add `AGENTS.md` as the tool-neutral entry, with `CLAUDE.md` pointing to it, as Varve does |
| 8 | Signed commits | Yes, with Varve's stated deviation | A `Signed Commits` ruleset on `main`. Cloud-session commits are exempt through the same bypass, for the same reason (the sandbox key is registered to nobody), and are attested by the push path and the session record |
| 9 | Detroit-style testing | Yes, narrow | It applies to the checkers only. Each validator gets a fixture tree it must accept and one it must refuse, so that "INVALID" is itself tested |
| 10 | Managed test data | Yes | The fixtures above, plus the How examples, which already rebuild with throwaway keys (`DDD-dec-62`) |
| 11 | Highly componentised | Yes, as already done | The principle/projection split (`DDD-dec-04`) is the componentisation. Nothing new |
| 12 | Open project management | Yes | **Upstream board: the method's roadmap**, one card per step (1 to 10), moving as each step's register moves. **Downstream board: work**, with a WIP limit. Proposal: a limit of 2, since one principal rules everything |
| 13 | User voice channel | Yes | Turn on Discussions. Issue templates (this session, G2) include a field-report template for people who try the method |
| 14 | Modern distribution | Yes, adapted | No package to install. Distribution is a GitHub Release per method version, with the step cards attached, plus a rendered site (Layer 3). `product-cli` carries the installable tooling in its own repository |

## Not in the fourteen, but in the standard's page

| Item | Finding at arrival | Proposal |
|---|---|---|
| `Maturity` property | `Exploring` ("unknown state, no promises made, most likely not released") | `Experimental`: "R&D code released for friendly testing (Alpha)". This matches "ready to try" while step 1 is projected. Move to `Incubating` when step 1 is reported |
| `Product` property | `Decision Driven Design` | Keep |
| Principle: "Open Source and CopyLeft" | The licence is CC BY 4.0 for text and Apache-2.0 for code. Neither is copyleft. Varve moved to MPL-2.0 for this reason (its ADR 0031) | **Ruling needed.** Either CC BY-SA 4.0 with MPL-2.0, stated as a decision, or keep the current licence and state it as a deviation. Claude has no recommendation on the licence itself; this is the principal's call |
| Repository description | "LLMs are knowledge forecasting machine…", which does not describe this repository | Replace with one line stating the projection and its preview status |
| Topics, Discussions, rulesets | None, off, none | Declare them in `.github/repo-standard.yaml` with the `repo-standard` tool Varve uses, so that drift is checked weekly |

## Root clean-up — why it is not in G2

`PATCH-REPORT.md`, `RECONCILIATION-REPORT.md`, `migration-report.md` and `migration/` are cited
by path in ruled records (`DDD-dec-07`, `core/decisions/README.md`, and several session records).
`validate-core-order.py` is cited by path in `DDD-dec-10` and the CI workflow. Moving them is
therefore not purely mechanical: it leaves ruled records pointing at paths that no longer exist
at the head.

Proposal: move the three reports and `migration/` to `meta/history/`. Add one decision recording
the move, which states that paths in records resolve at the record's own commit. Move
`validate-core-order.py` to `scripts/` in the same decision, leaving a two-line shim at the root
for one release.
