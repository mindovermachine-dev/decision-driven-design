---
step: summary
version: 0
status: trial
tracking: mindovermachine-dev/decision-driven-design#75
---

# Source step: summary

**Trial, `[PROPOSED]`.** This is not an output format. It is a step that builds the source. It gives every part of a source a summary, from the bottom up, so that meaning propagates to the top. Derived formats then read summaries at the depth they need.

After Emil's direction of 2026-11-12: treat the parts of a source as chunks, and let a model produce, for each chunk, the output that stands for it.

## The levels

| Level | Part | Summarised from | Length |
|---|---|---|---|
| 1 | A section (`###`) | Its headline and its own statements. Nothing else. | 1 sentence, at most 30 words |
| 2 | A chapter (`##`) | Its introduction and the summaries of its sections. Not the statements inside the sections. | At most 3 sentences |
| 3 | The document (`#`) | Its introduction and the summaries of its chapters. Nothing deeper. | At most 3 sentences |

Each level reads only the level beneath it. That is the point: if meaning does not survive the step, the level above cannot repair it.

## The rule

**A summary says what its children together say, and nothing they do not.**

- A summary may generalise. It may name what several children have in common, in words none of them uses, if every child it cites supports the wording.
- A summary may leave children out. Lead with what the part is for.
- A summary may not add a reason, an example, a number, a judgement, or a definition.
- Use the source's terms exactly as written. Do not explain them.
- British spelling. Plain words.
- List in `cites` the identifiers of the children the summary rests on. Cite only children of the part being summarised.

## Output

Write one YAML file, a mapping from the part's identifier to its summary:

```yaml
W3:
  summary: "…"
  cites: [W3.0, W3.1]
```

Write nothing else to the file.
