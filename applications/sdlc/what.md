# The What — what a software application is and does

<!-- ddd:doc
reader: architects, developers and product owners specifying a software product, and the people and agents who build or check software against that specification
act: write a product's What, change it by decision, and hand it to the people and agents who realise it and check against it
pin: v5.15.2
basis: [DDD-dec-41, DDD-dec-42, DDD-dec-43, DDD-dec-44, DDD-dec-45, DDD-dec-46, DDD-dec-47, DDD-dec-49, DDD-dec-51, DDD-dec-52, DDD-dec-54, DDD-dec-55, DDD-dec-57, DDD-dec-58, DDD-dec-63, DDD-dec-64, DDD-dec-73, DDD-dec-85, DDD-dec-86, DDD-dec-113]
status: current
supersedes: 84aa466:applications/sdlc/what.md
-->

Use this when you are about to build, change or take over a piece of software and need one place
that says what it is and does, before anyone decides how to build it. After reading it you can
write down a product's What (its domains, its systems, and the behaviour and screens they carry),
change it by decision, and hand it to the people and agents who realise it, with an executable
oracle they can be checked against.

**How settled this is.** Decided throughout, except one point marked *(open)* in §3.2.2. The
document was moved here from the Product Framework and rewritten against the rulings on the move.
It was ratified when its pull request merged.

**How to read it.** To write or change a What, read §1, §2.1, §3, §4 and §5. Tool builders and
anyone implementing a checker or a conformance runner also need §2.2–§2.3 (identity and hashes),
§6 (the conformance wire) and §7 (encoding and the validation regime). Passages set as quotations
are the Product Framework's own words, kept where the rulings leave them right. Each section's
source is in "Where this comes from" at the end.

**The worked example** is a small shop, Acme Shop: one domain, Ordering, and two systems,
`shop-api` and `shop-bff`. Customers place orders and refund them, and staff see every order.
`shop-bff` targets the web, as a GUI.

**Companions.**
- The vocabulary is [`what/ontology.ttl`](what/ontology.ttl), sdlc edition 1.
- The constraints are [`what/shapes.ttl`](what/shapes.ttl).
- The worked example is [`what/examples/acme-shop.ttl`](what/examples/acme-shop.ttl), the How
  test product's What, with its later versions [`acme-shop-4.ttl`](what/examples/acme-shop-4.ttl)
  and [`acme-shop-5.ttl`](what/examples/acme-shop-5.ttl). The last carries no findings.
- [`what/check.py`](what/check.py) runs the shapes, the identity form and the hash law over the
  examples, and checks the hashes against [`what/vectors.json`](what/vectors.json),
  [`vectors-4.json`](what/vectors-4.json) and [`vectors-5.json`](what/vectors-5.json).
- The wire schemas are in [`what/conformance/`](what/conformance/).
- The How that realises a What is [`how.md`](how.md).

---

## 1. Scope, and what this rests on

### 1.1 What the What is

The What is the opinionated specification of what a software application is and does. A system
is not a coordinate of any act. It is ground and tolerance: "the specification that says how a
given piece of software should work". The What as a whole is the software's declared ground, over
which decisions are made, and the tolerance each act must meet. Step 1 of the method reads its
addresses off the What instead of inventing them.

### 1.2 Not here

| Not here | Where it is |
|---|---|
| The How: how the What is realised in code and deployments | [`how.md`](how.md) |
| Delivery: features, releases, `done`, versions, direction, drift | retired, not carried |
| Work units, seams, verification as a process | retired. The gate is Writ |
| Two Pillars conformance | dropped. This repository consumes canon by pin |
| Data conformance | an add-on that reads the What, outside the framework |
| Force: the genesis grant, grants, acceptance, baselines, waivers | the genesis grant and the authority profile, [`authority.md`](authority.md) |
| Catalogues: components, tokens, strings | packages with their own genesis |
| The §4–§7 classes of the old `pf:` ontology | not carried in any namespace. The `pf:` namespace ends with this move |

### 1.3 The rulings this rests on

Each line is a rule this document applies. The decision behind each is in "Where this comes from".

- Only the What moves here. How and Delivery are retired, and Two Pillars is dropped. This
  repository is the What's home.
- Every decision anchors to a What element or to the product. Every change of the What is a
  decision.
- Tools never change the What. Everything gathered is signed by a human principal.
- The design system and content store are targets the What declares. Their catalogues are
  packages. The bindings are How.
- Reification and content coverage are obligations. Their content is decisions.
- Authoring scopes are central, and instantiate the genesis grant over a product.
- Verdicts are computed, never stored. What is recorded is the declaration and the ground
  reading.
- Encoding is cut down to one graph and stable identity, and conformance to one level.
- The identity form is §2.2–§2.3.
- Subjects and authorization (§3.7) are taken from the Product Framework's v1.11.0, with
  `SubjectKind` and `subject` for its actor terms, and no `pf:` term.
- Edition 1 is completed for its tag: the validation regime, violations and warnings, the five
  §3.4 and §3.7 checks, the description checks, a context mapping's direction, and
  `acme-shop-5.ttl`.

---

## 2. The What as decisions, and its identity

### 2.1 The What changes only by decision

- **A decision is not a What element.** Each decision anchors to the What element it governs.
- **Every change is a decision.** The What changes only through decisions anchored to the
  elements they change. A What element's current form is the result of the decisions anchored to
  it, and the What's history is its decision history.
- **Gathered material is a proposal.** Tools and processes where parts of the What already live
  are valid sources. What they supply is a proposed change, and it enters the What only when a
  human principal signs and accepts it (§5).

**Anchoring a decision that creates elements.** "A decision that creates elements anchors to the
narrowest element that exists at the position it is proposed and covers every element it creates;
for a new domain that is the product, which is the empty-What case and not a loophole". An element
being created does not yet exist at that position, so it is never its own creating decision's
anchor. This is the How's anchor rule (how.md §3) applied to the What.

### 2.2 Identity

Nothing in an identity carries meaning.

- **The product.** The product IRI P is named in the product's genesis record and is stable across
  genesis transfer. P is itself the product node, the root of the What.
- **Elements.** Every other element is `P/what/<key>`. The key is a ULID minted when the element
  is created ([`what/mint.py`](what/mint.py)), and it is never changed or reused. The IRI encodes
  neither kind nor position.
- **Names.** The human name is `rdfs:label` and changes by decision. Resolving a key to its name
  is `explain`'s job.
- **What keeps identity.** A rename, a property change or a move happens under the same IRI. A
  kind change, a split or a merge makes new elements, linked to the old ones by
  `sdlc:succeeds`. Baselines are not carried over.
- **Elements and descriptions.** An element is any node referred to by identity, and it is
  always an IRI. Blank nodes are allowed inside an element's description (lists, payload
  bindings, scope keys). A blank node belongs to exactly one description.

