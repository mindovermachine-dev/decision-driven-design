# The How vocabulary — `sdlc:`

<!-- ddd:doc
reader: tool builders and authors of How decision records
act: write and read How decision records, vocabulary editions and readings in `dpp/1`, using the How's terms
pin: v5.15.2
basis: [DDD-dec-55, DDD-dec-56, DDD-dec-57, DDD-dec-58, DDD-dec-59, DDD-dec-60, DDD-dec-61, DDD-dec-62, DDD-dec-119, DDD-dec-52]
status: current
supersedes: 84aa466:applications/sdlc/how-vocabulary.md
-->

This is the vocabulary of [`how.md`](how.md): the terms a How decision record uses, the fact
terms its violation description reads, and where the What's and Writ's terms come in. Use it
when you write or read a How record, or build a tool that does.

**How settled this is.** Decided, with `how.md`, and ratified when the pull request that carried
both merged. One point is Claude's reading, not yet confirmed by Emil: the namespace IRI (below).

**Namespace.** `https://decision-driven-design.dk/ns/sdlc#`, prefix `sdlc:`. It sits beside
Writ's `https://decision-driven-design.dk/ns/writ#` (Writ ADR 0007). The host is the one Emil
operates for Writ's vocabulary. The path follows Writ's own reasoning: "`/ns/writ#` leaves room
for sibling vocabularies under one host". No IRI under `/ns/sdlc` is served or registered yet,
and the choice is Emil's *(Claude's reading, not yet confirmed by Emil)*.

**In records.** In a `dpp/1` record, How content goes in one hashed dotted member,
`dk.decision-driven-design.sdlc`. That is the namespace host reversed, per protocol §3.7: "names
SHOULD be reverse domain names under the operator's control". Fields the authority profile owns
go in `dk.decision-driven-design.authority`. That covers the violation description, which
belongs to the profile, and the stand-ins for genesis, grant and acceptance. The
How defines none of the authority fields. Hashed content is objects, arrays and strings only
(protocol A-6), so numbers and booleans never appear in these members.

**Three kinds of term.**

- **How terms**: decision-level, defined here.
- **Fact terms**: what violation descriptions read. They are defined here as a demand on Writ's
  code-facts page (`how.md` §9.4, D-1), not as a fact format.
- **What terms**: defined by the What, and read here (§3).

---

## 1. How terms

