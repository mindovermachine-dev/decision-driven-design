# Prompt — applications/ for readers, redone, 2026-11-09

The session prompt, verbatim. Per `DDD-dec-20`, this file is committed before any other file
changes, so the session's scope is fixed at arrival.

---

New session: applications/ for readers, redone, 2026-11-09, in mindovermachine-dev/decision-driven-design. It succeeds PR #48 (closed, not merged). Start only once PR #64 (the PDLC and the SDLC) has landed; branch from main and report its head. If #64 has not landed, stop and say so. Open an issue; Refs #N on every commit. Commit prompt.md and bootstrap.md under meta/sessions/2026-11-09-applications-for-readers-redo/ first.
Emil's rulings, verbatim
Claude's question dialog on claude.ai, 2026-11-09. They are also recorded on PR #48 (issuecomment-6736005356):
Q: "What should happen to PR #48 (applications/ for readers, DDD-dec-94/95), now 92 commits behind and colliding with #64?" A: "Close; successor redoes it (Recommended)" (option text: "Land #64 first. Close #48, branch kept as record. A new session lands DDD-dec-94 + spec/doc-format.md, then redoes the rewrite (DDD-dec-95) on current applications/, pdlc/ and sdlc.md, reusing #48's report and check")
Q: "#48 asked whether to keep the reader format given its reader test could not show it helps. Your ruling?" A: "Keep it, human test decides" (option text: "Apply the format; a human first-contact test (successor A-4) decides later")
The second answers #48's ruling request 1. Its requests 2 to 4 are still open: whether merging PR #41 settled the How's unruled parts (DDD-dec-58, -59); the named-algorithm heading against DDD-dec-64 P-5; and the six content gaps every reader found, starting with the example scenario that contradicts the wire rule.
Sources to read before writing anything

* The #48 branch, claude/applications-for-readers-2026-11-02 at 068cb23, as the record: its session folder meta/sessions/2026-11-02-applications-for-readers/ (prompt, rulings, report.md, independent-check.md, the reader test and its pre-registration), core/decisions/DDD-dec-94.yaml and -95.yaml, spec/doc-format.md.
* main as landed: applications/ in full, including applications/pdlc/ and applications/sdlc/sdlc.md from #64; DDD-dec-113 (sdlc edition 1), -114, -115; the 2026-10-26 doc-format rulings DDD-dec-94 re-files; graph/upstream.yaml.

The work
Predict before each operation. Stop at every gate.

1. Record the rulings above verbatim in rulings.md.
2. Check that DDD-dec-94 and -95 are still held only by the #48 branch. Re-check every branch for any other use. Report it if either is held elsewhere.
3. Gate A, the format. File DDD-dec-94 on main from the #48 branch's file, with its content unchanged except: its date, its re-filing note naming this session and #48, and anything main has since made wrong (say what and why). Port spec/doc-format.md the same way. Commit, run the validators, and stop for Emil.
4. Put #48's open ruling requests 2 to 4 to Emil, each with what #48 found and what main says now. Record his answers verbatim before writing anything they affect.
5. Gate B, the rewrite. Redo DDD-dec-95's rewrite against applications/ as it now stands, in the format of spec/doc-format.md. Cover every document, including applications/pdlc/ and applications/sdlc/sdlc.md. Use #48's work as input, not as text to paste: its what.md / what-reference.md and how.md / how-reference.md split, and the 64 differences its independent check found, as a list of traps. Keep every section anchor that other documents cite (pdlc.md cites what.md §3.0 to §4.2): either keep the numbering, or update every citation in the same commit and list them. Nothing proposed may read as decided, and nothing decided may be weakened; that was #48's main failure class. Include the release session's F-2: applications/README.md still calls sdlc.md [PROPOSED], while sdlc.md and DDD-dec-115 say its proposals were ruled in Round 28 of the 2026-11-07 record. Read that round first and state each document's register as the decisions give it.
6. File DDD-dec-95 for the rewrite, adapted to what it now covers. Say what differs from the #48 version and why.
7. Independent equivalence check. Brief a separate agent that has not seen the rewrite being made. Give it the old and new text, not your conclusions, and have it report differences in meaning, register (ruled / [PROPOSED] / [OPEN]) and falsifiers. Fix each difference or record why not.
8. The human first-contact test (Emil's ruling: "human test decides"). Do not run it with model readers as a substitute. Write its pre-registration as successor A-4: who the readers are, what they are given, what counts as the format helping and as it failing, and what happens in each case. Add it to successor-items.md for Emil to schedule.
9. Run the validators. Push, wait for green CI, report the head and the land commands, and stop. Do not land.
