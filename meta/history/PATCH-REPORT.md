# v4.3 Patch Application Report

Applied per `PATCH.md` in the v4.3 patch package. All new files were copied verbatim
(byte-identical to the package, verified with `diff`). No prose, numbers, tables, or equations
were altered anywhere. This file replaces the v4.2 report, which remains available in git
history.

## 1. Prerequisite check

Both prerequisites **existed** before any patch action was taken:

- `core/08-the-measure.md` — present (v4.1 applied) ✔
- `core/09-the-floor-mechanism.md` — present (v4.2 applied) ✔

`apparatus/prefix-stability.md` §6 depends on both; its cross-references resolve. Proceeded.

## 2. New files — dropped in byte-identical

- `apparatus/prefix-stability.md` — copied verbatim from the package; `diff` confirms
  byte-identical. Not one word of its prose was edited.
- `apparatus/assets/prefix-stability-check.py` — copied verbatim; byte-identical.
  `apparatus/assets/` did not exist and was created.

## 3. The core/04 §3 replacement — a precise account

The package's `core/04-section-3-patch.md` was used as the delivery vehicle, exactly as
PATCH.md Edits §0 directs. The splice was done by line range programmatically, with anchor
assertions on both files, and the replaced region was verified byte-identical to the vehicle's
corresponding lines afterward.

**Replaced:**

- The entire former `## 3. Selection and training` (the closure-only version, including the
  "Training is what you do when the acceptance predicate closes / Selection is what you do when
  it does not" headline) — replaced by the two-factor §3 ("Closure decides whether training is
  *available*. Cost decides the *ratio* when it is."), with its two sub-arguments (closure as a
  hard constraint, not a price; cost decides the rest) and the
  `selection intensity ≈ f(closure) × g(training cost)` formulation.
- The entire former `### 3.1 The honest version — it is a gradient, not a dichotomy` (four-row
  profession table, single-factor falsifiable form) — replaced by
  `## 3.1 The gradient, and what the two factors explain` (five-row table including the
  accountant row and the cardiac-surgeon anomaly, the two-factor separability argument, the
  sharpened falsifiable form, and the **pre-registration guard** — see §6 below).

**Inserted (new, after §3.1 and before §3.2):**

- `## 3.1a Worked example: military selection, and why it needs two factors` — the two clusters
  (untrainable vs. trainability-filter), the explicit **exclusion of teamwork** as a category
  error, the tiered structure as the funnel applied to actor acquisition, the **scarcity /
  evaluation-economics rival explanation** and its discriminating test (criteria must change in
  kind, not merely in standard), marked *projected*.
- `## 3.1b Worked example: LLM training` — closure gating availability (pretraining/SFT closes;
  RLHF does not → the reward model as a **manufactured closing predicate**, reward hacking as
  the gap; RLVR closes), cost deciding the ratio (best-of-N, checkpoint selection, routing,
  distillation), the **actor-selection vs. act-selection** distinction, and the falsification
  condition.

**Left completely untouched:**

- `### 3.2 What this predicts about models` — verified unchanged by git diff; not a character
  of it was modified.
- Everything else in `core/04-actors.md`: §1, §2, §4, §5, §6, §7 — all unchanged.

**Not carried over from the vehicle:** its front matter (title, "Applies to", "Why" preamble)
and its trailing "## What this does not change" section — both are vehicle commentary, not
replacement text.

**Deleted:** `core/04-section-3-patch.md` was applied and never committed to the repository —
it existed only in the extracted patch package, so the repo never contained it. The
"apply it and delete it" instruction is satisfied: no delivery vehicle ships with v4.3.

**One mechanical joint, disclosed:** a `---` horizontal rule was placed between the end of
§3.1b and the untouched `### 3.2`, matching the separator convention the copied sections use
between themselves (§3 | §3.1 | §3.1a | §3.1b). No text of §3.2 was touched.

## 4. Wiring edits

- `README.md` — the `apparatus/prefix-stability.md` row appended to the Apparatus table,
  PATCH.md's exact text.
- `apparatus/README.md` — the **prefix-stability** index line appended, PATCH.md's exact text.

## 5. Attribution — both sections and both citation rows landed

- `meta/lineage-and-limits.md` gained **§1.12 Martin — the Stable Dependencies Principle** and
  **§1.13 Smith — the weighted shortest processing time rule (1956)**, inserted directly after
  §1.11 (before "Additional context worth acknowledging"), following the §1.8–1.11 pattern.
  PATCH.md's exact text, verbatim.
- **The §1.13 correction survives verbatim**: "NOTE A CORRECTION: an earlier formulation of
  this result claimed ascending RE-DERIVATION RATE was optimal. That is false… The framework
  applied a known scheduling result; it did not derive a new one." — present, untouched.
- The §6 citation table gained both rows: *Prefix ordering by stability* → Martin (SDP), and
  *The optimal ordering is rate/length* → Smith 1956 (WSPT).

## 6. Load-bearing caveats — all verified present, none softened

