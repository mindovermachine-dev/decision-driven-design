# Equivalence — `applications/sdlc/how.md`

Old: `e5a332d:applications/sdlc/how.md` (700 lines). New: `applications/sdlc/how.md` (practitioner)
and `applications/sdlc/how-reference.md` (reference). Conventions:
[`../gate2-conventions.md`](../gate2-conventions.md). "New" sections are named by heading; "ref" is
`how-reference.md`.

## Opening (status, register, companions)

| # | Old: section and rule, in brief | New: document and section | Note |
|---|---|---|---|
| 1 | Status: ruled in part 2026-10-28; Emil ratifies by merging; sessions, decisions 55–61, 54 | how.md, "Where this comes from" (closing paragraph) | removed: history (opening) |
| 2 | "What was not ruled separately stays `[PROPOSED]` until the merge" | how.md, every *(not settled yet)* point and "Not settled yet" | same: points kept unsettled, not upgraded (the merge of PR #41 is not read as ruling them) |
| 3 | Register key (*Ruled*, `[PROPOSED]`, `[OPEN]`, `UNVERIFIED`) | how.md opening, "How settled this is" | removed: deliberation (register key replaced by words) |
| 4 | Companions: vocabulary, worked decisions with a checker | how.md first line (ref link); "The worked example" | same |

## §1.1 Scope and non-goals

| # | Old | New | Note |
|---|---|---|---|
| 5 | The How is the set of decisions that say how a product's What is realised in code and deployments | how.md, "What the How is"; ddd:doc `act` | same |
| 6 | This document fixes what a How decision is, what it may anchor to, how the gate holds it, how a vendor ships it, how another product imports it | how.md opening bullets and section order | same |
| 7 | Force (genesis, grants, scopes, acceptance, baseline, waiver) is the authority profile's | how.md, "What the How is", "Not in this document" row 1 | same |
| 8 | The gate's verbs, positions, partitions, guarantees are Writ's | same table, row 2 | same |
| 9 | Record, reference, resolver, hash law are the protocol's, token `dpp/1` | same table, row 3; ref, "Namespace and records" | same |
| 10 | The What's element kinds and identities are the moved What's | same table, row 4 | same |
| 11 | Execution (work units, Build seam, SPMC bundles, verdict events) retired, not carried | same table, row 5 | same |
| 12 | Delivery (features, releases, done, versions, direction, drift) retired | same table, row 6 | same |
| 13 | Generation out of scope | same table, row 7; "Generation" | same |
| 14 | Data conformance is an add-on outside the framework | same table, row 8 | same |

## §1.2 Preconditions

| # | Old | New | Note |
|---|---|---|---|
| 15 | Update: preconditions 1 and 2 discharged; provisional records superseded; precondition 3 stands | ref, "Demands on others" (the What: answered); how.md "How settled this is" (authority profile written separately) | removed: history, except the standing fact that the authority profile is not yet on `main` |
| 16 | Precondition 1: the What had not moved | — | removed: history (discharged) |
| 17 | Precondition 2: provisional IRIs accepted provisionally; test product only; never acceptable into a real product; superseded, never edited | — | removed: history (discharged; the supersession is recorded in `how-examples/README.md`, unchanged) |
| 18 | Precondition 3: authority profile not written; the How redefines none of its terms; demands on it in §9.4; examples use stand-ins | how.md, "How settled this is"; "What the How is" table row 1 ("redefines none of them"); ref, "Demands on others" | same |
| 19 | Precondition 4: Writ defined, not built; the definition is the authority, at Draft 2, with reporters and a closed provenance set plus the two deployment values; Draft 2 cited as Emil states it | how.md "How settled this is"; ref, "What the How needs from Writ" (Draft 2 as Emil states it) | same; "Claude has not read Draft 2" removed: history |
| 20 | Token paragraph: `decprov/1` superseded by `dpp/1`; records rebuilt; checker green | ref, "Demands on others" (token: answered); "Namespace and records" | removed: history, rule kept (`dpp/1`) |

## §2 The thesis, tested

| # | Old | New | Note |
|---|---|---|---|
| 21 | Thesis: the How is a set of decisions, each anchored, accepted under genesis, held by a gate, shipped as a package, imported by `basedOn` under the importer's genesis | how.md, "What the How is" | extracted from deliberation |
| 22 | Verdict on the thesis; table of clauses and repairs; "examples exercise every clause except vendor distribution" | — | removed: deliberation (§2). Each repair's rule is carried where it lands (rows 23–28) |
| 23 | Everything that varies by target lives in vocabulary editions, which are decisions, so the set is closed | how.md, "Specified once…"; "Packages" table row 2 | extracted from deliberation |
| 24 | Anchor reading (product node is an element; narrowest covering element) | how.md, "Anchoring" 1–4 | same (ruled in §3; the §2 `UNVERIFIED` superseded by §3's ruling) |
| 25 | Deployment provenance: Draft 2 has reporters; `deployment-declared` and `deployment-observed` added | how.md, "Which facts the gate may use"; ref, "Recorded readings" | same |
| 26 | A package's What is empty; `DDD-dec-46` clause superseded | how.md, "Packages" | same |
| 27 | An import is a decision in the importer's space with its own anchor | how.md, "Importing a package" part 2 | same |
| 28 | Kind 2 is "binding"; Writ adopts the word; its Realisation contract becomes the Binding contract; `writ:realisation` never minted; "realisation" used as a term nowhere | ref, How terms `sdlc:Binding`, `sdlc:expressible`; ref, Writ mapping | extracted from deliberation |
| 29 | A decision's shape in a target is derived and needs no name; whether it can be checked is "expressible" | how.md, "Specified once…"; ref, `sdlc:expressible` | extracted from deliberation |
| 30 | `DDD-dec-46`'s realisation scope is left as ruled | how.md, "Where this comes from" (`DDD-dec-46` cited) | could not restate: the sentence protects a ruled term from the renaming; the practitioner text uses "realisation" only in its ordinary sense and does not mention the scope. Left to `DDD-dec-46` |
| 31 | "Writ narrows, the How does not widen": Writ's Binding contract is kind 2 only; constraint has no binding, evaluates over projector facts; citation attributes are fact vocabulary; contract has no binding, evaluates over reporter facts; mapping constraint → projector facts, binding → Binding contract, contract → reporter facts | ref, "Mapping to Writ's vocabulary" and the sentence after it | extracted from deliberation |

## §3 Anchoring

| # | Old | New | Note |
|---|---|---|---|
| 32 | A How decision anchors to exactly one What element or to the product; the product is the degenerate case an empty What forces | how.md, "Anchoring", lead and 2 | same |
| 33 | "Every Decider in Ordering" anchors to the domain; "every Decider" to the product; the product anchor is the loophole only when a narrower element exists and was not used; the checker warns | how.md, "Anchoring" 3–4 | same |
| 34 | 1. The product node is a What element (root of the What) | "Anchoring" 1 | same |
| 35 | 2. The product as space is the degenerate case: only when the What is empty (repository with no What, or a package) | "Anchoring" 2 | same |
| 36 | 3. Anchor to the narrowest element whose subtree contains everything governed; examples; wider is a finding | "Anchoring" 3–4 | same |
| 37 | 3. The checker warns when the narrowest covering element *today* is narrower than the anchor | "Anchoring" 4 | same |
| 38 | 3. Covering per kind: binding → narrowest common container of instances; constraint over code → code of declared systems within the anchor; contract anchors to the element it realises, not checked | "Anchoring" 5 | same ("realises" → "holds", to avoid "realise" for a contract's relation to a demand; meaning unchanged) |
| 39 | 3. The warning reads present instances only; a product-wide "every Decider" with all Deciders in one domain warns though legitimate; advisory; examples' self-test shows it | "Anchoring" 4; example paragraph | same |
| 40 | 4. Quantifiers range within the anchor; evaluator binds `?anchor`; one text serves any anchor | "Anchoring" 6; ref, "Violation descriptions" | same |
| 41 | 5. Creating decisions: for the How the question does not arise, because How decisions create no What elements | "Anchoring" 7 | same (the old heading "A creating decision anchors to the element it creates" is not carried: its body says the question does not arise for the How) |
| 42 | An empty-What product can adopt every constraint and contract; bindings vacuous; Writ's reference customer (Context& package over Varve) is that case | "Anchoring", paragraph after the list | same |

## §4.1 What every How decision is

| # | Old | New | Note |
|---|---|---|---|
| 43 | A How decision is a `dpp/1` record | how.md, "A How decision"; ref, How terms | same |
| 44 | It carries a kind | "A How decision" bullet 1 | same |
| 45 | It carries an anchor per §3 | bullet 2 | same |
| 46 | It carries a violation description, the field placed in the authority profile; a SPARQL 1.1 `SELECT`, one row per violation with `?subject` and `?reason`; evaluator may bind `?anchor` and `?target`; Writ's form; not a new rule language | "A How decision" bullet 3 (summary); ref, "Violation descriptions" (full) | moved to reference |
| 47 | It carries the provenance it requires: for a contract, declared, observed, or both; constraints and bindings read projector facts (`file`, `compiler`) | "A How decision" bullet 4; ref, `sdlc:factSources` | same |
| 48 | A verdict is computed from the decision in force and the facts at a position; never stored; what is recorded is the decision and the readings | "A How decision", paragraph after list | same |

## §4.2 The three kinds

| # | Old | New | Note |
|---|---|---|---|
| 49 | Kinds table: is over / typical anchors / facts / evaluator / gates `land` / worked | how.md, "The three kinds" table | same. "Facts" and "evaluator" rows merged into "Reads"; the evaluator detail is in ref |
| 50 | Contract gates `land` only via `deployment-declared` facts; an observed fact is not of the change | table row "Can block…"; "What the gate checks" | same; kept *(not settled yet)* per §13 item 1 |
| 51 | Contract with no fresh reading: reported gap, open question | "When a reporter is absent" | same |
| 52 | Constraint: the layout model is a set of constraints over path facts; each rule kind (`must-exist`, `may-exist-here`, `must-co-exist`, `must-not-exist`) is a violation description | "The three kinds", Constraint | same (rule-kind names given in words) |
| 53 | No orphans reads decisions in force at p as well as facts; a file or component no allow decision covers is a violation; "everything not covered is a violation until a decision covers it" | Constraint, second paragraph | same; *(not settled yet)* per Appendix A (H-8 not ruled separately) |
| 54 | No-orphans is the mirror of binding coverage | "Coverage and gaps", "The other direction" | same |
| 55 | Guard 1 (every rule cites the principle it protects) is the protocol's `why` plus `basedOn`; Guard 2 (prefer the allowlist) stays advice | Constraint, second paragraph | same |
| 56 | Binding needs a correspondence between What identities and code elements: the fact `sdlc:realises`, mapped per edition (`[Realises(…)]`, `@realises`) | Binding paragraph; ref, fact terms | same |
| 57 | Writ's "decision citations on code elements" are the same fact read the other way | ref, fact terms, `sdlc:realises` | moved to reference |
| 58 | A binding is the only kind whose evaluator reads the What graph | Binding paragraph | same |
| 59 | Bindings absorb pure core, the canonical REST projection, reification, content resolution, and the split between system identity and deployment identity (shared with contract: binding says which unit realises a system; contract says what the unit must satisfy) | Binding bullet list | same |
| 60 | Old §5.2 does not go here; it is generation | "Generation" | same |
| 61 | Contract is over a deployable unit; its identity (domain name, bundle identifier, account, region) is How | Contract paragraph | same |
| 62 | Kind-2 architectural demands are What elements; the contract that holds one anchors to it | Contract paragraph | same |
| 63 | Kind-1 runtime bounds are What elements; which telemetry measures them is a contract over `telemetry` facts anchored to the bound | Contract paragraph | same; kept *(not settled yet)* per §13 item 1 |

## §4.3 A fourth kind? No

| # | Old | New | Note |
|---|---|---|---|
| 64 | Principle is not a kind: a decision with no violation description that others rest on; gate evaluates nothing for it | "The three kinds", "Principles are not a fourth kind" | same; *(not settled yet)* |
| 65 | `explain` shows it in every derivation that rests on it; when superseded, everything resting on it shows "rests on superseded version" | same paragraph | same |
| 66 | Adding a kind would give the gate a category with no evaluator | "Not settled yet", first entry | removed: deliberation (reason), kept as the consequence in the open-point entry |
| 67 | Earn-their-place carries over as a report: a decision with neither violation description nor dependent is idle; `check` lists it; idle is not wrong; a principle may be recorded before anything rests on it | "Idle decisions are reported, not rejected"; ref, `sdlc:Idle` | same; *(not settled yet)* |
| 68 | Two record types beside the kinds, neither a kind: target declarations (which targets, which unit; set what coverage ranges over); exclusions (obligation does not apply to an (element, target) pair, with reason) | "Two record types sit beside the kinds"; ref, How terms | same; *(not settled yet)* |

## §4.4 Should any kind split? No

| # | Old | New | Note |
|---|---|---|---|
| 69 | Binding into a language and into a design system/content store: same evaluator and coverage rule; differ only in which edition names the shape; one kind | "No kind splits" bullet 1 | same; *(not settled yet)* |
| 70 | Contract declared and observed are one kind; violation description says which provenance it requires; residency may use declared; "no public endpoint" needs observed; a rule needing both is one decision over two provenances, two verdicts apart | bullet 2 | same; *(not settled yet)* |
| 71 | Constraint and contract kept apart: an absent fact means different things (projector gap reported, commit decidable; missing contract reading → open question); they differ in what they can gate | bullet 3 | same; *(not settled yet)* |

## §5.1 What a target is

| # | Old | New | Note |
|---|---|---|---|
| 72 | A target is a vocabulary of shapes plus the fact source that reads them; three sorts: language (projector over repository at commit), platform (reporter over unit), design system/content store layering over a language | how.md, "Targets"; ref, target terms | same |
| 73 | Design systems and content stores are targets, not catalogues; the What declares them; catalogue is the target's vocabulary edition in a package with its own genesis, typically a design team's; AIO-to-CIO and key-to-string decisions are kind 2 anchored to the AIO or key; nothing in a catalogue is a What element | "Targets", bullet list | same |
| 74 | Targets declared in two places: the What (platform contexts, design systems, content stores, locales); How target declarations (languages, deployment platforms); coverage ranges over both | "Targets", paragraph | same |
| 75 | `[PROPOSED]`, not ruled separately: the rest of this section and §5.2 | "An interface standard is not a target" *(not settled yet)*; "Specified once" *(not settled yet, as a whole)* | same |
| 76 | An interface standard (HTTP, OpenAPI, AsyncAPI, CloudEvents) is not a target; a decision may name it; choosing one standard is a different decision; the old "use the standards" table survives as advice | "An interface standard is not a target" | same; *(not settled yet)* |

## §5.2 Specified once, realised per target

| # | Old | New | Note |
|---|---|---|---|
| 77 | A decision's statement and violation description use only How terms, What terms, interface standards, and one design-system/content-store target's terms | "Specified once…" list; ref, "Violation descriptions" | same; *(not settled yet)* |
| 78 | A decision never names a language or platform term; per-target shape lives in the target's vocabulary edition, a decision record | "Specified once…" | same |
| 79 | The edition maps each fact term to its native shape and carries target-specific classifications (effects; jurisdictions) | "Specified once…"; ref, `sdlc:VocabularyEdition` | same |
| 80 | A decision's shape in a target is derived, never authored: the composition of the edition's mappings for the fact terms it reads | "Specified once…" | same |
| 81 | Expressible iff the edition maps every fact term the decision reads; the checker computes it | "Specified once…"; ref, `sdlc:expressible` | same |
| 82 | Adding a second language is adding an edition; no decision is touched | "Specified once…" | same |
| 83 | Table of the three checks in C# and TypeScript, decision text untouched | "Specified once…", *In Acme Shop* table | same |
| 84 | Where it fails: a target whose facts cannot be stated in the How's fact terms; repair is a new fact term, a decision in this repository, not a change to any product's decisions | "Where this breaks" | same |
| 85 | Fact terms are a demand on Writ's unwritten code-facts page; the How states the facts it reads, not a competing fact format | "Where this breaks"; ref, fact terms heading and "Demands on others" | same |
| 86 | Purity is approximate: `PURE` checks the component for effects, not decide/evolve; behavioural conformance needs runner facts against the Decider's scenarios; Writ's Draft 2 has `runner`; worked decisions do not use it | "Purity is approximate in the example" | same |

## §6 The package

| # | Old | New | Note |
|---|---|---|---|
| 87 | A package is a product with its own genesis held by the vendor; in another product's space it is provenance, never authority | how.md, "Packages" lead | same |
| 88 | A package contains decision records and nothing else (table: kinds; vocabulary editions as decisions; projector/reporter editions named inside editions, name/version/digest, name content, binary not; release record `basedOn` everything, signed; analyzers etc. not content, referenced by digest) | "Packages" table | same |
| 89 | This tightens the proposal (vocabularies and editions are decisions or named inside decisions) | — | removed: deliberation |
| 90 | A package is one thing: a decision log another product can walk | "Packages", after the table | same |
| 91 | A package carries no What: kinds are framework vocabulary referenced by name; a What of kinds per package would be a private copy of the ontology; its decisions anchor to the package product | "A package has no What" | same; the private-copy reason removed: deliberation |
| 92 | `DDD-dec-46`'s "its What is its decisions" is superseded by `DDD-dec-56`; `DDD-dec-42` stands; "a product with an empty What, a genesis, and a decision log"; includes vocabulary editions | "A package has no What"; ref, `sdlc:Package`; "Where this comes from" | same |
| 93 | A package needing a What kind the framework lacks cannot ship it; a new kind is a framework change; an instance of a new kind is a What element in the importer | "Packages", last paragraph | same |
| 94 | `[OPEN]`: whether adopters may register AIOs | "Packages", last paragraph; "Not settled yet" | same; *(not settled yet)* |

## §7 Import and supersession

| # | Old | New | Note |
|---|---|---|---|
| 95 | A package's decisions enter by import, `basedOn` the package's versions, in force only under the importer's acceptances | "Importing a package", lead | same |
| 96 | `[PROPOSED]` An import has three parts | "An import has three parts *(not settled yet…)*"; "Not settled yet" | same (see report: `DDD-dec-59`'s statement names the same three parts) |
| 97 | Landing: records pinned into the importer's log; a copy is not the record; the pin is how the importer knows it holds what the vendor signed; a gate reading the vendor's system at check time would break G1 | part 1; ref, Writ table note on G1 | same |
| 98 | Import decision: in the importer's system; `basedOn` package decision and release, pinned; `why` is a ref to the package decision; its own anchor | part 2; ref, `sdlc:Import` | same |
| 99 | An import may narrow (anchor lower), never alter; altering is a local decision `basedOn` the package's, a fork | "An import may narrow…"; ref, `sdlc:Fork` | same; *(not settled yet)* |
| 100 | Acceptance under the importer's genesis chain; until then proposed, nothing in force | part 3 | same |
| 101 | Example: `IMP-pure@1` proposed by an agent, in force only because a human How-grant holder accepted it (`ACC-1@1`) | *In Acme Shop* paragraph | same, example restated against the landed version 2 records (`IMP-pure@2`, `ACC-1@2`), checked against the record files |
| 102 | Supersession: nothing in the importer changes; in force under its own acceptance on the pinned version; `explain` shows "rests on superseded version"; re-import is new landing + new import decision superseding the old + new acceptance | "When the vendor supersedes a decision" | same |
| 103 | Condition: no forward link in the protocol; the importer learns only by reading the versions listing; that reading must be recorded; `explain` shows supersession as of the last recorded reading, never live; the examples' checker reads the listing directly (a checker, not a gate) | same section, second paragraph | same; *(not settled yet)*. "The examples' checker reads the listing directly" removed: example detail, in `how-examples/README.md` |
| 104 | Withdrawal: a package may declare a version withdrawn by a superseding record with `status: withdrawn` (hashed, so a new version); the only signal ever more than information; never acts by the vendor's authority | "When the vendor withdraws a version"; ref, `sdlc:Withdrawal` | same |
| 105 | Once a withdrawal reading is recorded, every importer decision on it is an open answer at every `check` until a re-import or retention is accepted; a product with an open answer cannot claim its How is specified | withdrawal, "What it obliges" | same |
| 106 | It does not fail `land` and does not take the import out of force; either would be authority from the package | "What it does not do" | same |
| 107 | Teeth if wanted: the importer can adopt a decision that withdrawals from this vendor block `land`; the importer's authority | "If you want it to block" | same |

## §8 Coverage and gaps

| # | Old | New | Note |
|---|---|---|---|
| 108 | `[PROPOSED]` generalised obligation: every binding in force × element of its kind in its anchor × declared target; exactly one of realised / debt (baseline entry) / boundary (exclusion); gate reports which | "Every bound element, in every target"; "Not settled yet" | same; *(not settled yet)* (see report: `DDD-dec-58`'s statement states the same rule) |
| 109 | Targets come from target declarations, so coverage is computed and never listed by hand | same section | same ("and from the What" added, as §5.1 already says coverage ranges over both) |
| 110 | Old §4.5 and §4.6 coverage are instances, as `DDD-dec-45` ruled them into the What as obligations | same section | same |
| 111 | `PURE@1` and `REST@1` show it; their "no code element realises it in this target" rows are the uncovered pairs | same section, *In Acme Shop*; ref, "Violation descriptions" | same |
| 112 | Two different things: debt is a baseline entry per (element, target), reported baselined, shrinks (removed by landing the realising code; added only by a decision); boundary is an exclusion decision anchored to the element with reason, reported not applicable, no ratchet | "Debt and boundaries are different things" table | same |
| 113 | Never a waiver: a waiver suspends a violation that applies; an unreifiable pair is not one; using a waiver would let waivers stand in for boundaries | "A waiver never covers a gap" | same |
| 114 | `UNVERIFIED`: ratchet semantics of baseline assumed, profile not written | same paragraph; "Not settled yet" | same; *(not settled yet)* |
| 115 | An exclusion is a decision with a principal; a baseline entry is added by a decision but is a member of the baseline, not a decision of its own | "Debt and boundaries…", last paragraph | same |
| 116 | The other direction: no-orphans asks whether every piece of code is covered by a decision; the old §14.5 symmetry; the How has it at both ends | "The other direction" | same; *(not settled yet)* (H-8); the §14.5 cross-reference removed: history |

## §9 Facts, provenance, and what the gate enforces

| # | Old | New | Note |
|---|---|---|---|
| 117 | The gate is Writ; the How does not restate its verbs, positions, partitions or guarantees | how.md, "What the gate checks" lead; ref, "What the How needs from Writ" | same |
| 118 | Table: How requirement → Writ guarantee (G2, G2 importer-only, G3, `land` condition 3, G7, three verdicts, G8, G1/G7) | how.md table in plain words; ref, the same table with Writ's guarantee names | same; guarantee names moved to reference |
| 119 | Only facts recorded with provenance from Writ's closed G8 set (`file, compiler, graph, runner, data, telemetry, attestation`), plus `deployment-declared` and `deployment-observed` | "Which facts the gate may use"; ref, "Recorded readings" | same |
| 120 | "Two provenance values, not two inputs"; carrying the split as two inputs "would hide it where it matters, in the verdict" | same | same |
| 121 | A contract's violation description says which value it requires | same | same |
| 122 | Reading fields table (source, provenance, input, edition, subject, read at, by/attributed to) | ref, "Recorded readings" | moved to reference |
| 123 | `facts/manifest.json` has this shape; its `provenance` is Writ's value | ref, "Recorded readings" | moved to reference |
| 124 | A fact with no provenance is not usable; a reporter's own claim is not a fact until recorded with provenance | how.md "Which facts…"; ref, "Recorded readings" | same |
| 125 | Absent reporter: fact no reporter could supply is a reported gap; verdict needing it is an open question with the absent reporter as candidate (G8) | "When a reporter is absent" | same |
| 126 | A contract names its fact sources and a freshness bound (`RESID@1`: both, within `P1D`) | same; ref, `sdlc:Contract` (`freshness`) | same |
| 127 | Fresh reading → violation description runs, clean or violation; none/stale → gap reported, open question, absent reporter named; not a pass, not a violation; encode/verify: ground you do not control verified on a schedule, unreachable never a pass | same | same; the `apparatus/encode-verify.md` reference moved to "Where this comes from" |
| 128 | An open question can block; what it blocks is Writ's to define | same | same |
| 129 | Declared/observed disagreement for one unit is drift, not a third verdict; each provenance has its own verdict | same | same |
| 130 | §9.4 demands D-1 to D-8 | ref, "Demands on others, not resolved here" | moved to reference; D-labels removed; D-8 marked answered per §1.2's update |

## §10 Generation

| # | Old | New | Note |
|---|---|---|---|
| 131 | Out of scope; Writ records generation as open, decided by evidence, after its 1.0; old realisation declarations and code-generation seam not carried | how.md, "Generation" | same |
| 132 | Condition: an edition's mapping is what a generator would read (dual-read); nothing may make an edition check-only | same | same |
| 133 | A generator reading editions changes code; code changes go through `land`; it does not change the How; tools never change it | same | same |

## §11 Conformance

| # | Old | New | Note |
|---|---|---|---|
| 134 | `[PROPOSED]` one level, matching the What's: specified and in force, at a stated position | how.md, "Conformance" | same; *(not settled yet)* |
| 135 | Conditions 1–6 | same, list 1–6 | same |
| 136 | It does not claim the code satisfies the How; satisfaction is a verdict, computed, never stored; a red `check` can coexist with a specified How | same, last paragraph | same |
| 137 | Old conformance levels 2–4 went with the How and Delivery, not revived | — | removed: history |

## §12 The worked decisions

| # | Old | New | Note |
|---|---|---|---|
| 138 | One decision per kind plus REST; written once, imported, anchored, evaluated in two targets, accepted under a test genesis by a delegated human | how.md, "The worked example" | same |
| 139 | The checker verifies pins, signatures, authority links, wide anchors, expressibility, supersession; records conformant under the reference implementation unmodified | same | same (conformance detail stays in `how-examples/README.md`) |
| 140 | Violation descriptions run over hand-written facts; no projector or reporter exists; verdicts analytic, planted, predicted, fired; show only that descriptions execute | same | same |
| 141 | Table of kinds, anchors (`acme:product`, `acme:domain-ordering`, `acme:qd-residency-eu`), targets, planted verdicts | same table | same, anchors restated against the landed records: product; the Ordering bounded context; the demand "personal data resides in the EU" (`IMP-*@2`, checked against the record files) |

## §13 Open, for Emil

| # | Old | New | Note |
|---|---|---|---|
| 142 | Closed by the 2026-10-28 rulings: anchor reading, package's What, catalogue, provisional anchoring, binding in Writ, deployment provenance, token | — | removed: deliberation |
| 143 | Not ruled separately, stand as proposed: three kinds/no fourth/no split/idle/record types; shapes from editions/standards not targets; recorded-reading condition/narrow-never-alter; Kind-1 wiring/`deployment-declared` gating `land` | how.md, "Not settled yet" | same |
| 144 | `[OPEN]` whether adopters may register What kinds | "Not settled yet" | same |

## Appendix A and Appendix B

| # | Old | New | Note |
|---|---|---|---|
| 145 | Appendix A: every departure from the proposal (H-1 to H-17), their reasons and the rulings on the appendix | — | removed: deliberation. Each H-item's resulting rule is carried in the rows above |
| 146 | Appendix A, rulings: "Not ruled separately: H-3, H-8, H-9, H-11, H-12, H-13, H-17" | how.md *(not settled yet)* points: specified once (H-3); runtime bounds (H-9); recorded reading (H-11); narrow, never alter (H-12); idle (H-13); record types (H-17) | same, including H-8 (no orphans as coverage of code), marked *(not settled yet)* in the Constraint paragraph and "The other direction" |
| 147 | Appendix B: where the old §§4–7 went | — | removed: history |

## Counts

| Note | Rows |
|---|---|
| same | 123 |
| moved to reference | 5 |
| extracted from deliberation | 5 |
| removed: deliberation | 6 |
| removed: history | 7 |
| could not restate | 1 |
| **Total** | **147** |

Rows with a compound note are counted by their first note.
