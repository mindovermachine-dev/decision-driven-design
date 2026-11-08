# Bootstrap — specification feasibility, 2026-11-08

Filled in at arrival and committed with `prompt.md` as the session's first commit.

| Parameter | Value |
|---|---|
| Invocation | Interactive. The rulings were given in a claude.ai project conversation on 2026-11-08 and filed from the same conversation. `prompt.md` carries Emil's messages verbatim |
| Principal | Emil (sole ratifier; ratifies by landing the branch) |
| Issue | [#62](https://github.com/mindovermachine-dev/decision-driven-design/issues/62). Every commit of the session carries `Refs #62` |
| Upstream repo | github.com/mindovermachine-dev/actor-indexed-determination (read only in this session) |
| Upstream pin | `v5.15.2` (`graph/upstream.yaml`), unchanged by this session |
| Downstream repo | github.com/mindovermachine-dev/decision-driven-design |
| Downstream base | `1ab1de0` — head of `main` at arrival |
| Downstream branch | `claude/specification-feasibility-2026-11-08` |
| Read only | `mindovermachine-dev/product-cli` at `4ce90e9` (main) and at the tag `rust-final`; `Hafeok/product-framework` |
| Parallel work | `claude/sdlc-pdlc-applications-0u6318` (session `2026-11-07-sdlc-and-pdlc`, unlanded), which holds `DDD-dec-114` and `DDD-dec-115` and touches `applications/sdlc/` |
| Model | Claude Opus 5.5 |

## Gates

| Gate | What | Who |
|---|---|---|
| G0 | This charter committed before any other change | Claude |
| G1 | `rulings.md`; `DDD-dec-116` and `DDD-dec-117` filed; `findings.md`, `successor-items.md`; predictions before each run; `scripts/ci.py` green; pushed | Claude; **stops for Emil** |
| G2 | Land the branch (`canon land`) | **Emil** |

## Scope at arrival

In scope: `DDD-dec-116`, `DDD-dec-117`, this session record, and the session's row in
`meta/sessions/README.md`.

Out of scope, and listed in `successor-items.md`: applying the rulings to `what.md`, the `sdlc:`
ontology and shapes, `authority.md`, `how.md` and `applications/sdlc/product-cli/product-definition.md`;
any change to the product-cli repository; every claim.

## Decision ids

Checked across every branch of both repositories at arrival (2026-11-08, 12:15 UTC).

- **Upstream** (`actor-indexed-determination`, 28 remote refs): the highest id on any branch is
  `DDD-dec-39`.
- **Downstream** (every `origin/*` branch): the highest decision file is `DDD-dec-115`, on
  `claude/sdlc-pdlc-applications-0u6318`. `DDD-dec-116` to `DDD-dec-119` appear only in
  `2026-11-03-protect-main/bootstrap.md`, as part of a range checked free ("`DDD-dec-108` to
  `DDD-dec-119`"). No session reserves them.

This session takes **`DDD-dec-116`** and **`DDD-dec-117`**.

**Correction (Claude).** In the conversation, Claude said the next free id "looks like
`DDD-dec-120`", reading the range mention as use. It is not use. Recorded here per the project's
rule that corrections are attributed.

## Read at arrival

- `applications/sdlc/what.md` §3.0 to §3.7, §4 and §5; `what/ontology.ttl` (the properties
  `sdlc:reads`, `sdlc:folds`, `sdlc:keyedBy`, `sdlc:projects`, `sdlc:changes`, `sdlc:mapsFrom`).
- `applications/sdlc/how.md` §4 and §5; `applications/sdlc/authority.md` §1, §5.2 and Appendix B;
  `applications/sdlc/product-cli/product-definition.md` §1 and §8.
- `core/decisions/DDD-dec-113.yaml`: Q-C2, "outside systems with no What", is open there.
- product-cli at `rust-final`: grants, roles and authoring scopes existed
  (`ledger-core/src/authority/grant.rs`, `ledger-cli` `RoleCmd`, `product-core/src/pf/authoring_scope.rs`).
  The rewrite at `4ce90e9` has none.