**Containment.** The one containment edge is `sdlc:within`. Every element but the product node
is within exactly one element, and a subtree is `within*`. It replaces the old `in_context`,
`owns_domain`, `owns_system`, `system_of`, `journey_of` and `bounded_by`, with no typed
sub-properties. One edge makes "the subtree an anchor covers" a single transitive walk, which is
what the How's anchors read (how.md §3). The relation's name is carried by the kind pair and
enforced by the shapes. A reader that needs ownership versus attachment reads the kinds.

**What is an element.** Interactions, fields (attributes, payload fields, view fields and
claims), state annotations, content keys and scenarios are elements, not the blank nodes
product-cli made of some of them. Anything a binding, a baseline, `reads`, a scope key or a wire
request names is an element with its own IRI. Blank nodes are only where nothing names the node.
A binding anchors to an interaction or a content key, a Decider reads a field, and a scope key
compares two fields. The cost is that adding a field is a What decision, and that is the correct
cost: a wire contract changed.

### 2.3 Versions of the What

- **The record.** A What-version is a `dpp/1` record. It pins every What decision in force and
  lists every element by IRI and element hash.
- **The canonical form** is RDFC-1.0 over RDF 1.2 canonical N-Quads. Language tags are lowercase,
  and ECHAR and UCHAR escapes are as Varve writes them. A graph is canonicalised alone, never across
  named graphs, and a triple term never holds a blank node.
- **The element hash** is taken over the element's description, canonicalised on its own.
- **The graph hash** is taken over the whole canonical graph.
- **Authored logic.** A Decider's logic and a Projector's fold are artefacts carried by
  `sdlc:logic` digest, so both hashes cover them.
- **Equalities.** Equal graph hash means the same specification. Equal record hash means the same
  specification reached by the same decisions.
- **No force.** A What-version confers none. Force stays with the decisions it pins.

**The ontology is never hashed.** A What graph's hash and its export cover the What graph alone,
never the edition's `ontology.ttl`, which a validation merges in (§7.2).

The examples' hashes are in `what/vectors.json` (`acme-shop.ttl`, `what@1` to `what@3`),
`what/vectors-4.json` (`acme-shop-4.ttl`, `what@4`) and `what/vectors-5.json` (`acme-shop-5.ttl`,
`what@5`). The first two graphs are pinned by published records and never change.
`what/check.py` computes them with pyoxigraph, which conforms to the canonical form on every
vector in `what/canonical-form-vectors.json`. pyld (URDNA2015 over RDF 1.1 N-Quads) does not
conform: it keeps uppercase language tags and mis-escapes controls. It serves only as a
cross-check on graphs where it cannot diverge. A conforming second implementation, from Varve's
published vectors, is still to come. Recorded since: product-cli's slice 0 admission test found
Varve `0.1.0-preview.15` reproducing `acme-shop.ttl`'s graph hash. product-cli's element-hash
vectors, when they come, are a further cross-check, not a substitute.

---

## 3. The What — structure and behaviour

> The What is the specification every role reads and agrees on. It is organised by a three-level
> ownership hierarchy that fixes *where each part lives* and *what is shared* — so that several
> surfaces of one product draw on the same concepts and the same rules rather than re-deciding
> them.

**Product → domains and systems.** The product owns one or more domains and one or more systems.
A system references whole domains. It does not own them.

> The dividing line is a single principle: **the domain owns meaning and rules; a system owns
> surface and journey.** … The decisive test: **if two systems would disagree about it, it is
> system-level; if they must agree, it is domain-level.**

In the graph, ownership is `sdlc:within`. Domains, systems, journeys and product-wide quality
demands are within the product node. A system's use of a domain is `sdlc:referencesDomain`.

*In Acme Shop:* the domain Ordering and the systems `shop-api` and `shop-bff` are within the
product node, and each system references Ordering.

### 3.0 The product and its boundary

The product node "carries little of its own — a name and purpose — because its job is *ownership
and boundary*, not behaviour". Its product-wide concerns are:

- product-level quality demands (§3.6);
- journeys (§3.0.1);
- product-wide content keys and declared targets, where a design system or content store serves
  every system.

The direction the product is moving toward is not carried. Direction was Delivery.

> The product's boundary is exactly the set of domains and systems it owns. A second product is a
> second root: it may *reference* a shared domain across a declared boundary (the Translation
> pattern, §3.2.0, is how its systems would communicate), but it does not absorb it.

A second product is a second genesis, with its own P.

#### 3.0.1 Journeys — flows that span systems

A journey is "a **product-level, derived composition**: a declared path through single-system
flows, linked at their crossing points, where **every crossing is a Translation**". It composes
flows (`sdlc:composesFlow`) and crosses through automated triggers of Translation patterns
(`sdlc:crossesVia`). It owns nothing. The rules carry over unchanged:

> - **Every crossing is a Translation, or it is a finding.** …
> - **A journey references; it does not contain.** … Remove a journey and nothing else changes …
> - **Systems stay independent.** …

Blast radius stays: it is a traversal of `sdlc:within` and the edges below. Value-anchoring went
with Delivery.

### 3.1 The domain model — structure and reference data

A domain is "the home of *meaning and rules*: the shared definition of **what concepts mean**, how
they relate, and **how they behave**". Within it sit:
- bounded contexts, and in them entities, value objects, relations and invariants;
- the event model: commands, events, views, Deciders and Projectors (§3.2–§3.4);
- subject kinds (§3.7).

**Structure.**

> - **Bounded contexts, not one flat model.** Within a context a term has exactly one meaning
>   (the **ubiquitous language**); the same word may mean different things in different
>   contexts. Cross-context correspondences are **explicit declared mappings**, never assumed.
> - **Entities, relations, value objects, invariants.** Relations carry cardinality **and
>   rationale**. Invariants are stated as machine-checkable constraints. … an aggregate holds
>   *exactly its invariant-bearing state* — what its Deciders must read at decision time — and
>   everything else a screen wants is a Projector's output, not a stored field (§3.4).
> - **Machine-readable, with a constraint language.** The model must be expressible as a graph
>   with validatable shapes (RDF + SHACL is the reference; an equivalent is conformant).

**Every box says what it is.** An entity carries a business-language `sdlc:definition`, and so do
a bounded context and a subject kind. A domain states its `sdlc:purpose`, as a system does. The
bounded-context, subject-kind and domain checks are warnings, because they were added after the
examples were pinned (§7.2).

**A context mapping has a direction.** A mapping names the concepts it connects with
`sdlc:mapsTo`. When it also names one with `sdlc:mapsFrom`, it has exactly one `mapsTo`, and it
reads: the concept in `mapsFrom` corresponds to the concept in `mapsTo`, and `mapsFrom`'s meaning
is the source. A mapping without `mapsFrom` is a warning, "direction undeclared". DDD's strategic
pattern kinds (Customer–Supplier, Conformist, Anticorruption Layer and the rest) are not What:
they describe teams or realisation, not meaning, and belong in the How.

