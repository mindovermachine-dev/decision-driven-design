# Step 1b — Map the flow of demand `[PROPOSED]`

**Register: `[PROPOSED]`.** The step's place and scope are ruled; its content is not. Emil ruled
that mapping the flow of demand through a process is a method step, placed after step 1 (Round
23), that the step is general and each process declares its own kinds of demand (Round 24), and
that the method gives the PDLC's kinds as a starting point (Round 25). The rounds are verbatim in
the demand-flow session's [`rulings.md`](../meta/sessions/2026-11-08-demand-flow/rulings.md) and
filed as `DDD-dec-118`. The procedure below, the card's fields and the worked example are
Claude's, `UNVERIFIED — Emil review`. The four claims the step rests on are **projected** and
scoped to the PDLC. Moving the step to ruled is a MINOR release (`DDD-dec-82`).

**Numbering.** "1b" holds the step's place after step 1 until the numbering is ruled (open item
N-1 in the session's [`successor-items.md`](../meta/sessions/2026-11-08-demand-flow/successor-items.md)).
No file is renumbered.

**Weakest point.** The kinds of demand. The PDLC has three, and nobody knows whether another
process has the same three. One process is the whole of the evidence (Round 24: "I don't think we
have enough evidence to say if the three kinds of demand entities are general enough for all
processes"). Every use of this step on a second process is a test of them.

## What the step does

Step 1 maps acts, one occurrence at a time. It does not say how demand arrives in a running
process, from where, or who may order it. This step does. It takes the act map and traces demand
across it: where each item enters, which owner orders it, which seams it crosses, and where it is
discharged. Then it asks what else pulls, and classifies every source of pull into the kinds of
demand the process declares.

The step is not about delivery. "Delivery" is reserved by upstream `core/13` for whether an
authored decision reaches the act it governs. This step is about how demand arrives and is
ordered, which neither delivery nor supply (who resolves a governing decision, and when) says.

## The procedure

Seven parts, in this order. Each part's source is named. The order is the one the PDLC was mapped
in (Rounds 1–22 of the 2026-11-07 session's
[`rulings.md`](../meta/sessions/2026-11-07-sdlc-and-pdlc/rulings.md)).

1. **Map acts forward from the request.** This is step 1, run first
   ([`01-map-and-index-acts.md`](01-map-and-index-acts.md)). Its act map, with addresses and the
   causal time index, is this step's ground.
2. **Name the loci.** For each kind of change the process makes, name the coordinate of
   `DDD-frame-01`'s tuple ⟨task, ground, acceptance relation, tolerance, arrangement, assurance⟩
   that it moves. A change that moves no coordinate is a finding. (PDLC: four loci, What,
   Assurance, Ground and How, [`pdlc.md`](../applications/pdlc/pdlc.md) §7.)
3. **Place owners per decision.** For each boundary decision, name the one owner who holds the act,
   with its control and liability. An owner is a scope: a set of decision kinds and element kinds
   one grant covers (`DDD-dec-117`). A role is a named, reusable scope. Every other owner reads the
   act's verdict only as ground (`DDD-flow-04`; PDLC: pdlc.md §6).
4. **Declare each owner's ground and the seams.** Each owner controls its own ground. For each
   seam between owners, say what crosses it, which act produces it and which act reads it. Ground
   that crosses a seam is read-only for the receiver (PDLC: pdlc.md §2.1 and §13). Splitting the
   process into owners manufactures seam demand (upstream `term:seam`, `core/06`); this part makes
   it visible, it does not remove it.
5. **Trace one demand item end to end, then ask what else pulls.** Follow one real item from where
   it enters to where it is discharged, act by act, along edges of the act map. Then ask what else
   makes demand arrive, and list each source of pull.
6. **Classify each source of pull into the kinds of demand the process declares** (Round 24). For
   each source, say where it enters (an act of the map), who orders it, and where it is
   discharged. The kinds are declared per process, not fixed by the method. Start from the PDLC's
   three (below), and declare what you keep, add or drop.
7. **Put a meter on each owner and each seam.** For each owner, the measure it answers for. For
   each seam, the measure that shows its price. (PDLC: the DORA keys for the How owner, the option
   metrics for the When owner, and the meter, the What-locus share of o6 directions, for the What
   owner and the What → How seam: pdlc.md §3, §6, §10, §13.)

## The starting point: the PDLC's kinds of demand

*Ruled (Round 25):* the method references the PDLC's kinds "to give users a starting point".
**These three are the PDLC's, offered as a start. They are not the method's fixed set**, and
nothing claims they hold for any other process (Round 24). Each is tested relative to the
decisions in force:

| Kind | One-line test | In the PDLC: enters at, ordered by |
|---|---|---|
| **New** | No governing decision in force covers it: the decisions must change before it can be met | o0, the option pool; the When owner, at o2a |
| **Owed** | A governing decision in force covers it, and an act does not meet that decision: an escape | oC, the What owner's classification; the How owner, in the SDLC |
| **Own-ground** | It concerns no decision about what the process must produce, but the ground of the arrangement that realises the decisions | oG; the How owner, in the SDLC |

**How to use them.** Test each source of pull in your own process against the three. Then declare
your process's kinds:
- **keep** a kind that some source of pull of yours falls into;
- **add** a kind for a source that falls into none of the three;
- **drop** a kind no source of yours falls into;

and for each, name the source of pull that made you keep, add or drop it.

**Record the declaration.** Write it down beside your act map, in the form of the table below, and
send it to this repository as a field report (the issue template), citing `DDD-dec-118`. Each
declaration is evidence for the open item that decides whether the kinds are general: a second
process whose declared kinds match the PDLC's, or do not (promotion item P-1). A declaration that
matches is as useful as one that does not.

| Kind | Kept, added or dropped | Its one-line test | The source of pull that made you do it |
|---|---|---|---|
| … | … | … | … |

## The claims it rests on

All four are this repository's, filed by `DDD-dec-118`: **projected**, session-authored,
`UNVERIFIED — Emil review`, and scoped by `region` to **the PDLC only**. Generality is not claimed.
Statements are quoted from the claim files, whitespace-normalised. The claim file governs.

| Claim | Kind | Status | Statement |
|---|---|---|---|
| [`DDD-flow-01`](../core/claims/DDD-flow-01.yaml) | conceptual | **projected**, PDLC only | In the PDLC, relative to the decisions in force, an arriving demand item is of exactly one of three kinds: new (no governing decision for it is in force yet), owed (a governing decision is in force but an act does not meet it, which is an escape, including the undelivered case of core/13) or own-ground (it concerns the ground of the arrangement that realises the decisions, which in the PDLC is the How owner's own ground). |
| [`DDD-flow-02`](../core/claims/DDD-flow-02.yaml) | empirical | **projected**, PDLC only | In the PDLC, ordering a queue of demand items is a decision whose ground includes the ground of every kind of demand in the queue, so a queue that mixes kinds under one orderer who does not hold each kind's ground is ordered, for the kinds whose ground is missing, by judgment from ground not held. |
| [`DDD-flow-03`](../core/claims/DDD-flow-03.yaml) | conceptual | **projected**, PDLC only | In the PDLC, a demand item enters at the act of the owner whose ground detects it, and reaches other owners only along declared seams, as ground read-only for the receiver, not along the reporting lines between the people who hold the owners' scopes. |
| [`DDD-flow-04`](../core/claims/DDD-flow-04.yaml) | normative | **projected**, PDLC only | In the PDLC, responsibility is placed per decision: for each boundary decision exactly one owner holds the act, with its control and liability, and every other owner reads that act's verdict only as read-only ground. |

Upstream canon they derive from, read at the pinned `v5.15.2`: `core/05` §5 (answerability,
liability and control are separable), `core/13` (escape and the undelivered case,
`DDD-delivery-02`), `core/14` §1 (`DDD-frame-01`) and §5 (the act address, `DDD-ground-06`).

## The step card

Fields are the method's ([`README.md`](README.md)). Claude's assembly, `UNVERIFIED — Emil review`.

| Field | Content | Source |
|---|---|---|
| Step | 1b — Map the flow of demand. After step 1; numbering open (N-1) | Round 23; `DDD-dec-118` |
| Decision discharged | Which kinds of demand the process has, where each enters, who may order it and where it is discharged; and which owner holds each boundary decision. The commitment level is not filed | Rounds 23, 24; `DDD-flow-01`, `-04` |
| Ground in | The act map from step 1, with addresses and the time index. The request and the process's owners, each a scope under a grant. The decisions in force, against which every kind is tested | Step 1; `DDD-dec-117`; `DDD-flow-01` |
| Act | The seven parts above. Done by whoever maps the process, with each owner confirming the decisions placed with it | Procedure as done for the PDLC (Round 23) |
| Artefact out | Graph data beside the act map: the declared kinds with their tests, entry acts, orderers and discharge acts; the sources of pull, each classified; one traced item per kind; the seam table; a meter per owner and seam. PDLC: [`demand-flow.ttl`](../applications/pdlc/graph/demand-flow.ttl), checked by `check.py` | Round 23; pdlc.md §2.1 |
| Value made visible | **Who may order what**, and where an orderer lacks the ground for a kind in its queue. **Where demand enters and which seams it crosses.** **Owed demand that sits unpaid**: an escape against a decision in force, waiting in a queue nobody orders on its own ground | The prompt's minimum (item 5); `DDD-flow-02`, `-03` |
| Cost and relocation | One mapping per process, paid in the mapper's and the owners' judgment, and redone when an owner or a seam changes. Splitting a process into owners manufactures seam demand; the step prices it and does not remove it. Skip the step and the ordering decision still gets made: by one orderer over a mixed queue, from ground it does not hold | Upstream `term:seam`, `term:conservation`; `DDD-flow-02` |
| Exit check | Every source of pull is in exactly one declared kind. Every kind has one orderer, who holds the ground the kind is judged on. Every entry and discharge is an act of the map. At least one item per kind is traced along edges of the map, through its kind's entry and discharge acts. Every crossing is a row of the seam table. Every owner and seam has a meter. For the PDLC, `python3 applications/pdlc/graph/check.py` checks all but the last two | Claude's reading, `UNVERIFIED — Emil review` |
| Principal | The holder of the grant every owner's scope delegates from (in the PDLC, the product's genesis grant). A dispute about placement escalates there | pdlc.md §2, §6 (rule 3). The role is not filed for the method |

## Worked example: the PDLC

*Ruled (Round 23):* the worked example is "the feature, the bug and the debt flows through When,
What and How". It is the acme shop of [`applications/pdlc/`](../applications/pdlc/), an
illustrative, invented record: issue #101 (new), #103 (owed) and #104 (own-ground). Graph data:
[`demand-flow.ttl`](../applications/pdlc/graph/demand-flow.ttl), with the act map in
[`acts.ttl`](../applications/pdlc/graph/acts.ttl) and
[`../applications/sdlc/acts/acts.ttl`](../applications/sdlc/acts/acts.ttl).

Each flow is a stream of state changes in causal order: each line is an act whose ground reading
contains the line before it (`DDD-address-01`). No categorical axis is embedded in space. The
address follows the act: its layer path, then surface · locus · authority (pdlc.md §11,
sdlc.md §3). The SDLC's acts read the locus the issue declares, which is How for all three issues.
Seam crossings are marked `══`. The holding owner is outside the address, as the address leaves
the occupant out (`DDD-ground-06`).

**New: the feature (#101).** The kind's test: no decision in force lets a returning customer
reorder in one step.

```
o0   propose an option      PDLC                    pool · none · owner scope        When owner          → ex:opt1 in the pool            ◀ enters
o2a  release for work       PDLC                    pool · none · owner scope        When owner          → pulled, rank 1, as #101        reads o0
o1   frame the issue        PDLC                    issue · How · owner scope        locus owner         → #101 framed, locus How         reads o2a
 ══  When → How: a released issue, in order (o2a → o2b) · What → How: the What and its product assurance (o1 → o1b)
o1b  plan the realisation   PDLC▸SDLC▸frame         issue · How · none               How owner           → the plan, on the issue         reads o1 (new)
o2b  allocate the occupant  PDLC▸SDLC▸frame         issue · How · base map           How owner           → label or assignee              reads o1b, o2a
o3   dispatch               PDLC▸SDLC▸frame         issue · How · base map           How owner           → a session started              reads o2b
o4   commit the charter     PDLC▸SDLC▸build         branch · How · none              How owner           → prompt + bootstrap             reads o3
o5   work run               PDLC▸SDLC▸build         branch · How · none              How owner           → commits                        reads o4
o9   gate the candidate     PDLC▸SDLC▸accept        candidate · How · none           How owner           → required checks on the SHA     reads o5
o10  approve <sha>          PDLC▸SDLC▸accept        candidate · How · base map       locus owner         → an approval                    reads o9
o11  agent review           PDLC▸SDLC▸accept        candidate · How · approval       How owner           → the gates App's check          reads o10
o12  fast-forward main      PDLC▸SDLC▸land and run  trunk · How · approval           How owner           → main at the SHA                reads o11
o13  deploy, dark           PDLC▸SDLC▸land and run  production · How · none          How owner           → production, dark (r:o13-1)     reads o12
 ══  How → What: the change in production, dark, with its verdicts and telemetry presence
oR   ready for users        PDLC                    production · What · owner scope  What owner          → ex:ready101: ready             reads o13
 ══  What → When: the ready-for-users verdict
o16  turn the toggle on     PDLC                    production · none · owner scope  When owner          → ex:on101, released 2026-11-08  reads oR  ◀ discharged
oU   use the product        PDLC                    use site · none · none           software and users  → evidence and telemetry         reads o16
```

Ordered once, by the When owner at o2a, on market ground. Two seams in, two out. The record also
holds an o6 direction and a second o5 run for #101; repetition at one site is told apart in the
occurrence record ([`example-record.ttl`](../applications/sdlc/acts/example-record.ttl)), not in
the trace.

**Owed: the bug (#103).** The kind's test: the Place order Decider's stock invariant is in force,
and reorder breaks it.

```
oU   use the product       PDLC                    use site · none · none         software and users  → the out-of-stock line in the basket
 ══  How → What: telemetry of the product in use; a user's report
oC   classify the defect   PDLC                    use site · What · owner scope  What owner          → ex:class103: owed             reads oU  ◀ enters
 ══  What → How: the classification verdict, owed (oC → o1b). No o2a, no pool
o1b  plan the realisation  PDLC▸SDLC▸frame         issue · How · none             How owner           → the plan                      reads oC (owed)
o2b  allocate … o12        PDLC▸SDLC▸…             as for #101                    How owner           → ordered by the How owner, not the When owner
o13  deploy, dark          PDLC▸SDLC▸land and run  production · How · none        How owner           → production, restores r:o13-1  reads o12  ◀ discharged
```

Ordered by the How owner, measured as time to restore. No oR and no o16: the fix restores
behaviour the What already promised (pdlc.md §9). The When owner sees it only as cadence. Detected
on the How owner's telemetry and a user's report, it enters at the What owner's oC, because only
the What in force can tell owed from new. That is the tension `DDD-flow-03` flags: whether
"detects" means first sighting or classification. `check.py` prints it as a note.

**Own-ground: the debt (#104).** The kind's test: no decision about what the shop must do is at
stake; the How owner cannot deploy without a manual cache purge.

```
oG        frame own-ground work  PDLC▸SDLC▸frame         issue · How · owner scope  How owner  → #104 framed, kind own-ground  reads earlier o13s (its own record)  ◀ enters
o1b       plan the realisation   PDLC▸SDLC▸frame         issue · How · none         How owner  → the plan                      reads oG (own-ground)
o2b       allocate … o3          PDLC▸SDLC▸frame         as for #101                How owner
o4        commit the charter     PDLC▸SDLC▸build         branch · How · none        How owner  → r:o4-104, 2026-11-07          ── recorded so far
o5 … o12  run … fast-forward     PDLC▸SDLC▸…             as for #101                How owner  → not yet taken
o13       deploy, dark           PDLC▸SDLC▸land and run  production · How · none    How owner  → not yet taken                 ◀ discharged when reached
```

It starts inside the SDLC and crosses no seam on the way in (pdlc.md §13). Ordered by the How
owner, justified by the DORA keys. Until Round 26 (2026-11-08, in the 2026-11-07 session's `rulings.md`) it
sat in the example option pool as a How-owner option, where the When owner would have ordered it
on market ground. Round 26 moved it here.

**What else pulls.** pdlc.md §9 lists six sources of pull. Classified, as the step's part (6):

| Source of pull | Kind | Detected on | Enters at | Ordered by | Pool |
|---|---|---|---|---|---|
| A market need | New | When owner | o0 | When owner | Yes |
| Users can't do the designed act (product assurance not met) | New | What owner (evidence in use) | o0 | When owner | Yes |
| The software deviates from the What in force | Owed | How owner (record, gates, telemetry); users | oC | How owner | No |
| A reported defect that is the What being wrong | New | How owner, What owner | o0, after oC | When owner | Yes |
| Technical debt, the arrangement, the How owner's ground | Own-ground | How owner | oG | How owner | No |
| Regulation, or another change in the What owner's ground | New | What owner | o0 | When owner | Yes |

**What the map makes visible here.** From `check.py`'s flow readings:
- **Who may order what.** The When owner orders new demand. The How owner orders owed and
  own-ground demand. No queue mixes kinds under an orderer who lacks a kind's ground.
- **Where demand enters and which seams it crosses.** New demand crosses When → How and What → How
  on the way in, owed demand What → How (after How → What telemetry), own-ground none.
- **Owed demand that sits unpaid.** #103 was restored the day it was classified. #104 is
  own-ground, not owed, and sits at o4: the map shows the How owner owes the rest of its path. In
  a classic backlog both would sit in the When owner's order (`DDD-flow-02`'s violation case).

## Relation to other steps

The step draws on step 1 (the act map), step 4 (ground), step 7 (accountability per decision),
step 9 (the record that holds the traces) and step 10 (supersession on evidence in use, which is
where new demand from the What owner comes from). Step 7's line, "Attribution, principal,
authority, stake, remediation per allocation", is applied in the PDLC to the decisions this step
places (pdlc.md §6, Round 28, R28).

**The method's other sustained example** is the HTTP slice of Varve's quick start
([`quick-start.md`](quick-start.md)), ruled 2026-11-02. This step's is the PDLC (Round 23). How
the two relate is open item E-1 for Emil.

## What would break it

- **The claims.** Each `DDD-flow` claim carries its falsifier. The two that bite first: a demand
  item in the PDLC that is none of new, owed or own-ground (`DDD-flow-01`), and a PDLC queue mixing
  kinds under an orderer without a kind's ground that orders that kind as well as its own owner
  would (`DDD-flow-02`).
- **The kinds beyond the PDLC.** A second process whose sources of pull do not fit the three. That
  does not break the step, which declares kinds per process. It decides promotion item P-1.
- **The step, as a method step.** The draft's default falsifier, `[PROPOSED]`: "practitioners
  perform the step and cannot name the value it gave them."

Previous: [01 — Map and index acts](01-map-and-index-acts.md) · Next: [02 — Anchor authority](02-anchor-authority.md) `[PROPOSED]` · [All steps](README.md)
