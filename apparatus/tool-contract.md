# The Tool Contract

<!-- ddd:doc
reader: an engineer building the harness for a local agent
act: specify what each tool response must declare, and bind a toolset to a task before the run
pin: v5.15.1
basis: [DDD-floor-01, term:governing-decision, term:admission-test, term:escape, term:judgment, term:encoded, term:closure, term:seam-identity, term:poisoned-ground, term:encode-verify-split, held:2026-10-26-doc-format/P-2, held:2026-10-26-doc-format/P-3, held:2026-10-26-doc-format/P-8, held:2026-10-26-doc-format/P-9, held:2026-10-26-doc-format/P-10]
status: held
supersedes: 5e649a1:apparatus/tool-contract.md
-->

**This is for you if you are building the harness around a local agent:** the code that gives a model its tools, runs it on a task, and decides what to trust in what comes back.

After reading it you will be able to do three things:
1. Say what every tool response must declare, so the harness can tell a current fact from an expired one.
2. Bind a toolset to a task **before the run**, and state which of the task's decisions are resolved, which are verified, and which nothing covers.
3. Give the agent a way to stop when it needs a tool you did not give it.

**Scope.** In-process tools, called by a local agent, on a machine you control. There is no server, no transport, no discovery and no capability negotiation. Those exist to bridge trust between strangers, and a local agent calling its own tools has no strangers to bridge. Paying for that machinery adds a seam you do not need (`term:seam-identity`).

**What this rests on.** Some of it is canon. Some of it is not yet, and is marked **held** where it is used.

| Basis | Status |
|---|---|
| The floor mechanism: residual demand escapes where an actor is overloaded **and** the decision has no verifier (`DDD-floor-01`) | canon, reported |
| Governing decision, admission test, escape, judgment and encoded stores, closure (upstream terms) | canon |
| Poisoned ground, and the encode/verify split (upstream terms) | canon, but **not yet pinned** in this repository |
| Control decides which side of the encode/verify split ground falls on (P-2) | **held** |
| Tool classes: exporter, resolver, verifier (P-3) | **held** |
| Classes need pinned ground (P-8); model-picked tools escape (P-9); a fixed toolset makes the open set computable (P-10) | **held** — results of this document, registered for filing |

---

## The contract in one paragraph

A tool response declares what ground it touched, whether that ground is controlled, and how to tell if it still holds. Only then is it meaningful to ask what the call resolved, what it left open and what it verified. Only then can a harness bind a toolset and state, before the run, exactly which decisions have nowhere to live.

---

## 1. What every tool response declares

A tool declares only what a tool can know. It does not know the task, so it does not declare its own class; the harness works that out (§2).

| Field | Values | Why the harness needs it |
|---|---|---|
| **Ground relation** | `controlled` or `uncontrolled` | A controlled response *is* the source of truth, so it cannot be stale. An uncontrolled one is a reading of something owned elsewhere, so it can. |
| **Observed at** | a timestamp | Only for uncontrolled responses. When the reading was taken. |
| **Revalidation** | how to check it still holds | Only for uncontrolled responses. See the rules below. |
| **Resolution** | `resolved` or `unresolved` | Resolved: the tool made the decision, and the agent reads a fact (a symbol lookup, a typed query). Unresolved: the tool handed over material, and every inference the agent now makes is an open decision this call created. |
| **Still to decide** | a short list | For unresolved responses, where the tool can say. "4000 lines; locating the definition and its type are unresolved" lets the harness count the open set. "4000 lines" does not. |
| **Bounded** | yes, and by what; or no | Unbounded output is what overloads an agent. A tool that cannot bound its output says so, and the harness bounds it at the call site or does not bind the tool. |
| **Verdict** | what it checked, and what it did not | Only for tools that check the agent's own output: tests, type checks, schema validation. These are the only declarations that reduce escape, because they turn an escape into a retry (`DDD-floor-01`). |

**Four rules go with the table.**

1. **Declare per response, not per tool.** The same `fetch` tool reading a workspace file and reading a remote URL touches different ground under one name. The declaration is runtime data on the response, not metadata on the tool.
2. **Revalidate by default.** If checking is cheap, check on every call. A local tool that can re-stat a file, re-read an mtime or compare a hash has no excuse for serving a cached claim. Where checking is expensive, prefer a cheap validator (etag, version, content hash, mtime) to a time-to-live. A validator asks the source; a TTL guesses on its behalf. A TTL is a promise about someone else's system, an observation with an expiry and no alarm on it **(held: P-2)**.
3. **A lapsed response is not a valid pin.** It may still be returned. But the harness treats every decision that depends on it as unpinned, and the agent's attribution for those decisions does not hold.
4. **A verdict states its scope.** A passing test suite is a verdict on the behaviour under test. It says nothing about conventions or structure. Overstating a verdict's scope is how open decisions get treated as closed.

