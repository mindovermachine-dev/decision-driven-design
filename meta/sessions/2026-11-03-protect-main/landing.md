# Landing and applying — protect main, 2026-11-03

The session stops at a green head. Everything below is Emil's to run, in this order. The head is
the branch's head at the end of the session. It is named in the closing report on issue #51 and
is `land/protect-main` once step 1 has run.

## 1. Land (`DDD-dec-101`, `DDD-dec-108`)

There is no pull request, so the commit form is used. `<head>` is the exact SHA reported on issue
#51, not the branch name, so `main` moves only to the commit that was reviewed:

```bash
canon land --commit <head> --name protect-main
```

Wait for `pipeline (devcontainer)` to go green on `land/protect-main`, then:

```bash
canon land --commit <head> --name protect-main --main
```

The branch is a fast-forward of `main` at `5ccdf41`. If `main` has moved, canon refuses, and the
branch is merged or rebased first. From a checkout without canon installed,
`dotnet run --project tools/canon/src/Canon --` replaces `canon`.

## 2. Apply (repository admin)

With Varve's `repo-standard` built from `Hafeok/varve` (`tools/repo-standard/README.md`,
"Building it"), and a token with Administration read and write on this repository in
`GITHUB_TOKEN`. Plan first:

```bash
repo-standard plan --repo mindovermachine-dev/decision-driven-design --file .github/repo-standard.yaml
```

The plan is expected to show four rulesets created (`+`). It is also expected to show the
description, the topics and Discussions changed (`~`), as `DDD-dec-81` intends. Then:

```bash
repo-standard apply --repo mindovermachine-dev/decision-driven-design --file .github/repo-standard.yaml
```

The file manages `repository:` too, so apply also changes the description and topics and turns
Discussions on. To apply the rulesets alone, apply a copy of the file without `repository:`
(a kind that is left out is not managed).

## 3. Checks after applying

**Check 1: the rules in force on `main`.** Read only.

```bash
gh api repos/mindovermachine-dev/decision-driven-design/rules/branches/main --jq '.[].type' | sort
```

Expected: `deletion`, `non_fast_forward`, `required_signatures`, `required_status_checks`.

**Check 2: a direct push to `main` is refused.** From a clean clone of `main`, as Emil (admin,
so this also tests that `trunk` has no bypass):

```bash
git commit --allow-empty -S -m "Probe: a direct push to main must be refused (DDD-dec-108)"
```

```bash
git push origin HEAD:main
```

Expected: refused, `GH013: Repository rule violations found for refs/heads/main`, naming the
required status check `pipeline (devcontainer)`. The probe commit is local and is discarded with
`git reset --hard origin/main`. If the push is **accepted**, the ruleset is not in force. `main`
then carries one empty probe commit, which is harmless and records the failure. Report it on
issue #51.

**Check 3: whether `land/` excludes a cloud session (F-2).** From a cloud session, not Emil's own
machine:

```bash
git push origin HEAD:refs/heads/land/probe-session
```

If it is refused, `land/` is Emil's alone. If it is accepted, the session's push counts as Emil's
for the bypass (F-2). Delete it afterwards as Emil:

```bash
git push origin --delete land/probe-session
```

## Outcome — 2026-11-03

Add-only. Nothing above this heading is edited. Emil's report, in the session:

> Emil landed 458d05b with canon land (main at 458d05b, land/protect-main deleted), applied
> repo-standard.yaml (description, topics, Discussions, then the four rulesets: trunk, land,
> Release Tags, Signed Commits), and ran the probe as himself: a signed empty commit d270e4b
> pushed directly to main was refused with GH013, "Required status check "pipeline
> (devcontainer)" is expected." So the trunk ruleset is in force and has no bypass, even for the
> admin. A-2 and A-3 are done.

Verified against the live repository at 08:47 UTC, read only:

- **Step 1, landed.** `origin/main` is `458d05bbed9b`. No `refs/heads/land/*` exists.
- **Step 2, applied.** `GET /rulesets` lists four rulesets, all `active`: `trunk` (26435014),
  `land` (26435017), `Release Tags` (26435021, target `tag`) and `Signed Commits` (26434567). The
  description and the five topics match the file, and Discussions is on.
- **Check 1.** `GET /rules/branches/main` gives `deletion`, `non_fast_forward`,
  `required_signatures`, `required_status_checks`, as predicted.
- **Check 2.** The probe `d270e4b` is a signed commit (`verified`, `valid`), authored by
  `Hafeok`, whose parent is `458d05b`. Its message is the one given in check 2. It is not on
  `main`. GitHub holds the object from the refused push. The refusal's text is Emil's report and
  was not re-read here.
- **Check 3** (F-2: whether `land/` excludes a cloud session) has not been run. It stays open as
  S-5.

`UNVERIFIED — Emil review`: "A-2 and A-3" are not ids in this session's record. They are read as
the two acts of this file after the landing: A-2 is step 2 (apply) and A-3 is check 2 (the
direct-push probe).

## Correction — Round 2, 2026-11-03

Add-only. The reading flagged `UNVERIFIED` at the end of "Outcome" above is wrong, and this
replaces it (`rulings.md`, Round 2, item 0). A-2 and A-3 are the ready-to-try session's admin acts
(`meta/sessions/2026-11-02-ready-to-try/successor-items.md`): A-2 "Turn on Discussions" and A-3
"Apply `.github/repo-standard.yaml`". Both are done as of 2026-11-03. The probe (check 2) is a
check, not an admin act.

## The second landing — `320fccb`, 2026-11-03

Emil landed `320fccb`, the "Outcome" record, with `canon land` (`--name protect-main-record`,
then `--main`). Verified live at 09:06 UTC: `main` is at `320fccb9dc90`, and no `land/` branch
exists. Before `--main`, `land/protect-main-record` was at `320fccb`, carrying two
`pipeline (devcontainer)` check runs on that SHA, both `success` and both from app 15368: one
from the push of the session branch, one from the `land/` push.

**It was the first landing the `trunk` ruleset checked.** `458d05b` landed before the rulesets
were applied. `320fccb` landed after, by a fast-forward of `main` to a commit with a successful
`pipeline (devcontainer)` check from GitHub Actions. So `canon land --main` passes `trunk`, and
the required check's `integration_id` (15368) can be satisfied.
