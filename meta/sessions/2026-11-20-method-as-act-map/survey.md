# Survey — where the repository says the method has ten steps, names a step, or states step 1's register

Deliverable 1 of #88. Read at `1ecf914` (`main`), 2026-11-20. Nothing is changed by this survey.

## How it was read

- **Search.** `git grep` over the whole tree except `meta/sessions/`, for "ten steps", "all ten", "step N", "steps N to M", "method/0N", "ruled for test" and their variants. 220 raw lines. Each was read in place. The false positives are listed at the end, with why each is not a method step.
- **Beyond the issue's list.** The issue names `method/`, `README.md`, `applications/`, `core/`, `releases/` and the tooling. `GOVERNANCE.md`, `CONTRIBUTING.md`, `CHANGELOG.md` and `.github/ISSUE_TEMPLATE/` also say these things, so they are included.
- **Session records** under `meta/sessions/` are history. 54 files there mention step 1 or ten steps. They are counted, not listed: a session record is never edited, so none of them is a place #88 would change.
- **#74's branch** (`claude/confident-goldberg-c0y0ia`, held) is not on `main` and is not surveyed row by row. Its plugin has 19 matching lines in 9 files under `plugins/ddd-method/`. They are named for deliverable 4 and not touched.

## Columns

| Column | Values |
|---|---|
| Says | **10**: says the method has ten steps, or counts to ten. **N**: names a step by number. **R1**: states step 1's register |
| Held by | **Ruled**: a decision file, a claim file or a release descriptor (a release is a filed decision, `GOVERNANCE.md` "Releases"). **Exposition**: anything else. Where exposition restates a ruling, the ruling is named |

## `method/`

