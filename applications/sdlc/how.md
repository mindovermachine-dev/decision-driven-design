# The How — deciding how your product's What is built and deployed

<!-- ddd:doc
reader: architects and developers deciding how a product's What is realised in code and deployments
act: write, import and check How decisions — constraints, bindings and contracts — against a product's What
pin: v5.15.2
basis: [DDD-dec-42, DDD-dec-44, DDD-dec-45, DDD-dec-46, DDD-dec-47, DDD-dec-49, DDD-dec-52, DDD-dec-54, DDD-dec-55, DDD-dec-56, DDD-dec-57, DDD-dec-58, DDD-dec-59, DDD-dec-60, DDD-dec-61, DDD-dec-62, DDD-dec-65, DDD-dec-95]
status: current
supersedes: e5a332d:applications/sdlc/how.md
-->

Tool builders: the vocabulary, record layouts, fact terms and the mapping to the gate are in
[`how-reference.md`](how-reference.md).

Use this when you know what a product is and does (its What, [`what.md`](what.md)) and now have
to decide how it is built and deployed: which layers the code has, which shape a Decider takes in
C#, where personal data may be stored.

After reading it you can:
- write a How decision of the right kind, and anchor it to the right part of the What;
- reuse decisions a vendor ships as a package, and know what stays your call;
- see what the gate checks, what it reports as a gap, and what "the How is specified" claims.

**How settled this is.** Part of this is decided by explicit rulings. The rest was proposed and
has not been ruled on its own: the earlier text said those parts stay proposed until it was
merged, and whether the merge settled them has not been ruled. Until it is, every point without a
ruling of its own is marked *(not settled yet)* and listed at the end. None of it has yet been
tried on a real product beyond the worked example, so try it before you rely on it. The gate that enforces the How, Writ, is defined but not yet built. The authority
profile that defines grants, acceptance, baselines and waivers is written separately; until it
lands, the worked example uses stand-in records for those.

**The worked example** is Acme Shop, the same product as in [`what.md`](what.md). It has two
systems: `shop-api`, written in C# and deployed on Azure, and `shop-bff`, written in TypeScript
and deployed on AWS. Acme Shop does not write its How from scratch. It imports four decisions from
a test vendor's package, and its architect accepts them. All of it is in
[`how-examples/`](how-examples/), with a checker that runs.

---

## What the How is

The How is not a description of how the software happens to be built. It is a set of decisions.
Each one:

- is anchored to a part of the What, or to the product;
- is in force only once it is accepted under the product's founding grant, its genesis grant;
- is held against the code and the deployments by a gate;
- may be shipped by a vendor as a package;
- and may be imported into another product, where it rests on the package's version and is in
  force only under that product's own genesis grant.

Every change to the How is a decision. Tools never change the How. Whatever a tool gathers is a
proposal, and it counts only once a human holder accepts it.

**Not in this document:**

