# Production Is Ground

<!-- ddd:doc
reader: engineering and delivery leads deciding where their team should verify changes, and people who use the DORA metrics
act: sort a team's checks into what a validator should catch, what needs real traffic and what needs real users, and compute how many change failures were self-inflicted
pin: v5.15.2
basis: [term:floor, DDD-floor-01, DDD-measure-01]
status: current
supersedes: 84aa466:applications/sdlc/production-as-ground.md
-->

Read this if you lead a delivery team, or use the DORA metrics, and want to decide where your
team should check its changes. It argues that a test suite checks code against a copy of the
world, not the world, and uses that to sort checks into three tiers, each with its right place to
run. It ends with a number you can compute from your own incident history. It applies two ideas
from the framework's apparatus to software delivery, the
[encode/verify split](../../apparatus/encode-verify.md) and the
[closure principle](../../apparatus/closure-principle.md), and tests them against the DORA
research programme.

**How settled this is: reported, partially. The correspondence with DORA's published findings is
real and is checked below, including two places the framework fails to add anything and one place
it may be wrong.** The framework was *not* validated against DORA's underlying data — that data is
not public; only aggregate findings are. This is a retrodiction check against published results,
not a statistical test, and it is presented as such.

The ideas below that come from the principle's canon are pinned in
[`graph/upstream.yaml`](../../graph/upstream.yaml); "Where this comes from" names them.

<!-- ddd:ref id=term:floor -->
<!-- ddd:ref id=DDD-measure-01 -->
<!-- ddd:ref id=DDD-floor-01 -->

## 1. The claim, stated carefully

A tempting formulation is: *"you cannot know whether software works before it is in production."*
**That is too strong and the framework rejects it.** Compilers, type checkers, and test suites close
predicates. The framework holds that digital work with checkable predicates has zero intrinsic floor. Taken
literally, the strong claim would make nearly all software floor-exposed, which is false and would
contradict the framework's own central result.

The defensible version is about **ground**, not about knowledge:

> **Pre-production predicates close over *substitute* ground. Production predicates close over *real*
> ground. A green test suite tells you the code is correct with respect to the substitute — not with
> respect to the world.**

Which makes the gap an instance of something already named:

> **A test suite is an encoded observation of ground you do not control.** It encodes what production
> was believed to look like when the test was written. By the encode/verify split, *you cannot amortise an
> observation of something you do not control* — so that belief has an expiry date and no alarm on it.

Green tests over drifted fixtures is the **poisoned ground** signature exactly
(`apparatus/closure-principle.md`): the reasoning is sound, the premises are stale, and the result is
confident and wrong.

**So the reframed claim:**

> **The gap between pre-production and production verification is the gap between your copy and the
> source of truth — and it is unbounded until you deploy.**

---

## 2. What DORA measures, read as demand

DORA's four keys split cleanly along the encode/verify seam:

| Metric | Read in framework terms |
|---|---|
| **Deployment frequency** | how often encoded belief is checked against real ground |
| **Change lead time** | **the interval during which encoded belief goes unverified** |
| **Change failure rate** | how often the encoded belief turns out to have been wrong |
| **Failed-deployment recovery time** | the cost of being wrong, once discovered |

Two measure the **size of the unverified gap**; two measure **what it costs when the gap contained an
error.** That is the encode/verify split, instrumented.

**And DORA's own causal story matches.** Their account of the batch-size mechanism runs: manual
pipeline steps → deploy less often → larger batches → *"feedback arriving far too late."* In framework
terms, a large batch is **a large accumulation of encoded claims about production that nobody has
checked** — unverified demand in flight. Continuous delivery's core prescription (small batches,
deployed often) is, denominated in demand: **minimise the quantity of unverified encoded belief
outstanding at any moment.**

Trunk-based development fits the same shape: a long-lived branch is a set of encoded decisions
diverging from ground that keeps moving, and the merge pain is the accumulated drift being paid at
once.

---

## 3. The finding that tests the framework

Most of §2 is retrodiction — the framework explains findings that already have explanations. **One
finding is different**, because DORA reported it as counterintuitive and the framework predicts it
directly.

