# Successor items — the SDLC and PDLC applications, 2026-11-07

What this session leaves open. Each row names who or what closes it. The workflows, actions and
the dispatcher are **not written** (prompt, item 7). They are the next gate, after Emil rules the
specs.

## The next gate: the reference implementation, under `applications/sdlc/`

Each row adds files under `applications/sdlc/` only. They are reference files a product
repository copies or calls, and they are never run against this repository's trunk.

| # | Item | Act | Files it would add |
|---|---|---|---|
| N-1 | **The dispatcher.** On `issues: labeled` it checks the sender against the map's How-scope holders and the issue's single `locus:` label, writes the bootstrap header, and starts Claude Code Action in automation mode with the issue body as prompt and `include_comments_by_actor` set to the map's humans. A per-issue concurrency group stops the session when the label is removed | o2b, o3 | `workflows/dispatch.yml`, `dispatcher/header.py` (the bootstrap), `dispatcher/README.md` |
| N-2 | **The session-branch check** (trunk-worthy) on pushes to issue-number branches | o7 | `workflows/on_session.yml` |
| N-3 | **The candidate gate.** The product's required checks on push to `ready/**`, once per SHA, plus the toggle-default check | o9 | `workflows/on_ready.yml`, `checks/toggles-default-off.py` |
| N-4 | **The judge.** Main's script on main's map, triggered by `issue_comment` and `workflow_run`, posting `agent review` as the gates App. It reads approve <sha> from the issue, applies D-1 to D-7, and reads the assurance level | o11 | `workflows/agent-review.yml`, `judge/agent-review.py` (or a port of `canon agent-review`), `judge/tamper/` (Varve's tamper cases, re-stated for issues and scopes) |
| N-5 | **The landing.** The gates App fast-forwards main to the SHA green on o9 and o11, and deletes `ready/<N>` | o12 | `workflows/land.yml` |
| N-6 | **Deploy dark.** Main to production on every push to main | o13 | `workflows/on_main.yml` (a placeholder deploy, as takt's is) |
| N-7 | **The record writer.** Appends one Turtle file per occurrence to `sdlc/record` with the gates App's token, validated against `acts/shapes.ttl` before it is written | all | `actions/record/action.yml`, `actions/record/write.py` |
| N-8 | **The product repository's templates.** The identity map with scopes; the rulesets (trunk; `ready/**` forward-only; `sdlc/record` append-only, the App only); the issue template (locus, acceptance criteria in criterion form, assurance level); the toggle registry's schema | — | `templates/identities.json`, `templates/repo-standard.yaml`, `templates/ISSUE_TEMPLATE/issue.md`, `templates/toggles.schema.json` |
| N-9 | **The toggle-on act (o16)** is the PDLC's: a store outside the trunk, refusing without a ready-for-users verdict. It needs `sdlc.md` O-4 ruled first | o16 | `applications/pdlc/` (not `sdlc/`), after O-4 |

## Other items

| # | Item | Closes it |
|---|---|---|
| S-1 | **Rule the specs.** `applications/pdlc/pdlc.md` and `applications/sdlc/sdlc.md` are `[PROPOSED]`. Their open items are `pdlc.md` §13 O-1 to O-6 and `sdlc.md` §16 O-1 to O-7. The ones that are Emil's: F-2 (o2a before o1), the scope-cut act, the forecast band, D-9 (ADR 0239's delegate), the assurance levels, the toggle store, and when the issue closes | **Emil** |
| S-2 | **Land the branch** (`landing.md`) | **Emil** |
| S-3 | **Wire the two `lc:` checkers into `scripts/ci.py`.** `applications/pdlc/graph/check.py` and `applications/sdlc/acts/check.py` run green here, but no gate runs them. `scripts/` was out of this session's scope | A successor session, once the specs are ruled |
| S-4 | **Record kinds for the When owner's acts** (o2a, o16, an option's exit) in the authority profile (`pdlc.md` O-6) | A successor session |
| S-5 | **Read takt's mechanism.** The squash, the landing and the issue closing live in `devx-cafe/takt-actions` and `devx-cafe/gh-tt`. They are not vendored in `how-we-work` and were not read. Nothing in the SDLC depends on them, since it drops the squash and replaces the landing. But `sdlc.md` §6's account of what takt does is only as good as the wiring that was read (findings F-7) | A successor session, if Emil wants takt's mechanism on record |
