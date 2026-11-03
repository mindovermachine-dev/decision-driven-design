# Governance

Decision-Driven Design is run to the **Mind Over Machine open-source stewardship standard**
([mindovermachine-dev](https://github.com/mindovermachine-dev)), adopted in full as it applies to
a specification repository ([`DDD-dec-76`](core/decisions/DDD-dec-76.yaml)). How each of the
standard's fourteen items applies was ruled item by item
([`DDD-dec-81`](core/decisions/DDD-dec-81.yaml)). This document follows Varve's
`GOVERNANCE.md` in form, so that moving between the organisation's projects feels familiar. Where
it differs from another of them, that is a defect unless it says why.

**Three departures from the standard are stated here, each with the decision that rules it:**
merging as a blocking review for decisions (item 5), session branches that live as long as their
gates (item 4), and the signing exception (item 8), which is now withdrawn
([`DDD-dec-110`](core/decisions/DDD-dec-110.yaml)). Every other item applies as the standard
writes it, or as `DDD-dec-81` adapts it.

## Who decides

**Emil Okkels Klein** is the principal: the maintainer, the sole copyright holder, and the only
person who can rule a decision, merge a pull request or cut a release. Decisions name the
principal as `principal: Emil`.

That is the whole list. One principal is the reason several rules here look stricter than a small
project needs: with nobody else to catch a mistake in review, the record and the gates have to
catch it instead.

## How decisions are recorded

**A decision is a file, or it did not happen.** Every decision about the method, the projection
or this repository is a node under [`core/decisions/`](core/decisions/), `DDD-dec-NN`. Each
carries its principal, when and where it was made, its resolution, and its `basedOn` edges. A
decision with no `basedOn` is an escaped decision, and the checker refuses it.

**A ruled decision is never edited.** A decision that changes gets a superseding decision, and the
old one keeps its text, so the reasoning that was wrong stays readable. Ids are never reused and
never renumbered. Retired claims stay in the graph with the correction that retired them.

**Rulings are recorded verbatim.** A session records each ruling in its own words under
[`meta/sessions/`](meta/sessions/), in the round it was given, before the decision that files it.
Readings beyond the words are flagged `UNVERIFIED — Emil review` until Emil confirms them.

**Authority, in order.** The actor-general canon in the principle repository, at the tag pinned in
[`graph/upstream.yaml`](graph/upstream.yaml) ([`DDD-dec-04`](core/decisions/DDD-dec-04.yaml)).
Then [`meta/way-of-working.md`](meta/way-of-working.md), which wins over older material. Then the
claim files under [`core/claims/`](core/claims/), which govern their prose: prose that contradicts
its claim is a bug in the prose. Then the decisions. Then everything else.

**Paths in records resolve at the record's own commit**
([`DDD-dec-80`](core/decisions/DDD-dec-80.yaml)). A file moved later is not a broken record. Read
the record at its commit, or look in [`meta/history/`](meta/history/) and [`scripts/`](scripts/).

A decision may be **proposed by anyone**, as an issue using the decision-proposal template. Emil
rules on it, and a refusal says why in writing.

## How work reaches the trunk

**`main` is the trunk.** Every gate runs on every push and every pull request, from one entry
point, [`scripts/ci.py`](scripts/ci.py), inside the development container
([`.devcontainer/`](.devcontainer/devcontainer.json)). The gates are claims, decisions, core order
and upstream pins, the What, the How examples, and the checker fixtures. Running
`python3 scripts/ci.py` locally is the same pipeline.

**A commit reaches `main` only once its own checks have passed, and Emil has approved it**
([`DDD-dec-108`](core/decisions/DDD-dec-108.yaml),
[`DDD-dec-109`](core/decisions/DDD-dec-109.yaml)). The mechanism is `canon land`
([`DDD-dec-101`](core/decisions/DDD-dec-101.yaml), [`tools/canon/`](tools/canon/DESIGN.md)):

1. **Emil approves the head.** He comments `approve <head sha>` on the pull request, by hand,
   with at least 12 characters of the head. The gates App then posts the check `agent review`,
   green, on that head ([`.github/workflows/agent-review.yml`](.github/workflows/agent-review.yml)).
2. `canon land <pr>` pushes the pull request's head to `land/<name>`.
3. CI runs there, and `pipeline (devcontainer)` goes green on that SHA.
4. `canon land <pr> --main` fast-forwards `main` to `land/<name>`, then deletes `land/<name>`.
   It never makes a merge commit. Both `canon land` steps refuse a head that does not carry the
   gates App's green `agent review`.
5. The `trunk` ruleset refuses everything else that it can see: a deletion of `main`, a
   non-fast-forward push to it, and a push whose head lacks a successful
   `pipeline (devcontainer)` check from GitHub Actions or a successful `agent review` check
   from the gates App. Nobody bypasses it, the admin role included.

**Why the approval is a comment, and why it must be by hand.** Sessions push and comment under
Emil's account, so neither the rulesets nor a GitHub login can tell Emil from a session. Agent
review counts a comment only when GitHub records no app as having made it, and only when it was
not edited. A session's comments are made through the Claude app. The identity map is
[`.github/identities.json`](.github/identities.json), read from `main`. A session is known on a
commit by its `Claude-Session:` trailer, not by the account that pushed it. Every pull request needs
the approval, whoever wrote its commits ([`DDD-dec-109`](core/decisions/DDD-dec-109.yaml)).

Two paths stay open beside `canon land`: a fast-forward of `main` to a commit green on another
branch, and a GitHub merge of a green pull request. Once `agent review` is required, both need
Emil's approval of that head as well. Neither is how work lands here; `canon land` is. **Until
the gates App is installed and the file re-applied, `agent review` is declared but not
required**, and the landing works as before without step 1.

### Departure 1 — merging is a blocking review for decisions (item 5)

The standard requires human review for a release, not for a merge. **Here, merging the pull
request that files a decision is Emil's ratification act**, and so it is a blocking review
([`DDD-dec-78`](core/decisions/DDD-dec-78.yaml)). It applies to any change that files, supersedes
or ratifies a decision, and so to every change under `core/`. That merge is this repository's
counterpart of the standard's release review.

Editorial changes, such as links, typos, community files and tooling that changes no decision, may
reach `main` without a ratification act. Reviews on them are non-blocking, as the standard asks.

### Departure 2 — session branches live as long as their gates (item 4)

The standard asks for trunk-based development. **A canon session may hold a branch open only for
as long as its gates** ([`DDD-dec-78`](core/decisions/DDD-dec-78.yaml)). A session that needs
Emil's ruling at a gate cannot land the work past that gate before Emil rules, so the work waits on
the branch, and only that work. Anything not behind a gate lands on the trunk. The branch closes
when the session's last gate is ruled.

### Releases

**The version is the method's** ([`DDD-dec-75`](core/decisions/DDD-dec-75.yaml)), under SemVer as
mapped by [`DDD-dec-82`](core/decisions/DDD-dec-82.yaml). The version stays below 1.0 until all
ten steps are ruled. MINOR moves when a step card is added or a step's register moves. PATCH moves
for editorial changes. From 1.0, MAJOR moves when a ruled step is superseded incompatibly. A
release is a decision, filed as a descriptor and cut on Emil's merge under the release-head guard
(upstream `DDD-dec-39`). The cut happens only at the head Emil ratified.

`CHANGELOG.md` is generated from the descriptors ([`DDD-dec-104`](core/decisions/DDD-dec-104.yaml)),
so a release goes in two commits (ruled 2026-11-03). The first carries the descriptor and its
`CHANGELOG.md` section, and is the head Emil ratifies. The second only fills `ratified_head`
(`canon ratify`). The release-head guard is unchanged: the merged head is the ratified head plus
at most the descriptor ([`spec/release-format.md`](spec/release-format.md), rule 7).

## Repository settings

The settings are declared in [`.github/repo-standard.yaml`](.github/repo-standard.yaml), written
for the `repo-standard` tool Varve uses. **Emil applied it on 2026-11-03, in two runs.** The
first, at `main` `5ccdf41`, applied the description, the topics, Discussions and the `Signed
Commits` ruleset. The second, at `main` `458d05b`, created `trunk`, `land` and `Release Tags`.
Emil then probed it the same day: a signed direct push to `main` was refused with `GH013`,
"Required status check "pipeline (devcontainer)" is expected."

| | What |
|---|---|
| **`trunk`** ruleset on `main` | no deletion, no force push, **no bypass**; the required status checks `pipeline (devcontainer)`, from GitHub Actions only ([`DDD-dec-108`](core/decisions/DDD-dec-108.yaml)), and `agent review`, from the gates App only ([`DDD-dec-109`](core/decisions/DDD-dec-109.yaml); declared, not yet applied) |
| **`Signed Commits`** ruleset on `main` | Signed commits required, with the admin role the only actor on the **bypass list** ([`DDD-dec-81`](core/decisions/DDD-dec-81.yaml), [`DDD-dec-110`](core/decisions/DDD-dec-110.yaml); the Claude GitHub App's entry removed, not yet applied) |
| **`land`** ruleset on `land/**` | creating, moving, deleting or force-moving a `land/` branch is restricted to Emil ([`DDD-dec-108`](core/decisions/DDD-dec-108.yaml)) |
| **`Release Tags`** ruleset on `v*` tags | creating, deleting or force-moving a `v*` tag is restricted to Emil ([`DDD-dec-108`](core/decisions/DDD-dec-108.yaml)) |
| **Discussions** | On |
| **Description and topics** | One line stating the projection and its preview status |
| **Maturity** (organisation property) | `Experimental`, moving to `Incubating` when step 1 is reported |
| **Projects** | An upstream roadmap board and a downstream work board (below); not managed by the file |

### Departure 3 — the signing exception (item 8), withdrawn

**Withdrawn** ([`DDD-dec-110`](core/decisions/DDD-dec-110.yaml)). Sessions here sign with a key
registered on GitHub, and their commits verify. The 40 most recent commits on `main` were all
verified on 2026-11-03. So the Claude GitHub App (integration 1236702) is no longer on the
`Signed Commits` bypass list. The admin role stays the only bypass. A session commit that does
not verify is refused, unless it reaches `main` in a push the admin bypass covers. Sessions push
under Emil's account, so that bypass may cover their pushes too. That push can only be
`canon land`, after Emil has approved the head ([`DDD-dec-110`](core/decisions/DDD-dec-110.yaml),
notes).

The exception, as it stood until then, is kept below for the record.

Commits from AI sessions in the claude.ai cloud workspace were **exempt from the signature
requirement**, through the `Signed Commits` ruleset's bypass. This was Varve's stated deviation,
adopted for the same reason ([`DDD-dec-81`](core/decisions/DDD-dec-81.yaml)). Those sessions do sign, but with a
key the sandbox platform provides, which is registered to nobody, so GitHub reports
`unknown_key`. Registering that key was rejected for Varve and is rejected here. The key is not
ours, cannot be rotated by us and is reused across sessions, so registering it would let any such
session produce commits GitHub attests as Emil's.

Two things attest those commits instead. The **push path**: only Emil's installation pushes here.
The **session record**: [`meta/sessions/`](meta/sessions/) says what was asked and what came back.
A Claude Code session with a registered key signs like a human and needs no exception. The
ready-to-try session moved to one for that reason and re-signed its earlier commits (its
`bootstrap.md`, amendment 1).

## The two boards

The standard asks for an **upstream board representing the roadmap** and **downstream boards
designed to minimise work in progress** (item 12). There is one of each.

**Roadmap** (upstream). The method's roadmap: one card per method step, 1 to 10. A card moves as
the step's register moves, from proposed to ruled to reported. It answers "how far along is the
method?" and it moves slowly.

**Work** (downstream). A Kanban with a **work-in-progress limit of 2** in *In progress*, because
one principal rules everything. It answers "what is happening now?" An issue enters it only when
it is next. An issue that cannot progress goes back rather than sitting in *In progress*.

**Traceability** (item 6). Every session is recorded under `meta/sessions/` (`DDD-dec-20`). Every
session also gets an issue, and its commits carry `Refs #N`. `scripts/ci.py` will enforce that
once the first session has done it by hand.

## Channels

| For | Where |
|---|---|
| Questions, ideas, what you tried | [Discussions](https://github.com/mindovermachine-dev/decision-driven-design/discussions), once turned on |
| Trying the method and reporting what happened | An issue, with the field-report template |
| A projection under pressure, a decision proposal, a checker defect | An [issue](https://github.com/mindovermachine-dev/decision-driven-design/issues), with its template |
| A falsification of a core (actor-general) claim | The [principle repository](https://github.com/mindovermachine-dev/actor-indexed-determination/issues) |
| A vulnerability | **Privately.** [`SECURITY.md`](SECURITY.md) |
| Conduct | [emil@okkels-klein.dk](mailto:emil@okkels-klein.dk), [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) |

Blank issues are disabled.

## Licence and contributions

Specification text is CC BY-SA 4.0 and code is MPL-2.0 ([`DDD-dec-79`](core/decisions/DDD-dec-79.yaml),
[`LICENSING.md`](LICENSING.md)). The repository could be relicensed in 2026 because every author was
Emil or an AI working under Emil. After the first outside contribution that stops being true:
a licence change would then need every contributor's consent. There is **no CLA and no copyright
assignment**, so in practice the licence is then settled.

## Becoming a maintainer

There is one maintainer. These would lead to a second:

1. **A track record here.** Several merged changes, at least one of which touched a decision, not
   only tooling.
2. **Judgement about the rules**, shown by using them. For example, noticing that a change needs a
   superseding decision, or that a claim's evidence does not reproduce.
3. **An invitation from Emil**, filed as a decision.

## AI assistance

Decision-Driven Design is developed with AI assistance under Emil's rulings. Sessions are held to
the same rules as anyone else: the same gates, and the same requirement that a decision be a file
with its basis.

Every AI session leaves a record under `meta/sessions/`. Its prompt and bootstrap are committed
first (`DDD-dec-20`), its rulings verbatim, and its predictions before the operations they
predict. Every commit that changes canon carries a `Basis:` line naming the claims and decisions
it rests on. [`AGENTS.md`](AGENTS.md) is the instruction file a session reads.

The division is plain: **a session produces work, and Emil is accountable for it.** Emil accepts
it by merging, and that merge is the ratification act (Departure 1).
