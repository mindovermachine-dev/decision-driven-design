# Rulings — the authority profile, 2026-11-02

Rulings given during the session, verbatim, recorded when given. `prompt.md` stays the arrival
charter, and this file carries what came after it.

## The charter's own rulings

The list under "Already ruled; do not reopen" in `prompt.md`, verbatim there. It is filed as
`DDD-dec-85`, as `DDD-dec-54` filed the How charter's list.

## Round 1, 2026-11-02 — the plan approved; recorded in `DDD-dec-86`

Verbatim:

> Round 1, authority-profile session (2026-11-02). Plan approved with the rulings below.
>
> F-1 — ruled as read. An acceptance is its own signed record whose by and at are the acceptor and the time, and which pins the decision’s version hash. acceptedBy/acceptedAt as fields were Draft 3’s shorthand and are gone with A-10.
>
> F-2 — ruled: hashed members, never extensions. Anything a signature must cover (a grant’s scope, a baseline, a waiver’s expiry, a key binding) is a top-level dotted member inside the canonical form, as how-vocabulary.md does it. extensions is for what may change without a new version, and nothing authority-bearing may. Where I wrote “in extensions” earlier, that was wrong; this ruling replaces it.
>
> F-3 — [D2.11], stated. After Varve’s answer of 2026-10-28: header clocks are monotone by the writer’s clamp (ts = max(clock, head); a backwards wall-clock step yields equal timestamps, never a refusal); as-recorded replay is a fixture import through a writer whose injected clock returns each recorded timestamp in turn, never a re-stamped log; G6 is re-evaluation of the recorded log, which the store serves as-of; the stamped instant is the staging instant under group commit. Nothing in it changes the profile beyond what Q-6 settles.
>
> Q-1 to Q-5, Q-7 — ruled as answered, including: the genesis is founded, not accepted, and a transfer needs the successor’s acceptance; closing the prior genesis on transfer is not a revocation; an acceptance may be revoked; the grantor vouches for a new holder’s first key, with an optional since on a close for compromise; a machine is an identity named in a signed attribution record and any record carrying attributedTo is refused as acceptance, review, grant, waiver or key binding; a team is not a holder; one conformance class with thirteen properties, plus a reference evaluator labelled as not Writ’s suite.
>
> Q-6 — ruled: expiry is a header-clock time, and Writ follows. A position does not advance on a quiet product, so a position-based expiry never fires exactly where a waiver most needs to; a header-clock time is deterministic because the clock is in the log ([D2.3]). Writ’s definition is amended today to say a waiver’s review-by is a header-clock time, not a position.
>
> Q-8 — ruled as proposed. A grant delegates only if it says so, and only a subset of its own scope.
>
> Q-9 — ruled: extend the acme shop product. Records are added, never edited; what@4 is the correct cost of a decision that adds a What field.
>
> Q-10 — ruled as proposed. The violation-description field is covered by the profile; attestations are a successor item.
>
> Ids from 77; the supersession of -47 is right. Proceed through the seven commits; open the PR for the record when green.

### Where each ruling landed

| Ruling | Landed | State |
|---|---|---|
| F-1 acceptance record | authority.md §4.1; `DDD-dec-88` supersedes `-47` | ruled |
| F-2 hashed members, never extensions | authority.md §1.3; authority-vocabulary.md; every new record | ruled |
| F-3 `[D2.11]` | authority.md §6.2, verbatim as stated; the evaluator accepts equal clocks and refuses a backward step | ruled |
| Q-1 founded, not accepted; grant acceptance; transfer accepted | §2.2, §2.3, §3.3; `DDD-dec-87`; acme `GACC-*`; A4 | ruled |
| Q-2 revocation, chain falls; transfer close not a revocation; acceptance revocation | §2.3, §3.5, §4.6; acme p11; A5, A6 | ruled |
| Q-3 keys per product; first key by the grantor; `since` | §5.3; acme p13; A8 | ruled. Key loss (A-9) is flagged |
| Q-4 review | §4.5; acme p15 | ruled |
| Q-5 attribution; `attributedTo` refused; teams | §5.1, §5.2; acme p1, p4; A2 | ruled |
| Q-6 expiry by header clock; Writ follows | §4.4, §6.2; acme p14, p15; A10 | ruled. Writ's amendment is Emil's act |
| Q-7 one class, 13 properties, reference evaluator | §8; `authority/evaluate.py`, `authority/properties.py` (1,000 histories, 0 failures; 8 mutations each caught) | ruled. The subset rule folded into A3 (A-13) |
| Q-8 delegation | §3.2; acme p7, p8; A3 | ruled |
| Q-9 acme, `what@4` | `how-examples/log/acme.json`, 25 records; `what/examples/acme-shop-4.ttl`, `what/vectors-4.json` | ruled. The re-founding is flagged (A-5) |
| Q-10 the violation-description field; attestations | §7; successor item P-3 | ruled |
| "Ids from 77" | superseded by R-14: 85 onward | R-14 |
| Seven commits, the PR when green | `e88eb6f`, `71d0fdf` (R-14), `e84d637`, `dbffc27`, `0933cd9`, `308c9a8`, `533ac8e`, `637ea7f`, and the commit of this table | done |

## R-14, 2026-11-02 — the ids move to 85 onward

Verbatim:

