---
format: brief
version: 7
reader: model
projects-for: human
status: trial
tracking: mindovermachine-dev/decision-driven-design#75
---

# Format: brief

**Trial, `[PROPOSED]`.** A brief is the outermost projection of a canon: what a reader meets first. It is built from the canon's shared summaries, a top written for one reader, and the glossary. This file is read by the models that weight the chapters and write the top. The brief they lead to is read by a human.

Version 6 lets the reader's needs decide how much space each chapter gets. Up to version 5 every chapter got one line, whatever it was worth to the reader.

## How a brief is made

| Step | Made by | From |
|---|---|---|
| Shared summaries of the canon's leaves | a model, once (`formats/summary.md`) | the canon |
| Glosses of the terms | a model, once (`formats/glossary.md`) | each term's home section |
| The weights for one reader | a model (this file, "Weighting") | the reader's description and the shared summaries |
| The top for one reader | a model (this file, "The top") | the shared summaries, and the canon's own text for the chapters weighted most |
| The brief | a script | the top, with each term linked at first use and listed with its gloss |

The weights and the top are written per reader. Everything else is shared.

## A brief is for a human

`formats/foundations.md` holds the rules for every format. Read it first. Its rules 1 and 2 bind a brief. What they mean here:

- The headline names the subject, in words this reader would use. The first sentence of the summary starts with the subject.
- You still end every sentence with the keys it rests on, as below. What you write is read by a script, not by a human. The script takes the keys out of the text and records them beside the brief. The reader never sees them.
- Keys do not count towards a word limit. The headline takes no keys.
- A term gets its explanation and nothing else. You do not write the explanations; the glossary is attached after you.
- Do not say what you left out.
- Do not tell the subject's history: what it replaces, that it was rewritten, or which draft this is. Say what it is.

## Weighting

This is foundations rule 7 at work: a format settles how deep it goes into the canon. A brief settles it chapter by chapter, by what its reader needs.

**Input.** One file: a description of the reader, the document's introduction, and every chapter with the shared summaries of its leaves.

**Task.** Share out 240 words among the chapters.

- Give a chapter words in proportion to how much of what this reader needs it holds. Go by the reader's "Needs" and "Does not need", not by how long the chapter is.
- A chapter that holds nothing this reader needs gets 0.
- No chapter gets more than 100. A chapter that gets anything gets at least 15.
- The total is at most 240.

**Output.** One YAML file:

```yaml
weights:
  C1: {words: 90, why: "…"}
  C6: {words: 0, why: "…"}
```

Give every chapter key an entry. Keep each `why` to one short sentence. Write nothing else to the file.

## The top

**Input.** One file. It holds:

- a relevance: a description of the reader;
- the document's introduction, key `C0`;
- every chapter with its word budget. A chapter with a budget of 50 or more comes with the canon's own text. A chapter with a smaller budget comes with the shared summaries of its leaves. A chapter with a budget of 0 is not shown.

**What to write.**

0. **The headline.** At most 8 words. It names the subject, in words this reader would use. It is not the canon's title if that title names the document.
1. **The document summary.** At most 3 sentences and 75 words. First what the subject is, then how it works, in the terms of what this reader needs. The first sentence starts with the subject.
2. **Each chapter that has a budget.** Within its budget. What the chapter holds for this reader. One sentence where the budget is under 50; several where it is more.

**The rule.** This is rule 5 of the foundations, as it applies here.

**Every sentence states only what the keyed material it cites states.**

- End every sentence with the keys it rests on, in square brackets: `[C1]` or `[C3.2, C3.3]`. Cite the document's introduction as `[C0]`. Cite a chapter by its key, or one of its sections by that section's key.
- You may compress. Cite everything a sentence rests on.
- You may not add a reason, an example, a number, a comparison, a judgement or a definition.
- Use the canon's terms exactly as written, and do not explain them.
- Do not cite rulings (`[D1.n]`), dates or decision identifiers. Say what is ruled, not that it was ruled.
- Use what the reader already knows. Do not spend words on it.
- Do not address the reader, and do not mention the relevance or the budgets.
- British spelling. One idea per sentence, except where you compress.

**Output.** One YAML file:

```yaml
headline: "…"
document:
  summary: "… [C0, C1]"
chapters:
  C1:
    summary: "… [C1] … [C1]"
  C6:
    summary: null
```

Give every chapter key an entry; a chapter with no budget gets `summary: null`. Write nothing else to the file.
