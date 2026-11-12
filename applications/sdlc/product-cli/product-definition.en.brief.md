# product-cli: machine-checkable statements of what a product does

product-cli yields a machine-checkable statement of what a product does, with an executable oracle for its behaviour, exported as one graph that someone else can sign. An agent proposes each step in conversation and the author [adopts](#term-adoption) or rejects it, a [Decider](#term-decider) and a [Projector](#term-projector) are simulated against [scenarios](#term-scenario) drawn from the [flows](#term-flow), and the same scenarios later judge realised code. It puts nothing in force; [Writ](#term-writ) lands the [canonical document](#term-canonical-document) it produces.

## In more detail

- **The promise.** [The What](#term-the-what) is authored in conversation, and every step of it is a decision: an agent proposes, and the author adopts or rejects each [proposal](#term-proposal). The What is a graph with [shapes](#term-shape), never prose with diagrams. Behaviour is executable before any code exists: a Decider and a Projector are simulated against scenarios that later judge realised code. The tool puts nothing in force and decides nothing about realisation.
- **Who it is for.** Three roles share one surface: an author who models the product and adopts or rejects proposals, an agent that writes only proposals, and a [realiser](#term-realiser) who runs the behavioural-conformance runner against realised code.
- **The surface.** Every verb is a commit to the [draft log](#term-draft-log), kept in Git. An agent's write is a proposal held beside [the head](#term-head), and the author adopts or rejects it. The [workbench](#term-workbench) serves a live view of the draft log in a browser. An agent session uses the same verbs over MCP and ends with an export.
- **The formats.** Every format has a specification page and a conformance suite before any implementation, and the canonical export is the graph document plus the logic artefacts its digests name, byte-identical for the same [draft position](#term-draft-position).
- **The guarantees.** Guarantees are tested in a public suite; nothing an agent wrote is in the What unless a person adopted it.
- **Boundaries and decisions taken.** The scope is the What alone; the How and code generation are not in it.

## Terms used here

- <a id="term-adoption"></a>**adoption**: The author's acceptance of a proposal, recorded as a new version of its decision with status accepted and the change set pinned.
- <a id="term-decider"></a>**Decider**: The place where the business rules for one aggregate live: it accepts or rejects each command, and says which events result when it accepts.
- <a id="term-projector"></a>**Projector**: The executable form of a read model: a fold that takes the current state and an event and gives the new state.
- <a id="term-scenario"></a>**scenario**: An element within a Decider or Projector with three parts: prior events given, a command or event applied, and the result expected.
- <a id="term-flow"></a>**flow**: A chain of slices, where a slice is a single instance of a pattern on the graph.
- <a id="term-writ"></a>**Writ**: not explained in this definition.
- <a id="term-canonical-document"></a>**canonical document**: The What graph at one draft position, written out in one fixed canonical form; the only graph document Writ lands.
- <a id="term-the-what"></a>**the What**: The opinionated specification of what a software application is and does: its declared ground, and the tolerance each act must meet.
- <a id="term-proposal"></a>**proposal**: An agent's write: a set of changes held beside the head of the draft log, not in it, until the author adopts or rejects it.
- <a id="term-shape"></a>**shape**: A check, written in SHACL, that is applied to each node of a given kind in the graph.
- <a id="term-realiser"></a>**realiser**: An engineer, or a build agent under Writ, who builds the code and runs the behavioural-conformance runner against it.
- <a id="term-draft-log"></a>**draft log**: The working copy, kept as a positioned log of its own in Git, in which every verb is a commit.
- <a id="term-head"></a>**head**: not explained in this definition.
- <a id="term-workbench"></a>**workbench**: A live, local view of the draft log in a browser, where pending proposals can be adopted or rejected.
- <a id="term-draft-position"></a>**draft position**: not explained in this definition.
