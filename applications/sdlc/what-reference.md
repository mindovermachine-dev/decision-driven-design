# The What — reference for tool builders

<!-- ddd:doc
reader: developers building tools that read, write, check or hash a What, or that run its conformance wire
act: implement identity, What-versions, the vocabulary, scopes and the behavioural-conformance wire exactly as specified
pin: v5.15.2
basis: [DDD-dec-46, DDD-dec-47, DDD-dec-51, DDD-dec-52, DDD-dec-55, DDD-dec-57, DDD-dec-62, DDD-dec-63, DDD-dec-64, DDD-dec-73]
status: current
supersedes: e5a332d:applications/sdlc/what.md
-->

*For what a What is and how to write one, see [`what.md`](what.md).*

Use this when you build a tool that works on a What: an editor, a checker, a store adapter, a
hashing library or a conformance runner. It specifies identity, What-versions and their hashes, the
vocabulary, authoring scopes as data, and the wire on which an implementation's behaviour is
checked.

**How settled this is.** Everything here is decided, except the points marked *(not settled
yet)*. One canonical-form implementation passes the published vectors. A second, independent one
does not exist yet.

**Files.**

| File | Holds |
|---|---|
| [`what/ontology.ttl`](what/ontology.ttl) | The vocabulary, sdlc edition 1. Every term carries its source |
| [`what/shapes.ttl`](what/shapes.ttl) | The shapes a described What satisfies |
| [`what/examples/acme-shop.ttl`](what/examples/acme-shop.ttl) | The worked example |
| [`what/examples/logic/`](what/examples/logic/) | The example's Decider logic and Projector fold, held by digest |
| [`what/check.py`](what/check.py) | Runs the shapes, the identity form and the hash law over the example, and checks the hashes against `vectors.json` |
| [`what/vectors.json`](what/vectors.json) | The example's element and graph hashes |
| [`what/canonical-form-vectors.json`](what/canonical-form-vectors.json) | Test vectors for the canonical form |
| [`what/mint.py`](what/mint.py) | Mints element keys |
| [`what/conformance/`](what/conformance/) | The four JSON schemas of the conformance wire |

---

## Identity

**Nothing in an identity carries meaning.**

- **The product.** The product IRI, P, is named in the product's genesis record. It is stable when
  the genesis grant is transferred. P is itself the product node, the root of the What.
- **Elements.** Every other element is `P/what/<key>`. The key is a ULID minted when the element is
  created ([`what/mint.py`](what/mint.py)). It is never changed and never reused. The IRI encodes
  neither kind nor position.
- **Names.** The human name is `rdfs:label`, and it changes by decision. Resolving a key to its
  name is `explain`'s job in the governance tooling.
- **What keeps identity.** A rename, a property change or a move happens under the same IRI. A
  change of kind, a split or a merge makes new elements, linked to the old ones by
  `sdlc:succeeds`. Baselines are not carried over to the new elements.
- **Kind is immutable.** An element's kind never changes in place.
- **Elements and descriptions.** An element is any node referred to by identity, and it is always
  an IRI. Blank nodes are allowed inside an element's description: lists, payload bindings, scope
  keys. A blank node belongs to exactly one description.

**What is an element.** Anything a binding, a baseline, `reads`, a scope key or a wire request
names is an element, with its own IRI. That includes interactions, fields (attributes, payload
fields, view fields and claims), state annotations, content keys and scenarios. Blank nodes are
only where nothing names the node. So a binding anchors to an interaction or a content key, a
Decider reads a field, and a scope key compares two fields.

**Containment.** The one containment edge is `sdlc:within`. Every element except the product node
is within exactly one element, and a subtree is `within*`. There are no typed sub-properties. One
edge makes "the subtree an anchor covers" a single transitive walk, which is what the How's anchors
read. The relation's meaning is carried by the pair of kinds, and the shapes enforce it. A reader
that needs ownership as opposed to attachment reads the kinds.

**Creating decisions.** A decision that creates elements anchors to the narrowest element that
exists at the position where it is proposed and covers every element it creates. For a new domain
that is the product. An element being created does not exist yet at that position, so it is never
its own creating decision's anchor.

