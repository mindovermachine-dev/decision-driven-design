# Rulings — the Product Framework How, 2026-10-27

Rulings given during the session, verbatim, recorded when given. `prompt.md` stays the arrival
charter; this file carries what came after it.

## The charter's own rulings — recorded as `DDD-dec-54`

The six bullets under "Already ruled; do not reopen" in `prompt.md`, verbatim in `DDD-dec-54`.

## Round 1, 2026-10-28 — recorded in `DDD-dec-55` to `DDD-dec-61`

Emil's ruling on the proposal (`how.md` at `88bf686`), verbatim:

> Rulings on the How branch (`claude/epic-babbage-5cmeeh`), 2026-10-28.
> 1. Anchor reading — ruled as proposed. The product node is a What element. A decision anchors to the narrowest element that covers everything it governs; “every Decider in the Ordering domain” anchors to the domain, “every Decider” anchors to the product. Anchoring to the product is what the empty What forces and what an “every” rule over the whole product legitimately needs; it is the loophole only when a narrower element exists and was not used, and the checker should warn on that.
> 2. A package’s What is empty — ruled. `DDD-dec-46`’s “its What is its decisions” is superseded; `DDD-dec-42` stands. The kinds a package binds to are references in its decisions’ anchors, not What elements of the package. A package is a product with an empty What, a genesis, and a decision log.
> 3. Design system and content store — ruled: targets, not catalogues. The ruling of the 27th (§11 and §12 are What because you cannot build without them) means this: the product’s What declares the target (this design system at this edition, these locales against this content store), exactly as it declares iOS. The catalogue itself (the components, tokens, strings) is that target’s vocabulary edition: a package with its own genesis, typically a design team’s. The AIO-to-CIO and key-to-string bindings are How decisions of kind 2, anchored to the AIO or the content key. Nothing in a catalogue is a What element of the product that uses it.
> 4. Decisions written before the identity form is fixed — accepted, provisionally. They live in the test product only; they are not acceptable into any real product; and when the What lands with its identity form, each is superseded by a version against the real identifiers, never edited. Record that obligation on `DDD-dec-55` to `61` now so it cannot be forgotten.
> Four repairs — three accepted, one corrected.
>
> * “Every X” anchoring: accepted, see 1.
> * Kind 2 renamed “binding”: accepted, and Writ adopts the word. Writ’s vocabulary is unbuilt, its Realisation contract becomes the Binding contract, and `writ:realisation` is never minted. One word across both repositories; the How vocabulary is the authority on what a decision is, Writ is the authority on enforcing it.
> * A package is one decision log, vocabulary editions included: accepted.
> * Missing reporter → “unknown”: corrected. Writ’s G7 says `explain` never says unknown, and its verdicts are three: clean, violation, open question. A fact no reporter could supply is a reported gap, and a verdict that would need it is an open question with the absent reporter as one candidate (G8). Replace “unknown” with that; it is the same semantics with a name the gate can act on (an open question can block).
>
> Writ’s reporter contract — not a request, an existing definition plus one addition. The Writ product definition (Draft 2, `[D2]` and later) already has reporters: a Projector takes a repository at a commit or a reporter input with its hash; a reports partition per reporter; provenance from the closed set `file, compiler, graph, runner, data, telemetry, attestation`. What the How exposes is that deployment facts (declared regions, bundle identifiers, runtime) fit none of those; `deployment` is added to the set as a Writ definition change today. The repository at Hafeok/writ is behind the definition; the definition is the authority.
> Token — one of two, ruled by Emil, applied by whoever loses. `DDD-dec-53` says `decprov/1`; `main` ships `dpp/1` with a merged suite, a `system.json`, and the well-known path `decision-provenance`. Recommendation: supersede `dec-53` to `dpp/1`, because the path already carries the long name and the merged suite has 65 checks that should not be rewritten for a token. If `decprov/1` stands, PR #40’s successor renames everything before any further record is written. Either way, this branch’s checker stops substituting the string.
> Gaps — ruled as proposed: a missing binding that should exist is a baseline entry under the ratchet; a pair that cannot apply is an exclusion decision; a waiver never covers a coverage gap. Withdrawal — ruled as proposed: the importer must answer with a re-import or a decision to keep; the vendor blocks nothing. Generation — out of scope, confirmed.
> Ids. This branch holds 54 to 61; the move session’s charter said 54 was free. The move session takes 62 onward, and whichever merges second reconciles.
> Open a pull request. Not for merge; for the record. Emil ratifies by merging after the move’s identity form lands and item 4’s supersession obligation is written.

### Where each ruling landed

