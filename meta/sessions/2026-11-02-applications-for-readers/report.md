# Gates 2 and 3 — report

2026-11-02, branch `claude/applications-for-readers-2026-11-02`. The session stops here for Emil's
review.

## Weakest point first

**The reader test fired its first limb, and so cannot show that the new format helps.** All four
readers, two on the old `what.md` and two on the new pair, scored 8 of 8. The rubric was written to
avoid the ceiling the 2026-10-26 pilot hit, and it hit the same ceiling. The pre-registered rule is
plain: the new text's mean on the hard criteria (4.0) is not above the old text's (4.0), so limb 1
fires. What the test does show is that the rewrite lost nothing a capable reader needs for this
task, and that no reader of the new text found the format's own devices confusing (limb 2 did not
fire).

The readers are model proxies. A model reads an 861-line record and a 646-line application equally
well. The person who found the old text unreadable was Emil, and the format exists for people. A
human first-contact test is the test that can decide this, and it is not run.

## What changed

| Document | Before | After |
|---|---|---|
| `applications/README.md` | 10 lines; one folder listed | Both folders, how the documents are written, what they do not carry |
| `organizations/README.md` | Four claims and falsifiers, with a stale "UNVERIFIED" note | Four predictions, each with "it is wrong if", the claims quoted verbatim |
| `sdlc/README.md` | v3 history; stale statuses for the What and the How | Where to start, by task; two examples and why; the general-to-software reading |
| `sdlc/what.md` | 861 lines, opening with the move's status and rulings | `what.md` (646, practitioners) and `what-reference.md` (264, tool builders) |
| `sdlc/how.md`, `how-vocabulary.md` | 700 and 113 lines, written as a charter's answer | `how.md` (599) and `how-reference.md` (270); the vocabulary merged |
| `sdlc/how-examples/README.md` | Opened with supersession history; stale counts | Run it, the cast, the decisions, the checks; history last; counts re-run |
| `sdlc/production-as-ground.md` | "Location: proposed" and a status block before the content | A task-named opening; body unchanged; three wrong cross-references corrected |

Every document opens with its reader, what they can do, and how settled it is, in words. No
decision or claim id appears in running text: M-1 holds. The ids are in each document's closing
"Where this comes from" table and its `ddd:doc` block.

## Predictions

| # | Prediction | Outcome |
|---|---|---|
| P-1 | `what.md` under 450 lines; the pair shorter than 861 | **Not held.** 646 and 910. Most of the old length was rules, not history |
| P-2 | `how.md` loses at least a quarter | **Not held.** 700 to 599, 14%. Restoring the unsettled markers (below) added lines back |
| P-3 | At least one rule found only inside deliberation | **Held.** Five, all in `how.md`'s "thesis, tested", extracted into the body |
| P-4 | `production-as-ground.md` keeps its argument structure | **Held** |
| P-5 | No validator result changes | **Held.** `scripts/ci.py` passed after every commit |
| M-1 | No id outside the block and the basis table | **Held** |
| M-2 | CI passes after every Gate 2 commit | **Held** |
| M-3 | The independent check finds no lost or changed rule | **Not held.** It found 64 points; every one is fixed or given a recorded reason (`independent-check.md`) |

## The independent check was the most useful step

The equivalence tables written alongside the rewrite marked every row "same". Three agents that had
not written the text then found 64 differences. Five were serious, and they include:

- a falsifier weakened from "or" to "and", which made a claim harder to refute;
- a definition of the principle stated without the limits canon gives it;
- "a field belongs if and only if a Decider reads it" weakened to "only if";
- five wrong statements about the worked example (customers request refunds; staff do not);
- **the How rewrite marking as decided what the old text left proposed.** The conventions forbade
  this upgrade, and the rewrite made it anyway in one opening sentence.

Plain prose made these slips easy to write and easy to find. Record style hid them under ids. The
lesson for `apparatus/` is to run the independent check on every document before the reader test,
not after.

## The reader test (Gate 3)

Pre-registration `prereg-first-contact.md`, SHA-256 `79901d47e00967a4…`, committed at `45ab620`
before any rewrite existed, re-verified unchanged at this report.

| Limb | Rule | Observed | Fires |
|---|---|---|---|
| 1 | New mean on K3, K5, K6, K8 above old mean | Old 4.0 (A 4, C 4). New 4.0 (B 4, D 4) | **Yes** |
| 2 | A new-text reader names the format's devices as confusing | None did. Their "unsure" items are about content, or about documents they were not given | No |

Also reported, as pre-registered: all four scored 8 of 8. No old-text reader named ids or section
numbers as confusing either. The answers and the scoring are in `first-contact/`.

**Pre-registered consequence.** "F3 and F7 are not shown to help this reader. The fallback named in
Gate 1 applies: ids stay out of sight, but invisible point-of-use markers replace the closing table
as the trail. Emil rules."

**What first contact found about the content.** Every reader, on both versions, found the same
gaps. None of them is the format's to fix:

1. **The What has no unpaid order.** `Order` is "a placed, paid order", and `Order placed` carries
   `paid_total`. The task could not be done without a product decision on payment.
2. **The example contradicts the wire rule.** Its one scenario puts the customer's claim inside the
   command's `with`. The What says the subject is "supplied beside the command, never inside its
   `with`". This is a defect in `acme-shop.ttl`, or in the rule.
3. **Anchoring a decision that both creates and changes elements is not specified.** The rule
   covers creation and change separately.
4. **Subject coverage is ambiguous, and the example may already fail it.** "Every pair of command
   and subject kind" could range over all subject kinds or only those a Decider serves. The example
   has one scenario for two commands.
5. **Whether "adding a field is a decision of its own" forces a separate decision** when the field's
   owner is created in the same change.
6. **No command carries an order identifier**, so how a command addresses its aggregate is not
   modelled.

## Rulings requested

1. **The format, after the test.** Limb 1 fired on a ceiling, and limb 2 did not. Options:
   (a) keep F1–F8 as ruled, and make a human first-contact test the deciding one before `apparatus/`;
   (b) apply the pre-registered fallback now: invisible point-of-use markers instead of the closing
   table; (c) both. Claude recommends (a) `[PROPOSED]`. The test showed no loss. The complaint the
   format answers was a human reader's. The fallback would trade one invisible device for another,
   and the closing table is what the independent check used to find most of its 64 points.
2. **Did merging the How settle its unruled parts?** The old `how.md` said "what was not ruled
   separately stays `[PROPOSED]` until the merge", and PR #41 merged, although it was titled "for the
   record, not for merge". The rewrite keeps all of those parts marked *(not settled yet)*.
   `DDD-dec-58` and `DDD-dec-59` appear to rule two of them word for word: coverage, and the three
   parts of an import. Rule which, if any, are now settled.
3. **The named-algorithm heading.** `DDD-dec-64` P-5 ruled the title "Named-algorithm primitives".
   The rewrite's heading is "Named algorithms — computation you name instead of deriving". Keep the
   ruled title, or accept the new one?
4. **The six content findings above.** Each is a successor item. Finding 2 is a defect in a ruled
   example and should be fixed first.

## Not done, and why

- **`authority.md`** is on PR #45, unmerged. It gets the same format after it merges.
- **`what/ontology.ttl` and `what/shapes.ttl`** still cite "what.md §6" and `how-vocabulary.md`. Both
  are hashed into the vocabulary edition the What-versions pin. Re-pointing them needs a new edition.
- **The project instructions** say the protocol token is decprov/1. It is dpp/1 (`DDD-dec-62`). They
  live outside the repository.
