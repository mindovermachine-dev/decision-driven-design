# Prompt — canon's lock file, 2026-11-18

Verbatim, as given by Emil.

---

Work issue #83 in mindovermachine-dev/decision-driven-design:
"The agent review check builds again: canon's lock file and the SDK it is built with".

Read first: issue #83 in full, AGENTS.md, meta/way-of-working.md, then the files #83 names.

Set up before any other change
- Branch from main. Name it claude/canon-lock-file-<date>.
- Create meta/sessions/<date>-canon-lock-file/ with prompt.md (this prompt, verbatim) and
  bootstrap.md. Commit them first. Write predictions.md before each operation.

Work the deliverables in the issue's order
- Deliverable 1: reproduce NU1004 and confirm or correct the diagnosis in the issue. It is
  marked UNVERIFIED. Do not take it as ground.
- Deliverable 2: the proposals, weakest point first, each saying what happens at the next .NET
  patch release. STOP at G1. I rule which fix.
- Deliverable 3 only after my ruling. STOP at G2 with a pull request against main, and name the
  head to ratify.

Discipline
- This issue is the one place tools/canon may be changed. Change nothing that alters what
  canon checks.
- The agent review workflow runs from main (pull_request_target). A change to the workflow
  file is not exercised by the pull request that makes it. Say how the fix is shown to work
  before it lands.
- Every commit carries "Refs #83". Run the whole validate workflow locally before each push.
  After each push, report the workflow runs for that head, both required checks:
  "pipeline (devcontainer)" and "agent review".
- Do not touch the branches of #80, the archive branch, or any claim, card or lifecycle data.
- Record my rulings in rulings.md when I give them, in my words, with the time.

If the ground for a ruling is missing, ask me. Do not fill the gap.
