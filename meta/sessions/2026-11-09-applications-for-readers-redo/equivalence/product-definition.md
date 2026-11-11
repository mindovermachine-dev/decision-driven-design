# Equivalence — `applications/sdlc/product-cli/product-definition.md`

Old text: `84aa466:applications/sdlc/product-cli/product-definition.md`. New text: same path. Every
chapter number and section heading is kept. The rewrite moves the inline ruling markers
(`[D1.n]` with their dates), decision ids, ADR numbers and item numbers (P-, R-, E-, M-) out of the
running prose into "Where this comes from", keyed by chapter and section. No sentence of the body
changes otherwise, except the rows below. #48 did not rewrite this document (it was not on
#48's base).

| # | Old: section and rule, in brief | New: section | Note |
|---|---|---|---|
| 1 | Header: "Draft 4, 2026-11-03 (Draft 3 ...; Draft 1, 2026-10-21)" | "How settled this is" (Draft 4, of 2026-11-03); the draft history in "Where this comes from" | moved |
| 2 | Header: written outside-in; chapters 1 to 6 are the product; chapter 7 may change without the product changing | Opening, second paragraph | same |
| 3 | Header: the definition replaces the Rust workspace; it lives here; tool, ADRs, tests in product-cli; carry-over in ch. 8; "it was like that before" is not a reason | Opening, first paragraph | same; `[D1.24]` moved |
| 4 | Header: rulings marked `[D1.n]`; Drafts 2 and 3 add D1.2–D1.15 (ADR-0010–0012, on `dpp/1` 1.0 draft of 2026-10-27); Draft 4 adds D1.16–D1.25 from gate checks A1–A8 against the named commits; D1.24 supersedes D1.23; D1.25 adds step 0; superseded rulings keep their number and the text states the ruling in force | "Where this comes from", "Drafts" paragraph; "How settled this is" | moved; the rule "the text states the ruling in force" kept in both places |
| 5 | Every inline `[D1.n]` marker with its date (D1.1–D1.25, including "amended by" and "superseding" notes) | "Where this comes from", one row per section | moved; each marker's supersession note kept in its row (D1.3 by D1.16; D1.7 and D1.14 superseded; D1.9 by D1.20; D1.4 by D1.18 and D1.21; D1.23 by D1.24; D1.22 amending Draft 3's clause) |
| 6 | Ch. 3 "**Open.** Some kinds are in the vocabulary but have no `domain new` kind ... Either they gain kinds, or the definition names the verb" | Ch. 3 "*(open)*"; "Not settled yet" | same register, in the ruled phrase |
| 7 | Ch. 3 interactions, fields, state annotations, content keys "are elements by `DDD-dec-64` P-3" | "which are elements by the rule \"anything a binding, a baseline, reads, a scope key or a wire request names is an element\"" | same; P-3 quoted verbatim, as a short test, id in the table |
| 8 | Ch. 3 MCP "by elicitation answered by the author (D1.15)" | "(\"Adopting on the fly\")" | same; the cross-reference names the section that states D1.15 |
| 9 | Ch. 4 "Element identity is the ruled form of `DDD-dec-63`" | "the What's ruled identity form (`what.md` §2.2 and §2.3)" | same; id in the table |
| 10 | Ch. 4 "as `DDD-dec-72` rules" (edition pinned by versionIRI and hash) | "as decision-driven-design rules for its editions" | same |
| 11 | Ch. 4 "The one hash law (D1.3)" | "(\"The canonical export\", below)" | same |
| 12 | Ch. 4 regime "ruled in `DDD-dec-113`, E-1 and E-2; `what.md` §7.2"; warning clause "(`DDD-dec-113`, E-2)" | "(`what.md` §7.2)"; clause unchanged | same; ids in the table |
| 13 | Ch. 4 canonical document "under the hash law of `DDD-dec-73`" | "under decision-driven-design's hash law for the What (`what.md` §2.3)" | same |
| 14 | Ch. 4 logic digest and media type "as `DDD-dec-63` §6 rules"; element hash "(`DDD-dec-63` §4, `what.md` §2.3)"; What-version "`DDD-dec-63` §6's record"; logic held by digest "(`DDD-dec-63` §6)" | `what.md` §2.3 in each place | same; `what.md` §2.3 states each of these |
| 15 | Ch. 4 "M-12's second implementation stays Varve's published vectors (`DDD-dec-73`)" | "The conforming second implementation of the canonical form that decision-driven-design is waiting for stays Varve's published vectors" | same; M-12 and the ids in the table |
| 16 | Ch. 5 "W3 and W4 are its warnings (`DDD-dec-113`)" | same without the id | same |
| 17 | Ch. 6 "under the regime of D1.19"; ch. 7 "hash-checked at build (D1.20)" | "(chapter 4, \"Shapes\")" | same |
| 18 | Ch. 7 "(ADR-0005)"; step 0 "(ADR-0002, ADR-0003, ADR-0004)" | "(a product-cli ADR)"; ADR numbers in the table | same |
| 19 | Ch. 7 "`[D1.23]` is superseded by D1.24. It put the rewrite in a new repository." | "**Where it lives.** An earlier decision put the rewrite in a new repository; this one replaced it." | same |
| 20 | Ch. 7 lift: ownership edges become `sdlc:within` "(`DDD-dec-64` P-2)"; blank nodes become elements "(P-3)"; wire names "(`what.md` §6, R-1, R-2)" | "the What's single containment edge"; "by the same rule that makes interactions and fields elements (chapter 3)"; "(`what.md` §6)" | same |
| 21 | — | — | (row withdrawn: a first restatement of P-3 dropped "reads"; replaced by the verbatim quote in row 7) |
| 22 | Ch. 7 behaviour fixture "*Amended 2026-11-06 (decision-driven-design `DDD-dec-113`, E-5):* it was `acme-shop-4.ttl` ... lacks the (Place order, Customer) scenario and the E-7 descriptions" | "It was `acme-shop-4.ttl` and `vectors-4.json` until 2026-11-06 ... lacks the (Place order, Customer) scenario and the descriptions edition 1 asks of every domain, bounded context and subject kind" | same; E-5 and E-7 in the table. E-7 asks a Domain for `sdlc:purpose`, and a Bounded Context and a Subject Kind for `sdlc:definition` |
| 23 | Ch. 7 step 1 "Edition 1 shipped in ... `v0.6.0` (`DDD-dec-113`)" | same without the id | same |
| 24 | Ch. 8 declared targets "(`what.md` §4.1, `DDD-dec-57`)" | "(`what.md` §4.1)" | same |
| 25 | Ch. 8 "through the D1.21 lift" | "through the lift (chapter 7)" | same |
| 26 | Ch. 8 interim rule "of Writ ADR 0008" | "Writ's interim rule for ADRs" | same; ADR 0008 in the table |
| 27 | Ch. 8 subjects "adopted from the unmerged v1.11.0 by ruling, 2026-10-28" | "adopted from the Product Framework's unmerged v1.11.0" | same; the ruling and date in the table |
| 28 | Ch. 8 "The checks this tool needs that `what.md` §3.7 still marks `[OPEN]` are the subject half of W3 and claim justification. They are in edition 1 as warning shapes (`DDD-dec-113`, E-4)" | "The checks this tool needs for subjects, the subject half of W3 and claim justification, are in edition 1 as warning shapes (`what.md` §3.7)" | fact corrected: `what.md` §3.7 has had no `[OPEN]` mark since `8a5b4e9` (edition 1), which says `shapes.ttl` "carries all of it". Recorded in "Where this comes from" |
| 29 | Cross-repository table: "Ruling" column keyed by D1.n; states citing `DDD-dec-113` (E-1, E-2, E-4), `DDD-dec-73`, E-3, M-12, `DDD-dec-63` §6, "withdrawn with D1.7 (D1.16)" | "Needed for" column naming the section; states in words | same states (met, open, to deliver, withdrawn, amended); the ids in the closing table's last row |
| 30 | Every other sentence of chapters 1 to 8 and the table | unchanged | same |
