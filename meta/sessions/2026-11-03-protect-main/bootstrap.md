# Bootstrap — protect main, 2026-11-03

Filled in at arrival and committed with `prompt.md` as the session's first commit.

| Parameter | Value |
|---|---|
| Invocation | Interactive. Emil's ruling was given through the claude.ai question dialog on 2026-11-02 and handed to this Claude Code session as its prompt. `prompt.md` carries it verbatim |
| Principal | Emil (sole ratifier; ratifies by landing the branch) |
| Issue | [#51](https://github.com/mindovermachine-dev/decision-driven-design/issues/51). Every commit of the session carries `Refs #51` |
| Upstream repo | github.com/mindovermachine-dev/actor-indexed-determination (read only in this session) |
| Upstream pin | `v5.15.2` (`graph/upstream.yaml`), unchanged by this session |
| Downstream repo | github.com/mindovermachine-dev/decision-driven-design |
| Downstream base | `5ccdf41` — head of `main` at arrival |
| Downstream branch | `claude/sharp-davinci-89xeil` (assigned by the harness) |
| Parallel session | The canon CLI's Gate 3 (`2026-11-02-canon-cli/`), taking `DDD-dec-109` onward |
| Reference | `Hafeok/varve`, `.github/repo-standard.yaml` and `GOVERNANCE.md`, read from a shallow clone of its default branch at arrival |
| Signing | `Claude (Emil) <claude+emil@okkels-klein.dk>`, key `SHA256:xDu5EyJd05ROum1g+8Aj1Up3MjE6RbHnI70/xNHljDY` |
| Model | Claude Opus 5.5 |

## Gates

| Gate | What | Who |
|---|---|---|
| G0 | This charter committed before any other change | Claude |
| G1 | `DDD-dec-108` filed; the three rulesets declared; `GOVERNANCE.md` and the two README rows; predictions before each run; CI green on the pushed head | Claude; **stops for Emil** |
| G2 | Land the branch (`canon land`), then apply `.github/repo-standard.yaml` | **Emil** |

## Scope at arrival

In scope: `DDD-dec-108`, `.github/repo-standard.yaml`, `GOVERNANCE.md`, the two README rows named
in the prompt, this session record, and the session's row in `meta/sessions/README.md`. Out of
scope: applying any setting, the Signed Commits bypass list (reported, changed only on a ruling),
`tools/canon/` (including `DESIGN.md` §4.2's pending citation, which is the canon CLI session's
S-8), `scripts/`, CI, and every claim.

## Decision ids

Checked across every branch of both repositories at arrival (2026-11-03, 08:15 UTC).

- **Upstream** (`actor-indexed-determination`, 27 branches): the highest id on any branch is
  `DDD-dec-39`. No file on any branch mentions `DDD-dec-100` to `DDD-dec-109`.
- **Downstream** (48 remote branches): the highest decision file on any branch is
  `DDD-dec-107`. No file on any branch mentions `DDD-dec-108` to `DDD-dec-119`.

This session takes **`DDD-dec-108`** and only that id, as the prompt assigns.

## Read at arrival

- `main`'s head `5ccdf41`: four check runs named `pipeline (devcontainer)`, all `success`, all
  from the app with id **15368** (`github-actions`). The commit's GitHub author is `Hafeok`, user
  id **2194785**.
- `GET /repos/.../rulesets` returns `[]`: the repository has no rulesets.
