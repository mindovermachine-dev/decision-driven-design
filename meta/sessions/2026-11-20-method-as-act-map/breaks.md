# What this breaks — deliverable 4

Each row is something `DDD-dec-124` breaks or leaves stale elsewhere, with a draft issue. **None of
them is changed by this session**, and no issue is opened: the drafts are for Emil. Line numbers
are at `1ecf914` unless marked. Rows B-1 to B-6 are the issue's list. B-7 to B-12 come from the
survey and the worked example.

| # | What breaks | Where | Draft |
|---|---|---|---|
| B-1 | #74's plugin runs the method "one step at a time, from its step cards" (`/ddd-method:run 1`). Its evals test step 1 and "a `[PROPOSED]` step asked to run as ruled" | `plugins/ddd-method/` on `claude/confident-goldberg-c0y0ia` (head `d80a102`): 19 lines in 9 files, among them `README.md:3-4, 24-25`, `skills/run/SKILL.md`, `evals/step-1-small/` | D-1 |
| B-2 | `quick-start.md` runs "step 1" from declared axes, with no scope and no pull, and calls step 1's exit check and claims its own | `method/quick-start.md:1, 3, 12-13, 18, 63, 107, 117, 124, 131` | D-2 |
| B-3 | The version rule counts ten steps. 1.0 is "all ten steps are ruled", and MINOR moves "when a step card is added or a step's register moves". Under four moves, the 1.0 condition names nothing. Step 1's register moving is MINOR under the rule as it stands | `DDD-dec-82` (statement); `README.md:43-44`; `GOVERNANCE.md:116-119`; `method/README.md` (old part, line 39 at `1ecf914`) | D-3 |
| B-4 | #81's outcome line orders "scope, demand, acts". G1 Q-2 and Q-5 rule the four moves. Its product-cli phase order (W9) follows | Issue #81's text | D-4 |
| B-5 | #82's core process (six moves, finding pulls before acts) is superseded in order for making a map (G1 Q-5). Its deliverable 2 places the process as "step 1's exit check" and "the content of steps 9 and 10", and neither is a step now | Issue #82's text | D-5 |
| B-6 | The cards' citations in `applications/`: "method step 7", "method step 10", "method step 1", "method step 1b, part 5/6" | `pdlc.md:46-50, 275, 345-346, 571, 682-683, 701, 708-709`; `sdlc.md:88`; `what.md:53`; `pdlc/graph/ontology.ttl:11, 34, 288, 294, 329`; `shapes.ttl:251, 338` (a message the checker prints); `demand-flow.ttl:7-8`; `check.py:19, 122, 257` | D-6 |
| B-7 | The roadmap board is "one card per method step, 1 to 10", and the maturity property moves "to `Incubating` when step 1 is reported" | `GOVERNANCE.md:146, 181-183`; `DDD-dec-81` (resolution table) | D-7 |
| B-8 | The field-report template asks for "step N" and "Which step card" | `.github/ISSUE_TEMPLATE/field-report.md:3-4, 16-18, 24` | D-8 |
| B-9 | The lifecycle data holds "frame the issue" (o1) as one act site at locus "declared". Under the trace's step 3 it is two sites on the change-locus axis, one inside the How owner's scope and one outside. And "frame own-ground work" (oG) declares no reading, so its pull cannot be found | `applications/pdlc/graph/acts.ttl` (o1); `applications/sdlc/acts/acts.ttl` (oG); `make-an-act-map.md`, worked example | D-9 |
| B-10 | The unsealed T2b pre-registration needs G1 P-7's items: T-2 superseded by the trace, T-7 (group A for every act) and T-8 (the edge pass) added | `prereg-t2b.md`, not yet written; design branch `claude/t2b-design-2026-10-26` (head `50807e0`) | D-10 |
| B-11 | Claims whose `breaks` or `notes` name a step: `DDD-address-06` (region, "method steps 2 to 10"), `-08` and `-10` ("Step 1b's …"), `DDD-flow-01` (notes), `DDD-flow-04` ("step 7's line"); and `core/claims/README.md:24` ("method step 1b") | `core/claims/` | D-11 |
| B-12 | The next release. Step 1's register moved and a card was added, which is MINOR under `DDD-dec-82` as it stands. Its descriptor and `CHANGELOG.md` section are not written | `releases/` | D-12 |

## Draft issues

