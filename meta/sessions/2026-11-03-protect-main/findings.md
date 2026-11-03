# Findings — protect main, 2026-11-03

What the session found that the ruling does not settle. Reported, not acted on. Each is flagged
`UNVERIFIED — Emil review` where it rests on Claude's reading.

## F-1 — the Signed Commits Integration bypass (1236702)

The prompt asks two questions: whether 1236702 is this organisation's Claude app, and whether
the bypass is still needed.

**Is 1236702 the right id? Not verifiable from this session.** The id was copied from Varve
(`Hafeok/varve`, `.github/repo-standard.yaml`: "Integration 1236702 the Claude GitHub App").
`GET /apps/claude` is refused from here: the session's GitHub access is bound to this
repository's endpoints. The repository's events show no app as the actor of any push (below), so
nothing in this repository names the app's id either. A GitHub App's id is global, not per
organisation. So if this organisation's Claude app is the same public Claude GitHub App that
Varve's installation uses, the id is the same. Emil can settle it with one read:

```bash
gh api /apps/claude --jq '.id, .slug, .owner.login'
```

**Is it still needed? On the evidence, no, for the commits it was put there for.**

- The 40 most recent commits on `main` (back to `f199fb0`) are all `verified: true`,
  reason `valid`. Every session commit among them is signed by
  `Claude (Emil) <claude+emil@okkels-klein.dk>` with a registered key. No commit in that range
  needed the exception.
- `GET /repos/.../events` (the last 100 events, 2026-10-25 to 2026-11-02) shows 35 pushes. Every
  one, to `main` and to `claude/*` session branches alike, has `Hafeok` (user 2194785) as its
  actor, and none has an app. If GitHub evaluates bypass against that actor, the
  `RepositoryRole 5` (admin) entry already exempts every such push. The Integration entry would
  then add nothing.

`UNVERIFIED — Emil review`: how GitHub attributes a push made with the Claude app's
user-to-server token, for a ruleset's bypass. The events API says the user. Whether the bypass
check also sees the app was not tested.

**What Emil could rule** (not changed here, as the prompt says): remove the Integration
1236702 entry, since registered-key signing has replaced the exception in practice. A second
question follows from the second bullet: whether the `RepositoryRole 5` entry should stay, since
it exempts everything pushed under Emil's account from the signing rule. Varve keeps it so the
maintainer's `land/` fast-forward passes over unsigned agent commits. Here, with every commit
signed, it would only be needed for a commit that is not.

## F-2 — `land/**` and `v*` restricted to Emil may not exclude sessions

Same evidence as F-1: cloud sessions push under Emil's account (`Hafeok`, 2194785). The `land` and
`Release Tags` rulesets name exactly that user as their only bypass actor. If GitHub reads such a
push as Emil's, a cloud session can create a `land/` branch or a `v*` tag, and "restricted to
Emil" does not separate Emil from the sessions working under Emil. Recorded in `DDD-dec-108`'s
notes. The check is in `landing.md` (check 3).

## F-3 — what the trunk ruleset does not refuse

The `trunk` ruleset refuses a deletion of `main`, a non-fast-forward push to it, and a push whose
head lacks a successful `pipeline (devcontainer)` check from GitHub Actions. It does not refuse
two things, by anyone with write access. A fast-forward of `main` to a commit that went green on
another branch is accepted. So is a GitHub merge of a pull request whose check is green.
`canon land` is the landing mechanism by `DDD-dec-108`, and the `land` ruleset makes `land/`
Emil's. Neither of those closes the two paths. Stated in `GOVERNANCE.md` and in the decision's
notes. Varve accepts a merge of a pull request as a second way in. Whether this repository wants
merges off (repository `merge:` settings, which `repo-standard.yaml` does not manage today) is
Emil's question.
