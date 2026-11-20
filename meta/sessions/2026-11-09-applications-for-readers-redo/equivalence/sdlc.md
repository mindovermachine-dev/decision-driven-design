# Equivalence — `applications/sdlc/sdlc.md`

Old: `84aa466:applications/sdlc/sdlc.md` (762 lines). New: the Gate B rewrite (831 lines).
Every numbered section §0 to §19 kept its number, title and order. No `ddd:ref` marker changed.
These rows are the writer's. They are not evidence of equivalence; the independent check is.

| # | Old: section and rule, in brief | New: section | Note |
|---|---|---|---|
| 1 | Register banner: ruled (Rounds 28 and 30); two layers (what the decision files; what Round 28 ruled); exposition covered by no item is governed by the decision | Opening "How settled this is"; "Where this comes from", first paragraph | same; rounds moved to the closing section |
| 2 | Where this text and `DDD-dec-115` disagree, the decision governs | Opening; "Where this comes from" | same |
| 3 | The arrangement is the SDLC and has no other name; not Delivery, with the reason | Opening | same; the quotes moved to the table |
| 4 | Scope: a product repository that adopts it; this repository's trunk stays under `DDD-dec-108`–`110`, unchanged | Opening | same; ids moved |
| 5 | Upstream basis pinned at v5.15.2; three `ddd:ref` markers | Opening | same; markers unchanged |
| 6 | §0: the weakest point; two untested assumptions; if either fails, force fails and the ruled shape stays | §0 | same ("ruled" → "decided") |
| 7 | §1: composite act within the PDLC, owned by the How owner | §1 | same; Round 5's quote paraphrased with the same content, quoted in the table |
| 8 | §1: inputs (issue by three entries; the What; product assurance), outputs (production dark; the record; telemetry), no calendar input | §1 | same |
| 9 | §2: axes accepted for now, revisited after first recorded issues; declared before positions are read | §2 | same; O-3 cross-reference added (it is the same item) |
| 10 | §2 table: three axes, values and reasons | §2 | same; "(`DDD-dec-114` P-8)" → "(the PDLC's locus, `../pdlc/pdlc.md` §7)" |
| 11 | §2: occupant not an axis nor in any address (`DDD-ground-06`) | §2 | same; status of the basis stated in words: projected upstream (`graph/upstream.yaml`, `status_at_pin: projected`) |
| 12 | §3: act map as graph data; SHACL regime; one address, one owner, PDLC ▸ SDLC path, occupant lens; acyclic within an issue; the checker command | §3 | same; "the regime of `DDD-dec-113` E-1" → "the same regime as the What" |
| 13 | §3: the stream o1b–o13 | §3 | same, verbatim block |
| 14 | §3: o8 and o14 retired, ids not reused | §3 | same |
| 15 | §3: three causal-index readings (ruled R12) | §3 | same; claim ids moved to the table |
| 16 | §4: the four stores; each step card's Discharges / Store / Cost | §4 | same; "(Round 2)" on o9 and o10's quote removed from prose, content kept ("o10 carries production acceptance" restated) |
| 17 | §5: the issue as seam; plan before allocation; allocation its own act; same addresses for either occupant | §5 | same |
| 18 | §5: whether o10 needs another person; three bullets | §5 | same |
| 19 | §5: implementation assurance sets whether self-acceptance is enough | §5 | same |
| 20 | §5: implementation assurance defined; How owner's; three parts table; independence levels self/independent | §5 | same; Round 19 and R3 moved to the table |
| 21 | §5: a How decision anchored to the What element, or declared on the issue; o9, o11 read it as ground | §5 | same |
| 22 | §5: not product assurance; judged at ready-for-users; the first version's misplacement moved by Round 19 | §5 | same; history kept in one sentence without the round |
| 23 | §5: tune down until outcomes move; Emil's quote | §5 | same; the quote paraphrased ("If neither moves, that is fine: the verification removed was probably not giving any value") and kept verbatim in the table |
| 24 | §5: relation to Varve ADR 0088, three bullets | §5 | same; `DDD-dec-109` → "this repository's own trunk rule" |
| 25 | §5: falsifier | §5 | same |
| 26 | §6: takt's shape with Varve's force; candidate; trailers and gate; approval and landing; precedence (Round 2's "Drop it" governs) | §6 | same; the precedence restated as "an earlier ruling … a later ruling dropped the squash. Both are recorded, and the later governs" |
| 27 | §6: the mechanics 1–6 and the ruleset | §6 | same |
| 28 | §6: what leaves takt (READY_PUSHER, pr-to-ready, on_semver) and why | §6 | same |
| 29 | §6: where Varve's force changes; new and unexercised | §6 | same |
| 30 | §7: main deploys to prod; o10 carries production acceptance; dark behind a toggle | §7 | same |
| 31 | §7: o13, dark by default, toggles.yaml checked at o9; creating and retiring the How owner's; retiring never turns on | §7 | same |
| 32 | §7: turning on is the PDLC's (o16, When owner, refused without verdict; `DDD-dec-114` P-4) | §7 | same; P-4 → `../pdlc/pdlc.md` §12, which states it |
| 33 | §7: state outside the trunk, with the reason | §7 | same |
| 34 | §7: the store is a service the When owner uses, recording traceability; branch-file alternative rejected; Round 30's "not the whole PROV-O" | §7 | same; "ruled differently from the proposal" made explicit in words ("decided otherwise than proposed") |
| 35 | §7: what the service does; four recorded facts; `lc:ToggleOnShape`; who reads; the SDLC never writes on state | §7 | same |
| 36 | §8: the request quote | §8 | same in substance ("All communication happens on the issue, and the issue controls the developer session behind it"); quote verbatim in the table |
| 37 | §8: who may allocate; locus label; kind label; which comments are instructions (three conditions); data; framing; control verbs table | §8 | same; `DDD-dec-109` rule 5 moved to the table |
| 38 | §9: Round 1's ruling with its option text | §9 | same content as plain statement; the verbatim ruling in the table |
| 39 | §9: the port, whole, of ADR 0087 with amendments, read at Varve `81fba3d`; "The whole section is ruled (Round 28, R21)" | §9 | same; R21 moved to the table, and a pointer to §11 added |
| 40 | §9: the map (humans, agents, exempt, delegate changes, holders of Approve) | §9 | same |
| 41 | §9: the three gates, verbatim quotes and regex | §9 | same |
| 42 | §9: the exit to the ledger; identities.json retired | §9 | same |
| 43 | §10: How one layer up; stricter rule (main judges; the base decides); cannot approve itself; `DDD-address-03`'s case | §10 | same; claim status stated in words (local, projected) |
| 44 | §11: "Each is flagged as a departure; D-1 to D-8 ruled (R21), D-9 ruled (R1)" | §11 | same ("All nine are decided"); rounds moved |
| 45 | §11: D-1 to D-9, each departure and reason | §11 | same; in "Why", decision ids and round numbers replaced by what they are (this repository's trunk rule; the PDLC's owners and placement rule, `pdlc.md` §2, §6; "decided with the landing"); D-9's "Tension"/"Proposed:"/"Ruled (R1): as proposed" collapsed to "Decided:" with the proposal's content |
| 46 | §12: Round 1's "Claude Code Action"; sources [GA], [SEC], [USE]; nothing from memory | §12 | same |
| 47 | §12: triggering, who may trigger, comments and injection, pushes and CI, branches, signing, cost | §12 | same; "this is unverified" → "This is not verified" (a fact about the docs, not a register mark) |
| 48 | §13: session records (prompt, bootstrap with its fields, committed by o4, each run records what it read) | §13 | same; `DDD-dec-20`, `DDD-dec-52` moved; `DDD-dec-52`'s content kept as the reason |
| 49 | §13: the occurrence record from edition 1 (Round 2, with option text) | §13 | same, as plain statement |
| 50 | §13: the field table | §13 | same; "`DDD-dec-52`" in the Ground read row → "What the occurrence read" |
| 51 | §13: where stored (R23): orphan branch, ruleset, why the App | §13 | same |
| 52 | §13: the checker over "an illustrative record of one invented issues, #101 (new) and #103 (owed …)" with 10 plants plus one DORA plant | §13 | **fact corrected**: the record holds three invented issues, #101, #103 and #104 (own-ground, charter only) (`acts/example-record.ttl` l. 124–133); `check.py` run confirms 10 plants plus one DORA plant |
| 53 | §13: the two fields from Round 22 | §13 | same |
| 54 | §13: the SDLC's output; forecast from throughput and flow time (ruled, Round 27, Kanban cycle time; P-14); DORA keys; split of capacity | §13 | same; "based on the Kanban cycle time" kept, ids moved |
| 55 | §14: hotspots computed from the record; o5 ↔ o6 (why, three classes with levers, metric); o10 (why, lever, metric); worked numbers | §14 | same |
| 56 | §15: nine falsifiers | §15 | same; the replacement falsifier's history ("Claude's (Round 20), ruled by Round 28 (R20). It replaces Claude's Round 19 falsifier … which Emil withdrew") → "This replaces an earlier falsifier … which was withdrawn"; the round history is in the table |
| 57 | §16: Round 22's ruling with option text; the classifier; kinds defined in pdlc.md §9 | §16 | same, as plain statement |
| 58 | §16: the table; act map scoping; the shape; what the PDLC reads; When sees only cadence; owed fix usually not dark; the guard from both sides | §16 | same |
| 59 | §17: oR is the PDLC's; the SDLC supplies two things; the check; "the H-9 pattern (`DDD-dec-60`, now `DDD-dec-70`)"; gap never "unknown"; in the record; until the schema has observation needs | §17 | same; H-9 described as "the How's pattern for measurement wiring, a contract over `telemetry` facts (`how.md` §4.2)", where how.md states it |
| 60 | §18: Round 20's quote; answerability in core/05 §5's sense; the table of four keys | §18 | same; quote paraphrased, verbatim in the table |
| 61 | §18: production is an input; the reading's shape; the worked values | §18 | same; values re-run by `acts/check.py` and unchanged |
| 62 | §18: the forecast's spread (Round 29) | §18 | same |
| 63 | §18: which occurrences feed each key; flow time a different interval | §18 | same |
| 64 | §19: O-1, O-2, O-3 | §19 | register: unmarked open items → *(open)*; content same |
| 65 | §19: O-4 to O-7 "Ruled (Round 28, Rn)", closed | §19 | same ("Closed."); rounds moved to the table |
| 66 | §19: O-8, with "Proposed, not ruled:" and "Whether a model may occupy it … is open" | §19 | register kept: *(open)* for the item, *(proposed, not yet ruled)* for the proposal, *(open)* for the model question; content same |
| 67 | §19: O-9 | §19 | register kept: *(open)*; content same |
| 68 | (none) | §19 preamble: the O-numbers are this document's own, separate from `pdlc.md` §15's | added from Round 31's "How it governs" (record of fact, no rule) |
| 69 | (none) | "Not settled yet" | added, as the format requires; lists only what §19 and §0/§12 already leave open |

## Not restated

None. Every normative sentence is in the new text with the same strength.

## Register notes

- R5's "PROV" reading is not `UNVERIFIED` at `84aa466`: Round 30 withdrew Claude's PROV-O reading
  and ruled "traceability for the act". The old text already said so, and the new text keeps it as
  decided.
- O-8 holds two registers in one item: the proposed act, and the open model-occupancy question.
  Both are marked separately.
