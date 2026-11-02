# Bootstrap — applications/ for readers, 2026-11-02

Filled in at arrival and committed with `prompt.md` as the session's first commit.

| Parameter | Value |
|---|---|
| Invocation | Interactive, from the claude.ai project "Decision Driven Design". `prompt.md` carries Emil's message verbatim |
| Principal | Emil (sole ratifier; ratifies by merging the session's pull request) |
| Upstream pin | `v5.15.2` per `graph/upstream.yaml`; unchanged by this session |
| Downstream base | `e5a332d`, head of `main` at arrival |
| Branch | `claude/applications-for-readers-2026-11-02` |
| Model | Claude Opus 5.5 |
| Gates | Three, per `prompt.md` |
| Next free decision id | `DDD-dec-94`. `DDD-dec-85` to `DDD-dec-93` are held by `claude/bold-franklin-i7b16g` (PR #45), unmerged; every branch in both repositories was checked |

## Found at arrival

1. **PR #45 is open and adds `applications/sdlc/authority.md`** (head `e120251`), written in the
   same record style. This session does not edit another session's open branch. The ruled format
   applies to `authority.md` after #45 merges.
2. **The doc-format principle is ruled, but not on `main`.** On 2026-10-26 Emil ruled "only canon
   carries authority; every other folder exists for a named reader doing a named act" (pre-session
   ruling 1), and a `ddd:doc` opener with a validator check (ruling 2). Both are recorded only on
   `claude/doc-format`, which shares no history with `main` and was never merged. Its decision id
   `DDD-dec-39` now belongs to the release-head guard. This is basis loss: a ruling that governs
   this session exists only on an orphaned branch.
3. **That branch's Gate 3 pilot found the problem this charter names.** Readers of a reformatted
   `apparatus/tool-contract.md` listed decision ids, promotion numbers and "held" markers among the
   things they did not understand. Gate 1 builds on that finding.
4. **The project instructions are stale on the protocol token.** They say decprov/1. `DDD-dec-62`
   superseded `DDD-dec-53`: the token is dpp/1.
