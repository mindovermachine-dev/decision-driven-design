# Bootstrap — contributing and landing, explained, 2026-11-03

Filled in at arrival and committed with `prompt.md` as the session's first commit.

| Parameter | Value |
|---|---|
| Invocation | Interactive. Emil's instruction handed to this Claude Code session as its prompt; `prompt.md` carries it verbatim |
| Principal | Emil (lands the branch; this change is editorial, `DDD-dec-78`) |
| Issue | [#54](https://github.com/mindovermachine-dev/decision-driven-design/issues/54). Every commit of the session carries `Refs #54` |
| Upstream pin | `v5.15.2` (`graph/upstream.yaml`), unchanged by this session |
| Downstream base | `458d05b` — head of `main` at arrival |
| Downstream branch | `claude/optimistic-keller-trxr7y` (assigned by the harness) |
| Signing | `Claude (Emil) <claude+emil@okkels-klein.dk>`, key `SHA256:xDu5EyJd05ROum1g+8Aj1Up3MjE6RbHnI70/xNHljDY` (GitHub reports `valid` for it on `458d05b`) |

## Gates

| Gate | What | Who |
|---|---|---|
| G0 | This charter committed before any other change | Claude |
| G1 | `CONTRIBUTING.md` replaced and checked; `GOVERNANCE.md`'s settings paragraph replaced; gates green; CI green on the pushed head | Claude; **stops for Emil** |
| G2 | Land the branch (`canon land --commit`) | **Emil** |

## Scope at arrival

In scope: `CONTRIBUTING.md`, the one paragraph of `GOVERNANCE.md` under "Repository settings",
this session record and its row in `meta/sessions/README.md`. Out of scope: Departure 3 (the
agent-review round changes it), `.github/repo-standard.yaml`'s own "NOT YET APPLIED" header,
every claim and decision. No decision id is taken.
