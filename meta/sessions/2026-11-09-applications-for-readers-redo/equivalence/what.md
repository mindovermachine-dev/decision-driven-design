# Equivalence — `applications/sdlc/what.md`

Old: `84aa466:applications/sdlc/what.md` (922 lines). New: this branch (995 lines). The writer's
table, per `gate-b-conventions.md` §7. It is not evidence of equivalence; the independent check is.

**Method.** Every numbered section keeps its number, its order and its file. Every rule's sentence
is kept, with only these edits: decision, round, Q-/P-/R-/E-/H- ids and `PF §` citations removed
from running text and moved to "Where this comes from"; "*Ruled (…)*" lead-ins removed (decided is
the default); "v1.11.0" / "PF §x" as an attribution became "the source" where a sentence needs a
subject. Product Framework quotations are kept verbatim, without their citations; the opening says
that quoted passages are the source's text. Rows below are grouped by section; a row marked
`same` means every normative sentence of that section is word for word, apart from the id and
citation edits above.

| # | Old: section and rule, in brief | New | Note |
|---|---|---|---|
| 1 | Opening "Status: moved, 2026-10-28; not yet ratified … Emil ratifies by merging" | Opening, "How settled this is": ratified when its pull request merged | `fact corrected`: #42 merged; `DDD-dec-64`'s made line names acceptance of the pull request as the ratification act |
| 2 | Opening: move session, source repository and commits, v1.11.0 adopted by ruling | "Where this comes from", "The source" | `removed: history` from the body; kept in the closing |
| 3 | "Register" paragraph (*Ruled*, `[PROPOSED]`, `[OPEN]`, PF quoting) | Opening "How settled this is" and "How to read it" | Register words per Round 2. No `[PROPOSED]` point exists in the old body; the one `[OPEN]` point stays *(open)* |
| 4 | Companions list | Companions | `same` |
| 5 | — | Opening: reader, act, how to read, the worked example in brief | new framing; every example fact checked against `acme-shop.ttl` (one domain Ordering; systems `shop-api`, `shop-bff`; Customer issues Place order and Refund order; scope rules "customers see their own orders", "staff see every order"; `shop-bff` targets GUI, context `web`) |
| 6 | §1.1 the What; a system is not a coordinate; declared ground over which decisions are made; step 1 reads addresses off the What | §1.1 | `same` ("Read with `DDD-dec-42`" moved to closing) |
| 7 | §1.2 table, seven rows | §1.2 | `same`, ids to closing. Force row: "in their own pull request after this one … *Update, 2026-11-02:* authority.md" became "the authority profile, `authority.md`" (`removed: history`; the profile now exists) |
| 8 | §1.3 table: eleven rulings with their decisions | §1.3, eleven bullets in the same order; decisions in the closing table, in the same order | `same` in substance. "§9 cut down … §10 one level" restated as "Encoding … cut down … conformance to one level" (PF section numbers are source citations) |
| 9 | §2.1 three rules; gathered material enters only when a human principal signs and accepts it "(§8)" | §2.1, pointer "(§5)" | `fact corrected`: old §8 is the move's choices table; signing and acceptance is §5 |
| 10 | §2.1 creating decisions anchor to the narrowest existing covering element; product for a new domain; never its own anchor; "How ruling 1 applied to the What" | §2.1, "the How's anchor rule (how.md §3) applied to the What" | `same`; quoted ruling kept verbatim |
| 11 | §2.2 identity (five bullets), containment, what is an element | §2.2 | `same` |
| 12 | §2.3 record, canonical form, hashes, equalities, no force; ontology never hashed; vectors; pyoxigraph/pyld; second implementation "successor item M-12 (`DDD-dec-73`): Varve's published vectors"; Varve preview.15 reproduction "Recorded" | §2.3 | `same`; "successor item M-12" restated as "still to come", item number in the closing |
| 13 | §3 intro quotes; one or more domains and systems; system references whole domains; `within`, `referencesDomain` | §3 | `same`; one example line added (checked) |
| 14 | §3.0 product concerns; direction not carried; boundary quote; second genesis | §3.0 | `same` |
| 15 | §3.0.1 journey definition, edges, owns nothing, three rules; "the old journey payoff named value-anchoring and blast radius" | §3.0.1 | `same` for rules; the "old payoff named" clause shortened to "Blast radius stays … Value-anchoring went with Delivery" (`removed: history`, the two outcomes kept) |
| 16 | §3.1 contents; structure quote; every box says what it is; mapping direction; strategic patterns are How; field datatypes; reference data quote and test; production data and data conformance not framework | §3.1 | `same`. "PF §3.1's three callouts … describe §13's profile" became "The source's three callouts … describe a data-conformance profile". One example line added (checked: `Order`'s three fields and three invariants) |
| 17 | §3.2 three bullets | §3.2 | `same` |
| 18 | §3.2.0 blocks, patterns, two rules; trigger source and subject; nature admitted per source; payload schemas; slices | §3.2.0 | `same`. "v1.11.0 called this edge `acts_as`" → "The source called this edge `acts_as`". One example line added (checked) |
| 19 | §3.2.1 UI step quote; AIO type split; buildable core; offered to; modelled meaning; intent is debt; the rate stays a What-side signal; reification is not the What's | §3.2.1 | `same` ("(§4.5)" source citation removed from the quoted phrase) |
| 20 | §3.2.2 AIO quote; the ten AIOs; input AIOs; `[OPEN]` adopter-registered AIOs; context of use; interaction class | §3.2.2 | `register: [OPEN] -> *(open)*` (Round 2 wording), listed in "Not settled yet". One example line added (checked) |
| 21 | §3.2.3 WCAG quote; `mustSatisfy`; criteria not re-minted; inherited and added; verification type; attestations: signed record and ground reading, not a stored verdict; held by the profile | §3.2.3 | `same` ("Under this repository's rulings" → "Here") |
| 22 | §3.2.4, §3.2.5 | §3.2.4, §3.2.5 | `same`. One sentence added after the PF Acme quote saying it is the source's illustration, not the worked example (#48 W5 trap) |
| 23 | §3.3 signature; subject is input; six derived-signature rules; logic by digest; four conformance rules incl. subject coverage; wire scalar alphabet; scenarios; pure core is a How binding | §3.3 | `same`. One example line added (checked: Decider `Order` handles both commands, rejects with the three invariants) |
| 24 | §3.4 signature; symmetric; three rules; actor not an input quote; `keyedBy`; state justification "if and only if"; at least one reachable rejection; claim justification; shapes are warnings | §3.4 | `same`; "if and only if" kept |
| 25 | §3.5 title "Named-algorithm primitives", no subtitle; "Floor" is canon's; derivability quote; reference, I/O contract, oracle; exempt; oracle conformance is a How binding; dishonesty quote | §3.5, title unchanged | `same`. One plain-words gloss sentence added as the section's first sentence, as Round 2 (request 3) allows |
| 26 | §3.6 two kinds table; honesty test; located not listed; contract anchors to the demand | §3.6 | `same` ("H-9" moved to closing) |
| 27 | §3.7 subject-kind wording; two authorities; authentication is How; authorization table; subject kind (nature, claims, role or kind, delegation); View scope (five rules); checks bind once one kind declared; checks table; shapes list; warnings | §3.7 | `same`. One example line added (checked: Customer and Staff within Ordering; the two scope rules on `Order summary`) |
| 28 | §4.1 declared targets; one kind `DeclaredTarget`; edition may not resolve; "not a check this tool requires"; catalogues are packages; `pf:` classes not carried | §4.1 | "this tool" → "the What's own checker" (the old "this tool" had no referent outside the move session; #48's fix 13). Otherwise `same` |
| 29 | §4.2 obligations 1–3; content lives in How bindings; debt, boundary, never a waiver; neither holds the other's part | §4.2 | `same` |
| 30 | §5 intro: scopes central, instantiate genesis, tools never change the What, gathered material signed by a human principal | §5 | `same` (quoted ruling kept, typo "helds" included) |
| 31 | §5.1 force is the profile's; genesis unscoped; scope definition; acceptance validity; multi-scope rule "(Round 5)"; Writ's [D2] conjunction; kind vocabulary is the ontology; derived kinds in no scope; kind immutable "(`DDD-dec-63` §3)"; update 2026-11-02 on the profile and `CUR@1` "(§9)"; two grants | §5.1 | `same`. "Writ's [D2] conjunction" → "Writ's conjunction" ([D2] in closing). "Kind is immutable (`DDD-dec-63` §3)" → "(a kind change makes new elements, §2.2)". "(§9)" → "(authority.md §9)": `fact corrected`, what.md has no §9. "*Update, 2026-11-02*" label removed (`removed: history`; content kept) |
| 32 | §5.2 tool is a gathering source; declaration; enforcement oracle; gap split; completeness join; symmetry | §5.2 | `same` ("PF §14" → "the source's authoring-scope chapter") |
| 33 | §6 the wire moves, is the oracle's interface, corrects how.md Appendix B; runner quote; decision requests; subjects beside the command, never inside `with`; projection requests; equality; names on the wire (five bullets); schemas; ground readings | §6 | `same`. One example line added (checked: the four wire names). The A-8 contradiction is not touched (Round 2) |
| 34 | §7.1 seven bullets; edges carried and not carried | §7.1, title "Encoding, cut down" | `same` (title lost "(PF §9" citation) |
| 35 | §7.2 three conditions; "this half cannot be claimed until it exists (Q-4). *Update, 2026-11-02:* it exists … §4.7" | §7.2, "The authority profile is therefore part of conformance. 'In force' is authority.md §4.7" | `fact corrected` / `removed: history`: the profile exists; the condition is unchanged |
| 36 | §7.2 validation regime; violations and warnings; edition 1 warnings list; check.py | §7.2 | `same` |
| 37 | §8 "The move's own choices — `DDD-dec-64`, ruled": P-1 Round 2, P-2–P-7, R-1, R-2 Round 5, as proposed; additions; table P-1..P-7 | §8 "The choices made when the What moved here": seven choices, all decided as proposed, two additions; table without P numbers | `same` in substance; P numbers and rounds to the closing. Title reworded (no ruling names it) |
| 38 | Appendix — where the source went | Appendix | `same` (decision ids and Q-2 removed from cells; in the closing) |
| 39 | — | "Not settled yet" | lists the one *(open)* point |
| 40 | — | "Where this comes from" | every id, round and PF citation removed from the body, keyed by section |

**Could not restate.** None.

**Register changes.** `[OPEN]` → *(open)* at §3.2.2 (wording only). Status line "not yet ratified"
→ ratified (fact). No proposed or open point was raised, and no decided point lowered.