**DORA (2024, and the year prior): AI adoption correlates with *worsened* software delivery
performance.** DORA's stated mechanism is **not** that AI code is poor quality. It is that **batch
size increases when AI is used** — AI makes it easier to produce more code, and larger changesets
carry more risk.

The framework says the same thing without needing to observe it:

> AI raises the rate at which **encoded belief** is produced. It does not raise the rate at which that
> belief is **verified against real ground** — that rate is set by deployment frequency, which is a
> property of the delivery system, not of the code generator.
>
> **So AI increases unverified demand in flight.** Generation capacity grew; verification capacity did
> not. The gap widens, and the framework's escape term grows with it.

This is the framework's structure at the organisational scale: **production capacity outran verification
capacity, and the surplus went into the escaped store.** Not a defect in the model's output — a
mis-allocation, exactly the sort the conservation principle predicts when one store's throughput
increases and the others do not.

**The prescription follows and is non-obvious:** the fix for AI-degraded delivery performance is not
better code review or more tests against substitute ground. It is **raising the verification rate to
match the new generation rate** — deploy more often, in smaller increments, so the interval of
unverified belief does not grow. That is a claim about *where to intervene*, and it is derived rather
than observed.

---

## 4. Feedback loops as verification — and which ones are waste

DORA's prescription is *shorten the loop*. That is correct advice **given the loop is necessary**. The
framework says there is a prior move: **most loops are not necessary, and the necessary ones are a
minority.**

A feedback loop is a **verification mechanism** — an expensive one, denominated in deployment latency
and blast radius. Current practice uses it for two entirely different jobs and does not distinguish
them:

- **Discovering what the predicate *is*.** You do not yet know what "correct" means, so you ship and
  observe. Irreducible where the predicate is open.
- **Checking a predicate you already have.** You know what correct means; you simply have no cheap
  mechanical check for it, so you use the expensive one.

**The second class is waste, and it is most of them.**

> **Where the predicate closes, a feedback loop is a mechanical check you declined to build.** You are
> paying deployment latency for an answer a validator would have returned in milliseconds.

The reference case: a resource name resolved from template interpolation that exceeds a published
length limit. **The rules are published. The predicate closes. The value is computable statically.**
And yet standard practice is to discover it at deploy time — a feedback loop substituting for an
unwritten check.

### 4.1 Three tiers, not two

The tempting cut is *technical closes, user response does not*. That is nearly right, and the
exception matters:

| Class | Predicate | Where it must be verified |
|---|---|---|
| **Static technical** | **closes statically** — compiles, schema conforms, name valid, migration applies, contract holds | a **validator**. Reaching production unverified is self-inflicted. |
| **Ground-dependent technical** | **closes only over real ground** — behaviour under production load, emergent interaction across services, correctness against the actual data distribution | **progressive delivery** — real traffic, bounded blast radius |
| **User response** | **does not close** — no ground truth until observed, and the standard is non-stationary | **deploy and observe.** Irreducible. |

The middle tier is why the naive two-way cut fails. *"Does this query hold at production traffic"* is
a **technical** question whose predicate does not close statically — you can benchmark against
substitutes, but the real answer requires real load. Likewise correctness against production's actual
`P(input)`, which is the framework's deployment-distribution caveat arriving in practice: you do not have
production's input distribution in staging.

**And this is what progressive delivery is *for*.** Canaries and shadow traffic are not a
higher-fidelity staging. They are the verification mechanism for the middle tier — technical questions
whose predicate closes only over real ground. Which is precisely why §7's prediction has teeth:
fidelity practices improve the *substitute*, and the middle tier is where no substitute suffices.

### 4.2 The rule, and the diagnostic

> **Deploy to learn how users respond. Deploy to learn how the system behaves at real scale. Never
> deploy to learn whether the code is correct.**

Most teams route all three tiers through one channel and cannot tell them apart. Which yields a
diagnostic a team can compute from its own incident history:

> **What fraction of your change failures were tier one?**
>
> Every tier-one failure is **a validator you did not build.** Tier two and three failures are the cost
> of doing business; **tier-one failures are self-inflicted.**

