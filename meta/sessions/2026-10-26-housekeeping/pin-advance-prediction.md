# Predicted firing of the pin advance v5.15.1 → v5.15.2 (housekeeping session)

**Written and committed before the ref moves.** The staging commit that follows, and the bump on
Emil's acceptance of upstream PR #26, are the operation. Verification compares the observed firing
with this file limb by limb and records any divergence rather than reconciling it.

## The advance

| | Value |
|---|---|
| From | `v5.15.1` (the pin at `baec167`) |
| Staged at | upstream branch `claude/release-head-guard`, head `630475c` (PR #26) |
| To, on acceptance | tag `v5.15.2`, cut when PR #26 merges, under the release-head guard |
| Releases crossed | v5.15.2 only |
| Pins before | 74 |
| Pins added | 0 |
| Pins after | 74 |

## Prediction, limb by limb

| Limb | Predicted | Why |
|---|---|---|
| **E12** | **0** | PR #26 adds, removes and renames no claim or term. |
| **E13** | **0** | No `canonical_md` moves; nothing embedded here changes. |
| **W5** | **0** | No pinned status moves. `DDD-frame-02` stays projected; `DDD-dec-26` is a decision and is not pinned. |
| **W6** | **0** | The two canon edits in PR #26 are notes-only (`DDD-frame-02` notes; `DDD-dec-26` notes). Notes are outside the three fields `pinned_content_digest` hashes (statement, region, `canonical_md`). `DDD-frame-02`'s pinned digest `sha256:0002f60b…` is predicted unchanged. |
| **W7** | **1, unchanged** | The one standing shadowed id. |

Summary line expected from the checker at the staged ref and at the tag alike: **74 pins resolved,
0 basis-loss, 0 content-drift, 1 shadowed id**. No re-instrumentation step follows, because no
hash moves. This is the near-zero firing the charter asked for as the guard's dry run: the guard's
first release is one whose downstream consequence is predicted at nothing, so any firing at all is
a finding.

## Conditions that void this prediction

- **PR #26 changes before merge in a hashed field.** A ruled change to `DDD-frame-02`'s statement
  or region, or to any pinned term's `canonical_md`, voids the W6 limb; the prediction is restated
  in a new commit to this directory before the bump. Notes-only changes do not.
- **Another release lands first.** If any upstream release is cut between `v5.15.1` and
  `v5.15.2`, the prediction is re-run against it before the bump.
- **The guard refuses the cut.** If `v5.15.2`'s descriptor fails rule 7 at the merge (the head
  moved), no tag exists to bump to; the fix is a new descriptor commit upstream, and this
  prediction stands unchanged, since the canon it predicts over is unchanged.
