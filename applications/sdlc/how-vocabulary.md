# The How vocabulary — `sdlc:`

**Status: `[PROPOSED]`**, with [`how.md`](how.md) (`DDD-dec-55` to `DDD-dec-61`, unruled).

**Namespace.** `https://decision-driven-design.dk/ns/sdlc#`, prefix `sdlc:`. It sits beside
Writ's `https://decision-driven-design.dk/ns/writ#` (Writ ADR 0007). The host is the one Emil
operates for Writ's vocabulary. The path follows Writ's own reasoning: "`/ns/writ#` leaves room
for sibling vocabularies under one host". `UNVERIFIED — Emil review`: no IRI under `/ns/sdlc` is
served or registered yet, and the choice is Emil's.

**In records.** In a `decprov/1` record, How content goes in one hashed dotted member,
`dk.decision-driven-design.sdlc`. That is the namespace host reversed, per protocol §3.7: "names
SHOULD be reverse domain names under the operator's control". Fields the authority profile owns
go in `dk.decision-driven-design.authority`. That covers the violation description, which
`DDD-dec-52` places in the profile, and the stand-ins for genesis, grant and acceptance. The
How defines none of the authority fields. Hashed content is objects, arrays and strings only
(protocol A-6), so numbers and booleans never appear in these members.

**Three kinds of term.**

- **How terms**: decision-level, defined here.
- **Fact terms**: what violation descriptions read. They are defined here as a demand on Writ's
  code-facts page (`how.md` §9.4, D-1), not as a fact format.
- **What terms**: provisional. They are read from Product Framework v1.10.0 §3 and owned by the
  move (`how.md` §1.2).

---

## 1. How terms

