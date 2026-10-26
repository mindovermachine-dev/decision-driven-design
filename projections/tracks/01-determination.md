# Track 1 — Determination

**A single ordered path through the determination vocabulary, taught against one decision held
constant while the words change.** Ten rungs. For software engineers; C#/.NET fluency assumed,
framework vocabulary assumed absent.

> **Ratified.** All ten rungs were drafted at Gate 3, 2026-08-18, and accepted by Emil's merge of
> pull request #24 (e96aa89).
> The `[PROPOSED]` banner that stood here was struck 2026-10-26 (`DDD-dec-40`). Ratified means
> filed, not tested: the track's claim, `DDD-track-01`, is projected.

---

## Manifest

| Field | Value |
|---|---|
| **Source canon** | `actor-indexed-determination` at **`v5.8.0`**, pinned in `graph/upstream.yaml` |
| **Audience** | software engineers — C#/.NET fluency assumed, no framework vocabulary assumed |
| **Register** | engineering |
| **Rendered** | 2026-08-18 |
| **Filter** | the determination vocabulary: what a decision is, what resolves it, what it is resolved against, and how an arrangement commits in advance |
| **Worked decisions** | retry-count, rungs 1–9 (uncontested by design); retention-period, rung 10 (contested by design — `DDD-dec-27` §9) |
| **Status floor** | none — every projected or draft node is flagged **at the point of use**, not only here |
| **Governing decision** | `DDD-dec-27` (rung order, filing, and the ground-provenance ruling) |
| **Track claim** | `DDD-track-01` — carries the track's pre-registered falsifier and its `Q27` revision obligation |

**Nodes cited, and their status at the pinned version.** A `ddd:ref` marker appears at each
node's first substantive use; the marker is what makes a stale citation mechanically detectable
rather than a matter of someone remembering.

| Node | Status at `v5.8.0` | First cited |
|---|---|---|
| `term:determinable` | settled | rung 1 |
| `term:determinate` | settled | rung 1 |
| `term:tolerance` | settled | rung 1 |
| `DDD-frame-13` | **projected** | rung 1 |
| `DDD-ground-05` | **projected** | rung 1 |
| `term:decision` | settled | rung 2 |
| `term:admission-test` | settled | rung 2 |
| `term:governing-decision` | settled | rung 2 |
| `term:ground` | settled | rung 3 |
| `DDD-ground-02` | **projected** | rung 3 |
| `term:actor` | settled | rung 4 |
| `term:arrangement` | settled | rung 4 |
| `term:judgment` | settled | rung 4 |
| `term:act` | settled | rung 4 |
| `DDD-frame-01` | **projected** | rung 5 |
| `DDD-frame-02` | **projected** | rung 5 |
| `term:commitment-level` | draft | rung 5 |
| `term:capability` | settled | rung 5 |
| `DDD-frame-08` | **projected** | rung 4 |
| `term:residual-discretion` | draft | rung 6 |
| `term:acceptance-predicate` | settled | rung 7 |
| `term:closure` | settled | rung 7 |
| `DDD-floor-02` | **projected** | rung 7 |
| `DDD-frame-06` | **established** | rung 7 |
| `DDD-frame-03` | **projected** | rung 8 |
| `term:assurance` | settled | rung 8 |
| `term:encoded` | settled | rung 8 |
| `term:mechanical` | settled | rung 8 |
| `term:escape` | settled | rung 9 |
| `DDD-frame-15` | **projected** | rung 9 |
| `DDD-frame-04` | **projected** | rung 9 |
| `DDD-frame-16` | **projected** | rung 10 |
| `term:accountability` | settled | rung 10 |
| `term:attribution` | settled | rung 10 |
| `term:answerability` | settled | rung 10 |
| `term:liability` | settled | rung 10 |
| `DDD-ground-04` | **projected** | rung 10 |
| `term:governing-decision` | settled | rung 2 |

### Declared forward pointers

The rung order must not require a reader to know a word a later rung introduces. Four uses
survive that rule as **declared forward pointers**, listed here rather than left to be noticed —
canon carries fifty-nine of its own under the same discipline (`W1`), and the test is the same
one: does deleting the word leave the passage intact?

| Rung | Word | Introduced | Why it stays |
|---|---|---|---|
| 3 | *assurance* | 8 | inside `DDD-ground-02`'s statement, quoted verbatim; deleting it misquotes canon |
| 5 | *assurance* | 8 | inside `DDD-frame-01`'s tuple, quoted verbatim; the tuple has six coordinates or it is not the tuple |
| 8 | *escape risk* (×2) | 9 | rung 8's whole point is that the risk is identical across sources; naming it later would blunt the rung that sets rung 9 up |

Each is legible from context at the point of use and is defined properly at its own rung. **A
fifth reading of the constraint fails, and is reported at Gate 3 rather than hidden here** — see
`DDD-dec-27` §7 on the document-granularity check.


---

## Before you start

**What this track gives you is capability, not competence.**

Rungs 1 through 9 teach you to see things you cannot currently see, and to say things you cannot
currently say. In the framework's own vocabulary that is **capability** — a typing over what
ground you can read and what distinctions you can resolve against it
<!-- ddd:ref id=term:capability --> — and capability is the entry fee. It is what lets you
attempt the work. It is not evidence that you did it, and it is not a qualification.

Nothing you own changes until rung 10, where you record one real decision from your own system
and put your name on it. Nine rungs of vocabulary with no rung 10 is a glossary you have read.

Read the rungs in order. Each one moves the same decision one step, and no rung needs a word a
later rung introduces.

## The decision

One decision, unchanged across rungs 1 to 9. It is deliberately unglamorous, and deliberately
uncontested — rung 10 says why, and changes it.

```csharp
services.AddHttpClient<PaymentGatewayClient>()
    .AddPolicyHandler(HttpPolicyExtensions
        .HandleTransientHttpError()
        .WaitAndRetryAsync(3, attempt =>
            TimeSpan.FromSeconds(Math.Pow(2, attempt))));
```

**How many times do we retry a failed outbound call?** Here: three.