- **Pre-registration guard** (core/04 §3.1): "Pre-register the cost proxy, or the claim is not
  a claim." — present, with the proxy fixed as time-to-competence × cost-per-unit-time ×
  washout rate.
- **Teamwork exclusion** (core/04 §3.1a): "a category error the framework should refuse" —
  present in full, including "Listing trained capabilities as untrainable is how this analysis
  degrades into mythology."
- **Scarcity rival** (core/04 §3.1a): the "scarcity and evaluation economics" rival
  explanation and the in-kind-not-in-standard discriminating test — present, with the
  *projected* status marker.
- **Actor-selection vs. act-selection** (core/04 §3.1b): present, including "Collapsing the two
  would reduce the claim to 'people use argmax.'"
- **§1.13 ordering-rule correction** — present verbatim (above).
- **CHANGELOG Corrected section** carries both corrections: the selection/training two-factor
  fix and the ordering-rule retraction ("was WRONG and is retracted… 551 vs optimum 151").

## 7. Script verification — the expected falsification pattern, exactly

`python3 apparatus/assets/prefix-stability-check.py` ran clean (stdlib only, exit 0). Four
cases, with precisely the required pattern:

| Case | ascending rate | ascending rate/len |
|---|---|---|
| 1 — typical | match=True (78.00) | match=True (78.00) |
| 2 — stress (volatile huge) | **match=False, waste 551.00** | match=True, **waste 151.00** |
| 3 — random mix | **match=False, waste 1312.50** | match=True, waste 557.50 |
| 4 — realistic prefix | match=True (108.75) | match=True (108.75) |

This matches the table in `apparatus/prefix-stability.md` §3 (551/151; 1312/557 — the doc
rounds the .50s) and the CHANGELOG's "waste 551 vs optimum 151". The failures are the point:
they are the falsification of the naive rule. Nothing was "fixed."

## 8. Dead-link check — no dead links

Every markdown link in the edited files (`README.md` — including the new
`apparatus/prefix-stability.md` row) and every backtick path reference in the new/edited
content (`apparatus/encode-verify.md`, `apparatus/closure-principle.md`, `core/00`, `core/03`,
`core/05`, `core/07`, `core/08`, `core/09`, `assets/prefix-stability-check.py` relative to
`apparatus/`) was checked against the filesystem. **Dead links found: none.** The
`prefix-stability.md` references to the `ground` PRD / INV-6 are mentions of the external
reference tooling, not repository links — the same pre-existing pattern the v4.2 report noted.

## 9. Register check

No new content uses "law" for the framework's own claim. Grep over the new/edited regions
finds zero occurrences; "law" remains only in the shipped homage senses (Tesler's, Ashby's)
and historical changelog entries. Martin's SDP is consistently a "Principle."

## 10. Flagged but not changed (per the hard constraints)

- **Heading levels in core/04 §3:** the copied sections arrive as `## 3.1`, `## 3.1a`,
  `## 3.1b` (H2, verbatim from the vehicle, whose internal `### Why closure…`-style
  sub-headings depend on that level), while the untouched `### 3.2` remains H3. The levels are
  inconsistent within §3, but normalising them would mean restructuring final documents and/or
  touching §3.2 — both forbidden. Left as delivered.
- **Stale single-factor statements elsewhere:** the closure-only formulation
  ("selection intensity is inversely proportional to predicate closure") still appears in
  `core/04` outside the replaced region — the header claim list, §6 (Polanyi/Collins), §7 —
  and in `README.md` "Start here" item 2 and the Status section. PATCH.md's edit list does not
  touch these, so they were left as-is; they now lag the corrected two-factor §3.
- **`apparatus/README.md`** closing line still reads "All three are instances of one
  discipline…" though the index now lists five documents — pre-existing (flagged in the v4.2
  report), and PATCH.md specifies only the added index line.
- No number, table, or equation discrepancies were found between the new docs and the script
  output — nothing to report under the copy-error rule. No caveat was tidied; the ones that
  read deliberately awkwardly (the §3.1 "or the claim is not a claim" guard; §1.13's
  self-correction) ship exactly as written.

## Summary

The v4.3 patch applied cleanly on a verified v4.1+v4.2 base: both prerequisite files existed;
`apparatus/prefix-stability.md` and `apparatus/assets/prefix-stability-check.py` were dropped
in byte-identical; `core/04-actors.md` §3–§3.1 were replaced with the two-factor correction
and §3.1a/§3.1b inserted, with §3.2 verified untouched and the delivery vehicle never entering
the repository; the README and apparatus index were wired with PATCH.md's exact rows; §1.12
(Martin) and §1.13 (Smith) landed in the lineage with the ordering-rule correction verbatim,
plus both §6 citation rows; the CHANGELOG 4.3 entry carries both corrections; the verification
script produces exactly the required falsification pattern (naive rule fails on cases 2 and 3,
Smith's rule optimal on all four); every internal reference resolves; and the register is
unchanged — the framework's claim remains a principle.
