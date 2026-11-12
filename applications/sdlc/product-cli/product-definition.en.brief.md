---
name: product-definition
culture: en
format: brief
audience: authoriser
derived-from: product-definition.md
canon-blob: 8019dc03ce2e4083bcfafbe8b6625f7fae901b24
summaries-of-canon-blob: 8019dc03ce2e4083bcfafbe8b6625f7fae901b24
format-version: 2
assembled-by: script, from stored summaries, an audience top and the glossary
cites:
- C0
- C1
- C2
- C3.3
- C3.6
- C4
- C4.5
- C5
- C7
- C8
- CX
terms-without-explanation:
- Writ
- head
- grant
---

# Product: product definition

This is the definition of the rewritten product-cli, which replaces the Rust workspace of the same name. [C0] The promise is a machine-checkable statement of what a product does, with an executable oracle for its behaviour, exported as one graph that someone else can sign. [C1] The tool puts nothing in force; acceptance and force belong to [Writ](#term-writ), and nothing an agent wrote is in [the What](#term-the-what) unless a person [adopted](#term-adoption) it. [C1, C5]

## Chapter by chapter

- **The promise.** The What is authored in conversation, where an agent proposes and the author adopts or rejects; the tool decides nothing about realisation, and acceptance and force belong to Writ. [C1]
- **Who it is for.** It is for an author, an agent that writes only [proposals](#term-proposal), and a [realiser](#term-realiser) who needs an oracle to realise against; neither author nor realiser edits the other's artefact. [C2]
- **The surface.** An agent's write is a proposal beside [the head](#term-head), which the author adopts or rejects; the agent surface has no adopt, reject, land, [grant](#term-grant) or signing. [C3.3, C3.6]
- **The formats.** Every format is under a read-forever rule from the first release, and the tool's published [profile](#term-profile) states that no record of this system binds anyone. [C4, C4.5]
- **The guarantees.** Each guarantee is a property test in a public suite; the tool holds no key, and nothing an agent wrote is in the What unless a person adopted it. [C5]
- **Implementation.** This chapter may change without chapters 1 to 6 changing, and the order of work ends by retiring the Rust binary. [C7]
- **Boundaries and decisions taken.** The scope is the What alone: the How, work units, features, releases and code generation are not in it, and the tool records decisions and never puts one in force. [C8]
- **Cross-repository dependencies.** Most cross-repository dependencies are met; still open are Writ landing canonical N-Quads as the What document and Writ's embedded log and `land`. [CX]

Left out for this reader: The contracts between parts.

## Terms used here

- <a id="term-writ"></a>**Writ**: not explained in the canon. Writ is a system outside this repository.
- <a id="term-the-what"></a>**the What**: The opinionated specification of what a software application is and does: its declared ground, and the tolerance each act must meet. *(`what.md`, "1.1 What the What is")*
- <a id="term-adoption"></a>**adoption**: The author's acceptance of a proposal, recorded as a new version of its decision with status accepted and the change set pinned. *(`product-definition.md`, "Proposals and decisions")*
- <a id="term-proposal"></a>**proposal**: An agent's write: a set of changes held beside the head of the draft log, not in it, until the author adopts or rejects it. *(`product-definition.md`, "Proposals and decisions")*
- <a id="term-realiser"></a>**realiser**: An engineer, or a build agent under Writ, who builds the code and runs the behavioural-conformance runner against it. *(`product-definition.md`, "2. Who it is for")*
- <a id="term-head"></a>**head**: not explained in the canon. No explanation was found.
- <a id="term-grant"></a>**grant**: not explained in the canon. It is Writ's term, and Writ is outside this repository.
- <a id="term-profile"></a>**profile**: A published statement of what this tool's record statuses mean, that its records bind no one, and which members and identity schemes it uses. *(`product-definition.md`, "Decision records and the profile")*