Each in the shape #88 uses: outcome, ground, deliverable, out of scope. Text only.

**D-1. The method plugin reads one card, not ten.** Outcome: the plugin of #74 runs making an act
map: it reads `method/make-an-act-map.md` and offers its four moves, each `[PROPOSED]`, and refuses
to treat any move as ruled. Ground: `DDD-dec-124`, `DDD-dec-121`, #74's branch. Deliverable: the
skill and evals rewritten on #74's branch after its hold lifts, an eval for "a not-live card asked
to run", and the eval table re-run. Out of scope: method content.

**D-2. The quick start makes an act map.** Outcome: `quick-start.md` runs the four moves on the
HTTP slice of Varve: scope first, an act placed, the trace to the edge, and its pull named. The
present page stays below a superseding section. Ground: `make-an-act-map.md`, `DDD-dec-77`,
`DDD-dec-124`. Exit: the junior-engineer test can be run on the page as written. Out of scope:
Varve.

**D-3. The method's version without ten steps.** Outcome: a decision superseding `DDD-dec-82`'s
mapping: what 1.0 means when the method is four moves, and what moves MINOR (a move's register; a
field of the act description; a card). Ground: `DDD-dec-82`, `-75`, `-124`, `GOVERNANCE.md`
"Releases". Deliverable: options with their weakest points; the decision; the three texts that
restate the rule. Out of scope: cutting a release.

**D-4. #81 follows #88's G1.** A comment for Emil to post or not, not an issue: #88's G1 ruled the
four moves (Q-2, Q-5). #81's outcome line ("scope, demand, acts") and product-cli's phase order
read under them. Group A of the act description is what the What's kinds map onto (#88
`proposals.md`, Part D).

**D-5. #82 starts from the four moves.** A comment for Emil, not an issue: #82's six-move process
is superseded in order for making a map (G1 Q-5), and its moves 4 to 6 stay its own, as the check
of a map. "Step 1's exit check" and "steps 9 and 10" are no longer steps. X-1 and X-2 stand.

**D-6. `applications/` cites moves and fields, not steps.** Outcome: each citation of a method
step in `applications/` names the move or the act-description field instead, by superseding
section where the text is ruled, and the graph data's comments and the shape message are changed
with the lifecycle's own decision. Ground: survey rows for `applications/`; `DDD-dec-114`
(R28's mapping onto step 7, which becomes field B-6). Out of scope: any act.

**D-7. The roadmap and the maturity property.** Outcome: the roadmap board has one card per move,
or one card for the method, and the maturity trigger is restated without step 1. Ground:
`GOVERNANCE.md`, `DDD-dec-81`. A ruling is needed on each.

**D-8. The field report asks for a move.** Outcome: the template asks which move, which card and
commit, and which act-description fields were filled. Ground: `make-an-act-map.md`, `DDD-dec-124`.
A PATCH.

**D-9. The lifecycle map, read with the trace.** Outcome: "frame the issue" (o1) is two act sites
on the change-locus axis, in both the PDLC and the SDLC data, and "frame own-ground work" (oG)
declares its readings with their sources (the DORA trends from the deployment record; a
dependency advisory at the edge; others as the How owner names them). Ground: the worked example
in `make-an-act-map.md`; `sdlc.md` §5; `DDD-address-07` (a shared act must have one address in
both maps). Out of scope: the What.

**D-10. T2b's pre-registration carries the four moves.** Outcome: `prereg-t2b.md`, when written
and sealed, carries T-1 and T-3 to T-6 as registered on 2026-11-18, T-2 as superseded by the
trace, and T-7 and T-8. The pre-registration of 2026-09-27 is not edited. Ground: #88 G1 P-7;
`effects.md` of 2026-11-18.

**D-11. Claims that name steps.** Outcome: a notes entry on each claim listed in B-11 reading its
step references under `DDD-dec-124`, no field reworded; `core/claims/README.md` updated. Ground:
`DDD-dec-124`; the `DDD-address-02` and `-09` precedent.

**D-12. Release the act map.** Outcome: a descriptor for the next MINOR release under
`DDD-dec-82` as it stands, or under D-3's decision if that lands first, with `CHANGELOG.md` from
`canon changelog`. Ground: `DDD-dec-124`, `-82`, `releases/`. Out of scope: anything not landed.

**D-13. The front door names the current release** (drafted at G1, `proposals.md`, Part E).
