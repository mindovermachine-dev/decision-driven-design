# Third run: a brief derived from the canon

A brief derived straight from the canon contained nothing invented, and answered about half of its reader's questions. Fidelity held; usefulness did not.

## What was run

| Step | Made by | Output |
|---|---|---|
| Shared summaries of the canon's 21 leaves | two model runs, each leaf from its own text | `../../product-definition.summaries.yaml` |
| A gloss per term, from the term's home section | a model run, three terms redone | `../../product-definition.glossary.yaml` |
| A top for the authoriser, from the introduction and the shared summaries | a model run that did not see the canon | `top-authoriser.yaml` |
| The brief | `../scripts/canon.py` | `../../product-definition.en.brief.md` |
| Fidelity check: every sentence against the canon sections it cites | a separate model run | `verify.yaml` |
| The authoriser's ten questions from the first run | a separate model run | `judge-scores.yaml` |

Citation is by section of the canon (`keymap.md`). The canon carries no statement identifiers.

## Results against predictions

| Prediction | Result |
|---|---|
| 1. The check finds at most one sentence the cited sections do not support. | **Held.** 11 sentences and 5 glosses: 15 supported, 1 partly, 0 unsupported. |
| 2. The brief scores 7 or more of 10 on the authoriser's questions. | **Failed.** 5.5. |
| 3. Every term the brief uses gets a gloss, except Writ's terms and terms with no home. | **Held.** Writ, grant and head are reported as not explained in the canon. |

The falsifier did not fire: citation by section kept invention out of this brief.

## What else the run shows

- **The judging is less stable than the second run suggested.** The same text, the earlier hybrid top, scored 7.0 then and 5.5 now. So a score is good to about one and a half questions, not half a question. By this judge the new brief and the earlier top score the same, 5.5.
- **The brief covers eight chapters in the space the earlier top used for two.** The three questions it misses all rest on chapter 1 detail that the chapter's 75-word summary dropped.
- **The one "partly" verdict** is the line on cross-repository dependencies. It names the two rows marked open and reads as complete, while a third row is not yet met.
- **Seven of 36 glosses are null.** The home section uses the term without saying what it is: View, trigger, Translation, decision record, draft position, finding, orphan. Either the proposed home is wrong, or the term is nowhere explained.
- **The authoriser's top reported what the canon does not hold:** what the product is for in business terms, who Writ is, and cost, timeline and progress.

## Limits

One canon, one reader, one run of each step, one judge. The questions were written for chapters 1 and 5 only. The summaries and glosses are model output and were checked only where the brief uses them.

---

*Trial material; nothing here is ruled. Run on 2026-11-12, after Emil ruled that `product-definition.md` is the canon and retired the `source` slot. The predictions were recorded on issue #75 before the runs. The brief has since been reassembled under the rule for a human reader: no frontmatter, and an opening that starts with the subject.*
