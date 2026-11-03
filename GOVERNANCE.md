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
gates (item 4), and the signing exception (item 8). Every other item applies as the standard
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
for the `repo-standard` tool Varve uses. **The file is not yet applied.** Applying it needs
repository admin, which is Emil's act. Until it is applied, the repository and the file disagree,
and the file states the intent.

| | What |
|---|---|
| **`Signed Commits`** ruleset on `main` | Signed commits required, with the admin role and the Claude GitHub App on the bypass list (see below) |
| **Discussions** | On |
| **Description and topics** | One line stating the projection and its preview status |
| **Maturity** (organisation property) | `Experimental`, moving to `Incubating` when step 1 is reported |
| **Projects** | An upstream roadmap board and a downstream work board (below); not managed by the file |

### Departure 3 — the signing exception (item 8)

Commits from AI sessions in the claude.ai cloud workspace are **exempt from the signature
requirement**, through the ruleset's bypass. This is Varve's stated deviation, adopted for the
same reason ([`DDD-dec-81`](core/decisions/DDD-dec-81.yaml)). Those sessions do sign, but with a
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
