# Findings — map the flow of demand, 2026-11-08

What the session found while doing the work, in the order found. Corrections are attributed.

**F-a. Canon has a term `demand`.** `term:demand` ("determination demand") is settled upstream,
established by `core/01`. That ruled out `demand` as the claim area (`bootstrap.md`), and it
constrains the step's wording: the step is about demand *items* arriving and being ordered, which
canon's term does not name. The card says "demand item" throughout. Whether canon's term and the
PDLC's "kinds of demand" need an explicit bridge is part of promotion item P-1.

**F-b. Owed demand is escape, and undelivered is a case of it.** Round 23's table listed "an
escape, or a judgment-mediated delivery that did not arrive". Upstream `DDD-delivery-02` holds that
filed-but-undelivered governance is escape and widens nothing. `DDD-flow-01` says "including the
undelivered case of core/13". Recorded in its `notes:` per rulings.md R-b.

**F-c. "Liability without control" is Round 23's phrase; core/05 §5's is "answerable and liable
with no control".** `DDD-flow-02`'s notes use canon's words. In the PDLC the party in that position
under a single orderer is the How owner: it answers for the DORA keys, and the When owner would
order the work that moves them.

**F-d. Owed demand enters away from where it is detected (`DDD-flow-03`).** Detected on the How
owner's telemetry and users' reports, entered at the What owner's oC. Flagged in the claim, printed
by `check.py`, open as R-1. **Closed by Round 26** (see F-k).

**F-e. pdlc.md §9 says owed demand "is judged on the What in force"; the How owner orders it.** Read
as two decisions placed with two owners (`DDD-flow-04`): the classification at oC is judged on the
What in force by the What owner; the ordering is judged on time to restore by the How owner, who
reads the verdict across the seam. Open as R-2. Read literally, §9 would make the How owner an
orderer without its kind's ground, which is `DDD-flow-02`'s violation.

**F-f. `DDD-dec-74`'s front door lists every step.** `README.md`'s "Status, step by step" table is
the front door that decision governs ("states every method step at the register it is filed at").
The prompt named only `method/README.md`'s table (item 8); the 1b row was added to both, so the
front door does not omit a filed step. Flagged as a step beyond the prompt's letter.

**F-g. The field-report template is the vehicle for the starting point's declarations.** Round 25's
keep, add or drop declarations are evidence for P-1. The card asks for them as a field report
citing `DDD-dec-118`, the existing route for "you ran a method step on a real system".

**F-h. The PDLC checker is not a CI gate** (C-1). Pre-existing. The flow checks run by hand, as
the act map's always have.

**F-i. A false reading, corrected (Claude).** At arrival Claude noted `meta/sessions/README.md`'s
index as repeating nine rows. It does not: two printouts of the file overlapped. The note was
removed from `bootstrap.md` before the first commit.

**F-j. `DDD-dec-118` adds to `DDD-dec-114` and supersedes nothing, but Round 24 superseded a
ruling.** Round 23's second answer ("Upstream, as projected") was superseded inside the
conversation and was never a filed decision, so there is nothing to name in a `supersedes` field.
rulings.md's table records it.

**F-k. Round 26 closes R-1, and moves one entry (2026-11-10).** With entry defined as the act that
assigns the kind, "a reported defect that is the What being wrong" enters at oC, not o0: its kind,
new, is assigned by the What owner's classification, and it becomes an option at o0 afterwards. New
demand therefore has two entry acts, o0 and oC. The graph data says so (`lc:NewDemand lc:entersAt
m:o0 , m:oC`), the card's kinds and sources tables say so, and `DDD-flow-01`'s `breaks` was brought
into line (a phrase, beyond the round's letter; flagged here). The check.py note that flagged
"entry outside detection" flagged exactly the oC case; under the ruled wording that entry is correct
by construction, because the defect reaches oC along the How → What telemetry seam. The note is now
a reading that names the seam, and the failure it guarded is a SHACL refusal with planted defects
(no seam; a seam not read at the entry act; a seam whose producing act the supplier does not hold).

**F-l. pdlc.md keeps "detects".** Its two uses (§9's "Detected by" column, §10's "the new demand it
detects") mean first sighting, not entry, so Round 26's instruction to change entry-sense uses does
not reach them. Unchanged.
