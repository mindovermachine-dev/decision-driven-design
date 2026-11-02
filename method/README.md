# The method

Decision-Driven Design as a practical method: ten steps, each presented as a step card. **Only
step 1 is ruled, and it is ruled for test**: its claims are projected and wait on an independent
case. Steps 2 to 10 are `[PROPOSED]`, and their cards carry nothing beyond what is filed.

**Weakest point.** The sequence itself is `[PROPOSED]`. The ten steps, their order and the step
card's fields come from one session draft, not from a ruling. Only step 1's form was ruled.

| # | Step | Register | Card |
|---|---|---|---|
| 1 | Map and index acts | **Ruled for test**; claims projected; waits on T2b | [01](01-map-and-index-acts.md) |
| 2 | Anchor authority | `[PROPOSED]` | [02](02-anchor-authority.md) |
| 3 | Surface decisions | `[PROPOSED]` | [03](03-surface-decisions.md) |
| 4 | Declare ground | `[PROPOSED]` | [04](04-declare-ground.md) |
| 5 | Classify closure and set assurance | `[PROPOSED]` | [05](05-classify-closure-and-set-assurance.md) |
| 6 | Allocate | `[PROPOSED]` | [06](06-allocate.md) |
| 7 | Complete accountability | `[PROPOSED]` | [07](07-complete-accountability.md) |
| 8 | Derive forward | `[PROPOSED]` | [08](08-derive-forward.md) |
| 9 | Execute and record | `[PROPOSED]` | [09](09-execute-and-record.md) |
| 10 | Observe and supersede | `[PROPOSED]` | [10](10-observe-and-supersede.md) |

Try step 1: [`quick-start.md`](quick-start.md).

## Registers

| Register | Means | What moves it |
|---|---|---|
| `[PROPOSED]` | Written down, not ruled. Do not rely on it | A ruling, filed as a decision |
| Ruled for test | The form is ruled, and the claims it rests on are projected: argued, with falsifiers nobody has met | An independent test that the claims survive moves the step to **reported** |
| Reported | Exercised evidence: the claims it rests on have met their test | A falsifier firing moves it back to open |

The registers follow the method draft ("Projected means a clean derivation, unexercised. Reported
means exercised evidence") and `DDD-dec-74` ("ruled for test and projected, not reported"). This
table's wording is Claude's: `UNVERIFIED — Emil review`.

A step whose register moves is a MINOR release, and so is a card added. Editorial changes are
PATCH (`DDD-dec-82`). The version stays below 1.0 until all ten steps are ruled.

## The step card

Every step is presented in these fields. They are the method draft's fields
([`method-instructions-draft.md`](../meta/sessions/2026-09-27-act-address/method-instructions-draft.md),
`[PROPOSED]`).

| Field | Content |
|---|---|
| Step | Name and position |
| Decision discharged | What this step decides, and at which commitment level |
| Ground in | What must be declared before the step can run, with provenance |
| Act | What is done, and by which arrangement |
| Artefact out | What exists afterwards, preferably graph data, not prose |
| Value made visible | What the practitioner can now see, do, or refuse that they could not before |
| Cost and relocation | What the step costs and where demand went |
| Exit check | The acceptance relation for the step, and whether it closes |
| Principal | Who authorises the step's output |

A step whose value cannot be shown to the person doing it is a defect in the method, not a matter
of presentation (the draft's purpose, `[PROPOSED]`).