An entity's attributes are `sdlc:Field` elements within it. Their types come from the single
datatype vocabulary: string, integer, number (`xsd:decimal`), boolean and date (the source's datatype list).

*In Acme Shop:* the entity `Order`, in the Ordering bounded context, has the fields
`customer_id`, `paid_total` and `refunded_total`, and the invariants "order has lines", "refund by
owner" and "refund within paid".

**Reference data is What.**

> Some instance data is *constitutive* — the system's behaviour is undefined without it: the set
> of valid shipping methods, the tax categories, the product taxonomy, the currencies accepted.
> This is **reference data**, and it lives in the What …

The test carries over: "If changing a datum changes what the system *means* … it is reference
data … If it is just more rows of the same kind … it is production data".

**Production data is not What, and data conformance is not framework.** The source's three
callouts on data conformance (reading both ways, asserted continuously, the data-divergence rate)
describe a data-conformance profile. That profile is "a value add on not something thats part of
the framework". An add-on that reads the What may check production data against its shapes.
Nothing here depends on one.

### 3.2 The event model — behaviour

> The description of **what happens over time**, peer to the domain model, in the same graph.

- **Built from domain-typed primitives.** "Behaviour may not reference structure that does not
  exist": every event changes a real entity, and every command targets one.
- **State space.** A view declares its state space: `present`, plus any of `loading`, `empty` and
  `failed` it can exhibit (`sdlc:hasState`).
- **Proportional depth.** "Concepts with rich or historical behaviour get full event models;
  simple create/read/update/delete concepts get a minimal one or none".

#### 3.2.0 Building blocks and patterns

The four blocks are Trigger, Command, Event and View. They compose into four patterns:

| Pattern | Shape |
|---|---|
| **Command** | `Trigger → Command → Event(s)` |
| **View** | `Event(s) → View` |
| **Automation** | `Event(s) → View → Trigger(automated) → Command → Event(s)` |
| **Translation** | `Event(s) [system A] → View → Trigger(automated) → Command → Event(s) [system B]` |

Their rules carry over:
- an automated trigger "contains no business logic";
- a Translation's read side "reads events from exactly one source system", and its write side may
  fan out.

**A trigger's source and its subject.** A trigger has exactly one **source** (`user`,
`external`, `automated`). Its source is the **channel**, and it "stays three-valued because the
patterns are checked by it". *Who* acts through the channel is a separate edge, `sdlc:subject`:
the subject kind the trigger acts as. The source called this edge `acts_as`. The subject's nature
must be one the source admits: `user` → human, `automated` → process, `external` → external.

*In Acme Shop:* the triggers for Place order and Refund order have source `user` and act as the
subject kind Customer.

**Payload schemas.** A Command or Event "MAY declare a **payload schema**: a list of named
fields, each optionally typed from the datatype vocabulary". "With one system a payload is a
private convenience; between two systems … it is a **public wire contract** and must be authored,
not guessed." Payload fields are `sdlc:Field` elements within their Command or Event. Their order
is an RDF list (`sdlc:fieldOrder`) inside the owner's description.

**Slices.** "A single pattern instance on the graph is a **slice**: the smallest coherent unit that
can be handed to an implementer". A flow is a chain of slices. The old identification of a slice
with a work unit, and the containment *feature ⊇ flow ⊇ slice*, went with Delivery and work
units.

#### 3.2.1 The UI step — the What of a screen

> A **UI step** is the point in a flow where a person sees something and acts. It is **What**,
> owned by product and design: it says what a screen is *for* and *means*, never how it looks.

**The split between meaning and widget is a type.** "A UI step may reference only **Abstract
Interaction Objects** … never a concrete control … from a design system". Each interaction of a
step is an `sdlc:Interaction` element within it, typed as exactly one AIO. It surfaces one
projection, offers one command, or enters one payload field. A concrete control is not a What
term at all. It is a design-system target's vocabulary, and the AIO-to-CIO choice is a How
binding anchored to the interaction (§4).

**The buildable core.** These are derived, not authored:
- **intent**, the marked debt (below);
- the **information shown**: projections, through display AIOs;
- the **actions available**: commands, through action or input AIOs;
- the **transitions**: `navigate` edges of the page graph.

**Offered to.** A step is **offered to** one or more human subject kinds (`sdlc:offeredTo`). This
is "system-level, because the admin tool and the shop offer the same command to different
principals".

**Modelled meaning.** These are checkable elements, not prose:
- **emphasis**;
- **projection states as meaning**: a step "may annotate only states the projection actually
  has … and it must give a meaning to *every* state the projection can be in, or explicitly
  waive one with a reason". Each is an `sdlc:StateAnnotation` within the step;
- **accessibility obligations** (§3.2.3);
- **content references**: a step references `sdlc:ContentKey` elements with a declared role,
  "never written as literal strings in the UI step". The words are not the What's (§4).

**Intent is specification debt.** This is carried as written:

> **Whatever intent was used to decide must be promoted into the model.** … Intent therefore
> shrinks monotonically toward a pure statement of purpose … the **intent-reliance rate** — how
> often realising a screen required consulting intent to settle something the model did not
> determine.

The rate is a What-side signal, and stays one. The source's list of what intent is promoted into
included "a missing reification rule". The reification rule is not the What's. What is promoted
into the What is the missing AIO, context of use, or meaning declaration. A missing reification
is a missing binding, which is debt on the How's coverage (how.md §8).

#### 3.2.2 Abstract Interaction Objects and the context of use

> **An AIO is meaning, not a widget.** `single-select` means "choose exactly one from a set"; it is
> *not* a dropdown, a radio group, or a segmented control — those are the concrete forms it can
> take.

**The base set.** Ten AIOs are framework vocabulary (`sdlc:aioTriggerAction` … `sdlc:aioEdit`),
not What elements: `trigger-action`, `single-select`, `multi-select`, `text-entry`,
`numeric-entry`, `date-entry`, `display-value`, `display-collection`, `navigate` and `edit`.
"Input AIOs derive their shape from the domain model": an input interaction enters a command
payload field, whose type and allowed values come from the domain. *(open)* Whether an adopter
may register AIOs, as the source allowed, is how.md §6's open question. Under this ontology a
registered AIO would be a vocabulary change in this repository, not a What element.

**The context of use is a declared model.** A system declares its contexts of use
(`sdlc:ContextOfUse` elements, each a value of one dimension: platform, form factor, modality,
terminal capability). "Platform is a context dimension like any other". "iOS, Android, or both" is
which platform contexts a system targets. "Context-of-use is What-side knowledge … but it carries
no realisation." It is what the How's bindings are written against (§4).

**The interaction class gates the other dimensions.** GUI brings form factor and pointer or
touch. TUI brings terminal capabilities and rules form factor out. A system declares the classes
it targets (`sdlc:targetsClass`). "The AIO vocabulary itself does **not** change across classes".

*In Acme Shop:* `shop-bff` targets the class GUI and one context of use, `web`, on the platform
dimension.

#### 3.2.3 Accessibility as ingested criteria, not prose

> The normative reference is **WCAG 2.2**, version-pinned; an instance ingests its structure
> from the W3C machine-readable source … These are referenceable nodes, not authored text.

A step or an interaction `sdlc:mustSatisfy` a criterion by its W3C IRI. Criteria are not What
elements, and nothing is re-minted under P.

