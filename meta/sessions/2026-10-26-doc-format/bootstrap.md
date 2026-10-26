# Bootstrap — doc format

Filled in at arrival and committed with `prompt.md` as the session's first commit.

| Parameter | Value |
|---|---|
| Invocation | The contents of `prompt.md`, given verbatim |
| Principal | Emil (sole ratifier) |
| Upstream repo | github.com/mindovermachine-dev/actor-indexed-determination |
| Upstream base | `1cb3819` — head of `main` at arrival; tag `v5.15.1` verified to point at it |
| Downstream repo | github.com/mindovermachine-dev/decision-driven-design |
| Downstream base | `baec167` — head of `main` at arrival |
| Pin | `graph/upstream.yaml` `ref: v5.15.1`, verified at arrival |
| Branch | `claude/doc-format`, from `origin/main` |
| Next free decision ID | `DDD-dec-39` expected (highest is `DDD-dec-38`, in both repositories); confirmed at GATE 1 |
| Gates | 0 arrival · 1 survey · 2 format · 3 pilot · 4 roll-out · 5 close |

## Context at arrival

- The session arose from Emil's observation that `apparatus/` documents read like canon. The pre-arrival survey found that none of the seven has a claim file behind it, and that their status is carried in prose headers. `adversarial-ground.md` names `core/` as its destination.
- The harness guide session (`2026-10-25-harness-guide`, branch `claude/harness-guide`) is parked at GATE 0. Its placement and its basis in `apparatus/tool-contract.md` depend on this session.