### 4.3 What this predicts that "shorten the loop" does not

> **Two teams at identical deployment frequency should differ in performance according to how much of
> their decision set they have moved *out* of the feedback loop into static verification.**

Loop frequency is a **second-order** lever once you have stopped using the loop for closable
decisions. This explains the team that deploys constantly and still carries a high change failure
rate: **deployment is their primary verifier**, so every closable decision they have not encoded rides
to production to be checked there. Deploying faster discovers those errors sooner; it does not stop
manufacturing them.

*Caveat, and it is real: classifying a decision by predicate closure is undecidable in general, as the
framework itself states. In practice you do not need the general solution — the abundant cases (published
rules, static constraints, schema conformance) are obvious. But the framework should not claim the
decision set can be cleanly partitioned, because it cannot.*

---

## 5. Where the framework adds nothing — stated plainly

**Batch size.** The batch-size result predates DORA and the framework alike. Reinertsen's queueing
arguments, and Lean batch-size theory generally, give the same prescription from a different
mechanism, and DORA cites that lineage. **The framework offers a redescription here, not an
explanation DORA lacks.** Anyone claiming otherwise is overreaching.

**Feedback latency.** "Shorten the feedback loop" is the oldest advice in the field. Restating it as
"shorten the interval of unverified encoded belief" is more precise, but it is not new guidance.

**A caution about post-hoc fit.** DORA's findings are consistent with the framework — and also with
queueing theory, Lean, and general feedback-loop arguments. **Consistency with a mature empirical
programme is weak evidence**, because many stories fit. The honest claim is *"the framework explains
why these metrics work"*, never *"the framework predicted them."* §3 is the only place the ordering
runs the other way, and even there the framework and DORA agree on the mechanism — the framework's
contribution is deriving it rather than measuring it.

---

## 6. Where the framework might be wrong

**The 2024 cluster anomaly.** For the first time, the *medium* cluster posted a **lower** change
failure rate (~10%) than the *high* cluster (~20%), breaking the usual pattern in which all four keys
move together.

A naive reading of the framework predicts these should move together — more frequent verification
against real ground should mean *both* faster delivery *and* fewer failures, since escape falls.
**The anomaly is at least a partial counterexample**, and it should be recorded rather than explained
away.

A defence is available, and it is weak enough that it should be labelled as such: change failure rate
counts failures *per deployment*, so a team deploying far more often can carry a higher per-deployment
failure rate with a lower *absolute* volume of unverified belief in flight, and a lower cost per
failure. That may be right — but it is exactly the kind of post-hoc rescue the framework has
elsewhere refused to accept, and it should not be treated as settled. **Booked as an open
discrepancy.**

---

## 7. A prediction the framework makes that DORA has not tested

For this to be more than retrofitting, the framework must say something checkable that DORA's own
account does not already imply.

**The candidate.** DORA's capability catalogue includes *test data management*, whose guidance is
essentially: make substitute ground adequate, on-demand, and non-constraining. In framework terms that
is **improving the quality of the substitute** — which reduces, but cannot eliminate, the gap between
your copy and the source of truth.

> **Prediction: practices that convert substitute ground into *real* ground should outperform
> practices that improve the substitute — and the gap should widen as the substitute's fidelity
> requirement rises.**
>
> Concretely: **progressive delivery** against real traffic (canaries, shadow traffic, feature flags
> evaluated in production, staged rollout) should predict delivery performance **more strongly** than
> test-environment fidelity practices (better fixtures, more production-like staging, richer test data
> management) — *at matched investment.*

**Why this is not obvious.** Both families reduce failure risk, and industry advice treats them as
complementary rungs on one ladder. The framework says they are **different in kind**: one shrinks the
encode/verify gap by *verifying against the source of truth*, the other shrinks it by *improving the
copy*. By the encode/verify split, only the first can close it, because the second is still an encoded
observation of ground you do not control.