## What-versions and hashes

- **The record.** A What-version is a `dpp/1` record. It pins every What decision in force, and
  lists every element by IRI and element hash.
- **The canonical form** is RDFC-1.0 over RDF 1.2 canonical N-Quads. Language tags are lowercase.
  ECHAR and UCHAR escapes are as Varve writes them. A graph is canonicalised alone, never across
  named graphs, and a triple term never holds a blank node.
- **The element hash** is taken over the element's description, canonicalised on its own.
- **The graph hash** is taken over the whole canonical graph. The graph's name is not hashed.
- **Authored logic.** A Decider's logic and a Projector's fold are artefacts carried by digest in
  `sdlc:logic`, so both hashes cover them.
- **Equalities.** Equal graph hashes mean the same specification. Equal record hashes mean the
  same specification, reached by the same decisions.
- **No force.** A What-version confers no force. Force stays with the decisions it pins.

**Implementations.** `what/check.py` computes the hashes with pyoxigraph, which conforms to the
canonical form on every vector in `what/canonical-form-vectors.json`. pyld (URDNA2015 over RDF 1.1
N-Quads) does not conform: it keeps uppercase language tags and mis-escapes control characters. It
serves only as a cross-check, on graphs where it cannot diverge. A second, independent conforming
implementation is *(not settled yet)*.

## Encoding

- Everything is one graph.
- Every What element has a stable identity (above).
- Derivation edges run between What elements.
- RDF and SHACL are the reference encoding. An equivalent encoding conforms.
- There are no edges into the How's realisation or into delivery. The terms `applies`,
  `realizes`, `enforces`, `realizes_step`, `composes`, `binds`, `renders`, `at_tier`,
  `versioned_as`, `realises_version`, `in_target`, `stamped_with` and `graph_hash` do not exist in
  this vocabulary.
- The Product Framework's `pf:` namespace ends with this vocabulary. None of its classes is carried
  in any namespace, including `pf:DesignSystem`, `pf:ContentStore`, `pf:Cio`, `pf:Token` and
  `pf:ReificationRule`: catalogues are packages, not What.