| Term | Definition | Record shape (`dpp/1`) |
|---|---|---|
| `sdlc:HowDecision` | A decision about how a product's What is realised in code or deployments. It has a kind, an anchor and, usually, a violation description | a record whose `…sdlc.record` is `"decision"`. `statement`, `by`, `at`, `why` and `basedOn` are as in the protocol |
| `sdlc:kind` | One of `constraint`, `binding`, `contract` | `…sdlc.kind` |
| `sdlc:Constraint` | A How decision whose violation description reads code facts alone | `…sdlc.kind: "constraint"` |
| `sdlc:Binding` | A How decision whose violation description joins What elements to the code or content that realises them through `sdlc:realises`, and so carries a coverage obligation. The word is used here and in Writ, whose Realisation contract becomes the Binding contract | `…sdlc.kind: "binding"`; `…sdlc.binds`: the What kind it ranges over |
| `sdlc:Contract` | A How decision over a deployable unit, read from reporter readings | `…sdlc.kind: "contract"`; `…sdlc.freshness`: an ISO 8601 duration string |
| `sdlc:anchor` | The one What element a decision anchors to: the narrowest covering element. Or, in an empty What, the product as space (`how.md` §3) | `…sdlc.anchor`: an IRI |
| `sdlc:binds` | For a binding, the What element kind its quantifier ranges over within the anchor | `…sdlc.binds`: a What term, e.g. `"sdlc:Decider"` |
| `sdlc:standards` | Interface standards a decision names. They are not targets | `…sdlc.standards`: array of strings |
| `sdlc:factSources` | Which provenance a decision's violation description requires, from Writ's set: `file`/`compiler` for projector facts, `deployment-declared` and/or `deployment-observed` for a contract | `…sdlc.factSources`: array of strings |
| violation description | Not a How term: the field the authority profile holds. The How requires it to be a SPARQL 1.1 `SELECT` with one row per violation (`?subject`, `?reason`). The evaluator may bind `?anchor` and `?target` | `…authority.violation`: `{language, binds, text}` |
| `sdlc:Target` | A vocabulary of shapes plus the fact source that reads them | named in vocabulary editions and target declarations: `…sdlc.target` |
| `sdlc:LanguageTarget` | A target read by a fact projector over a repository at a commit | `…sdlc.targetKind: "language"` |
| `sdlc:PlatformTarget` | A target read by a reporter over a deployable unit | `…sdlc.targetKind: "platform"` |
| `sdlc:DesignSystemTarget`, `sdlc:ContentStoreTarget` | Targets whose shapes (CIOs; strings per locale) are expressed in turn in a language target. The product's What declares them (this design system at this edition, these locales against this content store), as it declares iOS. Their catalogue is their vocabulary edition, in a package with its own genesis. AIO-to-CIO and key-to-string bindings anchor to the AIO or the content key | `…sdlc.targetKind: "design-system"` or `"content-store"`; `…sdlc.over`: the language target |
| `sdlc:VocabularyEdition` | A decision fixing, for one target at one edition, the native shape of each fact term, and the target's classifications (effects, jurisdictions) | `…sdlc.record: "vocabulary-edition"`, with `target`, `targetKind`, `edition`, `facts` (term → native shape), classification members, and `factSource` (`{kind, name, version, digest}` or `status`) |
| `sdlc:expressible` | A decision is expressible in a target iff the target's edition maps every fact term its violation description reads. Its shape there is derived from the edition and has no term of its own: "realisation" is not minted, in either repository | none: computed |
| `sdlc:TargetDeclaration` | A decision, anchored to a system, naming its language and deployment-platform targets, the repository, and the deployable unit that realises it. User-facing targets (platform contexts, design systems, content stores, locales) are declared by the What instead. Coverage ranges over both | `…sdlc.record: "target-declaration"`; `language`, `platform` (and design-system or content-store) objects, each naming its edition by reference |
| `sdlc:Exclusion` | A decision that an obligation does not apply to one (element, target) pair. A boundary gap | `…sdlc.record: "exclusion"`; `anchor` (the element), `binding` (a reference), `target`. The reason is `why` |
| baseline entry | Not a How term: the authority profile's. The How requires that it attach to (binding, element, target) and be added only by a decision. It marks a debt gap | `sdlc:BaselineEntry`, `{decision, subject, target}` on an acceptance ([`authority-vocabulary.md`](authority-vocabulary.md); authority.md §4.3) |
| waiver | Not a How term: the authority profile's. Never used for a coverage gap | `sdlc:Waiver` ([`authority-vocabulary.md`](authority-vocabulary.md); authority.md §4.4) |
| `sdlc:Coverage` | For each in-force binding, element of its kind within its anchor, and declared target: realised, baselined, or excluded | none: computed |
| `sdlc:Package` | "A product with an empty What, a genesis, and a decision log", vocabulary editions included. The kinds it binds to are references in its decisions' anchors | a system of `dpp/1` records |
| `sdlc:Release` | One version of a package: the set its holder accepts and ships together | `…sdlc.record: "release"`; `basedOn` every member, pinned; signed by the holder; supersedes the previous release |
| `sdlc:Import` | A decision in the importer's space, `basedOn` a package decision and its release, anchored in the importer's What. It may narrow the decision; it never alters it | `…sdlc.record: "import"`; `…sdlc.imports`: the reference; `why: {ref}` to the package decision |
| `sdlc:Fork` | A local decision `basedOn` a package decision that changes its statement or violation description | a How decision whose `basedOn` contains the package decision |
| `sdlc:Retention` | An importer's decision to keep resting on a superseded or withdrawn version, with its reason | `…sdlc.record: "retention"`, `basedOn` the withdrawal reading and the import |
| `sdlc:Withdrawal` | A package's declaration that a version is unsafe to rest on | a record superseding that version with `status: "withdrawn"` |
| `sdlc:Reading` | A recorded batch of facts with provenance: source, provenance from Writ's closed set (`file`, `compiler`, … , `deployment-declared`, `deployment-observed`), input, edition, subject, time read | a manifest entry (`how-examples/facts/manifest.json`). How Writ records it is a demand on Writ (`how.md` §9.4, D-3) |
| open question | Not a How term: one of Writ's three verdicts (clean, violation, open question). A contract with no reading of a required source within freshness has a **reported gap**, and its verdict is an open question with the absent reporter as one candidate (G8). It replaces the proposal's `sdlc:Unknown`, which is not minted | Writ's |
| `sdlc:Drift` | A difference between a unit's `deployment-declared` and `deployment-observed` facts | none: computed |
| `sdlc:Idle` | A How decision with neither a violation description nor a dependent. Reported, never a violation | none: computed |

## 2. Fact terms — a demand on Writ's code-facts page

Each fact term needs a mapping in every target edition that is used to evaluate a decision
reading it. `check.py` holds the same list.

| Term | Read by | Means |
|---|---|---|
| `sdlc:Component` | projector | a unit of code that can depend on another (a project; a workspace package) |
| `sdlc:inLayer` | projector | the layer name a component declares |
| `sdlc:dependsOn` | projector | a declared dependency between two components of one repository |
| `sdlc:CodeElement` | projector | a named declaration in code (a type; an exported function) |
| `sdlc:inComponent` | projector | the component whose sources contain an element |
| `sdlc:realises` | projector | the What element a code element declares that it realises. This is the binding correspondence, and Writ's "decision citations on code elements" read the other way |
| `sdlc:usesApi` | projector | an API a component references |
| `sdlc:handlesRoute`, `sdlc:method`, `sdlc:path` | projector | an HTTP route an element handles |
| `sdlc:DataStore` | reporter | a resource of a unit that holds data at rest |
| `sdlc:holdsPersonalData` | reporter | a store's declared personal-data classification |
| `sdlc:inRegion` | reporter | the region a resource is in |

