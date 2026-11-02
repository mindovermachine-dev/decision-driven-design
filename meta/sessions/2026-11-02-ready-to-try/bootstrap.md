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

## Amendment 1 — 2026-11-02: the session moves to Claude Code

Add-only. Nothing above this heading is edited.

At Emil's instruction — "We need to run in in a claude code session we get the correct signature
etc" — the session moved from the claude.ai cloud workspace, where its first four commits were
made, to a Claude Code session. GitHub reported those four commits as unverified
(`unknown_key`): the workspace's signing key is registered to nobody.

The Claude Code session re-signed them with its own key
(`SHA256:xDu5EyJd05ROum1g+8Aj1Up3MjE6RbHnI70/xNHljDY`, identity
`Claude (Emil) <claude+emil@okkels-klein.dk>`) by
`git rebase --exec 'git commit --amend --no-edit -S' origin/main`, then pushed with
`--force-with-lease` against the old head. For each pair, author, author date, message and tree
are unchanged and `git diff <old> <new>` is empty. Only the committer date and the signature
differ. GitHub reports all four new commits `verified: true`, reason `valid`.

| Old | New | Tree | Commit |
|---|---|---|---|
| `d38fbdf4fef6a6ff2ea5897cd3a83cee4980982c` | `7599efb6d735ca69d56dee0290a861c663990ab1` | `79329e5` | G0 charter |
| `8d4557411c3a5c37b00a1a3ffa28950ab10d1bf7` | `8eda2fb4864eb1ad73646a4d8588c99612c61b80` | `52ca273` | G1, round 1 |
| `30dc4eb4c2cbcb561f81d3c48eeee7e95b7e6a90` | `1ecb35064260f7af5e0bd463f799d2c2cbc34854` | `69f0568` | P-1..P-4 |
| `455a13ca8a142aaafb6a0820e8c11739f5f90861` | `fcf75947b9c07b1756ae0c28f278736cb898c3b0` | `0a07a70` | G2 |

The old hashes are cited in earlier messages and replies of this session. They no longer exist
on the branch, so read them through this table. The base is still `1d0f40c`. The `Claude-Session`
trailer of each re-signed commit names the claude.ai workspace session that wrote it. Commits from
this amendment onward name the Claude Code session.

Decision ids, re-checked after the move across every branch of both repositories. Upstream holds
up to `DDD-dec-39`, downstream `main` up to `DDD-dec-62`, and `claude/stoic-einstein-v3y8w9` up
to `DDD-dec-73` (head `5588e9a`, 2026-11-02 08:38 UTC). Only this branch holds `DDD-dec-74` to
`DDD-dec-76`. The range is unchanged.

## Amendment 2 — 2026-11-02: main moved; the id range widens

Add-only. Nothing above this heading is edited.

- **Base.** PR #42 (the What move) merged into `main` at 09:22 UTC, moving it from `1d0f40c` to
  `2b6e4a7`. The branch took `main` by a signed merge (`736324c`), not a rebase, so the hashes in
  amendment 1 still hold. One conflict, `meta/sessions/README.md`, was resolved by keeping both
  rows in date order. Validators after the merge: 31 claims (6 warnings), 61 decisions, 74 pins,
  0 basis-loss, all exiting 0.
- **Decision ids.** Re-checked after the merge on every branch of both repositories. Upstream
  holds up to `DDD-dec-39`, `main` up to `DDD-dec-73`, and nothing holds `DDD-dec-77` or above.
  The session's range widens to `DDD-dec-74` to `DDD-dec-82`. `DDD-dec-77` to `82` file Round 2.
- **Scope.** Round 2 ruled G3, G4 and G6, so the stops at those gates are lifted. The session now
  stops for Emil's review at the end of G3's execution, and again at the end of G5. G6's
  CHANGELOG heading and release descriptor follow G5 and are proposed only. The release is cut on
  Emil's merge, under the release-head guard (upstream `DDD-dec-39`).
- **Environment.** The checkers' Python dependencies were installed in this session's container
  to run every gate: rdflib 7.6.0, PyLD 3.3.0, pyshacl 0.40.2, pyoxigraph 0.5.13, and PyYAML
  6.0.3, which was already present. Python is 3.13 here; CI uses 3.11.

## Amendment 3 — 2026-11-02: the session's issue

Add-only. Nothing above this heading is edited.

On Emil's Round 3 ruling for R-11 ("Open an issue now"), the session opened
[issue #44](https://github.com/mindovermachine-dev/decision-driven-design/issues/44), "Ready to
try: present the method as a preview (session 2026-11-02)". It links PR #43 and this record.
Every commit from this amendment onward carries `Refs #44`. Earlier commits, up to `f20d8b6`
(Round 3), do not, and are not rewritten. Enforcement in `scripts/ci.py` follows later, as
`DDD-dec-81` item 6 and R-11 say.

## Amendment 4 — 2026-11-02: DDD-dec-83 is never used

Add-only. Nothing above this heading is edited.

On Emil's Round 4 ruling for R-14 ("From 85 onward"), **`DDD-dec-83` is recorded as never used**.
This session holds `DDD-dec-74` to `DDD-dec-82` and `DDD-dec-84`. The authority-profile session
(`claude/bold-franklin-i7b16g`) re-checks and starts at `DDD-dec-85`. No decision file exists or
will exist for `DDD-dec-83`. Ids are never reused, and the gap is not a defect.
