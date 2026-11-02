# Equivalence — `applications/sdlc/how-examples/README.md`

Old text: `e5a332d:applications/sdlc/how-examples/README.md`. New text: same path.

| # | Old: section and rule, in brief | New: document and section | Note |
|---|---|---|---|
| 1 | Companion to how.md §12 | Opening | same; section number dropped because how.md is restructured |
| 2 | Every record is `dpp/1`, pinned by the hash law of `spec/decision-provenance/`; built by build.py, checked by check.py | Opening; "Run it"; "Where this comes from" | same |
| 3 | Version 1 accepted provisionally, to be superseded against real identifiers, never edited | "Two versions of the records" | same; moved from the top to the end |
| 4 | Version 2 records list (`GEN`, `GRANT-how`, `TGT-*`, `IMP-*`, `ACC-1`, vendor `REST`); `REL@3` ships it | "Two versions of the records" | same |
| 5 | No version 1 record changed; build.py refuses to build if it would change one | "Run it"; "Two versions of the records" | same |
| 6 | The checker reads the landed `../what/examples/acme-shop.ttl`; `what/acme-shop.ttl` here is history | "The What, as decisions"; "Two versions of the records" | same |
| 7 | Projector readings `facts/*.r2.ttl` are new; `r1` files stay, unread | "The facts"; "Two versions of the records" | same |
| 8 | `DDD-dec-65`..`71` supersede `55`..`61` on the same terms | "Where this comes from" | same |
| 9 | The What as decisions: `GRANT-what@1`, `WHAT-found@1` anchored at the product node, `ACC-what@1`, `what@1` | "The What, as decisions" | same |
| 10 | Version 1's pins still hold and are checked, as history | "Two versions of the records" | same |
| 11 | A test product; nothing acceptable into a real product | Opening, "How settled this is" | same |
| 12 | Provisional → landed identifier table | "Two versions of the records" | same, unchanged |
| 13 | "105 ok or note lines, 1 expected warning, 0 failures; all 36 records conformant" | "Run it": 112 lines, 38 records, re-run 2026-11-02 | corrected: the old counts were stale; re-run at this commit |
| 14 | Records rebuilt with `dpp/1` and fresh test keys (Round 3); the `decprov/1` set was never conformant, in history at `d11df86` | "Run it" (fresh keys); "Where this comes from" (`d11df86`) | same |
| 15 | build.py refuses to build if `main`'s token and `DDD-dec-62` disagree | "Run it" | same, without the id |
| 16 | Without rdflib, anchor and verdict steps are SKIP, never passed | "Run it" | same |
| 17 | The cast table; throwaway ed25519 keys; no real key ever used or held by a session; `ssh-sig`, namespace `decision-provenance` | "The cast" | same |
| 18 | The three decisions table; no target named in statement or violation description; check.py checks it | "The three decisions, written once" | same; residency anchor cited as "the residency quality demand in the What" instead of "what.md §3.6, Kind 2" |
| 19 | `REST@2`: binding, `POST /commands/{wire name}`, supersedes `REST@1`, anchored at the Ordering bounded context, reads the wire name | "The three decisions"; "Where this comes from" | same |
| 20 | `what@3` supersedes `what@2` supersedes `what@1`; same graph; edition named by hash; pins at `2c4f276` and `655db92` | "The What, as decisions" | same; the old text stated the `what@2` paragraph twice |
| 21 | `REL@2` supersedes the layer rule with `LAYER@2` (adds `test`); importer rests on version 1; check.py shows nothing in force changed | "The three decisions" | same |
| 22 | Two targets: C#/Azure and TypeScript/AWS; per-target shape only in edition records; second language touched no decision | "Two targets each" | same; one sentence added: "To add a third target, do the same", which restates the rule for the reader's act |
| 23 | Both fact-term tables | "Two targets each" | same, unchanged |
| 24 | No projector or reporter exists; fact files hand-written; manifest gives provenance | "The facts" | same |
| 25 | "The What graph in `what/` is provisional too (`../how.md` §1.2)" | "Two versions of the records" | same |
| 26 | Planted defects table; expectations analytic, not evidence; shows nothing about whether the How is right | "The facts"; opening, "How settled this is" | same |
| 27 | `RESID@1` requires both provenance values in its `factSources` | "The three decisions" | same |
| 28 | What check.py checks, items 1–9 | "What the checker checks", items 1–9 | same; item 4's "test stand-in for the unwritten authority profile" kept as "a stand-in check for the authority profile, which the checker does not yet implement"; item 8's "ruling 1" moved to the basis table |