| File:line | Says | What it says | Held by |
|---|---|---|---|
| `method/README.md:3` | 10 | "a practical method: ten steps, each presented as a step card" | Exposition. The count is the method draft's, `[PROPOSED]` (line 7 says so) |
| `method/README.md:4` | R1 | "Only step 1 is ruled, and it is ruled for test" | Exposition of `DDD-dec-38` and `DDD-dec-74` |
| `method/README.md:5` | N | "Steps 2 to 10 are `[PROPOSED]`" | Exposition of `DDD-dec-74` |
| `method/README.md:7-8` | 10, R1 | Weakest point: "The ten steps, their order and the step card's fields come from one session draft, not from a ruling. Only step 1's form was ruled" | Exposition |
| `method/README.md:10-22` | N, R1 | The step table, rows 1, 1b and 2 to 10. Row 1: "**Ruled for test**; claims projected; waits on T2b" | Exposition of `DDD-dec-74`, `-118` |
| `method/README.md:24` | N | "Try step 1" | Exposition |
| `method/README.md:31` | R1 | The register "Ruled for test" defined. Line 36: the table's wording is Claude's, `UNVERIFIED — Emil review` | Exposition, quoting `DDD-dec-74` |
| `method/README.md:38-39` | 10 | "A step whose register moves is a MINOR release … The version stays below 1.0 until all ten steps are ruled" | Exposition of `DDD-dec-82` |
| `method/README.md:41-60` | — | The step card's nine fields, from the method draft | Exposition, `[PROPOSED]` |
| `method/01-map-and-index-acts.md:1` | N | "# Step 1 — Map and index acts" | Exposition |
| `method/01-map-and-index-acts.md:3-9` | R1 | "**Register: ruled for test, projected.** … Step 1 stands or falls on **T2b**" | Exposition of the act address rulings R-2, R-4 to R-8, filed by `DDD-dec-38`, and of `DDD-dec-74` |
| `method/01-map-and-index-acts.md:15-22` | R1 | The first part, "`[PROPOSED]` inside a card ruled for test" | Exposition of `DDD-dec-122` |
| `method/01-map-and-index-acts.md:24` | — | "**Why it comes first.** A pull cannot be placed until the map's scope says what is world, and acts cannot be mapped until the pulls say where demand enters" | Exposition of `DDD-dec-122` (11-18 R-2) and `DDD-ground-05`. The order #88 supersedes |
| `method/01-map-and-index-acts.md:28-36` | — | The five parts, in order: scope, the determinables at the edge, the three readable states, the gaps, the trace to an entry act | Exposition of `DDD-dec-122` (Q-8, S-2 option A) |
| `method/01-map-and-index-acts.md:73` | N | "Finding it before it lands is the work of assurance, in step 5" | Exposition of `DDD-dec-122` (K-3) |
| `method/01-map-and-index-acts.md:97-99` | — | "Map the acts … forward from the domain and the request" | Exposition; superseded in reading by line 18 (`DDD-dec-122`) |
| `method/01-map-and-index-acts.md:128` | N | "Step 1 only has to make the addresses they need" | Exposition |
| `method/01-map-and-index-acts.md:138` | N | Card row "Step: 1 — Map and index acts" | Exposition, citing the method draft |
| `method/01-map-and-index-acts.md:162, 164` | N | "Step 1b reads this step's act map"; "Next: 02" | Exposition |
| `method/01b-map-the-flow-of-demand.md:1, 3-14` | N | "Step 1b"; "placed after step 1"; "1b holds the step's place after step 1 until the numbering is ruled (N-1)" | Exposition of `DDD-dec-118` |
| `method/01b-map-the-flow-of-demand.md:28, 40, 57` | N | "step 1's first part"; "Step 1 maps acts"; "This is step 1, run first" | Exposition of `DDD-dec-122`, `-118` |
| `method/01b-map-the-flow-of-demand.md:147, 149` | N | Card rows "1b … After step 1"; "Ground in: The act map from step 1" | Exposition of `DDD-dec-118` |
| `method/01b-map-the-flow-of-demand.md:266-268` | N | "The step draws on step 1 …, step 4 …, step 7 …, step 9 … and step 10" | Exposition |
| `method/01b-map-the-flow-of-demand.md:287` | N | "Previous: 01 · Next: 02" | Exposition |
| `method/02` to `10`, line 1 | N | "# Step N — … `[PROPOSED]`", one per card | Exposition |
| `method/02` to `10`, lines 3-10 | N | "Register: `[PROPOSED]` … Moving the step to ruled is a MINOR release (`DDD-dec-82`)" | Exposition of `DDD-dec-74`, `-82` |
| `method/02` to `10`, line 14 | N | "What is filed, verbatim": the draft's numbered line, "> N. **Name.** …" | Exposition, verbatim from `method-instructions-draft.md` (`[PROPOSED]`) |
| `method/02` to `10`, lines 30-39 | N | "What this step adds to the act map `[PROPOSED]`": the superseding "Value made visible" and "Attaches to" rows | Exposition of `DDD-dec-122` (Q-9, K-2) |
| `method/05-classify-closure-and-set-assurance.md:37` | N | "this step classifies closure before step 6 allocates the arrangement it is closed for" | Exposition (K-2, open) |
| `method/07-complete-accountability.md:44` | N | "Step 1b places each boundary decision with one owner … this step's line is applied" | Exposition of `DDD-flow-04`, pdlc.md §6 |
| `method/02` to `10`, last line | N | "Previous: [N-1] · Next: [N+1]" | Exposition |
| `method/quick-start.md:1, 3` | N | "Quick start — step 1 on Varve's HTTP slice"; "runs step 1, map and index acts" | Exposition of `DDD-dec-77` |
| `method/quick-start.md:12-13` | R1 | "The claims under step 1 stay **projected** until … T2b has run" | Exposition of `DDD-dec-74` |
| `method/quick-start.md:18, 63, 107, 117` | N | Step 1's axes, "Step 1 maps **forward from the request**", its value, its exit check | Exposition. Starts from declared axes, with no scope and no pull: it predates `DDD-dec-122` |
| `method/quick-start.md:124, 131` | N, R1 | The junior-engineer test performs step 1; "It would not move step 1's claims from projected; only T2b can do that" | Exposition |

## `README.md` and the other front-door files

