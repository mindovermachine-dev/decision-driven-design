## Text T1

- The product is a machine-checkable statement of what a product does, with an executable oracle for its behaviour, exported as one graph that someone else can sign. An agent proposes and the author adopts or rejects each proposal, and every element of the What traces to the person who adopted it. The tool puts nothing in force: acceptance of its canonical document and its being in force belong to Writ.
- The product is a machine-checkable statement of what a product does, with an executable oracle for its behaviour, exported as one graph that someone else can sign. An agent proposes and the author adopts or rejects each proposal, and every element of the What traces to the person who adopted it. The tool's records carry no force; acceptance of its canonical document and its being in force belong to Writ.
- Each guarantee is a property test in a public suite. The tool holds no key and no grant and puts nothing in force, and a proposal never reaches the head of the draft log on its own. No change set carrying a violation enters the draft log, coverage gaps and orphans are findings, and a What with a failing scenario exports but its What-version record says so.

## Text T2

# What the rewritten product-cli promises and refuses

The rewritten product-cli promises a machine-checkable statement of what a product does, with an executable oracle for its behaviour, exported as one graph that someone else can sign. An agent proposes, and the author adopts or rejects each proposal. The tool puts nothing in force; what the canonical document is held against, who accepts it and from which position it is in force belong to Writ.

## Chapter by chapter

- **The promise.** The What is authored in conversation, and every step of it is a decision. Each adoption is a decision record with its reason, so every element of the What traces to the person who adopted it. The What is a graph with shapes, and the tool says so when something is not yet specified. Behaviour is executable before any code exists, and the same scenarios later judge realised code. The tool decides nothing about realisation.
- **Who it is for.** Three roles share one surface: an author who adopts or rejects proposals, an agent that writes only proposals, and a realiser who needs an oracle.
- **The surface.** An agent's write is a proposal, which the author adopts or rejects, and `accepted` means adopted into the author's draft, carrying no force, permission or grant; the agent surface has no adopt, reject, land, grant or signing.
- **The guarantees.** Each guarantee is a property test, and the suite is public. No change set enters the draft log if it carries a violation. Each coverage gap is a finding, never a silent pass. The tool holds no key and no grant, and puts nothing in force. Nothing an agent wrote is in the What unless a person adopted it.
- **Boundaries and decisions taken.** The scope is the What alone, without the How, work units, features, releases or code generation, and the tool records decisions and never puts one in force.

## Terms used here

- **adoption**: The author's acceptance of a proposal, recorded as a new version of its decision with status accepted and the change set pinned.
- **proposal**: An agent's write: a set of changes held beside the head of the draft log, not in it, until the author adopts or rejects it.
- **canonical document**: The What graph at one draft position, written out in one fixed canonical form; the only graph document Writ lands.
- **Writ**: not explained in this definition.
- **the What**: The opinionated specification of what a software application is and does: its declared ground, and the tolerance each act must meet.
- **decision record**: not explained in this definition.
- **shape**: A check, written in SHACL, that is applied to each node of a given kind in the graph.
- **scenario**: An element within a Decider or Projector with three parts: prior events given, a command or event applied, and the result expected.
- **realiser**: An engineer, or a build agent under Writ, who builds the code and runs the behavioural-conformance runner against it.
- **grant**: not explained in this definition.
- **change set**: not explained in this definition.
- **draft log**: The working copy, kept as a positioned log of its own in Git, in which every verb is a commit.
- **violation**: A severity for a failed check: the write is refused.
- **finding**: not explained in this definition.


## Text T3

