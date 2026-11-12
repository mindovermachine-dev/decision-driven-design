# Verifying a brief against its canon

You are given a brief, the canon it was derived from, and a key map. Every sentence of the brief's first two sections ends with keys in square brackets, such as `[C1]` or `[C3.3, C3.6]`. The key map says which part of the canon each key names.

For every sentence of the document summary and of "Chapter by chapter", decide whether the parts of the canon it cites support it.

| Verdict | Meaning |
|---|---|
| supported | Everything the sentence states is stated in the cited parts. |
| partly | The cited parts state most of it. One element is stronger, broader or different from what they state. Name the element. |
| unsupported | The sentence states something the cited parts do not state, or contradicts them. Name it. |
| miscited | The canon supports the sentence, but in a part the sentence does not cite. Name the part. |

Then, for every entry under "Terms used here" that gives an explanation, decide whether the section named in italics after it supports the explanation. Use the same verdicts. You may open the named file for this. Entries that say "not explained in the canon" are not checked.

Rules:
- Judge only against the text of the canon. Do not credit what you know or could infer.
- A faithful compression is supported. A changed subject, a dropped condition that changes the meaning, or an added claim is not.
- Be strict. Quote the canon's words when you give a verdict other than supported.

Output one YAML file:

```yaml
sentences:
  - text: "first words of the sentence…"
    cites: [C1]
    verdict: supported
    note: null
glosses:
  - term: the What
    verdict: supported
    note: null
summary: {supported: 0, partly: 0, unsupported: 0, miscited: 0}
```

Write nothing else to the file.
