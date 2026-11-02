# Rulings — ready to try, 2026-11-02

Every ruling Emil gave in this session, verbatim, in the round it was given. Claude's readings
are marked `UNVERIFIED — Emil review` where Emil did not confirm them.

## Round 1 — 2026-11-02, 09:32 CET

Emil answered the four questions of Claude's proposal (`prompt.md`) in one message:

> 1. yes ready to try 2. could Varve work ? 3. The method 4. we adopt the full as it applies to us.

| Q | Question asked | Answer | Filed as |
|---|---|---|---|
| 1 | Positioning: "ready to try (preview)", or something else? | "yes ready to try" | `DDD-dec-74` |
| 2 | The worked example for the quick start (not Phoenix) | "could Varve work ?" — a question, not a ruling | G4, open |
| 3 | Versioning: the method, the claim graph, or the upstream pin? | "The method" | `DDD-dec-75` |
| 4 | Stewardship: the standard in full, or with recorded deviations? | "we adopt the full as it applies to us" | `DDD-dec-76` |

### Claude's readings — UNVERIFIED — Emil review

- **Ruling 3.** "The method" is read as: the repository's version number moves when the method
  moves, not when a claim's status or the upstream pin moves. How a method change maps to MAJOR,
  MINOR and PATCH is not ruled; it is G6.
- **Ruling 4.** "As it applies to us" is read as Varve's form: every item of the standard applies
  unless a ruled applicability table states why it does not, or how it applies differently. The
  table is `applicability.md`, G3. Until G3 is ruled, no item is booked as a deviation.

### Question 2 — Claude's answer, `[PROPOSED]`

Carried to Emil in the reply that delivered G2. Recorded here when Emil rules on it.

## Round 2 — 2026-11-02

Given by Emil through the question dialog in the claude.ai conversation. The questions and
answers below are verbatim. Where the dialog showed option text with an answer, that text is
recorded too.

> Q: "G4 — worked example for the quick start: Varve, scoped to the HTTP slice of its own quick
> start (write, delete, read, read as-of, commit feed — no RDF needed), pinned at a release tag,
> and stated as the subject of design, not a dependency?"
>
> A: "Varve, scoped (Recommended)"

> Q: "G3 — deviations from the stewardship standard: merging stays your ratification act for
> anything that files or supersedes a decision (editorial changes may reach main without it),
> and canon sessions may hold a branch open only for as long as their gates. Accept both, stated
> as scoped deviations in GOVERNANCE.md?"
>
> A: "Accept both (Recommended)"

> Q: "G3 — licence: the organisation's principles call for CopyLeft, but this repository is CC
> BY 4.0 (text) with Apache-2.0 (code). Which way?"
>
> A: "Move to copyleft" (option text: "CC BY-SA 4.0 for text, MPL-2.0 for code, as Varve did;
> filed as a decision")

> Q: "G6 — SemVer for the method: stay below 1.0 until all ten steps are ruled; MINOR when a
> step card is added or its register moves (proposed → ruled → reported, or back to open); PATCH
> for editorial changes; MAJOR after 1.0 when a ruled step is superseded incompatibly. The first
> release continues the existing tags as v0.5.0, and the 4.x CHANGELOG headings stay as history.
> Rule it?"
>
> A: "As proposed (Recommended)"

> Q: "The rest of G3 in applicability.md was not in those questions. It covers: Maturity
> Exploring → Experimental; one decision moving the root reports and migration/ to meta/history/
> and validate-core-order.py to scripts/, with a root shim for one release; Varve's signing
> exception; a downstream board WIP limit of 2; Discussions on; and settings in
> repo-standard.yaml. Rule the rest of the table as proposed?"
>
> A: "Rule rest as proposed (Recommended)"

| Gate | Ruled | Filed as |
|---|---|---|
| G4 | Varve, scoped to the HTTP slice of its quick start, pinned at a release tag, the subject of design and not a dependency | see the decisions index below |
| G3 | The two scoped deviations (items 4 and 5) | idem |
| G3 | Copyleft: CC BY-SA 4.0 for text, MPL-2.0 for code | idem |
| G3 | The rest of `applicability.md` as proposed, including the root move | idem |
| G6 | The SemVer mapping, with v0.5.0 first and the 4.x headings kept as history | idem |

### Round 1 readings confirmed

Emil's message carrying Round 2 states that these rulings also confirm the readings flagged
`UNVERIFIED — Emil review` in Round 1. These are the reading of ruling 3 in `DDD-dec-75` (the
version moves when the method moves) and the reading of ruling 4 in `DDD-dec-76` (adoption is the
default, and each departure is stated with its reason in a ruled applicability table). Both are
confirmed as of Round 2. The decisions themselves are not edited; their notes keep the flag as
it was written, and this entry is the confirmation.

### Copyright for the relicensing

Checked on 2026-11-02 against `origin/main` at `2b6e4a7`, with
`git log --format='%an <%ae>'`. Every author is Emil or an AI working under Emil:

| Commits | Author |
|---|---|
| 197 | `Claude <noreply@anthropic.com>` |
| 36 | `Emil Klein <emk@delegate.dk>` |
| 25 | `Claude (Emil) <claude+emil@okkels-klein.dk>` |
| 17 | `Emil Klein -  Claude Code AI <emk@delegate.dk>` |
| 17 | `Claude <hannibal.okkels@gmail.com>` |
| 10 | `Emil (via agent) <hannibal.okkels@gmail.com>` |
| 8 | `Emil Klein -  Claude Code AI <emil@okkels-klein.dk>` |
| 6 | `Emil Klein <emil@okkels-klein.dk>` |

Committers are the same identities, plus `GitHub <noreply@github.com>` on Emil's merges. Every
`Co-Authored-By` trailer names a Claude model. No third-party contributor holds copyright in the
repository, so moving to copyleft needs no consent beyond Emil's.
