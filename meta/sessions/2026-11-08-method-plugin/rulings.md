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
