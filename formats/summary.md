---
step: summary
version: 2
status: trial
tracking: mindovermachine-dev/decision-driven-design#75
---

# Projection step: shared summaries

**Trial, `[PROPOSED]`.** This step gives every leaf of a canon a summary. A leaf is a section of the canon that has no sections of its own. The summaries are shared: every reader's projection is built over the same ones.

Version 2 reads the canon directly (Emil, 2026-11-12: `product-definition.md` is the canon; the `source` slot is retired). Versions 0 and 1 read a separate source file of identified statements.

## Input

One file. It holds several parts. For each part it gives:

- the part's key and heading;
- a length limit;
- a relevance: the introduction of the part of the canon that contains this one;
- the text of the part, as it stands in the canon.

## Relevance

- Relevance decides **selection**. Of all the part says, keep what bears most on the relevance. Drop what bears least.
- Relevance never licenses adding. It chooses among what the part says. It gives you nothing new to say.
- Do not mention the relevance in the summary.

## The rule

**A summary says what its part says, and nothing it does not.**

- Summarise each part from its own text only. Do not carry anything from one part into another.
- A summary may generalise, if the text supports the wording.
- A summary may leave things out. Lead with what the part is for.
- A summary may not add a reason, an example, a number, a judgement, or a definition.
- Keep the subject of every claim. If the text says that A is checked, do not write that B is checked.
- Use the canon's terms exactly as written. Do not explain them. Terms are explained elsewhere.
- Do not cite rulings (`[D1.n]`), dates or decision identifiers. Say what is ruled, not that it was ruled.
- British spelling. Plain words.

## Output

One YAML file, a mapping from each part's key to its summary:

```yaml
C3.2:
  summary: "…"
```

Write nothing else to the file.