- Two edges are decision-side, not What-side: a decision's anchor (the How vocabulary's
  `sdlc:anchor`) and supersession (the protocol's `supersedes`). The What graph itself carries
  `sdlc:succeeds` between elements.
- The store is Varve.

## The vocabulary, by concept

Every term is in [`what/ontology.ttl`](what/ontology.ttl) with its source. This table maps the
concepts of [`what.md`](what.md) to their terms.

| Concept | Terms |
|---|---|
| Containment; succession | `sdlc:within`; `sdlc:succeeds` |
| A system's use of a domain | `sdlc:referencesDomain` |
| Journeys | `sdlc:Journey`, `sdlc:composesFlow`, `sdlc:crossesVia` (the automated triggers of Translations) |
| Fields, typed from string, integer, number (`xsd:decimal`), boolean, date | `sdlc:Field` |
| Payload field order | `sdlc:fieldOrder`, an RDF list inside the owner's description |
| A view's states | `sdlc:hasState`: `present`, and any of `loading`, `empty`, `failed` |
| A trigger's channel and subject | the trigger's source (`user`, `external`, `automated`); `sdlc:subject` |
| Interactions and their abstract type | `sdlc:Interaction`; the ten base types `sdlc:aioTriggerAction` … `sdlc:aioEdit` (framework vocabulary, not What elements) |
| Offered to | `sdlc:offeredTo` |
| State meanings | `sdlc:StateAnnotation` |
| Content references | `sdlc:ContentKey`, with a declared role |
| Contexts of use; interaction classes | `sdlc:ContextOfUse`; `sdlc:targetsClass` |
| Accessibility obligations | `sdlc:mustSatisfy`, to a WCAG 2.2 criterion by its W3C IRI. Criteria are not What elements, and nothing is re-minted under P |
| Flows; entry page; membership; the root | `sdlc:Flow`, `sdlc:entryPage`, `sdlc:inFlow`, `sdlc:SystemRoot` |
| A system's kind | `sdlc:systemKind` |
| Scenarios | `sdlc:Scenario`, within its Decider or Projector; given and expected emissions are RDF lists inside its description; its *when* names the subject it is issued as |
| Decider and Projector logic | `sdlc:logic`, by digest |
| A keyed fold | `sdlc:keyedBy` |
| Named algorithms | `sdlc:NamedAlgorithm`: reference, I/O contract, and an oracle of input and output pairs held by digest |
| Quality demands | `sdlc:RuntimeBound`; `sdlc:ArchitecturalConstraint` |
| Subjects and scopes | `sdlc:SubjectKind`, its claims as `sdlc:Field`; `sdlc:ScopeRule`, one per subject kind |
| Declared targets | `sdlc:DeclaredTarget`, with `targetKind` (`design-system` or `content-store`), `sdlc:edition` (a `dpp/1` reference to the target's vocabulary-edition record) and, for a content store, one `sdlc:locale` per BCP 47 tag. The How's vocabulary has the target kinds ([`how-reference.md`](how-reference.md)) |
| Wire names | `sdlc:wireName` |

An edition reference may not resolve from the product that names it. That is the protocol's "not
reachable", and resolving it is Writ's `explain`, not a check the What's own checker requires.

## Authoring scopes, as data

- **The genesis grant** is unscoped within the product. It covers every element kind, everywhere
  under P.
- **A scope** is a set of What element kinds, the classes of `what/ontology.ttl`, optionally
  narrowed to the subtree (`sdlc:within*`) of one element. A grant delegating from the genesis
  carries a scope.
- **Acceptance.** An acceptance of a What decision is valid only if every element the decision
  creates, changes or retires is of a kind in the grant's scope, and inside its subtree.
- **A decision spanning scopes** needs a valid acceptance under each scope, from the same holder or
  different holders. It is in force only while all of them are live. This is Writ's [D2]
  conjunction applied to scopes, the same shape as derived acceptance for blends. The authority
  profile inherits this rule and does not choose otherwise.
- **The kind vocabulary is the ontology.** A scope names `sdlc:UIStep`, `sdlc:Interaction`,
  `sdlc:ContentKey` and so on. A scope introduces no ontology of its own.
- **Derived kinds are in no scope**, for example a read model's state space. No grant authorises
  authoring them.
- **Kind is immutable**, so a scope's boundary cannot be crossed by reclassifying an element.

The product owner's What scope and the architect's How scope are two grants over two sets of kinds
of one product: Writ's "two grants over two subgraphs of the same log".

**Gathering declarations.** A gathering source declares, per kind it may supply, a completeness
(`sufficient` or `partial`) and a channel, plus an explicit list of excluded kinds. Material for an
excluded kind is never proposed. The gap findings are `unauthored-within-scope` (the source could
supply it and did not) and `outside-scope` (route to another source). A completeness join reports
each required kind as covered (by which source and which grant holder), coverable but ungathered,
or uncovered.

## The behavioural-conformance wire

The wire is how anyone claims that an implementation computes what the What's Deciders and
Projectors say. It is the oracle's interface, not a verification process.

**A conformance runner** is any process that reads a JSON array of requests on stdin and writes a
JSON array of outcomes on stdout, one per request, in order, and exits 0.

**Decision requests.** One per Decider scenario:
`{ "given": [EventRef…], "when": CommandRef, "subject"?: SubjectRef }`. The runner folds `given`
into fresh aggregate state, decides `when`, and answers `{ "emit": [EventRef…] }` or
`{ "reject": "<invariant>" }`. If a response carries both keys, `reject` wins.

**Subjects.** A `SubjectRef` is `{ "kind": "<subject kind>", "claims": { claim: scalar |
[scalar…], … } }`. It is supplied beside the command, never inside its `with`. A set-valued claim is
the one array on the wire. A request with no subject conforms only for a Decider whose set of
subject kinds is empty.

**Projection requests.** One per Projector scenario: `{ "given": [EventRef…], "key"?: { field:
scalar, … } }`. The runner answers the view state or, for a keyed Projector, the named partition's
state. Scoping is not on this wire.

**Equality.** Exact for decisions: the verdict, the invariant, the emitted events in order, and
each payload. Full-state for projections: an extra field is as non-conformant as a wrong one.

**The scalar alphabet.** Values are `boolean`, 64-bit signed `integer` and `string`. A `number` or
`date` field travels as a string until the alphabet is extended. Exactly one list-valued position
is admitted: a set-valued claim, which travels in the subject block as an array of scalars.

**Names on the wire.** Every element kind that appears on the wire carries an authored wire name,
`sdlc:wireName`. That is commands, events, payload fields, invariants in rejections, subject kinds
and their claims, and view fields, which a projection response names. The REST projection and the
conformance protocol use the wire name, never the key and never the label:
- **not the key**, because keys are opaque ULIDs, and a payload keyed by ULIDs would be unreadable
  to every runner author;
- **not the label**, because labels change freely by decision, and a rename would silently break
  every runner.

A wire name is authored, is a `dpp/1` token, and is stable by default. It is changed only by a
decision, which is by definition a breaking change to the wire contract. It is unique product-wide
for commands, events, invariants and subject kinds. A field's wire name is unique within its owning
command, event, subject kind or view, because the wire names a field only inside its owner. A
payload between systems is a public wire contract that must be authored, not guessed, and the wire
name is that contract's vocabulary.

**The schemas** are in [`what/conformance/`](what/conformance/): decision request and response,
projection request and response. Their `$id`s are under
`https://decision-driven-design.dk/ns/sdlc/conformance/1/`.

**Results.** A runner's answers are ground readings, not stored verdicts. Whether an implementation
conforms is computed by the gate, from the What's scenarios and the recorded run.

## Shapes: what is checked mechanically

`what/shapes.ttl` checks, among the rest of the described What:
- the Decider rule that a Decider has at least one reachable rejection;
- the step half of subject coverage;
- that a trigger's source and its subject's nature agree;
- all three scope-coverage rules.

*(Not settled yet.)* Not yet written as shapes, though each is a query over the same graph:
- that every automated or external trigger acts as a subject kind;
- the scenario-per-pair half of subject coverage;
- claim justification.

## Not settled yet

- **A second canonical-form implementation.** Only pyoxigraph is shown to conform. A second,
  independent conforming implementation is a successor item, tracked against Varve's published
  vectors.
- **The three missing shapes**, listed above.
- **Adopter-registered kinds.** Whether an adopter may register abstract interaction objects, or What
  kinds in general, is open. If allowed, a registration would change this vocabulary, not a product's
  What.

## Where this comes from

| Section | Rests on |
|---|---|
| Identity | `DDD-dec-63` (the identity form, §3 kind immutable, §4 nothing re-minted under P, §8 creating anchors, Round 6); `DDD-dec-64` P-2 (one containment edge), P-3 (what is an element) |
| What-versions and hashes | `DDD-dec-63` §6; `DDD-dec-73` (RDFC-1.0 qualified three ways, superseding `DDD-dec-63`'s form; the graph name not hashed, Round 4 of the What move); successor item M-12, tracked as Hafeok/varve#192 |
| Encoding | `DDD-dec-51` (§9 cut down; Varve); Round 1, Q-3 of the What move (the `pf:` namespace ends); `DDD-dec-57` |
| The vocabulary | `what/ontology.ttl` (each term's `dct:source`); `DDD-dec-64` P-4 (`DeclaredTarget`), P-6 (the kinds the move added); `DDD-dec-57` |
| Authoring scopes | `DDD-dec-46`; `DDD-dec-64` P-7, with its multi-scope rule (Round 5); Writ product definition, Draft 2, chapter 2; `DDD-dec-43` (gathering) |
| The conformance wire | Product Framework v1.11.0 §6.3.1, moved with the What (Round 1, Q-1), with `actor` renamed `subject` (Q-5); `DDD-dec-64` P-1, R-1, R-2 (wire names); `DDD-dec-52` (answers are ground readings); the scalar alphabet from v1.11.0 §3.3 |
| Shapes | `what/shapes.ttl` at `e5a332d` |

The earlier text of these sections was part of `what.md` at `e5a332d`.