| Ruling | Landed in | Ruled, or still proposed |
|---|---|---|
| 1 Anchor reading; the checker warns on a wider anchor | `DDD-dec-55`; `how.md` §3; `check.py` | ruled |
| 2 A package's What is empty; `DDD-dec-46`'s clause superseded | `DDD-dec-56`; `how.md` §6 | ruled. `DDD-dec-46` is left unchanged and its clause is superseded by `DDD-dec-56`, as `DDD-dec-45` superseded a reading in `DDD-dec-44` |
| 3 Design system and content store are targets the What declares; the catalogue is a vocabulary edition in its own package | `DDD-dec-57`; `how.md` §5.1, §13 | ruled. The rest of `DDD-dec-57` (shapes derived from editions, standards not targets, platform targets) was not ruled separately and stands as proposed |
| 4 Provisional anchoring, with the supersession obligation | `DDD-dec-55` to `DDD-dec-61` (each carries the obligation); `how.md` §1.2; `how-examples/README.md` | ruled |
| Kind 2 renamed binding; Writ adopts the word | `DDD-dec-55`; `how.md` §2, H-1; `how-vocabulary.md` | ruled. Adopting it in Writ is an act on Hafeok/writ (S-4) |
| One decision log, vocabulary editions included | `DDD-dec-56` | ruled |
| "Unknown" corrected to an open question, with a reported gap and candidates | `DDD-dec-60`; `how.md` §9.3; `check.py`; `expected.json` | ruled |
| Writ's reporters exist; `deployment` added to Writ's provenance set | `DDD-dec-60`; `how.md` §9.2, §9.4 | recorded. Claude has not read Writ Draft 2: Hafeok/writ is still at Draft 1 (`3b1c5af`, re-fetched 2026-10-28). The definition is the authority, and its content here is as Emil states it |
| Token | not filed: no id taken (62 onward is the move's) | **not ruled**. A recommendation (supersede `DDD-dec-53` to `dpp/1`) is recorded. `DDD-dec-53` stands until superseded, so records still say `decprov/1`. The checker no longer substitutes, so its conformance step is red until the token is settled and applied |
| Gaps | `DDD-dec-58` | ruled |
| Withdrawal | `DDD-dec-59` | ruled. The rest of `DDD-dec-59` (the recorded-reading condition; narrow, never alter) was not ruled separately and stands as proposed |
| Generation | `DDD-dec-61` | ruled |
| Ids | — | ruled: 54–61 here, 62 onward the move's |
| Open a pull request, for the record | the pull request | done. Emil ratifies by merging after the move's identity form lands and item 4's supersessions are written |

Not ruled separately, and so standing as proposed until the merge ratifies them: the three kinds,
no fourth kind and no split, the idle report, target declarations and exclusions as record types
(`DDD-dec-55`); shapes derived from editions (`DDD-dec-57`); the recorded-reading condition on
supersession, and narrow-never-alter (`DDD-dec-59`); Kind-1 wiring as contracts, and declared
readings gating `land` (`DDD-dec-60`).

## Round 2, 2026-10-28

Verbatim:

> Round 2 rulings (2026-10-28).
>
> 1. Token — ruled: `[dpp/1 | decprov/1]`. If `dpp/1`: file a supersession of `DDD-dec-53` under the move session’s range (62 onward, coordinated with that session), rebuild the records with the real keys, and the conformance step goes green. If `decprov/1`: `main` renames before any further record is written, and this branch waits. `build.py` refusing on a token mismatch stays as it is.
> 2. “Binding” in Writ — ruled: Writ narrows, the How does not widen. Writ’s Binding contract is kind 2 only: a What element to a shape in a target. A constraint has no binding; it evaluates over the projector’s facts, and the citation attributes the projector recognises (`[DesignDecision]`, `[Contract]`) are part of its fact vocabulary, not a binding. A contract has no binding; it evaluates over a reporter’s facts. The mapping of the three kinds onto Writ is therefore: constraint → projector facts; binding → Binding contract; contract → reporter facts. Writ’s definition is amended today (`[D2.8]`) to say exactly this; `writ:realisation` is never minted.
> 3. Declared versus observed deployment — ruled: two provenance values, not two inputs. The G8 set gains `deployment-declared` (from IaC or a manifest) and `deployment-observed` (from the platform’s own API). A contract’s violation description says which it requires; residency may be satisfied by declared, “no public endpoint” needs observed. Carrying the split as two inputs under one value would hide it where it matters, in the verdict. Change the reporter section accordingly.
> 4. Writ Draft 2. The authority is the product definition held outside the repository; Hafeok/writ is behind it and will be brought up to date before any Writ format page is written. Your recording of reporters and `deployment` as I stated them is correct; no action on your side.
> 5. No watch on #41. It is for the record; ratification is a manual merge after the move’s identity form lands. Leave the session idle.
>
> Everything marked “standing until the merge” stands. Nothing else to change on the branch beyond items 1 and 3.

### Where each ruling landed

| Ruling | Landed | State |
|---|---|---|
| 1 Token | nowhere yet. The ruling is written as a choice, `[dpp/1 \| decprov/1]`, with an action for each outcome, the same form as `DDD-dec-48`. Neither outcome is selected, so neither action runs: no supersession of `DDD-dec-53` is filed, no id is taken, nothing is rebuilt. `build.py` is unchanged | **waiting on the choice.** If `dpp/1`: supersede `DDD-dec-53` at an id coordinated with the move session (62 onward), and rebuild with the real keys. Those are Emil's to supply; this session holds only throwaway test keys. If `decprov/1`: wait for `main` to rename |
| 2 Binding in Writ narrows | Writ's definition (`[D2.8]`), outside this repository | recorded. By the closing line, nothing on this branch changes. `how.md` §2 and §13 item 2, and `how-vocabulary.md` §4's binding row, still carry the flag this ruling answers ("binding is wider in Writ"). They are left as written; the flag stands answered here |
| 3 Two provenance values | `how.md` §4.1, §4.2, §9.2, §9.3, §13, H-9; `how-vocabulary.md`; `DDD-dec-60`; `how-examples/facts/manifest.json`, `check.py`, `README.md` | applied. `RESID@1`'s hashed `factSources` still read `reporter:declared` and `reporter:observed`. Rewriting them is a new version, which waits for the token rebuild (item 1). The checker maps them onto the two provenance values |
| 4 Writ Draft 2 | — | no action, as ruled |
| 5 No watch on #41 | — | no subscription; the session is left idle |

## Round 3, 2026-10-28

Verbatim:

> Round 3 (2026-10-28).
>
> 1. Token — ruled: `dpp/1`. (or `decprov/1`; one word.) File the supersession of `DDD-dec-53` under the move session’s range, coordinated with it. Rebuild the records with fresh test keys: the examples live in a test product under a test genesis with a declared test holder, and no real key is ever used for a fixture or held by a session. Your scratch run is the model. `RESID@1` gets its new version in the same rebuild.
> 2. Strike the three stale flags (`how.md` §2, §13 item 2, `how-vocabulary.md` §4 binding row). Ruled text and prose must agree; a flag that a ruling has answered is noise for the next reader.
> 3. Then: checker green, PR #41 stays draft, session idle.

### Where each ruling landed

| Ruling | Landed | State |
|---|---|---|
| 1 Token `dpp/1` | `DDD-dec-62` supersedes `DDD-dec-53`. Every action in the ruling belongs to the `dpp/1` outcome, so the parenthetical "(or `decprov/1`; one word.)" is read as restating one token (`DDD-dec-48`), and is recorded with that reading in `DDD-dec-62` | done. Id 62 is the first of the move's range; the move session had not started and no branch held 62, so the claim is recorded here, in `DDD-dec-62` and in PR #41. **The move session now takes 63 onward** |
| 1 Rebuild | `how-examples/records/`, `facts/manifest.json`, `build.py` (`TOKEN = "dpp/1"`; the signing namespace `decision-provenance`; keys discarded after every build) | done, with fresh throwaway keys, none kept. `RESID@1` issued with `deployment-declared` and `deployment-observed`; the checker's mapping of the old spelling removed. The `decprov/1` set stays in history at `d11df86` |
| 2 Three stale flags | `how.md` §2 now states Round 2's narrowing as ruled text; §13's token and binding items struck; `how-vocabulary.md` §4 binding and constraint rows | done |
| 3 Checker green | `check.py` against the reference implementation on `main`, unmodified | **71 ok, 1 expected warning (the anchor self-test), 0 failures**. Every record conformant |
| 3 PR #41 draft; session idle | — | unchanged |

## Successor items, not this session's

- **S-1.** Closed (Round 3): the token is `dpp/1` (`DDD-dec-62`), and the records are rebuilt.
- **S-2.** The move session takes `DDD-dec-63` onward (`DDD-dec-62` was taken here in Round 3). Before it fixes the What's identity form
  and kind names, it reads `how.md` §1.2 and D-8. When that form lands, every example record
  anchored to a What element is superseded against the real identifiers (ruling 4), and `DDD-dec-55`
  to `61` are re-pointed by supersession too.
- **S-3.** The authority profile (the move's Gate 2) answers `how.md` D-6: baseline entries, the
  waiver/exclusion line, `acceptedBy`/`acceptedAt` mapped to the acceptance record's `by`/`at`.
- **S-4.** In Hafeok/writ: the Realisation contract renamed the Binding contract, `writ:realisation`
  never minted, `deployment` in the provenance set, and the remaining demands D-1, D-4 and D-5.
  That is an act on another repository, and only with Emil's go-ahead.
