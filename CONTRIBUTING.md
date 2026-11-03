# Contributing

This repository is the software projection of Decision-Driven Design. It holds the method, the
claim graph behind it and the decisions that rule it. Contributions are welcome. The most useful
one is a report of what happened when you tried the method.

This page says where a contribution goes, how to make one, and how it reaches `main`.
[`GOVERNANCE.md`](GOVERNANCE.md) says who decides and why the rules are as they are.

## Where it goes

| You want to | Do this |
|---|---|
| Report what happened when you tried a method step | Open an issue with the **Field report** template |
| Show that the software projection bends or contradicts itself | Open an issue with the **Projection pressure** template |
| Propose a decision, or a change to one | Open an issue with the **Decision proposal** template |
| Report a checker that reports wrongly | Open an issue with the **Checker defect** template |
| Show that a core claim is false (the floor, selection and training, the measure, conservation) | Open an issue in the [principle repository](https://github.com/mindovermachine-dev/actor-indexed-determination/issues). Core claims are canon there; this repository only pins them |
| Ask a question, or share an idea | Use [Discussions](https://github.com/mindovermachine-dev/decision-driven-design/discussions) |
| Report a security problem, or material that must not be here | Follow [`SECURITY.md`](SECURITY.md). Never open a public issue |

Never include customer-identifying material in an issue, a commit or a file. Describe a system by
its kind, not its owner.

## Two kinds of change

Every change is one of two kinds, and they land differently ([`DDD-dec-78`](core/decisions/DDD-dec-78.yaml)).

| Kind | What it is | What it needs |
|---|---|---|
| **Editorial** | Links, typos, wording that changes no ruling, community files, tooling that changes no decision | Green CI. Review is welcome and does not block |
| **Canon** | Anything that files, supersedes or ratifies a decision, and so every change under `core/` | Green CI, and Emil's ratification. A canon change waits until Emil rules |

If you are unsure which kind your change is, treat it as canon.

## Making a change

### 1. Open an issue first

Every commit names an issue, as `Refs #N` in its message ([`canon.yaml`](canon.yaml),
`issue-refs`). Open the issue before you start, so the work has a number to cite.

### 2. Work in the development container

The [devcontainer](.devcontainer/devcontainer.json) has everything the gates need: Python with the
checkers' dependencies, the .NET SDK, git and `ssh-keygen`. Outside it, install
[`scripts/requirements.txt`](scripts/requirements.txt), whose header also lists the system tools,
and the .NET SDK named in [`tools/canon/global.json`](tools/canon/global.json).

### 3. Write the commit message

| Rule | Applies to | Checked by |
|---|---|---|
| `Refs #N` naming the issue | Every commit | `canon issue-refs` |
| `Basis: <ids>` naming the claims and decisions the change rests on | Every commit that touches `core/` | `canon issue-refs --basis` |
| Signed (SSH or GPG, with the key registered on your GitHub account) | Every commit | The `Signed Commits` ruleset on `main` |

`Basis:` is not bookkeeping. A change to canon with no cited basis is, by this repository's own
ontology, an escaped decision (`DDD-agent-01`; [`AGENTS.md`](AGENTS.md)).

### 4. Follow the rules for decisions and claims

- A filed decision is never edited. A change to it is a new decision that supersedes it, or a
  dated, add-only note in its `notes`.
- A claim or decision id is never reused, and never renumbered.
- Ids share one space across this repository and the principle repository. Before you file one,
  check every branch of both repositories for the highest id in use.
- Every decision has `basedOn` edges. A decision with none is refused as an escaped decision.
- Reasoning nobody with authority has confirmed is marked `UNVERIFIED — Emil review`.

[`meta/way-of-working.md`](meta/way-of-working.md) and [`spec/claim-format.md`](spec/claim-format.md)
are the full rules.

### 5. Run the gates before you push

```bash
python3 scripts/ci.py
cd tools/canon
dotnet test --project tests/Canon.Tests -c Release
dotnet run --project src/Canon -c Release -- changelog --check
dotnet run --project src/Canon -c Release -- issue-refs --basis
dotnet run --project src/Canon -c Release -- check --compare
```

That is exactly what CI runs. Each command must exit 0.

### 6. Open a pull request

Push your branch, or your fork, and open a pull request against `main`. The template asks for what
changed, the decisions involved, what was predicted and measured, and what is left. CI runs
`pipeline (devcontainer)` on every push to your branch and on the pull request (GitHub checks out
the pull request's merge with `main` for that run, not its head).

Do not merge the pull request on GitHub, even if you can. Work reaches `main` only by landing.

## How a change reaches `main`

**`main` accepts only a fast-forward to a commit whose own check has passed**
([`DDD-dec-108`](core/decisions/DDD-dec-108.yaml)). The `trunk` ruleset refuses everything else
that it can see: a direct push without a green `pipeline (devcontainer)` on that exact SHA, a
force-push and a deletion. Nobody bypasses it, the admin role included.

**Emil approves the head first** ([`DDD-dec-109`](core/decisions/DDD-dec-109.yaml)). He comments
`approve <head sha>` on the pull request, by hand, naming at least the first 12 characters of its
current head. The gates App then posts the check `agent review`, green, on that head, and the
`trunk` ruleset requires it beside `pipeline (devcontainer)`. A push after the approval needs a
new one. Some comments do not count: an approval of an earlier head, an edited comment, and a
comment made through an app. Every comment a Claude session writes is made through the Claude
app, even under Emil's login. Until the gates App is installed and `.github/repo-standard.yaml`
re-applied, the check is declared but not yet required.

Landing is Emil's act, after the approval. He lands with `canon land`
([`tools/canon/`](tools/canon/DESIGN.md)), which refuses a head without the gates App's green
`agent review` once `main`'s `.github/repo-standard.yaml` requires it:

```bash
alias canon='dotnet run --project tools/canon/src/Canon -c Release --'

                          # first: Emil's comment "approve <head sha>" on #47
canon land 47 --print     # fetch, then show the pushes and make none
canon land 47             # push the pull request's head to land/pr-47
                          # wait for pipeline (devcontainer) to go green on land/pr-47
canon land 47 --main      # fast-forward main to land/pr-47, then delete land/pr-47
```

`canon land --commit <sha>` does the same for a commit with no pull request; its `land/` branch
is named by the commit's first twelve characters unless `--name <name>` names it. Once
`agent review` is required, such a commit cannot be approved, and it lands through a pull request
instead. A head that adds
a release descriptor lands on `land/release-<version>` instead. The second step refuses if
`land/<name>` has moved, or if `main` is not an ancestor of it. Only Emil
can create or move a `land/` branch.

For a canon change, Emil's landing is his ratification act. Your pull request is closed as merged
when `main` contains its head.

## Releases

A release is a decision, filed as a descriptor under [`releases/`](releases/), and cut only from
the head Emil ratified ([`DDD-dec-84`](core/decisions/DDD-dec-84.yaml),
[`spec/release-format.md`](spec/release-format.md)). It takes two commits:

1. The descriptor and its `CHANGELOG.md` section, which `canon changelog` generates from it. This
   is the head Emil ratifies.
2. `canon ratify <version>`, which fills `ratified_head` and changes nothing else.

After landing, `canon release <version>` cuts the signed tag and the GitHub Release. It refuses if
the tag exists anywhere: locally, on the remote or as a GitHub Release. A cut release's descriptor
is never edited again; the releases gate fails if it differs from the file at its tag. Only Emil
can create a `v*` tag.

## AI-assisted sessions

Much of this repository is written by AI sessions working under Emil's rulings. They follow the
same rules as anyone else, and these in addition:

- A session commits `prompt.md` and `bootstrap.md` under `meta/sessions/YYYY-MM-DD-<slug>/` before
  any other change ([`meta/sessions/README.md`](meta/sessions/README.md)).
- It writes predictions before it runs an operation, and records each outcome under its
  prediction.
- It records each of Emil's rulings verbatim, when it is given.
- It stops at every gate. Nothing self-ratifies.
- **It never lands.** It pushes its branch, waits for green CI, reports the head and the
  `canon land` commands, and stops. Landing is Emil's act.
- It signs with a key registered on GitHub, so its commits show as verified.

[`AGENTS.md`](AGENTS.md) is the instruction file a session reads.

## What the framework will not do

- Claim physical-law status without a measurable quantity.
- Group opposite error directions under one mechanism.
- Assert intelligence where the acceptance predicate does not close, or deny it there either. The
  framework declines that verdict on purpose.

## Licence

By contributing, you agree that your contribution is licensed as the repository is: specification
text under CC BY-SA 4.0, code and schemas under MPL-2.0 ([`LICENSING.md`](LICENSING.md),
[`DDD-dec-79`](core/decisions/DDD-dec-79.yaml)). There is no contributor licence agreement and no
copyright assignment.
