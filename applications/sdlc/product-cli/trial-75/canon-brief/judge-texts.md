## Text T1

- The product is a machine-checkable statement of what a product does, with an executable oracle for its behaviour, exported as one graph that someone else can sign. An agent proposes and the author adopts or rejects each proposal, and every element of the What traces to the person who adopted it. The tool puts nothing in force: acceptance of its canonical document and its being in force belong to Writ.
- The product is a machine-checkable statement of what a product does, with an executable oracle for its behaviour, exported as one graph that someone else can sign. An agent proposes and the author adopts or rejects each proposal, and every element of the What traces to the person who adopted it. The tool's records carry no force; acceptance of its canonical document and its being in force belong to Writ.
- Each guarantee is a property test in a public suite. The tool holds no key and no grant and puts nothing in force, and a proposal never reaches the head of the draft log on its own. No change set carrying a violation enters the draft log, coverage gaps and orphans are findings, and a What with a failing scenario exports but its What-version record says so.

## Text T2

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

## Text T3


# Product: product definition

This is the definition of the rewritten product-cli, which replaces the Rust workspace of the same name. [C0] The promise is a machine-checkable statement of what a product does, with an executable oracle for its behaviour, exported as one graph that someone else can sign. [C1] The tool puts nothing in force; acceptance and force belong to Writ, and nothing an agent wrote is in the What unless a person adopted it. [C1, C5]

## Chapter by chapter

- **The promise.** The What is authored in conversation, where an agent proposes and the author adopts or rejects; the tool decides nothing about realisation, and acceptance and force belong to Writ. [C1]
- **Who it is for.** It is for an author, an agent that writes only proposals, and a realiser who needs an oracle to realise against; neither author nor realiser edits the other's artefact. [C2]
- **The surface.** An agent's write is a proposal beside the head, which the author adopts or rejects; the agent surface has no adopt, reject, land, grant or signing. [C3.3, C3.6]
- **The formats.** Every format is under a read-forever rule from the first release, and the tool's published profile states that no record of this system binds anyone. [C4, C4.5]
- **The guarantees.** Each guarantee is a property test in a public suite; the tool holds no key, and nothing an agent wrote is in the What unless a person adopted it. [C5]
- **Implementation.** This chapter may change without chapters 1 to 6 changing, and the order of work ends by retiring the Rust binary. [C7]
- **Boundaries and decisions taken.** The scope is the What alone: the How, work units, features, releases and code generation are not in it, and the tool records decisions and never puts one in force. [C8]
- **Cross-repository dependencies.** Most cross-repository dependencies are met; still open are Writ landing canonical N-Quads as the What document and Writ's embedded log and `land`. [CX]

Left out for this reader: The contracts between parts.

## Terms used here

- **Writ**: not explained in the canon. Writ is a system outside this repository.
- **the What**: The opinionated specification of what a software application is and does: its declared ground, and the tolerance each act must meet. *(`what.md`, "1.1 What the What is")*
- **adoption**: The author's acceptance of a proposal, recorded as a new version of its decision with status accepted and the change set pinned. *(`product-definition.md`, "Proposals and decisions")*
- **proposal**: An agent's write: a set of changes held beside the head of the draft log, not in it, until the author adopts or rejects it. *(`product-definition.md`, "Proposals and decisions")*
- **realiser**: An engineer, or a build agent under Writ, who builds the code and runs the behavioural-conformance runner against it. *(`product-definition.md`, "2. Who it is for")*
- **head**: not explained in the canon. No explanation was found.
- **grant**: not explained in the canon. It is Writ's term, and Writ is outside this repository.
- **profile**: A published statement of what this tool's record statuses mean, that its records bind no one, and which members and identity schemes it uses. *(`product-definition.md`, "Decision records and the profile")*

