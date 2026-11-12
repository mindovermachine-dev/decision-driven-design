# What the rewritten product-cli promises and refuses

The rewritten product-cli promises a machine-checkable statement of what a product does, with an executable oracle for its behaviour, exported as one graph that someone else can sign. An agent proposes, and the author [adopts](#term-adoption) or rejects each [proposal](#term-proposal). The tool puts nothing in force; what the [canonical document](#term-canonical-document) is held against, who accepts it and from which position it is in force belong to [Writ](#term-writ).

## Chapter by chapter

- **The promise.** [The What](#term-the-what) is authored in conversation, and every step of it is a decision. Each adoption is a [decision record](#term-decision-record) with its reason, so every element of the What traces to the person who adopted it. The What is a graph with [shapes](#term-shape), and the tool says so when something is not yet specified. Behaviour is executable before any code exists, and the same [scenarios](#term-scenario) later judge realised code. The tool decides nothing about realisation.
- **Who it is for.** Three roles share one surface: an author who adopts or rejects proposals, an agent that writes only proposals, and a [realiser](#term-realiser) who needs an oracle.
- **The surface.** An agent's write is a proposal, which the author adopts or rejects, and `accepted` means adopted into the author's draft, carrying no force, permission or [grant](#term-grant); the agent surface has no adopt, reject, land, grant or signing.
- **The guarantees.** Each guarantee is a property test, and the suite is public. No [change set](#term-change-set) enters the [draft log](#term-draft-log) if it carries a [violation](#term-violation). Each coverage gap is a [finding](#term-finding), never a silent pass. The tool holds no key and no grant, and puts nothing in force. Nothing an agent wrote is in the What unless a person adopted it.
- **Boundaries and decisions taken.** The scope is the What alone, without the How, work units, features, releases or code generation, and the tool records decisions and never puts one in force.

## Terms used here

- <a id="term-adoption"></a>**adoption**: The author's acceptance of a proposal, recorded as a new version of its decision with status accepted and the change set pinned.
- <a id="term-proposal"></a>**proposal**: An agent's write: a set of changes held beside the head of the draft log, not in it, until the author adopts or rejects it.
- <a id="term-canonical-document"></a>**canonical document**: The What graph at one draft position, written out in one fixed canonical form; the only graph document Writ lands.
- <a id="term-writ"></a>**Writ**: not explained in this definition.
- <a id="term-the-what"></a>**the What**: The opinionated specification of what a software application is and does: its declared ground, and the tolerance each act must meet.
- <a id="term-decision-record"></a>**decision record**: not explained in this definition.
- <a id="term-shape"></a>**shape**: A check, written in SHACL, that is applied to each node of a given kind in the graph.
- <a id="term-scenario"></a>**scenario**: An element within a Decider or Projector with three parts: prior events given, a command or event applied, and the result expected.
- <a id="term-realiser"></a>**realiser**: An engineer, or a build agent under Writ, who builds the code and runs the behavioural-conformance runner against it.
- <a id="term-grant"></a>**grant**: not explained in this definition.
- <a id="term-change-set"></a>**change set**: not explained in this definition.
- <a id="term-draft-log"></a>**draft log**: The working copy, kept as a positioned log of its own in Git, in which every verb is a commit.
- <a id="term-violation"></a>**violation**: A severity for a failed check: the write is refused.
- <a id="term-finding"></a>**finding**: not explained in this definition.
