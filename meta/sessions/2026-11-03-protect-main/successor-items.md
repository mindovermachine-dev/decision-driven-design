# Successor items — protect main, 2026-11-03

What this session leaves open. Each row names who or what closes it.

| # | Item | Closes it |
|---|---|---|
| S-1 | **Land and apply.** Land the branch with `canon land`, then apply `.github/repo-standard.yaml` and run the three checks (`landing.md`) | **Emil** |
| S-2 | **The Signed Commits bypass list** (F-1): whether Integration 1236702 is this organisation's Claude app, and whether it, or the admin role entry, stays | **Emil**, by a ruling; a decision superseding nothing, adding to `DDD-dec-81` and `DDD-dec-108` |
| S-3 | **canon in a shallow clone.** `canon issue-refs --basis` reported `Basis on 0` and exited 0 when `basis.from` (`99d0a0f`) was not in the clone's history, so the Basis rule silently covered nothing. A checker that cannot see its start commit should say so (DESIGN.md §6.3's own lesson). CI is unaffected (`fetch-depth: 0`) | The canon CLI session (Gate 3) |
| S-4 | **Cite `DDD-dec-108`** in `tools/canon/DESIGN.md` §4.2, which says `DDD-dec-<pending>` (the canon CLI session's S-8) | The canon CLI session, once this lands |
| S-5 | **F-2 and F-3.** Whether sessions are excluded from `land/` and `v*` (check 3), and whether pull-request merges are turned off | **Emil** |

## After Round 2 (2026-11-03)

Add-only. The table above stands as written.

| # | Status | Closes it |
|---|---|---|
| S-1 | **Closed.** Landed (`458d05b`, then `320fccb`), applied, checks 1 and 2 held (`landing.md`) | Done by Emil |
| S-2 | **Ruled: "Remove it"** (`rulings.md`, Round 2). Integration 1236702 leaves the Signed Commits bypass list; the admin role stays the only bypass. Filed in this round | This round (`DDD-dec-110`) |
| S-5 | **Answered by evidence; check 3 not run.** Every push comes from Hafeok (the last 9 pushes, Emil's check), so a session's push to `land/` would be accepted. This confirms F-2. Agent review closes it (Round 2) | This round (`DDD-dec-109`) |

## Emil's admin acts for Round 2 (not attempted)

In this order. The order matters. The trunk ruleset as declared requires a check that nothing
can post until the App is installed and its key is in place. And once this branch lands, `canon
land` reads the pin from `main` and refuses any later head without that check.

| # | Act | Why here |
|---|---|---|
| R2-0 | **Confirm the gates App.** Is integration 5220446 (Varve's gates App) the App to use here, and can it be installed on the `mindovermachine-dev` organisation? A private App owned by a user account cannot be installed on an organisation. If it cannot, create one with **Checks: read and write** (Metadata: read is granted to every App), and its id replaces 5220446 in `.github/repo-standard.yaml` before anything is applied | The ruleset and `canon land` both trust this id and no other |
| R2-1 | **Land this branch** with `canon land`, as before. The applied `trunk` ruleset does not yet require `agent review`, so this landing needs no approval | The workflow must be on `main` before it can run (`pull_request_target` and `issue_comment` run `main`'s copy) |
| R2-2 | **Install the gates App** on this repository | It posts `agent review` |
| R2-3 | **Create the environment `gates`**, with deployment branches limited to `main` alone, and **add its secrets** `GATES_APP_CLIENT_ID` and `GATES_APP_PRIVATE_KEY` (the App's client id and a private key) | A session can push any branch with any workflow on it. The key must be reachable from `main` only (`DDD-dec-109`, notes) |
| R2-4 | **Re-apply `.github/repo-standard.yaml`** with `repo-standard` (`plan` first: expect `~ trunk`, with `agent review` added, and `~ Signed Commits`, with 1236702 removed) | Makes `agent review` required, and removes the bypass (`DDD-dec-110`) |
| R2-5 | **First approval.** On the next pull request, comment `approve <head sha>` by hand. Expect `agent review` green from the gates App on that head. Then `canon land` | Proves the chain end to end. A comment a session writes for Emil does not count, by design |

## Open after Round 2

| # | Item | Closes it |
|---|---|---|
| S-6 | **The admin bypass on Signed Commits may cover session pushes** (`DDD-dec-110`, notes). Sessions push as Hafeok, who holds the admin role. Removing that entry too, or having `canon land` refuse an unverified commit in the range, would close it | Emil, if wanted |
| S-7 | **`updated_at` and reactions** (`DDD-dec-109`, notes): whether anything but an edit moves a comment's `updated_at`. If something does, an approval goes stale and Emil comments again | Seen at R2-5, or later |
| S-8 | **The contributing session's branch** (`claude/optimistic-keller-trxr7y`, issue #54) rewrites CONTRIBUTING.md's landing section and GOVERNANCE.md's "Repository settings" paragraph. This branch adds the approve step to both files. Whichever lands second takes the approve step into its own text | That session, or this one, at the second landing |
| S-9 | **canon in a shallow clone** (S-3 above) is still open in the canon CLI session | The canon CLI session |

## After Round 3 (2026-11-03)

Add-only. The table above stands as written.

| # | Status | Closes it |
|---|---|---|
| R2-0 | **Done.** Gates App: "mom-gates", owned by `mindovermachine-dev`, integration id 5594102, with Checks: read and write and Pull requests: read (Round 3). Pinned in place of 5220446 | Done by Emil |
| R2-1 to R2-5 | **Open, unchanged**, with the App now named: R2-2 installs "mom-gates"; R2-3's secrets are its client id and a private key | **Emil** |
