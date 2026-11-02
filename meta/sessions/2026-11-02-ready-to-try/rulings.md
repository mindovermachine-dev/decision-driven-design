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

### Round 2 filed — 2026-11-02

Added after filing; the Round 2 entry above is not edited. Its "Filed as" column reads:

| Gate | Ruling | Decision |
|---|---|---|
| G4 | Varve, scoped | `DDD-dec-77` |
| G3 | The two scoped deviations | `DDD-dec-78` |
| G3 | Copyleft | `DDD-dec-79` |
| G3 | The root move, with paths resolving at the record's commit | `DDD-dec-80` |
| G3 | The rest of the applicability table | `DDD-dec-81` |
| G6 | The SemVer mapping | `DDD-dec-82` |

Claude's readings beyond the dialog's words are flagged `UNVERIFIED — Emil review` in the notes
of `DDD-dec-79` to `DDD-dec-82`.

## Round 3 — 2026-11-02

Given by Emil through the question dialog in the claude.ai conversation, after an independent
review of the G3 execution at `227630b` (16 commits verified, CI green on push and pull
request). The questions and answers are verbatim. Option text is recorded where the dialog
showed it.

> Q: "R-9 — GitHub reports the licence as NOASSERTION because LICENSE.md sits beside LICENSE.
> Renaming LICENSE.md makes GitHub detect MPL-2.0 (tested with licensee). Which?"
>
> A: "Rename to LICENSING.md (Recommended)" (option text: "Stays at the root beside LICENSE and
> NOTICE; GitHub detects MPL-2.0")

> Q: "R-10 — the release-head guard (DDD-dec-39) exists only in the principle repository. The
> v0.5.0 release descriptor here needs either a port of the guard or a stated manual check.
> Which?"
>
> A: "Port the guard (Recommended)" (option text: "Copy check-release-head.py and the release
> format into this repo, as a gate in ci.py, before v0.5.0")

> Q: "R-11 — the standard asks for every commit to reference an issue (Refs #N). This session
> has no issue. Which?"
>
> A: "Open an issue now (Recommended)" (option text: "The session opens one issue for itself;
> commits from here carry Refs #N; enforcement in ci.py follows later")

> Q: "G3 review — approve the G3 execution as delivered and proceed to G5? This also accepts
> DDD-dec-82's two flagged readings: an incompatible change to a ruled step before 1.0 is MINOR,
> and 'editorial' means wording that changes no ruling, plus links and tooling. It also accepts
> the description and topics drafted in repo-standard.yaml."
>
> A: "Approve, proceed to G5 (Recommended)" (option text: "Readings and repo-standard wording
> confirmed")

### Confirmations

- **`DDD-dec-82`.** Both readings flagged `UNVERIFIED — Emil review` in its notes are confirmed
  as of Round 3. An incompatible supersession of a ruled step before 1.0 is MINOR. "Editorial"
  means wording that changes no ruling, plus links and tooling. The decision is not edited; this
  entry is the confirmation.
- **`.github/repo-standard.yaml`.** The description and topics are confirmed. The file's
  `UNVERIFIED — Emil review` comment is removed as an editorial change citing this round.
- **G3.** The execution at `227630b` is approved, and the session proceeds to G5.

### Reviewer's finding (editorial)

The independent review found that `scripts/ci.py` crashes with a traceback in the How gate when
`ssh-keygen` is absent, and that `scripts/requirements.txt` lists only Python packages. The fix
checks for `ssh-keygen` first and fails with a message naming it, and lists the system
dependencies.

## Round 4 — 2026-11-02

Given by Emil through the question dialog in the claude.ai conversation, after an independent
review of `3797364`: 27 commits verified, and CI red on `releases` only, with `ratified_head`
missing, as P-25 predicted. The questions and answers are verbatim, with option text where the
dialog showed it.

> Q: "R-14 — the authority-profile session (claude/bold-franklin-i7b16g) has nothing filed yet,
> but its plan names DDD-dec-77 and 78. This branch already filed and pushed 77–82 and 84; 83 was
> left free. Where should the authority session file?"
>
> A: "From 85 onward (Recommended)" (option text: "83 is recorded as never used; the authority
> session re-checks and starts at 85")

> Q: "The v0.5.0 descriptor sets prerelease: true, flagged UNVERIFIED. This matches 'ready to try
> (preview)' and Varve's preview releases. Keep it?"
>
> A: "Keep prerelease: true (Recommended)" (option text: "GitHub marks v0.5.0 as a pre-release")

### What follows from it

- **`DDD-dec-83` is never used.** It is recorded as such in `bootstrap.md` (amendment 4) and in
  `successor-items.md` (R-14 closed). No decision is filed for it: ids are never reused, and a gap
  is not a defect. The authority-profile session re-checks and starts at `DDD-dec-85`.
- **`prerelease: true` is confirmed.** The descriptor's `UNVERIFIED — Emil review` comment on it
  is replaced by this confirmation, as an editorial change citing Round 4.

## Editorial instruction — 2026-11-02, after PR #43 merged

Given by Emil in the claude.ai conversation, verbatim:

> "The where this is the wrong tool part of our readme needs to change - it should lead with all
> the reasons why someone should use it. And the one about it hasnt been show to work should be
> last"

Carried out as an editorial change to `README.md`, with no ratification act, landed on `main` by
fast-forward after CI was green. The text came with the instruction in two blocks:
- a new opening with a "Why use it" table, replacing the old "What it gives you" section and
  "Weakest point" paragraph;
- "Where it is the wrong tool", moved after "Quick start", with "shown to work" as its last
  bullet.

Every id cited in the new text was checked before commit against the live claim files, at the
pin `v5.15.2` (`084bce7`, equal to upstream `main`), and in this repository:

| Id | Where | Status | Table says |
|---|---|---|---|
| `DDD-ground-06`, `DDD-ground-01`, `DDD-floor-02`, `DDD-hyp-05`, `DDD-agent-01` | upstream, pinned | projected | Projected |
| `DDD-floor-01` | upstream, pinned | reported | Reported |
| `DDD-address-01`, `-02`, `-03` | here | projected | Projected |
| `DDD-dec-62`, `DDD-dec-74` | here | ruled decisions | Ruled |

Readings — Claude, `UNVERIFIED — Emil review`, recorded and not edited into the README:
- **`DDD-floor-01`.** It is reported on toy actors only (its region). It states overflow ∩ open as
  sufficient for escape, not necessary.
- **`DDD-agent-01`.** It claims that grounding "reduces drift relative to context-carried
  instruction". The README row says "is the remedy", which is stronger.
