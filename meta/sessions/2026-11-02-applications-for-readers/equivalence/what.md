# Equivalence — `applications/sdlc/what.md`

Old text: `e5a332d:applications/sdlc/what.md` (861 lines). New text: `applications/sdlc/what.md`
(practitioner, "W") and `applications/sdlc/what-reference.md` (tool builders, "R").

| # | Old: section and rule, in brief | New: document and section | Note |
|---|---|---|---|
| 1 | Status banner: moved 2026-10-28, not yet ratified; session path; rulings `DDD-dec-41`..`63`; source commits | W, "Where this comes from" | removed: history. Stale as well: the move merged in PR #42 |
| 2 | Register key (Ruled, `[PROPOSED]`, `[OPEN]`, quoted PF text) | W opening, "How settled this is" | removed: replaced by the words convention (`DDD-dec-94`) |
| 3 | Companions list (ontology, shapes, example, check.py, vectors, conformance, how.md) | R, "Files"; W, "The tools" | same |
| 4 | §1.1 The What is the opinionated specification of what software is and does; a system is not a coordinate; ground and tolerance; step 1 reads addresses off the What | W, "What a What is", last paragraph | same |
| 5 | §1.2 Not here: How → how.md | W, "What the What does not cover" | same |
| 6 | §1.2 Delivery retired, not carried | W, "What the What does not cover" | same, in words |
| 7 | §1.2 Work units, seams, verification as a process retired; the gate is Writ | W, "What the What does not cover" (How); R, conformance wire "Results" (the gate computes) | same; "the gate is Writ" is stated in how.md |
| 8 | §1.2 Two Pillars dropped; canon consumed by pin | — | removed: history. Nothing for a practitioner to act on; `DDD-dec-42` in the basis table |
| 9 | §1.2 Data conformance is an add-on outside the framework | W, "What the What does not cover"; W, Domains (production data) | same |
| 10 | §1.2 Force (genesis, grants, acceptance, baselines, waivers) is the authority profile's | W, "What the What does not cover"; W, "Who may change what" | same |
| 11 | §1.2 Catalogues are packages with their own genesis | W, "What the What does not cover"; W, "Design systems and content" | same |
| 12 | §1.2 The `pf:` namespace ends with this move; old §4–§7 classes not carried | R, "Encoding" (the old edge names do not exist) | moved to reference; the namespace history removed |
| 13 | §1.3 Table of rulings | W and R, "Where this comes from" | removed: history; ids moved to basis tables |
| 14 | §2.1 A decision is not a What element; it anchors to the element it governs | W, "Every change is a decision" | same |
| 15 | §2.1 Every change is a decision; current form is the result of anchored decisions; history is decision history | W, "Every change is a decision" | same |
| 16 | §2.1 Gathered material is a proposal; enters only when a human principal signs and accepts | W, "Gathering what already exists elsewhere" | same |
| 17 | §2.1 A creating decision anchors to the narrowest existing element covering every element it creates; for a new domain that is the product, not a loophole; an element being created is never its own anchor | W, "Adding something new"; R, "Identity", "Creating decisions" | same |
| 18 | §2.2 Nothing in an identity carries meaning | R, "Identity" | moved to reference |
| 19 | §2.2 Product IRI P named in the genesis record, stable across transfer; P is the product node | R, "Identity" | moved to reference |
| 20 | §2.2 Elements are `P/what/<key>`; ULID minted at creation; never changed or reused; IRI encodes neither kind nor position | R, "Identity" | moved to reference |
| 21 | §2.2 Human name is `rdfs:label`, changes by decision; resolving is `explain`'s job | R, "Identity" | moved to reference |
| 22 | §2.2 Rename, property change, move keep identity; kind change, split, merge make new elements linked by `sdlc:succeeds`; baselines not carried over | W, "What keeps its identity"; R, "Identity" | same; in words in W, exact in R |
| 23 | §2.2 Elements are IRIs; blank nodes only inside one description | R, "Identity" | moved to reference |
| 24 | §2.2 One containment edge, `sdlc:within`; every element but the product is within exactly one; subtree is `within*`; no typed sub-properties; why (single transitive walk); meaning carried by kind pair, enforced by shapes | R, "Identity", "Containment" | moved to reference; the list of replaced product-cli edges removed as history |
| 25 | §2.2 Interactions, fields, state annotations, content keys, scenarios are elements; anything a binding, baseline, `reads`, scope key or wire request names is an element; adding a field is a What decision and that is the correct cost | R, "Identity", "What is an element"; W, "What keeps its identity" (adding a field is a decision) | same |
| 26 | §2.3 What-version is a `dpp/1` record pinning every What decision in force and listing elements by IRI and hash | R, "What-versions and hashes" | moved to reference |
| 27 | §2.3 Canonical form RDFC-1.0 over RDF 1.2 N-Quads; lowercase language tags; escapes as Varve; graphs alone; no blank node in a triple term | R, "What-versions and hashes" | moved to reference |
| 28 | §2.3 Element hash; graph hash; authored logic by `sdlc:logic` digest; equalities; no force | R, "What-versions and hashes" | moved to reference; "graph name not hashed" added from Round 4 of the move, which `e5a332d`'s text did not state |
| 29 | §2.3 pyoxigraph conforms on every vector; pyld does not and is a cross-check only; second implementation is successor item M-12 | R, "Implementations"; R, "Not settled yet" | moved to reference |
| 30 | §3 intro: product owns domains and systems; a system references whole domains, does not own them | W, "How the What is organised" | same |
| 31 | §3 intro: domain owns meaning and rules, system owns surface and journey; the "would two systems disagree" test | W, "How the What is organised" | same; the test kept verbatim in substance |
| 32 | §3 intro: ownership is `sdlc:within`; system's use of a domain is `sdlc:referencesDomain` | R, "The vocabulary, by concept" | moved to reference |
| 33 | §3.0 Product carries a name and purpose; its job is ownership and boundary | W, "The product" | same |
| 34 | §3.0 Product-wide concerns: quality demands, journeys, product-wide content keys and declared targets | W, "The product" | same |
| 35 | §3.0 "Direction" not carried (was Delivery) | — | removed: history |
| 36 | §3.0 Boundary is exactly the owned domains and systems; a second product is a second root and second genesis; may reference a shared domain across a declared boundary (Translation), never absorbs it | W, "The product" | same |
| 37 | §3.0.1 A journey is a product-level derived composition of single-system flows linked at crossings; every crossing a Translation; owns nothing | W, "Journeys across systems" | same |
| 38 | §3.0.1 Every crossing is a Translation or a finding; a journey references, does not contain; systems stay independent | W, "Journeys across systems" | same |
| 39 | §3.0.1 Blast radius stays (a traversal); value-anchoring went with Delivery | W, "Journeys across systems", last line | same; value-anchoring removed as history |
| 40 | §3.0.1 `sdlc:composesFlow`, `sdlc:crossesVia` | R, vocabulary table | moved to reference |
| 41 | §3.1 Domain is the home of meaning and rules; contains bounded contexts, entities, value objects, relations, invariants; the event model; subject kinds | W, "Domains" | same |
| 42 | §3.1 Bounded contexts; one meaning per term per context; explicit declared mappings | W, "Domains", Structure | same |
| 43 | §3.1 Relations carry cardinality and rationale; invariants machine-checkable; aggregate holds exactly its invariant-bearing state; the rest is a Projector's output | W, "Domains", Structure | same |
| 44 | §3.1 Machine-readable with a constraint language; RDF + SHACL reference; equivalent conformant | W, "Domains", Structure | same |
| 45 | §3.1 Attributes are `sdlc:Field`; single datatype vocabulary: string, integer, number (`xsd:decimal`), boolean, date | W, "Domains" (types); R, vocabulary table (terms) | same |
| 46 | §3.1 Reference data is What; constitutive; the means-vs-more-rows test | W, "Domains", Reference data | same |
| 47 | §3.1 Production data is not What; data conformance is not framework; an add-on may check data against shapes; nothing depends on one | W, "Domains"; W, "What the What does not cover" | same |
| 48 | §3.2 Event model is what happens over time, peer to the domain model, same graph | W, "Behaviour" | same |
| 49 | §3.2 Behaviour may not reference structure that does not exist; every event changes a real entity; every command targets one | W, "Behaviour" | same |
| 50 | §3.2 A view declares its state space: `present` plus any of `loading`, `empty`, `failed` (`sdlc:hasState`) | W, "Behaviour"; R, vocabulary | same |
| 51 | §3.2 Proportional depth | W, "Behaviour" | same |
| 52 | §3.2.0 Four blocks, four patterns (table) | W, "Building blocks and patterns" | same |
| 53 | §3.2.0 Automated trigger contains no business logic; Translation reads from exactly one source system; write side may fan out | W, "Building blocks and patterns" | same |
| 54 | §3.2.0 A trigger has exactly one source (`user`, `external`, `automated`), the channel, three-valued because patterns are checked by it; who acts is `sdlc:subject`; nature must match source | W, "Building blocks"; R, vocabulary | same; "v1.11.0 called this `acts_as`" removed as history |
| 55 | §3.2.0 Command or Event MAY declare a payload schema; within one system private, between two a public wire contract that must be authored | W, "Building blocks", Payloads | same |
| 56 | §3.2.0 Payload fields are `sdlc:Field` within their owner; order is `sdlc:fieldOrder` | R, vocabulary | moved to reference |
| 57 | §3.2.0 A slice is one pattern instance, the smallest unit handed to an implementer; a flow is a chain of slices | W, "Building blocks", Slices | same; the slice/work-unit history removed |
| 58 | §3.2.1 A UI step is where a person sees and acts; What; says what a screen is for and means, never how it looks | W, "The UI step" | same |
| 59 | §3.2.1 A UI step references only AIOs, never a concrete control; each interaction typed as exactly one AIO; surfaces one projection, offers one command or enters one payload field; concrete control is a target's vocabulary; AIO-to-CIO is a How binding anchored to the interaction | W, "The UI step", Meaning, not widgets | same |
| 60 | §3.2.1 The buildable core is derived: intent, information shown, actions available, transitions | W, "The UI step", What follows from the model | same |
| 61 | §3.2.1 A step is offered to one or more human subject kinds; system-level | W, "The UI step", Offered to | same |
| 62 | §3.2.1 Modelled meaning: emphasis; state annotations (only states the projection has; meaning for every state or explicit waiver with reason); accessibility; content references with role, never literal strings; words not the What's | W, "The UI step", What you model | same |
| 63 | §3.2.1 Intent is specification debt; promoted into the model; shrinks toward purpose; the intent-reliance rate | W, "The UI step", Intent | same |
| 64 | §3.2.1 Promote the missing AIO, context of use or meaning; a missing reification is a missing binding, debt on the How's coverage | W, "The UI step", Intent | same; the history of the old list removed |
| 65 | §3.2.2 An AIO is meaning, not a widget; single-select example | W, "Abstract interaction objects" | same |
| 66 | §3.2.2 Ten base AIOs, framework vocabulary, not What elements; input AIOs derive shape from the domain | W, "Abstract interaction objects"; R, vocabulary | same |
| 67 | §3.2.2 `[OPEN]` whether an adopter may register AIOs; a registered AIO would be a vocabulary change | W, "Abstract interaction objects" *(not settled yet)*; W and R, "Not settled yet" | same; stays open |
| 68 | §3.2.2 Context of use is a declared model; dimensions; platform is a dimension like any other; What-side but carries no realisation; what bindings are written against | W, "Abstract interaction objects", context of use | same |
| 69 | §3.2.2 Interaction class gates dimensions (GUI, TUI); system declares classes (`sdlc:targetsClass`); AIO vocabulary unchanged across classes | W, same section; R, vocabulary | same |
| 70 | §3.2.3 WCAG 2.2, version-pinned, ingested from the W3C machine-readable source; referenceable nodes | W, "Accessibility, from the standard" | same |
| 71 | §3.2.3 `sdlc:mustSatisfy` by W3C IRI; criteria not What elements; nothing re-minted under P | W (in words); R, vocabulary | same |
| 72 | §3.2.3 Obligations inherited from AIOs plus added; the union | W, Accessibility | same |
| 73 | §3.2.3 Verification type machine, assisted, manual; verdict states level and basis, never bare "accessible: true" | W, Accessibility | same |
| 74 | §3.2.3 Manual criterion discharged by attestation; a signed record and a ground reading, not a stored verdict; how it is held is the authority profile's | W, Accessibility; W, "Not settled yet" | same |
| 75 | §3.2.4 Navigation is one graph of pages and `navigate` edges | W, "The page graph" | same |
| 76 | §3.2.4 Flow: named connected subgraph with an entry page; root with global destinations; top-level is derived, never a tag | W, "The page graph"; R, vocabulary | same |
| 77 | §3.2.5 A system carries name, kind, purpose, domains, target contexts and classes, declared targets | W, "Systems" | same |
| 78 | §3.2.5 System owns its page graph, flows, steps, triggers; a flow belongs to exactly one system; behaviour shared; system quality demands within the system | W, "Systems" | same |
| 79 | §3.2.5 System identity is What, deployment identity is How (Acme example); target declaration binds a deployable unit; contract states what it must satisfy | W, "Systems" | same; the example's domain list adjusted to the worked example's actual domain (Ordering only) |
| 80 | §3.3 Signature `decide(state, command, subject)`, `evolve` | W, "Deciders" | same |
| 81 | §3.3 In business terms: rules are rejections; a Decider also says what results | W, "Deciders" | same |
| 82 | §3.3 Subject is the authenticated principal, supplied by authentication, never by the caller; not a payload field | W, "Deciders" | same |
| 83 | §3.3 Signature derived, only logic authored; six derivation rules | W, "Deciders", Only the logic | same |
| 84 | §3.3 Logic held by digest (`sdlc:logic`) | R, "What-versions and hashes"; R, vocabulary | moved to reference |
| 85 | §3.3 Conformance rules: no foreign commands, command coverage, output-alphabet containment, subject coverage (with the pair rule) | W, "Deciders", The rules | same |
| 86 | §3.3 Wire scalar alphabet; number and date travel as strings; one list-valued position, the set-valued claim | R, conformance wire, "The scalar alphabet" | moved to reference |
| 87 | §3.3 Scenarios: simulated before realisation; given, when, then; `sdlc:Scenario` within its Decider or Projector; lists inside description; when names the subject | W, "Deciders", Scenarios; R, vocabulary | same |
| 88 | §3.3 Pure core is a How binding over Deciders; What states only the oracle | W, "Deciders", What this asks of the How | same |
| 89 | §3.4 `project(state, event)`; symmetric to the Decider: signature derived, fold authored, simulated, oracle for its View | W, "Projectors" | same |
| 90 | §3.4 No foreign events, event coverage, output containment | W, "Projectors" | same |
| 91 | §3.4 Actor (subject) not an input to the fold; one fold serves every subject; scope applied at the seam; keyed-by fields; every scope key field among them (`sdlc:keyedBy`) | W, "Projectors"; R, vocabulary | same |
| 92 | §3.4 State justification and Decider justification; each a finding pointing at an unmodelled invariant; claim justification joins them; Decider justification is in shapes | W, "Projectors", Two checks; W, "Who may act", checks; R, "Shapes" | same |
| 93 | §3.5 Title "Named-algorithm primitives", no subtitle; "floor" is canon's | W, "Named algorithms" | could not restate exactly: the heading is "Named algorithms — computation you name instead of deriving", which the format's task-naming rule (F1, F4) produces. It does not reintroduce "floor". Reported for Emil: `DDD-dec-64` P-5 rules the title "Named-algorithm primitives", with no subtitle |
| 94 | §3.5 Derivable exactly to the degree variability is declared data | W, "Named algorithms" | same |
| 95 | §3.5 Specified by reference, I/O contract, oracle by digest; exempt from derivation and simulation; oracle check is a How binding; What carries the oracle; undisclosed algorithm passing as projection is the dishonesty prevented | W, "Named algorithms"; R, vocabulary | same |
| 96 | §3.6 A quality demand is never prose; exactly two kinds by how checked | W, "Quality demands" | same |
| 97 | §3.6 Runtime bound and architectural constraint, with their How sides | W, "Quality demands" table; R, vocabulary | same; "H-9" and how.md section numbers removed |
| 98 | §3.6 The test: production measurement or realisation inspection; neither → prose, debt | W, "Quality demands" | same |
| 99 | §3.6 Demands are located within the element they scope (product, system, flow, step, Decider, Projector) | W, "Quality demands" | same |
| 100 | §3.6 The How's contract anchors to the demand; the What holds only the demand | W, "Quality demands" | same |
| 101 | §3.7 Subject kind for actor kind; subject for `acts_as`; why "subject" | — | removed: deliberation (the choice of word). The words are used |
| 102 | §3.7 Two authorities, never one: product authorization vs authority over the specification; the second is genesis and authority profile; subject kind never a grant and vice versa; author not a subject | W, "Who may act", opening | same |
| 103 | §3.7 Authentication is How; provider binding per deployment as a How contract; What never names a provider; provider coverage belongs to the How | W, "Who may act" | same |
| 104 | §3.7 Authorization split table | W, "Who may act" table | same |
| 105 | §3.7 Nature: exactly one of human, process, external; closed; not a role | W, Subject kinds | same |
| 106 | §3.7 Claims typed, may be set-valued, may draw from reference data | W, Subject kinds | same |
| 107 | §3.7 Framework ships no actor kinds and no roles; offered-to vs only-a-rule test | W, Subject kinds | same |
| 108 | §3.7 Delegation not modelled; until then an external subject kind whose claims carry the delegating principal | W, Subject kinds | same |
| 109 | §3.7 Read side: public or scoped; rules per subject kind; conjunction of keys; `equals` or `member-of` | W, "What a subject may see" | same |
| 110 | §3.7 Rule with no keys is declared every row; no rule → sees nothing, deny by default | W, same | same |
| 111 | §3.7 Fold unchanged; scope at the seam; every key field a key of the fold | W, same | same |
| 112 | §3.7 Cross-row aggregates folded keyed by the scoping dimension; disjunctive scope as a recorded fact and a keyed View | W, same | same |
| 113 | §3.7 Checks bind once a subject kind is declared; none declared → unstated, not absent | W, "The checks" | same |
| 114 | §3.7 Checks table: subject coverage, scope coverage, claim justification | W, "The checks" table | same |
| 115 | §3.7 What shapes.ttl carries; `[OPEN]` three not yet written as shapes | R, "Shapes"; W, "Not settled yet" | same; stays open |
| 116 | §4.1 Design system and content store are targets the What declares, as it declares iOS | W, "Design systems and content" | same |
| 117 | §4.1 A system or the product declares platform contexts and classes, a design system at an edition, a content store with edition and locales | W, same; R, vocabulary (`DeclaredTarget`, `targetKind`, `edition`, `locale`) | same |
| 118 | §4.1 One kind, `sdlc:DeclaredTarget`; edition reference may not resolve; that is "not reachable", Writ's `explain`, not a required check | W (in words); R, vocabulary | same |
| 119 | §4.1 Catalogue is the target's edition, a package with its own genesis; nothing in a catalogue is a What element of the user; `pf:` classes not carried; How vocabulary has target kinds | W, "Design systems and content"; R, vocabulary | same; the `pf:` list removed as history |
| 120 | §4.2 Obligations, not content; ships obligations, never widgets or words | W, "Design systems and content" | same |
| 121 | §4.2 Obligations 1–3 (reification exists; reification coverage; content coverage), pairs computed from the What | W, same, numbered list | same |
| 122 | §4.2 Content is a How binding anchored to interaction or key; baseline entry for declared missing (shrinks under the ratchet); exclusion with reason for unreifiable; a waiver never covers a coverage gap | W, "Where the content lives" | same |
| 123 | §4.2 The What states the pairs; the How the bindings and gaps; neither holds the other's part | W, same | same |
| 124 | §5 Authoring scopes are central; who can change what, and who holds the genesis grant; they instantiate the genesis grant; tools never change the What; everything gathered is signed by a human | W, "Who may change what"; W, "Gathering" | same |
| 125 | §5.1 Force, grants and acceptance are the authority profile's; this section states what a scope ranges over and the multi-scope rule | W, "What the What does not cover" | same |
| 126 | §5.1 Genesis unscoped, covers every kind everywhere under P | W, "Who may change what"; R, "Authoring scopes, as data" | same |
| 127 | §5.1 A scope is a set of kinds, optionally narrowed to a subtree; acceptance valid only if every created, changed or retired element is in scope and subtree | W (in words); R, exact | same |
| 128 | §5.1 Decision spanning scopes needs acceptance under each; in force only while all live; Writ's [D2]; the profile inherits it | W (in words); R, exact | same |
| 129 | §5.1 Kind vocabulary is the ontology; scope introduces no ontology | R, "Authoring scopes, as data" | moved to reference |
| 130 | §5.1 Derived kinds in no scope; no grant authorises authoring them | W, "Who may change what"; R | same |
| 131 | §5.1 Kind immutable, so scope boundary cannot be crossed by reclassifying | W; R | same |
| 132 | §5.1 Product owner's What scope and architect's How scope are two grants over two sets of kinds; Writ's "two grants over two subgraphs" | W, Acme example; R | same |
| 133 | §5.2 A tool is a gathering source; material is a proposed decision; enters only on a covering grant holder's signed acceptance | W, "Gathering" | same; "PF made it a co-author; reversed" removed as history |
| 134 | §5.2 Gathering declaration: kinds, completeness, channel, excluded list; grants nothing; bounds proposals | W, "Gathering"; R | same |
| 135 | §5.2 Out-of-scope material never proposed; Figma/Decider example | W, "Gathering" | same |
| 136 | §5.2 Gap split: unauthored-within-scope, outside-scope; findings that route work | W, "Gathering"; R | same |
| 137 | §5.2 Completeness join: covered (by whom), coverable but ungathered, uncovered; two halves, a source and a grant holder | W, "Gathering"; R | same |
| 138 | §5.2 Symmetry: top is grants over kinds; bottom is the How's coverage; both bidirectional joins over one What | W, "Gathering", last paragraph | same |
| 139 | §6 The conformance wire moves with the What; it is the oracle's interface, not a verification process; corrects how.md Appendix B | R, "The behavioural-conformance wire" | moved to reference; the correction of how.md removed as history |
| 140 | §6 Runner definition; decision requests; reject wins; subjects; projection requests; scoping not on the wire; equality | R, same | moved to reference, same |
| 141 | §6 Names on the wire: wire names on every kind on the wire (P-1, R-2 list); never key nor label, with why; authored, dpp/1 token, stable, changed only by a breaking decision; uniqueness (R-1) | R, "Names on the wire" | moved to reference, same |
| 142 | §6 Payload is a public wire contract; wire name is its vocabulary | R, "Names on the wire"; W, Payloads | same |
| 143 | §6 Four schemas in `what/conformance/`, `$id`s under `…/sdlc/conformance/1/` | R, "The schemas" | moved to reference; "moved from v1.11.0's `preview/conformance/`" removed as history |
| 144 | §6 Runner answers are ground readings, not stored verdicts; conformance computed by the gate | R, "Results"; W, "When a What is complete" | same |
| 145 | §7.1 Encoding list (one graph, identity, derivation edges, RDF/SHACL, How edges dropped, two decision-side edges, `succeeds`, Varve) | R, "Encoding"; W, "The tools" (Varve) | moved to reference |
| 146 | §7.1 Which PF §9 links are carried and which not | R, "Encoding" | moved to reference; restated as the terms that do not exist |
| 147 | §7.2 One level, described and in force: described, in force (chain to genesis under the profile; cannot be claimed until it exists), versioned | W, "When a What is complete and in force"; W, "Not settled yet" | same |
| 148 | §7.2 Does not claim a realisation satisfies the What; a verdict, computed, never stored | W, same | same; adds "what is recorded is the declaring decision and what was read", which is `DDD-dec-52` as already applied in §3.2.3 and §6 of the old text |
| 149 | §8 The move's own choices, `DDD-dec-64` P-1 to P-7, table | W and R, "Where this comes from" | removed: deliberation; each choice's content is in rows 24, 25, 93, 117, 127, 141 |
| 150 | Appendix — where the source went | — | removed: history; reachable at `e5a332d` |

