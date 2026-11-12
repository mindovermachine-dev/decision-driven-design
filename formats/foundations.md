# What holds for every format

A file that a human will read starts with the information itself, and holds nothing its reader does not need. Everything else about the file is kept beside it.

These rules are the same for any format. A format's own file says only what is particular to it.

## For a human reader

Ruled by Emil on 2026-11-12. A human expects a quick and easy start to the information. If they do not get it, they stop and do something else. A model does not. This is a fundamental difference between the two.

### 1. Never start with information about the content

The file opens with a headline that names the subject, and a first sentence that starts with the subject itself: what the thing is or does.

| Do not open with | Open with |
|---|---|
| Frontmatter | The headline. |
| "This is the definition of the rewritten tool." | "The tool turns … into …" |
| "This document describes …" | The thing described, doing what it does. |
| "Draft 4, superseding draft 3." | Nothing of the kind. |
| A status note, a table, or how to read the file | The first thing the reader came for. |

### 2. Hide or remove anything that is not important for the reader

What the reader does not need goes beside the file, in the set's projections file. It is not deleted; it is kept where a check can read it.

| Not for the reader | Where it goes |
|---|---|
| Provenance: what the file was derived from, and when | The projections file |
| Citation keys: which part of the canon a sentence rests on | The projections file, sentence by sentence |
| Where an explanation of a term was taken from | The projections file |
| What was left out for this reader | The projections file |

A status the reader must know to read the file rightly, such as "nothing here is ruled", is for the reader. It goes at the end.

## For every projection

Accepted by Emil on 2026-11-12. Rules 5 to 7 were proposed by Claude and accepted the same day.

### 3. Canon is the centre

A projection is derived from the canon, never the reverse. The canon depends on no projection.

The canon will mostly be read and projected by models, and it is labelled as such. Rules 1 and 2 do not bind it. A human reads a projection of it.

### 4. Terms are served to the reader

A term is available where the reader meets it, or in a separate list where they look it up. A word is a term when a statement depends on its precise meaning here, and a newcomer's ordinary reading would get it wrong.

### 5. Nothing is added

Every sentence of a projection states only what the canon states. It may compress and it may leave things out. It may not add a reason, an example, a number, a judgement or a definition.

### 6. A format declares its reader

A format says whether its files are read by a human or by a model, as the canon already does under rule 3. Rules 1 and 2 bind a file for a human. A file for a model, such as an index or a set of stored summaries, may lead with what a model needs first.

### 7. What a format's own file settles

How deep the projection goes into the canon, which paths through it the projection follows, and how terms are served.

## How the rules are checked

| Rule | Check |
|---|---|
| 1 | Mechanical. A file fails if it starts with frontmatter, a note or a table, or with words such as "This document", "Draft", "Status" or "Trial". |
| 2 | Mechanical for citation keys. A file fails if it shows them. |
| 3 | The projections file records the canon's hash. A projection is stale when the hash has changed. |
| 4 | Every term a projection uses is listed with its explanation, or is shown as not explained. |
| 5 | A separate model reads each sentence against the parts of the canon it rests on. |

---

*Tracked in mindovermachine-dev/decision-driven-design#75. All seven rules are ruled or accepted by Emil (2026-11-12). They have been exercised on one canon and one format, on a trial branch.*
