# The How — reference for tool builders

<!-- ddd:doc
reader: people building tools that read, write or check How decisions: gates, projectors, reporters, checkers
act: read and write How records, violation descriptions and fact readings in the exact form the How defines
pin: v5.15.2
basis: [DDD-dec-52, DDD-dec-54, DDD-dec-55, DDD-dec-56, DDD-dec-57, DDD-dec-58, DDD-dec-59, DDD-dec-60, DDD-dec-61, DDD-dec-62, DDD-dec-65, DDD-dec-95]
status: current
supersedes: e5a332d:applications/sdlc/how.md
-->

Practitioners: what the How is and how to use it are in [`how.md`](how.md). This is its exact form.

Use this when you build something that reads, writes or checks How decisions: the gate, a fact
projector for a language, a reporter for a platform, or a checker like the one in
[`how-examples/`](how-examples/). It gives the namespace, every term, the record members, the form
of a violation description, the fact terms, the fields of a recorded reading, and what the How
needs from the gate.

**How settled this is.** Everything here is decided, except the points marked *(not settled yet)*.
None of it has been run by a real gate yet: the gate (Writ) is defined but not built, its
code-facts format is not written, and the authority profile is written separately.

---

## Namespace and records

**Namespace.** `https://decision-driven-design.dk/ns/sdlc#`, prefix `sdlc:`. It sits beside Writ's
`https://decision-driven-design.dk/ns/writ#`. The host is the one operated for Writ's vocabulary,
which leaves room for sibling vocabularies under one host. No IRI under `/ns/sdlc` is served or
registered yet *(not settled yet)*.

**Records.** Every How decision is a `dpp/1` record of the Decision Provenance Protocol. How content
goes in one hashed dotted member, `dk.decision-driven-design.sdlc`: the namespace host reversed, as
the protocol asks ("names SHOULD be reverse domain names under the operator's control"). Fields the
authority profile owns go in `dk.decision-driven-design.authority`. That covers the violation
description and the stand-ins for genesis, grant and acceptance. The How defines none of the
authority fields.

Hashed content is objects, arrays and strings only, so numbers and booleans never appear in these
members.

In the tables below, `…sdlc.` stands for `dk.decision-driven-design.sdlc.` and `…authority.` for
`dk.decision-driven-design.authority.`

**Three kinds of term:**
- **How terms**: decision-level, defined here.
- **Fact terms**: what violation descriptions read. They are defined here as a demand on the gate's
  code-facts format, not as a fact format of their own.
- **What terms**: defined by the What ([`what.md`](what.md)), and only read here.

---

## How terms

