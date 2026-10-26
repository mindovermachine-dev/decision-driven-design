# The Tool Contract

**Location:** proposed `apparatus/tool-contract.md`, or `applications/` if scoped to the local-agent
harness specifically. Derives from the floor mechanism (`core/11`), the encode/verify split
(`apparatus/encode-verify.md`), and tool surfaces (`apparatus/tool-surfaces.md`). It is the
tool-level counterpart of foundations RFC 0005 — **the same ground-relation requirement, one altitude
down.**

**Scope, deliberately narrow.** In-process tools, invoked by a local agent, on a machine you control,
with a harness that binds the toolset per task. **No server, no transport, no discovery, no capability
negotiation.** Those exist to bridge a trust boundary between strangers; a local agent calling its own
tools has no such boundary, and paying for one manufactures seam demand (`core/06`,
`|D_comp| = |D_single| + |S|`) to buy interop it does not need.

---

**Upstream basis.** This document is part of the software projection; it builds on the
principle repo's canon (`actor-indexed-determination`). The `core/NN` references below resolve
there, pinned at a version and a status in `graph/upstream.yaml`:

<!-- ddd:ref id=term:seam-identity -->
<!-- ddd:ref id=DDD-floor-01 -->

## 1. Ground first

The organising claim, and the reason this document does not lead with tools:

> **Tools act on ground. If the ground is not pinned, a tool's demand consequence is undefined —
> because you cannot say what a call *resolves* without knowing what it resolved against.**

A resolver that resolves against **stale** ground is not a resolver. It returns a confidently wrong
answer *with a resolver's authority*, which is worse than an exporter — an exporter at least hands
over raw material the actor might notice is wrong. That is poisoned ground
(`apparatus/closure-principle.md`) wearing a resolver's costume, and it carries the worst signature:
**confident, well-reasoned, catastrophic.**

So the three classes of `apparatus/tool-surfaces.md` carry a precondition that must be stated
plainly:

> **The classes are only meaningful over pinned ground.** Unpinned, every class collapses toward
> *exporter* — because the actor must hold open the question *"is this still true?"*, which is an open
> decision the tool created by declining to answer it.

### 1.1 The gap this addresses

Current tool ecosystems specify **capability** — what may be called, with which arguments, over which
transport — and specify **ground** not at all. The consequence is structural rather than incidental:

> **Capability without ground relation is motion without traction.** You can have flawless capability
> declaration over ground nobody pinned, and the actor still cannot distinguish a current fact from an
> expired one.

This is the same claim foundations RFC 0005 makes about the Context axis, at a different altitude:

| Altitude | Claim |
|---|---|
| **RFC 0005** (WorkUnit) | a context fragment must declare its ground relation, or the C axis is not pinned |
| **This contract** (tool call) | a tool response must declare its ground relation, or the call's demand consequence is undefined |

One concept, two points in the stack.

---

## 2. What a tool must declare

Tools declare **only what tools can know.** The harness supplies the rest (§3). This division is
forced: class depends on ⟨tool, task, consumption⟩ (`tool-surfaces.md` §3), and a tool does not know
the task.

### 2.1 Ground relation — per response, not per tool

Every tool response declares the ground it depended on:

- **controlled** — the tool (or the system it belongs to) is authoritative over what it returned.
  It *is* the ground; it cannot be stale relative to a source of truth because it is the source of
  truth.
- **uncontrolled** — the response is a **reading** of ground owned elsewhere. True as of an
  observation; may have drifted since.

**Per response, not per tool.** Per-tool is simpler and wrong: a fetch tool hitting a local workspace
file and the same tool hitting a remote URL touch different ground under one name. The declaration is
therefore **runtime data on the response**, not static metadata on the tool.

An uncontrolled response additionally carries:

- **observed-at** — when the reading was taken.
- **revalidation** — how to tell whether it still holds (§2.2).

### 2.2 Revalidation — check by default

> **Default: revalidate every call.** If checking is cheap, check. A local tool that can re-stat a
> file, re-read an mtime, or compare a hash has no excuse for serving a cached claim.

**TTL is an optimisation, not the norm**, and it must be justified per tool by the cost of checking.
A TTL is a promise that ground will not move within a window — which is a claim about someone else's
system, and therefore exactly the kind of encoded observation of uncontrolled ground that
`encode-verify.md` warns is a belief with an expiry and no alarm on it.

Where checking is expensive, prefer a **cheap validator** (etag, version, content hash, mtime) over a
wall-clock TTL. A validator asks the source; a TTL guesses on its behalf.

**A lapsed response is not a valid pin.** It may still be returned — but the harness must treat the
decisions depending on it as **unpinned**, and the actor's attribution for them does not hold.

### 2.3 Resolution — what the call decided

