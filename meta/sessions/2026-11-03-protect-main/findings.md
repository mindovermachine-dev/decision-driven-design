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

## Round 2 — 2026-11-03

Add-only.

**F-1, its open half answered.** 1236702 is this organisation's Claude app. The REST API marks
every issue, pull request and comment that a session made here with
`performed_via_github_app: {id: 1236702, slug: claude}`, though the `user` is `Hafeok`. Issues
#37 to #54 carry it, and so does this session's own comment on #51 (6598918330). Read from
`GET /repos/.../issues` and `/issues/51/comments` at 09:2x UTC. The bypass entry named the right
app. Emil ruled it removed regardless (S-2).

**F-4 — what tells Emil from a session on GitHub.** Pushes and comments both carry `Hafeok` as
the actor, so neither the rulesets nor a login can separate Emil from a session. Two things
can. A commit made by a session carries a `Claude-Session:` trailer, which is the ruling's
identifier. A comment made by a session carries `performed_via_github_app` (the Claude app).
GitHub sets that field, and a session cannot clear it. Agent review uses both
(`DDD-dec-109`).
`UNVERIFIED — Emil review`: that no path open to a session posts a comment without the app.
The evidence is every session comment here, all of which carry it.

## Round 3 — 2026-11-03

Add-only.

**F-5 — why the gates App's id changed, 5220446 → 5594102.** 5220446 was copied from Varve's
`.github/repo-standard.yaml`, where it names Varve's gates App. Round 2 asked Emil to confirm it
before anything relied on it (R2-0). Emil's Round 3 ruling covers the case where that App cannot
be installed on `mindovermachine-dev`: a new App owned by the organisation. Emil created it:
"mom-gates", integration id 5594102, with Checks: read and write and Pull requests: read. The
id was swapped before any landing, as the ruling asks. It is pinned in one place,
`.github/repo-standard.yaml`'s trunk ruleset, which both `canon land` and `canon agent-review
--post` read. The tests hold it as the gates App's id, and one asserts the live pin equals it.
`GOVERNANCE.md` and the workflow's header name it. canon's source has no id in it to change.
