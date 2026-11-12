# Judging

You are given a set of questions, each with its expected answer, and three texts labelled T1, T2 and T3.

For every question and every text, decide whether a reader who had only that text could give the expected answer.

| Score | Meaning |
|---|---|
| 1 | The text states the expected answer, in any wording. |
| 0.5 | The text states part of the expected answer, or states it so generally that the reader would get the gist but not the specific point. |
| 0 | The text does not state it. |

Rules:
- Judge only what the text says. Do not credit what a knowledgeable reader could infer or already knows.
- Judge each text on its own.
- Do not try to guess what the labels stand for.
- Ignore the `statements` field of the questions; it is not part of any text.

Output one YAML file, a mapping from question id to scores:

```yaml
Q1: {T1: 0, T2: 1, T3: 0.5}
```

Write nothing else to the file.