| Term | Definition | Record shape (`dpp/1`) |
|---|---|---|
| `sdlc:HowDecision` | A decision about how a product's What is realised in code or deployments. It has a kind, an anchor and, usually, a violation description | a record whose `…sdlc.record` is `"decision"`. `statement`, `by`, `at`, `why` and `basedOn` are as in the protocol |
| `sdlc:kind` | One of `constraint`, `binding`, `contract` | `…sdlc.kind` |
| `sdlc:Constraint` | A How decision whose violation description reads code facts alone | `…sdlc.kind: "constraint"` |
| `sdlc:Binding` | A How decision whose violation description joins What elements to the code or content that realises them through `sdlc:realises`, and so carries a coverage obligation. The word is used here and in Writ, whose Realisation contract becomes the Binding contract | `…sdlc.kind: "binding"`; `…sdlc.binds`: the What kind it ranges over |
| `sdlc:Contract` | A How decision over a deployable unit, read from reporter readings | `…sdlc.kind: "contract"`; `…sdlc.freshness`: an ISO 8601 duration string |
| `sdlc:anchor` | The one What element a decision anchors to: the narrowest covering element. Or, in an empty What, the product as space ([`how.md`, Anchoring](how.md#anchoring)) | `…sdlc.anchor`: an IRI |
| `sdlc:binds` | For a binding, the What element kind its quantifier ranges over within the anchor | `…sdlc.binds`: a What term, e.g. `"sdlc:Decider"` |
| `sdlc:standards` | Interface standards a decision names. They are not targets | `…sdlc.standards`: array of strings |
| `sdlc:factSources` | Which provenance a decision's violation description requires, from Writ's set: `file` or `compiler` for projector facts; `deployment-declared` and/or `deployment-observed` for a contract | `…sdlc.factSources`: array of strings |
| violation description | Not a How term: the field belongs to the authority profile. Its form is below | `…authority.violation`: `{language, binds, text}` |
| `sdlc:Target` | A vocabulary of shapes plus the fact source that reads them | named in vocabulary editions and target declarations: `…sdlc.target` |
| `sdlc:LanguageTarget` | A target read by a fact projector over a repository at a commit | `…sdlc.targetKind: "language"` |
| `sdlc:PlatformTarget` | A target read by a reporter over a deployable unit | `…sdlc.targetKind: "platform"` |
| `sdlc:DesignSystemTarget`, `sdlc:ContentStoreTarget` | Targets whose shapes (components; strings per locale) are expressed in turn in a language target. The product's What declares them (this design system at this edition, these locales against this content store), as it declares iOS. Their catalogue is their vocabulary edition, in a package with its own genesis grant. Bindings from abstract interaction object to component, and from key to string, anchor to the interaction object or the content key | `…sdlc.targetKind: "design-system"` or `"content-store"`; `…sdlc.over`: the language target |
| `sdlc:VocabularyEdition` | A decision fixing, for one target at one edition, the native shape of each fact term, and the target's classifications (effects, jurisdictions) | `…sdlc.record: "vocabulary-edition"`, with `target`, `targetKind`, `edition`, `facts` (term → native shape), classification members, and `factSource` (`{kind, name, version, digest}` or `status`) |
| `sdlc:expressible` | A decision is expressible in a target if and only if the target's edition maps every fact term its violation description reads. Its shape there is derived from the edition and has no term of its own. "Realisation" is not minted as a term, in this vocabulary or in Writ's | none: computed |
| `sdlc:TargetDeclaration` | A decision, anchored to a system, naming its language and deployment-platform targets, the repository, and the deployable unit that realises it. User-facing targets (platform contexts, design systems, content stores, locales) are declared by the What instead. Coverage ranges over both | `…sdlc.record: "target-declaration"`; `language`, `platform` (and design-system or content-store) objects, each naming its edition by reference |
| `sdlc:Exclusion` | A decision that an obligation does not apply to one (element, target) pair. A boundary gap | `…sdlc.record: "exclusion"`; `anchor` (the element), `binding` (a reference), `target`. The reason is `why` |
| baseline entry | Not a How term: the authority profile's. The How requires that it attach to (binding, element, target) and be added only by a decision. It marks a debt gap | the profile's |
| waiver | Not a How term: the authority profile's. Never used for a coverage gap | the profile's |
| `sdlc:Coverage` | For each in-force binding, element of its kind within its anchor, and declared target: realised, baselined, or excluded | none: computed |
| `sdlc:Package` | A product with an empty What, a genesis grant, and a decision log, vocabulary editions included. The kinds it binds to are references in its decisions' anchors | a system of `dpp/1` records |
| `sdlc:Release` | One version of a package: the set its holder accepts and ships together | `…sdlc.record: "release"`; `basedOn` every member, pinned; signed by the holder; supersedes the previous release |
| `sdlc:Import` | A decision in the importer's space, `basedOn` a package decision and its release, anchored in the importer's What. It may narrow the decision; it never alters it *(not settled yet: narrow, never alter)* | `…sdlc.record: "import"`; `…sdlc.imports`: the reference; `why: {ref}` to the package decision |
| `sdlc:Fork` | A local decision `basedOn` a package decision that changes its statement or violation description | a How decision whose `basedOn` contains the package decision |
| `sdlc:Retention` | An importer's decision to keep resting on a superseded or withdrawn version, with its reason | `…sdlc.record: "retention"`, `basedOn` the withdrawal reading and the import |
| `sdlc:Withdrawal` | A package's declaration that a version is unsafe to rest on | a record superseding that version with `status: "withdrawn"`. The status is hashed, so this is a new version |
| `sdlc:Reading` | A recorded batch of facts with provenance: source, provenance from Writ's closed set (`file`, `compiler`, … , `deployment-declared`, `deployment-observed`), input, edition, subject, time read | a manifest entry, as in `how-examples/facts/manifest.json`. How Writ records it is a demand on Writ (below) |
| open question | Not a How term: one of Writ's three verdicts (clean, violation, open question). A contract with no reading of a required source within its freshness has a **reported gap**, and its verdict is an open question with the absent reporter as one candidate. `sdlc:Unknown` is not minted | Writ's |
| `sdlc:Drift` | A difference between a unit's `deployment-declared` and `deployment-observed` facts | none: computed |
| `sdlc:Idle` | A How decision with neither a violation description nor a dependent. Reported, never a violation *(not settled yet)* | none: computed |

---

## Violation descriptions

A violation description is a SPARQL 1.1 `SELECT` that returns one row per violation, each with a
`?subject` and a `?reason`. The evaluator may bind two variables:

- `?anchor`, to the anchor of the decision as in force;
- `?target`, to the target being evaluated.

Because `?anchor` is bound to the anchor in force, a decision that ranges over a kind ("every
Decider") ranges over the instances of that kind inside its anchor's subtree (`sdlc:within*`), and
one decision text serves any anchor it is imported at. This is the form Writ's definition names ("a
rule is written as a query … and carries its violation shape"). It is not a new rule language.

A binding's coverage is part of its violation description: its "no code element realises it in this
target" rows are the uncovered (element, target) pairs.

A decision's statement and violation description use only How terms, What terms, interface
standards, and, for a binding into one design system or content store, that target's own terms
*(not settled yet)*. The example checker checks that no statement or violation text contains a
target's name, effect list, region list or native file kind.

---

## Fact terms — what the How needs from the code-facts format

Each fact term needs a mapping in every target edition used to evaluate a decision that reads it.
`how-examples/check.py` holds the same list.

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

In a target, `sdlc:realises` is mapped by the edition to a native shape, such as `[Realises(…)]` on a
C# type or a `@realises` JSDoc tag on a TypeScript export.

## What terms the How reads

`sdlc:Product`, `sdlc:Domain`, `sdlc:System`, `sdlc:Decider`, `sdlc:Command`,
`sdlc:QualityDemand`; the containment edge `sdlc:within`, used transitively as `sdlc:within*`;
`sdlc:localId`; and `sdlc:referencesDomain`. The abstract-interaction-object, context-of-use,
content-key and locale kinds that bindings into design-system and content-store targets range over
are likewise the What's. **None of these is defined here.** They are defined by the What
([`what.md`](what.md), [`what/ontology.ttl`](what/ontology.ttl)), and the How reads them.

---

## Recorded readings

A fact is usable by the gate only when recorded with provenance from Writ's closed set: `file`,
`compiler`, `graph`, `runner`, `data`, `telemetry`, `attestation`, `deployment-declared`,
`deployment-observed`. The last two are separate provenance values, not two inputs under one value,
so that the split shows in the verdict. Each reading carries:

| Field | Projector reading | Reporter reading |
|---|---|---|
| source | `projector` | `reporter` |
| provenance | `file` or `compiler` | `deployment-declared` (from infrastructure as code or a manifest) or `deployment-observed` (from the platform's own API). A measurement of a runtime bound is `telemetry` |
| input | the repository at a commit | the declaration at a commit, or the platform's API at a time. Writ hashes the input |
| edition | the vocabulary edition it implements, by pinned reference | the same |
| subject | repository at commit | the deployable unit's identity, and the commit for `deployment-declared` |
| read at | the landing position | the time of the reading, and the position at which it was recorded |
| by / attributed to | the software identity that read; the human responsible, where known | the same |

`how-examples/facts/manifest.json` has this shape. A fact with no provenance is not a fact the gate
may use. A reporter's claim about its subject is not a fact about the subject until recorded with
this provenance.

A reading of another system's list of versions (to learn of a supersession or withdrawal) is recorded
too, at a position before any verdict uses it *(not settled yet)*.

---

## What the How needs from Writ

The How does not restate Writ's verbs, positions, partitions or guarantees. It requires:

| The How requires | Held by (Writ's definition) |
|---|---|
| a How decision applies at a position only under a live acceptance chain at that position | G2 |
| an import is in force only under the importer's acceptance, never the vendor's | G2, applied to the importer's log only. A vendor acceptance is provenance |
| no agent accepts | G3 |
| constraint and binding verdicts, and contract verdicts over `deployment-declared` facts, gate a change *(not settled yet for `deployment-declared`)* | `land`, condition 3 |
| every verdict names its decision, kind, anchor, import chain, and the readings it used | G7: `explain` never says unknown |
| a verdict is clean, violation, or open question | Writ's three verdicts |
| a missing fact is a reported gap, and a verdict that needs it is an open question with its candidates | G8, which covers reporters |
| an exclusion and a baseline entry are visible at a position and change verdicts only as declared | G1, G7 |

G1 is that a verdict at a position is a pure function of the log up to that position. So the gate
never reads a vendor's system, or a list of versions, live at check time.

**Mapping to Writ's vocabulary.** Writ's vocabulary page is not written; Writ's Draft 2 is the
authority, as Emil states it.

| How | Nearest `writ:` term (Writ definition, chapter 4) |
|---|---|
| constraint | evaluates over projector facts. The citation attributes the projector recognises (`[DesignDecision]`, `[Contract]`) are fact vocabulary, not a binding |
| binding | Writ's Binding contract. Writ adopts the word, and narrows the contract to bindings only: a What element to a shape in a target |
| contract | none as a term. Its facts are reporter facts with provenance `deployment-declared` or `deployment-observed` |
| expressible | none. `writ:realisation` is never minted |
| vocabulary edition | none. Writ: "a second language is a second realisation, not a second ontology". Consistent with it |
| fact projector | Writ's Projector contract. Not the What's Projector, which is a read-model fold |
| reporter | Writ Draft 2's reporters, a reports partition per reporter |
| package | "a set of accepted decisions under this vocabulary" (Writ definition, chapter 5) |

So the three kinds map onto Writ as: constraint → projector facts; binding → the Binding contract;
contract → reporter facts.

### Demands on others, not resolved here

| On | Demand | State |
|---|---|---|
| Writ, code facts | carry the fact terms above, language-neutral, with per-language mapping supplied by an edition | open |
| Writ, contracts | reporters, and `deployment-declared` and `deployment-observed` in the provenance set | answered: Draft 2 has them |
| Writ, the log | reporter readings, and readings of another system's list of versions, are recorded at a position before any verdict uses them | reporter readings answered by Draft 2's reports partition and hashed inputs; the list-of-versions reading is open |
| Writ, `check` | the What graph is readable by `check` at a position, since bindings join over it; the evaluator binds `?anchor` and `?target` | open |
| Writ, `explain` | show anchor, kind, the import chain, and "rests on superseded version" from the last recorded reading | open |
| the authority profile | a baseline entry attaches to (decision, element, target) and is added only by a decision; a waiver never covers a coverage gap; `acceptedBy` and `acceptedAt` map to the acceptance record's `by` and `at`, since `dpp/1` removed them as record members and an undotted member may not be invented. The example does this | open until the profile lands |
| the protocol token | records use the ruled token | answered: `dpp/1` |
| the What | fix the What element identity form and the kind names the How reads | answered: the What has landed with its identity form |

---

## Not settled yet

- **The namespace.** No IRI under `/ns/sdlc` is served or registered yet, and the choice of host and
  path is a reading not yet confirmed.
- **Narrow, never alter.** Whether `sdlc:Import` may only narrow, with any change a `sdlc:Fork`.
- **Idle.** Whether `sdlc:Idle` is reported rather than rejected.
- **Specified once.** Whether a decision's text is restricted to How terms, What terms, interface
  standards and one design-system or content-store target's terms.
- **Gating on declared deployments.** Whether contract verdicts over `deployment-declared` facts
  gate `land`.
- **Recorded list-of-versions readings.** How the gate records a reading of another system's list of
  versions is open on Writ's side.

The full list of open points about the How, in practitioner terms, is in
[`how.md`, "Not settled yet"](how.md#not-settled-yet).

## Where this comes from

For reviewers and auditors.

| Section | Rests on |
|---|---|
| Namespace and records | `DDD-dec-62` (token `dpp/1`); `DDD-dec-52` (the violation description belongs to the authority profile); Writ ADR 0007 (Writ's namespace) |
| How terms | `DDD-dec-55`, `DDD-dec-65` (kinds; "binding"; anchoring); `DDD-dec-56` (package, release); `DDD-dec-57` (targets, design systems, content stores); `DDD-dec-58` (coverage, exclusion, baseline, waiver); `DDD-dec-59` (import, withdrawal, retention); `DDD-dec-60` (provenance, open question, drift) |
| Violation descriptions | `DDD-dec-52`; `DDD-dec-55` (quantifiers within the anchor) |
| Fact terms | proposed with `DDD-dec-55` as a demand on Writ's code-facts format |
| What terms | `DDD-dec-42`, `DDD-dec-63` (the What's vocabulary and identity form) |
| Recorded readings | `DDD-dec-60` |
| What the How needs from Writ | `DDD-dec-54` ruling 5 (the gate is Writ); `DDD-dec-60`; `DDD-dec-61` |

This document merges two earlier texts. The record layouts, fact fields and demands come from
`e5a332d:applications/sdlc/how.md`. The vocabulary was `applications/sdlc/how-vocabulary.md`, whose
full earlier text is at `e5a332d:applications/sdlc/how-vocabulary.md`.
