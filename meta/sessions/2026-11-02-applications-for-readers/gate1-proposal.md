# Gate 1 — the format for applications/, proposed and demonstrated

2026-11-02. Everything here is `[PROPOSED]` until Emil rules. The demonstration is
[`gate1-demo-what.md`](gate1-demo-what.md).

## Weakest point first

**The format moves the decision trail from the sentence to the end of the document.** Today a
reviewer can see, beside each rule, which decision governs it. In the proposed format a reviewer
looks the rule up in the section's row of "Where this comes from". That costs one step for every
check a reviewer makes.

Two things make the cost smaller than it looks:

- **The inline ids are not instrumented.** `what.md` and `how.md` carry 165 decision ids between
  them and no `ddd:ref` marker. No validator reads those ids. They serve a human reviewer only, and
  the basis table serves the same reviewer.
- **The `ddd:doc` block can be checked.** Emil ruled a checked opener on 2026-10-26 (finding 2
  below). If it is revived, each document's basis becomes machine-readable, and a moved basis
  warns. That is more instrumentation than the documents have today, not less.

If Emil rules that reviewers need point-of-use citations, the fallback is invisible `ddd:ref`
markers at the point of use, which render as nothing.

## Findings that bear on the format

1. **The doc-format principle is ruled, but is not on `main`.** Pre-session ruling 1 of
   2026-10-26 says: "only canon carries authority; every other folder exists for a named reader
   doing a named act". Ruling 2 adopted a `ddd:doc` opener and a warning-level check. Both are
   recorded only on `claude/doc-format`. That branch shares no history with `main`, and its decision
   id `DDD-dec-39` has since been reused. This session rests on those rulings, so they need
   re-filing on `main`.
2. **That session's pilot already tested this problem.** Its Gate 3 readers listed decision ids,
   promotion numbers and "held" markers among the things they did not understand. Status flagged
   at the point of use helped; status flagged *with ids* did not. Its proposed amendment, "say it in
   words the reader can use, and keep IDs out", was not ruled before the branch stalled.
3. **The register model already has plain words.** `DDD-dec-74`'s "ready to try" and the method
   README's three registers give the vocabulary that status lines need, without ids.

## Survey

