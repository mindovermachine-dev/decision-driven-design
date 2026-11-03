# Release format specification

> **Port note (`DDD-dec-84`).** Ported from `mindovermachine-dev/actor-indexed-determination` at tag
> `v5.15.2` (commit `084bce7`; last changed upstream at `1097055`). Below this note the text is
> unchanged. Read it with three differences for this repository:
>
> 1. **The canon gates are `scripts/ci.py`.** Where §3 says "every canon gate in `CLAUDE.md`",
>    read the gates `scripts/ci.py` runs. Its `releases` gate runs `scripts/validate-releases.py`,
>    and `scripts/check-release-head.py` for every descriptor not yet cut.
> 2. **The examples are upstream's.** `v5.5.0`, `v5.14.0`, `v5.15.0` and `d4fff7e` are the
>    principle repository's history. This repository's versions follow `DDD-dec-82`: `v0.1.0` to
>    `v0.4.0` were cut before this format existed and have no descriptors, and `v0.5.0` is the
>    first release under it.
> 3. **There is no release workflow yet.** Merging a descriptor does not cut a tag here. Emil cuts
>    it by hand at the merged head, after `main`'s CI has run the guard there. Porting the
>    workflow is a successor item.
> 4. **The order of a release's commits** (ruled 2026-11-03, S-11 of the canon CLI session). Here
>    `CHANGELOG.md` is the projection of `releases/` (`DDD-dec-104`), so adding a descriptor
>    changes `CHANGELOG.md` too. The descriptor and its `CHANGELOG.md` section are therefore
>    committed together, and that commit is the ratified head. `ratified_head` is then filled
>    alone, in the next commit (`canon ratify <version>`, which defaults to `HEAD`). The rule
>    itself is unchanged: the merged head is the ratified head plus at most the descriptor
>    (rule 7). Only the order of the commits differs from `v0.5.0`'s, whose ratified head came
>    before the descriptor.

**Format version: 2.** This file is the versioned schema artifact for release descriptors — shape
and validation rules only. It contains no process (how a release is proposed and reviewed is the
way of working) and no content (see `releases/`, one file per version). As with `claim-format.md`,
the three change independently.

**Versioning rules.** A format change bumps the format version and ships a migration note in this
file stating how existing descriptors move (or that they are valid unchanged). Descriptors declare
the format they conform to; validation is always against the declared version.

Storage: one YAML file per release under `releases/`, named for the version it declares —
`releases/v5.5.0.yaml`. The file **is** the release request. Adding one in a pull request is how a
release is proposed; merging it to the default branch is how the release is cut. There is no
second, out-of-band step, and no privileged local credential in the path.

---

## 1. Schema

```yaml
format: 1                    # spec version this descriptor conforms to; mandatory
version: v5.5.0              # v<major>.<minor>.<patch>; equals the filename stem; never reused
title: >                     # one line; the tag message is composed as "<version> — <title>",
                             # so the title carries no version prefix of its own
commit: e8663b8              # optional; the commit to tag. Omitted (the normal case) means
                             # "the commit that lands this file on the default branch", which
                             # is the only value a pull request cannot know about itself.
                             # Present pins an explicit earlier commit — a retro-cut.
date: 2026-08-16             # optional; when the release was prepared, not when it was cut
basis:                       # mandatory, non-empty; claim and decision IDs this release pins.
  - DDD-ground-01            # each must resolve to core/claims/ or core/decisions/
summary: >                   # mandatory; the release notes body, markdown, written not generated
draft: false                 # optional; create the GitHub Release as a draft
prerelease: false            # optional; mark the GitHub Release as a prerelease
```

## 2. Rules

1. **The version is the identity.** It matches `v<major>.<minor>.<patch>`, equals the filename
   stem, and is unique across `releases/`. Versions are never reused — the same rule claim IDs
   live under, for the same reason: a cut tag is a fact about history, not a name to recycle.
