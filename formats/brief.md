---
format: brief
version: 1
status: trial
tracking: mindovermachine-dev/decision-driven-design#75
---

# Format: brief

**Trial, `[PROPOSED]`.** Instructions for a model that derives a brief from a `<name>.source.md` file.

## What a brief is

A brief is the source read from the top, stopped early. It gives the document's introduction, then each chapter's introduction, then the headlines beneath. It goes no deeper.

| | |
|---|---|
| Reader | The person who authorises the work. They have not read the source. |
| Reader's task | Decide whether to authorise, continue or stop. |
| Reading time | Two minutes. |

## Inputs

You are given exactly two inputs beside this file:

1. One source file, `<name>.source.md`.
2. One culture file, `cultures/<culture>.md`.

Read nothing else. Do not use what you know about the subject from any other place.

## How a source is built

A source has the shape of any written document.

| Mark | Meaning |
|---|---|
| `#` | The document's headline. |
| `##` | A chapter's headline. Chapters are in reading order. |
| `###` | A section's headline, led by its identifier (`### W1 Shape before storage.`). A section headline is a statement and may be cited by its identifier. |
| `**Introduction.**` | The statements that follow introduce the document, or the chapter, they stand in. |
| `- **ID** text {…}` | One statement. The braces hold fields that are not content. |

Order and position carry meaning. What stands higher and earlier is what the document is for. What stands lower and later is how. An `## Appendix` is not content.

## The one rule

**Every sentence of the body states only what cited source statements state.**

- End every sentence and every bullet with the identifiers it rests on, in square brackets: `[W1.1]` or `[P1.3, P1.4]`.
- You may compress several statements into one sentence. Cite all of them. This takes precedence over the culture file's rule of one idea per sentence.
- You may not add a reason, an example, a number, a comparison, a judgement or a definition that no cited statement contains.
- You may not explain a term the source does not explain. Use the source's term as it stands.
- A statement with `depends-on` is a consequence of the statement it names. Present it as one, or leave it out.

If the reader's task needs something the source does not hold, do not write it. Record it under `gaps` in the frontmatter, one line each. A gap is a finding about the source, not a failure of yours.

## What to render

Follow the source's own order. Do not regroup it.

1. **The document's introduction.** Render it as a short paragraph under the document's headline.
2. **Each chapter, in order.** Use the chapter's headline as a `##` heading, without its number.
   - Render the chapter's introduction as a short paragraph.
   - Then list the chapter's section headlines, one bullet each, in order, each cited by its section identifier.
   - Do not render the statements inside a section. The one exception: where a section headline is a bare label that asserts nothing (for example "Coverage."), add the section's first statement to its bullet, so the bullet says something.
3. **Open for review.** A last `##` section. List every statement whose `note` contains `UNVERIFIED`, and say what is unverified in the note's own terms. You may name a ruling here. Write "Nothing." if there are none.

There is no word limit. The depth rule sets the length.

## Output

Write one file, `<name>.<culture>.brief.md`, beside the source. It begins with this frontmatter:

```yaml
---
name: <name>
culture: <culture>
format: brief
derived-from: <source file name, without path>
source-blob: <the hash you were given>
format-version: 1
culture-version: <version in the culture file>
rendered: [<every identifier cited in the body, in source order>]
gaps: [<one quoted line per gap; [] if none>]
---
```

Then the document's headline as the single `#` heading, then the body as described. Nothing else.
