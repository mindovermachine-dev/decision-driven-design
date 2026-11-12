# The brief, with the keys each sentence rests on

- (summary) product-cli yields a machine-checkable statement of what a product does, with an executable oracle for its behaviour, exported as one graph that someone else can sign. [C0, C1]
- (summary) An agent proposes each step in conversation and the author adopts or rejects it, a Decider and a Projector are simulated against scenarios drawn from the flows, and the same scenarios later judge realised code. [C1]
- (summary) It puts nothing in force; Writ lands the canonical document it produces. [C1, C3.1]
- (C1) The What is authored in conversation, and every step of it is a decision: an agent proposes, and the author adopts or rejects each proposal. [C1]
- (C1) The What is a graph with shapes, never prose with diagrams. [C1]
- (C1) Behaviour is executable before any code exists: a Decider and a Projector are simulated against scenarios that later judge realised code. [C1]
- (C1) The tool puts nothing in force and decides nothing about realisation. [C1]
- (C2) Three roles share one surface: an author who models the product and adopts or rejects proposals, an agent that writes only proposals, and a realiser who runs the behavioural-conformance runner against realised code. [C2]
- (C3) Every verb is a commit to the draft log, kept in Git. [C3.2]
- (C3) An agent's write is a proposal held beside the head, and the author adopts or rejects it. [C3.3]
- (C3) The workbench serves a live view of the draft log in a browser. [C3.4]
- (C3) An agent session uses the same verbs over MCP and ends with an export. [C3.6]
- (C4) Every format has a specification page and a conformance suite before any implementation, and the canonical export is the graph document plus the logic artefacts its digests name, byte-identical for the same draft position. [C4, C4.3]
- (C5) Guarantees are tested in a public suite; nothing an agent wrote is in the What unless a person adopted it. [C5]
- (C8) The scope is the What alone; the How and code generation are not in it. [C8]

## Terms used here

- **adoption**: The author's acceptance of a proposal, recorded as a new version of its decision with status accepted and the change set pinned. *(`product-definition.md`, "Proposals and decisions")*
- **Decider**: The place where the business rules for one aggregate live: it accepts or rejects each command, and says which events result when it accepts. *(`what.md`, "3.3 The Decider — the executable form of behaviour")*
- **Projector**: The executable form of a read model: a fold that takes the current state and an event and gives the new state. *(`what.md`, "3.4 The Projector — the executable form of a read model")*
- **scenario**: An element within a Decider or Projector with three parts: prior events given, a command or event applied, and the result expected. *(`product-definition.md`, "Scenarios and the wire protocol")*
- **flow**: A chain of slices, where a slice is a single instance of a pattern on the graph. *(`what.md`, "3.2.0 Building blocks and patterns")*
- **canonical document**: The What graph at one draft position, written out in one fixed canonical form; the only graph document Writ lands. *(`product-definition.md`, "The canonical export")*
- **the What**: The opinionated specification of what a software application is and does: its declared ground, and the tolerance each act must meet. *(`what.md`, "1.1 What the What is")*
- **proposal**: An agent's write: a set of changes held beside the head of the draft log, not in it, until the author adopts or rejects it. *(`product-definition.md`, "Proposals and decisions")*
- **shape**: A check, written in SHACL, that is applied to each node of a given kind in the graph. *(`product-definition.md`, "Shapes")*
- **realiser**: An engineer, or a build agent under Writ, who builds the code and runs the behavioural-conformance runner against it. *(`product-definition.md`, "2. Who it is for")*
- **draft log**: The working copy, kept as a positioned log of its own in Git, in which every verb is a commit. *(`product-definition.md`, "The draft log")*
- **workbench**: A live, local view of the draft log in a browser, where pending proposals can be adopted or rejected. *(`product-definition.md`, "The workbench")*
