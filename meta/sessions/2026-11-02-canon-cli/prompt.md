# Prompt — the canon CLI, 2026-11-02

The session prompt, verbatim, as given at invocation. Per `DDD-dec-20`, this file is committed
before any other file changes, so the session's scope is fixed at arrival.

---

New session: the canon CLI, 2026-11-02, in mindovermachine-dev/decision-driven-design.
Open an issue for it and put Refs #N on every commit. Commit prompt.md and bootstrap.md
under meta/sessions/2026-11-02-canon-cli/ before anything else. Check decision ids on
every branch of both repositories before filing; DDD-dec-83 is never used, and the
authority-profile session starts at 85.

## Charter: Emil's rulings, verbatim (claude.ai question dialog, 2026-11-02)

Emil: "all these scripts and file etc. I think we need a proper C# CLI for managing the
repo, we should base it on Varve"

Q: "product-cli (Rust) already ships `ddd`, a Decision-Driven Design governance CLI over a
.ddd/ graph, and the project instructions name product-cli as the tooling home. How
should a C# repo CLI relate to it?"
A: "C# for this repo, ddd for products" (option text: "C# governs the canon repositories.
product-cli's `ddd` governs product repos that apply the method")

Q: "What form should the C# tooling take?"
A: "A dotnet tool" (option text: "A packaged CLI (`dotnet tool install`) with subcommands,
reusable from other repos")

Q: "Should the C# gates validate the claim and decision graph through Varve (Turtle and
SHACL shapes), replacing the Python validators after a parallel run?"
A: "Yes, SHACL via Varve (Recommended)" (option text: "Shapes for claims, decisions and
releases come first. The Python validators run in parallel until every fixture agrees,
then are retired by decision")

Q: "Where should the C# canon tool live?"
A: "inside decision-driven-design untill we can see the need to split it out"

Q: "What should the tool and its command be called?"
A: "canon"

Reading, UNVERIFIED — Emil review: canon serves this repository first.
actor-indexed-determination adopting it is the expected trigger for splitting it out.

## Gate 1 — decisions and design, no code

File the rulings as decisions:
- the boundary between canon and ddd
- the form: a dotnet tool under tools/canon/, and the split trigger
- SHACL via Varve, the parallel run, and retirement by decision

Then write tools/canon/DESIGN.md. Name the weakest point first: a gating dependency on a
preview Varve (0.1.0-preview.15 on nuget.org, checked live). The design covers:

- **Layout, following Varve's conventions:**
  - net10.0, current C#, central package management, MPL-2.0 headers
  - Detroit-style tests against real fixtures, no mocks
- **Commands, each mapped from the script or manual step it replaces:**
  - `canon check`: every gate, replacing scripts/ci.py
  - `canon land`: Varve's land.cs semantics; never a GitHub merge
  - `canon release`: descriptor, guard, signed tag, GitHub Release. It refuses if the tag
    already exists anywhere, checked with ls-remote. That is today's v0.5.0 lesson.
  - `canon ratify`: fills ratified_head
  - `canon changelog`
  - `canon issue-refs`
  - `canon pins`: replaces validate-core-order.py; fix R-7 while porting
- **SHACL shapes for the graph:** claims, decisions and releases first, then the What. A
  JSON-LD context or a YAML-to-RDF mapping for the existing YAML files, without changing
  the files.
- **What stays Python:**
  - the dpp/1 reference implementation and the How examples, kept as the protocol's
    independent implementation
  - the papers' checkers
  - the primer generator
  Say why for each.
- **The parallel-run plan:**
  - `canon check` and `scripts/ci.py` both run in CI.
  - Every fixture must give the same verdict from both.
  - A disagreement is a defect in one of them, recorded and not suppressed.
- **Devcontainer and CI changes:** the .NET SDK beside Python.

Write predictions before any operation. Stop at Gate 1 for Emil's review.

## Later gates, after Emil's review

- Gate 2: build canon's repo operations (land, release, ratify, changelog, issue-refs)
  with tests.
- Gate 3: the shapes and `canon check` running in parallel with the Python gates.
- Gate 4: the decision retiring each Python validator, after full agreement.
