---
format: brief
version: 0
status: trial
tracking: mindovermachine-dev/decision-driven-design#75
---

# Format: brief

**Trial, `[PROPOSED]`.** Instructions for a model that derives a brief from a `<name>.source.md` file.

## Reader and purpose

| | |
|---|---|
| Reader | The person who authorises the work. They have not read the source. |
| Reader's task | Decide whether to authorise, continue or stop. |
| What they need | What the thing is, what it commits to, what it refuses to do, and what is unsettled. |
| Reading time | Two minutes. |

## Inputs

You are given exactly two inputs beside this file:

1. One source file, `<name>.source.md`. Its fenced YAML blocks hold statements. Each has an `id`, and either a `title` (a group) or a `text` (a statement).
2. One culture file, `cultures/<culture>.md`.

Read nothing else. Do not use what you know about the subject from any other place.

## The one rule

**Every sentence of the body states only what cited source statements state.**

- End every sentence, bullet and table cell with the identifiers it rests on, in square brackets: `[W1.1]` or `[P1.3, P1.4]`.
- You may compress several statements into one sentence. Cite all of them.
- You may leave statements out.
- You may not add a reason, an example, a number, a comparison, a judgement or a definition that no cited statement contains.
- You may not explain a term the source does not explain. Use the source's term as it stands.
- A statement with `follows-from` is a consequence. Present it as one, or leave it out. Do not present it as independent.

If the reader's task needs something the source does not hold, do not write it. Record it under `gaps` in the frontmatter, one line each. A gap is a finding about the source, not a failure of yours.

## Required content

- Every group must be represented. Cite the group's identifier, or at least one statement in it.
- Every statement whose `note` contains `UNVERIFIED` must appear in the last section.
- Entries of kind `ruling` are not content. Do not render them.

## Structure

Use these sections, in this order, with these headings.

| Section | Content | Limit |
|---|---|---|
| `## What it is` | The thing, in the source's own terms. | 2 sentences |
| `## What it commits to` | The commitments that matter to someone authorising the work. Group them; do not list every statement. | 8 bullets |
| `## What it does not do` | The refusals and limits the source states. | 5 bullets |
| `## Open for review` | The `UNVERIFIED` statements, each with what is unverified. Write "Nothing." if there are none. | as needed |

The body is at most 350 words. Count before you finish.

## Output

Write one file, `<name>.<culture>.brief.md`, beside the source. It begins with this frontmatter:

```yaml
---
name: <name>
culture: <culture>
format: brief
derived-from: <source file name>
source-blob: <the hash you were given>
format-version: 0
culture-version: <version in the culture file>
rendered: [<every identifier cited in the body, sorted>]
gaps:
  - <one line per gap, or an empty list>
---
```

Then a single `#` heading naming the subject, then the four sections. Nothing else.
