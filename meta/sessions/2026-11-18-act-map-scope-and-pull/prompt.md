Work issue #80 in mindovermachine-dev/decision-driven-design:
"The act map, scope and pull: what they are, and how step 1 starts from them".

Read first, in this order
1. Issue #80, in full. It is the charter. Its "State at opening" section is part of it.
2. AGENTS.md and meta/way-of-working.md.
3. The two session records on the archive branch claude/pull-and-scope-2026-11-18
   (head 47cf4cc when this prompt was written; check it):
   meta/sessions/2026-11-17-act-map-and-process/ and meta/sessions/2026-11-18-pull-and-scope/.
   rulings.md in each is the ruled ground. proposals-2.md and survey.md in the first are material.
4. The ground files the issue names, and canon at the tag in graph/upstream.yaml.
   Fetch upstream at that tag. Never cite an id or a canon sentence from memory.

Set up before any other change
- Branch from main. Name it claude/act-map-scope-and-pull-<date>.
- Create meta/sessions/<date>-act-map-scope-and-pull/ with prompt.md (this prompt, verbatim)
  and bootstrap.md (parameters, gates, base and archive heads, the decision-id check across
  every branch of both repositories, deviations). Commit them first.
- Write predictions.md before each operation, and record the result against each prediction.

The archive branch
- It is a source to copy from, never a branch to merge or rebase. Its commits carry no Refs line.
- Do not delete it and do not push to it. It keeps DDD-dec-122 and DDD-address-06 to -08
  visible as taken until this branch is pushed.
- Deliverable 1: copy the two session directories from it as they stand, in one commit that
  names the source commit. Reword nothing in them. Do not copy its claims, its decision, its
  two method sentences or its row in meta/sessions/README.md. Those are written by this session.

Rulings already given (do not re-ask; they are in the two rulings.md files and in #80)
- Ids: the act map, a second act map, and a process keep DDD-address-06, -07, -08, and the
  decision keeps DDD-dec-122, each amended before landing. New claims take DDD-address-09
  onwards. Each amended claim says in its notes that it was first drafted on 2026-11-17 on a
  branch that did not land and was amended on the rulings of 2026-11-18.
- Everything else listed under "Ruled before this issue was opened" in #80.
"Stated, not ruled" in #80 is not ruled. Propose it; do not treat it as ground.

Work the deliverables in the issue's order, and stop at the gates
- Deliverables 2 to 5, then STOP at G1. Give me each proposal with its weakest point first,
  its falsifier, what it breaks, and which filed claim or ruling it rests on, or that it rests
  on none. State the effect on T2b's pre-registration, on step 1b's kinds and on
  DDD-address-02's region before any card changes. I rule each proposal and where it is filed.
- Deliverable 6 only after my G1 rulings. Change ruled material by supersession, never by
  rewriting. Then STOP at G2. Open a pull request against main and name the head to ratify.
  Merging is mine.

Discipline
- Every claim is Ruled, [PROPOSED] or [OPEN]. You propose; I rule. Nothing self-ratifies.
- Mark reasoning I have not confirmed as "UNVERIFIED — Emil review".
- Projected means derived and unexercised. Reported means exercised. Do not fuse them.
- Record my rulings in the session's rulings.md when I give them, in my words, with the time.
  Record corrections, including your own, with attribution.
- Carry one worked example through every part of the pull procedure, and test each part
  against a junior engineer's first contact. Phoenix is never the worked example and is never
  named.
- Human-read .md files start with the information itself, not with a description of the file.
  British spelling. One idea per sentence. Tables for structure, prose for arguments.
- Use canon terms exactly as registered. Do not coin Danish terms.
- The four states are credited to GitHub user pjarnhus. Write the handle without an @.
  Only the four names are his. The mapping to canon is ours, made from the names.

The gate that must pass
- Run the whole validate workflow locally before every push, not only scripts/ci.py:
    python3 scripts/ci.py
    cd tools/canon
    dotnet test --project tests/Canon.Tests -c Release
    dotnet run --project src/Canon -c Release -- changelog --check
    dotnet run --project src/Canon -c Release -- issue-refs --basis
    dotnet run --project src/Canon -c Release -- check --compare
- Every commit carries "Refs #80" as its own line. Every commit that changes core/ also
  carries a "Basis:" line naming the claim and decision ids it rests on, and names the ids it
  touches.
- After each push, look at the workflow run for that commit and report its result. Do not
  report a gate as passing from a local run alone.
- The "Agent review" check fails today on a build error in tools/canon (NU1004, a package
  lock file mismatch). The branch does not cause it. Report it; do not fix it here.

Out of scope
- Building the lifecycle's index of determinables. Changing any act or any lifecycle data
  under applications/. Mantle. Canon in the principle repository. tools/canon.
- Cutting a release.

If the ground for a ruling is missing, ask me. Do not fill the gap.
