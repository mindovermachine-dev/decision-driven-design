---
name: product-definition
culture: en
format: brief
derived-from: product-definition.source.md
source-blob: 15145480aba5398566027a22ccd2983f7689ca6b
format-version: 2
culture-version: 0
assembled-by: script, from stored summaries
rendered:
- DOC
- CH1
- P1
- P2
- P3
- P4
- CH5
- W1
- W2
- W3
- W4
- W5
- W6
- W7
- W8
- W9
- W10
- W11
- W12
- P4.3
- P4.4
---

# Product: product definition

This is the definition of the rewritten product-cli, written outside-in: the promise first, the implementation last. The product is a machine-checkable statement of what a product does, with an executable oracle for its behaviour, exported as one graph that someone else can sign. The tool records the author's decisions as `dpp/1` records carrying no force, holds no key and puts nothing in force, and each guarantee is a public property test over generated What graphs and scenarios. [DOC]

## The promise

The product is a machine-checkable statement of what a product does, with an executable oracle for its behaviour, exported as one graph that someone else can sign. The What is authored in conversation as a graph with shapes, and its behaviour is executable before code exists. The tool records the author's decisions as `dpp/1` records carrying no force, while acceptance and position in force belong to Writ. [CH1]

- The What is authored in conversation: an agent proposes, the author adopts or rejects, and each adoption is a `dpp/1` decision record tracing every element to its adopter. [P1]
- The What is a graph with shapes, and the tool says that anything that cannot be stated as a node, an edge or a shape is not yet specified. [P2]
- Behaviour is executable before code exists: a Decider and a Projector are simulated sound and complete against scenarios drawn from the flows, and the same scenarios later judge realised code. [P3]
- The tool records the author's decisions as `dpp/1` records carrying no force and produces a canonical document, while its acceptance and position in force belong to Writ. [P4]

## The guarantees

Each guarantee is a public property test over generated What graphs and scenarios, and every test observes bytes in the draft log or in an export. A change set carrying a violation, a disagreeing signature and a type-boundary breach are kept out or refused, coverage gaps and orphans are findings, and exports are simulated before being marked ready and are byte-identical across platforms and through import. The tool holds no key and puts nothing in force, and every change at the head of the draft log is attached to a decision record whose `by` is the author. [CH5]

- No change set carrying a violation enters the draft log, and a failed write leaves the log unchanged. [W1]
- A Decider's and a Projector's signatures are computed from the graph, and an authored signature or logic that disagrees with the computed signature is refused. [W2]
- Each coverage gap is a finding, never a silent pass: commands are handled, events folded, command and subject kind pairs shown by scenarios, surfaced Views scoped, and triggers given subjects. [W3]
- Orphans are findings: every aggregate field, projected field and claim is read, consumed or compared, and every Decider has a reachable rejection. [W4]
- Each type-boundary breach is refused at write: UI steps reference only AIOs, a trigger's present subject matches its `source`, and a journey crosses systems only through a Translation. [W5]
- Every Decider and Projector with scenarios is simulated sound and complete before an export is marked ready, and a What with a failing scenario exports but says so. [W6]
- Two exports of the same draft position are byte-identical on every platform, and every derived export is a deterministic function of the canonical graph and artefacts. [W7]
- Importing a canonical export yields a draft whose export is byte-identical to the input, graph and artefacts. [W8]
- An agent session cannot author a node before the nodes it derives from exist, and the gate is the session transport, not advice in a prompt. [W9]
- The tool holds no key and no grant, puts nothing in force, knows no Writ position, writes only to its own draft log, and exporters produce documents only. [W10]
- The draft log is a conformant system under `dpp/1`, every record it exposes is conformant, and a Writ decision landing the export reaches each author decision and agent proposal. [W11]
- Every change at the head of the draft log is attached to a decision record whose `by` is the author, and a proposal never reaches the head on its own. [W12]

## Open for review

- The tool produces a canonical document. [P4.3] UNVERIFIED — Emil review. The definition places the D1.11 marker before P4.1. Whether the ruling extends to P4.3 and P4.4 is read from position, not stated.
- What the canonical document is held against, who accepts it under which grant, and from which position it is in force, belong to Writ. [P4.4] UNVERIFIED — Emil review. Same question of extent as P4.3.