Whether the response is an **answer** or **material**:

- **resolved** — a decision was made authoritatively before the actor saw anything (a symbol lookup,
  a typed query). The actor reads a fact.
- **unresolved** — content handed over for the actor to interpret. Every structural inference the
  actor must now perform is an **open decision this call created.**

A tool returning unresolved content should say **what remains to be decided**, where it can. This is
the difference between *"here are 4000 lines"* and *"here are 4000 lines; locating the relevant
definition and determining its type are unresolved."* The second lets the harness count the open set;
the first does not.

### 2.4 Boundedness

Whether the response size is **bounded**, and by what. Unbounded responses are the ground-exporter
signature and the direct driver of the load term in `escape = open_residual × p_err(load)`
(`core/11`). A tool that cannot bound its output must say so, so the harness can bound it at the call
site or decline to bind the tool at all.

### 2.5 Verdict

Whether the call **supplies a closing predicate on the actor's own output** — a test result, a type
check, a schema validation. This is the verifier class, and it is the only declaration that
*subtracts* from the floor: it converts escape into retry (`core/11` §3).

A verdict declares **what it checked** and, critically, **what it did not.** A test suite passing is a
verdict on *the behaviour under test*, not on conventions, structure, or anything else. Overstating a
verdict's scope is how a false sense of coverage is manufactured — and how decisions that are still
open get treated as closed.

---

## 3. What the harness computes

The harness supplies what tools cannot know, and it binds **before the run**.

**Per task, at bind time:**

1. **Enumerate the governing decision set** for the task at its declared assurance level.
2. **Bind a toolset**, and from the tools' declarations compute:
   - which decisions are **resolved** by some bound tool,
   - which are **verified** by some bound verdict,
   - which remain **open** — the escape set (`core/11`: overflow ∩ open, the mechanism of
     capacity-generated escape).
3. **Freeze the binding.** The toolset is fixed for the run.

### 3.1 The LLM never picks tools

**A governing decision, allocated correctly.** Tool selection passes the admission test: vary it and
the outcome moves past tolerance. So it is demand, and it lands in a store.

If the **model** selects tools mid-run, that decision sits in the **judgment store** — per-run,
resolved under load, and with **no verifier**, because no closing predicate on *"was that the right
tool here?"* is available to the model at selection time. Open decision, made under load, unchecked:
**the escape intersection exactly.**

Model-selected tools are therefore *structurally* escape-exposed. This is not a claim that models
choose badly. It is that the choice **has no backstop**, so it escapes when the run is loaded —
which is precisely when it matters.

Harness binding moves the same decision to the **encoded store**: resolved once, before the act,
against the task's decision set, amortising across runs.

And there is a second reason, arguably stronger:

> **A fixed toolset makes the open set computable.** Bound at assembly time, the harness can enumerate
> exactly which decisions remain unverified *before the run starts*. If the model may add tools
> mid-run, the open set is a moving target and can only be observed after the fact. **Binding is what
> makes the analysis possible at all** — not merely safer.

This also extends the frozen-bundle discipline (a WorkUnit is fully resolved with no callbacks) from
context to capability.

### 3.2 The insufficiency path — the load-bearing edge case

Fixed binding gives up genuine adaptivity: the task may turn out to need something the harness did not
anticipate. **The framework's answer is that surfacing this is correct**, but it only works if the path
exists.

> **An unanticipated tool need is an unanticipated decision.** The actor must be able to declare *"this
> task requires a capability I was not given"* and **stop** — routing the decision to a human, rather
> than improvising with what it has.

Without this path the model will improvise, and the escape you prevented at bind time reappears one
level down — now disguised as a completed run. **The refusal path is not a nicety; it is what keeps
binding honest.**

---

## 4. What is deliberately absent

- **No server, transport, or lifecycle.** Solved problems, for a problem this scope does not have.
- **No discovery or capability negotiation.** The harness knows the tools at build time; it wrote them.
- **No dynamic tool loading.** See §3.1.
- **No tool-declared class.** Tools declare facts about themselves; the harness computes class by
  composing those with the task (`tool-surfaces.md` §3).

**What is kept from the protocol lineage**, because it is demand-routing rather than distribution
machinery: an equivalent of **elicitation** (route an unresolvable decision to a human — §3.2) and an
equivalent of **sampling** (route a decision to a model actor across a seam, `core/06`). Those two are
the parts a demand-aware design would have invented independently.

---

## 5. The one line

> **Pin the ground first: a tool response declares what ground it touched, whether that ground is
> controlled, and how to tell if it still holds. Only then is it meaningful to ask what the call
> resolved, what it left open, and what it verified — and only then can a harness bind a toolset and
> state, before the run, exactly which decisions have nowhere to live.**
