# Writing a reader's questions

You are given a description of a reader and a source document made of identified statements.

Write the ten questions this reader most needs answered in order to do their task, as their description states it.

Rules:
- Every question must be answerable from the source's statements. Do not ask what the source cannot answer.
- Choose by the reader's needs, not by what the document says most about. Do not write questions the reader's "does not need" line excludes.
- Each question asks for one thing.
- Do not use the wording of the statements in the question where a plain question will do.
- For each question, give the answer in one sentence, and the identifiers of the statements that answer it.
- Spread the questions across the document where the reader's needs allow.

Output one YAML file:

```yaml
- id: Q1
  question: "…"
  answer: "…"
  statements: [W1.1]
```

Write nothing else to the file.
