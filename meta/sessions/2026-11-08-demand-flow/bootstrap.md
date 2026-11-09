# Bootstrap — map the flow of demand, 2026-11-08

Filled in at arrival (2026-11-09) and committed with `prompt.md` as the session's first commit.

| Parameter | Value |
|---|---|
| Invocation | Interactive. The rulings (Rounds 23 to 25) were given in the claude.ai project conversation of 2026-11-07/08; `prompt.md` carries them verbatim |
| Principal | Emil (sole ratifier; ratifies by landing the branch) |
| Issue | [#67](https://github.com/mindovermachine-dev/decision-driven-design/issues/67). Every commit of the session carries `Refs #67` |
| Upstream repo | github.com/mindovermachine-dev/actor-indexed-determination, **read only** (Round 24: nothing is written upstream) |
| Upstream head at arrival | `main` = `084bce7` = tag `v5.15.2` (28 remote branches) |
| Upstream pin | `v5.15.2` in `graph/upstream.yaml`, as the prompt requires. Unchanged by this session |
| Downstream repo | github.com/mindovermachine-dev/decision-driven-design |
| Downstream base | `2f575f3`, head of `main` at arrival. **`main` has not moved past `2f575f3`** |
| Downstream branch | `claude/map-demand-flow-dvsjl9`, from `main` at `2f575f3` |
| Model | Claude Opus 5.5 |

## Gates

| Gate | What | Who |
|---|---|---|
| G0 | This charter committed before any other change; item 0 checked | Claude |
| G1 | `rulings.md` (Rounds 23–25 verbatim); `DDD-flow-01`…`04` filed; `DDD-dec-118` filed; the step card, the worked example and its graph data; `method/README.md` and the one-line relations in steps 1 and 7; `scripts/ci.py` green; pushed, CI green | Claude; **stops for Emil** |
| G2 | Land the branch (`canon land`); cut the MINOR release (`DDD-dec-82`) | **Emil** |

## Item 0 — the option pool carries no How-owner option

Checked on `main` at `2f575f3`. `applications/pdlc/graph/example-pool.ttl` holds four options, with
contributors When, What, When, When; none is the How owner's. Line 33 records that the How owner's
"manual cache purge" was removed in Round 26 (the 2026-11-07 session's `rulings.md`). `pdlc.md`
§10 says it is now issue #104 at the own-ground entry (oG). **Passes; not back.**

## Ids

Checked across every branch of both repositories at arrival (2026-11-09).

**Decisions.**
- **Upstream** (28 remote branches and every tag): the highest is `DDD-dec-39`.
- **Downstream** (every `origin/*` branch): the highest decision file is `DDD-dec-117`, on `main`.
  `DDD-dec-118` to `DDD-dec-120` appear only as range mentions in two bootstrap and findings
  records ("`DDD-dec-108` to `DDD-dec-119`", "`DDD-dec-116` to `DDD-dec-119`", and a corrected
  "`DDD-dec-120`"). None of these is use, as the specification-feasibility bootstrap ruled for the
  same kind of mention. Validator fixtures `DDD-dec-9xx` are not decisions.
- **This session takes `DDD-dec-118`.**

**Claims.**
- Areas held downstream: `address`, `cost`, `delivery`, `org`, `sim`, `tool`, `track`. Upstream:
  `agent`, `cost`, `delivery`, `floor`, `frame`, `ground`, `hyp`, `measure`.
- No file or text on any branch of either repository uses `DDD-flow-`, `DDD-pdlc-`,
  `DDD-demand-` or `DDD-pull-`.
- **This session takes `DDD-flow-01` to `DDD-flow-04`**, a new area. Proposed, for Emil:

**The area name, proposed: `flow`.** Why, and why not the others:
- **`flow`** names the method step ("map the flow of demand") the four claims are filed for. It is
  not a term upstream (`core/graph/terms.yaml` has `term:overflow` only).
- **Not `pdlc`.** The scope is the PDLC, and `DDD-org-01` puts scope in `region`, not in the id.
  Ids travel with a claim if it relocates and are never reused. If a second process gives the
  evidence and a claim is promoted, a `pdlc` id would name a scope the claim no longer has.
- **Not `demand`.** `term:demand` ("determination demand") is settled upstream, established by
  `core/01`. An area named `demand` reads as claims about that term, and these are about how
  demand items arrive and are ordered, not about what demand is.
- **Not `delivery`.** `core/13` holds it.
- **The caution.** "Flow time" is a ruled name in the PDLC (the 2026-11-07 session's Round 27;
  `pdlc.md` §15 O-9), for the forecast's interval o2b to o13. The area and that name share a word
  and nothing else. Flagged so the two are not read together.

## Read at arrival

- Upstream at `v5.15.2`: `core/05-accountability.md` §2 and §5; `core/13-delivery.md`;
  `core/14-indexed-determination.md` §1 and §5; `DDD-delivery-01`…`03`, `DDD-frame-01`, `-02`,
  `DDD-ground-01`, `-06`; `core/graph/terms.yaml` (`term:demand`, `term:seam`, `term:escape`,
  `term:judgment`, `term:delivery`).
- Downstream: `method/README.md`, `method/01-map-and-index-acts.md`,
  `method/07-complete-accountability.md`; `DDD-dec-74`, `-82`, `-114`, `-116`, `-117`;
  `applications/pdlc/pdlc.md` §2, §6, §7, §9, §10, §13–§15; `applications/pdlc/graph/acts.ttl`,
  `example-pool.ttl`; `applications/sdlc/sdlc.md` §3 (the stream); `core/claims/README.md`,
  `spec/claim-format.md`, `scripts/validate-claims.py`.