**How it could fail.** If test-environment fidelity predicts performance as strongly as progressive
delivery at matched investment, the substitute/real distinction is not doing the work the framework
claims, and this section is wrong. That is a real risk: fidelity practices might dominate simply
because they catch errors earlier and cheaply, which would be a straightforward economic effect the
framework does not need.

**Testability.** DORA's capability catalogue and survey instrument already cover both families. The
comparison would require access to response-level data, which is not public — so this is a prediction
offered *to* the research programme, not one this framework can settle.

---

## 8. What survives

- **Production is where the ground is real.** Everything earlier verifies against a copy.
- **A test suite is an encoded observation of uncontrolled ground** — with an expiry and no alarm.
- **DORA's four keys instrument the encode/verify gap**: two measure its size, two measure the cost of
  being wrong inside it.
- **Feedback loops are verification, and most are waste** (§4). Three tiers — static technical
  (should be a validator), ground-dependent technical (progressive delivery), user response
  (irreducible). *Deploy to learn how users respond; never deploy to learn whether the code is
  correct.* The diagnostic: **what fraction of your change failures were tier one?** Those are
  self-inflicted — a validator you did not build.
- **The AI finding is the framework's best case** (§3): generation capacity outran verification
  capacity, and the surplus went to escape. Derived, not observed — and it yields a specific
  intervention.
- **Batch size and feedback latency are not the framework's contributions** (§5). Cite Reinertsen and
  Lean.
- **The 2024 cluster anomaly is an open discrepancy** (§6), not a resolved one.
- **The progressive-delivery-over-fidelity prediction** (§7) is the only genuinely novel, falsifiable
  claim here — and it is offered to DORA, not settled by this document.

---

## 9. The one line

> **Production is the only ground that is not a copy. Everything shipped before it was verified against
> an encoded belief about the world, and the whole apparatus of continuous delivery is an empirical
> programme for shrinking the interval during which that belief goes unchecked.**

---

## Not settled yet

- **The 2024 cluster anomaly** (§6). DORA's medium cluster posted a lower change failure rate
  than its high cluster, which a naive reading of the framework says should not happen. The
  defence in §6 is weak, and it should not be treated as settled. It is booked as an open
  discrepancy.
- **Progressive delivery over environment fidelity** (§7). The prediction has not been tested.
  Testing it needs DORA's response-level data, which is not public, so it is offered to the
  research programme, not settled here.
- **The partition is not clean** (§4.3). Classifying a decision by predicate closure is
  undecidable in general. The abundant cases are obvious enough to act on, but the decision set
  cannot be cleanly partitioned.

## Where this comes from

| Section | Rests on |
|---|---|
| Opening | `apparatus/encode-verify.md`; `apparatus/closure-principle.md`; the principle repository `actor-indexed-determination`, pinned in `graph/upstream.yaml` at `v5.15.2` |
| 1. The claim, stated carefully | Zero intrinsic floor for digital work with checkable predicates: upstream `core/03`, `DDD-floor-01` (reported) and `term:floor` (settled); the amortisation limit, `apparatus/encode-verify.md`; the poisoned-ground signature, `apparatus/closure-principle.md` |
| 2. What DORA measures | DORA's published four keys and batch-size account |
| 3. The finding that tests the framework | DORA 2024 and 2023 reports (AI adoption and batch size); the cost structure of upstream `core/10` |
| 4.1 Three tiers | The deployment-distribution caveat of upstream `core/09`, `DDD-measure-01` (projected) |
| 4.3 What this predicts | Undecidability of closure in general, upstream `core/03` |
| 5. Where the framework adds nothing | Reinertsen's queueing arguments; Lean batch-size theory |
| 6. Where the framework might be wrong | DORA 2024 cluster results |
| 7. A prediction | DORA's capability catalogue (test data management; progressive delivery); `apparatus/encode-verify.md` |

The text this replaces is `84aa466:applications/sdlc/production-as-ground.md`. That text opened
with "Location: proposed `applications/sdlc/production-as-ground.md`", which was stale: the
document is at that path. Its §8 cited §4, §5 and §6 for points made in §5, §6 and §7; the
citations are corrected here, and no rule changed.
