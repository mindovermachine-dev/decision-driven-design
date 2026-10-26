# Bootstrap — harness guide

Filled in at arrival and committed with `prompt.md` as the session's first commit.

| Parameter | Value |
|---|---|
| Invocation | The contents of `prompt.md`, given verbatim |
| Principal | Emil (sole ratifier) |
| Upstream repo | github.com/mindovermachine-dev/actor-indexed-determination |
| Upstream base | `1cb3819` — head of `main` at arrival; tag `v5.15.1` verified to point at it |
| Downstream repo | github.com/mindovermachine-dev/decision-driven-design |
| Downstream base | `baec167` — head of `main` at arrival; matches the project instructions' pin |
| Pin | `graph/upstream.yaml` `ref: v5.15.1`, verified at arrival |
| Branch | `[OPEN]` — the harness-assigned branch, recorded when the session runs |
| Steward ground bundle | `[OPEN]` — not yet supplied. The Steward PRD and project instructions live in a separate Claude project and are not readable from this session. GATE 1 cannot run without them |
| Gates | 0 arrival · 1 survey · 2 charter and step 1 · 3 steps 2–5 · 4 steps 6–10 · 5 close |

## Deviations recorded at arrival

- **Not pushed.** The drafting session had no push credentials. `prompt.md` and `bootstrap.md` were written against the bases above and handed to Emil. The first commit happens when the session runs with write access.

## Correction after arrival (Claude, 2026-10-25)

The "Not pushed" deviation above was true when written and is superseded here, not rewritten. Push access was granted after drafting. GATE 0 was committed as `2b06bfc` on branch `claude/harness-guide` and pushed. The branch row's `[OPEN]` resolves to `claude/harness-guide`. The Steward ground bundle remains `[OPEN]`.

## Parked at GATE 0 (Claude, 2026-10-26)

Emil ruled on 2026-10-26 that the doc format session (`2026-10-26-doc-format`, branch `claude/doc-format`) runs first. This session resumes at GATE 1 after that session closes. Its placement and its reading of `apparatus/tool-contract.md` are to be taken from the format that session rules.
