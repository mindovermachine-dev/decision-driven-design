# Rulings — protect main, 2026-11-03

Emil's rulings and corrections, verbatim, in the round they were given. Round 1 is the charter
(`prompt.md`).

## Round 2 — 2026-11-03

Given in the session after the first landing, verbatim:

> Round 2, 2026-11-03. Refs #51 on every commit.
>
> 0. Corrections, add-only, in this round's first commit:
>    - A-2 and A-3 are the ready-to-try session's admin acts (its successor-items.md): A-2
>      "Turn on Discussions", A-3 "Apply .github/repo-standard.yaml". Both are done as of
>      2026-11-03. The probe is a check, not an admin act. Replace the UNVERIFIED reading.
>    - S-2 is ruled ("Remove it"), as below.
>    - S-5: check 3 is not run. Every push comes from Hafeok (the last 9 pushes), so a
>      session's push to land/ would be accepted. The evidence answers it; agent review
>      closes it.
>    - Record that Emil landed 320fccb with canon land. It was the first landing the trunk
>      ruleset checked.
>
> Emil's rulings, verbatim (claude.ai question dialog), after an independent check of 458d05b
> (6 commits verified, CI green, the four rulesets as ruled; the repository's last 9 pushes
> all come from Hafeok, sessions included):
>
> Q: "Sessions push as your account, so the rulesets cannot tell you from a session. How
> should this repository make ratification yours alone?"
> A: "Varve's agent review (Recommended)" (option text: "Install Varve's gates App here.
> Required check `agent review` on trunk, green only on your `approve <sha>` comment;
> `canon land` refuses without it")
>
> Q: "Signed Commits keeps an Integration bypass (1236702, copied from Varve). Every recent
> commit is verified and every push comes from your account, so it appears unused. Remove
> it?"
> A: "Remove it (Recommended)" (option text: "Admin role stays the only bypass; a session
> commit that fails to sign is refused")
>
> On a new branch from main:
>
> 1. Record Round 2 verbatim in rulings.md.
> 2. Re-check decision ids on every branch of both repositories. The canon session is also
>    filing (its S-20 decision), so take the next id above the highest held anywhere, and
>    report it.
> 3. File two decisions: one for agent review, one for removing the bypass. Neither
>    supersedes DDD-dec-108; both add to it.
> 4. Read Varve's mechanism before designing anything: eng/agent-review.cs,
>    eng/agent-review-tamper.cs, eng/identities.json, ADR 0087 and its amendments, and the
>    workflow that posts the agent review check. Then port it:
>    - identities: the eng/identities.json equivalent names Emil as the responsible human.
>      A session is identified by its Claude-Session trailer, not by the pushing account.
>    - `canon agent-review`: green only when the pull request's head carries a comment
>      `approve <head sha>` from a listed identity. That covers a pull request, or the pull
>      request behind a land/ push.
>    - the workflow that runs it and posts the check as the gates App.
>    - the trunk ruleset in .github/repo-standard.yaml: add the context `agent review` with
>      the gates App's integration_id. Varve's file has 5220446; ask Emil to confirm it is
>      the same App before relying on it.
>    - `canon land`: refuse when agent review is not green on the head.
> 5. Remove the Integration 1236702 bypass from the Signed Commits ruleset in
>    .github/repo-standard.yaml. Update GOVERNANCE.md's Departure 3 to match.
> 6. Update CONTRIBUTING.md and GOVERNANCE.md's landing steps with the approve step: Emil's
>    `approve <head sha>` comment on the pull request comes before `canon land`.
> 7. Write Detroit-style tests. Include tamper cases:
>    - a session-authored comment must not satisfy the check;
>    - a check posted by anything but the gates App must not satisfy the ruleset;
>    - an approval of an older head must not count.
> 8. List Emil's admin acts, and do not attempt them:
>    - install the gates App on this repository
>    - add its secret(s)
>    - re-apply .github/repo-standard.yaml with repo-standard
> 9. Predict before each operation. Push, wait for green CI, report the head and the canon
>    land commands, and stop. Do not land.

**Before the round arrived in full**, item 0 reached the session alone. Claude recorded it in a
commit (`3343745`) that said the rest of the round had not arrived. That commit was pushed to
this branch, never landed, and is replaced by this one, made on the branch restarted from `main`
at `320fccb`, as item 9's "a new branch from main" asks. Between them, Emil confirmed the landing:

> Landed 320fccb with --main;

| Item | Where it lands |
|---|---|
| 0 | `landing.md` ("Correction — Round 2", "The second landing"), `predictions.md`, `successor-items.md` ("After Round 2") |
| Agent review | `DDD-dec-109`; `tools/canon/`, the workflow, `.github/identities.json`, `.github/repo-standard.yaml` |
| Remove the bypass | `DDD-dec-110`; `.github/repo-standard.yaml`; `GOVERNANCE.md` Departure 3 |
| 6 | `GOVERNANCE.md`, `CONTRIBUTING.md` |
| 8 | `successor-items.md`, "Emil's admin acts" |

## Round 3 — 2026-11-03

Given in the session after the head `c4f9f9b`, verbatim:

> Round 3, 2026-11-03. Emil's rulings, verbatim (claude.ai question dialog), after an
> independent check of c4f9f9b (11 commits verified, CI green; of 7 PR comments in the
> repository, the 5 by sessions carry performed_via_github_app 1236702, Emil's 2 carry none):
>
> Q: "If the gates App (5220446) can't be installed on mindovermachine-dev, which way?"
> A: "New org-owned App (Recommended)" (option text: "Create a 'gates' App owned by
> mindovermachine-dev (Checks: read & write, Pull requests: read). The session swaps the id
> before you land")
>
> Q: "DDD-dec-109 goes beyond Varve in four flagged ways. Accept them? (1) every PR needs your
> approval, not only ones with session commits; (2) an edited approval comment doesn't count;
> (3) no land/** push trigger for the check; (4) the gates environment is not declared in
> repo-standard.yaml."
> A: "Accept all four (Recommended)" (option text: "Each follows from sessions and you
> sharing one account")
>
> Result of Emil's check: the gates App id is 5594102  (new
> org-owned App "mom-gates">).
>
> 1. Record Round 3 verbatim. Record the four confirmations as an add-only note in
>    DDD-dec-109; do not edit its body.
> 2. If the id changed, replace 5220446 everywhere it is pinned:
>    - repo-standard.yaml's trunk ruleset
>    - canon's pin read
>    - the workflow
>    - the tests
>    - GOVERNANCE.md
>    Record why it changed.
> 3. Merge main if it moved. Run the gates, push, wait for green, report the head and the
>    land commands. Refs #51. Do not land.

| Item | Where it lands |
|---|---|
| The four confirmations | `DDD-dec-109`, notes, an add-only "Round 3" paragraph |
| The id, 5220446 → 5594102 | `.github/repo-standard.yaml`, the tests, `GOVERNANCE.md`'s table, the workflow's header comment; why, in `findings.md` F-5 |
| `main` merged | `0846ae7` |