---

## 2. What the harness does before the run

The harness supplies what tools cannot know, and it does so **at bind time, before the run**:

1. **List the task's governing decisions** at its declared assurance level: the choices that, if varied, would move the outcome past tolerance (`term:admission-test`).
2. **Bind a toolset.** From the tools' declarations, mark each decision:
   - **resolved** — some bound tool decides it,
   - **verified** — some bound verdict checks it,
   - **open** — neither. This is the set that can escape (`DDD-floor-01`).
3. **Freeze the binding.** The toolset is fixed for the run.

Show the open set to whoever owns the task before the run starts. Every decision on it has nowhere to live.

### Why the model never picks the tools

Choosing a tool is itself a governing decision. Vary it and the outcome moves, so it is demand, and something must carry it.

- **If the model picks tools mid-run**, that choice is made in the judgment store: per run, under load, and with nothing to check it, because no test of "was that the right tool here?" exists at the moment of choosing. An open decision, made under load, unchecked, is exactly where escape happens. **(held: P-9)** This is not a claim that models choose badly. It is that the choice has no backstop, so it fails when the run is loaded, which is when it matters.
- **If the harness binds the toolset**, the same decision moves to the encoded store: made once, before the act, against the task's decision set, and reused across runs.

There is a second reason, and it is the stronger one. **A fixed toolset makes the open set computable before the run. (held: P-10)** If the model may add tools mid-run, the open set moves while you watch, and you can only observe it afterwards. Binding is what makes the analysis in step 2 possible at all.

### Why ground comes first

Everything in §1 starts with the ground relation, for a reason. A tool that resolves against stale ground still answers with a resolver's authority, and the answer is confidently wrong. That is poisoned ground (`term:poisoned-ground`) dressed as a resolver. It is worse than handing over raw material, because raw material at least invites a second look.

So the tool classes only mean something over pinned ground. **(held: P-8)** Unpinned, every tool behaves like an exporter: the agent must keep asking "is this still true?", and that question is an open decision the tool created by declining to answer it.

---

## 3. When the agent needs a tool you did not bind

A fixed binding gives up some adaptivity. The task may need something you did not anticipate. **An unanticipated tool need is an unanticipated decision**, and surfacing it is the correct outcome, but only if there is a path for it.

Give the agent a way to declare "this task needs a capability I was not given", and to **stop**. The decision goes to a human. Without this path the agent improvises with what it has, and the escape you prevented at bind time comes back one level down, disguised as a completed run. The refusal path is what keeps binding honest.

---

## 4. What this contract leaves out, deliberately

| Left out | Why |
|---|---|
| Server, transport, lifecycle | Solved problems, for a problem this scope does not have |
| Discovery and capability negotiation | The harness knows its tools at build time; it wrote them |
| Dynamic tool loading | See §2: the model never picks the tools |
| Tool-declared class | Class depends on the tool, the task and how the output is used (held: P-3). The harness computes it. |

Two things are kept from the protocol lineage, because they route decisions rather than distribute tools:
- **Elicitation:** route a decision the agent cannot make to a human (§3).
- **Sampling:** route a decision to another model across a seam (`term:seam-identity`).

**Related.** Foundations RFC 0005 makes the same requirement one level up: a context fragment must declare its ground relation, as a tool response must here. The RFC lives outside this repository.

---

## Worked example

A local agent is asked "which services read the config key `retry.max`?". It has three tools.

| Tool | Ground | Resolution | Bounded | Verdict |
|---|---|---|---|---|
| `grep_repo` (searches the workspace) | controlled | unresolved: "which matches are reads, not writes or comments, is still to decide" | yes, first 200 matches | — |
| `config_service.get` (remote config service) | uncontrolled; observed at 10:02; revalidate by version number | resolved | yes | — |
| `run_contract_tests` | controlled | resolved | yes | checks the services' config-loading tests; does **not** check services without tests |

At bind time the harness lists the decisions: which files read the key; which services those files belong to; whether the remote value matters to the answer. It marks the file-to-service mapping as **open**: no bound tool resolves it, and no verdict checks it. It shows that before the run. If, mid-run, the agent finds a service whose config lives in a database it cannot read, it declares the missing capability and stops.
