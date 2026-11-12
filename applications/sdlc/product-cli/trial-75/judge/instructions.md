# Judging

You are given a set of questions, each with its expected answer, and eight texts: four labelled K1 to K4, each at two depths, `top` and `full`.

For every question and every text, decide whether a reader who had only that text could give the expected answer.

| Score | Meaning |
|---|---|
| 1 | The text states the expected answer, in any wording. |
| 0.5 | The text states part of the expected answer, or states it so generally that the reader would get the gist but not the specific point. |
| 0 | The text does not state it. |

Rules:
- Judge only what the text says. Do not credit what a knowledgeable reader could infer or already knows.
- Judge each text on its own. A `full` text contains its `top` text plus more, so its score for a question is never lower than the `top` score.
- Do not try to guess what the labels stand for.
- Ignore the `statements` field of the questions; it is not part of any text.

Output one YAML file, a mapping from question id to scores:

```yaml
Q1: {K1_top: 0, K1_full: 1, K2_top: 0.5, K2_full: 1, K3_top: 0, K3_full: 0, K4_top: 1, K4_full: 1}
```

Write nothing else to the file.
