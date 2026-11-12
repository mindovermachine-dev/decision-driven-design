---
name: product-definition
culture: en
format: brief
derived-from: product-definition.source.md
source-blob: 15145480aba5398566027a22ccd2983f7689ca6b
format-version: 1
culture-version: 0
rendered: [I0.1, I0.2, I0.3, I0.4, I0.5, P0.1, P0.2, P0.3, P1, P2, P3, P4, P4.3, P4.4, W0.1, W0.2, W0.3, W0.4, W0.5, W0.6, W1, W2, W3, W3.0, W4, W4.0, W5, W5.0, W6, W7, W7.1, W8, W8.1, W9, W9.1, W10, W11, W12]
gaps:
  - "The source does not state which decision the reader is asked to make: what is to be authorised, continued or stopped."
  - "The source does not state the state of the work: what is built, what remains, or any cost or date."
  - "I0.4 and I0.5 name chapters 1 to 7, but the source holds only chapters 1 and 5."
  - "The source does not state why the rewritten product-cli replaces the Rust workspace."
---

# Product: product definition

This is the definition of the rewritten product-cli, which replaces the Rust workspace of the same name. [I0.1, I0.2] The definition is written outside-in: the promise first, the implementation last. [I0.3] Chapters 1 to 6 are the product. [I0.4] Chapter 7 is how the product happens to be built, and may change without the product changing. [I0.5]

## The promise

The product is a machine-checkable statement of what a product does, with an executable oracle for its behaviour, exported as one graph that someone else can sign. [P0.1] Four consequences follow from the promise and are the whole product. [P0.2] Everything below the promise is how. [P0.3]

- The What is authored in conversation, and every step of it is a decision. [P1]
- The What is a graph with shapes, never prose with diagrams. [P2]
- Behaviour is executable before any code exists. [P3]
- The tool puts nothing in force and decides nothing about realisation. [P4]

## The guarantees

Each guarantee is a property test over generated What graphs and scenarios, and the suite of property tests is public. [W0.1, W0.2] Every test observes bytes, in the draft log or in an export, never the return value of the verb that produced them. [W0.3] W1 and W5 are the edition's violations. [W0.4] W3 and W4 are the edition's warnings. [W0.5] The checks themselves are the edition's shapes, not code in this tool. [W0.6]

- Shape before storage. [W1]
- Derived, not declared. [W2]
- Coverage: each coverage gap is a finding, never a silent pass. [W3, W3.0]
- Justification: orphans are findings. [W4, W4.0]
- Type boundary: each type-boundary breach is refused at write, not reported later. [W5, W5.0]
- Simulation before realisation. [W6]
- Canonical export: two exports of the same draft position are byte-identical, on every platform, graph and logic artefacts alike. [W7, W7.1]
- Round-trip: importing a canonical export yields a draft whose export is byte-identical to the input, graph and artefacts. [W8, W8.1]
- Phase order: an agent session cannot author a node before the nodes it derives from exist. [W9, W9.1]
- Nothing in force, nothing landed. [W10]
- Decision-provenance conformant. [W11]
- Nothing an agent wrote is in the What unless a person adopted it. [W12]

## Open for review

- The tool produces a canonical document; the definition places the D1.11 marker before P4.1, and whether the ruling extends to P4.3 and P4.4 is read from position, not stated. [P4.3]
- What the canonical document is held against, who accepts it under which grant, and from which position it is in force, belong to Writ; the same question of extent as P4.3 is unverified. [P4.4]