- **Inherited and added.** Obligations are inherited from the AIOs a step uses, plus the criteria
  the step adds. The step's obligation is the computed union.
- **Verification type.** Each criterion carries one: machine, assisted or manual. "A conformant
  accessibility verdict therefore states a **conformance level and its basis** … and never a bare
  'accessible: true'".
- **Attestations.** A manual criterion is discharged by an attestation, "a dated, attributed
  assertion that a named criterion was evaluated and met". Here an attestation is a signed record
  and a ground reading. It is not a stored verdict. How it is held is the authority profile's.

#### 3.2.4 The page graph — navigation as one graph

> Navigation is not a separate "shell" layered above the screens; it is **one graph whose nodes
> are pages (UI steps) and whose edges are `navigate` transitions.**

- **Flows.** A flow is a named, connected subgraph with an entry page (`sdlc:Flow`,
  `sdlc:entryPage`, `sdlc:inFlow`).
- **The root.** Each system has a root (`sdlc:SystemRoot`), whose out-edges are the global
  destinations.
- **"Top-level" is derived**: a page has an inbound edge from the root. It is never a tag.

#### 3.2.5 The system — what is being described

A system is a surface: one way the product is used. It carries:
- a name (`rdfs:label`);
- a kind (`sdlc:systemKind`: application, website, service, CLI, …);
- a purpose;
- the whole domains it references;
- its target contexts and interaction classes;
- the targets it declares (§4).

It owns its page graph, its flows, its UI steps and its triggers. "A flow belongs to exactly one
system; the behaviour it invokes is shared by all systems referencing that domain".
System-specific quality demands are within the system (§3.6).

> **System identity is What; deployment identity is How.** … The What says "Acme Shop is a
> consumer e-commerce application, referencing the Ordering and Catalog domains, targeting iOS,
> Android, and web"; the How says "iOS bundle `com.acme.shop`, web served at `shop.acme.com` from
> these runtimes."

That quotation is the source's illustration, not the worked example, whose one domain is
Ordering and whose `shop-bff` targets the web.

The How's side of this line is how.md §4.2: a target declaration binds a deployable unit to the
system, and a contract states what the unit must satisfy.

### 3.3 The Decider — the executable form of behaviour

The signature is the source's v1.11.0 one:

```
decide(state, command, subject) -> Accepted[events] | Rejected[invariant]
evolve(state, event)            -> state
```

> In business terms. A Decider is where the **business rules** live — but it is more than the
> rules. The rules are its *rejections* … and a Decider also says *what results* when a command
> is allowed (the events it emits).

**The subject is an input, not a payload field.** The subject "is the authenticated principal
issuing the command — its actor kind and its claims — **supplied by the system's authentication,
never by the caller**". Here it is the subject kind and its claims.

**The signature is derived, and only the logic is authored.**
- The Decider decides for one aggregate.
- It handles exactly the commands that target that aggregate.
- It may emit only events its handled commands are declared to emit.
- It evolves from the events that change the aggregate.
- Its rejections are the aggregate's invariants, plus rejections over the subject's claims.
- Its subject alphabet is the subject kinds its commands are offered to or issued as.

The logic is an artefact held by digest (`sdlc:logic`, §2.3).

*In Acme Shop:* the Decider `Order` decides for the entity `Order`, handles Place order and
Refund order, and rejects with the entity's three invariants.

**The conformance rules.**
- **No foreign commands.**
- **Command coverage.**
- **Output-alphabet containment.**
- **Subject coverage** (the source's actor coverage): "for every (command, actor kind) pair in its
  alphabets, the Decider either accepts the command for that kind or has a reachable rejection
  over its claims, and a scenario per pair shows which".

**The wire scalar alphabet.** Values are `boolean`, 64-bit signed `integer` and `string`. A
`number` or `date` field "travels **as a string** on the conformance wire … until the alphabet is
extended". "One list-valued position is admitted now, and only one: a **set-valued claim** …
travels in the actor block of a conformance request as an array of wire scalars". Here that block
is the subject block (§6).

**Scenarios.** "Before realisation, the Decider is *simulated* against scenarios drawn from the
flows (a flow gives a *given* of prior events, a *when* command, and a *then* of expected events)".
A scenario is an `sdlc:Scenario` element within its Decider or Projector. Its given and its
expected emissions are RDF lists inside its description. Its *when* names the subject it is
issued as.

**What this imposes on the How.** The source said that the realised code "must keep its decision
logic in a pure core", stated as a contract. Here that is a How binding over Deciders (how.md,
`PURE@1`). The What states only the oracle: the Decider, its logic and its scenarios.

### 3.4 The Projector — the executable form of a read model

```
project(state, event) -> state          -- the read-model fold
```

The Projector is "**symmetric to the Decider in every respect**":
- its signature is derived;
- only the fold is authored;
- it is simulated before realisation;
- it is the oracle for its View.

Its rules are **no foreign events**, **event coverage** and **output containment**.

> **The actor is not an input to the fold.** … `project` keeps its signature — no actor argument
> — and **one fold serves every actor**; the scope is a selection applied at the seam over the
> fold's output. … a Projector over a scoped View declares the field(s) its fold is **keyed by**,
> and every field a scope key reads must be one of them.

`sdlc:keyedBy` names those fields. "Actor" there reads "subject" here.

**State justification and Decider justification.** Both carry over as written. "A field belongs
on an aggregate if and only if some Decider reads it", and "a Decider must have **at least one
reachable rejection**". Each is a finding that points at an unmodelled invariant. Their v1.11.0
twin, **claim justification**, joins them (§3.7). These are What-side checks, and all are in
`what/shapes.ttl` as warnings (§7.2): Decider justification on `DeciderShape`, state
justification as `StateJustificationShape`, and the Projector's event coverage as
`ProjectorEventCoverageShape`.

### 3.5 Named-algorithm primitives

Some computation is named rather than derived: a standard or algorithm the What refers to instead
of specifying step by step. The section has no subtitle. "Floor" is canon's word, so the source's
old subtitle, "the Polanyi floor", is not carried.

> A computation is mechanically derivable from spec **exactly to the degree its variability is
> declared data over a generic interpreter.**

A named-algorithm primitive (`sdlc:NamedAlgorithm`) is specified by **reference** (the algorithm
or standard it implements), by an **I/O contract** in the domain's terms, and by an **oracle** of
reference input and output pairs, held by digest. It is "explicitly **exempt from derivation and
from behavioural simulation**". The source checked it by oracle conformance. Here that check is a
How binding over primitives, and the What carries the oracle. "An undisclosed algorithm
masquerading as a mechanical projection is the dishonesty the [primitive] exists to prevent".

### 3.6 Quality demands — the non-functional, made checkable

> **a quality demand is never prose.** … Admitted into the spec, a quality demand is one of
> exactly **two kinds**, distinguished by *how it is checked*.

