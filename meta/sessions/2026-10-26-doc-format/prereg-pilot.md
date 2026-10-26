# Pre-registration — the `tool-contract` pilot

Written and committed before the reformatted `apparatus/tool-contract.md` exists. Its SHA-256 is recorded in `gate3-report.md`, and this file is never edited afterwards. Corrections go in a new file.

Old text: `apparatus/tool-contract.md` at `5e649a1` (unchanged since `baec167`).

## 1. The falsifier, as ruled at GATE 0 and GATE 2

The pilot falsifies the format if **either** limb fires.

**Limb 1, first contact.** A junior engineer cannot bind a toolset from the reformatted document faster than from the current one.

**Limb 2, lost result.** The reformat drops a load-bearing result that has no claim to point to. "Drops" means it is absent from the new document and also absent from `promotions.md` and from canon.

## 2. The load-bearing content of the old text

Enumerated now, so limb 2 is checked against a fixed list, not a list drawn up after the rewrite.

| # | Content | Section | Kind |
|---|---|---|---|
| R1 | Tool classes are meaningful only over pinned ground. Unpinned, every class collapses toward exporter. | §1 | **result** |
| R2 | Ground relation is declared per response, not per tool. | §2.1 | design rule |
| R3 | Revalidate by default. A TTL is an optimisation, justified per tool. A lapsed response is not a pin. | §2.2 | design rule, resting on P-2 |
| R4 | A response is resolved or unresolved; unresolved content should name what remains to decide. | §2.3 | design rule |
| R5 | A response declares its boundedness. | §2.4 | design rule |
| R6 | A verdict declares what it checked and what it did not. | §2.5 | design rule |
| R7 | The harness enumerates the decision set, binds the toolset, computes resolved, verified and open, and freezes the binding before the run. | §3 | design rule |
| R8 | A model that picks tools mid-run is structurally escape-exposed: the selection is open, made under load, with no verifier. | §3.1 | **result**, resting on `DDD-floor-01` |
| R9 | A fixed toolset makes the open set computable before the run. | §3.1 | **result** |
| R10 | The actor must be able to declare an unanticipated tool need and stop, routing to a human. | §3.2 | design rule |
| R11 | What is deliberately absent, and what is kept (elicitation, sampling). | §4 | design rule |

## 3. Predictions

| # | Prediction | Why |
|---|---|---|
| P1 | R1, R8 and R9 are results with no claim behind them, and are **not** in `promotions.md`. The pilot registers them as P-8, P-9 and P-10, target canon here (`tool` area), and the new document cites them as held. | GATE 1 classified `tool-contract` as "project: normative design, not result". Reading it in full says that was partly wrong. This is recorded now, before the rewrite, so the registration cannot be read as a rescue after the fact. |
| P2 | The new document fires W13 on P-3 and on each new held item. | GATE 2 ruling 5's recorded prediction, extended. |
| P3 | The new document fires W10 on `term:poisoned-ground` and `term:encode-verify-split`. Both are upstream canon, and neither is pinned in `graph/upstream.yaml`. Adding pins is out of scope, so they become a successor item, not a silent omission. | DDD-agent-01: a basis cited without a pin can move silently. |
| P4 | Limb 2 does not fire. Every R-item is either in the new document or registered. | The held-basis mechanism exists for exactly this. |
| P5 | Limb 1: the new document scores at least as well on the rubric, and the readers finish no slower. `UNVERIFIED — Emil review`: Claude's expectation, held with low confidence. | The old text front-loads theory (§1) before the reader reaches what to build (§2–§3). |

## 4. The first-contact test

**Readers.** No human junior engineer is available inside the session, so readers are proxies: fresh agents with no access to the repository, the conversation or the framework. Each is told it is a junior engineer who knows software but not this framework, and is given **one** version of the document and nothing else. Two readers per version, four in all, run independently. **The proxy is a limitation, not a substitute.** A human first-contact test is a successor item whatever the result.

**Task, identical for all four readers:**

> You are building the harness for a local agent whose task is: "bump the library `fastjson` to the latest version compatible with this project, and leave the tests passing". The harness can give the agent these tools: `read_file` (reads a file in the project workspace), `list_dir` (lists a workspace directory), `fetch_url` (fetches a URL; here, the package registry's index page for `fastjson`), `run_tests` (runs the project's test suite) and `write_file` (writes a file in the workspace).
>
> Using only the document you were given:
> 1. For each tool, say what its responses must declare for this task.
> 2. Bind a toolset for this task. Say which of the task's decisions are resolved, which are verified, and which remain open.
> 3. Say what should happen if, mid-run, the agent finds it needs a capability you did not bind.
> 4. List any point in the document where you were unsure what to do.

**Rubric, one point each, eight in all.** Scored by Claude against these criteria only, with the answers' version labels hidden until scoring is done.

| # | The answer… |
|---|---|
| K1 | declares `fetch_url`'s registry response **uncontrolled**, with when it was observed and how to revalidate it |
| K2 | declares `read_file` / `list_dir` / `write_file` workspace responses **controlled**, or notes that ground relation is per response |
| K3 | prefers a **validator** (etag, version, hash, mtime) or revalidating every call over a TTL |
| K4 | requires **boundedness** for at least one tool likely to return large output |
| K5 | treats `run_tests` as a **verdict** and says what it does **not** check |
| K6 | has the **harness bind and freeze** the toolset before the run; the model does not pick tools |
| K7 | names at least one decision that stays **open** after binding (for example, compatibility beyond what the tests cover) |
| K8 | has the agent **declare the missing capability and stop**, routing to a human, rather than improvising |

**Speed.** Each reader's wall-clock duration and total tokens, as the agent runner reports them.

**Limb 1 fires if** the new version's mean rubric score is lower than the old version's, **or** its mean duration is more than 10% longer than the old version's. The 10% band is there because two runs per version are noisy. The band is fixed now and not adjusted after.

**Also recorded, not scored:** each reader's list of unsure points (task item 4), as the qualitative read of first contact.
