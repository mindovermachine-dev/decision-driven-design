---
name: product-definition
culture: en
format: brief
derived-from: product-definition.source.md
source-blob: 5b96fe974ba4b05c07e0166d634fb7554f3746cd
format-version: 0
culture-version: 0
rendered: [P0.1, P0.2, P1, P1.4, P1.6, P2, P3, P4, P4.3, P4.4, W0.1, W0.2, W1.1, W2.1, W2.2, W3.0, W4.0, W5.0, W6, W7.1, W8.1, W9.1, W10.1, W10.4, W11.1, W12]
gaps:
  - The source does not state what is to be authorised, continued or stopped, or the current state of the work.
  - The source states no cost, schedule or risk.
  - The source does not say which four consequences P0.2 means.
  - The source does not explain `dpp/1`, Writ, the edition, the What, Decider, Projector or the draft log.
  - The source does not say who the author is, or who "someone else" in P0.1 is.
  - The source's statements do not say what was left out; only its frontmatter says it covers chapter 1 and chapter 5.
---

# Product definition

## What it is

The product is a machine-checkable statement of what a product does, with an executable oracle for its behaviour, exported as one graph that someone else can sign. [P0.1]
Four consequences follow from the promise and are the whole product. [P0.2]

## What it commits to

- The What is authored in conversation, and every step of it is a decision. [P1]
- Each adoption is a `dpp/1` decision record with its reason. [P1.4] As a consequence, every element of the What traces to the person who adopted it. [P1.6]
- The What is a graph with shapes, never prose with diagrams. [P2]
- Behaviour is executable before any code exists. [P3] Simulation comes before realisation. [W6]
- Each guarantee is a property test, and the suite is public. [W0.1, W0.2]
- No change set enters the draft log if it carries a violation. [W1.1] Signatures are computed from the graph. [W2.1, W2.2] Coverage gaps and orphans are findings. [W3.0, W4.0] Each type-boundary breach is refused at write. [W5.0]
- Two exports of the same draft position are byte-identical. [W7.1] Importing a canonical export yields a draft whose export is byte-identical to the input. [W8.1]
- The draft log is a conformant system under `dpp/1` §8. [W11.1]

## What it does not do

- The tool puts nothing in force and decides nothing about realisation. [P4]
- The tool holds no key and no grant, and writes to no log but its own draft log. [W10.1, W10.4]
- Nothing an agent wrote is in the What unless a person adopted it. [W12]
- An agent session cannot author a node before the nodes it derives from exist. [W9.1]

## Open for review

- The tool produces a canonical document. [P4.3] Unverified: whether the ruling in its basis extends to this statement. [P4.3]
- What the canonical document is held against, who accepts it under which grant, and from which position it is in force, belong to Writ. [P4.4] Unverified: the same question of extent. [P4.4]
