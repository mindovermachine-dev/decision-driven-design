# Decision Provenance Protocol (`dpp/1`)

A system-agnostic protocol through which any system that records decisions can expose them, so
that a decision in one system can reference, by pinned version, the decisions in others it rests
on, and anyone can walk the chain back to its origin. It fixes three things: the record shape,
the resolver, and the hash law.

| Path | What |
|---|---|
| [`dpp-1.md`](dpp-1.md) | The specification, version 1.0 (draft). Appendix A holds the decisions: every departure from Draft 3 and the answers to the five open questions. |
| [`suite/`](suite/) | The conformance suite: canonicalisation vectors, a resolver fixture, a three-system chain fixture, a runner, and hash-only JavaScript and Go cross-checks (hash function only; not readers). |
| [`reference/dpp.py`](reference/dpp.py) | The reference implementation, and the measure of the size budget: hash law with input checks in 30 non-blank lines; with the file-based resolver and walk, 99 lines. Python standard library only. |
| [`example/`](example/) | Worked example: an ADR directory made conformant with no code, and a rules engine referencing one of its ADRs. |

Run the suite:

```
python3 suite/run.py                                   # 65 checks against the reference implementation
node suite/crosscheck/hash.js suite/canonical/vectors.json   # hash-only
go run suite/crosscheck/hash.go suite/canonical/vectors.json  # hash-only
```

`suite/run.py path/to/module.py` runs the same checks against another Python implementation.

Source: Part 1 of *The Decision Provenance Protocol, Writ's authority profile, and the
architecture*, Draft 3 (2026-10-22). Parts 2 and 3 of that draft are one vendor's profile and
architecture; they appear here only as the non-normative Appendix B of the specification.
