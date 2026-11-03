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
