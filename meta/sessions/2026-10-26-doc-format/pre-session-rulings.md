# Pre-session rulings — doc format

Given by Emil in conversation on 2026-10-26, before the session opened. They are recorded at arrival, not at close.

| # | Question put | Ruling |
|---|---|---|
| 1 | Is "only canon carries authority; every other folder exists for a named reader doing a named act" the principle? | **Yes.** Ruled. |
| 2 | Where does the format live, and is it checked by a validator? | Emil asked for Claude's recommendation. **Not yet ruled.** The recommendation follows, `[PROPOSED]`. |
| 3 | Does this run as its own session, with the harness guide parked? | **Yes.** Its own session; the harness guide resumes after. Ruled. |

## Ruling 2 — Claude's recommendation `[PROPOSED]`

`UNVERIFIED — Emil review`.

| Element | Recommendation | Reason |
|---|---|---|
| Schema | `spec/doc-format.md`, in this repository | `spec/` is where this repository's file formats live. Upstream cannot hold it: the charters name this repository's folders, and upstream carries no reference to its dependents. |
| Canon format | Unchanged, upstream (`ddd:contract`, `core/README.md`) | Ruling 1 places authority there. This session does not touch it. |
| Charters | One per folder, in that folder's `README.md`: reader, act served, opener, authority | A reader arriving in a folder sees its charter without leaving it. The spec holds the schema; the README is the instance. |
| Opener | A `ddd:doc` comment block: `reader`, `act`, `pin`, `basis`, `status` | It sits beside `ddd:contract` and `ddd:ref`, so the same tooling reads it. |
| Check | Extend `validate-core-order.py`: the block is present; `reader` and `act` are non-empty; every `basis` ID resolves at the pin; `status` is a registered value | That script already resolves `ddd:ref` against the pin, so `basis` gains W5 and W6 staleness for free. |
| Severity | Warnings first. A move to errors is a later ruling, after roll-out | Errors from day one would fail every existing document at once. |

**Weakest point.** `basis` resolves only upstream claims and terms. Successor item S-8 already records that decisions cannot be pinned. A document resting on a decision would warn wrongly until S-8 lands.

**Falsifier.** If, after roll-out, the check stays silent on a document whose basis claim has changed status since the pin, the check adds nothing over `ddd:ref`, and the opener should be prose only.

## Ruling 2 — given (Emil, 2026-10-26)

**Agreed as recommended.** Ruled. The recommendation above stands as the ruling, unchanged. Its weakest point (S-8) and its falsifier are carried into GATE 2. Emil also ruled to proceed to GATE 1.