## Could not restate

- **Row 93, the named-algorithm heading.** `DDD-dec-64` P-5 ruled the title "Named-algorithm
  primitives", with no subtitle. The new heading is "Named algorithms — computation you name
  instead of deriving". It keeps P-5's purpose: "floor" is not used. But it is not the ruled title.
  Emil to rule: keep the ruled title as written, or accept the reader's heading.

## Found while rewriting

- **Prediction P-1 did not hold.** The practitioner document is 641 lines, not under 450, and the
  pair (641 + 261 = 902) is longer than the old 861. The old text's deliberation was smaller than
  predicted; most of its length was rules. The new text adds worked-example passages, states rules
  in full sentences where the old text quoted fragments, and repeats a few rules in both documents,
  in words in one and exactly in the other.
- **The vocabulary files cite sections that no longer exist.** `what/shapes.ttl` (four messages)
  and `what/ontology.ttl` (one comment) cite "what.md §6". Both files are hashed into the
  vocabulary edition that the What-versions pin, so editing them changes the edition. They are
  left as they are. Re-pointing them is a successor item for the next edition.
- **`build.py` comments** in `how-examples/` cite "what.md §2", "§5" and "§6". They are comments in
  a build script, outside this session's scope. Successor item.
- **The old system-identity example** named a "Catalog" domain and iOS and Android targets, which
  the worked example does not have. The new text keeps the iOS, Android and web wording as an
  illustration of the line between What and How, but names only the Ordering domain.
