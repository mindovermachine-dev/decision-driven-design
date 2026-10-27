# The How — a product's realisation, as decisions

**Status: `[PROPOSED]`. Nothing in this document is ruled.** It is Claude's answer to the charter
at `meta/sessions/2026-10-27-product-framework-how/prompt.md`. Emil rules, and his rulings are
recorded verbatim in that directory's `rulings.md`. The decisions it asks for are
`DDD-dec-55` to `DDD-dec-61`. They are filed as proposals and are not in force until ruled.
`DDD-dec-54` records the charter's own rulings, which this document does not reopen.

**Register.** *Ruled* cites a decision. `[PROPOSED]` is Claude's, awaiting a ruling. `[OPEN]`
is not settled by this document. `UNVERIFIED — Emil review` marks a reading of ruled material
that Emil has not confirmed.

**Companions.** The vocabulary is [`how-vocabulary.md`](how-vocabulary.md). The worked decisions
are in [`how-examples/`](how-examples/), with a checker that runs them.

---

## 1. Scope, and what this rests on

### 1.1 Scope and non-goals

The How is the set of decisions that say how a product's What is realised in code and in
deployments. This document fixes what a How decision is, what it may anchor to, how the gate
holds it, how a vendor ships it, and how another product imports it.

It does not define:

| Not here | Where it is |
|---|---|
| Force: genesis, grants, scopes, acceptance, baseline, waiver | the authority profile (`DDD-dec-47`; `DDD-dec-54` ruling 4) |
| The gate's verbs, positions, partitions and guarantees | Writ (`DDD-dec-54` ruling 5) |
| The record, the reference, the resolver, the hash law | the Decision Provenance Protocol, token `decprov/1` (`DDD-dec-53`) |
| The What's element kinds and their identities | the moved What (`DDD-dec-41`, `DDD-dec-42`, `DDD-dec-51`) |
| Execution: work units, the Build seam, SPMC bundles, verdict events (old §5, §5.1, §5.3) | nowhere. Retired by `DDD-dec-42`, not carried forward |
| Delivery: features, releases, `done`, versions, direction, drift (old §7) | nowhere. Retired by `DDD-dec-42` |
| Generation of code from decisions (old §4.2 realisation declarations, §5.2) | out of scope (§10, `DDD-dec-61`) |
| Data conformance (old §13) | an add-on, outside the framework (`DDD-dec-44`) |

### 1.2 Preconditions this document does not have — the weakest point first

The charter assumes four things the repository does not yet hold (`bootstrap.md`, arrival
findings 1–3). The How below is written against them anyway, and each assumption is marked
where it bites.

1. **The What has not moved.** The What element kinds this document binds to (Decider, Command,
   AIO, context of use, content key, locale, system, domain, quality demand) have no landed
   definition in `applications/sdlc/`. They are read from Product Framework v1.10.0 §3, which
   `DDD-dec-41` names as what moves. If the move renames or reshapes a kind, every binding over
   it changes with it.
2. **What element identity has no form.** Anchoring needs stable identities (`DDD-dec-51`). The
   move charter's risk 3 says that form is fixed "before any decision is written against them".
   This document writes decisions against them, using provisional IRIs
   (`https://acme.example/products/shop/what#domain-ordering`). That breaks the move charter's
   order. It is done so the How can be tested at all. The examples are re-anchored by
   supersession if the move fixes another form.
3. **The authority profile is not written.** This document uses its six terms as the charter
   lists them and redefines none of them. Where the How needs something of them, it says so as
   a demand on the profile (§9.4). The worked examples use stand-in records for genesis, grant
   and acceptance. Those stand-ins are the examples', not the profile's.
4. **Writ is defined, not built.** Its definition (Hafeok/writ `3b1c5af`,
   `docs/product-definition.md`, Draft 1) fixes its verbs, guarantees G1–G10 and five
   contracts. Its four format pages are "not written". So this document states what Writ
   enforces against a definition. Where Writ's definition has no place for something the How
   needs, that is listed as a demand on Writ (§9.4), not invented here.

The token is also unsettled on `main`. `DDD-dec-53` rules `decprov/1`. The protocol on `main`
still says `dpp/1`, because PR #40 merged before PR #39 ratified the ruling. Records here say
`decprov/1`. The examples' checker runs the reference implementation with that one literal
substituted, and says so.

---

## 2. The thesis, tested

> The How is not a description of a realisation. It is a set of decisions: each anchored to a
> What element or to the product, accepted under the product's genesis, held against code and
> deployments by a gate, shipped as a package by a vendor, and imported into another product by
> `basedOn` under that product's genesis.

**Verdict `[PROPOSED]`: the thesis holds. It needs four repairs. It does not need a replacement.**
Each clause was tested against the old §§4–7 and against the worked decisions. The examples
exercise every clause except "shipped by a vendor" as a real distribution.

