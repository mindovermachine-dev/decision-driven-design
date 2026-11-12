# product-cli: what a product does, made checkable

The rewritten product-cli promises a machine-checkable statement of what a product does, with an executable oracle for its behaviour, exported as one graph that someone else can sign. The tool puts nothing in force and decides nothing about realisation; acceptance and force belong to [Writ](#term-writ). An agent writes only [proposals](#term-proposal), and nothing an agent wrote is in [the What](#term-the-what) unless a person [adopted](#term-adoption) it.

## Chapter by chapter

- **The promise.** The What is authored in conversation, where an agent proposes and the author adopts or rejects, and its behaviour is executable before code exists.
- **Who it is for.** The tool serves an author who adopts or rejects the agent's proposals, an agent who writes only proposals, and a [realiser](#term-realiser) who needs an oracle to realise against.
- **The surface.** Every agent write is a proposal that the author adopts or rejects, and `accepted` means adopted into the author's draft, carrying no force, permission or [grant](#term-grant).
- **The formats.** Every format is under a read-forever rule from the first release, and the tool's published [profile](#term-profile) states that no record of this system binds anyone.
- **The guarantees.** Each guarantee is a property test in a public suite, and the tool holds no key and puts nothing in force.
- **Implementation.** The implementation may change without the product changing, and the order of work ends by retiring the Rust binary.
- **Boundaries and decisions taken.** The scope is the What alone, without the How, work units, features, releases or code generation, and the tool records decisions and never puts one in force.
- **Cross-repository dependencies.** Most cross-repository dependencies are met; still open are Writ landing canonical N-Quads as the What document and Writ's embedded log and `land`.

## Terms used here

- <a id="term-writ"></a>**Writ**: not explained in this definition.
- <a id="term-proposal"></a>**proposal**: An agent's write: a set of changes held beside the head of the draft log, not in it, until the author adopts or rejects it.
- <a id="term-the-what"></a>**the What**: The opinionated specification of what a software application is and does: its declared ground, and the tolerance each act must meet.
- <a id="term-adoption"></a>**adoption**: The author's acceptance of a proposal, recorded as a new version of its decision with status accepted and the change set pinned.
- <a id="term-realiser"></a>**realiser**: An engineer, or a build agent under Writ, who builds the code and runs the behavioural-conformance runner against it.
- <a id="term-grant"></a>**grant**: not explained in this definition.
- <a id="term-profile"></a>**profile**: A published statement of what this tool's record statuses mean, that its records bind no one, and which members and identity schemes it uses.
