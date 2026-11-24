# Rulings — an installable plugin for the method, 2026-11-08

Emil's Round 27, verbatim, from the claude.ai conversation of 2026-11-08. The round number is that
conversation's. The 2026-11-07 session's `rulings.md` has a Round 27 of its own, with different
content ("flow time"), so cite this round together with this record ("Round 27, method-plugin
`rulings.md`").

The blockquote is copied from `prompt.md` byte for byte, apart from the quote markers. It includes
the prompt's framing sentence (what Claude flagged and recommended), because the answers respond
to it. Each answer is the option Claude marked Recommended, and the option text is Claude's
wording, which Emil chose.

## Round 27, verbatim

> Round 27, claude.ai conversation, 2026-11-08. Emil: "For the method part we should have a skill you can install". Claude flagged that a skill copying the method's text would drift as steps are ruled and superseded, and recommended a thin skill that reads the repository at a pin. Then:
> Q: "Who installs the skill, and from where?" A: "From the repo, for practitioners (Recommended)" (option text: "A Claude Code plugin in decision-driven-design (a skill plus marketplace entry), installable by anyone adopting the method; versioned with the method")
> Q: "What does the skill cover?" A: "The whole method (Recommended)" (option text: "All steps, each run from its step card; refuses to treat [PROPOSED] steps as ruled; step 1 and the demand-flow step first in practice")
> Q: "How does the skill hold the method's content?" A: "Thin, reads the repo at a pin (Recommended)" (option text: "The skill carries procedure and discipline; step cards and canon are fetched from the repository at the pinned version, so it never drifts")

## What it rules, and what it leaves open

**Ruled:**
- **Form and place.** The plugin is a Claude Code plugin in this repository, a skill plus a
  marketplace entry, for anyone adopting the method. It is versioned with the method.
- **Scope.** The whole method: every step, each run from its card. The skill refuses to treat a
  `[PROPOSED]` step as ruled. In practice, step 1 and the demand-flow step come first.
- **How it holds content.** Thinly. The skill carries procedure and discipline. The step cards
  and canon are fetched from the repository at the pinned version.

**Not ruled, and proposed in `design.md`:** the plugin's and the marketplace's names; how
"versioned with the method" maps onto the plugin's `version`; how the skill reaches the
repository; and how a step that is `[PROPOSED]` is run without being treated as ruled. These are
Claude's proposals, `UNVERIFIED — Emil review`.

**Not filed in Round 27.** It was recorded and not filed as a decision. Round 28 files it, as `DDD-dec-121`.

## Round 28, verbatim

Given in this session on 2026-11-11: Emil's answers in Claude's question dialog on claude.ai, with
his instructions. "Round 28" is this record's next round. The 2026-11-07 session's `rulings.md`
also has a Round 28, with different content, so cite this one as "Round 28, method-plugin
`rulings.md`". The blockquote is the message byte for byte, apart from the quote markers.

> Record this message verbatim in rulings.md as the next round, and predict before each operation. These are my answers in Claude's question dialog on claude.ai:
> Q: "The plugin session built past its design gate (F-1). Review design.md before landing, or accept design and build together?" A: "Accept both (Recommended)" (option text: "Design and build are separate commits and the design matches the charter; record the missed gate as a finding")
> Q: "F-3: plugin version = the method pin it reads, with +p.N for plugin-only changes?" A: "Yes (Recommended)" (option text: "0.7.0 now; 0.7.0+p.1 for a plugin fix; 0.8.0 when it re-pins to v0.8.0. Claude Code updates on any version-string change")
> Q: "F-4: Round 27 is recorded but not filed as a decision. File one (next free id, DDD-dec-121)?" A: "File it (Recommended)" (option text: "Thin skill reading at a pin, one entry skill, the version scheme, and the README claiming discipline rather than step quality")
> Q: "Also fix F-9 (root README still says "v0.5.0 is a preview") in this PR, and open the pull request?" A: "Fix F-9, open the PR (Recommended)" (option text: "The session already edits the root README; I open the PR once it pushes")
>
> 1. F-1: record the missed design gate as a finding. Design and build are both accepted.
> 2. F-3: the version scheme is ruled. State it in design.md, in the plugin's README and in the decision below.
> 3. F-4: file one decision for Round 27 and this round. It covers the thin skill reading the method at a pin; one entry skill; the version scheme; and what the plugin claims. The claim is discipline, not better step execution: on step 1 the evals show no gain (0.81 to 0.95 with the plugin, 0.86 to 0.90 without), while the refusals and the unreachable case show the gain. The redo branch claude/zealous-ptolemy-3txf8k holds DDD-dec-119 and -120, so the next free id should be 121. Re-check every branch just before you commit and again just before you push, and take the next free id.
> 4. Make the plugin's README say the same about what the plugin claims, citing the eval table in findings.md.
> 5. F-9: correct the root README's opening line to the current release, v0.7.0, a pre-release. Change nothing else in that line's paragraph.
> 6. Run scripts/ci.py, the plugin gate, `claude plugin validate` (with --strict), and canon's checks as CI runs them. Push, wait for green CI, and report the new head. Claude will open the pull request. Stop. Do not land.

## What Round 28 rules

- **F-1.** The design and the build are both accepted. The missed design gate is recorded as a
  finding (`findings.md`, F-1).
- **F-3.** The version scheme is ruled: the plugin's version is the method pin it reads, without
  its `v`. A plugin-only change at the same pin takes `+p.N`. A re-pin takes the new pin's version.
- **F-4.** Round 27 and this round are filed as one decision, `DDD-dec-121`. It covers the thin
  skill reading at a pin, the one entry skill, the version scheme, and what the plugin claims:
  discipline, not better step execution.
- **F-9.** The root README's opening line names the current release, `v0.7.0`, a pre-release.
  Nothing else in its paragraph changes. Emil opens the pull request.

## Round 29, verbatim

Given in this session on 2026-11-19. "Round 29" is this record's next round. Other records have
rounds with the same number, so cite this one as "Round 29, method-plugin `rulings.md`". The
blockquote is the message byte for byte, apart from the quote markers.

> Ruling: #74 is held. It does not land at v0.7.0. Record this message verbatim in the
> session's rulings.md, as a new round, before you do anything else.
>
> The reason. main is now at dc8b737. #84 landed today and changed step 1: it starts from
> scope and pull (DDD-address-06 to -11, DDD-dec-122), and method/01 to method/10 changed.
> The plugin reads the step cards at v0.7.0, which is the main from before that. Landing it now
> would ship a plugin that teaches a step 1 I have superseded.
>
> What changes when the hold lifts. I will cut a release that includes #84 and tell you the
> tag. Then, under DDD-dec-121's own rule that a re-pin is a new plugin version:
>
> - re-pin the plugin to that tag;
> - rework the step-1-small eval. Its axes-first grader passes a reply that declares ground
>   axes first. Step 1 now starts with scope, then the pulls;
> - rework the demand-flow-start eval against DDD-address-10, which reads a kind of demand as
>   a position on a declared ground axis;
> - re-run every eval and replace the table in the plugin's README and in findings.md. Keep
>   the old table in the record as the v0.7.0 result. Do not overwrite it;
> - rebase onto main and resolve the conflict.
>
> What to do now, and nothing more:
>
> 1. Record the ruling, as above.
> 2. Fetch main and read what #84 filed. Then give me your own list of what in the plugin, its
>    evals, its check and DDD-dec-121 is affected. I listed three things. Tell me what I
>    missed and where I am wrong. Mark anything you cannot confirm as UNVERIFIED.
> 3. Tell me whether DDD-dec-121 needs amending before it lands, or whether its version scheme
>    already covers this. It is unlanded, so an amendment in place is open to me. Propose; do
>    not amend.
> 4. Check that DDD-dec-121 is still free on every branch of both repositories.
> 5. Commit the record with Refs #72, run the whole validate workflow locally, and push. Do
>    not rebase yet, and do not re-pin. Report and stop.

## Round 30, verbatim

Given in this session on 2026-11-19, on the Round 29 report. Cite it as "Round 30, method-plugin
`rulings.md`". The blockquote is the message byte for byte, apart from the quote markers.

> Rulings on your Round 29 report. Record this message verbatim as Round 30 before you act.
>
> 1. The release that carries #84 is v0.8.0. It falls under the first row of DDD-dec-82's
>    table: a ruled step superseded incompatibly is MINOR below 1.0. This confirms that row,
>    which DDD-dec-82 flags as an unconfirmed reading. Do not edit DDD-dec-82. The release is
>    cut in its own session, after #73 and #87 land. You do not cut it.
>
> 2. DDD-dec-121: amendments 1 to 4 are accepted. Amendment 5 is declined: #84 is the occasion,
>    not the basis. Name DDD-dec-122 in the notes instead. Amend in place, since the decision
>    is unlanded, and say in its notes that it was amended before landing and in which round.
>
> 3. The skill: accepted. A generic rule that a superseding section governs where it differs,
>    holding no card text. More than one register on a step. The demand-flow wording brought in
>    line with DDD-address-08 and -10. One source for the pin, read by the graders, the
>    scaffold, the descriptions and both READMEs.
>
> 4. The check that the pin equals the newest version in releases/: accepted in principle.
>    Before you build it, tell me how the evals run for a re-pin made in the same change as a
>    release, when the descriptor is on the branch and the tag does not exist yet. Propose;
>    do not build the check until I answer.
>
> 5. Step 1's order: scope first, then the pulls. Ground axes are still declared before any
>    occurrence gets a position. Rework step-1-small on that reading: the prompt, the register
>    grader, the address grader, and a grader for the pull statements. Strengthen the
>    unreachable case for the new first part.
>
> 6. The "source of pull" question in SKILL.md: show me the sentence and your proposed
>    replacement at the gate. Do not change it yet.
>
> Do now: items 2, 3 and 5, and the rebase onto main. Do not re-pin, do not run the evals, and
> do not change the version. The pin stays v0.7.0 until I tell you v0.8.0 is tagged. Run the
> whole validate workflow, push, and report: the new head, both required checks by their check
> names, your answers to 4 and 6, and what remains for the re-pin. Then stop.

## Round 31, verbatim

Given in this session on 2026-11-19, on the Round 30 report. Cite it as "Round 31, method-plugin
`rulings.md`". The blockquote is the message byte for byte, apart from the quote markers.

> Rulings on your Round 30 report. Record this message verbatim as Round 31.
>
> 1. I am not approving 6657942. #74 stays held. That is not a finding against the work.
>
> 2. Item 4: your first proposal is accepted, with one change. The list of trees must not be a
>    fixed three directories. Derive it from what the skill reads, or make the check fail when
>    the skill reads a file outside the list. Tell me which you choose when you build it.
>    Build it at the re-pin, not now.
>
> 3. Item 6: not ruled. Leave the sentence as it is. Two notes for when it comes back. A reason
>    for keeping, adding or dropping a kind is not a pull: a pull is a gap between two states
>    of a determinable (DDD-address-09), so do not use the word for it. And "the kind is read
>    from the item's position alone" is right.
>
> 4. The method is changing again. Issue #88 makes the method one thing, making an act map, in
>    four moves, with steps 2 to 10 recorded on the acts and decisions. It starts from an act
>    or a decision, not from the edge. The step-1-small rework you did on my item 5 will be
>    redone against what #88 files. Keep it as it is until then. Do not rework it now.
>
> 5. v0.8.0 is cut after #88 lands. I will tell you when it is tagged. Until then, do nothing
>    further on this branch. Record this round, run the whole validate workflow, push, and
>    stop. If the push moves the head, name the new one, and say that it is not for approval.

## Round 32, verbatim

Given in this session on 2026-11-24. Cite it as "Round 32, method-plugin `rulings.md`". The
blockquote is the message byte for byte, apart from the quote markers.

> The hold on #74 is lifted. Record this message verbatim as Round 32 before you act.
>
> v0.8.0 is tagged, on main at e57c5ee. Since your last round the method changed again, as
> Round 31 said it would. #89 landed DDD-dec-124: the method is one thing, making an act map,
> in four moves, each [PROPOSED]. The live card is method/make-an-act-map.md. The numbered step
> cards stay, each marked not live. Read DDD-dec-124, the live card, method/README.md and
> releases/v0.8.0.yaml at the tag before anything else. Read draft D-1 in
> meta/sessions/2026-11-20-method-as-act-map/breaks.md, and the note on issue #72.
>
> Stop at a gate before you change the skill. Report, with predictions written first:
>
> 1. What the plugin becomes when it reads one card and not ten. What /ddd-method:run offers,
>    what it refuses, and how it treats a not-live card that a user asks to run. Name the
>    weakest point first, and give a falsifier and what it breaks.
> 2. Which of your Round 30 work survives as it is (the superseding-section rule, more than one
>    register, one source for the pin), and which is redone (the step-1-small rework, the
>    demand-flow-start case, the unreachable case).
> 3. The eval set you propose for four moves: which cases stay, which go, which are new.
> 4. What in DDD-dec-121 must change before it lands. It is unlanded, so an amendment in place
>    is open to me. Propose; do not amend.
> 5. Whether main's 47 new commits conflict with the branch beyond meta/sessions/README.md.
>
> Then, on my rulings:
> - re-pin to v0.8.0, everywhere the pin check looks;
> - rewrite the skill and the evals as ruled;
> - build the pin check ruled in Round 31, with the list of trees derived from what the skill
>   reads, or failing when the skill reads outside it;
> - re-run every eval. Add the v0.8.0 table beside the v0.7.0 one and keep the old one;
> - apply the "source of pull" sentence only if it still exists after the rewrite, and without
>   calling a reason for a choice a pull;
> - rebase onto main, with the id check before commit and before push. DDD-dec-124 is now the
>   highest on main.
>
> Known and not ruled: issues #90 to #93 propose amendments to the live card, and #93 a
> different order. Build for the card at v0.8.0. Do not build for them.
>
> Work on a full clone. The gate is the whole validate workflow. At the end, name the head to
> ratify with both required checks by their check names, and stop.

## Round 33, verbatim

Given in this session on 2026-11-24, on the Round 32 report. Cite it as "Round 33, method-plugin
`rulings.md`". The blockquote is the message byte for byte, apart from the quote markers.

> Rulings on your Round 32 report. Record this message verbatim as Round 33 before you act.
>
> Item 1: accepted, with two changes.
> - The refusal of quick-start.md becomes general: refuse to offer any page that runs a
>   not-live card. Do not name the file in the skill.
> - Where an old step's content now sits is read from the live card at the pin. The skill
>   holds no such mapping in its own text.
> The skill reads a not-live card's section only where the live card cites it, and says that
> it is doing so.
>
> Item 3: accepted. Say in the plugin's README, beside the table, that the evals cover moves 1
> to 3 and that move 4 and the edge pass are not tested.
>
> Item 4: amendments 1 to 3 and 5 to 7 are accepted. Amendment 4: [yes, Round 27's "step 1 and
> the demand-flow step first" lapses under DDD-dec-124 / no]. Amend DDD-dec-121 in place.
>
> The pin-tree check: derive the list, as you propose.
>
> The live card pointing to a not-live card for the pull statement's form is a defect in the
> card, not in the plugin. Do not fix it here. Name it in findings.md.
>
> Now build, in the order Round 32 gave: re-pin to v0.8.0, rewrite the skill and the evals,
> build the pin check, re-run every eval with the v0.8.0 table beside the v0.7.0 one, rebase
> onto main with the id check before commit and before push. Work on a full clone. The gate is
> the whole validate workflow.
>
> Stop when it is done. Report the head to ratify in full, both required checks by their check
> names, the eval table, and anything the evals showed that the card or the skill should not
> be doing.

**Amendment 4 is not answered.** Its text, "[yes, … / no]", gives both options and chooses neither.
It is recorded as given and treated as not ruled. It is not applied to `DDD-dec-121`
(`findings.md`, Round 33).

## Round 34, verbatim

Given in this session on 2026-11-24, on the Round 33 build report. Cite it as "Round 34,
method-plugin `rulings.md`". The blockquote is the message byte for byte, apart from the quote
markers. It answers Round 33's amendment 4, which was left unchosen.

> Rulings on your build report. Record this message verbatim as Round 34 before you act.
>
> Amendment 4: yes. Round 27's "step 1 and the demand-flow step first" stays verbatim in
> DDD-dec-121, with a note that it lapses under DDD-dec-124, since neither step is live.
>
> C-2: the Round 33 rule was too tight. The skill may read a not-live card's first line and
> its superseding section, the part DDD-dec-124 filed above the rule line. It never reads or
> runs what lies below that line, except a section the live card cites. This supersedes the
> narrowing you made for S-1. Do not change the live card.
>
> E-1: the pull-statement rubric accepts a gap marked missing with its reason. Do not supply
> the states in the prompt.
>
> S-2: left as it is.
>
> Then: re-run the two cases these rulings change, not-live-card and act-map-small, both arms,
> three runs each. Report the new figures beside the ones you have, and keep both in
> findings.md. Update the table in the README and the numbers in DDD-dec-121. Run the whole
> validate workflow on a full clone, push, and name the new head to ratify with both required
> checks by their check names. Then stop.