| Document | Lines | Ids | What makes it read as a record | Who actually reads it |
|---|---|---|---|---|
| `applications/README.md` | 10 | 0 | Explains the projection relation; no reader, no way in | Anyone arriving in the folder |
| `sdlc/README.md` | 103 | 3 | Opens with "the framework through v3" history and an upstream-basis block | A practitioner choosing where to start |
| `sdlc/what.md` | 861 | 82 | Opens with move status, register key, a ruling table, and "where the source went"; 79 Product Framework section references in the body; quotes in source order | Two readers: practitioners specifying a product, and tool builders implementing identity, hashes and the wire |
| `sdlc/how.md` | 700 | 83 | Written as the answer to a charter: "the thesis, tested", "a fourth kind? No", "Open, for Emil", "Appendix A — every departure from the proposal" | The same two readers |
| `sdlc/how-vocabulary.md` | 113 | 5 | Namespace and record-member choices with their reasoning, flags and status | Tool builders |
| `sdlc/how-examples/README.md` | 170 | 11 | Mostly supersession history of the example records | Someone running or extending the example |
| `sdlc/production-as-ground.md` | 294 | 2 | "Location: proposed" line, an upstream-basis block, and a status paragraph before any content | An engineering lead weighing whether the framework explains delivery performance |
| `organizations/README.md` | 43 | 6 | Lists four claims verbatim with their statuses | Someone deciding whether the framework applies to organisation design |
| `sdlc/authority.md` (PR #45, unmerged) | — | many | Same pattern as `what.md` | Not touched here; the format applies after #45 merges |

The non-Markdown companions (`what/*.ttl`, `*.py`, the records) are out of scope, except their
header comments where a document links into them.

## The proposed format

**F1 — The opening says who it is for and what they can do.** The title names the task. Then come
two to four sentences: who uses the document, what they can do after reading it, and how settled it
is, in words ("decided, not yet tried on a real product"). There is no provenance before the
content.

**F2 — The `ddd:doc` block carries the machine side.** This is the opener ruled on 2026-10-26: an
HTML comment under the title holding `reader`, `act`, `pin`, `basis`, `status` and `supersedes`.
It renders as nothing.

**F3 — No ids in running text.** That covers decision and claim ids, Product Framework section
numbers, session paths and register tags. Decided is the default and goes unmarked. An unsettled
point says *(not settled yet)* where it arises, and is listed in plain words in a "Not settled yet"
section near the end.

**F4 — Ordered by the reader's task, not by the source.** Terms are defined where they are first
used. One worked example runs through every document in a folder.

**F5 — Reference material goes to its own document.** That means identities, hash laws, wire
protocols, vocabularies and record layouts. `what.md` and `how.md` each split in two: a practitioner
document and a `*-reference.md` for tool builders, linked both ways.

**F6 — Deliberation leaves the application.** Rejected alternatives, departures from a proposal,
questions put to Emil, and "where the source went" belong to the session record. The earlier text
stays reachable through `supersedes:`, so nothing is lost. A rule may keep a one-sentence reason
where the reason helps the reader apply it.

**F7 — "Where this comes from" closes every document.** It is a table from section to the
decisions and claims the section rests on, plus the source attribution. This is where the ids live,
for reviewers.

**F8 — Content does not change.** Every rule in the old text appears in the new text or its
reference document, with the same meaning. A rule that cannot be restated without changing it is
reported at Gate 2, not fixed.

## What the demonstration shows

[`gate1-demo-what.md`](gate1-demo-what.md) rewrites `what.md` §1, §2.1 and the start of §3 to F1–F7.
Writing it surfaced two faults the record style had hidden:

- **The first draft overclaimed twice, and both were caught by checking.** It said data is
  verified against the What, but data conformance is an add-on outside the framework. It also
  invented a decision history for the example that its records do not have: the whole What
  arrives in one founding decision. Plain prose makes such claims easy to write and easy to check.
  Record style hid the same claims under ids. Gate 2 checks every example statement against the
  example's files.
- **The example is not the method's example.** The method's worked example is Varve
  (`DDD-dec-77`). The What and How use Acme Shop. "One sustained example" (F4) is met per folder,
  not across the repository. Ruling 4 below asks whether that is enough.

## Falsifier

Gate 3 runs it, and it is pre-registered before Gate 2 writes anything.

- **The task:** "Acme Shop wants customers to cancel an unpaid order. Say what you add to the What,
  where each addition is anchored, who must sign, and what is in force before and after."
- **The readers:** two on the old `what.md`, two on the new one. None has seen the other version.
- **The rubric:** it includes at least two criteria the old text makes hard to reach. That avoids
  the ceiling the 2026-10-26 pilot hit, where every reader scored full marks on either text.
- **It fires if** the new text scores no better than the old on those criteria, or if any reader of
  the new text names the format's own markers as a source of confusion.

If it fires, F3 and F7 are wrong for this reader, and the fallback is the invisible-marker variant
from the weakest point.

## Predictions for Gate 2

| # | Prediction |
|---|---|
| P-1 | `what.md` splits into a practitioner document of fewer than 450 lines and a reference document. The two together are shorter than today's 861 lines, because the move history leaves |
| P-2 | `how.md` loses at least a quarter of its length to F6. Its §2, §4.3, §4.4, §13 and both appendices are deliberation |
| P-3 | The equivalence tables find at least one rule in `what.md` or `how.md` that is stated only inside a deliberative passage. It is reported, not silently moved |
| P-4 | `production-as-ground.md` keeps its argument structure. It is an evidence argument, not a how-to, so F4 applies only to its opening |
| P-5 | No validator result changes: claims, decisions, pins, the What check and the How examples all pass as at `e5a332d` |

## Rulings requested

1. **The format.** Adopt F1–F8 for `applications/`, or amend them?
2. **The 2026-10-26 rulings.** Re-file the doc-format principle and the `ddd:doc` opener on `main`
   as `DDD-dec-94`? And rule the pilot's amendment, "keep IDs out of prose", which this format
   relies on?
3. **The split.** Split `what.md` and `how.md` into practitioner and reference documents (F5), or
   keep one document each with a reference part?
4. **The example.** Is Acme Shop for the What and How, beside Varve for the method, acceptable? Or
   should the sdlc application move to Varve too, which would mean writing Varve's What?
5. **Scope beyond applications/.** Your earlier wish covers every folder: `apparatus/` reads like
   canon too. Is this session `applications/` only, with the rest later, or does Gate 2 take
   `apparatus/` as well?