| Kind | Is | Its How side |
|---|---|---|
| **Runtime bound** (`sdlc:RuntimeBound`) | a bound measured against telemetry: latency, throughput, capacity, uptime. It declares its bound and its measured source | the measurement wiring is a contract over `telemetry` facts, anchored to the bound (how.md §4.2) |
| **Architectural constraint** (`sdlc:ArchitecturalConstraint`) | a constraint on the realisation: residency, security posture, fault-tolerance topology | a contract anchored to it, held at build time (how.md §4.2; `RESID@1`) |

> **The test that keeps demands honest.** … *is it checked by measuring production, or by
> inspecting the realisation?* … If *neither* can confirm it, it is not a quality demand yet — it
> is prose, and prose is debt.

**Demands are located, not listed.** A demand is within the element it scopes:
- the product, for product-wide demands such as a residency rule binding every system;
- a system;
- a flow, a step, a Decider or a Projector.

The source said the second kind "binds to the **How**". Here, the How's contract anchors to the
demand, and the What holds only the demand.

### 3.7 Subjects and authorization — who may act

The source's v1.11.0 section is adopted, with **subject kind** for its "actor kind" and
**subject** for its `acts_as`. Of the three available words, "actor" is canon's, "principal" is
authority's, and "subject" is what OIDC calls the authenticated identity whose claims these are.
The claims are the point.

**Two authorities, never one.** The source makes this split, and it fits this repository's rulings
exactly:

> This section is about the *product's* authorization: who may act **in the product being
> specified** (a customer cancelling an order). It is not about authority **over the
> specification** — who may accept a decision about the product, sign a version, or ratify an
> act. That second authority belongs to whatever governance tooling holds the specification,
> never to the specification's own vocabulary.

Here, the second authority is the genesis grant and the authority profile. A subject kind is never
a grant. A grant is never a subject kind. A specification's author does not become a subject of
the product.

**Authentication is How.** Which identity provider authenticates a subject, how a session is
held, and what a token looks like are realisation. The binding of a subject kind to a provider is
declared per deployment. In the How it is a contract over the deployable unit (how.md §4.2). The
What never names a provider. The source's **provider coverage** check therefore belongs to the
How.

**Authorization splits by the framework's own test.**

| Authorization fact | Level | Lives on |
|---|---|---|
| who the kinds of subject are, and what each carries | domain | a **subject kind** (`sdlc:SubjectKind`, within a domain) and its **claims** (`sdlc:Field` elements within it) |
| a rule over who may change what ("only the order's customer may refund it") | domain | a **Decider rejection** that reads a claim (§3.3) |
| what each kind of subject may see of a View | domain | the View's **scope**: one `sdlc:ScopeRule` per subject kind |
| which kinds of subject a screen or trigger is offered to | system | `sdlc:offeredTo` on the step; `sdlc:subject` on the trigger |

**The subject kind.**
- **Nature.** It has exactly one: `human` (acts through a UI step), `process` (through an
  automated trigger) or `external` (an outside system through an API call). Nature is a closed
  vocabulary, "*not* a role".
- **Claims.** It carries typed claims. A claim may be set-valued, and may draw its values from
  reference data.
- **Role or kind?** "The framework ships **no actor kinds and no roles**." One test decides
  between a kind and a claim value: "if a surface is offered to it, it is an actor kind; if only a
  rule reads it, it is a claim".
- **Delegation** (an external system acting for a human) is not modelled. Until it is, it is an
  external subject kind whose claims carry the delegating principal.

**Read-side authorization is a View scope.**
- **Public or scoped.** A View is public, or it is scoped by rules, one per subject kind. A rule
  is a conjunction of keys, each comparing a view field with a claim (`equals`, or `member-of`
  for a set-valued claim).
- **Defaults.** A rule with no keys is a declared "every row". A subject kind with no rule on a
  scoped View sees nothing: deny by default.
- **The fold is unchanged.** The scope is applied at the seam, over the fold's output. "Every key
  field is a key of the fold".
- **Cross-row aggregates** are folded keyed by the scoping dimension.
- **A disjunctive scope** ("mine, or shared with me") is modelled as a recorded fact and a View
  keyed on it.

*In Acme Shop:* the subject kinds are Customer and Staff, both within the Ordering domain. The
View `Order summary` is scoped by two rules, "customers see their own orders" and "staff see
every order".

**The checks.** They bind once a What declares at least one subject kind. A What that declares
none has authorization that is "*unstated*, not *absent*".

