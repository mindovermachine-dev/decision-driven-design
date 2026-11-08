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

## After Rounds 16 to 22 (the continuation, 2026-11-07)

Add-only. The tables above stand as written. **`ontology.ttl` and `shapes.ttl` were not changed
in this session** (prompt-2, item 6). The What schema changes are successor items, each by its own
decision.

| # | Item | Files it would change | Closes it |
|---|---|---|---|
| W-1 | **The observation need as a What element** (Round 17; `pdlc.md` §5). A new element kind, located like a §3.6 demand (product, system, flow, step, Decider, Projector), declaring the data needed and the acceptance or outcome it evidences. It is not a third §3.6 kind | `applications/sdlc/what/ontology.ttl` (the class and its properties, with `dct:source`); `what/shapes.ttl` (location, required fields; severity under `DDD-dec-113` E-2: a new requirement enters as `sh:Warning`); `what.md` §3 (a new subsection); a new example What graph and its vectors (no pinned example edited, as `DDD-dec-113` E-5 did); `what/check.py`'s expected warnings | A decision of its own, then a session |
| W-2 | **The product-assurance declaration as a What element** (Rounds 18, 19; `pdlc.md` §4). Located like a §3.6 demand, inherited downward, stating how sure we must be that users perform the designed act. The levels need ruling first (`pdlc.md` O-7) | The same files as W-1, and the inheritance rule in `shapes.ttl` (a SPARQL constraint over `sdlc:within*`) | A decision of its own, after O-7 |
| W-3 | **The conformance vectors** for both elements: element and graph hashes in a new vectors file for the new example, with the canonical form unchanged (`DDD-dec-63`, `-73`) | `what/vectors-6.json` (or the next free name) | With W-1 and W-2 |
| W-4 | **The How side and the gates that read them.** The contract over `telemetry` facts anchored to an observation need (the H-9 pattern, `DDD-dec-70`). The presence check before ready-for-users (`sdlc.md` §17). The implementation-assurance How decision read by o9 and o11 (`sdlc.md` §5) | `applications/sdlc/how.md` and `how-vocabulary.md` (a worked example), and the judge and gate of N-3 and N-4 above | After W-1, with the reference implementation |
| W-5 | **The authority profile's record kinds** for the classification verdict (oC) and the When owner's acts (o2a, o16, an option's exit). This widens S-4 above | `applications/sdlc/authority.md`, `authority-vocabulary.md` | A successor session |
| W-6 | **The dispatcher's two new refusals**: an issue with no `kind:` label, and an owed or own-ground issue that carries a release for work. This widens N-1 above. The record writer (N-7) writes `lc:demandKind`, `lc:restores` and `lc:failureObservedAt` | N-1's and N-7's files | The next gate |
| W-7 | **Wire the `lc:` checkers into `scripts/ci.py`** (S-3 above, unchanged). The SDLC checker now also computes the four DORA keys over its example | `scripts/ci.py`, `scripts/fixtures/` | A successor session |

## After Round 26 (2026-11-08)

Add-only. The tables above stand as written.

| # | Item | Files it would change | Closes it |
|---|---|---|---|
| W-8 | **Editorial: `what.md` §5.1's "the product owner's What scope".** Round 12 rules that priority is a When decision, never the What owner's, and that a classic product owner fuses a What decision with a When decision. `what.md` §5.1 ends: "The product owner's What scope and the architect's How scope are two grants over two sets of kinds of one product." It uses "product owner" for the holder of the What scope. That does not contradict the PDLC, since §5.1 speaks of the What scope alone. But it carries the role name the PDLC takes apart (findings C-6). Proposed wording: "The What owner's scope and the How owner's scope …", citing `DDD-dec-114`. **Not edited in this session** (Round 26, item 3). It goes with W-1 to W-7, since those edit `what.md` §3 under their own decisions | `applications/sdlc/what.md` §5.1 (one sentence) | With W-1 to W-7, under the decision that edits `what.md` |