| File:line | Says | What it says | Held by |
|---|---|---|---|
| `README.md:3-6` | — | "map the acts …, place each decision …, and say which actor … makes each one": the method in one sentence; "the step cards" | Exposition |
| `README.md:8` | — | "**v0.5.0 is a preview: ready to try, not ready to use**". The tag `v0.7.0` exists, so the version named is stale (side finding, not #88's) | Exposition of `DDD-dec-74` |
| `README.md:24` | N | "What step 1 gives you today" | Exposition |
| `README.md:27-41` | N, R1 | "Status, step by step": rows 1, 1b, 2 to 10. Row 1: "**Ruled for test.** Claims projected; waits on T2b" | Exposition of `DDD-dec-74`, `-118` |
| `README.md:43-44` | 10 | "It stays below 1.0 until all ten steps are ruled. A step added or moving register is a MINOR release" | Exposition of `DDD-dec-82` |
| `README.md:48` | N | "runs step 1 on the HTTP slice" | Exposition |
| `README.md:60-62` | N | "Step 1 maps forward from the domain and the request, never back from code" | Exposition of `DDD-address-02` |
| `README.md:69-70` | N, R1 | "Every step is projected or `[PROPOSED]` (`DDD-dec-74`), and step 1 waits on its first independent application case" | Exposition of `DDD-dec-74` |
| `GOVERNANCE.md:116-119` | 10 | "The version stays below 1.0 until all ten steps are ruled. MINOR moves when a step card is added or a step's register moves" | Exposition of `DDD-dec-82` |
| `GOVERNANCE.md:146` | R1 | Maturity: "`Experimental`, moving to `Incubating` when step 1 is reported" | Exposition of `DDD-dec-81` |
| `GOVERNANCE.md:181-183` | 10 | "The method's roadmap: one card per method step, 1 to 10. A card moves as the step's register moves" | Exposition (`DDD-dec-81`, item 12) |
| `CONTRIBUTING.md:14` | — | "Report what happened when you tried a method step" | Exposition |

## `applications/`, as rewritten by #73

| File:line | Says | What it says | Held by |
|---|---|---|---|
| `applications/README.md:27, 54` | — | "The repository presents the method as ready to try, not ready to use" | Exposition of `DDD-dec-74` |
| `applications/pdlc/pdlc.md:46-50` | N | The owners are "mapped onto method step 7 (complete accountability). That step is itself *(proposed, not yet ruled)*" | Exposition of `DDD-dec-114` (Round 28, R28) |
| `applications/pdlc/pdlc.md:275` | N | "step 10, which is itself *(proposed, not yet ruled)*" | Exposition |
| `applications/pdlc/pdlc.md:345-346` | N | "**Mapped to method step 7.** The mapping is decided. The step itself is still *(proposed, not yet ruled)*" | Exposition of `DDD-dec-114` (R28) |
| `applications/pdlc/pdlc.md:571` | N | "The act map is the form of method step 1" | Exposition |
| `applications/pdlc/pdlc.md:682-683` | N | "**Method step 7** (§0, §6) and **method step 10** (§5) are *(proposed, not yet ruled)* … If step 7 changes, the mapping must be read again" | Exposition |
| `applications/pdlc/pdlc.md:701, 708, 709` | N | Sources table: "method step 7 `[PROPOSED]`", "method step 10 `[PROPOSED]`", "the step 7 mapping, Claude's, ruled" | Exposition of `DDD-dec-114` |
| `applications/pdlc/graph/ontology.ttl:11, 34` | N | "The act map's form (method step 1 …)"; `dct:source "method/01-map-and-index-acts.md; DDD-address-01"` | Exposition, as graph data. Line 34 is a triple, not a comment |
| `applications/pdlc/graph/ontology.ttl:288, 294, 329` | N | "Method step 1b"; `rdfs:comment` "(method step 1b, part 6)", "(method step 1b, part 5)" | Exposition, as graph data. Lines 294 and 329 are triples |
| `applications/pdlc/graph/shapes.ttl:251, 338` | N | "Method step 1b … the step card is [PROPOSED]"; `sh:message` "(method step 1b, part 5)" | Exposition, as graph data. Line 338 is a shape's message, which a checker prints |
| `applications/pdlc/graph/demand-flow.ttl:7-8` | N | "the worked example of method step 1b … [PROPOSED]" | Exposition (comment) |
| `applications/pdlc/graph/check.py:19, 122, 257` | N | "method step 1b" in the checker's help, a comment and a docstring | Exposition (code) |
| `applications/sdlc/sdlc.md:88` | N | The axes "are declared before any position is read on them (method step 1)" | Exposition. `sdlc.md` is ruled as a specification (`DDD-dec-115`, `-119`); this line cites the method, it does not rule it |
| `applications/sdlc/what.md:53` | N | "Step 1 of the method reads its addresses" off the What | Exposition of `DDD-dec-41`, `-42` |

No other document under `applications/` (`README.md`, `pdlc/README.md`, `sdlc/README.md`, `organizations/README.md`, `how.md`, `authority.md`, the vocabularies, `production-as-ground.md`, `product-cli/`) names a method step or the count.

## `core/claims/`

No claim **statement** names a method step. Every hit is in a region, test, breaks or notes field.

| File:line | Says | What it says | Held by |
|---|---|---|---|
| `DDD-address-06.yaml:36-37` (region) | N | "each of method steps 2 to 10 attaches to a part of it or to a record beside it (DDD-dec-122, S-1)" | Ruled (claim file, projected) |
| `DDD-address-06.yaml:44` (breaks) | — | The lifecycle graph data falls with the second limb | Ruled |
| `DDD-address-08.yaml:35` (breaks) | N | "Step 1b's use of 'a process' as its unit" | Ruled |
| `DDD-address-09.yaml:8` (region) | — | "**A pull is found at the edge first**: what crosses into the scope and out of it". Its own notes, line 53: "UNVERIFIED — Emil review: that a pull is found at the edge first is Claude's reading of 2026-11-18 E-4" | Ruled file, holding an unverified reading. In tension with the 2026-11-19 order. See finding F-2 |
| `DDD-address-09.yaml:26` (region) | N | "Finding it before it lands is the work of assurance, in method step 5 (K-3)" | Ruled |
| `DDD-address-09.yaml:31` (test) | N | "two practitioners run the five-part procedure of step 1 on one scope … The first case is T2b" | Ruled. Names the five-part procedure #88 would replace |
| `DDD-address-09.yaml:33` (breaks) | N | "Step 1's first part, which starts from scope and pull" | Ruled |
| `DDD-address-10.yaml:20` (breaks) | N | "Step 1b's classification of each source of pull into kinds" | Ruled |
| `DDD-flow-01.yaml:73` (notes) | N | "a second process mapped with the method step (method/01b-…)" | Ruled |
| `DDD-flow-04.yaml:22` (breaks) | N | "the mapping of step 7's line … onto its rows (Round 28, R28)" | Ruled |
| `core/claims/README.md:24` | N | Promotion "waits on a second process mapped with method step 1b" | Exposition |

## `core/decisions/`

| File:line | Says | What it says | Held by |
|---|---|---|---|
| `DDD-dec-74.yaml:17-18` (resolution) | N, R1 | "step 1 is ruled for test and projected, not reported; it stands or falls on T2b. Steps 2 to 10 are [PROPOSED]" | Ruled. Its **statement** says only "every method step at the register it is filed at"; the count and step 1's register are in the resolution, as the state "at the ruling" |
| `DDD-dec-82.yaml:5` (statement) | 10 | "It stays below 1.0 until all ten steps are ruled. MINOR moves when a step card is added or a step's register moves" | **Ruled, in the statement.** The one ruled text whose operative rule counts ten steps. See finding F-3 |
| `DDD-dec-82.yaml:12-14, 28` (resolution) | 10 | The question as ruled, and "1.0 is reached when all ten steps are ruled" | Ruled |
| `DDD-dec-118.yaml:5` (statement) | N | "a step of the method, placed after step 1 and filed as method/01b-… until the numbering is ruled" | Ruled |
| `DDD-dec-118.yaml:12, 22, 50` (resolution) | N | Round 23 "New step after step 1"; Round 24 "The method step stays after step 1"; "the seven-part" card | Ruled |
| `DDD-dec-118.yaml:82-83` (notes) | 10, N | "N-1, the numbering: renumber steps 2-10 to 3-11, or keep … 1b. Either way the rule 'the version stays below 1.0 until all ten steps are ruled' …" | Ruled file; an open item, not a ruling |
| `DDD-dec-122.yaml:5` (statement) | N, R1 | "method step 1 starts from scope and pull: the five-part pull procedure becomes the first part of step 1's card, [PROPOSED] inside a card ruled for test. Steps 2 to 10 each record what they add to the act map, [PROPOSED]" | **Ruled, in the statement.** #88 supersedes the order of step 1's first part, which this filed |
| `DDD-dec-122.yaml:58, 59, 62, 68, 74` (resolution) | N | Q-8 "the five parts become the first part of step 1's card"; Q-9 "The nine 'Value made visible' rows of steps 2 to 10"; Q-10 "step 1b's kinds"; K-3 "assurance's work, in step 5"; "the cards of steps 1, 1b and 2 to 10" | Ruled |
| `DDD-dec-122.yaml:81-82` (resolution) | R1 | "step 1 stays ruled for test, with a [PROPOSED] first part, and steps 1b and 2 to 10 stay [PROPOSED]" | Ruled. #88's first reading would change this register |
| `DDD-dec-122.yaml:91-92` (resolution); `:131, 133` (notes) | N | "Amends DDD-dec-118. Step 1b stays after step 1 … step 1 now starts from scope and pull"; K-3; "Open, not ruled here: step 5 classifies closure before step 6" | Ruled |
| `DDD-dec-114.yaml:305, 381` | N | "R28: the mapping to method step 7"; "mapped to method step 7" | Ruled |
| `DDD-dec-41.yaml:31, 44, 58` | N | "step 1 of the method reads its addresses off it"; "method steps 9–10 (Delivery)"; "a step 1 test item" | Ruled |
| `DDD-dec-42.yaml:14, 34` | N | "step 1 reads addresses off it"; "a decision matching no address is one in step 1" | Ruled |
| `DDD-dec-49.yaml:25`, `DDD-dec-52.yaml:5, 14` | N | Step 1's test items (verdicts that change no data) | Ruled. Statement of `-52` names "the step 1 test item" |
| `DDD-dec-77.yaml:22` | N | "a reader needs no RDF to follow step 1" | Ruled |
| `DDD-dec-81.yaml:38` (resolution table) | R1 | Maturity: "Incubating when step 1 is reported" | Ruled |

## `releases/` and `CHANGELOG.md`

Released history. A cut release is never edited; these rows say what a reader meets, not what #88 would change.

| File:line | Says | What it says | Held by |
|---|---|---|---|
| `releases/v0.5.0.yaml:18, 36, 40, 42-44, 46` | 10, N, R1 | "with step 1 ruled for test"; "Only one of the ten steps is ruled, and it is ruled for test"; "Steps 2 to 10 are `[PROPOSED]`" | Ruled (release descriptor, cut) |
| `releases/v0.6.0.yaml:30` | — | "product-cli's step 1" (product-cli's order of work, not the method) | False positive |
| `releases/v0.7.0.yaml:18, 20, 35, 37-38, 41` | N | "Step 1b … a new step card"; "Its place after step 1"; "traces demand across step 1's act map" | Ruled (release descriptor, cut) |
| `CHANGELOG.md:7, 11-12, 15` | N | The v0.7.0 section, as above | Exposition, generated from the descriptor (`canon changelog`) |
| `CHANGELOG.md:67, 73, 75-77, 79` | 10, N, R1 | The v0.5.0 section, as above | Exposition, generated from the descriptor |

## Tooling

| File:line | Says | What it says | Held by |
|---|---|---|---|
| `.github/ISSUE_TEMPLATE/field-report.md:3-4, 11, 16-18, 24` | N | "You ran a method step"; title "Field report: step N on <kind of system>"; "how a step moves from projected to reported"; "Its register (Ruled, [PROPOSED], [OPEN]) is on the card" | Exposition (template). The one tool a practitioner meets that assumes numbered steps |
| `scripts/`, `tools/canon/src`, `.github/workflows/` | — | **Nothing.** No script, check or workflow reads a step number, the count of ten, a card file name or a step's register. `canon release` numbers its own steps (1 to 9), which are not method steps | — |
| `applications/pdlc/graph/check.py`, `shapes.ttl` | N | Listed under `applications/`: the only executable text that names a method step, and only "1b" in messages | Exposition |

## False positives, read and excluded

| Where | Why it is not a method step |
|---|---|
| `applications/sdlc/product-cli/product-definition.md:395, 459, 467, 484, 494, 536-538`; `releases/v0.6.0.yaml:30`; `CHANGELOG.md:52` | product-cli's own "order of work", steps 0 to 5 |
| `applications/sdlc/what.md:925`; `applications/sdlc/what/check.py:29` | The Product Framework's funnel; the checker's own steps |
| `spec/decision-provenance/dpp-1.md:411, 437, 464-465` | The `dpp/1` canonicalisation algorithm's steps |
| `tools/canon/DESIGN.md:289, 641, 678-679`; `tools/canon/src/Canon/Commands/ReleaseCommand.cs:65`; `Releases/TagPresence.cs:12`; `tests/Canon.Tests/ReleaseTests.cs` (10 lines) | `canon release`'s nine steps |
| `GOVERNANCE.md:93` | A landing step |
| `core/claims/DDD-flow-01.yaml:45`, `DDD-flow-02.yaml:44`, `DDD-flow-03.yaml:43, 55` | Steps of a derivation inside the claim |
| `core/decisions/DDD-dec-27.yaml:228`; `DDD-dec-64.yaml:15, 104`; `DDD-dec-87` to `-91`, line 9 | Track rungs; steps of a plan or a move |
| `meta/conversion-protocol.md:26`, `meta/corpus-test-results-2026-08-14.md:9`, `meta/ground-audit-2026-08-24.md:280`, `meta/history/migration-report.md` (7), `meta/history/migration/README.md:9`, `meta/holding-note-ground-axes-rev18.md` (3), `meta/successor-items-ground-audit.md:84`, `meta/vocabulary-delivery-session-2026-08-15.md:12` | Steps of a protocol, walk, kickoff or session plan |

## Findings

| # | Finding | Why it matters at G1 |
|---|---|---|
| F-1 | **"Start with north" is not a ruling.** #88's second reading supersedes "the wording of the ruling of 2026-11-18 that mapping starts with north". The record of that day, `meta/sessions/2026-11-18-pull-and-scope/rulings.md`, row E-2 (07:23), holds "we should start with North …" as **"Direction given … Not ruled"**. What was ruled that day is R-2 (08:50, 09:08): "scope must be the first else we cant place the pull". `DDD-dec-122` files R-2, not E-2. The order of the five parts on step 1's card rests on R-2 and `DDD-ground-05` | Question Q-2 asks what the 2026-11-19 ruling supersedes. If it is R-2's order, a filed ruling is superseded. If only E-2, nothing filed is |
| F-2 | **A claim's region says a pull is found at the edge first.** `DDD-address-09`'s region: "A pull is found at the edge first: what crosses into the scope and out of it". Its test names "the five-part procedure of step 1". Its statement ("placed by a trace back from the request that stops where the answer lies outside the scope") fits the 2026-11-19 order. The region and the test do not. The region's line is flagged in the claim's own notes (line 53) as Claude's unverified reading of 2026-11-18 E-4, a statement, not a ruling | #88 changes no claim's **statement**. A region or test is part of the claim file. Proposal P-9 says how this is carried without rewording |
| F-3 | **The one operative rule that counts ten steps is ruled.** `DDD-dec-82`'s statement: "It stays below 1.0 until all ten steps are ruled", and MINOR "when a step card is added or a step's register moves". With four moves, "all ten" names steps that no longer exist as steps | The version is in #88's deliverable 4. Its supersession needs a decision, and the question of what 1.0 means now is Emil's |
| F-4 | **Step 1's register "ruled for test" is held by two ruled texts.** `DDD-dec-74`'s resolution (as the state at the ruling) and `DDD-dec-122`'s resolution ("step 1 stays ruled for test"). Everything else that says it is exposition: `method/README.md`, the card, `README.md`, `quick-start.md`, and the released descriptor `v0.5.0` | Moving step 1 to `[PROPOSED]` is a register move. Under `DDD-dec-82` that is MINOR |
| F-5 | **Graph data names step 1b's parts.** `ontology.ttl:294, 329` and `shapes.ttl:338` carry "method step 1b, part 5/6" inside triples and a shape message | Out of scope by #80 and #88 (no lifecycle data changes). Named for deliverable 4 |
| F-6 | **The maturity property is tied to step 1.** `DDD-dec-81` and `GOVERNANCE.md:146`: "Incubating when step 1 is reported" | With no step 1, the trigger needs restating. Named for deliverable 4 |
| F-7 | **No tooling depends on the step numbers.** Only the field-report template assumes them | Changing `method/` breaks no check |
| F-8 | **`README.md:8` names v0.5.0 as the current preview**, while `v0.7.0` is tagged | Not #88's. Recorded for a draft issue |
