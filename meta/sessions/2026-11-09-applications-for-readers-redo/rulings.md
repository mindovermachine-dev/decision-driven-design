# Rulings — applications/ for readers, redone

Recorded verbatim, when given.

## Round 1 — before the session, on PR #48 (2026-11-09)

Given in Claude's question dialog on claude.ai on 2026-11-09. They are also recorded on PR #48
(issuecomment-6736005356) and in this session's `prompt.md`.

> Q: "What should happen to PR #48 (applications/ for readers, DDD-dec-94/95), now 92 commits behind and colliding with #64?" A: "Close; successor redoes it (Recommended)" (option text: "Land #64 first. Close #48, branch kept as record. A new session lands DDD-dec-94 + spec/doc-format.md, then redoes the rewrite (DDD-dec-95) on current applications/, pdlc/ and sdlc.md, reusing #48's report and check")

> Q: "#48 asked whether to keep the reader format given its reader test could not show it helps. Your ruling?" A: "Keep it, human test decides" (option text: "Apply the format; a human first-contact test (successor A-4) decides later")

The second answers #48's ruling request 1, which was option (a) of `report.md` §"Rulings
requested". Requests 2 to 4 are still open and go to Emil in Round 2.

## Round 2 — at Gate A (2026-11-10)

Claude's question dialog in this session, after Gate A was pushed at `1378851`. Questions as put,
answers as given, with the chosen option's text.

> Q (Gate A): "Gate A is pushed (claude/zealous-ptolemy-3txf8k, head 1378851, all CI gates green). DDD-dec-94 and spec/doc-format.md are #48's text, changed only where main made them wrong: the made line cited #48's record and PR as if on main. One application question before Gate B (findings F-5): the spec marks every unsettled point *(not settled yet)*, but applications/ distinguishes [PROPOSED] (proposal awaiting a ruling) from [OPEN] (no proposal). How should the rewrite say registers?" A: "Accept; two phrases (Recommended)" (option text: "Gate A accepted. In prose: *(proposed, not yet ruled)* for [PROPOSED] and *(open)* for [OPEN]; the closing table keeps the bracket markers. No change to DDD-dec-94")

> Q (#48 request 2): "#48 ruling request 2: did merging PR #41 settle the How's unruled parts? how.md on main (untouched since) still says 'What was not ruled separately stays [PROPOSED] until the merge', and #41 merged (1d0f40c). DDD-dec-58 states coverage (debt/boundary/waiver) word for word; DDD-dec-59 states withdrawal and the three parts of an import (landing, import decision, acceptance) word for word, yet how.md §5/§7 mark those [PROPOSED]. Appendix A attributes H-3, H-8, H-9, H-11, H-12, H-13, H-17 to decisions -55/-57/-59/-60 while calling them 'not ruled separately'. Which are settled?" A: "The merge ratified them all" (option text: "Every 'not ruled separately' item became ruled when #41 merged; the rewrite drops their [PROPOSED] marks")

> Q (#48 request 3): "#48 ruling request 3: DDD-dec-64 P-5 ruled what.md §3.5's title as 'Named-algorithm primitives', no subtitle ('floor' is canon's). main still has that title. #48's rewrite changed it to 'Named algorithms — computation you name instead of deriving'. Which title should the redo use?" A: "Keep the ruled title (Recommended)" (option text: "'Named-algorithm primitives', no subtitle; a plain-words gloss may go in the first sentence of the section, not the heading")

> Q (#48 request 4): "#48 ruling request 4: six content gaps every reader found, all still true on main: (1) no unpaid order; (2) the example scenario puts the customer_id claim inside the command's `with`, against what.md §6 'supplied beside the command, never inside its with' — in acme-shop.ttl, -4 and -5, all hashed, so a fix needs a new What-version; (3) anchoring a decision that both creates and changes; (4) subject coverage's range; (5) whether a field's creation rides with its owner's; (6) no command carries an order id. How should this session treat them?" A: "Successor items; A-8 first (Recommended)" (option text: "Not fixed or marked in the rewrite (presentation only). Kept as A-8 to A-12 plus (1); A-8, the wire-rule contradiction, scheduled first in its own session with a new What-version")

### Claude's reading — UNVERIFIED, Emil review

- **Request 2 reaches the items `how.md` itself lists as "not ruled separately"**: the §10 list
  (the three kinds, no fourth and no split, the idle report, the record types; shapes derived from
  editions, standards not targets; the recorded-reading condition and narrow-never-alter; Kind-1
  wiring as contracts and `deployment-declared` facts gating `land`), Appendix A's H-3, H-8, H-9,
  H-11, H-12, H-13 and H-17, and the passages marked `[PROPOSED]` with "not ruled separately" or
  "the proposal kept". It does **not** reach §10's item 2, which is `[OPEN]` (whether adopters may
  register What kinds), and it does not reach material in other documents. The ruling is a change
  of register, so it is filed as a decision of its own (`DDD-dec-119`) rather than carried only
  inside the format decision.
- **Request 4, item (1)** (no unpaid order) has no #48 number, and is added as A-16.

## Round 3 — after the stop, on PR #73 (2026-11-11)

Emil's message, verbatim:

> PR #73 is open on your branch at 86d9042. Record this message verbatim in rulings.md as Round 3, and predict before each operation. These are my answers in Claude's question dialog on claude.ai:
> Q: "DDD-dec-119's reach: does "the merge ratified them all" also cover how.md §5.2's term list and §11's conformance level (covered only by the document's banner)?" A: "Yes, it covers them (Recommended)" (option text: "The banner made them 'not ruled separately' items, which the ruling names; §10 item 2 stays [OPEN]")
> Q: "F-13: accept dropping the UNVERIFIED mark on how.md §2's anchor row, since DDD-dec-55's statement contains that reading?" A: "Accept (Recommended)" (option text: "DDD-dec-55 states the narrowest-element anchoring and the product-node reading")
> Q: "F-10: pdlc.md §2.1's seam rows 1–8 are not ruled (DDD-dec-114 P-3). What now?" A: "Rule rows 1–8 now" (option text: "They are checked against the act map by check.py; rule them as listed, and the register line becomes true")
>
> 1. DDD-dec-119: its reading of the reach is now ruled. Remove its UNVERIFIED mark, and cite this round.
> 2. F-13: closed as you did it. Cite this round.
> 3. F-10: pdlc.md §2.1's seam rows 1 to 8 are ruled as listed. Row 9, telemetry, was already ruled in Round 16 of the 2026-11-07 record. DDD-dec-114 is landed, so do not edit it. File a new decision that supersedes only P-3's sentence "It is not ruled here", and records rows 1 to 8 as ruled, row by row, as they stand in pdlc.md §2.1 at your head. Then make pdlc.md's register line and the rows' markers match. Ids: the plugin session (prompt-4) runs in parallel and may file a decision too. Re-check every branch for ids just before you commit and again just before you push. Take the next free id, and report it.
> 4. Run scripts/ci.py, applications/pdlc/check.py and canon's checks as CI runs them. Push, wait for green CI, and report the new head for my approval on #73. Stop. Do not land.
