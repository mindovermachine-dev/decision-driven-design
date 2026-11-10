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

**Not filed.** Round 27 is recorded here and is not filed as a decision. Whether to file it is
Emil's call (`findings.md`).