| What | Where |
|---|---|
| Who may accept a decision, and how it comes into force: the genesis grant, grants, scopes, acceptance, baselines, waivers | the authority profile. The How uses these terms and redefines none of them |
| The gate's verbs, positions, partitions and guarantees | Writ, the gate. The How states what it needs from Writ, not how Writ works |
| The record format, references, the resolver and the hash law | the Decision Provenance Protocol, `dpp/1` |
| The kinds of What element and their identities | [`what.md`](what.md) |
| Work units, a build seam, execution bundles, verdict events | nowhere. This framework has none of them |
| Features, releases, "done", product versions, direction, drift | nowhere. The framework does not model delivery |
| Generating code from decisions | out of scope (see [Generation](#generation)) |
| Checking production data against the What | an add-on, outside the framework |

---

## A How decision

Every How decision is a signed record in the Decision Provenance Protocol (`dpp/1`). Beyond what
every record carries (statement, author, time, reason, and what it rests on), a How decision has:

- **a kind**: constraint, binding or contract ([The three kinds](#the-three-kinds));
- **an anchor**: the part of the What it governs ([Anchoring](#anchoring));
- **a violation description**: a query that returns one row per violation, each naming the thing
  that violates and why. It is the form the gate evaluates. Its exact form is in
  [`how-reference.md`](how-reference.md). The field itself belongs to the authority profile;
- **the facts it needs**: which kind of evidence its violation description reads, such as code
  read from a repository, or a deployment as declared or as observed.

A verdict is never stored. It is computed from the decision in force at a position and the facts
recorded at that position. What is recorded is the decision and the facts it was computed over.

*In Acme Shop:* the vendor's decision "every data store holding personal data is in an EU region,
both as declared and as observed" carries a violation description that lists each offending store.
It requires two kinds of fact: the deployment as declared, and the deployment as observed.

---

## The three kinds

The How has three kinds of decision *(not settled yet)*.

| | **Constraint** | **Binding** | **Contract** |
|---|---|---|---|
| Is about | the code alone | a What element, and the code or content that realises it | a deployable unit |
| Usually anchored to | the product, or one system | the element it binds, or the narrowest element containing everything it ranges over | a system, or a quality demand |
| Reads | facts read from a repository at a commit | the What itself, plus code facts that say which What element each piece of code realises | facts about a running or declared deployment |
| Can block a change from landing? | yes | yes | only through facts about the deployment *as declared*. A fact about the deployment as observed is not part of the change *(not settled yet)* |
| In Acme Shop | the layer rule | pure core; the REST projection | data residency |

**Constraint.** A constraint governs the shape of the code. A repository layout model is a set of
constraints: each rule that a path must exist, may exist here, must exist alongside another, or
must not exist is a violation description over path facts.

"No orphans" is a constraint that reads the decisions in force as well as the code: a file or
component that no allow decision covers is a violation. So everything not covered is a violation until
a decision covers it *(not settled yet)*. Two habits from layout models carry over without rules of their own. Every
rule cites the principle it protects; the protocol's required reason and "rests on" do that.
Prefer an allowlist; that stays advice.

*In Acme Shop:* the layer rule says every component is in exactly one of four ranked layers
(domain, application, infrastructure, host), no component depends on a higher layer, and a
component in no layer is a violation.

**Binding.** A binding needs what a constraint does not: a correspondence between the What and the
code. That correspondence is a code fact. A piece of code declares the What element it realises,
for example with a `[Realises(…)]` attribute in C# or a `@realises` tag in TypeScript. A binding is
the only kind whose violation description reads the What.

Bindings cover:
- keeping a Decider's logic in a pure core, free of effects;
- the canonical REST shape of commands;
- which concrete component shows each abstract interaction object, per context of use;
- which words a content key resolves to, per locale;
- which deployable unit realises which system. The binding names the unit; a contract says what
  that unit must satisfy.

*In Acme Shop:* the pure-core binding says every Decider is realised, in every language of every
system that uses its domain, by code whose component uses no effect. The REST binding says every
command is handled at `POST /commands/{its wire name}`.

**Contract.** A contract is about a deployable unit. The unit's identity (domain name, bundle
identifier, account, region) is How. Architectural demands in the What, such as "personal data
resides in the EU", are held by contracts anchored to that demand. A runtime bound is a What element
too. Which telemetry measures it is a contract over telemetry facts, anchored to the bound
*(not settled yet)*.

*In Acme Shop:* the residency contract is anchored to the product-wide demand "personal data
resides in the EU", and reads each unit's declared and observed deployment within a day.

**Principles are not a fourth kind** *(not settled yet)*. A principle is a decision with no
violation description that other decisions rest on. The gate evaluates nothing for it. It still
matters: `explain` shows it under every decision that rests on it, and when it is superseded,
everything resting on it shows "rests on superseded version".

**Idle decisions are reported, not rejected** *(not settled yet)*. A How decision with neither a
violation description nor anything resting on it is idle, and `check` lists it. Idle is not
wrong: you may record a principle before anything rests on it.

**Two record types sit beside the kinds** *(not settled yet)*. Neither has a violation description
of its own:
- a **target declaration** says which language and deployment platform a system is realised in,
  and which unit realises it. It sets what coverage ranges over;
- an **exclusion** says that an obligation does not apply to one element in one target, and why.

**No kind splits** *(not settled yet)*.
- A binding into a language and a binding into a design system or content store have the same
  evaluation and the same coverage rule. They differ only in which vocabulary names the shape. One
  kind.
- A contract over declared facts and one over observed facts are one kind. The violation
  description says which it requires. Residency may be met by the declaration; "no public
  endpoint" needs the observation. A rule that needs both is one decision read over both, and its
  two verdicts stay apart.
- Constraints and contracts stay apart, because a missing fact means different things. A missing
  code fact is reported, and the change is still decidable. A missing deployment reading makes the
  verdict an open question. They also differ in what they can block.

---

## Anchoring

A How decision anchors to exactly one What element, or to the product.

1. **The product is a What element.** It is the root of the What. Anchoring to it is anchoring to
   a What element.
2. **The product as a bare space is the exception.** A decision anchors to the product with no
   What only when the product's What is empty: a repository with no What, or a package.
3. **Anchor to the narrowest element that covers everything the decision governs.** "Every Decider
   in Ordering" anchors to Ordering. "Every Decider" anchors to the product. A rule over every
   system's code anchors to the product, because nothing narrower covers both systems.
4. **Anchoring wider than needed is the loophole.** It is a loophole only when a narrower element
   exists and was not used. The checker warns when the narrowest element covering what a decision
   governs *today* is narrower than its anchor. The warning is advisory. A product-wide "every
   Decider" rule in a product whose Deciders all happen to sit in one domain warns, yet the anchor
   is right if the rule means the whole product.
5. **What "covers" means per kind.** A binding governs the elements of its kind within the anchor,
   so the covering element is their narrowest common container. A constraint over code governs
   the code of the declared systems within the anchor. A contract anchors to the element it holds, not to a
   container, and its anchor is not checked.
6. **"Every" ranges within the anchor.** A decision about "every Decider" means every Decider
   inside its anchor. The same decision text therefore serves wherever it is anchored.
7. **How decisions create no What elements**, so the question of what a creating decision anchors
   to does not arise in the How.

An empty-What product can still adopt every constraint and contract. Its bindings are vacuous,
because there is nothing to bind. The gate's own reference customer is that case: a Context&
architecture package, Varve's layering written as decisions, checked by Writ over Varve, which has
no What.

*In Acme Shop:* the layer rule is anchored to the product, the narrowest element covering both
systems' code. Pure core and the REST projection are anchored to the Ordering bounded context,
where the Deciders and commands sit. Residency is anchored to the demand it holds. The checker's
self-test re-anchors pure core at the product and expects the advisory warning.

---

## Targets

A **target** is a vocabulary of shapes plus the source that reads them. There are three sorts:

- a **language** (C#, TypeScript), read from a repository at a commit;
- a **platform** (Azure, AWS), read from a deployable unit;
- a **design system** or **content store**, whose shapes (components; strings per locale) are in
  turn expressed in a language. These layer over a language target.

Design systems and content stores are targets, not catalogues:
- The What declares them: "this design system at this edition, these locales against this content
  store", just as it declares iOS.
- The catalogue (components, tokens, strings) is the target's vocabulary edition. It lives in a
  package with its own genesis grant, typically a design team's.
- The choices of which component shows each abstract interaction object, and which string each
  key resolves to, are How bindings anchored to the interaction object or the content key.
- Nothing in a catalogue is a What element of the product that uses it.

So targets are declared in two places. The What declares the user-facing ones: platform contexts
such as iOS, design systems, content stores and locales. A How target declaration declares the
realisation ones: languages and deployment platforms. Coverage ranges over both.

**An interface standard is not a target** *(not settled yet)*. HTTP, OpenAPI, AsyncAPI and
CloudEvents are standards a decision may name, as the REST binding names `POST`. Choosing one
standard is a different decision from choosing another. Prefer naming established standards.

*In Acme Shop:* the two target declarations say `shop-api` is C# on Azure and `shop-bff` is
TypeScript on AWS.

---

## Specified once, realised in every target

*(not settled yet, as a whole)*

A decision's statement and violation description use only:
- How terms;
- What terms;
- interface standards;
- for a binding into one design system or content store, that target's own terms (a component
  identifier; a locale).

A decision never names a language or platform term. Every per-target shape lives in that target's
**vocabulary edition**, which is a decision of its own. The edition maps each fact term the How
defines to its native shape, and carries target-specific classifications: which APIs are effects,
which region is in which jurisdiction.

A decision's shape in a target is then derived, never written by hand. It is the edition's
mappings for the fact terms the decision reads. A decision is **expressible** in a target if that
target's edition maps every fact term it reads. Adding a second language is adding an edition. No
decision changes.

*In Acme Shop:*

| Decision | Kind | Shape in C# | Shape in TypeScript | Changed by adding the second language? |
|---|---|---|---|---|
| layer rule | constraint | `.csproj`, `<Layer>`, `<ProjectReference>` | workspace package, `"sdlc": {"layer"}`, workspace dependency | no |
| pure core | binding | `[Realises]` on a type; effects such as `DateTime.UtcNow`, `HttpClient` | `@realises` on an export; effects such as `Date.now`, `node:http` | no |
| REST projection | binding | `app.MapPost("/commands/{id}", …)` | `server.post("/commands/{id}", …)` | no |

**Where this breaks.** A target whose facts cannot be stated in the How's fact terms breaks it, for
example a language with no notion of a component that can depend on another. The repair is a new
fact term: a change to the How's vocabulary, made by a decision in this framework, not a change to
any product's decisions. The fact terms are a demand on the gate's code-facts format, which is not
yet written. The How states the facts it reads; it does not publish a competing fact format.

**Purity is approximate in the example.** The pure-core binding checks the realising component for
effects, not the decide and evolve functions themselves. Checking that the core computes what the
Decider says needs facts from a runner that executes the code against the Decider's scenarios.
The gate's definition has such a source. The worked decisions do not use it.

---

## Packages

A package is a product with its own genesis grant, held by its vendor. In another product it is a
source of decisions, never an authority.

**A package holds decision records and nothing else.**

| In the package | As |
|---|---|
| constraints, bindings, contracts | decision records |
| vocabularies | vocabulary-edition records, which are decisions. A change to how C# expresses a layer is a change to the How, and so a decision |
| the tools that read facts (projectors and reporters) | named inside the vocabulary edition they implement: name, version, digest. The name is content; the binary is not |
| a version of the package | a release record that rests on everything in that version and is signed by the holder |
| analysers, projectors, reporters, generators | **not content**. They are what the package ships alongside, referenced by digest |

So a package is one thing: a decision log another product can walk.

**A package has no What.** The kinds of What element it binds to are the framework's vocabulary,
referenced by name in its decisions. They are not What elements of the package. Its decisions
anchor to the package itself, the empty-What case, which is right here.

A package cannot ship a new kind of What element, such as a new interaction object like
`range-select`. A new kind is a change to the framework. An instance of a new kind is a What
element in the importing product. Whether adopters may register new kinds themselves is
*(not settled yet)*.

*In Acme Shop:* the test vendor's package holds the layer rule, pure core, the REST projection,
residency, four vocabulary editions (C#, TypeScript, Azure, AWS) and its release records.

---

## Importing a package

A package's decisions enter your product by import. Each import rests on the package's version,
and is in force only under your own acceptances.

An import has three parts *(not settled yet as a whole; see the end)*:

1. **Landing.** The package's records, pinned to their exact versions, are recorded into your log.
   A copy is not the record. The pin is how you know you hold what the vendor signed. The gate
   never reads the vendor's system at check time.
2. **An import decision**, in your own product. It rests on the package decision and the release,
   pinned, and gives the package decision as its reason. It has its own anchor in your What.
3. **Acceptance** under your genesis grant. Until then the import is only proposed, and nothing in
   it is in force.

**An import may narrow a decision, never alter it** *(not settled yet)*. Anchoring it lower is
narrowing. Changing its statement or violation description is not an import: it is a local
decision resting on the package's, a fork, recorded as one.

*In Acme Shop:* an agent proposed the pure-core import. It is in force only because the architect,
who holds the How grant delegated from the founder's genesis grant, accepted it. One acceptance
record covers the four imports and the two target declarations.

### When the vendor supersedes a decision

Nothing in your product changes. Your import stays in force under your acceptance, resting on the
version you pinned. `explain` shows "rests on superseded version". To move to the new version you
re-import: a new landing, a new import decision that supersedes the old one, and a new acceptance
*(not settled yet: written as a proposal; a decision on packages states that supersession forces
nothing, so this may already be settled)*.

You learn of a new version only by reading the package's list of versions; the protocol has no
link forward from an old record. That reading must itself be recorded in your log, and `explain`
shows supersession as of the last recorded reading, never from a live lookup
*(not settled yet)*.

*In Acme Shop:* the vendor's second release supersedes the layer rule with a version that adds a
`test` layer. Acme Shop still rests on the first. The checker shows that, and shows that nothing
in force changed. The examples' checker reads the list of versions directly: it is a checker, not
a gate, so it does not meet the recorded-reading condition above.

### When the vendor withdraws a version

A vendor may declare a version withdrawn: unsafe to rest on. It does so with a new record that
supersedes it with the status `withdrawn`. This is the only signal from a vendor that is more than
information, and even so it never acts by the vendor's authority.

- **What it obliges.** Once a withdrawal is recorded in your log, every decision of yours resting
  on that version is an **open answer** at every `check`, until you accept one of two decisions: a
  re-import, or a retention ("we keep resting on it, because …"). While an answer is open, your
  How is not specified ([Conformance](#conformance)).
- **What it does not do.** It does not block a change from landing, and it does not take the import
  out of force. Either would be authority from the vendor.
- **If you want it to block.** You can accept, under your own genesis grant, a decision such as
  "withdrawals from this vendor block landing". That is your authority, recorded.

---

## Coverage and gaps

### Every bound element, in every target

Take every binding in force, every What element of the kind it binds within its anchor, and every
target your product declares for that element. For each, exactly one of these holds, and the gate
reports which *(not settled yet as stated here; see the end)*:

1. it is realised: the binding's violation description finds nothing unrealised;
2. the gap is **debt**: a baseline entry on the binding, for that element in that target;
3. the gap is a **boundary**: an exclusion decision for that element in that target.

The targets come from target declarations and from the What, so coverage is computed, never listed
by hand. "Every reachable abstract interaction object has a component in every context" and "every
content key resolves in every locale" are instances of it. *In Acme Shop:* the pure-core and REST
bindings show it for Deciders and commands. Their "nothing realises it in this target" rows are
the uncovered pairs.

### Debt and boundaries are different things

| Gap | Example | Recorded as | The gate reports | Over time |
|---|---|---|---|---|
| **Debt**: should exist, does not yet | a missing translation; a Decider not yet ported to the second language | a **baseline entry** on the binding, per element and target | baselined, with where the entry was recorded | shrinks. An entry may be removed by landing the code that realises the pair. Only a decision may add one |
| **Boundary**: cannot apply | a collection of images in a text-only interface | an **exclusion**: a decision anchored to the element, with its reason | not applicable, with the reason | stays. It is not debt, and removing it would be wrong |

**A waiver never covers a gap.** A waiver suspends a violation that applies. An unreifiable pair is
not a violation that applies. Using a waiver for it would let waivers silently stand in for
boundaries. How baselines shrink is the authority profile's to define; the behaviour described
above is assumed until it does *(not settled yet)*.

An exclusion is a decision with a principal. A baseline entry is added by a decision, but the entry
is a member of the baseline, not a decision of its own.

### The other direction

Binding coverage asks whether every What element is realised in code. The no-orphans constraint
asks the converse: whether every piece of code is covered by a decision *(not settled yet)*. The
How has the check at both ends.

---

## What the gate checks

The gate is Writ. The How does not restate how Writ works. It states what Writ must hold:

| The How needs | In plain words |
|---|---|
| a decision applies only under a live acceptance chain | nothing is in force without a valid acceptance back to the genesis grant at that position |
| an import is in force only under your acceptance | a vendor's acceptance is provenance, never authority in your product |
| agents never accept | only a human holder brings a decision into force |
| constraint and binding verdicts, and contract verdicts over declared deployments, can block a change | they gate landing *(not settled yet for declared-deployment contracts)* |
| every verdict names its decision, kind, anchor, import chain and the facts it used | `explain` can always say why |
| a verdict is clean, violation, or open question | there is no "unknown" |
| a missing fact is a reported gap, and a verdict that needs it is an open question with its candidates | absence is never a pass |
| exclusions and baseline entries are visible at a position, and change verdicts only as declared | nothing hides a violation silently |

### Which facts the gate may use

Only facts recorded with their provenance, from the gate's closed set: `file`, `compiler`, `graph`,
`runner`, `data`, `telemetry`, `attestation`, plus two values for deployments:

- `deployment-declared`, from infrastructure as code or a manifest;
- `deployment-observed`, from the platform's own API.

They are two provenance values, not two inputs under one value, so the difference shows where it
matters: in the verdict. A contract's violation description says which it requires. A fact with no
provenance is not a fact the gate may use. A reporter's claim about its subject is not a fact until
it is recorded with provenance. The fields every recorded reading carries are in
[`how-reference.md`](how-reference.md).

### When a reporter is absent

A contract names its fact sources and how fresh they must be. For each unit and each source:

- a recorded reading within that time means the violation description runs, and the verdict is
  clean or violation;
- no reading, or none fresh enough, means the gap is reported and the verdict is an **open
  question**, with the absent reporter named as one possible cause. An open question is neither a
  pass nor a violation. Ground you do not control is checked on a schedule, and an unreachable
  source is never a pass.

An open question can block. What it blocks is Writ's to define, not the How's.

When the declared and observed facts about one unit disagree, that is reported as **drift**. Drift
is not a third verdict: each provenance has its own verdict.

*In Acme Shop:* a personal-data bucket declared and observed in `us-east-1` gives one violation for
each provenance. No observed facts exist for the Azure unit, so its observed verdict is an open
question, with the gap reported and the absent reporter named.

---

## Generation

Generating code from decisions is out of scope for the How. The gate's definition records it as
open, to be decided by evidence, after its 1.0. Declarations of how code is generated, and a
code-generation seam, are not part of this framework.

**One condition keeps generation possible later.** A vocabulary edition maps each fact term to a
native shape, and that mapping is exactly what a generator would read: one declaration that both
drives creation and checks it. So no vocabulary edition may be made check-only
*(not settled yet)*. A generator that
someday reads editions changes code, and code changes go through landing. It does not change the
How: tools never change it.

---

## Conformance

*(not settled yet, as a whole)*

There is one level, matching the What's single level: **specified and in force.** A product's How
conforms when all of these hold at a stated position:

1. Every How decision is a `dpp/1` record with a kind, an anchor per [Anchoring](#anchoring), and a
   violation description. A record without one is allowed, and is reported idle when nothing rests
   on it.
2. Every How decision claimed in force has an acceptance chain to the product's genesis grant under
   the authority profile.
3. Every decision in force is expressible in every target its anchor's systems declare, and every
   fact term it reads is mapped by a pinned edition.
4. Coverage: every element and target under every binding in force is realised, baselined or
   excluded.
5. Every import pins the package's decision and release, and every recorded withdrawal has an
   answer.
6. Every verdict at the position can be explained from recorded decisions and recorded facts alone.
   Gaps and open questions are listed.

**What conformance does not claim:** that the code satisfies the How. Satisfaction is a verdict at a
position, computed and never stored. A product whose `check` is red can still have a specified How.

---

## The worked example

Everything is in [`how-examples/`](how-examples/): one package decision per kind, plus the REST
projection as a second binding. Each is written once in the vendor's package, imported and
anchored in Acme Shop, evaluated in two targets, and accepted by the architect under Acme Shop's
genesis grant. The checker verifies every pin, signature and authority link, warns on wide anchors,
and checks expressibility per target and supersession across the import.

Acme Shop is a test product. Nothing in it is acceptable into a real product, and its records are
superseded, never edited. Every record is conformant under the reference implementation on `main`,
run unmodified.

No fact projector or reporter exists yet, so the facts are written by hand. The verdicts are
planted defects, predicted before the run, that fired as predicted. They show the violation
descriptions run as written, and nothing more.

| Kind | Decision | Anchored in Acme Shop | Targets | Planted defect, and verdict |
|---|---|---|---|---|
| constraint | layer rule | the product | C#, TypeScript | an upward reference: 1 violation. A component in no layer: 1 violation |
| binding | pure core | the Ordering bounded context | C#, TypeScript | an effect in the TypeScript core: 1 violation. C#: none |
| binding | REST projection | the Ordering bounded context | C#, TypeScript | a wrong TypeScript route: 1 violation. C#: none |
| contract | residency | the demand "personal data resides in the EU" | Azure, AWS | a US bucket, declared and observed: 1 violation each. Azure observed: **open question**, gap reported, absent reporter named |

---

## Not settled yet

Each of these was written as a proposal and has not been ruled on its own.

- **Exactly three kinds.** Whether the How has these three kinds; whether principles stay a decision others rest on rather than a fourth
  kind; whether idle decisions are reported rather than rejected; whether target declarations and
  exclusions are record types beside the kinds; and whether no kind splits. Ruling otherwise would
  add or divide a kind, and the gate would gain a category.
- **Contracts over runtime bounds.** Whether a contract over telemetry facts is how a runtime bound
  in the What is measured. Without it, runtime bounds have no How home.
- **Declared deployments blocking a change.** Whether contract verdicts over declared-deployment
  facts gate landing, while observed facts never do.
- **Specified once.** Whether decisions name no language or platform term, with every per-target
  shape derived from a vocabulary edition. Ruling otherwise would mean per-decision shapes, and
  adding a target would touch every decision.
- **Interface standards.** Whether standards such as HTTP are named in decisions rather than being
  targets.
- **The parts of an import.** The three parts (landing, import decision, acceptance) were written
  as a proposal. A decision on packages names the same three parts, so this may already be
  settled; it needs confirming.
- **Narrow, never alter.** Whether an import may only narrow a decision, with any change recorded as
  a fork.
- **Supersession from a recorded reading.** Whether `explain` shows supersession only from a
  recorded reading of the vendor's list of versions.
- **No orphans as coverage of code.** Whether a no-orphans constraint reads the decisions in force,
  so that code no decision covers is a violation, as the mirror of binding coverage.
- **Coverage, as generalised here.** The obligation (realised, debt or boundary, for every element
  and target) was written as a proposal. A decision on coverage states the same rule, so this may
  already be settled; it needs confirming.
- **How baselines shrink.** The behaviour described for debt is assumed until the authority profile
  defines baselines.
- **Supersession across an import.** Whether nothing in the importer changes when the vendor
  supersedes, with re-import as a new landing, import decision and acceptance. A decision on
  packages states that supersession forces nothing, so this may already be settled.
- **Generation stays additive.** Whether no vocabulary edition may be made check-only. The
  out-of-scope ruling on generation is decided; this condition on editions is not.
- **The form of violation descriptions, the record layout and the fact terms.** All of these are in
  [`how-reference.md`](how-reference.md), and none has a ruling of its own.
- **Platforms as targets, and a freshness bound per contract.** Both were proposed with the
  decisions on targets and on facts, and not ruled separately.
- **New What kinds from adopters.** Whether an adopter may register a new kind of What element, such
  as a new interaction object.
- **Conformance.** Whether "specified and in force", with its six conditions, is the one
  conformance level for the How.

## Where this comes from

For reviewers and auditors. The decisions are in [`core/decisions/`](../../core/decisions/).

| Section | Rests on |
|---|---|
| What the How is | `DDD-dec-54` (the charter's rulings: anchoring, tools never change the How, packages as provenance, force from the authority profile, the gate is Writ); `DDD-dec-42` (only the What moved; delivery and execution retired); `DDD-dec-44` (data conformance is an add-on); `DDD-dec-61` (generation out of scope); `DDD-dec-62` (token `dpp/1`) |
| A How decision | `DDD-dec-49`, `DDD-dec-52` (verdicts computed, never stored; the violation description); `DDD-dec-60` (provenance) |
| The three kinds | `DDD-dec-55`, `DDD-dec-65` (three kinds; "binding" as the word, adopted by Writ); `DDD-dec-57` (design-system and content-store bindings); `DDD-dec-60` (deployment provenance, telemetry). Not settled: the three kinds themselves, and the fourth-kind, idle, record-type, no-split and runtime-bound points |
| Anchoring | `DDD-dec-54` ruling 1; `DDD-dec-55`, `DDD-dec-65` (narrowest covering element; the product node; the advisory warning) |
| Targets | `DDD-dec-57` (design systems and content stores are targets the What declares; its ruling 3 is how `DDD-dec-44`'s "design system and content store are parts of the What" is to be read). Not settled: interface standards, platform targets |
| Specified once | not ruled separately (proposed with `DDD-dec-57`) |
| Packages | `DDD-dec-46`, `DDD-dec-54` ruling 3; `DDD-dec-56` (empty What; decision records only; supersedes `DDD-dec-46`'s "its What is its decisions") |
| Importing a package | `DDD-dec-59` (import, supersession forces nothing, withdrawal). Not settled: narrow-never-alter, recorded readings |
| Coverage and gaps | `DDD-dec-45` (coverage obligations), `DDD-dec-58` (debt, boundary, never a waiver) |
| What the gate checks | `DDD-dec-54` ruling 5 (the gate is Writ); `DDD-dec-60` (facts with provenance; open question; drift); [`apparatus/encode-verify.md`](../../apparatus/encode-verify.md) (ground you do not control is verified on a schedule) |
| Generation | `DDD-dec-61` |
| Conformance | not ruled separately; matches `DDD-dec-51`'s single What level |
| The worked example | `how-examples/README.md`; `DDD-dec-65` to `DDD-dec-71` (the landed versions) |

This text was first written as the answer to the How session's charter and ruled in part on
2026-10-28; the session is `meta/sessions/2026-10-27-product-framework-how/`. Its full earlier text,
including the thesis test, every departure from the proposal, and where the Product Framework's
old §§4–7 went, is at `e5a332d:applications/sdlc/how.md`. The vocabulary that was
`how-vocabulary.md` is now [`how-reference.md`](how-reference.md).