| Check | Twin of | Holds |
|---|---|---|
| **Subject coverage** (the source's actor coverage) | command coverage | every step that offers or surfaces something is offered to at least one human subject kind. Every automated or external trigger acts as one. Every (command, subject kind) pair has a scenario showing acceptance or a reachable rejection |
| **Scope coverage** | — | every surfaced View is public, or has a rule for every subject kind its step is offered to. Every claim a key reads belongs to the rule's subject kind. Every compared view field is a key of the fold |
| **Claim justification** | state justification | a claim no Decider reads and no scope uses is dead, or the trace of an unmodelled authorization rule |

`what/shapes.ttl` carries all of it:
- subject coverage: the step half (`SurfaceCoverageShape`), automated and external triggers
  (`TriggerSubjectCoverageShape`), and a scenario per (command, subject kind) pair
  (`PairScenarioCoverageShape`);
- the source–nature agreement on triggers (`TriggerShape`);
- the three scope-coverage rules (`ScopeRuleShape`, and `ScopedViewShape` at the seam);
- claim justification (`ClaimJustificationShape`).

The coverage and justification checks are warnings: each finds what is not yet modelled, not a
malformed element (§7.2).

---

## 4. Declared targets, and the obligations on the What

### 4.1 The What declares its targets

A design system and a content store are targets the What declares, "exactly as it declares iOS".
A system, or the product for every system, declares:

- its **platform contexts** and **interaction classes** (§3.2.2);
- a **design system** at an edition: an `sdlc:DeclaredTarget` with `targetKind` `design-system`
  and `sdlc:edition`, a `dpp/1` reference to the target's vocabulary-edition record;
- a **content store** and the **locales** it serves: an `sdlc:DeclaredTarget` with `targetKind`
  `content-store`, its edition, and one `sdlc:locale` per BCP 47 tag.

There is one kind, `sdlc:DeclaredTarget`, for both. Its edition reference may not resolve from
this product. That is the protocol's "not reachable", and it is Writ's `explain` to resolve, not a
check the What's own checker requires.

The catalogue (components, tokens, strings) is the target's vocabulary edition, in a package with
its own genesis, typically a design team's. "Nothing in a catalogue is a What element of the
product that uses it". So `pf:DesignSystem`, `pf:ContentStore`, `pf:Cio`, `pf:Token` and
`pf:ReificationRule` are not carried. The How's vocabulary has the target kinds
(`sdlc:DesignSystemTarget`, `sdlc:ContentStoreTarget`, how-vocabulary.md).

### 4.2 The obligations

Reification and content resolution enter the What "as obligations, not content". The framework
"ships obligations, never widgets or words".

1. **Reification exists.** For a declared design-system target, `reify(AIO, context) → CIO` is
   defined: each interaction in each context of use its system targets resolves to a concrete
   interaction object of that target.
2. **Reification coverage.** Every (interaction, context) pair a system can reach is covered or
   declared unreifiable. The pairs are computed from the What: the system's interactions, and its
   contexts within each declared interaction class.
3. **Content coverage.** Every (content key, locale) pair resolves or is declared missing. The
   pairs are computed from the What: the keys the system's steps reference, and the locales its
   content-store target declares.

**Where the content lives.** The content of each rule (which CIO, which words) is a How binding
anchored to the interaction or the content key. Coverage of those bindings is how.md §8:
- a pair that should be realised and is not yet is a baseline entry, which shrinks under the
  ratchet ("declared missing");
- a pair that cannot apply is an exclusion decision with its reason ("declared unreifiable");
- a waiver never covers a coverage gap.

The What states the pairs. The How states the bindings and their gaps. Neither holds the other's
part.

---

## 5. Authoring scopes — who can change what

Authoring scopes are "a central part of the framework, who can change what, and who helds the
genesis grant for a given product". They instantiate the genesis grant over a product. Tools never
change the What, and everything gathered is signed by a human principal.

### 5.1 A scope is a grant over What element kinds

Force, grants and acceptance are the authority profile's ([`authority.md`](authority.md)). This
section states what a scope ranges over, which is the What's to say. It also states the one rule
on scopes that the profile inherits rather than chooses: the multi-scope rule, below.

- **The genesis grant** is unscoped within the product. It covers every element kind, everywhere
  under P.
- **A scope** is a set of What element kinds (classes of `what/ontology.ttl`), optionally
  narrowed to the subtree of one element (`sdlc:within*`). A grant delegating from the genesis
  carries a scope. An acceptance of a What decision is valid only if every element the decision
  creates, changes or retires is of a kind in the grant's scope, inside its subtree.
- **A decision spanning scopes** needs a valid acceptance under each scope, from the same holder
  or different holders. It is in force only while all of those acceptances are live. This is
  Writ's conjunction for scopes, the same shape as derived acceptance for blends. The authority
  profile inherits it and does not choose otherwise.
- **The kind vocabulary is the ontology.** The source carried its kinds "as a parallel list
  pending expression as direct references into the sections above". Here they are those
  references: a scope names `sdlc:UIStep`, `sdlc:Interaction`, `sdlc:ContentKey` and so on. A
  scope introduces no ontology of its own.
- **Derived kinds** are in no scope. "Some kinds are **derived, not authored** — a read model's
  state space derives from the projection's shape … no tool is its author". Equally, no grant
  authorises authoring them.
- **Kind is immutable** (a kind change makes new elements, §2.2), so a scope's boundary cannot
  be crossed by reclassifying an element.

The profile carries the multi-scope rule as inherited, and it states how the kinds a decision
touches are recorded at signing ([`authority.md`](authority.md) §3.1, §4.2). The acme example's
`CUR@1` touches kinds in both scopes and is accepted under each (authority.md §9).

The product owner's What scope and the architect's How scope are two grants over two sets of
kinds of one product. That is Writ's "two grants over two subgraphs of the same log".

### 5.2 Gathering — tools as sources, never as authors

The source made a tool a "bounded co-author" whose in-scope content "is accepted into the What".
That is reversed. A tool is a **gathering source**. Its material is a proposed What decision, and
it enters only when a human holder of a grant whose scope covers it signs the acceptance.

What survives of the source's authoring-scope chapter, rewritten:

- **The gathering declaration.** Each source declares the kinds it may supply material for, each
  with a completeness (`sufficient` or `partial`) and a channel (how the meaning is carried). It
  also declares an explicit **excluded** list. These are the source's `authors` and `excluded`,
  renamed. A declaration grants nothing. It only bounds what the source may propose.
- **The enforcement oracle.** "Out-of-scope content is rejected, the basis naming the scope
  violation — a Decider authored in Figma is rejected *because Figma is not a sanctioned author of
  Deciders*, not because the Decider is wrong". Here: such material is never even proposed.
- **The gap split.** "`unauthored-within-scope`: the tool *could* author this and didn't" and
  "`outside-scope`: no work in this tool can author this — **route** to a sanctioned author".
  These are kept as findings that route work.
- **The completeness join.** A What is complete when every required kind is covered. A join
  across gathering sources and grants reports each required kind as covered (and by whom),
  coverable but ungathered, or uncovered. Coverage now has two halves: a source that can supply
  the kind, and a grant holder who can accept it.

**The symmetry.** "Authoring scopes are the **top** of a symmetry whose bottom is reification".
Here the top is grants over kinds, which say who may change what. The bottom is the How's
coverage (how.md §8), which says what is realised where. Both are bidirectional joins over one
authoritative What.

---

## 6. The behavioural-conformance wire

The source's conformance wire moves with the What, at v1.11.0. It is the What's because it is how
anyone claims that a realisation computes what the What's Deciders and Projectors say. It is the
oracle's interface, not a verification process. This corrects how.md Appendix B, which had it as
"not carried".

> A **conformance runner** is any process that reads a JSON array of requests on stdin and writes
> a JSON array of outcomes on stdout, one per request, in order, exiting 0. Payload values are
> drawn from the wire scalar alphabet (§3.3).

**Decision requests.** There is one per Decider scenario:
`{ "given": [EventRef…], "when": CommandRef, "subject"?: SubjectRef }`. The runner folds `given`
into fresh aggregate state, decides `when`, and answers `{ "emit": [EventRef…] }` or
`{ "reject": "<invariant>" }`. If a response carries both keys, `reject` wins.

**Subjects.** A `SubjectRef` is `{ "kind": "<subject kind>", "claims": { claim: scalar |
[scalar…], … } }`. It is supplied beside the command, never inside its `with`. The source's key
was `actor`. A set-valued claim is the one array on the wire. A request with no subject is
conformant only for a Decider whose subject alphabet is empty.

**Projection requests.** There is one per Projector scenario: `{ "given": [EventRef…], "key"?: {
field: scalar, … } }`. The runner answers the view state, or for a keyed Projector the named
partition's state. "Scoping is **not** on this wire."

**Equality.** It is exact for decisions: the verdict, the invariant, the emitted events in order,
and each payload. It is full-state for projections: "an extra field is as non-conformant as a
wrong one".

**Names on the wire.** "Opaque keys were ruled for identity, and identity is not a wire contract."
Every element kind that appears on the wire carries an authored **wire name** (`sdlc:wireName`):
commands, events, payload fields, invariants in rejections, subject kinds and their claims. The
REST projection and the conformance protocol use it, "never the key and never the label":
- **Why not the key.** Keys are opaque ULIDs (§2.2), and a payload object keyed by ULIDs would
  make the wire unreadable to every runner author.
- **Why not the label.** Labels change freely by decision, and a rename would silently break
  every runner.
- **What a wire name is.** It is authored, a `dpp/1` token, and stable by default. It is "changed
  only by a decision that is by definition a breaking change to the wire contract".
- **Where it is unique.** Product-wide for commands, events, invariants and subject kinds. For a
  field, it is unique within its owning command, event, subject kind or view, because the wire
  names a field only inside its owner.
- **Which kinds carry one.** Everything that appears on the wire. That is commands, events,
  payload fields, invariants in rejections, subject kinds and their claims, and view fields, which
  a projection response names.

The source already called the payload "a **public wire contract**" that "must be authored, not
guessed". The wire name is that contract's vocabulary.

*In Acme Shop:* the commands' wire names are `place-order` and `refund-order`, and the events'
are `order-placed` and `order-refunded`.

The four schemas are in [`what/conformance/`](what/conformance/), moved from v1.11.0's
`preview/conformance/` with `actor` renamed `subject`. Their `$id`s are under
`https://decision-driven-design.dk/ns/sdlc/conformance/1/`.

A runner's answers are ground readings, not stored verdicts. Whether a realisation conforms is
computed by the gate from the What's scenarios and the recorded run.

---

## 7. Encoding and conformance

### 7.1 Encoding, cut down

- Everything is one graph.
- Every What element has a stable identity (§2.2).
- Derivation edges run between What elements.
- RDF and SHACL are the reference encoding, and an equivalent is conformant.
- The edges into the retired How (`realizes`, `enforces`) are dropped.
- Two edges are added, a decision anchoring to an element and supersession. Both are
  decision-side: the How vocabulary's `sdlc:anchor` and the protocol's `supersedes`. The What
  graph itself carries `sdlc:succeeds` between elements.
- The store is Varve.

The edges are in `what/ontology.ttl`, each with its source. Of the source's table of edges:
- the What links are carried (renamed as `within` absorbs the ownership links);
- the How, work-unit, verification and delivery links (`applies`, `realizes`, `enforces`,
  `realizes_step`, `composes`, `binds`, `renders`, `at_tier`, `versioned_as`, `realises_version`,
  `in_target`, `stamped_with`, `graph_hash`) are not carried.

### 7.2 Conformance — one level

One level, **described and in force**. A product's What conforms at a stated position when:

1. **Described.** The What graph conforms to `what/shapes.ttl` at the sdlc edition it names, and
   every element is in the identity form (§2.2). It conforms when validation reports no
   `sh:Violation`. Warnings are reported with the claim, and never count against it.
2. **In force.** Every element has an accepted decision chain back to the genesis, under the
   authority profile. The authority profile is therefore part of conformance. "In force" is
   [`authority.md`](authority.md) §4.7, over a positioned log.
3. **Versioned.** The position is named by a What-version record whose element list and graph
   hash recompute from the graph.

What it does not claim: that any realisation satisfies the What. That is a verdict at a position,
computed and never stored.

**The validation regime.** "Conforms to `what/shapes.ttl`" means this, so that every
implementation computes the same results:
- **The data graph** is the What graph merged with the edition's `what/ontology.ttl`, in the
  default graph. The vocabulary's enumerated individuals (the states, the interaction classes, the
  AIOs) live in the ontology, so the What graph alone does not validate.