> Ruling R-14, 2026-11-02 (Emil): DDD-dec-77 to 82 and 84 are filed on
> claude/ready-to-try-2026-11-02 (PR #43); 83 is recorded as never used. Your provisional
> 77 and 78 move to 85 onward. Re-check every branch in both repositories before filing,
> and record this ruling and the renumbering in your bootstrap and plan.

### Where it landed

| Item | Landed | State |
|---|---|---|
| Re-check, 2026-11-02 | every branch of mindovermachine-dev/decision-driven-design: `claude/ready-to-try-2026-11-02` holds 74 to 82 and 84, and no other branch holds 74 or above. Every branch of `actor-indexed-determination`: up to 39 | done |
| 77 → 85, 78 → 86 | `core/decisions/DDD-dec-85.yaml`, `DDD-dec-86.yaml`, moved by `git mv` in their own commit. The first filing (`e88eb6f`, as 77 and 78) was never pushed. 85's notes record the move | done |
| The supersessions, planned as 79 to 83 | 87 to 91 (`plan.md`, Part 4, step 6) | as planned, renumbered |
| Bootstrap and plan | `bootstrap.md`, "Next free decision id"; `plan.md`, status note and Part 4 | done |

Round 1's verbatim "Ids from 77" is left as Emil wrote it; R-14 governs it.

## Round 2, 2026-11-02 — recorded in `DDD-dec-92`

Verbatim:

> Round 2, authority-profile session (2026-11-02).
>
> 1. A-5 — ruled: GEN@3 stands as the last re-founding. Same holder, same IRI, new key, recorded as a test-fixture re-founding and not as a transfer. It is acceptable only because item 2 ends the cause.
>
> 2. P-6 — ruled: keep the test keys for the fixture’s life. Commit them beside the fixture, marked as test keys of a declared test holder, never used outside the fixture, and rotated only by a new founding that the record states as such. A fixture that cannot be extended is not a fixture; a throwaway key per build was the wrong trade. This is the same model as Bailiff’s test holder.
>
> 3. The unruled readings — all ruled as proposed: A-6 any grant may have a fallback, and a fallback delegates from its primary; A-7 records in one header are judged in listed order; A-8 an act whose at differs from its header’s clock is refused; A-9 key loss is handled by a holder above, and for the genesis by transfer where a fallback exists, otherwise by the ruled new-product path; A-11 “touches” means every element the decision creates, changes or retires, per the scope wording; A-12 sdlc:Journey is the only derived kind; A-13 as written; A-14 refusals are header entries, not records, which matches Writ’s “written to the log with the agent as cause”; A-15 status carries no force.
>
> 4. The example’s verdicts as of the readings — accepted, with the note the checker prints. Re-evaluation at the log’s own clocks is a successor item that waits for an engine, not for this PR.
>
> R-14 — the renumbering is correct and correctly recorded.
>
> No watch on #45. It is for the record; I ratify by merging.

### Where each ruling landed

| Ruling | Landed | State |
|---|---|---|
| 1 A-5, `GEN@3` the last re-founding | authority.md §2.6 and A-5; `GEN@3`'s `why` says "test-fixture re-founding, not a transfer" | ruled. **The 25 records of 2026-11-02 were rebuilt once, before ratification.** Their keys had been discarded by the build that made them, so with no rebuild item 2 could not end the cause: `GEN@3`'s holder could never sign again. The records keep their ids, versions, statements, positions and clocks. Their keys, signatures and hashes change, and so do the pins in the log. This happened on the PR branch before any merge, and is recorded here and in the commit. No ratified record changed |
| 2 P-6, keep the test keys | `how-examples/test-keys/`, the seven private keys of the history with a README declaring them test keys of the declared test holders; `build.py` reads them and generates only missing ones; `log/acme-keys.json` and its refusal are removed | ruled. The stand-ins' keys (version 1 and 2 records, and the vendor's) were discarded earlier and cannot be recovered. The vendor's next act needs a founding ruling of its own (successor item P-9) |
| 3 A-6, A-7, A-12, A-13, A-14, A-15 | authority.md Appendix A: state "ruled, Round 2"; flags cleared in §2.4, §3.1, §4.2, §5.3, §6.1 and in `DDD-dec-87`, `-90` | ruled |
| 3 A-8, "an act whose at differs from its header's clock" | authority.md §6.2; `evaluate.py`: a date-only `at` must equal the clock's date, and an `at` with a time must equal the clock | ruled. Reading: "differs" is compared at the precision `at` carries, since `dpp/1` lets a record carry a date only (§3.4) |
| 3 A-9, key loss | authority.md §5.3 and A-9: a holder above, as ruled | ruled for every grant but the genesis. **Flagged, not applied:** "for the genesis by transfer where a fallback exists" meets two earlier rulings. A transfer is signed by the holder (`DDD-dec-46`), whose key is lost here, and a fallback "may act and may not transfer" (`DDD-dec-46`; `DDD-dec-85`). Who signs that transfer is not ruled, so the evaluator still refuses a fallback's transfer. Question Q-11 for Emil |
| 3 A-11, "touches" | authority.md §4.2 | ruled as proposed, with the scope wording quoted. Reading: a How decision creates one element, itself, of its kind's class at its anchor, so it "touches" that. Without this reading a How decision touches nothing, and no How acceptance could cover it |
| 4 the verdicts as of the readings | the checker's note, unchanged; successor item P-7 reworded to wait on an engine | ruled |
| R-14 | — | confirmed |
| No watch on #45 | no subscription | ruled |