| Clause | Holds? | Repair |
|---|---|---|
| a set of decisions | yes | Everything that varies by target lives in vocabulary editions. Those editions are decisions too (§6), so the set is closed |
| each anchored to a What element or to the product | **only with a reading** | A universally quantified decision ("every Decider…", "every component…") governs many elements, so it has no single element to anchor to. Read the product node as a What element, and anchor to the narrowest element that covers the scope (§3). Without this reading, every quantified decision in a non-empty What anchors to the product, which is the loophole `DDD-dec-54` ruling 1 forbids. `UNVERIFIED — Emil review` |
| accepted under the product's genesis | yes | none; the examples show the chain |
| held against code **and deployments** by a gate | **half** | Writ's five contracts include a Projector over "repository at a commit" and nothing over a running deployment. The contract kind needs a reporter, and a recorded reading so that G1 still holds. Both are demands on Writ (§9.4), not facts about it |
| shipped as a package by a vendor | yes, with a conflict | `DDD-dec-46` says a package's "What is its decisions". `DDD-dec-42` says a decision is not a What element. This document reads a package's What as **empty**. Its decisions then anchor to the package product: the degenerate case, legitimately (§6). `UNVERIFIED — Emil review` |
| imported by `basedOn` under the importer's genesis | yes | The import is itself a decision in the importer's space, with its own anchor there (§7) |

