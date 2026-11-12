# The brief, with the keys each sentence rests on

- (summary) The rewritten product-cli promises a machine-checkable statement of what a product does, with an executable oracle for its behaviour, exported as one graph that someone else can sign.. [C0, C1]
- (summary) An agent proposes, and the author adopts or rejects each proposal.. [C1]
- (summary) The tool puts nothing in force; what the canonical document is held against, who accepts it and from which position it is in force belong to Writ.. [C1]
- (C1) The What is authored in conversation, and every step of it is a decision.. [C1]
- (C1) Each adoption is a decision record with its reason, so every element of the What traces to the person who adopted it.. [C1]
- (C1) The What is a graph with shapes, and the tool says so when something is not yet specified.. [C1]
- (C1) Behaviour is executable before any code exists, and the same scenarios later judge realised code.. [C1]
- (C1) The tool decides nothing about realisation.. [C1]
- (C2) Three roles share one surface: an author who adopts or rejects proposals, an agent that writes only proposals, and a realiser who needs an oracle.. [C2]
- (C3) An agent's write is a proposal, which the author adopts or rejects, and `accepted` means adopted into the author's draft, carrying no force, permission or grant; the agent surface has no adopt, reject, land, grant or signing.. [C3.3, C3.6]
- (C5) Each guarantee is a property test, and the suite is public.. [C5]
- (C5) No change set enters the draft log if it carries a violation.. [C5]
- (C5) Each coverage gap is a finding, never a silent pass.. [C5]
- (C5) The tool holds no key and no grant, and puts nothing in force.. [C5]
- (C5) Nothing an agent wrote is in the What unless a person adopted it.. [C5]
- (C8) The scope is the What alone, without the How, work units, features, releases or code generation, and the tool records decisions and never puts one in force.. [C8]

## Terms used here

- **adoption**: The author's acceptance of a proposal, recorded as a new version of its decision with status accepted and the change set pinned. *(`product-definition.md`, "Proposals and decisions")*
- **proposal**: An agent's write: a set of changes held beside the head of the draft log, not in it, until the author adopts or rejects it. *(`product-definition.md`, "Proposals and decisions")*
- **canonical document**: The What graph at one draft position, written out in one fixed canonical form; the only graph document Writ lands. *(`product-definition.md`, "The canonical export")*
- **the What**: The opinionated specification of what a software application is and does: its declared ground, and the tolerance each act must meet. *(`what.md`, "1.1 What the What is")*
- **shape**: A check, written in SHACL, that is applied to each node of a given kind in the graph. *(`product-definition.md`, "Shapes")*
- **scenario**: An element within a Decider or Projector with three parts: prior events given, a command or event applied, and the result expected. *(`product-definition.md`, "Scenarios and the wire protocol")*
- **realiser**: An engineer, or a build agent under Writ, who builds the code and runs the behavioural-conformance runner against it. *(`product-definition.md`, "2. Who it is for")*
- **draft log**: The working copy, kept as a positioned log of its own in Git, in which every verb is a commit. *(`product-definition.md`, "The draft log")*
- **violation**: A severity for a failed check: the write is refused. *(`product-definition.md`, "Shapes")*
