---
step: glossary
version: 0
status: trial
tracking: mindovermachine-dev/decision-driven-design#75
---

# Projection step: glossary

**Trial, `[PROPOSED]`.** This step writes one short explanation, a gloss, for each term of an information set. A projection then serves the gloss to its reader: where the term is met, or in a list to look up (Emil, 2026-11-12).

## Input

One file. For each term it gives the text of the section the index names as the term's home.

## The rule

**A gloss says what the home section says the term is, and nothing it does not.**

- One sentence, at most 25 words.
- Write for someone who has not read the section. Prefer ordinary words.
- Do not use another term of the list to explain this one, unless the section itself does and there is no plain way round it.
- Do not add a reason, an example or a judgement.
- If the section uses the term without saying what it is, do not guess. Write the gloss as `null` and say why in `problem`.
- British spelling.

## Output

One YAML file:

```yaml
glosses:
  the What:
    gloss: "…"
  some term:
    gloss: null
    problem: "The section uses the term and does not say what it is."
```

Write nothing else to the file.
