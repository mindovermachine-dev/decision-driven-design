# Prompt — release v0.7.0, 2026-11-10

The session prompt, verbatim. Per `DDD-dec-20`, this file is committed before any other file
changes, so the session's scope is fixed at arrival.

---

New session: the v0.7.0 release descriptor, 2026-11-10, in mindovermachine-dev/decision-driven-design. Branch from main. On 2026-11-10 main was 87db443. Report main's head at arrival, and say so in bootstrap.md if it has moved. Open an issue; Refs #N on every commit. Commit prompt.md and bootstrap.md under meta/sessions/2026-11-10-release-v0.7.0/ first.
Emil's rulings, verbatim
Claude explained that the release goes through a descriptor, not by hand, and named it v0.7.0: a card was added (step 1b), which is MINOR under DDD-dec-82. Emil then ran it:
release: refused at step 1: releases/v0.7.0.yaml is not on origin/main (87db443b8671); a release is cut only from a landed descriptor
Whether v0.7.0 is a pre-release was asked but not answered. Write `prerelease: true`, as v0.6.0 did, since DDD-dec-74 keeps the method "ready to try (preview)", and mark it as a choice for Emil to confirm when he ratifies the head.
Sources
CONTRIBUTING.md §Releases; GOVERNANCE.md §Releases; spec/release-format.md; DDD-dec-75, -82, -84, -104; releases/v0.6.0.yaml as the model; tools/canon/README.md (canon changelog, ratify, release). Read what landed since v0.6.0: `git log v0.6.0..main`, DDD-dec-114 to -118, and PRs #63 to #68.
The work
Predict before each operation. Stop at every gate.

1. Confirm the version from the rules, not from this prompt. Since v0.6.0, step 1b's card was added (DDD-dec-118), so the release is MINOR: v0.7.0. Check that no other change in the range moves a step's register, which would also be MINOR, and that nothing calls for more. If the rules give something else, stop and say so.
2. Commit 1, the head Emil ratifies: releases/v0.7.0.yaml in format 2, modelled on v0.6.0.yaml.
   * basis: DDD-dec-114 to -118, and anything else the range carries, each with a comment line.
   * A title, and a summary written for readers: one idea per sentence, British spelling, registers stated (what is ruled, what is [PROPOSED], what is projected). Cover the PDLC and the SDLC as applications (#64), specification feasibility with grants and roles (#63), product-cli's definition (#65), sdlc.md O-8 and O-9 (#66), and step 1b with DDD-flow-01 to -04 scoped to the PDLC (#68). Say plainly that the step and the specs are [PROPOSED].
   * prerelease: true, marked as above. Then generate its CHANGELOG.md section with `canon changelog`; never edit CHANGELOG.md by hand. Run the releases gate and `canon changelog --check`.
3. Commit 2: `canon ratify v0.7.0`, which fills ratified_head with commit 1 and changes nothing else.
4. Run scripts/ci.py and canon's checks as CI runs them. Push, open the pull request, wait for green CI, and report the pull request, its head, and the steps: land it, then `canon release v0.7.0 --plan` and `canon release v0.7.0` from main. Stop. Do not land, and do not run canon release.
