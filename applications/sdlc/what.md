# The What — writing down what your software is and does

<!-- ddd:doc
reader: architects, developers and product owners specifying a software product
act: write a product's What, change it under control, and hand it to the people and agents who build from it
pin: v5.15.2
basis: [DDD-dec-41, DDD-dec-42, DDD-dec-43, DDD-dec-44, DDD-dec-45, DDD-dec-46, DDD-dec-47, DDD-dec-51, DDD-dec-52, DDD-dec-55, DDD-dec-57, DDD-dec-58, DDD-dec-63, DDD-dec-64, DDD-dec-73]
status: current
supersedes: e5a332d:applications/sdlc/what.md
-->

*For identities, hashes, the vocabulary and the conformance wire, see
[`what-reference.md`](what-reference.md).*

Use this when you are about to build, change or take over a piece of software, and you need one
place that says what it is and does, before anyone decides how to build it.

After reading it you can:
- write down a product's What: its domains, its systems, and the behaviour and screens they carry;
- change the What, and know who may make each change and when it comes into force;
- hand the What to the people and agents who build from it, and check what they build against it.

**How settled this is.** Everything here is decided, except the points marked *(not settled
yet)*. None of it has yet been tried on a real product beyond the worked example, so try it before
you rely on it.

**The worked example** is a small web shop, Acme Shop. Customers place orders and staff refund
them. Its whole What is in [`what/examples/acme-shop.ttl`](what/examples/acme-shop.ttl), and
every example below comes from it unless it says "if you added".

---

## What a What is

A What describes what a piece of software is and does, in the language of the people who own it.
It says nothing about how the software is built: which language, which framework, which cloud.
That is the How, and it is written against a settled What ([`how.md`](how.md)).

Three things make a What more than a requirements document:

1. **It is one connected graph, not a set of pages.** Every part has a stable identity and
   explicit links to the parts it depends on. "Describe this system" is a query, and "what does
   this change touch?" is a walk along the links.
2. **It changes only by signed decisions.** Nobody edits the What. Every change is a short
   record, signed by a person with the right to make that change. At any moment you can ask what
   the software should do, and who decided each part of it.
3. **It is what the software is checked against.** The What's rules for behaviour are executable,
   so an implementation can be checked against them over a defined wire, in any language. Nothing
   is checked against what someone remembers the What to be.

In the framework's own terms, the What is the software's declared ground and its tolerance. It is
what every act in the software reads, and the bar each act must meet. Step 1 of the method reads
its map of acts off the What instead of inventing one ([`../../method/`](../../method/)).