**A naming repair runs through all of it.** "Realisation" already has three meanings: Writ's
(a decision's code shape in one language), `DDD-dec-46`'s (a product's repository scope), and
the charter's kind 2. This document renames kind 2 to **binding**. It keeps "realisation" in
Writ's sense: the shape a decision takes in a target, which is derived and never authored
(§5). `DDD-dec-46`'s "realisation scope" is left as ruled.

---

## 3. Anchoring

*Ruled (`DDD-dec-54` ruling 1):* a How decision anchors to exactly one What element or to the
product. Anchoring to the product is the degenerate case an empty What forces.

**The reading `[PROPOSED]`, `UNVERIFIED — Emil review`.**

1. **The product node is a What element.** The old §3.0 makes the product "the root of the
   What". In a non-empty What, anchoring to the product node is anchoring to a What element.
2. **The product as space is the degenerate case.** The decision space of `DDD-dec-46` is the
   product as space. A decision anchors there only when the product's What is empty: a
   repository with no What, or a package (§6).
3. **The anchor is the narrowest covering element.** A decision anchors to the narrowest What
   element whose subtree contains everything the decision governs. "Every Decider in Ordering"
   anchors to the domain `ordering`. A layer rule over every system's code anchors to the
   product node, because nothing narrower covers both systems. Anchoring wider than needed is a
   finding: the loophole the ruling names.
4. **Quantifiers range within the anchor.** A decision that ranges over a kind ("every
   Decider") ranges over the instances of that kind inside its anchor's subtree. The evaluator
   binds `?anchor` to the anchor of the decision in force (§4.1). One decision text therefore
   serves any anchor it is imported at.
5. **A creating decision anchors to the element it creates.** `DDD-dec-42` left this open for
   the What. For the How the question does not arise: How decisions create no What elements.

Read this way, an empty-What product can still adopt every constraint and contract. Bindings
over it are vacuous, because there is nothing to bind. Writ's own reference customer is that
case: "a Context& architecture package (Varve's layering as decisions) checked by Writ over
Varve". Varve has no Product Framework What.

---

## 4. The kinds

### 4.1 What every How decision is

A How decision is a `decprov/1` record (shape in `how-vocabulary.md` §3). Beyond the protocol's
members it carries:

- **a kind**: constraint, binding or contract;
- **an anchor**, per §3;
- **a violation description**, the field `DDD-dec-52` places on the decision record and in the
  authority profile. Here it is a SPARQL 1.1 `SELECT` that returns one row per violation, each
  with a `?subject` and a `?reason`. The evaluator may bind two variables: `?anchor`, to the
  anchor of the decision as in force, and `?target`, to the target being evaluated. This is the
  form Writ's definition names ("a rule is written as a query … and carries its violation
  shape"). It is not a new rule language;
- **the fact sources it reads**: projector, reporter-declared, reporter-observed (§9).

A verdict is computed from the decision in force at a position and the facts recorded at that
position. It is never stored (`DDD-dec-49`). What is recorded is the decision and the readings
(`DDD-dec-52`).

### 4.2 The three kinds

| | **Constraint** | **Binding** | **Contract** |
|---|---|---|---|
| Is over | code facts alone | a What element (or a kind within an anchor) and the code or content that realises it | a deployable unit |
| Typical anchors | the product node; a system | the element it binds, or the narrowest element covering the instances it quantifies over | a system (deployment identity); a quality demand (§3.6 Kind 2 and the wiring of Kind 1) |
| Facts | projector facts over a repository at a commit | the What graph, plus projector facts that carry `sdlc:realises` (the correspondence from code element to What element) | reporter readings of a unit, declared (its declaration at a commit) or observed (the running unit) |
| Evaluator | the violation description over the facts at p | the same, joining What and code through `sdlc:realises`. Coverage (§8) is part of its violation description | the same, per reading. No fresh reading means **unknown** (§9.3) |
| Gates `land`? | yes | yes | declared readings only. An observed reading is not of the change |
| Worked | `LAYER@1` | `PURE@1`, `REST@1` | `RESID@1` |

**Constraint.** The old layout model (§4.3) is a set of constraints over path facts. Each of
its rule kinds (`must-exist`, `may-exist-here`, `must-co-exist`, `must-not-exist`) is a violation
description. "No orphans" is different in one respect. It is a violation description over the
**decisions in force at p** as well as the facts: a file or component that no allow decision
covers is a violation. That is the charter's "everything not covered is a violation until a
decision covers it". It is the mirror of binding coverage. Bindings require that every What
element be covered by code. No-orphans requires that every piece of code be covered by a
decision (§8.3). The old guards carry over without a rule of their own. Guard 1 ("every rule
cites the principle it protects") is the protocol's required `why` plus `basedOn`. Guard 2
(prefer the allowlist) is advice, and stays advice.

**Binding.** A binding needs what a constraint does not: a correspondence between What
identities and code elements. In the examples that correspondence is the fact `sdlc:realises`,
which each target's vocabulary edition maps to a native shape (`[Realises(…)]` in C#, a
`@realises` JSDoc tag in TypeScript). Writ's definition lists "decision citations on code
elements" among its code facts. That is the same fact, read the other way. A binding is the
only kind whose evaluator reads the What graph. Bindings absorb the old §4.2 "pure core", §4.4
(the canonical REST projection), §4.5 (reification: `reify(AIO, context) → CIO`), §4.6 (content
resolution: `resolve(key, locale) → string`) and §3.2.5's split between system identity and
deployment identity. The last of these is shared with contract: the binding says which unit
realises a system; the contract says what that unit must satisfy. Old §5.2 does not go here; it
is generation (§10).

**Contract.** A contract is over a deployable unit. That unit's identity (domain name, bundle
identifier, account, region) is How, per the old §3.2.5. Kind-2 architectural demands (old
§3.6) are What elements. The contract that holds them anchors to that element, as `RESID@1`
anchors to `qd-residency-eu`. Kind-1 runtime bounds are What elements too. *Which telemetry
measures them* is a contract with observed provenance, anchored to the bound. The old text put
Kind 1 under "runtime-bound conformance" with no How home. This document gives it one (H-9).

### 4.3 A fourth kind? No

The candidate is the old §4.1 "principle licensed by a top decision". **`[PROPOSED]`: not a
kind.** A principle is a decision with no violation description that others are `basedOn`. The
gate evaluates nothing for it. It still matters to the gate in two ways. `explain` shows it in
every derivation that rests on it. And when it is superseded, every decision resting on it
shows "rests on superseded version" (§7.2). Adding a kind would give the gate a category with no
evaluator.

The old earn-their-place rule ("a principle belongs only if a work unit applies it or a
verification enforces it") carries over as a report, not a violation. A How decision with
neither a violation description nor a dependent is **idle**, and `check` lists it. Idle is not
wrong. A product may record a principle before anything rests on it.

Two record types sit beside the three kinds. Neither is a kind, because neither has a violation
description of its own:

- **Target declarations** say which targets a system is realised in, and which unit realises it
  (`TGT-shop-api@1`). They set what coverage ranges over (§8).
- **Exclusions** say that an obligation does not apply to an (element, target) pair, with the
  reason (§8.2).

### 4.4 Should any kind split? No

- **Binding into a language** and **binding into a design system or content store** have the same
  evaluator and the same coverage rule. They differ only in which vocabulary edition names the
  shape. One kind.
- **Contract, declared** and **contract, observed** are one decision read over two provenances. A
  residency rule is the same rule before release and after. Splitting it would make the two
  readings disagree in text as well as in fact.
- **Constraint** and **contract** could merge into "a violation description over some facts".
  They are kept apart because they differ in what an absent fact means. A constraint's projector
  gap is reported per G8, and the commit is still decidable. A contract's missing reading makes
  the verdict unknown. They also differ in what they can gate.

---

## 5. Targets, vocabulary editions, and "specified once"

### 5.1 What a target is

**`[PROPOSED]`.** A **target** is a vocabulary of shapes plus the fact source that reads them.
It comes in three sorts:

- a **language** (C#, TypeScript), read by a fact projector over a repository at a commit;
- a **platform** (Azure, AWS), read by a reporter over a deployable unit;
- a **design system** or **content store**, whose shapes (CIOs; strings per locale) are realised
  in turn in a language. These targets layer over a language target.

An **interface standard** (HTTP, OpenAPI, AsyncAPI, CloudEvents) is not a target. A decision may
name it, as `REST@1` names `POST`. A decision that chooses a standard is a different decision
from one that chooses another standard. The old §4.4 table ("use the standards") survives as
advice on which standards to name.

### 5.2 Specified once, realised per target

**`[PROPOSED]`.** A decision's statement and violation description use only:

- How vocabulary terms;
- What vocabulary terms;
- interface standards;
- for a binding into a design system or content store, that one target's terms (a CIO
  identifier; a locale).

A decision never names a language or platform term. Every per-target shape lives in that
target's **vocabulary edition**, a decision record of its own (`VOC-csharp@1`). The edition maps
each fact term the How defines to its native shape, and carries target-specific
classifications: which APIs are effects, which region is in which jurisdiction.

A decision's **realisation** in a target is then derived, never authored. It is the composition
of the edition's mappings for the fact terms its violation description reads. A decision is
*realisable* in a target iff that target's edition maps every fact term it reads. The examples'
checker computes this. Adding a second language is adding an edition. No decision is touched.

The charter's three checks, each written once, are in `how-examples/`:

| Decision | Kind | C# shape (edition `csharp/1`) | TypeScript shape (edition `typescript/1`) | Decision text touched by the second target? |
|---|---|---|---|---|
| layer rule, `LAYER@1` | constraint | `.csproj`, `<Layer>`, `<ProjectReference>` | workspace package, `"sdlc": {"layer"}`, workspace dependency | no |
| pure core, `PURE@1` | binding | `[Realises]` on a type; effects `DateTime.UtcNow`, `HttpClient`, … | `@realises` on an export; effects `Date.now`, `node:http`, … | no |
| REST projection, `REST@1` | binding | `app.MapPost("/commands/{id}", …)` | `server.post("/commands/{id}", …)` | no |

**Where it would fail.** A target whose facts cannot be stated in the How's fact terms breaks
the property. An example would be a language with no notion of a component that one can depend
on. The repair is then a new fact term: a change to the How vocabulary, made by a decision in
this repository. It is not a change to any product's decisions. The fact terms are a demand on
Writ's code-facts page, which is not written. The How states the facts it reads; it does not
publish a competing fact format (§9.4, D-1).

**Purity is approximate in the examples.** `PURE@1` checks the realising element's component for
effects, not the decide and evolve functions themselves. Behavioural conformance would check
that the core computes what the Decider says. That needs a third fact source, a runner that
executes code against the Decider's scenarios (H-14). Writ's definition has no runner.

---

## 6. The package

*Ruled (`DDD-dec-46`; `DDD-dec-54` ruling 3):* a package is a product with its own genesis,
held by the vendor. In another product's space it is provenance, never authority.

**What a package contains `[PROPOSED]`: decision records, and nothing else.**

| In the package | As |
|---|---|
| constraints, bindings, contracts | decision records |
| realisation vocabularies | vocabulary-edition records, which are decisions. A change to how C# realises a layer is a change to the How, and so a decision (`DDD-dec-54` ruling 2) |
| projector and reporter editions | named inside the vocabulary edition they implement: name, version, digest. The name is content; the binary is not |
| a version of the package | a release record, `basedOn` everything in that version and signed by the holder (`REL@1`) |
| analyzers, projectors, reporters, generators | **not content**. They are the package product's realisation, shipped alongside and referenced by digest |

This tightens the proposal. The proposal listed vocabularies and editions beside decisions. Here
they are decisions, or are named inside decisions. A package is then one thing: a decision log
that another product can walk.

**A package carries no What `[PROPOSED]`.** The proposal said "only the element kinds it binds
to, never instances". Element kinds are not What elements. They are the framework's vocabulary,
here in the `sdlc` namespace, and a package references them by name. If a package's What held
kinds, every package would hold a private copy of the framework's ontology: the
two-sources-of-truth failure. So a package's What is empty. Its decisions anchor to the package
product: the degenerate case, and here the right one.

`DDD-dec-46`'s consequence clause says a package is a product "whose What is its decisions".
Against `DDD-dec-42` ("a decision is not itself a What element"), this document reads it as
"whose What is empty and whose How is its decisions". `UNVERIFIED — Emil review`. If Emil reads it
otherwise, `DDD-dec-46` or `DDD-dec-42` needs superseding.

A package that needs a What kind the framework lacks, such as a new AIO like `range-select`,
cannot ship it. A new kind is a change to the framework here. An instance of a new kind is a What
element in the importer's product. `[OPEN]`: whether the old §3.2.2 "an adopter may register
AIOs" survives the move.

---

## 7. Import and supersession

### 7.1 Import

*Ruled:* a package's decisions enter by import, `basedOn` the package's versions, in force only
under the importer's acceptances.

**`[PROPOSED]`.** An import has three parts:

1. **Landing.** The package's records, pinned, are recorded into the importer's log. A copy is
   not the record (protocol A-3). The pin is how the importer knows it holds what the vendor
   signed. A gate that read the vendor's system at check time would break G1.
2. **An import decision.** A record in the importer's system. It is `basedOn` the package
   decision and the release, pinned, and its `why` is a `ref` to the package decision. It carries
   its own anchor in the importer's What. **An import may narrow a decision, by anchoring it lower;
   it never alters one.** Changing the statement or the violation description is not an import. It
   is a local decision `basedOn` the package's: a fork, recorded as one.
3. **Acceptance** under the importer's genesis chain. Until then the import is proposed and
   nothing in it is in force.

The examples show all three. `IMP-pure@1` was proposed by an agent identity and is in force only
because a human holder of the How grant accepted it (`ACC-1@1`).

### 7.2 Supersession across the import

**`[PROPOSED]`, the proposal kept, with one condition.** When the vendor supersedes a decision,
nothing in the importer changes. The importer's decision is in force under its own acceptance,
resting on the version it pinned. `explain` shows "rests on superseded version". Re-import is a
new landing, a new import decision that supersedes the old one, and a new acceptance.

**The condition.** The protocol has no forward link (Q2): "a reader holding an old record cannot
learn from the protocol that another system has superseded it". The importer learns of a
successor only by reading the package's versions listing (§6.4). For G1 (a verdict at p is a pure
function of the log up to p), that reading must itself be **recorded** in the importer's log.
`explain` shows supersession *as of the last recorded reading*, never from a live lookup. The
examples' checker reads the listing directly. It is a checker, not a gate.

### 7.3 Withdrawal

**`[PROPOSED]`.** A package may declare a version withdrawn: unsafe to rest on. It does so with a
new record that supersedes it with `status: withdrawn` (protocol §3.4; the status is hashed, so
this is a new version). This is the only signal that is ever more than information. Even so, it
never acts by the vendor's authority:

- **What it obliges.** Once a withdrawal reading is recorded, every importer decision resting on
  the withdrawn version is an **open answer** at every `check`, until the importer accepts one
  of two decisions: a re-import, or a retention ("we keep resting on it, because …"). A product
  with an open answer cannot claim its How is specified (§11).
- **What it does not do.** It does not fail `land`, and it does not take the import out of force.
  Either would be authority from the package.
- **Teeth, if wanted.** The importer can adopt, under its own genesis, a decision such as
  "withdrawals from this vendor block `land`". That is the importer's authority, recorded.

---

## 8. Coverage and gaps

### 8.1 The generalised obligation

**`[PROPOSED]`, the proposal kept.** Take every binding in force, every What element of the kind
it binds within its anchor, and every target the product declares for that element. For each
such triple, exactly one of the following holds, and the gate reports which:

1. a realisation exists. The binding's violation description finds no "unrealised" row;
2. the gap is **debt**: a baseline entry on the binding for that (element, target);
3. the gap is a **boundary**: an exclusion decision for that (element, target).

The targets come from target declarations (§4.3), so coverage is computed and never listed by
hand. The old §4.5 (every reachable (AIO, context) pair) and §4.6 (every (key, locale) pair) are
instances of this, as `DDD-dec-45` ruled them into the What as obligations. `PURE@1` and
`REST@1` show it for Deciders and Commands. Their "no code element realises it in this target"
rows are the uncovered pairs.

### 8.2 Is a declared gap a waiver, a baseline entry, or a third thing? Two of them

The proposal said: a baseline entry. **`[PROPOSED]`: two different things, because gaps come in
two different kinds**, and `DDD-dec-45` already names both:

| Gap | Example | Is | Gate reports | Ratchet |
|---|---|---|---|---|
| **debt**: should exist, does not yet | a missing translation (`DDD-dec-45`: "declared missing"); a Decider not yet ported to the second language | a **baseline entry** on the binding, per (element, target) | baselined, with the entry's position | shrinks. An entry may be removed by landing the realisation. It may be added only by a decision |
| **boundary**: cannot apply | a `display-collection` of images in a TUI (`DDD-dec-45`: "declared unreifiable") | an **exclusion**: a decision anchored to the element, with the reason | not applicable, with the reason (old §6.2's third finding) | none. It is not debt, and removing it would be wrong |

**Never a waiver.** A waiver, as the authority profile will define it, suspends a violation that
applies. An unreifiable pair is not a violation that applies. Using a waiver for it would let
waivers silently stand in for boundaries. `UNVERIFIED — Emil review`: the ratchet semantics of
baseline are assumed here, because the profile is not written (§9.4, D-6).

`DDD-dec-45`'s consequence (Claude's reading, not ruled) was that "a declared-unreifiable pair
and a declared-missing key are themselves decisions with a principal". This keeps that for the
exclusion. It refines it for the debt: a baseline entry is added by a decision, but the entry is
a member of the baseline, not a decision of its own.

### 8.3 The other direction

Binding coverage asks whether every What element is realised. The no-orphans reading of a
constraint asks the converse: whether every piece of code is covered by a decision (§4.2). The
old §14.5 saw the same symmetry at the intake ("who may say what") and at reification ("what is
shown where"). The How has it at both ends of realisation.

---

## 9. Facts, provenance, and what the gate enforces

### 9.1 What Writ enforces, stated against its definition

*Ruled:* the gate is Writ. The How does not restate Writ's verbs, positions, partitions or
guarantees. It states what Writ must hold:

| The How requires | Held by (Writ's definition) |
|---|---|
| a How decision applies at p only under a live acceptance chain at p | G2 |
| an import is in force only under the importer's acceptance, never the vendor's | G2, applied to the importer's log only. A vendor acceptance is provenance |
| no agent accepts | G3 |
| constraint and binding verdicts, and contract verdicts over declared readings, gate a change | `land`, condition 3 |
| every verdict names its decision, kind, anchor, import chain, and the readings it used | G7. Its "explain never says unknown" is about a verdict's derivation. A contract verdict of **unknown** (§9.3) still has a full derivation: it names the reading that is missing |
| a missing fact is a gap, never assumed | G8, extended to reporters (§9.3) |
| an exclusion and a baseline entry are visible at p and change verdicts only as declared | G1, G7 |

### 9.2 Which facts the gate may rely on

**`[PROPOSED]`.** Only facts **recorded in the log at a position**, each with this provenance:

| Provenance field | Projector reading | Reporter reading |
|---|---|---|
| source | `projector` | `reporter` |
| mode | `files` or `compiler` (G8) | `declared` (the unit's declaration in a repository at a commit) or `observed` (the running unit) |
| edition | the vocabulary edition it implements, by pinned reference | the same |
| subject | repository at commit | the deployable unit's identity, and the commit for `declared` |
| read at | the landing position | the time of the reading, and the position at which it was recorded |
| by / attributed to | the software identity that read; the human responsible, where known (protocol §3.4) | the same |

`facts/manifest.json` in the examples has this shape. A fact with no provenance is not a fact
the gate may use. A reporter's own claim about its subject is not a fact about the subject until
it has been recorded with this provenance.

### 9.3 When a reporter is absent: unknown, not violation

**`[PROPOSED]`.** A contract names its fact sources and a freshness bound (`RESID@1`: declared
and observed, within `P1D`). For each unit and each source:

- a recorded reading within the bound means the violation description runs and gives zero or
  more violations;
- no reading, or none within the bound, means the verdict is **unknown**, and the missing source
  is named. Unknown is not a pass and not a violation. It is an open question on the record. This
  is `apparatus/encode-verify.md` applied: ground you do not control is verified on a schedule,
  and an unreachable source is unknown.

What an unknown blocks is not the How's to say. Release was Delivery, and Delivery is retired. An
importer that wants unknowns to block something decides so under its own genesis, as with
withdrawals.

Disagreement between declared and observed for the same unit is reported as **drift**. It is not
a third verdict. Each reading has its own verdict, and drift is the difference between them.

### 9.4 Demands this document makes on others — not resolved here

| # | On | Demand |
|---|---|---|
| D-1 | Writ, `code-facts.md` | carry the fact terms the How reads (`how-vocabulary.md` §2), language-neutral, with per-language mapping supplied by an edition |
| D-2 | Writ, contracts | a **Reporter** contract: deployable unit (declared or observed) → facts with provenance. Writ's five contracts have none |
| D-3 | Writ, the log | reporter readings, and readings of another system's versions listing, are recorded at a position before any verdict uses them (G1) |
| D-4 | Writ, `check` | the What graph is readable by `check` at p, since bindings join over it; and the evaluator binds `?anchor` and `?target` |
| D-5 | Writ, `explain` | show anchor, kind, the import chain, and "rests on superseded version" from the last recorded reading |
| D-6 | the authority profile | a baseline entry attaches to (decision, element, target) and is added only by a decision. A waiver never covers a coverage gap. Map `acceptedBy` and `acceptedAt` to the acceptance record's `by` and `at`, since `dpp/1` A-10 removed them as record members and an undotted member may not be invented. The examples do this |
| D-7 | the protocol branch | rename `dpp/1` to `decprov/1` on `main`, as `DDD-dec-53` ruled (now outstanding) |
| D-8 | the move | fix the What element identity form and the kind names this document reads (§1.2) |

---

## 10. Generation

**`[PROPOSED]`: confirmed out of scope.** Writ records generation as open and "decided by
evidence" ("whether the action grammar … can generate code from accepted decisions rather than
only check it"). It places generation after its 1.0. The old §4.2 realisation declarations
(backend, delegation tier) and the §5.2 code-generation seam are not carried forward.

**One condition, so that generation stays additive.** A vocabulary edition maps each How fact
term to a native shape. That mapping is exactly what a generator would read. It is the old §4.3
"dual-read" property: one declaration drives creation and gates it. So nothing in the How may
make an edition check-only. A generator that someday reads editions changes code, and code
changes go through `land`. It does not change the How: tools never change it
(`DDD-dec-54` ruling 2).

---

## 11. Conformance — what a product claims when it says its How is specified

**`[PROPOSED]`.** One level, matching the What's single level (`DDD-dec-51`): **specified and in
force.** A product's How conforms when all of these hold at a stated position:

1. Every How decision is a `decprov/1` record with a kind, an anchor under §3, and a violation
   description. Records without a violation description are allowed and are reported as idle
   where nothing rests on them (§4.3).
2. Every How decision claimed in force has an acceptance chain to the product's genesis under the
   authority profile.
3. Every in-force decision is realisable in every target its anchor's systems declare. Every fact
   term it reads is mapped by a pinned edition.
4. Coverage (§8): every (element, target) pair under every in-force binding is realised,
   baselined or excluded.
5. Every import pins the package's decision and release, and every withdrawal reading has an
   answer (§7.3).
6. Every verdict at the position can be explained from recorded decisions and recorded readings
   alone (G1, G7). Unknowns are listed.

**What it does not claim.** That the code satisfies the How. Satisfaction is a verdict at a
position, computed and never stored. A product with a red `check` can still have a specified How.
Old conformance levels 2–4 (Realised, Verified, Delivered) went with the How and Delivery and
are not revived.

---

## 12. The worked decisions

In [`how-examples/`](how-examples/). There is one decision per kind (plus `REST@1`, the third
"specified once" check). Each is written once, imported and anchored in a product with two
systems, evaluated in two targets, and accepted under a test genesis by a delegated human. The
checker verifies every record, pin, signature and authority link. It also checks realisability
per target and supersession across the import, and runs the violation descriptions over
hand-written facts in both targets. The facts are hand-written because no fact projector or
reporter exists. The verdicts are analytic: planted defects, predicted before the run, fired as
predicted. They show the descriptions execute as written, and nothing more.

| Kind | Decision | Anchored at (importer) | Targets | Planted → verdict |
|---|---|---|---|---|
| constraint | `LAYER@1` | `acme:product` | C#, TypeScript | upward reference → 1; orphan component → 1 |
| binding | `PURE@1` | `acme:domain-ordering` | C#, TypeScript | effect in the TS core → 1; C# → 0 |
| binding | `REST@1` | `acme:domain-ordering` | C#, TypeScript | wrong TS route → 1; C# → 0 |
| contract | `RESID@1` | `acme:qd-residency-eu` | Azure, AWS | US bucket, declared and observed → 1 each; Azure observed → **unknown** |

---

## 13. Open, for Emil

1. The anchor reading (§3): is the product node a What element, with the narrowest covering
   element as the rule?
2. A package's What (§6): empty, against `DDD-dec-46`'s "whose What is its decisions"?
3. The design-system and content-store catalogue. `DDD-dec-44` rules both are What;
   `DDD-dec-45` rules "which CIO, which words" are decisions anchored to the element they bind
   and the catalogue is "the set of accepted decisions". This document reads those decisions as
   How bindings into a layered target (§5.1). If Emil means the catalogue to be What, those are
   What decisions and binding splits into What-side and How-side.
4. Kind 1 runtime bounds' measurement wiring as contracts (§4.2, H-9).
5. The runner as a third fact source, and a demand on Writ (§5.2, H-14).
6. `[OPEN]` Whether adopters may register What kinds (§6, last paragraph).
7. The precondition breach (§1.2, item 2): writing decisions before the identity form is fixed.
   Accept it for a proposal, or hold this document until the move's Gate 3.

---

## Appendix A — Decisions: every departure from the proposal

Kept as proposed and not listed: constraint as a kind; the layout model as a constraint; contract
as a kind with reporter facts; principle is not a kind; coverage generalised across kinds;
`explain` shows supersession and nothing is forced; generation out of scope.

| # | The proposal said | This document says | Reason | Decision |
|---|---|---|---|---|
| H-1 | kind 2 is "Realisation" | kind 2 is **binding**; "realisation" is the derived per-target shape of any decision | "Realisation" already means three things (Writ's vocabulary, `DDD-dec-46`, and the charter's second use). Writ owns the per-target sense, and the gate speaks Writ's language | `DDD-dec-55` |
| H-2 | anchor to one What element or the product | the same, read as: the product node is a What element; anchor to the narrowest covering element; the product-as-space only when the What is empty | Without it, quantified decisions in a non-empty What have no legal anchor except the loophole | `DDD-dec-55` |
| H-3 | every language-specific shape is a realisation under a vocabulary edition | realisations are **derived** from editions, never authored per decision | If realisations were authored per decision, adding a target would need a record per decision, and that drifts. Derived, adding a target touches nothing but an edition | `DDD-dec-57` |
| H-4 | a target is a language, a design system or a content store | adds **platform** targets; excludes interface standards (decisions may name them); design system and content store layer over a language | Contracts need platform vocabularies (`RESID@1`). HTTP in the REST projection is a choice of standard, not a target | `DDD-dec-57` |
| H-5 | decisions; vocabularies; projector and reporter editions; nothing else | **decision records only**. Vocabularies are edition decisions; projector and reporter editions are named inside them; binaries are realisation | "Every change to the How is a decision" makes an edition a decision. The proposal's "editions as content" and "analyzers as realisation" were the same objects listed twice | `DDD-dec-56` |
| H-6 | a package carries the element kinds it binds to | a package carries **no What** | Kinds are framework vocabulary, not What elements. A What of kinds per package would be a private copy of the ontology | `DDD-dec-56` |
| H-7 | a declared gap is a baseline entry | debt is a baseline entry; a **boundary** is an exclusion decision; a waiver never covers a gap | `DDD-dec-45` already distinguishes "missing" (debt) from "unreifiable" (boundary). A boundary must not shrink under a ratchet | `DDD-dec-58` |
| H-8 | (not raised) | no-orphans is coverage of code by decisions, the mirror of binding coverage | It makes "no orphans" a violation description over in-force decisions, which is what the gate must evaluate | `DDD-dec-55` |
| H-9 | contracts hold the §3.6 Kind-2 demands | contracts also hold the **measurement wiring** of Kind-1 bounds; one decision, read under declared and observed provenance | Kind 1 had no How home once old §6 retired. A contract over observed readings is that home | `DDD-dec-60` |
| H-10 | state whether a package may withdraw a version | yes, by a superseding record with `status: withdrawn`. It obliges an answer (re-import or retention) and never blocks by the vendor's act | Provenance never authority (`DDD-dec-54` ruling 3), with an answer the importer cannot skip | `DDD-dec-59` |
| H-11 | `explain` shows "rests on superseded version" | the same, **from a recorded reading** of the package's versions listing | The protocol has no forward link (Q2), and G1 forbids live lookups in verdicts | `DDD-dec-59` |
| H-12 | (not raised) | an import may narrow a decision (anchor lower) and never alter it. Altering is a fork, recorded as a local decision `basedOn` the package's | Otherwise a vendor decision could be in force in a form the vendor never signed | `DDD-dec-59` |
| H-13 | principle is not a kind | kept, plus an **idle** report for decisions with neither a violation description nor a dependent | Carries the old earn-their-place rule as a report, not a violation | `DDD-dec-55` |
| H-14 | facts from projectors and reporters | names a third source, a **runner** (execution against the What's scenarios), as a demand on Writ. Not used by the worked decisions | The pure-core binding exists to make behavioural conformance possible. Static facts cannot check it | `DDD-dec-60` |
| H-15 | generation out of scope | confirmed, on condition that no edition may be made check-only | Keeps generation additive, as Writ's definition says it is | `DDD-dec-61` |
| H-16 | records use the ruled token | they do (`decprov/1`), and the protocol on `main` does not | `DDD-dec-53` is ruled; its rename is outstanding (D-7) | — |
| H-17 | (not raised) | target declarations and exclusions are record types, not kinds | Neither has a violation description of its own | `DDD-dec-55` |

## Appendix B — where the old §§4–7 went

| Old section | Disposition here |
|---|---|
| §4.1 decisions, principles, patterns | decisions: every How record. Principles: decisions others rest on (§4.3). Patterns: bindings. Earn-their-place: the idle report |
| §4.2 application contract: pure core | binding (`PURE@1`) |
| §4.2 infrastructure and runtime contract; deployment identity | contract; binding of a unit to a system (§4.2) |
| §4.2 the seam between them | contract, declared versus observed: drift (§9.3) |
| §4.2 realisation declarations, delegation tier | generation: out of scope (§10) |
| §4.3 repository layout model | constraints; no-orphans as coverage of code (§4.2, §8.3) |
| §4.4 interface contracts; canonical REST projection | standards named in decisions (§5.1); binding (`REST@1`) |
| §4.5 screen composition; Atomic Design; reification | bindings into a design-system target. Coverage and unreifiable pairs: §8 (`DDD-dec-45`). Atomic Design's levels and "tokens not literals": constraints a design-system package may ship |
| §4.6 content resolution | bindings into a content-store target; coverage per locale: §8 |
| §5, §5.1, §5.3 work units, the Build seam, seam demand | retired (`DDD-dec-42`); not carried. Writ's `land` is the only write path |
| §5.2 the code-generation seam | out of scope (§10) |
| §6.1–§6.2 verification requirements and anatomy | the gate is Writ: G1 for determinism, G7 for per-verdict derivation. "The oracle is derived, never authored in the check" becomes: violation descriptions read the What graph |
| §6.3 required verification kinds | layout and contract → constraint; seam and domain → binding; runtime-bound → contract (observed); behavioural → binding plus runner (H-14); data conformance → add-on (`DDD-dec-44`); pattern, journey, state and Decider justification → What-side checks, the move's |
| §6.3.1 conformance wire protocol | input to the runner demand (H-14); not carried |
| §7 Delivery | retired (`DDD-dec-42`) |
