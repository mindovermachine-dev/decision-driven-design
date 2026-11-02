# Rulings — the authority profile, 2026-11-02

Rulings given during the session, verbatim, recorded when given. `prompt.md` stays the arrival
charter, and this file carries what came after it.

## The charter's own rulings

The list under "Already ruled; do not reopen" in `prompt.md`, verbatim there. It is filed as
`DDD-dec-77`, as `DDD-dec-54` filed the How charter's list.

## Round 1, 2026-11-02 — the plan approved; recorded in `DDD-dec-78`

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

Filled in as the work lands (`plan.md`, Part 4).
