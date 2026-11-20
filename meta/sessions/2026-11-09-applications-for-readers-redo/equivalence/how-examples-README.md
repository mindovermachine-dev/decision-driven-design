# Equivalence — `applications/sdlc/how-examples/README.md`

Old: `84aa466`. New: this session's working tree. The sections are reordered for a reader who
wants to run the example first: run, cast, decisions, targets, facts, checks; the history last.

| # | Old: rule or statement, in brief | New: section | Note |
|---|---|---|---|
| 1 | Companion to how.md §12; every record `dpp/1` (token `DDD-dec-62`, superseding `-53`), pinned by the hash law; built by build.py, checked by check.py | opening | same; ids to the table |
| 2 | Version 1 records accepted provisionally (ruling 4); to be "superseded by a version against the real identifiers, never edited"; the What has landed in the identity form (`DDD-dec-63`) | How the records came to be: Superseded against the landed What | same; ruling and decision ids to the table |
| 3 | Version 2 records: `GEN`, `GRANT-how`, both `TGT-*`, all four `IMP-*`, `ACC-1`; and the vendor's `REST`; `REL@3` ships it | same | same |
| 4 | Nothing edited; build.py refuses to build if it would change one | same | same |
| 5 | The landed What is read; `what/acme-shop.ttl` is provisional history, no longer read | same | same |
| 6 | New readings `facts/*.r2.ttl`; `r1` files stay, unread | same | same |
| 7 | `DDD-dec-65` to `-71` supersede `-55` to `-61` on the same terms | same ("The How's decisions were superseded on the same terms"); ids in the table | same |
| 8 | The What itself as decisions: `GRANT-what@1`, `WHAT-found@1`, `ACC-what@1`, `what@1` | same | same |
| 9 | Version 1's pins still hold and are checked, as history. Still a test product; nothing acceptable into a real product | same; How settled this is | same |
| 10 | The provisional-to-landed table | same | same, verbatim; "ruling 1" written "the anchor rule" |
| 11 | Under the authority profile: a positioned log with **16 positions**; 25 records added, none edited | Under the authority profile (2026-11-02): "On 2026-11-02 it had 15 positions, and 25 records were added" | fact corrected: #45 shipped 15 positions; p16 (`SCN@1`) came with sdlc edition 1 on 2026-11-06 (`8a5b4e9`). The old text listed `SCN@1` inside the 2026-11-02 list |
| 12 | The list: `GEN@3` and the vendor's `GEN@2`; grants; re-acceptances with a baseline; `CUR@1` and `what@4`; delegation and revocation; rotation; waiver; review; two refusals | same | same; A-5, P-9 to the table. The old text's missing full stop after "signed" restored |
| 13 | `SCN@1` at p16: creates the scenario for (Place order, Customer), fills four descriptions, no findings under edition 1; `what@5`; `what@3` and `what@4` keep their edition hash | sdlc edition 1 (2026-11-06) | same; "accepted by `ACC-scn-what@1`" added, from `records/acme/ACC-scn-what` |
| 14 | Stand-in records stay as history, at no position, put nothing in force; build.py needs rdflib; refuses to rewrite a landed header; keys kept in `test-keys/`, never used outside; a rebuild reproduces every record; a later session can extend | Under the authority profile, last paragraph | same |
| 15 | The run command; "225 ok or note lines, 1 expected warning, 0 failures. All 64 records (26 of them written on 2026-11-02)" | Run it | fact corrected by a fresh run: 238 ok or note lines, 1 expected warning, 0 failures; 67 of 67 records conformant. 27 records date from 2026-11-02 (25 + `what@3` + vendor `GEN@2`), not 26; three added 2026-11-06 |
| 16 | Rebuilt with `dpp/1` and fresh keys on 2026-10-28; the `decprov/1` set never conformant, at `d11df86`; build.py refuses if the token and `DDD-dec-62` disagree; without rdflib, SKIP, never passed | Run it | same; "the ruled token" for `DDD-dec-62` |
| 17 | The cast table | The cast | same, verbatim |
| 18 | Throwaway keys for v1/v2; since Round 2 of 2026-11-02, keys kept in `test-keys/`; no real key ever used or held by a session (Round 3, ruling 1); `ssh-sig`, namespace `decision-provenance` | The cast | same; round numbers to the table |
| 19 | The three decisions, held once, no target named; check.py checks it; the decisions table | The three decisions, written once | same, verbatim |
| 20 | `REST@2`: a binding at `POST /commands/{wire name}`, the third "specified once" check; supersedes `REST@1`; anchored at the bounded context; reads the wire name, ruled in Round 2 (`DDD-dec-64`, P-1: "REST@2 stands") | same | same; "So Acme Shop imports four How decisions" added, verified against `records/acme/IMP-*` and check.py ("four imports") |
| 21 | `what@3` supersedes `what@2`, which superseded `what@1`; each kept the graph and renamed the edition by the hash of the files as amended before edition 1 was tagged; `what@2`'s pin held to `655db92`; `what@1`'s pin the files at `2c4f276` | What-versions 2 and 3 | same; the old paragraph's repetition merged |
| 22 | `REL@2` supersedes the layer rule with `LAYER@2` (adds `test`); the importer still rests on version 1; check.py shows it; nothing in force changed | The three decisions, written once | same |
| 23 | Two targets each; the two fact-term tables | Two targets each | same, verbatim |
| 24 | The facts, hand-written; manifest; What graph in `what/` provisional too (how.md §1.2); planted-defect table | The facts, and what is hand-written | same, verbatim |
| 25 | Expectations analytic, not evidence; "It shows nothing about whether the How is right" | same; How settled this is | same |
| 26 | `RESID@1` requires both provenance values | same | same |
| 27 | What check.py checks, 1 to 9 | What `check.py` checks | same, verbatim except item 8: "(ruling 1)" removed, "The ruling calls" became "The anchor rule calls" |