- The product is a machine-checkable statement of what a product does, with an executable oracle for its behaviour, exported as one graph that someone else can sign. An agent proposes and the author adopts or rejects each proposal, and every element of the What traces to the person who adopted it. The tool puts nothing in force: acceptance of its canonical document and its being in force belong to Writ.
- The product is a machine-checkable statement of what a product does, with an executable oracle for its behaviour, exported as one graph that someone else can sign. An agent proposes and the author adopts or rejects each proposal, and every element of the What traces to the person who adopted it. The tool's records carry no force; acceptance of its canonical document and its being in force belong to Writ.
- Each guarantee is a property test in a public suite. The tool holds no key and no grant and puts nothing in force, and a proposal never reaches the head of the draft log on its own. No change set carrying a violation enters the draft log, coverage gaps and orphans are findings, and a What with a failing scenario exports but its What-version record says so.
- An agent proposes, the author adopts or rejects each proposal, each adoption is a `dpp/1` decision record, and every element of the What traces to the person who adopted it.
- Anything that cannot be stated as a node, an edge or a shape is not yet specified, and the tool says so rather than accepting it.
- A Decider and a Projector are simulated sound and complete against scenarios drawn from the flows, and the same scenarios later judge realised code through a wire protocol.
- The tool records the author's decisions as `dpp/1` records carrying no force and produces a canonical document; its acceptance and its being in force belong to Writ.
- No change set carrying a violation enters the draft log, and a failed write leaves the log unchanged.
- A Decider's and a Projector's signatures are computed from the graph, and an authored signature or logic that disagrees with the computed signature is refused.
- Each coverage gap is a finding, never a silent pass, whether in Decider handling of commands, Projector folding of events, scenarios, scope rules or trigger subjects.
- Orphans are findings; every aggregate field is read by some Decider, every projected field consumed by some step, and every Decider has a reachable rejection.
- Each type-boundary breach is refused at write, not reported later; an absent subject on a trigger is accepted, and a What without subjects exports byte-identically.
- Every Decider and Projector with scenarios is simulated sound and complete before an export is marked ready; a What with a failing scenario exports but its What-version record says so.
- Two exports of the same draft position are byte-identical on every platform, and every derived export is a deterministic function of the canonical graph and artefacts.
- Importing a canonical export yields a draft whose export is byte-identical to the input, graph and artefacts.
- An agent session cannot author a node before the nodes it derives from exist, and the gate is the session transport, not advice in a prompt.
- The tool holds no key and no grant, puts nothing in force, writes to no log but its own draft log, and exporters produce documents only.
- The draft log is a conformant system checked by the `dpp/1` conformance suite, every record it exposes is conformant, and the export's What-version record rests on every decision in force.
- Every change at the head of the draft log is attached to a decision record whose `by` is the author, and a proposal never reaches the head on its own.

## Text T4

# product-cli: what a product does, made checkable

The rewritten product-cli promises a machine-checkable statement of what a product does, with an executable oracle for its behaviour, exported as one graph that someone else can sign. The tool puts nothing in force and decides nothing about realisation; acceptance and force belong to Writ. An agent writes only proposals, and nothing an agent wrote is in the What unless a person adopted it.

## Chapter by chapter

- **The promise.** The What is authored in conversation, where an agent proposes and the author adopts or rejects, and its behaviour is executable before code exists.
- **Who it is for.** The tool serves an author who adopts or rejects the agent's proposals, an agent who writes only proposals, and a realiser who needs an oracle to realise against.
- **The surface.** Every agent write is a proposal that the author adopts or rejects, and `accepted` means adopted into the author's draft, carrying no force, permission or grant.
- **The formats.** Every format is under a read-forever rule from the first release, and the tool's published profile states that no record of this system binds anyone.
- **The guarantees.** Each guarantee is a property test in a public suite, and the tool holds no key and puts nothing in force.
- **Implementation.** The implementation may change without the product changing, and the order of work ends by retiring the Rust binary.
- **Boundaries and decisions taken.** The scope is the What alone, without the How, work units, features, releases or code generation, and the tool records decisions and never puts one in force.
- **Cross-repository dependencies.** Most cross-repository dependencies are met; still open are Writ landing canonical N-Quads as the What document and Writ's embedded log and `land`.

## Terms used here

- **Writ**: not explained in this definition.
- **proposal**: An agent's write: a set of changes held beside the head of the draft log, not in it, until the author adopts or rejects it.
- **the What**: The opinionated specification of what a software application is and does: its declared ground, and the tolerance each act must meet.
- **adoption**: The author's acceptance of a proposal, recorded as a new version of its decision with status accepted and the change set pinned.
- **realiser**: An engineer, or a build agent under Writ, who builds the code and runs the behavioural-conformance runner against it.
- **grant**: not explained in this definition.
- **profile**: A published statement of what this tool's record statuses mean, that its records bind no one, and which members and identity schemes it uses.

