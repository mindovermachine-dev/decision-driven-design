# Prompt — protect main, 2026-11-03

The session prompt, verbatim, as given at invocation. Per `DDD-dec-20`, this file is committed
before any other file changes, so the session's scope is fixed at arrival.

---

New session: protect main, 2026-11-03, in mindovermachine-dev/decision-driven-design,
from main at 5ccdf41. Open an issue for it; Refs #N on every commit. Commit prompt.md and
bootstrap.md under meta/sessions/2026-11-03-protect-main/ first.

Emil's ruling, verbatim (claude.ai question dialog, 2026-11-02):
Q: "Protecting main: which rulesets should repo-standard.yaml declare? DDD-dec-81 ruled
only Signed Commits, so this is a new decision."
A: "Varve's set (Recommended)" (option text: "trunk (no deletion or force-push, required
check pipeline (devcontainer), no bypass), land/**, v* tags restricted to you, plus
Signed Commits")
Emil, 2026-11-03: "lets do both" (this session and the canon CLI's Gate 3, in parallel).

Context: the repository has no rulesets today. The authority-profile work and two edits to
a cut release's descriptor reached main by direct push.

1. File the ruling as DDD-dec-108, after re-checking every branch of both repositories.
   The canon CLI session takes 109 onward. 108 adds to DDD-dec-81 and does not supersede
   it. Its basedOn includes DDD-dec-78, DDD-dec-84 and DDD-dec-81. It names canon land
   (DDD-dec-101) as the landing mechanism.
2. .github/repo-standard.yaml: add three rulesets beside Signed Commits.
   - trunk, on ~DEFAULT_BRANCH:
     - rules: deletion, non_fast_forward, and required_status_checks with the single
       context "pipeline (devcontainer)" and the integration id of GitHub Actions. Read
       that id from main's head check runs (it was 15368).
     - strict policy false; bypass_actors: []
     - add the comment that renaming the job means renaming it here.
   - land, on refs/heads/land/**: creation, update, deletion and non_fast_forward.
     Bypass: User 2194785 (Emil, read from the author of main's head).
   - Release Tags, on refs/tags/v*: creation, deletion and non_fast_forward.
     Bypass: User 2194785.
   - Signed Commits: check whether its Integration bypass (1236702, copied from Varve)
     is the right id for this organisation's Claude app, and whether it is still
     needed, now that session commits are verified. Report what you find; change it
     only if Emil rules.
3. GOVERNANCE.md: state the four rulesets in Varve's table form. In "How work reaches the
   trunk", name the mechanism:
   - canon land <pr> pushes land/<name>
   - CI goes green on that SHA
   - canon land <pr> --main fast-forwards main
   - the trunk ruleset refuses anything else
4. Editorial, in the same branch: replace the two README rows for DDD-floor-01 and
   DDD-agent-01 with the corrected text below. Their old wording claimed more than the
   claims:
   | **One way escapes happen.** Work beyond an actor's capacity escapes where the
   decisions it sheds carry no verifier; overflow alone produces retries, not escapes.
   This is sufficient for escape, not the only cause, and it has been reproduced on toy
   actors so far | `DDD-floor-01` | **Reported** (toy actors) |
   | **Agents that drift less.** Long-running agent drift is decisions made with no
   basis. Grounding an agent in an external claim graph, with a basis cited per
   decision, is claimed to reduce drift compared with carrying instructions in context.
   This repository is run that way | `DDD-agent-01` | Projected |
5. Predict before you run. Validate the YAML. Push, wait for green CI, report the head
   and the canon land commands, and stop. Applying the rulesets is Emil's act, after the
   landing. Report the exact apply command and a check that proves a direct push to
   main is refused.
