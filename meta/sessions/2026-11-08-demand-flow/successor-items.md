# Successor items — map the flow of demand, 2026-11-08

Open items this session raises and does not close. Each is for Emil unless it says otherwise.

| # | Item | Closes it |
|---|---|---|
| N-1 | **The numbering of the new step.** Renumber steps 2–10 to 3–11, or keep a stable number such as 1b. What each touches is below. **Claude recommends option B**, for the reason the claim graph forbids renumbering: references already filed (`DDD-dec-114`'s "method step 7") keep their meaning. `UNVERIFIED — Emil review` | A ruling, filed as a decision |
| P-1 | **Promotion of `DDD-flow-01` to `-04` upstream.** The evidence needed: a second process mapped with step 1b, whose declared kinds of demand either match the PDLC's (new, owed, own-ground) or do not, with the source of pull behind each keep, add or drop. Until then nothing is proposed in `actor-indexed-determination` (Round 24). `DDD-flow-02` and `-03` depend on the kinds; `DDD-flow-04` depends on them least, and whether it can go up alone is for Emil | A second process's declaration, recorded (a field report citing `DDD-dec-118`), then a ruling |
| E-1 | **The two sustained examples.** The method's sustained example is the HTTP slice of Varve's quick start (ruled 2026-11-02, `method/quick-start.md`). Step 1b's is the PDLC (Round 23). The project asks for one sustained example through every step. Options as Claude sees them: map the flow of demand in Varve's HTTP slice too (it has one kind of demand at most, request handling, so it would test the starting point thinly); or name the PDLC the sustained example from step 1b on; or keep two, each named where it is used | A ruling |
| A-1 | **The area name `flow`**, proposed in `bootstrap.md` against `pdlc`, `demand` and `delivery` | A ruling; renaming before landing is free, after it is forbidden |
| R-1 | **Closed by Round 26, demand-flow `rulings.md` (2026-11-10).** Was: `DDD-flow-03`'s tension, whether "detects" meant first sighting or classification for owed demand sighted on the How owner's telemetry and entered at the What owner's oC. Ruled: sighting and entry are separate; entry is the act that assigns the kind; the How owner may sight a defect, but only the What owner says whether it is a bug. `DDD-flow-03` amended in place; `check.py` now refuses an item that reaches its entry act by no declared seam | **Closed** |
| R-2 | **Two readings in the graph data.** Where each kind is discharged (`lc:dischargedAt`: new at o16, owed and own-ground at o13), and that owed demand is ordered on the How owner's record, the What in force having been read at oC (`lc:judgedOn lc:HowOwner`). pdlc.md §9 says owed demand "is judged on the What in force"; Claude reads that as the classification, not the ordering. `UNVERIFIED — Emil review` | A ruling, or the step's own ruling |
| R-3 | **Rulings.md readings R-a and R-b** (the starting point is a default to test; the claims keep Round 23's wording narrowed by region) | Emil's review |
| C-1 | **`scripts/ci.py` does not run `applications/pdlc/graph/check.py`.** It did not before this session either. The flow checks added here, like the act map's, run only by hand. Adding a gate is a change to CI and is not this session's | A session on CI (Claude can do it on request) |
| C-2 | **The 2026-11-07 session's `rulings.md` says "Rounds 23 to 25 are not in this record … If those rounds exist elsewhere, they are not recorded here."** They are now recorded in this session's `rulings.md`. A pointer there would close the loop; that record is history and this session does not edit it | Emil's choice: a one-line pointer, or nothing |
| G-1 | **GOVERNANCE.md's roadmap board**: "one card per method step, 1 to 10". A card for 1b is board work, outside the repository | Emil |

## N-1, what each option touches

Surveyed on the branch at this session's head. Filed decisions and release records are never
edited; where they carry a step number, the note says what happens to it.

**Both options** have to change the count "ten steps", which a new step makes wrong:
- `method/README.md`, three places: the opening line ("ten steps, each presented as a step card"),
  the weakest-point note ("The ten steps, their order and the step card's fields come from one
  session draft"), and the release rule ("The version stays below 1.0 until all ten steps are
  ruled").
- `README.md`, below its status table: "It stays below 1.0 until all ten steps are ruled."
- `GOVERNANCE.md` line 118 (the same rule) and line 181 (the roadmap, "1 to 10").
- `DDD-dec-82`'s statement: "It stays below 1.0 until all ten steps are ruled." A filed decision is
  not edited. The rule needs a decision that amends it ("all steps", or "all eleven"), which is
  itself a governed change to when 1.0 can be reached.
- History that stays as it is: `releases/v0.5.0.yaml` line 40 and `CHANGELOG.md` line 39 ("ten
  steps is ruled").

**Option A, renumber 2–10 to 3–11**, also touches:
- Nine file renames, `method/02-…` to `method/10-…`, and `01b-…` to `02-…`.
- `method/README.md`'s table (eleven rows renumbered) and `README.md`'s status table.
- Every card's title ("Step N —") and its Previous and Next links: all eleven cards.
- Links to the card files from `README.md` and `applications/pdlc/pdlc.md`.
- Cross-references by number in prose: `applications/pdlc/pdlc.md` §0 ("method step 7"), §2.1's
  telemetry row ("method step 10"), §5 ("step 10"), §6 ("Mapped to method step 7").
- Filed references that cannot be changed: `DDD-dec-114` (its R28, "the mapping to method step 7",
  and its notes). After a renumber, "step 7" there means today's step 7, which would be step 8. The
  claim graph forbids renumbering for exactly this reason.
- The project instructions (`AGENTS.md`, `CLAUDE.md`) name no method step by number; nothing to
  change. The field-report issue template says "step N" generically; nothing to change.
- The release: under `DDD-dec-82`, renumbering is an editorial change (PATCH) or a supersession of
  the sequence; the mapping does not say which.

**Option B, a stable number (1b)**, touches nothing beyond the count above. The file
`method/01b-map-the-flow-of-demand.md`, the table rows and the cross-references this session wrote
already use it. Its costs: a later insertion takes another letter (4b and so on), and the order is
no longer the integers.