- **The semantics** are SHACL Core's class semantics (`rdf:type/rdfs:subClassOf*` over that merged
  graph), with SHACL-SPARQL, and no RDFS or OWL entailment.
- **The ontology** is never part of a What graph's hash or of its export (§2.3).

**Violations and warnings.** Each shape has one severity:
- `sh:Warning` when it can only hold once an element authored later exists, later in phase order
  or in a later write: a finding about what is not yet modelled. A tool that refuses a write on a
  failed shape refuses on violations only.
- `sh:Violation` when it concerns an element's own form, identity or type boundary.
- A requirement added to an edition after an example is pinned enters as `sh:Warning`. It may
  become a violation only in a later edition, once the pinned examples carry it. Existing
  violations are not demoted.

In edition 1, the warnings are:
- pattern conformance (§3.2.0);
- a command emits at least one event, and a view is built from at least one;
- command coverage (§3.3);
- Decider and state justification, and the Projector's event coverage (§3.4);
- subject coverage, claim justification and scope coverage at the seam (§3.7);
- the description checks of §3.1 and §3.7;
- a context mapping's direction (§3.1).

Every other shape is a violation. `what/check.py` runs the regime with pyshacl, and compares each
example's warnings, by message and focus node, with the set expected of it.

---

## 8. The choices made when the What moved here

The move made seven choices of its own. All are decided, as proposed, with two additions made when
they were ruled: the multi-scope rule, and view fields among the kinds that carry a wire name.

| Choice | Section |
|---|---|
| `sdlc:wireName`: the authored name the wire and public interfaces use, distinct from key and label. Field names are unique within their owner, and view fields carry wire names | §6 |
| `sdlc:within` as the single containment edge | §2.2 |
| interactions, fields, state annotations, content keys and scenarios are elements | §2.2 |
| `sdlc:DeclaredTarget` for design-system and content-store declarations | §4.1 |
| §3.5 is titled "Named-algorithm primitives", with no subtitle | §3.5 |
| the What-side kinds the move adds where product-cli's `schema/` had none: Domain, System, Journey, Trigger, Decider, Projector, Scenario, NamedAlgorithm, ReferenceData, StateAnnotation, ContentKey, QualityDemand, SubjectKind, ScopeRule, among others (each with its `dct:source`) | `what/ontology.ttl` |
| an authoring scope as a set of element kinds, optionally narrowed to a subtree; tools as gathering sources; a decision spanning scopes needs a live acceptance under each | §5 |

## Appendix — where the source went

| Source | Here |
|---|---|
| PF §1, §2, §2.1 | not carried. Scope is §1. The authoring order (step 6 of the funnel was the How) is not restated |
| PF §2.2 allocation reading | not carried. It was a reading of canon, and canon is consumed by pin |
| PF §3 introduction, §3.0, §3.0.1 | §3, §3.0, §3.0.1. Direction and value-anchoring struck |
| PF §3.1 | §3.1. The data-conformance callouts are cut to a pointer |
| PF §3.2, §3.2.0 | §3.2, §3.2.0, with v1.11.0's subject edge. The slice-as-work-unit clause is struck |
| PF §3.2.1–§3.2.4 | §3.2.1–§3.2.4. Reification rules become the obligation (§4.2) and How bindings |
| PF §3.2.5 | §3.2.5, plus declared targets (§4.1) |
| PF §3.3, §3.4 | §3.3, §3.4 at v1.11.0. The pure-core contract becomes a pointer to the How |
| PF §3.5 | §3.5, retitled. Oracle conformance becomes the How's |
| PF §3.6 | §3.6. "Binds to the How" becomes "a contract anchors to it" |
| PF v1.11.0 §3.7 | §3.7, with subject for actor. Provider coverage goes to the How |
| PF §4–§5, §6 except §6.3.1, §7 | retired |
| PF §6.3.1 | §6, at v1.11.0, with wire names |
| PF §8 | dropped |
| PF §9 | §7.1 and `what/ontology.ttl`, cut down |
| PF §10 | §7.2, one level |
| PF §11, §12 | §4: declared targets and obligations. Catalogues are packages |
| PF §13 | not carried: an add-on |
| PF §14 | §5: grants over element kinds, with tools as gathering sources |
| product-cli `schema/` | `what/ontology.ttl` and `what/shapes.ttl`, §3 subset. The diff from `spec/schema/` is recorded in the move's session |
| `examples/checkout/` manifests | not carried. They are instances, and the framework ships none |