2. **The title carries no version prefix.** The tag message is composed as `<version> — <title>`
   with an em dash, matching `v5.0.0`..`v5.4.0`. A title beginning with its own version would
   double it.
3. **`commit` is optional, and omitting it is normal.** A pull request cannot know the SHA of its
   own merge, so the default is "wherever this file lands". Set it only to pin a release at an
   earlier commit, which CI requires be an ancestor of the default branch — a release must never
   pin canon the default branch does not carry.
4. **`basis` is mandatory and must resolve.** A release pins canon, so it cites the canon it pins.
   Every ID must name a file in `core/claims/` or `core/decisions/`. This is `DDD-agent-01`'s
   basis-as-query applied to releases: the citation is checked against the live repo, not taken on
   the confidence of the prose that proposes it.
5. **`summary` is mandatory.** Release notes are written and reviewed in the pull request, not
   generated from a commit range after the fact.
6. **Descriptors are immutable once cut.** A version whose tag exists is skipped, so editing its
   file changes nothing about the release. Corrections ship as a new version, never as a rewrite
   of a cut one.

## 3. Validation

A descriptor is valid iff: it declares `format`; validation runs against the declared version's
rules (§2 for format 1; §2 plus §4 for format 2); `version`, `title`, `basis`, and `summary` are
present and well-formed; the filename agrees with `version`; every `basis` ID resolves; and, at
format 2, `ratified_head` is present and looks like a SHA. `scripts/validate-releases.py`
implements this and runs on every pull request touching `releases/`.

Validity is necessary but not sufficient for a cut. CI additionally requires, at the commit under
release, that the tag does not already exist, that the target is an ancestor of the default branch,
and that every canon gate in `CLAUDE.md` passes — ordering and transclusion, claim and decision
schema, and reproduction of every `core/assets/` computation — and, at format 2, that the
release-head guard (§4, rule 7) passes. A valid descriptor whose gates fail is not cut, and
leaves no tag behind.

## 4. Format 2 — the release-head guard (additive)

**Migration note.** Format 2 adds one mandatory field, `ratified_head`, and one rule (7). Format 1
descriptors are valid unchanged and stay at format 1; a cut descriptor is immutable (rule 6) and
is never migrated. New descriptors declare `format: 2`.

```yaml
format: 2
ratified_head: d4fff7e      # mandatory at format 2; the commit whose canon this release ratifies
```

7. **The merged head is the ratified head plus at most the descriptor.** `ratified_head` names
   the commit the principal ratifies. At the commit under release, CI requires that
   `ratified_head` is an ancestor of it, and that nothing but `releases/<version>.yaml` changed
   between `ratified_head` and the head that merged (the merge commit's second parent, where it
   is a merge). A release that fails either check is not cut, and leaves no tag behind. The
   descriptor commit therefore comes last on the branch, after the canon it ratifies, and a
   ruled change to the canon after the descriptor was written means a new descriptor commit
   naming the new head. `scripts/check-release-head.py` implements the check, and its
   `--hitlist` mode runs every cut descriptor against its own tag.

   Why: v5.14.0 and v5.15.0 were both cut from a head that was not the head the principal had
   ratified — the first before `DDD-dec-36` landed, the second one commit before the GATE 2 fix.
   Nothing in the tooling could see either, because no file said which head had been ratified.
   The descriptor is the release decision (§5), so the head it ratifies is part of its basis:
   recording it is `DDD-agent-01`'s basis-as-query applied to the release act. Ruled under
   `DDD-dec-39`.

## 5. Why the descriptor and not the tag (note)

Interpretation note, not a rule. The tag is the artifact; the descriptor is the decision that
produced it. Filing the decision as a reviewable file, with a principal (the pull request's author
and approver) and `basis` edges to the claims it rests on, is the ontology's own treatment of
decisions applied to this repository's releases — a release cut by an unreviewed command is an
escaped decision about which canon the world sees.
