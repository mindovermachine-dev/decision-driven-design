# Findings — release v0.8.0, 2026-11-24

## F-1. The version is v0.8.0, from the rules

**Checked against `DDD-dec-82` as it stands on `main` at `e334ec1`.** Below 1.0, MINOR moves when
a ruled step is superseded incompatibly, when a step card is added, or when a step's register
moves. Editorial changes are PATCH.

- **Step 1's register moved.** At `v0.7.0`, `method/README.md` marked step 1 "Ruled for test".
  On `main`, the live card (`method/make-an-act-map.md`) and `method/README.md` say every part of
  the method is `[PROPOSED]`, step 1 included. `DDD-dec-124`'s statement says step 1 "leaves
  'ruled for test'". That is a register move, back from ruled. It is MINOR.
- **A card was added.** `method/make-an-act-map.md` is new in #89 (`DDD-dec-124`). MINOR.
- **A ruled step was superseded.** #84 gave step 1 a superseding `[PROPOSED]` first part
  (`DDD-dec-122`), and #89 superseded step 1's parts 2 to 5 (`DDD-dec-124`, Q-2). Below 1.0 this
  is MINOR. It is the row Emil's Round 30 ruling names.
- **Nothing calls for more.** The version is below 1.0, so MAJOR cannot arise. The new decisions
  and claims move no number by themselves (`DDD-dec-75`).

Three changes give MINOR, and none gives anything else. `v0.7.0` becomes **`v0.8.0`**, as the issue
says. G1 does not fire on the version.

**Noted, not acted on.** `DDD-dec-82` still says "below 1.0 until all ten steps are ruled". The
method is now four moves, and the old cards are not live. The count is #97's to change. This
release does not wait on it, as the issue rules.

## F-2. The range holds nothing the issue does not name

`git log v0.7.0..main` holds 73 commits. They come from six pull requests: #85 (a fast-forward
to `1bf7e56`), #86, #84, #87, #73 and #89. The issue names exactly these six. Outside
`meta/sessions/`, every changed file traces to one of them (bootstrap, "The range at arrival").

Two items in the range are not in the issue's basis list. Both come from pull requests the issue
names:

- **`DDD-address-02`**, which gained an appended note in #84. Its statement did not change.
- **`spec/doc-format.md`**, which arrived in #73. It is the schema `DDD-dec-94` names, so it is
  not a claim or a decision, and has no id to cite.

`DDD-address-09` gained a note in #89. It is in the issue's list (`DDD-address-06` to `-11`).

`DDD-address-02` goes into `basis` under "anything else the range carries". G1 does not fire on
the range.

## F-3. Every basis id resolves on `main`

Each id was read from `origin/main` (`e334ec1`) with `git show`, before it went into the descriptor.
All 17 resolve:

- the version and the preview: `DDD-dec-82`, `-75`, `-74`;
- the method (#89): `DDD-dec-124`;
- the act map and the pull (#84): `DDD-dec-122`, and `DDD-address-06` to `-11` (all six
  `status: projected`), with `DDD-address-02` (projected);
- the waiver (#86): `DDD-dec-123`;
- `applications/` for readers (#73): `DDD-dec-94`, `-95`, `-119` and `-120`.

## F-4. `prerelease: true` is Claude's choice, for Emil to confirm

The issue says this is not ruled. The descriptor follows `v0.6.0` and `v0.7.0`, because
`DDD-dec-74` keeps the method "ready to try (preview)". It says so in a comment, and the pull
request asks Emil to confirm it.

## F-5. The issue's exit for step 2 cannot hold at commit 1

Step 2's exit says "the releases gate and `canon changelog --check` pass" at commit 1. At format
2, `ratified_head` is mandatory (`spec/release-format.md` §3), and commit 2 fills it. So the
releases gate fails at commit 1, by design, as it did at `v0.6.0` and `v0.7.0` (prediction 3).
`changelog --check` can pass at commit 1. Both must pass at commit 2, and that is checked there.

## F-6. #90 to #93 record trial rulings that are not filed

Issue #100 says #90 to #93 propose amendments to the live card, and that none is ruled. That holds
for the method: no decision files them, and the live card does not change. But each of the four
issues says it "files what [the trial] ruled and proposes the rest", from the SDLC trials of
2026-11-20 to 2026-11-22. Those rulings are in issue bodies only.

The summary says what the repository says: the amendments are proposed, and none is ruled into the
method. It does not mention the trial rulings. Whether they count as rulings before they are filed
is Emil's to say. `UNVERIFIED — Emil review`.
