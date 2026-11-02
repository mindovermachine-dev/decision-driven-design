# v4.0 Reconciliation Report

Build record for the v4.0 release assembly. Prepared 2026-07-20.

## 0. Repo-state mismatch and the decisions that resolved it

The v4.0 package was built against the **v3 repo state** (four design docs in `docs/`, no theory
layer). The live repository had moved past that state: commit `219ad6c` ("rewrite", 2026-07-07)
dissolved `docs/` into a law-register `core/` + `apparatus/` structure, and later commits added the
knowability and composition arcs, `experiments/escape-wind/`, and related files. The four v3 design
docs (`01-foundations.md`, `02-entity-reference.md`, `03-autonomy-levels.md`, `04-implementation.md`)
therefore no longer existed in the working tree — only in git history at `219ad6c^`.

Resolutions (confirmed with the maintainer before executing):

1. **The v4 package replaces the rewrite-era tree wholesale.** The pre-existing `core/`,
   `apparatus/`, `applications/`, and `experiments/` trees were deleted; the package's versions
   define the complete release contents. All removed content remains recoverable from git history.
2. **The four v3 design docs were not restored.** They are treated as superseded by the rewrite;
   `applications/sdlc/` ships with only its README. The README's links to the four docs are
   therefore dead (see §1) — a known, accepted consequence of this decision, not a build error.
3. **Rewrite-era files with no package counterpart were deleted** with their parent directories:
   `apparatus/composition/*`, `apparatus/model-actor-capacity.md`, `apparatus/task-shape-corpus.md`,
   `apparatus/difficulty-ladder-protocol.md`, `apparatus/glossary.md`, `apparatus/method/*`,
   `apparatus/biology-contrast.md`, `core/escape-under-pressure.md`, `core/context-window.md`,
   `core/assets/*`, `apparatus/assets/overview.svg`, and `experiments/escape-wind/`.

Because the four docs were not restored, tasks 2–3 of the build plan (move + light register pass on
the four docs) had nothing to operate on. Task 4 (`_CARRY_FORWARD_FROM_V3.md` deleted) was done. No
`docs/` stub was left: no file in the release tree links to `docs/` anywhere.

## 1. Dead internal links (task 5)

Full scan of every relative markdown link in the release tree. Four dead links, all one cause:

| File | Line | Target | Cause |
|---|---|---|---|
| `applications/sdlc/README.md` | 35 | `01-foundations.md` | v3 doc intentionally not restored (§0.2) |
| `applications/sdlc/README.md` | 39 | `02-entity-reference.md` | v3 doc intentionally not restored (§0.2) |
| `applications/sdlc/README.md` | 43 | `03-autonomy-levels.md` | v3 doc intentionally not restored (§0.2) |
| `applications/sdlc/README.md` | 48 | `04-implementation.md` | v3 doc intentionally not restored (§0.2) |

Every other internal link in the repository resolves. Note: the build plan stated "if the four
filenames don't exist after task 2, task 2 failed" — task 2 was superseded by decision §0.2, so
these four are expected-dead, awaiting either restoration of the docs or an edit to
`applications/sdlc/README.md` (not made, to avoid rewriting prose without instruction).

## 2. "Law" register audit (task 6)

Word-boundary, case-insensitive scan for "law"/"laws" across the whole release tree (markdown,
SVG, HTML). 72 occurrences. Classification: **HOMAGE** (named external law — Tesler, Ashby,
Newton, or the class "classical laws"), **FOIL** (deliberate rhetorical or register-discussion
use), **FLAG** (self-reference in the law register that may need changing). Per instructions, no
FLAG was auto-fixed.

