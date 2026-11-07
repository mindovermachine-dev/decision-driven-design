# Bootstrap — the SDLC and PDLC applications, 2026-11-07

Filled in at arrival and committed with `prompt.md` as the session's first commit (`DDD-dec-20`).

| Parameter | Value |
|---|---|
| Invocation | A cloud session started on 2026-11-07 with the prompt in `prompt.md`, verbatim. Emil's rulings (Rounds 1 to 15) were given in the claude.ai question dialog on 2026-11-06 and 2026-11-07 and handed to this session in the prompt |
| Principal | Emil (sole ratifier; ratifies by landing the branch) |
| Issue | [#61](https://github.com/mindovermachine-dev/decision-driven-design/issues/61). Every commit of the session carries `Refs #61` |
| Downstream repo | github.com/mindovermachine-dev/decision-driven-design |
| Downstream base | `1ab1de0` — head of `main` at arrival, as the prompt names; **not moved** (`git rev-parse origin/main` = `1ab1de005eb60ce2ea019e9942cd52b790aab0e7` after a fresh fetch) |
| Downstream branch | `claude/sdlc-pdlc-applications-0u6318` (assigned by the harness) |
| Upstream repo | github.com/mindovermachine-dev/actor-indexed-determination (read only), checked out at `v5.15.2` = `084bce7` |
| Upstream pin | `v5.15.2` (`graph/upstream.yaml`). No advance in this session |
| Reference repos (read only, shallow clones of the default branch at arrival) | `Hafeok/varve` at `81fba3d`; `mindovermachine-dev/how-we-work` (takt) at `4e11a1b` |
| Signing | `Claude (Emil) <claude+emil@okkels-klein.dk>`, key `SHA256:xDu5EyJd05ROum1g+8Aj1Up3MjE6RbHnI70/xNHljDY` |

## Decision ids

Checked across every branch of both repositories at arrival (2026-11-07), by listing every file
on every remote branch and extracting `DDD-dec-<n>`.

- **Downstream** (every `origin/*` branch, `core/decisions/`): the highest is `DDD-dec-113`.
- **Upstream** (every branch, every path): the highest is `DDD-dec-39`.

Both agree with the prompt. This session takes **`DDD-dec-114`** (the PDLC decision) and
**`DDD-dec-115`** (the SDLC decision).

## Arrival finding A-1 — `DDD-address-01` is not an upstream claim

The prompt names `DDD-address-01` among the upstream claim files and asks that both decisions'
`basedOn` pin it through `graph/upstream.yaml`. At `v5.15.2` (`084bce7`) no file upstream
defines any `DDD-address-*` id. The claims `DDD-address-01` to `-05` are **this repository's**
(`core/claims/DDD-address-0[1-5].yaml`, filed with `DDD-dec-38`'s act address landing). Pinning a
local id as upstream would fire E12 (pinned id absent at ref). So `DDD-address-01` enters both
decisions' `basedOn` as a local claim, resolved by the validator in `core/claims/`, and no pin
is added for it. `DDD-frame-01`, `DDD-frame-02` and `DDD-ground-06` are upstream and already
pinned at `v5.15.2`. The prompt's intent (every basis instrumented) holds; only the route
differs. Reported to Emil in the session's findings.

## Gates

| Gate | What | Who |
|---|---|---|
| G0 | This charter committed before any other change | Claude |
| G1 | `rulings.md`; `DDD-dec-114` and `DDD-dec-115` filed; `applications/pdlc/README.md`, `pdlc.md`; `applications/sdlc/sdlc.md` and its graph data; the two README updates; `successor-items.md`; predictions before each operation; `scripts/ci.py` green; CI green on the pushed head | Claude; **stops for Emil** |
| G2 | Rule the specs; land the branch (`canon land`) | **Emil** |

## Scope

In scope: the files above, this session record, and the session's row in
`meta/sessions/README.md`. Out of scope: workflows, actions and the dispatcher (successor items),
every claim file, every pin, `scripts/`, CI, `tools/canon/`, and this repository's own trunk
governance (`DDD-dec-108` to `-110`, unchanged).
