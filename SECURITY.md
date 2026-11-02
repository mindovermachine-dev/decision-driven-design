# Security policy

## Reporting a problem

**Report privately. Do not open a public issue.**

Email [emil@okkels-klein.dk](mailto:emil@okkels-klein.dk). You will get an acknowledgement within
five working days. If you do not, assume the message went astray and send it again. A silence is
a failure on our side, never a judgement about your report.

After acknowledgement you get an assessment and a plan. If we think it is not a security problem,
we say so and say why. You are credited when it is fixed, unless you ask not to be.

There is one maintainer, no fixed embargo and no bug bounty. A disclosure date is agreed with you,
not imposed on you.

## What this repository's security surface is

This repository is mostly a specification, so its surface is not the usual one. These are in
scope:

- **Material that must not be here.** Customer-identifying material in any file, prompt, session
  record or commit message; a real signing key, token or credential in a fixture or example. The
  worked examples use throwaway test keys under a declared test genesis, and no real key is ever
  used for a fixture (`DDD-dec-62`). A real one appearing is a vulnerability.
- **The Decision Provenance Protocol** (`spec/decision-provenance/`). Any way to make a record
  verify that its declared signer did not sign, to make two parties canonicalise one record
  differently, or to rebind a record to a decision or a What element it was not made for.
- **The checkers** (`scripts/`, the root `validate-core-order.py` shim, the `check*.py` and `build*.py` files).
  They read YAML and clone the pinned upstream ref. Any way a crafted file in a pull request makes
  them execute code, write outside the working tree, or report a clean result over an invalid
  graph.

Out of scope: a claim you believe is false. That is not a security problem; it is the most useful
kind of contribution, and it goes in an issue (see `CONTRIBUTING.md`).

## Supported versions

| Version | Supported |
|---|---|
| Latest release | Yes |
| Anything older | No |

The method is in preview (`DDD-dec-74`). Until 1.0 only the latest release is corrected.