**Derived by the gate from editions and in-force records, never read from code:**

- `sdlc:Effect` comes from an edition's `effects`.
- `sdlc:jurisdiction` comes from an edition's `jurisdictions`.
- `sdlc:inTarget` and `sdlc:ofSystem` come from the reading and its target declaration.
- `sdlc:ofUnit` comes from the reading's subject.
- `sdlc:target`, `sdlc:realisesSystem` and `sdlc:onPlatform` come from target declarations.

## 3. What terms — the What's, read here

`sdlc:Product`, `sdlc:Domain`, `sdlc:System`, `sdlc:Decider`, `sdlc:Command`,
`sdlc:QualityDemand`. Then `sdlc:within`, the ownership edge, used transitively as
`sdlc:within*`; and `sdlc:referencesDomain`. The AIO, context-of-use, content-key and locale
kinds that bindings into design-system and content-store targets range over are likewise the
What's. **None of these is defined here.** The How reads them. The What has moved, and they are
defined in its ontology ([`what/ontology.ttl`](what/ontology.ttl)); the worked example pins them
through a What-version. One provisional term is not carried by the What: `sdlc:localId`, which
the first REST binding read and which its successor replaced with the What's `sdlc:wireName`.

## 4. Mapping to Writ's vocabulary

Writ's vocabulary page is not written. Draft 2 is cited as Emil states it.

| How | Nearest `writ:` term (Writ definition, chapter 4) |
|---|---|
| constraint | evaluates over projector facts; the citation attributes the projector recognises (`[DesignDecision]`, `[Contract]`) are fact vocabulary, not a binding |
| binding | Writ's Binding contract (Writ adopts the word, and narrows the contract to kind 2: a What element to a shape in a target) |
| contract | none as a term. Its facts are reporter facts with provenance `deployment-declared` or `deployment-observed` (Writ Draft 2) |
| expressible | none. `writ:realisation` is never minted |
| vocabulary edition | none. Writ: "a second language is a second realisation, not a second ontology". Consistent with it |
| fact projector | Writ's Projector contract. Not the What's Projector (old §3.4), which is a read-model fold |
| reporter | Writ Draft 2's reporters, a reports partition per reporter (as Emil states it) |
| package | "a set of accepted decisions under this vocabulary" (Writ definition, chapter 5) |

## Not settled yet

- **The namespace IRI** *(Claude's reading, not yet confirmed by Emil)*. No IRI under
  `/ns/sdlc` is served or registered, and the choice is Emil's. Deciding it would fix the IRIs the
  terms above resolve to.

## Where this comes from

| Section | Rests on |
|---|---|
| Opening, register | with `how.md`: `DDD-dec-55` to `DDD-dec-61`, ruled in part on 2026-10-28 (binding as the word for kind 2 and in Writ; open question in place of unknown; `deployment-declared` and `deployment-observed` provenance, Round 2); the rest stood as proposed until the merge of PR #41 and is ratified by `DDD-dec-119` |
| Namespace | Writ ADR 0007; the IRI: formerly `UNVERIFIED — Emil review` |
| In records | `DDD-dec-62` (the token `dpp/1`); the violation description in the profile: `DDD-dec-52`; protocol §3.7, A-6 |
| §1 | binding: `DDD-dec-55` (2026-10-28); provenance values: `DDD-dec-60` (Round 2); design-system and content-store targets: `DDD-dec-57` (ruling 3); `expressible` and no "realisation": `DDD-dec-55`, `DDD-dec-57`; package: `DDD-dec-56`; open question replacing `sdlc:Unknown`: `DDD-dec-60`; import, fork, retention, withdrawal: `DDD-dec-59`; coverage, exclusion: `DDD-dec-58`; baseline and waiver: authority.md §4.3, §4.4 (2026-11-02) |
| §2 | `how.md` §9.4, D-1 |
| §3 | formerly "provisional, the move's", read from Product Framework v1.10.0 §3.0, §3.1, §3.2.5, §3.3, §3.2.0, §3.6 (old §9 `references_domain`); the What moved (`DDD-dec-41`, PR #42); `sdlc:wireName` and `REST@2`: `DDD-dec-64` P-1 |
| §4 | Writ definition, chapters 4 and 5; Round 2 of 2026-10-28 |

This text replaces `84aa466:applications/sdlc/how-vocabulary.md` in place. Its section numbers are
unchanged, because `how.md`, the authority vocabulary and the What's ontology cite this file.