**What the What does not cover.**
- **How the software is built and deployed.** That is the How ([`how.md`](how.md)).
- **Delivery.** Features, releases, "done", versions and roadmaps are not part of this framework.
- **Who holds authority over the What.** That is the authority profile (`authority.md`, which
  lands with pull request #45). This document says what authority ranges over, not how it is held.
- **Checking production data against the What.** That is a useful add-on that reads the What. It
  is not part of the framework, and nothing here depends on it.
- **Catalogues of components, tokens and strings.** Those belong to the design system or content
  store that supplies them, which is a product of its own.

---

## Changing the What

### Every change is a decision

You never edit the What directly. To change it, you write a decision: a record that says what
changes, and points at the part of the What it changes. That part is its **anchor**.

A decision is not itself part of the What. It sits beside the What, attached to its anchor. The
current form of any part of the What is the result of the decisions anchored to it, so the What's
history is its decision history.

*In Acme Shop:* the whole What, 44 elements, arrived in one founding decision, and the product
owner signed a second record accepting it. The rule "a refund cannot exceed what was paid" came in
with that founding decision. If someone later loosened it, that would be a new decision anchored
to the `Order` entity. The founding decision would stay on record.

### Adding something new

Something you are about to create does not exist yet, so it cannot be the anchor of the decision
that creates it. Anchor that decision to the **narrowest part that already exists and contains
everything you are adding**.

*In Acme Shop:* if you added a `Cancel order` command, its decision would anchor to the
`Ordering` domain. A whole new `Shipping` domain would anchor to the product itself. So did the
founding decision, which created `Ordering`. Anchoring to the product is the normal case for a new
domain, not a loophole.

### What keeps its identity, and what does not

Renaming a part, changing its properties or moving it keeps its identity. Changing what kind of
thing it is, splitting it or merging it makes new parts, linked back to the old ones. A part's
kind never changes in place. Adding a field is a decision of its own, because a field is something
other parts name: a wire contract changed.

### Who may change what

Every product has one **founding grant**, its genesis grant, held by the person who brought the
product into being. It covers everything in the product. Every other right to change the What is
delegated from it, directly or through others.

A delegated right is an **authoring scope**: a set of kinds of thing in the What, such as UI
steps, interactions or content keys, optionally limited to one part of the What and everything
inside it. A decision is accepted only if everything it creates, changes or retires is of a kind
in the signer's scope, and inside the part the scope is limited to. Because a part's kind never
changes in place, nobody can move a part out of someone else's scope by reclassifying it.

A decision that spans several scopes needs an acceptance under each of them, from the same person
or from different people. It is in force only while all of those acceptances stand.

Some things in the What are computed from others, never written by anyone. For example, the states
a screen's data can be in follow from the read model's shape. No scope covers them, so nobody may
write them by hand.

*In Acme Shop:* the founder holds the genesis grant. The product owner holds a What scope and the
architect holds a How scope, both delegated from it. These are two rights over two sets of kinds
of one product.

### Gathering what already exists elsewhere

Parts of a What usually exist already: in a Figma file, an Event Modeling board, an old database
schema, a Jira board. You can gather them from there. A tool is a **source**, never an author:

- **What you gather is a proposal.** It enters the What only when a person whose scope covers it
  signs and accepts it.
- **Each source declares its reach.** For each kind of thing it can supply, it says whether it can
  supply it fully or only partly, and through which channel the meaning arrives (a native
  annotation, a component name, a frame's structure). It also lists the kinds it must not supply.
  The declaration grants nothing. It only bounds what the source may propose.
- **Out-of-scope material is never proposed.** A Decider drawn in Figma is refused because Figma
  is not a source of Deciders, not because the Decider is wrong.
- **Gaps route work.** Something the source *could* supply but did not is work for that tool.
  Something no work in that tool could supply is routed to a source that can.
- **Completeness has two halves.** A What is complete when every kind it needs is covered. Covered
  means two things: a source that can supply the kind, and a person whose scope lets them accept it.
  A completeness check reports each needed kind as covered (and by whom), coverable but not yet
  gathered, or uncovered.

Who may change what is the top of a symmetry. Its bottom is the How's coverage, which says what is
built where ([`how.md`](how.md)). Both are checks over one What, run in both directions.

---

## How the What is organised

A product owns **domains** and **systems**:

- A **domain** owns meaning and rules: what an `Order` is, that a refund cannot exceed what was
  paid, which events an order emits.
- A **system** owns a surface and its journeys: which screens exist, how you move between them,
  and which platform it runs on.

A system uses whole domains; it never owns one. When you are unsure where something belongs, ask:
**would two systems disagree about it?** If they must agree, it belongs in the domain. If they may
differ, it belongs in the system. A refund is a refund in the customer app and in the staff tool,
so refund rules live in the domain. The two apps navigate differently, so navigation lives in each
system.

*In Acme Shop:* the product owns one domain, `Ordering`, and two systems, `shop-api` and
`shop-bff`. Both systems use `Ordering`, so both enforce the same refund rule without restating it.

### The product

The product carries little of its own: a name and a purpose. Its job is to own things and to draw
the boundary. Its product-wide concerns are:
- quality demands that bind the whole product;
- journeys that cross systems;
- content keys and declared targets that serve every system, such as a shared design system.

The product's boundary is exactly the domains and systems it owns. A second product is a separate
product with its own genesis grant. It may use a domain of this one across a declared boundary, its
systems talking through Translations (below), but it never absorbs it.

### Journeys across systems

A journey is a path through several systems' flows, linked where it crosses from one system to
another. It belongs to the product, and it owns nothing.

- **Every crossing is a Translation, or it is a finding.**
- **A journey refers to flows; it does not contain them.** Remove a journey and nothing else
  changes.
- **Systems stay independent.**

A journey lets you see what a change touches across systems: follow the links.

---

## Domains — meaning and rules

A domain is the home of meaning and rules: what its concepts mean, how they relate, and how they
behave. Inside it are bounded contexts, and inside those the entities, value objects, relations
and invariants; the event model, with its Deciders and Projectors; and the kinds of subject that
act in it.

**Structure.**
- **Bounded contexts, not one flat model.** Within a context, a term has exactly one meaning. The
  same word may mean different things in different contexts. A correspondence between contexts is
  an explicit, declared mapping, never assumed.
- **Entities, relations, value objects, invariants.** A relation carries its cardinality and its
  rationale. An invariant is a machine-checkable constraint. An aggregate holds exactly the state
  its Deciders must read to decide. Anything else a screen wants is a Projector's output, not a
  stored field.
- **Machine-readable, with a constraint language.** The model is a graph with shapes that can be
  validated. RDF and SHACL are the reference; an equivalent encoding conforms.
- **Fields have one set of types:** string, integer, number, boolean and date.

*In Acme Shop:* the `Order` entity has the fields `customer_id`, `paid_total` and
`refunded_total`, and the invariants "order has lines" and "refund within paid".

**Reference data is part of the What.** Some data defines what the system means: the valid
shipping methods, the tax categories, the product taxonomy, the accepted currencies. Behaviour is
undefined without it, so it lives in the What. The test: **if changing a datum changes what the
system means, it is reference data; if it is just more rows of the same kind, it is production
data.** Production data is not part of the What.

---

## Behaviour — what happens over time

The event model describes what happens over time. It sits beside the domain's structure, in the
same graph.

- **It is built from real structure.** Behaviour may not refer to structure that does not exist:
  every event changes a real entity, and every command targets one.
- **Every view declares its states.** A view is always `present`, and declares which of
  `loading`, `empty` and `failed` it can also be in.
- **Depth is proportional.** Concepts with rich or historical behaviour get a full event model.
  Simple create, read, update and delete concepts get a minimal one, or none.

### Building blocks and patterns

There are four building blocks: Trigger, Command, Event and View. They make four patterns:

| Pattern | Shape |
|---|---|
| **Command** | `Trigger → Command → Event(s)` |
| **View** | `Event(s) → View` |
| **Automation** | `Event(s) → View → Trigger (automated) → Command → Event(s)` |
| **Translation** | `Event(s) [system A] → View → Trigger (automated) → Command → Event(s) [system B]` |

- An automated trigger contains no business logic.
- A Translation reads events from exactly one source system. Its write side may fan out.

**A trigger has one channel and one subject.** Its channel, its **source**, is one of `user`,
`external` or `automated`. There are exactly three, because the patterns are checked by them. Who
acts through the channel is separate: the trigger's **subject**, the kind of subject it acts as
(see "Who may act in the product"). The subject must fit the channel: a `user` trigger acts as a
human, an `automated` one as a process, and an `external` one as an outside system.

**Payloads.** A Command or an Event may declare a payload: a list of named fields, each optionally
typed. Within one system, a payload is a private convenience. Between two systems it is a public
wire contract, and it must be written down, not guessed.

**Slices.** One pattern instance is a **slice**: the smallest coherent piece you can hand to an
implementer. A flow is a chain of slices.

*In Acme Shop:* the commands `Place order` and `Refund order` emit the events `Order placed` and
`Order refunded`. The view `Order summary` is built from those events.

### Deciders — where the business rules run

A Decider is the executable form of behaviour. It is where the business rules live: its
rejections are the rules, and its accepted outcomes are the events a command produces.

```
decide(state, command, subject) -> Accepted[events] | Rejected[invariant]
evolve(state, event)            -> state
```

**The subject is supplied by the system, never by the caller.** It is the authenticated subject
issuing the command, with its kind and its claims, as the system's authentication supplies them.
It is never a payload field.

**Only the logic is written by hand. Everything else follows from the model:**
- A Decider decides for one aggregate.
- It handles exactly the commands that target that aggregate.
- It may emit only the events its commands are declared to emit.
- It evolves from the events that change the aggregate.
- Its rejections are the aggregate's invariants, plus rejections over the subject's claims.
- The kinds of subject it serves are those its commands are offered to or issued as.

**The rules a Decider must satisfy:**
- **No foreign commands.**
- **Command coverage.**
- **Output containment:** it emits nothing outside its declared events.
- **Subject coverage:** for every pair of command and subject kind, the Decider either accepts the
  command for that kind or has a reachable rejection over its claims, and a scenario per pair shows
  which.

**Scenarios.** Before anything is built, a Decider is simulated against scenarios drawn from the
flows. A scenario gives the prior events, the command, and the expected events, and names the
subject the command is issued as.

**What this asks of the How.** Keeping the decision logic in a pure core is a How decision over
Deciders. The What states only the oracle: the Decider, its logic and its scenarios.

*In Acme Shop:* the scenario "refund beyond what was paid" shows the Order Decider rejecting a
refund larger than the order's paid total.

### Projectors — how read models are built

```
project(state, event) -> state          -- the read-model fold
```

A Projector is the executable form of a read model, and it mirrors the Decider in every respect:
only the fold is written by hand; it is simulated before anything is built; and it is the oracle for
its View. Its rules are **no foreign events**, **event coverage** and **output containment**.

**One fold serves every subject.** The subject is not an input to the fold. What a given subject
may see is a selection applied over the fold's output (see "Who may act"). A Projector behind a
scoped View declares the fields its fold is keyed by, and every field a scope rule reads must be one
of them.

**Two checks keep the model honest.** A field belongs on an aggregate only if some Decider reads
it. A Decider must have at least one reachable rejection. Each check, when it fails, points at an
invariant nobody has modelled.

### Named algorithms — computation you name instead of deriving

A computation can be derived from the specification exactly to the degree that its variability is
declared data over a generic interpreter. What remains, such as a geometric solver or a hash
function, is a **named algorithm**. You specify it by reference to the algorithm or standard it
implements, by an input and output contract in the domain's terms, and by an oracle of reference
input and output pairs. It is exempt from derivation and from behavioural simulation. Checking an
implementation against its oracle is the How's job; the What carries the oracle. An undisclosed
algorithm passed off as a mechanical projection is exactly what a named algorithm exists to
prevent.

---

## Screens — what a person sees and does

### The UI step

A UI step is the point in a flow where a person sees something and acts. It is What: it says what
a screen is *for* and what it *means*, never how it looks.

**Meaning, not widgets.** A UI step may refer only to abstract interaction objects, never to a
concrete control from a design system. Each interaction in a step is typed as exactly one abstract
interaction object. It shows one projection, offers one command, or enters one payload field.
Which concrete control realises it is a How decision, anchored to the interaction.

**What follows from the model:**
- the information shown: projections, through display objects;
- the actions available: commands, through action or input objects;
- the transitions: the `navigate` edges of the page graph;
- the step's intent, which is marked debt (below).

**Offered to.** A step is offered to one or more kinds of human subject. This belongs to the
system, because the staff tool and the shop may offer the same command to different people.

**What you model, as checkable parts rather than prose:**
- **emphasis**;
- **what each state of the data means on this screen.** A step may annotate only states its
  projection actually has, and it must give a meaning to every state the projection can be in, or
  explicitly waive one with a reason;
- **accessibility obligations** (below);
- **content references.** A step refers to content keys, each with a declared role. Text is never
  written as literal strings in a UI step. The words themselves are not the What's.

**Intent is specification debt.** Whatever intent was used to decide something must be promoted
into the model. Intent therefore shrinks steadily toward a pure statement of purpose. The
**intent-reliance rate**, how often building a screen needed intent to settle something the model
did not, measures the debt. When intent was needed, promote the missing abstract interaction object,
context of use or meaning into the What. A missing choice of concrete control is not the What's
gap: it is a missing How binding, and debt on the How's coverage.

*In Acme Shop:* `shop-bff` has one UI step, `Order detail`, offered to customers. Its intent is
"The customer checks an order and asks for part of it back", and its emphasis is "What is still
refundable". It has three interactions: it shows the `Order summary` (a `display-value`), takes
the refund amount (a `numeric-entry` into the command's `amount` field), and offers `Refund order`
(a `trigger-action`). It gives the `empty` state a meaning: "The order is not the customer's or
does not exist; offer the way back to their orders."

### Abstract interaction objects and contexts of use

An abstract interaction object is meaning, not a widget. `single-select` means "choose exactly one
from a set". It is *not* a dropdown, a radio group or a segmented control: those are the concrete
forms it can take.

**There are ten:** `trigger-action`, `single-select`, `multi-select`, `text-entry`,
`numeric-entry`, `date-entry`, `display-value`, `display-collection`, `navigate` and `edit`. They
are the framework's vocabulary, not parts of your What. An input object takes its shape from the
domain: it enters a command's payload field, whose type and allowed values the domain defines.
Whether you may add your own is *(not settled yet)*.

**A context of use is declared.** A system declares its contexts of use, each a value on one
dimension: platform, form factor, modality or terminal capability. Platform is a dimension like any
other, so "iOS, Android, or both" is which platform contexts a system targets. Contexts are What,
but they carry no realisation. They are what the How's bindings are written against.

**The interaction class decides which dimensions apply.** A graphical interface brings form factor
and pointer or touch. A text interface brings terminal capabilities and rules form factor out. A
system declares the classes it targets. The set of abstract interaction objects is the same in
every class.

### Accessibility, from the standard

Accessibility obligations come from WCAG 2.2, pinned to its version and taken from the W3C's
machine-readable source. Criteria are referenced, never written out as prose, and they are not
parts of your What. A step or an interaction declares the criteria it must satisfy.

- **Inherited and added.** A step's obligations are those of the abstract interaction objects it
  uses, plus any criteria the step adds.
- **How each is checked.** Each criterion is machine-checked, assisted or manual. An accessibility
  verdict states a conformance level and its basis, never a bare "accessible: true".
- **Attestations.** A manual criterion is met by an attestation: a dated, attributed statement
  that a named criterion was evaluated and met. Here an attestation is a signed record together
  with what was read to make it. It is not a stored verdict. How it is held is the authority
  profile's.

### The page graph

Navigation is not a separate shell above the screens. It is **one graph whose nodes are pages (UI
steps) and whose edges are `navigate` transitions.**
- **Flows.** A flow is a named, connected part of the graph, with an entry page.
- **The root.** Each system has a root, whose outgoing edges are its global destinations.
- **"Top-level" is computed:** a page is top-level when the root links to it. It is never a tag.

---

## Systems — the surfaces of a product

A system is one way the product is used. It has:
- a name;
- a kind: application, website, service, command-line tool, and so on;
- a purpose;
- the whole domains it uses;
- its target contexts and interaction classes;
- the targets it declares (see "Design systems and content").

It owns its page graph, its flows, its UI steps and its triggers. A flow belongs to exactly one
system. The behaviour a flow invokes belongs to the domain, so every system using that domain
shares it. Quality demands that bind only one system are placed inside it.

**System identity is What; deployment identity is How.** The What says "Acme Shop is a consumer
shop, using the Ordering domain, targeting iOS, Android and the web". The How says "the iOS bundle
is `com.acme.shop`, and the web is served at `shop.acme.com` from these runtimes". In the How, a
target declaration ties a deployable unit to the system, and a contract states what the unit must
satisfy.

---

## Who may act in the product

This section is about authorization **inside the product**: who may act in the software being
specified, such as a customer cancelling an order. It is not about who may change the What. That
is the genesis grant and the scopes (above). A kind of subject is never a grant, a grant is never a
kind of subject, and writing a specification does not make you a subject of the product.

**Authentication is How.** Which identity provider authenticates a subject, how a session is held,
and what a token looks like are realisation. Which provider serves which kind of subject is
declared per deployment, as a How contract. The What never names a provider, so checking that every
kind of subject has a provider is the How's job.

**Authorization splits by the same test as everything else:**

| Authorization fact | Belongs to | Lives on |
|---|---|---|
| who the kinds of subject are, and what each carries | the domain | a **subject kind**, and its **claims** |
| a rule over who may change what ("only the order's customer may refund it") | the domain | a **Decider rejection** that reads a claim |
| what each kind of subject may see of a View | the domain | the View's **scope**: one scope rule per subject kind |
| which kinds of subject a screen or trigger is offered to | the system | the step's "offered to"; the trigger's subject |

**Subject kinds.**
- **Nature.** Each has exactly one: `human` (acts through a UI step), `process` (through an
  automated trigger) or `external` (an outside system, through an API call). Nature is a closed list,
  and it is not a role.
- **Claims.** A subject kind carries typed claims. A claim may hold a set of values, and may draw
  its values from reference data.
- **Kind or claim?** The framework ships no subject kinds and no roles. One test decides: **if a
  surface is offered to it, it is a subject kind; if only a rule reads it, it is a claim.**
- **Delegation**, an outside system acting for a person, is not modelled. Until it is, model it as
  an external subject kind whose claims carry the person it acts for.

**What a subject may see is a View's scope.**
- **Public or scoped.** A View is public, or scoped by rules, one per kind of subject. A rule is a
  set of conditions that must all hold. Each compares a view field with a claim, as `equals`, or as
  `member-of` for a claim that holds a set.
- **Defaults.** A rule with no conditions explicitly means "every row". A kind of subject with no
  rule on a scoped View sees nothing: access is denied by default.
- **The fold does not change.** The scope is applied over the fold's output. Every field a scope
  compares is a key of the fold.
- **Totals across rows** are folded keyed by the dimension the scope selects on.
- **"Mine, or shared with me"** is modelled as a recorded fact, and a View keyed on it.

*In Acme Shop:* the subject kinds are `Customer` and `Staff`. "Only the order's customer may
refund it" is the Order Decider's rejection `refund by owner`, which reads the customer's claim. The `Order summary` view is scoped:
"customers see their own orders" compares the view's `customer_id` with the customer's claim, and
"staff see every order" has no conditions.

**The checks.** They apply once a What declares at least one kind of subject. A What that declares
none has authorization that is *unstated*, not absent.

| Check | Mirrors | Holds when |
|---|---|---|
| **Subject coverage** | command coverage | every step that offers or shows something is offered to at least one human subject kind; every automated or external trigger acts as one; every pair of command and subject kind has a scenario showing acceptance or a reachable rejection |
| **Scope coverage** | — | every View a step shows is public, or has a rule for every kind of subject the step is offered to; every claim a rule reads belongs to that rule's subject kind; every view field a rule compares is a key of the fold |
| **Claim justification** | the field check on aggregates | a claim no Decider reads and no scope uses is dead, or the trace of an authorization rule nobody has modelled |

Some of these checks are not yet automated *(not settled yet)*: see the end of this document.

---

## Quality demands — the non-functional, made checkable

**A quality demand is never prose.** Once it is part of the What, it is one of exactly two kinds,
told apart by how it is checked:

| Kind | Is | Its How side |
|---|---|---|
| **Runtime bound** | a bound measured against telemetry: latency, throughput, capacity, uptime. It declares its bound and where it is measured | the measurement wiring is a How contract over telemetry facts, anchored to the bound |
| **Architectural constraint** | a constraint on how the software is built: residency, security posture, fault-tolerance topology | a How contract anchored to it, checked at build time |

**The test that keeps demands honest:** *is it checked by measuring production, or by inspecting
what was built?* If neither can confirm it, it is not a quality demand yet. It is prose, and prose
is debt.

**Demands are placed, not listed.** A demand sits inside the part it governs: the product, for a
demand that binds every system, such as a residency rule; a system; or a flow, a step, a Decider or
a Projector. The How's contract anchors to the demand, and the What holds only the demand.

*In Acme Shop:* the product carries a residency demand, an architectural constraint that personal
data stays in the EU. The How contract that checks it is in [`how-examples/`](how-examples/).

---

## Design systems and content

A design system and a content store are **targets** the What declares, exactly as it declares iOS.
A system, or the product on behalf of every system, declares:
- its platform contexts and interaction classes;
- a **design system**, at a named edition;
- a **content store**, at a named edition, and the locales it serves.

The catalogue itself, the components, tokens and strings, belongs to the design system or content
store. It is a product of its own, with its own founding grant, typically a design team's. Nothing
in a catalogue is part of the What of a product that uses it. The edition a What names may not be
reachable from your product; resolving it is the governance tooling's job, not a check this
framework requires.

**The What carries obligations, never widgets or words.** Three obligations follow from declaring
these targets:

1. **Reification exists.** For a declared design system, every interaction in every context of use
   its system targets resolves to a concrete control of that design system.
2. **Reification coverage.** Every pair of interaction and context that a system can reach is
   covered, or declared unreifiable. The pairs are computed from the What: the system's
   interactions, and its contexts within each declared interaction class.
3. **Content coverage.** Every pair of content key and locale resolves, or is declared missing.
   The pairs are computed from the What: the keys the system's steps refer to, and the locales its
   content store serves.

**Where the content lives.** Which control, and which words, are How decisions, anchored to the
interaction or the content key. The How tracks the gaps:
- a pair that should be realised and is not yet is a baseline entry, and the baseline only shrinks;
- a pair that cannot apply is an exclusion decision, with its reason;
- a waiver never covers a coverage gap.

The What states the pairs. The How states the bindings and their gaps. Neither holds the other's
part.

*In Acme Shop:* `shop-bff` declares two targets: the Acme design system at edition 1, and the Acme
content store at edition 1, serving `en-GB` and `da-DK`. So every interaction of `Order detail`
must be reifiable in each of `shop-bff`'s contexts, and the heading's content key must resolve in
both locales, or be declared unreifiable or missing.

---

## When a What is complete and in force

A product's What conforms at a stated position when it is **described and in force**:

1. **Described.** The What graph satisfies the shapes of the vocabulary edition it names, and every
   part has an identity in the required form.
2. **In force.** Every part has an accepted chain of decisions back to the genesis grant, under the
   authority profile. *(Not settled yet: this half cannot be claimed until the authority profile
   lands.)*
3. **Versioned.** The position is named by a What-version record, whose list of parts and whose
   hash can be recomputed from the graph.

Conformance does not claim that any implementation satisfies the What. That is a verdict at a
position, computed and never stored. What is recorded is the decision that declares the check, and
what was read when it ran.

**The tools.** The vocabulary is [`what/ontology.ttl`](what/ontology.ttl), and the shapes are
[`what/shapes.ttl`](what/shapes.ttl). [`what/check.py`](what/check.py) checks the example against
the shapes, the identity form and the hash law. The What graph is stored in Varve.
[`what-reference.md`](what-reference.md) has the details for tool builders.

---

## Not settled yet

- **Adding your own abstract interaction objects.** The framework's ten are fixed for now. Whether
  an adopter may register more, and in general whether adopters may add kinds to the What, is open.
  If allowed, a new one would be a change to this repository's vocabulary, not a part of your What.
- **Checks not yet automated.** These subject checks are defined but not yet written as shapes:
  that every automated or external trigger acts as a kind of subject; the scenario-per-pair half of
  subject coverage; and claim justification. Each is a query over the same graph. Until they are
  written, check them by hand.
- **"In force" waits for the authority profile.** The second half of conformance, and how
  attestations are held, depend on the authority profile, which lands with pull request #45.

## Where this comes from

For reviewers and auditors. The decisions are in [`core/decisions/`](../../core/decisions/), and
the sessions that made them are in [`meta/sessions/`](../../meta/sessions/).

| Section | Rests on |
|---|---|
| What a What is | `DDD-dec-41` (the opinionated What; a system is ground and tolerance), `DDD-dec-42` (only the What moved; How and Delivery retired), `DDD-dec-51` (one graph; one conformance level; Varve) |
| What the What does not cover | `DDD-dec-42` (Delivery retired), `DDD-dec-44` (data conformance an add-on), `DDD-dec-46`, `DDD-dec-47` (authority), `DDD-dec-57` (catalogues are packages) |
| Every change is a decision | `DDD-dec-42`, `DDD-dec-55` |
| Adding something new | `DDD-dec-63` §8, ruled in Round 6 of the What move |
| What keeps its identity | `DDD-dec-63` §3 (kind immutable; `succeeds`); `DDD-dec-64` P-3 (fields are elements) |
| Who may change what | `DDD-dec-44`, `DDD-dec-46`; `DDD-dec-64` P-7 (scopes over kinds; the multi-scope rule, Round 5) |
| Gathering | `DDD-dec-43`; `DDD-dec-64` P-7 |
| How the What is organised; the product; journeys | Product Framework §3, §3.0, §3.0.1; `DDD-dec-64` P-2 |
| Domains | Product Framework §3.1; `DDD-dec-44` (production data and data conformance) |
| Behaviour; building blocks | Product Framework §3.2, §3.2.0; v1.11.0 §3.2.0 (source and subject), adopted in Round 1, Q-1 and Q-5 of the What move |
| Deciders; Projectors | Product Framework v1.11.0 §3.3, §3.4 (Round 1, Q-1, Q-5); the pure core as a How binding, `DDD-dec-55` |
| Named algorithms | Product Framework §3.5; `DDD-dec-64` P-5 (title) |
| Screens | Product Framework §3.2.1 to §3.2.4; v1.11.0 §3.2.1 (offered to); `DDD-dec-45`, `DDD-dec-57` (bindings are How); `DDD-dec-52` (attestations) |
| Systems | Product Framework §3.2.5 |
| Who may act in the product | Product Framework v1.11.0 §3.7, with "subject" for "actor" (Round 1, Q-1, Q-5); `DDD-dec-46`, `DDD-dec-47` |
| Quality demands | Product Framework §3.6 |
| Design systems and content | `DDD-dec-45` (obligations), `DDD-dec-57` (targets; catalogues are packages), `DDD-dec-58` (coverage, baseline, exclusion, waiver); `DDD-dec-64` P-4 |
| When a What is complete and in force | `DDD-dec-51`; `DDD-dec-47`; `DDD-dec-52`; `DDD-dec-63` §6 |

The text adapts the Product Framework, github.com/Hafeok/product-framework, v1.10.0 at `c895652`
and v1.11.0 at `55c9281` (CC BY 4.0). The earlier text of this document, at `e5a332d`, carries the
full record of the move: the rulings it was written against, the move's own choices, and where
every section of the Product Framework went. The move's session is
`meta/sessions/2026-10-28-product-framework-what-move/`.
