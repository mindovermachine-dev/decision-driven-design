# Findings — release v0.7.0, 2026-11-10

## F-1. The version is v0.7.0, from the rules

**Checked against `DDD-dec-82` and `method/README.md` §Registers.** MINOR moves when a step card
is added or a step's register moves. Below 1.0, everything else is PATCH or nothing.

- **A card added.** `method/01b-map-the-flow-of-demand.md` arrived in #68 (`DDD-dec-118`), at
  `[PROPOSED]`. That alone makes the release MINOR, so `v0.6.0` becomes `v0.7.0`.
- **No register moved.** Across `v0.6.0..main`, the step table in `method/README.md` and
  `README.md` gains the 1b row and nothing else. The cards for steps 1 to 10 are unchanged, except
  that 1 and 7 each gain one line pointing to 1b. Step 1 stays "Ruled for test". Steps 2 to 10
  stay `[PROPOSED]`.
- **Nothing calls for more.** The version is below 1.0, so MAJOR cannot arise (`DDD-dec-82`). The
  new decisions (`DDD-dec-114` to `-118`) and claims (`DDD-flow-01` to `-04`) move no number by
  themselves (`DDD-dec-75`). They count only through 1b's card.
- **Noted, not acted on.** `DDD-dec-118` (N-1) records that "the version stays below 1.0 until
  all ten steps are ruled" now counts eleven steps, and needs a ruling to say so. This does not
  change v0.7.0. It will matter at 1.0.

## F-2. The prompt calls the specifications `[PROPOSED]`. The repository says they are ruled. Emil to settle

The prompt says: "Say plainly that the step and the specs are [PROPOSED]."

**The step is `[PROPOSED]`.** That agrees with the card and with `DDD-dec-118`. Its place and
scope are ruled. Its procedure, fields and worked example are Claude's,
`UNVERIFIED — Emil review`.

**The PDLC and SDLC specifications are ruled**, according to the repository:

- `applications/pdlc/pdlc.md` opens with "Register: ruled (Rounds 28 to 30)".
- `applications/sdlc/sdlc.md` opens with "Register: ruled (Rounds 28 and 30)".
- The statements of `DDD-dec-114` and `DDD-dec-115` both say "Round 28 rules the … specification's
  proposals as drafted".

**One index disagrees.** `applications/README.md` still marks `sdlc/sdlc.md` as `[PROPOSED]`.
The `2026-11-07-sdlc-and-pdlc` row in `meta/sessions/README.md` does the same. The row is
historical and describes the session as it first landed. The index line is a stale line, a bug in
the prose (`AGENTS.md`). This session does not fix it: a fix after the ratified head would break
the release-head guard (rule 7), and the line is not the release's to change.

**What the summary says.** It follows the repository (`AGENTS.md`: "The repo is ground truth"):

- the specifications are **ruled**;
- step 1b is **`[PROPOSED]`**;
- `DDD-flow-01` to `-04` are **projected**;
- the parts of the specifications that remain proposals are named as such: O-8's plan-acceptance
  act, and `DDD-dec-116` and `-117` not yet applied.

**Another reading.** "The specs" in the prompt may mean the specifications that
`DDD-dec-116` (specification feasibility) governs. Read that way, the prompt and the repository
agree. `DDD-dec-116` and `-117` are ruled, and the changes they call for to `what.md`, `how.md`,
`authority.md` and product-cli's definition are not yet made (S-1 to S-8 in that session's
`successor-items.md`).

**If Emil wants the PDLC and SDLC called `[PROPOSED]`**, that contradicts `DDD-dec-114` and `-115`
as they stand. It needs a ruling, not a wording change. The summary then changes, which means a
new commit 1 and a new ratification.

## F-3. `prerelease: true` is Claude's choice, for Emil to confirm

The prompt says this was asked and not answered. The descriptor says so in a comment, and the
pull request asks for it.

## F-4. #67 is an issue

The prompt names "PRs #63 to #68". #67 is the demand-flow session's issue, not a pull request. The
range comes from five pull requests: #63, #64, #65, #66 and #68.