Three actors will appear at every rung, and they never merge:

| Actor | In this system |
|---|---|
| **the program** | the retry policy above — a `WaitAndRetryAsync` that runs the same way every time |
| **the LLM** | a model in the delivery pipeline that proposes the retry count when scaffolding a new client |
| **the on-call engineer** | the person who, at 03:00 with the gateway degraded, changes it |

Keep all three in view. Most of what the vocabulary buys you is the ability to say something
precise about *how they differ*, and the usual words — "automated", "manual", "human in the
loop" — cannot say it.

---

## Rung 1 — `3` is not a decision

**What you cannot do yet.** You can read that code and say "the retry count is three". You cannot
yet say what kind of thing "three" is, so you cannot say what would have to be true for a
different number to be *wrong* rather than merely different.

### The move

Two things are in that line and they are not the same thing.

<!-- ddd:ref id=term:determinable -->
The first is **retry-count**: a dimension along which the system could vary, where the variation
matters. That is a **determinable** — an outcome-relevant dimension of variation at the declared
tolerance. It is the axis. *(Canon uses the word "determinable"; engineers say "axis". They name
the same node — `term:determinable` reads, in canon, "the dimension of comparability an axis
names". This track uses "axis" in running prose and "determinable" where precision is needed.)*

<!-- ddd:ref id=term:determinate -->
The second is **3**: one specific way of occupying that axis. That is a **determinate** — what
resolving the decision produces. Not the axis plus a modifier; a way of being at the axis.

The asymmetry that makes this worth a rung:

| | Axis (determinable) | Value (determinate) |
|---|---|---|
| retry-count | the thing that can be governed | `3` |
| exists | before anyone chooses | only as an occupation of the axis |
| can be | declared, argued, owned, revisited | right or wrong, at a stated tolerance |
| answer to | "what varies here that matters?" | "and how did it land?" |

<!-- ddd:ref id=DDD-ground-05 -->
The order matters and is not stylistic. Declaring the axis is **constitutively prior** to
choosing a value on it: a value is only ever *a way of occupying* a declared axis, so a value
with no axis behind it is not a resolution of anything. *(`DDD-ground-05`, **projected** — a
clean derivation, unexercised. Flagged because you are reading a practice document: this is
canon's position, not a measured finding.)*

<!-- ddd:ref id=DDD-frame-13 -->
And "how fine-grained" is itself declared, not discovered. Determinateness comes in orders — red,
then scarlet, then this exact shade — and the **declared tolerance** names the order at which you
stop distinguishing <!-- ddd:ref id=term:tolerance -->. Whether `3` and `4` are different values
on your axis, or the same value at your grain, is something you say, not something the world
says. *(`DDD-frame-13`, **projected**.)*

### On the decision

`3` is not a decision. `3` is what a decision produced, or what happened where a decision was not
made — rung 9 is entirely about telling those two apart, and you cannot yet.

`retry-count` is the axis. Write it down as a name. The moment it has a name, three questions
become askable that were not askable before: *what values are permitted on it, who says, and
against what.*

Notice what the three actors share. The program, the LLM, and the on-call engineer all resolve
**the same axis**. They are not doing different jobs. This is the observation rung 4 is built on,
and it is invisible until the axis has a name.

### What you can now do

Name the axis under a literal. Not "why is it 3?" — **"what is the 3 a value of?"** Try it on the
last four constants you merged.

---

## Rung 2 — what makes it a decision

**What you cannot do yet.** You can name axes. You cannot yet tell which ones are worth
governing, so you will either govern everything and drown, or govern what is salient and miss
what matters.

### The move

Not every axis is a decision. There is a test, and it is a counterfactual, not a feeling.

<!-- ddd:ref id=term:admission-test -->
> **A choice is a decision iff varying *the choice* moves the outcome past tolerance.**
>
> **A fact is ground iff varying *the world* moves the outcome past tolerance.**

Read the first half now; the second is rung 3, and the fact that they are one test with two
directions is the point.

Three conditions have to hold together, and each one does real work:

| Condition | What it rules out | On retry-count |
|---|---|---|
| **declared** | an axis nobody has named — you cannot govern what has no name (rung 1) | somebody wrote `retry-count` down |
| **outcome-relevant** | axes whose variation stays inside tolerance | 3 vs 30 changes gateway load and customer-visible latency; 3 vs 4, at some tolerances, does not |
| **governed at a chosen abstraction and tolerance** | the pretence that "correct" is absolute | "the retry policy", not "this `Math.Pow` call"; and "p99 checkout latency under 800 ms", not "fast" |

<!-- ddd:ref id=term:tolerance -->
**Tolerance indexes everything.** It is the declared boundary of acceptable outcome deviation,
and without one the decision set is not well-formed — not "hard to evaluate", *not well-formed*.
Whether retry-count is a decision at all depends on a number you have to declare before the
question means anything.

This is the sentence engineers resist, so here it is concretely. At tolerance "the call
eventually succeeds", retry-count is barely a decision — 3, 5, 10, all fine. At tolerance "p99
checkout latency under 800 ms with the gateway degraded", retry-count is one of the two or three
things that decide whether you meet it. **Same axis, same code, same system.** The axis became a
decision when somebody declared a tolerance, and if nobody has declared one, the honest statement
is not "it's fine" — it is "we cannot say".

<!-- ddd:ref id=term:governing-decision -->
An axis that passes the test and has been resolved by something you can point at is a **governing
decision**. Rungs 4 and 5 are about what that something can be.

### On the decision

Run the test properly.

1. **Declared?** Yes, as of rung 1.
2. **Outcome-relevant?** Pick the tolerance first. Under "p99 checkout latency under 800 ms while
   the gateway is degraded": a failing call with three retries at exponential backoff holds a
   request open for roughly fourteen seconds before it gives up. That is not near the boundary.
   That is seventeen times past it. **Yes.**
3. **At what abstraction?** "The outbound retry policy for the payment gateway." Not the
   `Math.Pow` expression, which is an implementation of it. Not "resilience", which is a mood.

Retry-count is a decision. It was a decision before anyone decided it, which is exactly why rung
9 is possible.

### What you can now do

State the tolerance before arguing about the value. When the tolerance turns out not to exist,
you have found something more useful than the answer you were looking for.

---

## Rung 3 — ground, and where it comes from

**What you cannot do yet.** You can say retry-count is a decision. You cannot yet say what it
should be *resolved against*, so every discussion about the value collapses into whoever is most
confident.

### The move

<!-- ddd:ref id=term:ground -->
**Ground** is what a decision is determined against. It is the other half of rung 2's test, run
in the other direction: a fact is ground iff varying *the world* moves the outcome past tolerance.

**That definition is the whole of this rung's canon.** Note what it does not say. It does not say
ground is data, or telemetry, or documentation. Ground is defined by a counterfactual on the
world, so whether a fact is ground is a property of the decision and the tolerance — never of the
fact's format or where it is stored.

For retry-count, ground includes: the gateway's published rate limits, its actual behaviour under
load, whether its endpoints are idempotent, the checkout latency budget, and what the contract
with the payment provider obliges. Vary any of those and the right retry count moves.

#### Five kinds, and what they cost you — track-native, **not canon**

> ⚠️ **The five-way split below is expository scaffolding invented for teaching. It is not
> canon.** It is not a claim, and it is not a partition — the categories are not proven exclusive
> or exhaustive, and nothing in the framework rests on them. It appears here because engineers
> reliably conflate "we have a number for it" with "we know it", and naming the kinds breaks that
> conflation fast. The canon content of this rung is the definition above; if the scaffolding and
> the definition ever disagree, the definition wins.
>
> ⚠️ **`institutional` is additionally gated.** The mechanism by which authority, convention, and
> social practice supply ground is an open upstream question (`Q27`, trusted sources). Treat that
> row as the least settled of the five. `DDD-track-01` records this dependency: **if `Q27` lands,
> this section must be revised**, because a resolved `Q27` may restructure the split rather than
> confirm it.

| Kind | Where it comes from | On retry-count | What it costs you |
|---|---|---|---|
| **controlled** | maintained by your own system, enforceable through commitments you control | your latency budget; your circuit-breaker settings | cheap to read, and you can change it — but you can also change it *by accident* |
| **observed** | read from an external or independently changing system | the gateway's measured p99 and error rate last Tuesday | true when read, decaying afterwards at a rate nobody has stated |
| **inferred** | estimated from data or a model | "transient failures usually clear within two seconds" | carries the estimator's error, which does not appear in the number |
| **institutional** ⚠️ | rules, conventions, authority, social practice | "three is what our services do"; the provider's fair-use clause | often the real reason, almost never written down |
| **missing** | relevant, and unavailable to whatever is doing the resolving | whether *this* failure is a blip or an outage starting | the dangerous one — see below |

**A stored statement about uncontrolled ground is not a current observation of it.** This is the
sentence to carry out of the rung. The gateway's p99 in your runbook is not the gateway's p99. It
is a claim about the gateway's p99, made on a date, by someone, and decaying since. How fast it
decays depends on drift rate, consequence, and how strong your evidence has to be — rung 8 gives
that last one a name — not on a universal "read it every time" rule, which is unaffordable, and not on "read it once", which is how
runbooks become fiction.

**Missing ground is the one to sit with.** It is not the absence of a fact. It is a fact that is
relevant — it passes the ground test — and unavailable to the actor doing the resolving. It will
matter twice: at rung 4, because the three actors have *different* ground missing, and at rung 9,
where a decision made against no ground at all still governs production.

<!-- ddd:ref id=DDD-ground-02 -->
Canon does carry an instrument here, and it is worth having early. Source coverage
(covered · declared-empty · undeclared · unknown), resolution (resolved · deliberately-open ·
unknown), and assurance (adequate · inadequate · unknown) are **orthogonal** — and the rule that
bites is that **Unknown is never a pass**. "We didn't check" and "we checked and there's nothing"
are different states, and only one of them is safe. *(`DDD-ground-02`, **projected**.)*

### On the decision

What is retry-count = 3 resolved against?

Ask the question out loud in your own system and observe how quickly the answer becomes "we'd
have to go and look". That reaction is the finding. The value has been in production for months;
the ground it is answerable to has never been assembled.

Now split it by actor, because they do not have the same ground available:

| Actor | Ground it can actually read |
|---|---|
| **the program** | its own configuration, the response status, elapsed time. Not the gateway's rate limits. Not the latency budget. |
| **the LLM** | the repository, the prompt, whatever was retrieved for it. Not last Tuesday's p99 unless something put it there. |
| **the on-call engineer** | the dashboard, the incident channel, the fact the gateway sounded odd yesterday — and eight years of pattern-matching that nobody has written down |

Same axis. Same tolerance. **Three different sets of missing ground.** This is the observation the
next rung is built on.

### What you can now do

Ask "against what?" and refuse the answer "against experience" without asking whose, and whether
anything the executing system can read carries it.

---

## Rung 4 — actor and arrangement

**What you cannot do yet.** You can see that the three actors read different ground. You will
still, by reflex, compare them as *things* — "is the model as good as the engineer?" — and that
question has no answer, because it is not well-formed.

### The move

<!-- ddd:ref id=term:actor -->
An **actor** is a system that resolves decisions by reading ground: variation in declared ground
can alter the resolution through an internal pathway that selects among alternatives. A
thermostat qualifies. A falling rock does not. **Actorhood does not require intelligence**, and
the framework's use of "actor" is not a compliment.

<!-- ddd:ref id=term:act -->
All three of ours qualify, and they resolve the same axis at an **act** — the occasion on which a
determination is actually made.

Which raises the question you were reaching for at rung 3, and which the framework refuses in the
form you want to ask it.

<!-- ddd:ref id=term:arrangement -->
> The **arrangement** is the composition through which a resolution is produced and governed:
> executor, prior commitments, ground channels, checks, reviewers, record, and accountable
> principal. The unit of comparison is the arrangement, not the isolated actor.

Read the list. The executor is **one of eight items**. "Is the model as good as the engineer?"
varies one item and holds the other seven fixed by accident, then attributes the whole result to
the item that varied. It is the wrong unit, in the way that comparing two engines by their
pistons is the wrong unit.

Here are the three, written as arrangements:

| | **the program** | **the LLM** | **the on-call engineer** |
|---|---|---|---|
| executor | `WaitAndRetryAsync` | the model | the person |
| prior commitments | the compiled policy | the prompt, the house style, the scaffold | the runbook, the incident process |
| ground channels | response status, elapsed time | repository, retrieval, prompt | dashboards, the incident channel, colleagues, memory |
| checks | the integration suite | code review, the same suite | the deploy pipeline, or nothing at 03:00 |
| reviewers | whoever approved the PR | whoever approved the PR | possibly nobody until morning |
| record | git history | git history, if the tool is logged | a chat message, if they remember |
| accountable principal | the service owner | **the service owner — never the model** | the engineer, or the service owner, and this is usually unstated |

<!-- ddd:ref id=DDD-frame-08 -->
The last row is canon, not a house rule. Answering for an outcome is a **relation** — a record
tying the determination to what produced it, a persistent principal, authority linkage, stake, a
sanction path — and **an arrangement naming an executor but no principal is incomplete**
*(`DDD-frame-08`, **projected**)*. Rung 10 names the parts. A model can be an
executor. It cannot be a principal, because it cannot bear a consequence. Rung 10 is where that
stops being an abstraction.

Now the differences are legible, and almost none of them are about the executor. The engineer's
arrangement has the richest ground channels and the weakest record. The program's has the
narrowest ground available to it and a perfect record. The LLM's inherits its ground from whatever the pipeline
retrieved, which is a design choice somebody made and probably did not write down.

<!-- ddd:ref id=term:judgment -->
One line in that table needs its own definition, because it is where the framework is strictest.
**Judgment** is determination *during* the act, by an actor reading ground, **with an accountable
party named**. The last clause is not decoration:

> **A judgment allocation naming no accountable party is not an allocation. It is Escaped with an
> executor attached.**

"The on-call engineer will handle it" is not an allocation of the decision to judgment. It names
an executor. If no principal is named — if nobody's answer is required when it goes wrong — then
what you have is the forbidden state with somebody's name on the pager, which is worse than an
obvious gap because it looks handled.

### On the decision

Compare arrangements, not components.

The interesting result is that **the program's arrangement is the most tightly bounded and has
the least ground available to it**, while **the engineer's has the most ground available and the least record**. Neither is
better. They fail differently, and they fail differently *because of the seven items that are not
the executor*.

And most of those seven are changeable. You can give the program more ground — feed it the
gateway's published rate limits at startup instead of hard-coding around them. You can give the
engineer a record — a two-line entry that survives the incident. Neither change touches the
executor. Both change the arrangement, which is the unit that was under comparison all along.

### What you can now do

Fill in the seven non-executor rows before comparing two ways of resolving anything. When a row
is blank, that is the finding — most usefully the last row.

---

## Rung 5 — commitment level

**What you cannot do yet.** You can describe an arrangement. You cannot yet say *what it has
already settled* versus *what it leaves to the moment*, so you cannot say what changes when you
swap one actor for another.

### The move

The three actors are not three kinds of thing. They are three **levels at which an arrangement
commits behaviour in advance**.

<!-- ddd:ref id=term:commitment-level -->
> A **commitment level** is a level at which an arrangement fixes behaviour in advance:
> **outcome-level** — permitted resolutions fixed directly; **policy-level** — the
> generating procedure fixed; **principal-level** — a determiner selected by qualification
> and case-level resolution delegated. The three compose, and they are levels of
> commitment, not species of actor: the question is never which of three kinds an actor
> is, but at which levels the arrangement has committed.

<!-- ddd:ref id=DDD-frame-02 -->
*(`DDD-frame-02`, **projected** — behavioural commitments attach at three levels which compose
and are not actor species.)*

Mapped onto the decision:

| Level | What is fixed in advance | Our instance | What is left at the act |
|---|---|---|---|
| **outcome** | the permitted resolutions themselves | `WaitAndRetryAsync(3, ...)` — the value is *in* the artefact | nothing about the count |
| **policy** | the procedure that generates a resolution | the LLM's scaffolding step: given a client of this shape, propose a retry count | which count, this time |
| **principal** | who resolves, chosen by qualification, the case delegated | the on-call engineer, trusted because of who they are and what they know | essentially all of it |

**"Not actor species" is the load-bearing phrase.** The program is not *inherently* outcome-level.
It is outcome-level **in this arrangement**, because somebody hard-coded a literal. Write the
count into configuration read at startup and the same executor becomes policy-level on that axis.
Have the model select from an enumerated set of three approved counts and it becomes
outcome-level. **The level is a property of the arrangement, not of the thing executing.** This
is why the vocabulary is worth learning: it moves the question from "what is it?" — unanswerable
— to "what has been committed?" — checkable.

**And they compose.** Your real system is likely all three at once: a principal is selected (the
service owner, who owns the payment integration), bound to a policy (the house resilience
standard), enforced by outcome constraints (a lint rule capping retries at five). That is one
axis governed at three levels simultaneously, which the "human vs. automated" framing cannot
represent at all.

<!-- ddd:ref id=DDD-frame-01 -->
Sitting under this is the reason the framework exists. Unresolved determination is indexed by
⟨task, ground, acceptance relation, tolerance, arrangement, assurance⟩ — **not by the task
alone** *(`DDD-frame-01`, **projected**)*. Change the arrangement and the determination problem
changes, even though the task — "pick a retry count" — is written the same way. A parameter that
never varies is indistinguishable from a constant, which is why holding the arrangement fixed
made the determiner look like one.

### On the decision

Ask, of the retry count in your own system: **at which levels has anything been committed?**

The usual answer is one level, by accident. A literal in a source file is an outcome-level
commitment made without anyone deciding to make one — nobody chose to fix the permitted
resolutions; somebody typed a number. That is a real commitment with no decision behind it, which
is rung 9's subject, and you now have three of the four words needed to say what is wrong with it.

### What you can now do

State an arrangement's commitment level per axis, and notice that changing the level is usually
cheaper than changing the executor. That is a design move you did not have before.

**What you still cannot do.** You cannot yet say what is left *unfixed* after the commitments are
applied, or why an arrangement that always produces the same answer is not thereby a correct one.
That is rung 6.

---

---

## Rung 6 — residual discretion, and why zero variance is not correctness

**What you cannot do yet.** You can say what an arrangement has committed. You cannot yet say
what is left over — and "left over" is where your incidents come from.

### The move

Commitments do not reach everything. What they do not reach is **residual discretion**.

<!-- ddd:ref id=term:residual-discretion -->
> **Residual discretion** is the outcome-relevant variation remaining at the act after the
> arrangement's declared commitments are applied. It is not randomness: a deterministic
> arrangement can carry substantial discretion across unfamiliar cases, a randomised one
> can be tightly committed, and a zero-variance arrangement can be consistently wrong.

<!-- ddd:ref id=DDD-frame-02 -->
*(`DDD-frame-02`, **projected**.)*

Read the second sentence again, because it contradicts an intuition most engineers hold without
examining it: **that a system which always does the same thing has thereby been decided.**

| | Variance | Residual discretion | Correct? |
|---|---|---|---|
| `WaitAndRetryAsync(3, …)` | zero — always three | **zero, on this axis, at this abstraction** | unrelated question |
| the model, given the same prompt twice | low | **substantial** — its commitment is policy-level, and the policy was never exercised against a degraded gateway | unrelated question |
| the engineer at 03:00 | high | **nearly total** | unrelated question |

The third column and the fourth are independent, and the whole rung is that independence.
`WaitAndRetryAsync(3, …)` has zero residual discretion on retry-count and **is wrong under load**
— that is not a contradiction, it is the ordinary case. A committed arrangement is one whose
answer you can predict. Predicting an answer is not the same as it being right.

**"Not randomness" cuts the other way too.** The model's determinism is not a commitment. Fixing
the seed, or getting the same output twice, commits nothing — the arrangement has not fixed
anything about retry-count in advance, so the discretion is still there, waiting for a case
outside what the policy has seen. Reproducibility is a property of the executor. Commitment is a
property of the arrangement.

### What is actually happening across rungs 5 and 6

Something you can now watch, and which the rest of the track will keep showing you.

The commitments an arrangement declares **do not reduce the work; they relocate it**. Move
retry-count from a literal to configuration and you have not removed the decision — you have
moved it from the developer who typed the literal to whoever edits the configuration, and added a
new decision about who may edit it. Bind the model to an enumerated set of approved counts and
the work moves into whoever enumerates the set. Every one of those moves is defensible. None of
them makes the determination go away.

That is worth feeling before it is worth naming. Watch it at rungs 7, 8, and 9 — each is another
place the work turns up after you thought you had disposed of it.

### On the decision

Your retry policy's residual discretion on retry-count is zero. Nobody at the act can vary it;
it is compiled in.

Now ask the question that matters: **is zero the right amount?**

At 03:00 with the gateway returning 503 for everything, an arrangement with zero residual
discretion on retry-count retries three times, per request, for every request, and adds load to a
system that is failing because of load. The engineer who can override it has residual discretion
and can stop the bleeding. The engineer who cannot has an arrangement that was committed by
somebody who never imagined this Tuesday.

Zero residual discretion is a design choice with a cost, not a safety property.

### What you can now do

Separate "will it do the same thing every time?" from "is the thing it does right?" — and notice
that most arguments about determinism in your team are the first question wearing the second's
clothes.

---

## Rung 7 — acceptance, and where it closes

**What you cannot do yet.** You can say what is committed and what is left over. You cannot yet
say *which parts of this decision can be settled by a machine at all* — so you cannot say which
parts need a person, except by feel.

### The move

<!-- ddd:ref id=term:acceptance-predicate -->
> The **acceptance predicate** is the criterion that settles whether an outcome is acceptable at
> the declared tolerance. Everything about a task's checkability — and therefore its floor —
> lives here.

Not in the task. Not in the actor. **In the predicate.** This is the framework's sharpest
relocation and it takes a moment to accept: whether a decision needs judgement is not a fact
about how hard the decision feels, it is a fact about whether its acceptance criterion can be
evaluated.

<!-- ddd:ref id=term:closure -->
> **Effective closure, defined.** A predicate is **closed for an arrangement** when the relevant
> ground is observable and adequacy can be evaluated within declared resource, latency, and
> confidence bounds. **Decidable** is reserved for the formal special case.

Three things in that definition do work, and engineers routinely drop the third. Ground
observable — you can see what you need to see. Adequacy evaluable — you can tell pass from fail.
**Within declared bounds** — and if the evaluation takes six weeks, the predicate does not close
for an arrangement that has to answer today. Closure is not "is it possible in principle". It is
"can *this* arrangement settle it, in time, at the confidence required".

**And closure is per arrangement, not per task.** <!-- ddd:ref id=DDD-floor-02 --> The same
nominal task is routine for one arrangement and judgement-heavy for another; better ground,
contracts, checks, and institutions move the boundary without making the task intrinsically
simpler *(`DDD-floor-02`, **projected**)*. Which means the boundary is something you can move on
purpose — the single most useful consequence in this rung.

### On the decision

Split the retry decision by predicate, and it comes apart cleanly into two halves that need
completely different treatment.

| | **Closed** | **Open** |
|---|---|---|
| The question | does the handler retry exactly three times, with exponential backoff, on a transient failure, and give up cleanly after? | is three the right number when the gateway is degraded, the queue is deep, and every retry is load the gateway cannot absorb? |
| Ground | observable — a stubbed handler, a fake clock | requires the gateway's behaviour under a load you have not generated, and next quarter's traffic |
| Evaluated | in milliseconds, in CI, every commit | not within any bound you can declare |
| Confidence | total | contested among competent people |
| Verdict | **operationally closed** | **open** |

```csharp
[Fact]
public async Task RetriesThreeTimesOnTransientFailure()
{
    var handler = new CountingHandler(HttpStatusCode.ServiceUnavailable);
    await Assert.ThrowsAsync<HttpRequestException>(() => Client(handler).PayAsync(Order));
    Assert.Equal(4, handler.Calls);   // the original, then three retries
}
```

That test is green. It closes its predicate completely. **And it tells you nothing about whether
three is right**, because it was never the predicate that mattered.

<!-- ddd:ref id=DDD-frame-06 -->
Here is the sentence to take away, and it is the one node on this track that is
**established** rather than projected — a theorem, not a position. **Closure is distinct from
generation cost: verification being cheap implies nothing about the density or accessibility of
the acceptance region** *(`DDD-frame-06`, **established**; the theorem is Cook and Levin's, the
identification is the framework's)*. Checking that a retry count behaves as written is trivial.
Finding the retry count that survives peak load is not, and the ease of the first is not evidence
about the second. A green suite means the closed half is closed. It is silent on the other half,
and reading its silence as approval is how the open half stays ungoverned.

Notice, too, what happened to the work: it did not disappear into the test suite. The suite
absorbed the closed half exactly, and left the open half sitting where it was — the relocation
you were told to watch for at rung 6.

### What you can now do

Split any decision into its closed and open halves before arguing about who should own it. The
argument is usually two people each holding a different half.

---

## Rung 8 — assurance is not source

**What you cannot do yet.** You can say who resolved something, and you can say what closes. You
still, by habit, treat "a person decided it" and "it was checked" as one fact — so you cannot see
the risk that lives between them.

### The move

Two questions. They feel like one. They are not.

<!-- ddd:ref id=DDD-frame-03 -->
> The source of a resolution and the mechanism assuring it are separate dimensions.
> *(`DDD-frame-03`, **projected**.)*

| | Question | Values, for retry-count |
|---|---|---|
| **Source** | what supplied the resolution? | the compiled policy · the model's proposal · the engineer's call · nothing |
| **Assurance** | what evidence is there that tolerance is met? | the test suite · code review · a load test · **nothing** |

<!-- ddd:ref id=term:assurance -->
> **Tolerance** — which outcome deviations are acceptable — and **assurance** — the strength of
> evidence that tolerance is met. Two systems can share a tolerance and differ in required
> assurance.

They are independent, and the grid is the rung:

| | **assured** | **unassured** |
|---|---|---|
| **program** | the compiled count, with a load test that exercises the degraded path | the compiled count, and the only test is the one at rung 7 |
| **LLM** | the proposal, reviewed by someone who read the gateway's rate limits | the proposal, approved because the diff looked clean |
| **engineer** | the 03:00 change, with a follow-up validating it against the incident | the 03:00 change, and everyone went back to bed |

**Read the right-hand column.** Three different sources. Same escape risk. The value governing
production is not backed by evidence that it meets tolerance, and *which* of the three put it
there changes nothing about that. The intuition that the engineer's unassured call is safer than
the model's unassured call is doing no work — it is the executor asserting itself over the
arrangement again, which rung 4 already refused.

<!-- ddd:ref id=term:encoded -->
<!-- ddd:ref id=term:mechanical -->
Canon carries these as separate positions in time, which makes the independence concrete.
**Encoded** — a constraint fixed *before* the act, by a rule; it amortises, cheap to state and
expensive to find. **Mechanical** — a criterion applied *after* the act, by a check; it pays the
executability tax and is cheap to trust. Encoding is source. Checking is assurance. A system can
have either without the other, and "we have a standard for this" answers the first question while
people hear it as an answer to the second.

**The move that is available once you can see the two axes.** You do not have to change the
source to reduce the risk. Leave the compiled count exactly as it is, and add a load test that
exercises the degraded path — the source is untouched, and the escape risk drops. The reverse
also holds: promote the decision to a senior engineer, change nothing about assurance, and you
have moved a name without moving the risk. Most "who should own this?" arguments are assurance
problems being solved on the source axis, where they do not yield.

### On the decision

For your own retry count, fill in both cells honestly.

The common answer is **source: a literal somebody typed** and **assurance: the suite from rung
7** — which closes a predicate that was never the one at issue. That is the unassured column with
a green tick on it, and it is one step from the next rung.

### What you can now do

Ask the two questions separately, in this order: *what supplied it?* then *what assures it?* When
the second answer is a test that closes a different predicate, you have found something.

---

## Rung 9 — the escaped decision

**What you cannot do yet.** You have every word you need. What you cannot yet do is turn them on
the code in front of you and get a verdict.

### The move

Go back and look at where the `3` came from.

Not "who chose 3". **Whether anyone did.**

In most systems carrying this exact line, the honest history is one of these: it was the sample
in the library's documentation; it was in the scaffold the previous service was copied from; it
was the model's suggestion, accepted because it looked reasonable; it was the number the team
used at a previous employer. Sometimes it is genuinely a default the client library ships and
nobody ever touched.

Run the vocabulary over it:

| | |
|---|---|
| **axis** | never declared — nobody wrote down that retry-count was a dimension worth governing (rung 1) |
| **ground** | none consulted — not the rate limits, not the latency budget, not the gateway's degraded behaviour (rung 3) |
| **tolerance** | never stated, so the admission test was never run and could not have been (rung 2) |
| **commitment level** | outcome-level, in the artefact — the strongest kind of commitment available (rung 5) |
| **residual discretion** | zero, at the act (rung 6) |
| **assurance** | a green suite, closing a predicate that is not the one at issue (rungs 7, 8) |
| **principal** | nobody |

Every governance property is absent. The commitment is total. **And it governs production.**

<!-- ddd:ref id=term:escape -->
> **Escaped** — determined *never*, by nobody: decided-by-nobody as a first-class category.
> Latent defect exposure. **The only forbidden state.**

Read "the only forbidden state" as written. Not the worst state, not a state to minimise —
**the only one the framework forbids outright.** A decision resolved badly by a named principal
against stated ground is a decision you can find, argue with, and revise. This is not that. There
is nothing to argue with.

<!-- ddd:ref id=DDD-frame-15 -->
And here is the part that takes a moment. The act still happened. Every request that hit that
policy got a retry count, and the system behaved. Canon puts it in one line: at every completed
act the demand is discharged — by a filed decision, an actor's judgement, an **arrangement
default**, or an uncontrolled draw. **Demand is never unmet, only ungoverned**
*(`DDD-frame-15`, **projected**)*.

That is the whole of rungs 5 through 9 arriving at once. The determination did not wait for
someone to make it. It was made — by the library author who picked a sample value, for a system
they have never seen, under load they cannot imagine, and nobody who answers to you.
The work you thought you had avoided by not deciding was performed anyway, by the last party in
the chain who touched the artefact. **You cannot decline to determine. You can only decline to
govern.**

<!-- ddd:ref id=DDD-frame-04 -->
Canon predicts this shows up in your incidents: escaped decisions — consequential resolutions
with no adequate source-and-assurance combination — predict ungoverned failure modes and
design-review findings *(`DDD-frame-04`, **projected** — a prediction with an unrun falsifier,
not a measured finding; if escaped-decision analysis identifies nothing that ordinary workflow
review does not, across a set of postmortems, the claim fires)*. You are entitled to test it
against your own postmortems, and entitled to disbelieve it if it fails.

**Where the risk actually is.** Rung 8's grid had four unassured cells and treated them alike for
escape risk. This one is worse than the other three, and the difference is not the risk — it is
the **findability**. An engineer's unassured 03:00 change leaves a trace: a commit, a name, a
chat message. This leaves a green build and a file that looks exactly like every well-governed
file in the repository. The register shows coverage. There is nothing to grep for, because
*nothing is missing* — the value is right there, doing its job.

### On the decision

Go and find out where your retry count came from. Actually go.

The finding is usually not the number. It is that the question has no answer, and that nobody had
previously noticed the question had no answer. That is the thing this track exists to make
visible, and you can now see it in nine minutes in a repository you already know.

### What you can now do

Name an escaped decision, out loud, with the reason it qualifies — no axis, no ground, no
principal, and total commitment. That is the capability the first nine rungs were for.

**And it is only capability.** You can see it. Nothing about seeing it has changed anything in
your system, and no one is answerable for what you now know. That is rung 10.

---

## Rung 10 — discharge

Everything up to here you could do by reading. This rung you can only do by acting, and it is the
first one that puts your name on something.

### Why the previous nine do not count

<!-- ddd:ref id=term:capability -->
Rungs 1 through 9 gave you **capability** — a typing over the ground you can read and the
distinctions you can resolve against it. Capability is the entry fee. It is what lets you attempt
the work, and it is not evidence that you did it.

The distinction is not pedantry, and rung 9 is the proof. You can now identify an escaped
decision precisely. Identifying it changes nothing: the value still governs, still has no axis,
still has no principal. **A track that ends at rung 9 has taught you to describe your system more
accurately and has improved it by exactly nothing.**

<!-- ddd:ref id=DDD-frame-16 -->
Nor can you sit the question out. Discharge is act-indexed — standing supply is inherited per
act, occasioned supply produced per act, and there is no act-free discharge; governance never
chooses *whether* demand is supplied, only *by what*, chosen in advance or defaulted at the act
*(`DDD-frame-16`, **projected**)*. Your system is discharging that decision on every request
right now. Not recording it is not neutrality. It is choosing the arrangement default and
declining to say so.

### The decision changes here, and you are told why

Rungs 1 through 9 used the retry count deliberately, and one property of it did the teaching:
**nobody disputes the answer.** Three, five, ten — no one has a position worth defending, which
left the vocabulary as the only thing in the room. That is what a worked example is for while the
words are still new.

It is the wrong property for this rung. A discharge you cannot disagree with teaches nothing
about being the principal for one. Naming yourself accountable for a value nobody contests costs
nothing, and a rung that costs nothing has not moved the stake it exists to move. So the worked
example changes, once, here:

> **How long do we keep customer support transcripts?**

Pick your own equivalent if you have one — any axis where competent colleagues want different
values for stated reasons. The retry count is still yours to discharge, and you should; but do it
second, after you have felt what the first one costs.

### The act

**One decision. A real one, in a system you work on. Recorded.**

Five fields. Every one of them is required, and the last two are what make this a discharge
rather than a note.

| Field | What it must contain | Not sufficient |
|---|---|---|
| **axis** | the determinable, named — the dimension, not the value (rung 1) | "the data retention thing" |
| **value** | the determinate now governing (rung 1) | — |
| **ground cited** | what it is resolved against, with provenance and a date; **"none"** is a legitimate and valuable entry (rung 3) | "experience" |
| **α — declared assurance level** | how strong the evidence must be that tolerance is met, stated before you look at what evidence exists (rung 8) | "it's tested" |
| **principal** | a **named person** who answers when this is wrong (rung 4) | a team, a rota, a service |

> **Notation flag.** **α here denotes the declared assurance level.** Canon uses `α` in a
> different place — `DDD-cost-02`'s cost model, where it is a per-act cost parameter — and the two
> are unrelated. The collision is named rather than avoided because engineers will meet both; if
> it proves confusing in use, the track renames rather than canon.

#### Ground cited: "none" is the point

The field exists to be answerable, not to be filled. If you go looking and find that nothing was
consulted, **write "none consulted" and the date you established it.** That entry is worth more
than a plausible reconstruction, and reconstructing one is the failure this field is built to
prevent: a decision record that reads as governed because someone wrote something in the box.

#### α: declared before, not after

Declare the assurance level **before** you look at what evidence exists. Declared afterwards it
is not a standard, it is a description of what you happen to have, and it will always be met.

For retry-count under a peak-load tolerance, an honest α is high and an honest current state is
that you do not meet it. **Recording a decision you do not yet meet is a successful discharge.**
The record's job is to be true.

#### Principal: a person, and why not a team

<!-- ddd:ref id=term:accountability -->
> **Accountability** is a property of the arrangement, not of the executor: attribution of the
> determination, a persistent answerable party, and a borne consequence. An arrangement missing
> any of the three has not allocated the decision's consequence.

<!-- ddd:ref id=DDD-frame-08 -->
*(`DDD-frame-08`, **projected** — accountability is a relation, not an intrinsic capacity; an
arrangement naming an executor but no principal is incomplete.)*

Three components, and a team name supplies at most one:

<!-- ddd:ref id=term:attribution -->
<!-- ddd:ref id=term:answerability -->
<!-- ddd:ref id=term:liability -->

| Component | Canon |
|---|---|
| **attribution** | the record connecting the determination to the execution that produced it — provenance-shaped, and therefore checkable |
| **answerability** | the obligation to produce the chain: which determinations were made, by whom, against what ground |
| **liability** | bearing the consequence |

"The platform team" has no obligation to produce a chain and bears no consequence. Rung 4's
sentence applies exactly: a judgement allocation naming no accountable party is **escape with an
executor attached**. If you cannot name a person, you have not finished the rung — and finding
that you cannot is itself a finding worth recording.

**It may be you.** For most first discharges it should be. That is the discomfort this rung is
for, and it is the whole difference between rung 9 and rung 10.

#### Where it goes

Wherever your team will actually find it — an ADR, a decision log, a header comment above the
policy. The location is not the point. Two properties are, and they are testable:

1. **It is retrievable at the act it governs** — the next person changing that policy encounters
   it without having to know it exists.
2. **It distinguishes applied-and-satisfied from never-reached** — a reader can tell whether the
   decision was consulted or merely present.

<!-- ddd:ref id=DDD-ground-04 -->
And if you are recording a decision that was made long before you wrote it down — which, after
rung 9, is the likely case — **say so.** Canon requires two fields on a retro-filed decision: when
the gap was uncovered, distinct from when the act occurred, and that it was retro-filed at all. A
node added after the fact has different evidential status from one authored before it, and
without the marks, retro-filing launders escape into coverage: a later sweep reads the register
and reports clean *(`DDD-ground-04`, **projected**)*. Your record is a correction, not a
discovery that the decision was always governed. Write it as one.

### The worked example, finished

Two records. The first is the contested one; the second is the retry decision you have carried
since rung 1, discharged in four lines because it is now easy.

#### Transcript retention

| Field | |
|---|---|
| **axis** | `retention-period` for customer support transcripts |
| **value** | 24 months |
| **ground cited** | the statutory minimum for the records class (institutional, verified against the regulation's text, 2026-08-18); the data processing agreement's ceiling (institutional, contractual); storage cost per month at current volume (controlled, measured); **support's argument that older transcripts resolve repeat cases: asserted, never measured — no ground is available for it** |
| **α** | a legal review confirming the value sits inside both the statutory floor and the contractual ceiling, re-run whenever either moves — **met at filing, and it decays** |
| **principal** | the named data protection owner. **Not** the platform team, **not** the engineer who set the cron job |
| **retro-filed** | yes — value in force since the retention job shipped, gap uncovered 2026-08-18 |

Notice four things this record does that the retry record could not.

**The value is contested and the record does not hide it.** Legal wants the floor, support wants
longer, and the ground line says which of those positions has ground behind it and which does not.
"Asserted, never measured" is the single most useful line in the record, and writing it is a small
act of nerve.

**The ground is mostly institutional** — a statute, a contract — which rung 3 flagged as the least
settled of the five kinds and the one whose mechanism is an open question upstream. You are
governing against authority rather than against measurement, and the record says so rather than
dressing it as a technical finding.

**α is met and still decays.** The retry record's α was unmet, which is easy to write. This one
was satisfied at filing and stops being satisfied the moment the regulation or the contract moves.
A declared assurance level with a decay condition is doing more work than a green tick.

**The principal is uncomfortable, which is the point.** The engineer who wrote the cron job is the
executor. The platform team is a name. Neither answers to the regulator. Whoever does is the
principal, and if the record cannot name them, you have found something more important than the
retention period.

#### Retry count

| Field | |
|---|---|
| **axis** | `retry-count` for outbound calls to the payment gateway |
| **value** | 3, with exponential backoff — **unchanged** |
| **ground cited** | provider rate limits (published, read 2026-08-18); checkout latency budget p99 800 ms (owned by the checkout team); **degraded-gateway behaviour: none consulted — no load test exists against the degraded path** |
| **α** | the closed half assured mechanically in CI; the open half requires a load test against the degraded path — **currently unmet** |
| **principal** | the named engineer owning the payment integration |
| **retro-filed** | yes — act ≈ 2024, gap uncovered 2026-08-18 |

Nothing about the system changed. `3` is still `3`, and the code is untouched. What changed is
that a decision which was escaped is now governed, its ground is stated including the part that is
missing, its assurance level is declared and honestly recorded as unmet, and a person answers for
it. **That is the discharge**, and it is the whole of what rung 10 asks — the same five fields,
whether the value is fought over or nobody has ever thought about it.

Both took under an hour between them, and they are the only part of this track that altered
anything.

### What you can now do

Nothing new. **You have done something**, which is the difference the track was built around.

---

## Where this track ends

Ten rungs, two decisions, three actors, and no claim that you are now competent at anything.

Rungs 1–9 gave you capability: vocabulary that makes things visible which were previously not
even invisible — they were simply not the kind of thing you looked for. Rung 10 was the first act
you own, and it is one act, on one axis, in one system. Whether the vocabulary holds up across
the next fifty decisions is a question this track cannot answer and does not claim to.

**What this track deliberately does not do.** It does not measure anything. There are frameworks
in canon for quantifying determination demand, and none of them is cited here, because "learn the
determination vocabulary" has no acceptance predicate that closes — there is no test that settles
whether you learned it. Reaching for a measure where nothing closes would be precisely the error
rung 7 taught you to name, committed by the document that taught it.

<!-- ddd:ref id=term:governing-decision -->
The next thing to do is not another track. It is the second discharge, then the fifth, until
recording the axis alongside the value is what writing the value feels like.
