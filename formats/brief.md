---
format: brief
version: 2
status: trial
tracking: mindovermachine-dev/decision-driven-design#75
---

# Format: brief

**Trial, `[PROPOSED]`.** A brief is the outermost projection of a canon: what a reader meets first. Version 2 is built from the canon's shared summaries, a top written for one reader, and the glossary. Versions 0 and 1 read a separate source file, which is retired.

## How a brief is made

| Step | Made by | From |
|---|---|---|
| Shared summaries of the canon's leaves | a model, once (`formats/summary.md`) | the canon |
| Glosses of the terms | a model, once (`formats/glossary.md`) | each term's home section |
| The top for one reader | a model (this file) | the document's introduction and the shared summaries |
| The brief | a script | the top, with each term linked at first use and listed with its gloss |

Only the top is written per reader. This file instructs the model that writes it.

## Input

One file. It holds:

- a relevance: a description of the reader;
- the document's introduction, key `C0`;
- every chapter, with the shared summaries of its leaves, each under its key.

You have not been given the canon itself, and that is deliberate.

## What to write

1. **The document summary.** At most 3 sentences and 75 words. What this is, and what in it bears most on this reader.
2. **One line per chapter.** At most 1 sentence and 30 words each. What the chapter holds for this reader. If a chapter holds nothing this reader needs, give it no line: write `summary: null`.

## The rule

**Every sentence states only what the keyed material it cites states.**

- End every sentence with the keys it rests on, in square brackets: `[C1]` or `[C3.2, C3.3]`. Cite the document's introduction as `[C0]`.
- You may compress several summaries into one sentence. Cite all of them.
- You may not add a reason, an example, a number, a comparison, a judgement or a definition.
- Use the canon's terms exactly as written, and do not explain them. The glossary is attached to the brief after you.
- Use what the reader already knows. Do not spend words on it.
- Do not address the reader, and do not mention the relevance.
- British spelling. One idea per sentence, except where you compress.

## Output

One YAML file:

```yaml
document:
  summary: "… [C0, C1]"
chapters:
  C1:
    summary: "… [C1]"
  C7:
    summary: null
```

Give every chapter key an entry. Write nothing else to the file.