| Term | Definition | Record shape (`decprov/1`) |
|---|---|---|
| `sdlc:HowDecision` | A decision about how a product's What is realised in code or deployments. It has a kind, an anchor and, usually, a violation description | a record whose `…sdlc.record` is `"decision"`. `statement`, `by`, `at`, `why` and `basedOn` are as in the protocol |
| `sdlc:kind` | One of `constraint`, `binding`, `contract` | `…sdlc.kind` |
| `sdlc:Constraint` | A How decision whose violation description reads code facts alone | `…sdlc.kind: "constraint"` |
| `sdlc:Binding` | A How decision whose violation description joins What elements to the code or content that realises them through `sdlc:realises`, and so carries a coverage obligation | `…sdlc.kind: "binding"`; `…sdlc.binds`: the What kind it ranges over |
| `sdlc:Contract` | A How decision over a deployable unit, read from reporter readings | `…sdlc.kind: "contract"`; `…sdlc.freshness`: an ISO 8601 duration string |
| `sdlc:anchor` | The one What element a decision anchors to: the narrowest covering element. Or, in an empty What, the product as space (`how.md` §3) | `…sdlc.anchor`: an IRI |
| `sdlc:binds` | For a binding, the What element kind its quantifier ranges over within the anchor | `…sdlc.binds`: a What term, e.g. `"sdlc:Decider"` |
| `sdlc:standards` | Interface standards a decision names. They are not targets | `…sdlc.standards`: array of strings |
| `sdlc:factSources` | Which readings a decision's violation description runs over: `projector`, `reporter:declared`, `reporter:observed` | `…sdlc.factSources`: array of strings |
| violation description | Not a How term: the field `DDD-dec-52` assigns to the authority profile. The How requires it to be a SPARQL 1.1 `SELECT` with one row per violation (`?subject`, `?reason`). The evaluator may bind `?anchor` and `?target` | `…authority.violation`: `{language, binds, text}` |
| `sdlc:Target` | A vocabulary of shapes plus the fact source that reads them | named in vocabulary editions and target declarations: `…sdlc.target` |
| `sdlc:LanguageTarget` | A target read by a fact projector over a repository at a commit | `…sdlc.targetKind: "language"` |
| `sdlc:PlatformTarget` | A target read by a reporter over a deployable unit | `…sdlc.targetKind: "platform"` |
| `sdlc:DesignSystemTarget`, `sdlc:ContentStoreTarget` | Targets whose shapes (CIOs; strings per locale) are realised in turn in a language target | `…sdlc.targetKind: "design-system"` or `"content-store"`; `…sdlc.over`: the language target |
| `sdlc:VocabularyEdition` | A decision fixing, for one target at one edition, the native shape of each fact term, and the target's classifications (effects, jurisdictions) | `…sdlc.record: "vocabulary-edition"`, with `target`, `targetKind`, `edition`, `facts` (term → native shape), classification members, and `factSource` (`{kind, name, version, digest}` or `status`) |
| `sdlc:Realisation` | A decision's shape in a target. **Derived** from the edition's mappings for the fact terms the decision reads; never authored | none: computed |
| `sdlc:realisable` | A decision is realisable in a target iff the target's edition maps every fact term its violation description reads | none: computed |
| `sdlc:TargetDeclaration` | A decision, anchored to a system, naming the targets it is realised in, the repository, and the deployable unit that realises it. Coverage ranges over these | `…sdlc.record: "target-declaration"`; `language`, `platform` (and design-system or content-store) objects, each naming its edition by reference |
| `sdlc:Exclusion` | A decision that an obligation does not apply to one (element, target) pair. A boundary gap | `…sdlc.record: "exclusion"`; `anchor` (the element), `binding` (a reference), `target`. The reason is `why` |
| baseline entry | Not a How term: the authority profile's. The How requires that it attach to (binding, element, target) and be added only by a decision. It marks a debt gap | the profile's (`how.md` D-6) |
| waiver | Not a How term: the authority profile's. Never used for a coverage gap | the profile's |
| `sdlc:Coverage` | For each in-force binding, element of its kind within its anchor, and declared target: realised, baselined, or excluded | none: computed |
| `sdlc:Package` | A product whose What is empty and whose How is its decision records, held under the vendor's genesis | a system of `decprov/1` records |
| `sdlc:Release` | One version of a package: the set its holder accepts and ships together | `…sdlc.record: "release"`; `basedOn` every member, pinned; signed by the holder; supersedes the previous release |
| `sdlc:Import` | A decision in the importer's space, `basedOn` a package decision and its release, anchored in the importer's What. It may narrow the decision; it never alters it | `…sdlc.record: "import"`; `…sdlc.imports`: the reference; `why: {ref}` to the package decision |
| `sdlc:Fork` | A local decision `basedOn` a package decision that changes its statement or violation description | a How decision whose `basedOn` contains the package decision |
| `sdlc:Retention` | An importer's decision to keep resting on a superseded or withdrawn version, with its reason | `…sdlc.record: "retention"`, `basedOn` the withdrawal reading and the import |
| `sdlc:Withdrawal` | A package's declaration that a version is unsafe to rest on | a record superseding that version with `status: "withdrawn"` |
| `sdlc:Reading` | A recorded batch of facts with provenance: source, mode, edition, subject, time read | a manifest entry (`how-examples/facts/manifest.json`). How Writ records it is a demand on Writ (D-3) |
| `sdlc:declared`, `sdlc:observed` | Reporter modes: the unit's declaration in a repository at a commit, or the running unit | `mode` in a reading |
| `sdlc:Unknown` | A contract verdict where no reading of a required source is within freshness. Not a pass; not a violation | none: computed |
| `sdlc:Drift` | A difference between a unit's declared and observed readings | none: computed |
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

## 3. What terms — provisional, the move's

`sdlc:Product`, `sdlc:Domain`, `sdlc:System`, `sdlc:Decider`, `sdlc:Command`,
`sdlc:QualityDemand` (Product Framework v1.10.0 §3.0, §3.1, §3.2.5, §3.3, §3.2.0, §3.6). Then
`sdlc:within`, the ownership edge, used transitively as `sdlc:within*`; `sdlc:localId`; and
`sdlc:referencesDomain` (old §9 `references_domain`). The AIO, context-of-use, content-key and
locale kinds that bindings into design-system and content-store targets range over are likewise
the move's. **None of these is defined here.** The How reads them, and when the move lands they
become pinned references.

## 4. Mapping to Writ's vocabulary — `UNVERIFIED`, Writ's page is not written

| How | Nearest `writ:` term (Writ definition, chapter 4) |
|---|---|
| constraint | an enumerated decision "checked by its own shape", or a rule carrying "its violation shape" |
| binding | none. Writ's "mapping" relates slots across spaces, not What elements to code |
| contract | none. Writ has no deployment facts (D-2) |
| realisation | `writ:` realisation: "relates a decision to the code shape a projector recognises in one language". Same sense; derived here from editions |
| vocabulary edition | none. Writ: "a second language is a second realisation, not a second ontology". Consistent with it |
| fact projector | Writ's Projector contract. Not the What's Projector (old §3.4), which is a read-model fold |
| reporter | none (D-2) |
| package | "a set of accepted decisions under this vocabulary" (Writ definition, chapter 5) |
