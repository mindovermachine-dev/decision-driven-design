# Trial for issue #75: one summary tree or two?

**Trial material. Nothing here is ruled.** Run on 2026-11-12 over `../product-definition.source.md` (chapters 1 and 5).

## What was run

Four summary trees over the same source, each built bottom-up by `formats/summary.md`. Every level was a separate model run that saw only the level beneath it.

| Tree | Relevance | Built with |
|---|---|---|
| `neutral` | none | summary step version 0 (no word cap on chapters and document) |
| `intro` | the introduction of the containing part | version 1 |
| `authoriser` | `audiences/authoriser.md` | version 1 |
| `realiser` | `audiences/realiser.md` | version 1 |

Each audience has ten questions with expected answers (`questions/`), written by a model from the audience description and the source. A judge scored every tree against both sets (`judge/`). The judge saw the trees as K1 to K4: K1 realiser, K2 neutral, K3 authoriser, K4 intro.

Depth `top` is the document summary and the chapter summaries. Depth `full` adds the section summaries.

## Scores (out of 10)

| Tree | Authoriser questions, top | full | Realiser questions, top | full |
|---|---|---|---|---|
| authoriser | 6.0 | 8.5 | 1.5 | 6.0 |
| realiser | 3.0 | 6.0 | 4.0 | 8.5 |
| intro | 4.5 | 9.0 | 2.5 | 8.0 |
| neutral | 6.0 | 8.5 | 3.5 | 7.5 |

Overlap of the statements cited at section level, authoriser against realiser: 0.59 (Jaccard). At chapter level: 0.20 and 0.13.

## Predictions against results

The predictions were recorded on the issue before the runs.

| Prediction | Result |
|---|---|
| 1. With the introduction as relevance, the document summary keeps the reading guide (`I0.4`, `I0.5`). | **Failed.** It was dropped again. No tree answers the question that rests on it. |
| 2. Audience trees differ little at section level and clearly above it. | **Half held.** They differ clearly above (0.20, 0.13). They also differ at section level (0.59) more than predicted. |
| 3a. At top depth, an audience's own tree beats the other's by two questions or more. | **Held.** 3.0 and 2.5. |
| 3b. At full depth the gap is one question or less. | **Failed.** 2.5 and 2.5. |

## Limits

- Ten questions per audience, one judge, one run per tree. A difference of half a question is noise.
- The question writers saw the audience descriptions. That favours each audience's own tree.
- The neutral tree was built without the 75-word cap. Its top level had more room than the others.
- Version 1 also added a rule to keep the subject of every claim. So version 0 against version 1 is not a clean comparison.
- The 57 new summaries were not checked statement by statement for fidelity.
- Every role was played by the same model family. The models were not fully isolated from this project's instructions.
