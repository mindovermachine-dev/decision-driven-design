# Pre-registration — A-4, the human first-contact test

Successor item A-4. It is the test that decides whether the reader format stays (Emil, 2026-11-09:
"Keep it, human test decides"; option text: "Apply the format; a human first-contact test
(successor A-4) decides later"). This file was written and committed **before any Gate B rewrite
was committed**. Whoever runs the test records this file's SHA-256 when they start it, and checks
it again in the report. The file is not edited after the test is scheduled. A change is a new
pre-registration that names this one.

**Not run in this session.** Emil's ruling asks for a human test. Model readers are not a
substitute, and none is used. #48's model-reader test (four agents, 8 of 8 each) hit a ceiling and
could not discriminate. A model reads a long record as easily as a short guide. The format exists
for people.

## What is tested

Whether people new to the method use `applications/` better in the reader format than in the
record format it replaced. The two versions carry the same rules, and only the presentation
differs.

- **Old:** the documents at `84aa466` (`main` before this session).
- **New:** the same documents at the head Emil lands from this session, which `report.md` names.
- **In use:** `applications/sdlc/what.md`, `applications/sdlc/how.md`, `applications/sdlc/sdlc.md`
  and `applications/pdlc/pdlc.md`, rendered as HTML (GitHub's rendering is fine), with
  `applications/sdlc/what/examples/acme-shop.ttl`. Both groups get the same four documents in the
  same rendering, and nothing else from the repository.

## The readers

- **Six people at least, eight if possible**, split evenly between old and new at random (a coin
  or a shuffled list, recorded).
- **Who:** practitioners of the roles the documents name as readers: developers, architects and
  product owners. At least one of each role in each group, where the numbers allow.
- **Excluded:** Emil; anyone who has read any version of `applications/`, PR #48, or this
  session; anyone who has worked on the method or its repositories.
- **Recorded for each reader, not used to score:** role, years of practice, and whether they have
  used event modelling or decision records before.
- **Consent:** each reader knows the answers are kept, without their name, in the session record.

## What each reader is given

The four documents and the `.ttl` file, the three tasks below in writing, and **45 minutes in
all**, timed. No help from the person running the test beyond the written instructions. The time
limit is part of the design. #48's readers had unlimited time, and a careful reader with
unlimited time can find anything in either version.

### Task 1 — change the What (25 minutes)

> You are joining the team that owns Acme Shop, a small web shop. Its specification of what the
> software is and does (its "What") is described in the documents, and its full What is the file
> `acme-shop.ttl`.
>
> Acme Shop wants staff to be able to add a free-text note to an existing order. Customers must
> not see the note.
>
> 1. List what you would add to or change in the What, and where each belongs.
> 2. Say how each addition gets into the What: what is written, what it is attached to, and why
>    there.
> 3. Say who must sign or approve it, and what they must hold to be allowed to.
> 4. Say when the change is in force.
> 5. List anything in the documents you did not understand or were unsure about.
>
> Answer from the documents only. Say where you are guessing.

The task avoids the six known content gaps (successor items A-8 to A-12 and A-16). It changes an
existing paid order, adds a field to an existing entity, and creates no new owner in the same
change, so a reader can answer it fully from either version.

### Task 2 — how settled is it? (10 minutes)

> For each statement, say whether the documents present it as **decided**, **proposed but not
> yet decided**, **open (no proposal yet)**, or **an interpretation the author has not had
> confirmed**. Give the place you found it.

| # | Statement | Key (the same in both versions) |
|---|---|---|
| T1 | A What may use named-algorithm primitives | decided (`what.md` §3.5) |
| T2 | An adopter may register new abstract interaction objects (AIOs) | open (`what.md` §3.2.2; `how.md` §6) |
| T3 | The baseline's ratchet semantics, as used for coverage debt | an unconfirmed interpretation (`how.md` §8.2) |
| T4 | Method step 7, which the PDLC's accountability is mapped to | proposed (`pdlc.md`, its mapping to step 7) |
| T5 | An approval of a candidate is given by hand by a holder of Approve for the issue's locus | decided (`sdlc.md`, o10) |
| T6 | Whether adopters may register What kinds | open (`how.md` §10) |

Before the test runs, the person running it re-checks each key against both versions. If any
key differs between them, that item is dropped and the drop is reported. Items whose register
`DDD-dec-119` changed were left out on purpose.

### Task 3 — find it (10 minutes)

> Answer each in one sentence, and give where you found it.
> (a) In the SDLC, what must hold before `main` is moved to a candidate?
> (b) In the PDLC, who orders new demand, and who orders owed work?
> (c) In the What, what is a Decider for?

## Scoring

**Scored blind.** A third party removes names and version clues (file names, the `ddd:doc`
block's presence) from the answers and labels them A to H. The scorer is a person who knows the
method (Emil, or someone he names), and does not know which label read which version. A fresh
model agent may score the same blinded answers as a second rater. Its scores are reported only to
show agreement, never used in place of the human's.

**Task 1, eight criteria, one point each.** K3, K5, K6 and K8 are the hard ones. The old text
puts their answers in a decision-cited passage, an appendix or a numbered reference section.

| # | Criterion | Hard |
|---|---|---|
| K1 | Adds a field (the note) to the `Order` entity, and a command, or a payload field on one, by which staff add it | |
| K2 | Says the field is not in the customer's view: the `Order summary` view's scope or fields keep it from customers | |
| K3 | Anchors each decision to the narrowest existing element that covers what it creates or changes (`Order` for its new field), not to the new element | **yes** |
| K4 | Says the What is not edited in place: every change is a decision, and a tool only proposes | |
| K5 | Says the signer must hold a grant (an authoring scope) covering these element kinds, delegated from the product's founding (genesis) grant | **yes** |
| K6 | Says nothing is in force until a human holder accepts it, and a new What-version then names the What in force | **yes** |
| K7 | Says the new elements get new identities, and `Order` keeps its own | |
| K8 | Says who may issue the command (staff only), using the What's subject kinds and their rules | **yes** |

**Task 2:** one point per correct register, out of six (fewer if items are dropped). **Task 3:**
one point per correct answer with a correct location, out of three. **Time:** each reader's
minutes for Task 1 are recorded, and a reader who does not finish within time scores what they
wrote.

## What counts as the format helping, and as it failing

Fixed before any reader is recruited. With six to eight readers this is a coarse test. The rules
say what result moves the decision, not what is statistically significant.

**The format helps** if all three hold:

1. On the hard criteria (K3, K5, K6, K8), the new group's mean is at least **1 point above** the
   old group's mean (out of 4).
2. On Task 2, the new group's mean is **not below** the old group's. Ruling 2 put the register
   into words, and this checks that the words did not lose it.
3. **No more than one** new-text reader lists a format device as something they did not
   understand. The devices are the plain-words register phrases, the "Not settled yet" section,
   the "Where this comes from" table, and the opening "How settled this is".

**The format fails** if either holds:

1. On the hard criteria, the new group's mean is **at or below** the old group's mean, **and** on
   Task 2 it is at or below the old group's too.
2. **Two or more** new-text readers name the **same** format device as confusing.

**Otherwise the result is inconclusive.**

**Reported in every case, but not part of the rule:** the means on all eight criteria and on
Task 3; time used; any old-text reader who names ids, section numbers or register tags as
confusing; and content confusions common to both groups, which go to the successor items, not to
the format.

## What happens in each case

- **Helps:** the format stays as ruled (`DDD-dec-94`, `DDD-dec-95`). A-2 (`apparatus/`) may go
  ahead, with an independent equivalence check before anything else.
- **Fails, limb 1:** the format has not shown it helps people either. Emil chooses between
  (a) restoring the record presentation, where each document's `supersedes` pointer makes that one
  revert per document, and (b) #48's named fallback: ids stay out of the prose, with invisible
  point-of-use markers in place of the closing table. A-2 waits for that ruling.
- **Fails, limb 2:** the named device is changed or removed in `applications/` before any of it
  reaches `apparatus/`, and that device alone is tested again.
- **Inconclusive:** the format stays, since Emil's ruling keeps it until a test decides. He rules
  whether to run again with more readers or to accept the format as it stands.

The result, the blinded answers and the scores go in a session record. The decision that acts
on it cites this file and its SHA-256.