| File | Line | Occurrence (abridged) | Class |
|---|---|---|---|
| `README.md` | 46 | "not a new physical law … **Tesler's Law** of Conservation" | HOMAGE |
| `README.md` | 49 | "a **principle**, not a law" | FOIL |
| `README.md` | 112 | ""Law" → "Principle." No physical-law status" | FOIL |
| `CHANGELOG.md` | 8 | "the principle-not-law register" | FOIL |
| `CHANGELOG.md` | 20 | ""Law" → "Principle" … homage (Tesler's, Ashby's)" | FOIL |
| `CONTRIBUTING.md` | 21 | "Claim physical-law status without a measurable quantity" (a listed don't) | FOIL |
| `core/README.md` | 10 | "why it is a *principle*, not a law" | FOIL |
| `core/00-determination.md` | 7 | preface: "where an older section says 'the law,' read 'the principle'" | FOIL |
| `core/00-determination.md` | 8 | preface: "law" retained only for Tesler/Ashby or as foil | FOIL |
| `core/00-determination.md` | 9 | preface: "a deliberate rhetorical foil" | FOIL |
| `core/00-determination.md` | 12 | "what the law asserts" | FLAG¹ |
| `core/00-determination.md` | 21 | "hiding what the law is about" | FLAG¹ |
| `core/00-determination.md` | 34 | "The law is not about building" | FLAG¹ |
| `core/00-determination.md` | 37 | "reads as a law about software engineering … thermodynamics reads as a law" | FOIL |
| `core/00-determination.md` | 107 | "A law that admits everything forbids nothing" | FOIL |
| `core/00-determination.md` | 125 | ""Conservation" and "demand" survive; "law" does not" | FOIL |
| `core/00-determination.md` | 127 | "*Tesler's Law*" | HOMAGE |
| `core/00-determination.md` | 128 | "*Ashby's Law* — homage, not physics" | HOMAGE |
| `core/00-determination.md` | 142 | ""I have found a law governing immune systems…"" (quoted bad delivery) | FOIL |
| `core/00-determination.md` | 145 | ""not … a law, because I have no unit"" | FOIL |
| `core/00-determination.md` | 230 | "exactly the price the law…" | FLAG¹ |
| `core/00-determination.md` | 265 | "the law forcing…" | FLAG¹ |
| `core/00-determination.md` | 294 | "If the law were about engineering" | FLAG¹ |
| `core/00-determination.md` | 309 | "why the law stayed invisible" | FLAG¹ |
| `core/00-determination.md` | 313 | "Nobody writes a conservation law for a light switch" | FOIL |
| `core/00-determination.md` | 322 | "The law was always true" | FLAG¹ |
| `core/00-determination.md` | 342 | "The law does not describe how to build things" | FLAG¹ |
| `core/01-the-principle.md` | 8 | heading: "this is a principle, not a law" | FOIL |
| `core/01-the-principle.md` | 10 | "A conservation *law*, in the sense physics uses the word" | FOIL |
| `core/01-the-principle.md` | 14 | "*Tesler's Law of Conservation of Complexity*" | HOMAGE |
| `core/01-the-principle.md` | 15 | "*Ashby's Law of Requisite Variety* … "law" as homage" | HOMAGE |
| `core/01-the-principle.md` | 16 | "(Ashby) explicitly refused physical-law status" | HOMAGE |
| `core/01-the-principle.md` | 19 | "wherever the word "law" appears … it is homage, and it is flagged" | FOIL |
| `core/01-the-principle.md` | 23 | "worth more than a law that overclaims" | FOIL |
| `core/04-actors.md` | 17 | "Re-indexing the classical laws by actor" | HOMAGE |
| `core/04-actors.md` | 328 | "The classical laws are correct" | HOMAGE |
| `core/04-actors.md` | 345 | "**Tesler's law** cannot tell you…" | HOMAGE |
| `core/04-actors.md` | 357 | "**Ashby's law** is silent on…" | HOMAGE |
| `core/04-actors.md` | 420 | "that no classical law can produce" | HOMAGE |
| `applications/sdlc/README.md` | 53 | "they may still say "law" where `core/` now says "principle"" | FOIL |
| `meta/lineage-and-limits.md` | 15 | "never claim physical-law status for a heuristic" | FOIL |
| `meta/lineage-and-limits.md` | 25 | "Ashby — the Law of Requisite Variety" | HOMAGE |
| `meta/lineage-and-limits.md` | 33 | "our "law" is weaker than his" | FOIL |
| `meta/lineage-and-limits.md` | 39 | "Ashby himself refused physical-law status" | HOMAGE |
| `meta/lineage-and-limits.md` | 40 | ""an information law…" not a law like Newton's" | HOMAGE |
| `meta/lineage-and-limits.md` | 43 | "Tesler — the Law of Conservation of Complexity" | HOMAGE |
| `meta/lineage-and-limits.md` | 56 | "[Tesler's] Law, generalized" | HOMAGE |
| `meta/lineage-and-limits.md` | 119 | ""Law" → "Principle." No physical-law status…" | FOIL |
| `meta/lineage-and-limits.md` | 121 | "A conservation law names a quantity invariant under a symmetry" | FOIL |
| `meta/lineage-and-limits.md` | 127 | "Keep "Law" only in the informal register, the way "Tesler's" | HOMAGE |
| `meta/lineage-and-limits.md` | 128 | "Law" and "Ashby's Law" use it — as homage" | HOMAGE |
| `meta/lineage-and-limits.md` | 241 | "no longer a "law" — it is an accounting identity" | FOIL |
| `meta/lineage-and-limits.md` | 291 | "overreach we should retreat (physical-law status…)" | FOIL |
| `meta/lineage-and-limits.md` | 300 | "**Tesler**, Law of Conservation of Complexity" | HOMAGE |
| `meta/lineage-and-limits.md` | 317 | "*The Law of Conservation of Specification Demand*" (quoted as the superseded "Before" name) | FOIL |
| `meta/lineage-and-limits.md` | 321 | "generalization of Tesler's Law" | HOMAGE |
| `meta/consolidated-state.md` | 24 | "the discipline that keeps this a law" | FLAG² |
| `meta/consolidated-state.md` | 64 | "This is Tesler's Law of Conservation of Complexity, generalised" | HOMAGE |
| `meta/consolidated-state.md` | 66 | "Do not claim physical-law status" | FOIL |
| `meta/consolidated-state.md` | 68 | "If "Law" is used, it is homage" | FOIL |
| `meta/consolidated-state.md` | 69 | "*Tesler's Law* and *Ashby's Law*" | HOMAGE |
| `meta/consolidated-state.md` | 242 | "*"Law of Conservation of Specification Demand"*" (quoted in the Superseded table) | FOIL |
| `meta/consolidated-state.md` | 297 | "a law you can't measure invites the exact rebuttal" | FOIL |
| `meta/consolidated-state.md` | 311 | ""conservation" is an accounting identity, not a law" | FOIL |
| `meta/consolidated-state.md` | 326 | "generalisation of **Tesler's** Law" | HOMAGE |
| `assets/conservation-principle.html` | 6 | `<title>The Law of Conservation of Specification Demand</title>` | FLAG³ |
| `assets/conservation-principle.html` | 305 | `<h1>The Law of Conservation of Specification Demand</h1>` | FLAG³ |
| `assets/conservation-principle.html` | 484 | "the **tier–specification inverse law**" | FLAG³ |
| `assets/conservation-principle.html` | 510 | JS comment: "esc is the REMAINDER. that is the law." | FLAG³ |
| `assets/conservation-principle.svg` | 27 | title text: "The Law of Conservation of Specification Demand" | FLAG³ |
| `assets/conservation-principle.svg` | 165 | comment: "tier-specification inverse law" | FLAG³ |
| `assets/conservation-principle.svg` | 167 | "TIER–SPECIFICATION INVERSE LAW" | FLAG³ |

**¹** These nine self-references in `core/00-determination.md` are *acknowledged* by that
document's own preface (lines 7–9: "where an older section below says 'the law,' read 'the
principle'"), so they did not "slip through" unnoticed — but they are still self-references in the
law register, left untouched because `core/` is final. Decide whether the preface disclaimer is
sufficient or the nine lines should be re-registered.

**²** In the authoritative status document itself: §1.2's heading calls the admission tests "the
discipline that keeps this a **law**." Left untouched because `meta/` is final, but this is the one
self-reference with no covering disclaimer in its own document.

**³** The shipped diagram assets carry the *superseded* title — "The Law of Conservation of
Specification Demand" is listed in `meta/consolidated-state.md` §2 as "Superseded — do not cite."
The filenames say `conservation-principle.*` but the rendered title says Law. `assets/` is not
under the do-not-edit constraint, but per task 6 no FLAG was auto-fixed. The "tier–specification
inverse law" occurrences are a self-coined (not external) named result, hence FLAG not HOMAGE.

Tally: 24 HOMAGE · 31 FOIL · 17 FLAG. All 17 FLAGs are in `core/`, `meta/`, or `assets/`; none
were changed.

## 3. Flagged but not changed (constraint: core/, apparatus/, meta/ are final)

Observed while assembling; recorded here instead of edited:

1. **`meta/consolidated-state.md` §2, "Current `core/` set" table is out of sync with the shipped
   package layout.** It lists `05-lineage-and-limits.md` as a `core/` file (shipped as
   `meta/lineage-and-limits.md`), lists `closure-principle.md` and `adversarial-ground.md` under
   the `core/` set (shipped under `apparatus/`), and does not list the shipped
   `core/05-composition.md` or `core/06-determination-and-intelligence.md` at its actual index.
   It also marks `core/00` §7 (immune licensing) as "cut it" — whether the shipped `00-determination.md`
   already reflects that cut was not verified, since no edit was permitted either way.
2. **`meta/consolidated-state.md` references artifacts that are not in the release tree**:
   `determination.md`, `adversarial-ground.md` (present, but the note implies a pending revision),
   `linkedin-plan.md`, `ground-prd.md`. If these live outside the repo, fine; if they were meant to
   ship, they are missing.
3. **The asset-title mismatch** (§2, FLAG³): release assets rendering the superseded "Law of
   Conservation of Specification Demand" title contradict the register rule the release is named
   for. Highest-visibility FLAG in the set.
4. **`applications/sdlc/README.md` links to four documents that do not exist** (§1) — the file
   itself was shipped by the package expecting the docs to be moved in; the maintainer chose not to
   restore them. Either restore the four docs from `219ad6c^` in a later pass, or trim the README's
   per-document sections.

## 4. Summary

The v4.0 package replaced the repository tree wholesale: the new `core/` (00–06, principle
register), `apparatus/` (encode-verify, closure-principle, adversarial-ground), `meta/`
(lineage-and-limits, consolidated-state), `applications/`, root `assets/`, and the new README,
CHANGELOG, CONTRIBUTING, LICENSE.md, and .gitignore are now the entire repo. Deleted: the
rewrite-era law-register `core/` and `apparatus/`, `applications/sdlc.md`, `experiments/escape-wind/`,
and the old root files — all recoverable from git history. The four v3 design docs were *not*
restored into `applications/sdlc/` (maintainer decision: superseded by the rewrite), leaving four
known-dead links in that directory's README; consequently no register pass on them was needed and
the `_CARRY_FORWARD_FROM_V3.md` build note was deleted. Nothing under `core/`, `apparatus/`, or
`meta/` was edited; the 17 law-register FLAGs and 4 structural observations above await maintainer
decisions.
