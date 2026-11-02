# Equivalence — `applications/sdlc/how-vocabulary.md`

Old: `e5a332d:applications/sdlc/how-vocabulary.md` (113 lines), removed. New: merged into
`applications/sdlc/how-reference.md` ("ref"). Conventions:
[`../gate2-conventions.md`](../gate2-conventions.md).

| # | Old: section and rule, in brief | New: document and section | Note |
|---|---|---|---|
| 1 | Status line: with how.md, decisions 55–61, ruled in part 2026-10-28, which items were ruled, "the rest stands as proposed until the merge" | ref, "How settled this is"; *(not settled yet)* marks on the unruled terms | removed: history; unruled points kept unsettled |
| 2 | Namespace `https://decision-driven-design.dk/ns/sdlc#`, prefix `sdlc:`, beside Writ's `…/ns/writ#` (Writ ADR 0007); the host Emil operates; path follows Writ's reasoning | ref, "Namespace and records" | same (ADR 0007 moved to "Where this comes from") |
| 3 | `UNVERIFIED`: no IRI under `/ns/sdlc` served or registered; the choice is Emil's | ref, "Namespace and records" and "Not settled yet" | same; *(not settled yet)* |
| 4 | How content in one hashed dotted member `dk.decision-driven-design.sdlc`; reverse domain per protocol §3.7 | ref, "Namespace and records" | same |
| 5 | Authority-profile fields in `dk.decision-driven-design.authority`: the violation description and the stand-ins for genesis, grant, acceptance; the How defines none of them | ref, "Namespace and records" | same |
| 6 | Hashed content is objects, arrays and strings only (protocol A-6); no numbers or booleans | ref, "Namespace and records" | same |
| 7 | Three kinds of term: How terms (defined here); fact terms (a demand on Writ's code-facts page, not a fact format); What terms (provisional, read from PF v1.10.0 §3, owned by the move) | ref, "Three kinds of term" | same; "provisional … owned by the move" removed: history (the What has landed) |
| 8 | §1 `sdlc:HowDecision` | ref, How terms | same |
| 9 | §1 `sdlc:kind` | ref, How terms | same |
| 10 | §1 `sdlc:Constraint` | ref, How terms | same |
| 11 | §1 `sdlc:Binding`, with "*Ruled* (2026-10-28): the word, here and in Writ…" | ref, How terms | same (ruling tag removed) |
| 12 | §1 `sdlc:Contract` with `freshness` | ref, How terms | same |
| 13 | §1 `sdlc:anchor` (`how.md` §3) | ref, How terms (link to how.md "Anchoring") | same |
| 14 | §1 `sdlc:binds` | ref, How terms | same |
| 15 | §1 `sdlc:standards` | ref, How terms | same |
| 16 | §1 `sdlc:factSources` (ruled 2026-10-28, Round 2) | ref, How terms | same (ruling tag removed) |
| 17 | §1 violation description: not a How term; the profile's field; SPARQL 1.1 `SELECT`, `?subject`, `?reason`; `?anchor`, `?target` | ref, How terms; "Violation descriptions" | same |
| 18 | §1 `sdlc:Target` | ref, How terms | same |
| 19 | §1 `sdlc:LanguageTarget` | ref, How terms | same |
| 20 | §1 `sdlc:PlatformTarget` | ref, How terms | same |
| 21 | §1 `sdlc:DesignSystemTarget`, `sdlc:ContentStoreTarget` (*Ruled*, ruling 3) | ref, How terms | same (ruling tag removed) |
| 22 | §1 `sdlc:VocabularyEdition` | ref, How terms | same |
| 23 | §1 `sdlc:expressible`; "realisation" not minted in either repository (ruled 2026-10-28) | ref, How terms | same |
| 24 | §1 `sdlc:TargetDeclaration` (ruling 3) | ref, How terms | same |
| 25 | §1 `sdlc:Exclusion` | ref, How terms | same |
| 26 | §1 baseline entry: the profile's; attaches to (binding, element, target), added only by a decision; marks debt (`how.md` D-6) | ref, How terms | same (D-6 label removed) |
| 27 | §1 waiver: the profile's; never for a coverage gap | ref, How terms | same |
| 28 | §1 `sdlc:Coverage` | ref, How terms | same |
| 29 | §1 `sdlc:Package` (*Ruled*) | ref, How terms | same |
| 30 | §1 `sdlc:Release` | ref, How terms | same |
| 31 | §1 `sdlc:Import`: may narrow, never alter | ref, How terms | same; *(not settled yet)* for narrow-never-alter, per how.md §13 |
| 32 | §1 `sdlc:Fork` | ref, How terms | same |
| 33 | §1 `sdlc:Retention` | ref, How terms | same |
| 34 | §1 `sdlc:Withdrawal` | ref, How terms | same ("the status is hashed, so this is a new version" added from how.md §7.3) |
| 35 | §1 `sdlc:Reading`; how Writ records it is a demand on Writ (D-3) | ref, How terms | same (D-3 label removed) |
| 36 | §1 open question: Writ's verdict; reported gap; candidate absent reporter (G8); replaces `sdlc:Unknown`, not minted | ref, How terms | same |
| 37 | §1 `sdlc:Drift` | ref, How terms | same |
| 38 | §1 `sdlc:Idle` | ref, How terms | same; *(not settled yet)*, per how.md §13 |
| 39 | §2 heading: fact terms are a demand on Writ's code-facts page | ref, "Fact terms — what the How needs from the code-facts format" | same |
| 40 | §2 each fact term needs a mapping in every target edition used to evaluate a decision reading it; `check.py` holds the same list | ref, "Fact terms" | same |
| 41 | §2 fact terms table (11 rows) | ref, "Fact terms" table | same |
| 42 | §2 derived by the gate from editions and in-force records (`Effect`, `jurisdiction`, `inTarget`, `ofSystem`, `ofUnit`, `target`, `realisesSystem`, `onPlatform`) | ref, "Derived by the gate…" | same |
| 43 | §3 What terms: list; "None of these is defined here. The How reads them" | ref, "What terms the How reads" | same |
| 44 | §3 "provisional, the move's … when the move lands they become pinned references"; PF section numbers; `references_domain` | — | removed: history (the move has landed; see report on `sdlc:localId`) |
| 45 | §4 heading: Writ's page is not written; Draft 2 cited as Emil states it | ref, "Mapping to Writ's vocabulary" lead | same |
| 46 | §4 mapping table (8 rows) | ref, "Mapping to Writ's vocabulary" | same |

## Counts

| Note | Rows |
|---|---|
| same | 44 |
| removed: history | 2 |
| **Total** | **46** |

Rows with a compound note are counted by their first note.