## Not settled yet

- **Whether an adopter may register AIOs** (§3.2.2) *(open)*. The source allowed it. Under this
  ontology a registered AIO would be a vocabulary change in this repository, not a What element.
  It is the same question as how.md's open question on adopters registering What kinds. Deciding
  it yes would add a registration route for vocabulary; deciding it no would close the base set
  at ten.

## Where this comes from

**The source.** The Product Framework, github.com/Hafeok/product-framework: v1.10.0 at `c895652`,
and v1.11.0 at `55c9281` for §3.7 and the sections it threads. v1.11.0 was never merged in that
repository. It is adopted here by ruling. Quoted passages are its text, cited below by its section
("PF §3.1"). The move was made by the session at
`meta/sessions/2026-10-28-product-framework-what-move/` and ratified when its pull request (#42)
merged.

| Section | Rests on |
|---|---|
| §1.1 | `DDD-dec-41`; `DDD-dec-42` (declared ground) |
| §1.2 | How: `DDD-dec-55`…. Delivery, work units, Two Pillars: `DDD-dec-42`; the gate is Writ: `DDD-dec-54`. Data conformance: `DDD-dec-44`. Force: `DDD-dec-46`, `DDD-dec-47`, set aside for its own pull request (move Round 1, Q-4), now `authority.md` (`DDD-dec-85`, `DDD-dec-86`). Catalogues: `DDD-dec-57`. `pf:` ends: move Round 1, Q-3 |
| §1.3 | In order: `DDD-dec-41`, `-42`; `-42`, `-55`; `-43`; `-44`, `-57`; `-45`; `-44`, `-46`; `-49`, `-52`; `-51`; `-63`; move Round 1, Q-1, Q-3, Q-5; `DDD-dec-113` |
| §2.1 | `DDD-dec-42`, `DDD-dec-43`. Anchoring a creating decision: move Round 6, `DDD-dec-63` §8, applying `DDD-dec-55` (How ruling 1) |
| §2.2 | `DDD-dec-63`. Containment: `DDD-dec-64` P-2. What is an element: `DDD-dec-64` P-3; bindings anchor: `DDD-dec-57` |
| §2.3 | `DDD-dec-63` §6; the canonical form: `DDD-dec-73` (Round 3), superseding `DDD-dec-63`. Ontology not hashed: `DDD-dec-113` E-1. Second implementation: successor item M-12 (`DDD-dec-73`). Varve's reproduction: `DDD-dec-113` E-3 |
| §3, §3.0, §3.0.1 | PF §3, §3.0, §3.0.1. Direction struck: `DDD-dec-42`; PF §7.3. Second genesis: `DDD-dec-46`. Value-anchoring was PF §6/§7 |
| §3.1 | PF §3.1, §3.2.0 (datatypes). Every box says what it is: `DDD-dec-113` E-7. Context mapping direction: `DDD-dec-113` E-8. Data conformance: PF §13; `DDD-dec-44` |
| §3.2, §3.2.0 | PF §3.2, §3.2.0. Trigger source and subject: move Round 1, Q-1 and Q-5; PF v1.11.0 §3.2.0. Slices and work units: PF §5 |
| §3.2.1 | PF §3.2.1; offered to: Q-1, Q-5, PF v1.11.0 §3.2.1. Concrete controls: `DDD-dec-57`. The reification rule (PF §4.5) is not the What's: `DDD-dec-45` |
| §3.2.2 | PF §3.2.2. The open point: how.md §6 |
| §3.2.3 | PF §3.2.3. Criteria not re-minted: `DDD-dec-63` §4. Attestations: `DDD-dec-52`; held by the authority profile (move Round 1, Q-4) |
| §3.2.4, §3.2.5 | PF §3.2.4, §3.2.5 |
| §3.3 | PF v1.11.0 §3.3 (signature: Q-1; subject: Q-5); PF §3.3 (scenarios; pure core, PF §4.2) |
| §3.4 | PF §3.4, PF v1.11.0 §3.4 (Q-5). The checks in `shapes.ttl`: `DDD-dec-113` E-4 |
| §3.5 | PF §3.5; title `DDD-dec-64` P-5. Oracle conformance was PF §6.3 |
| §3.6 | PF §3.6; Kind 1 wiring how.md §4.2, H-9 |
| §3.7 | PF v1.11.0 §3.7, adopted by move Round 1, Q-1 and Q-5. Second authority: `DDD-dec-46`, `DDD-dec-47`. The checks in `shapes.ttl`: `DDD-dec-113` E-4 |
| §4.1 | `DDD-dec-57`; `DDD-dec-64` P-4. `pf:` classes: Q-3 |
| §4.2 | `DDD-dec-45`; content as How bindings `DDD-dec-57`; coverage `DDD-dec-58` |
| §5 | `DDD-dec-44`, `DDD-dec-46`, `DDD-dec-43` |
| §5.1 | `DDD-dec-64` P-7; force is the profile's (move Round 1, Q-4); the multi-scope rule: move Round 5; Writ's [D2]; genesis unscoped: `DDD-dec-46`; kind immutable: `DDD-dec-63` §3; PF §14.2. Recorded 2026-11-02: `authority.md` §3.1, §4.2, §9. Writ product definition, Draft 2, chapter 2 |
| §5.2 | `DDD-dec-43`; PF §14, §14.2–§14.5 |
| §6 | The charter; move Round 1, Q-1 (PF §6.3.1 at v1.11.0). `actor` → `subject`: Q-5. Wire names: move Round 2, `DDD-dec-64` P-1; uniqueness: R-1; kinds: R-2. Keys: `DDD-dec-63`. Ground readings: `DDD-dec-52` |
| §7.1 | `DDD-dec-51`; PF §9; identity `DDD-dec-63` |
| §7.2 | `DDD-dec-51`; PF §10; identity `DDD-dec-63`; in force `DDD-dec-47`, set aside until the profile existed (Q-4) and recorded on 2026-11-02 as existing (`authority.md` §4.7). Validation regime: `DDD-dec-113` E-1; violations and warnings: E-2 |
| §8 | `DDD-dec-64`, its table rows in order P-1 to P-7 (P-6: the What-side kinds the move adds); Q-2 (product-cli's `schema/` §3 as the subset); `examples/checkout` not carried: `DDD-dec-45`. P-1 ruled in move Round 2; P-2 to P-7, R-1 and R-2 ruled in Round 5, all as proposed; P-7's multi-scope rule and R-2's amendment to P-1's list added with the ruling |

Ids in this document are in this table and the `ddd:doc` block, not in its running text. The text
it replaces is `84aa466:applications/sdlc/what.md`.
