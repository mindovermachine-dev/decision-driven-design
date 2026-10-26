# GATE 2 report — doc format

2026-10-26, branch `claude/doc-format`. Everything filed here is `[PROPOSED]` until Emil accepts the session's PR.

## Weakest point first

**W11 sees only upstream bases.** It fires when a pinned upstream claim moves, because pins record a status and a content hash. Local canon records neither. Under GATE 1 ruling 1, four of the seven promotions file *here*, in `core/claims/`. A document resting on `DDD-cost-04` today, or on a promoted `P-3` tomorrow, gets no W11 when that claim moves from projected to reported, or is retired. Half of canon is uninstrumented for the very failure W11 exists to catch.

**Proposed amendment, for ruling before the pilot:** a basis entry for local canon may carry the status it was read at, as `DDD-cost-04@projected`. The check compares it with the claim file and fires W11 on a difference. An entry without `@` fires a new note asking for one. Local content movement (the W6 case) stays uncovered; it would need a hash per entry, and that is out of proportion until a case appears. `UNVERIFIED — Emil review`.

## What was filed

| File | What |
|---|---|
| `spec/doc-format.md` | The `ddd:charter` and `ddd:doc` schemas, scope, statuses, W8–W14, and how to write a new document. It carries its own `ddd:doc` block. |
| Charters | `ddd:charter` blocks with a prose line in the READMEs of the root, `core/`, `apparatus/`, `applications/`, `meta/`, `meta/sessions/`, `projections/` and `migration/`. New READMEs for `papers/` and `spec/`. |
| `core/decisions/DDD-dec-39.yaml` | The session's decision: the principle, reading A, the charters and opener, the dispositions (by reference to `promotions.md`), retention and held bases. `basedOn`: `DDD-agent-01`, `DDD-dec-04`, `DDD-dec-10`. |
| `validate-core-order.py` | Pass 5, `check_docs`: W8–W14, warnings only. `check_upstream` now returns the set of moved pins, which W11 reads. Both entry paths call the new pass. |
| `gate2-proposals.md` | The `way-of-working.md` §5 replacement and post-split note, and the `CLAUDE.md` sentence. Proposed, not made. |

The charters' readers and acts are Claude's wording. They were not ruled one by one. `UNVERIFIED — Emil review`.

## Validators

| Validator | Result |
|---|---|
| `validate-core-order.py core/` | Exit 0. 0 errors. 74 pins, 0 basis-loss, 0 content-drift. **48 governed documents, 1 with `ddd:doc`** (`spec/doc-format.md`). 47 warnings, all W8. No W9–W14. |
| `validate-claims.py core/claims/` | Valid, 31 claims, 6 warnings: unchanged from the base. |
| `validate-claims.py core/decisions/ --decisions` | Valid, 25 decisions, `DDD-dec-39` included. |

The 47 W8 are the roll-out's work list: 18 in `meta/`, 9 in `papers/`, 7 in `apparatus/`, 4 at the root, 3 each in `applications/` and `projections/`, 2 in `migration/`, 1 in `spec/`.

**One error caught by the check itself.** The first run reported the root charter as malformed. Its `act:` value contained a colon, which YAML reads as a mapping. The wording was fixed, and the check now reports a malformed charter once rather than once per document.

## The check, verified against its falsifier

Pre-session ruling 2's falsifier asks whether W11 fires on a document whose basis moved. It was tested before roll-out, on a throwaway copy of both repositories:
- Upstream `DDD-floor-01` was moved from `reported` to `projected` in the copy.
- A fixture document named it in `basis`, along with an upstream decision, two held entries (one real, one not) and a held entry under `status: current`.
- A second fixture was malformed and pinned at `v5.13.0`.

Every class fired as specified: W5 on the pin, **W11 on the document resting on it**, W10 with the S-8 note on `DDD-dec-37`, W13 on both held entries (one found, one named as missing), and W9 and W12 on the malformed fixture. W14 fired in the real run. The copy was deleted, and nothing from it was committed.

This shows the mechanism works. It does not discharge the falsifier, which is about documents after roll-out. That test happens at GATE 5.

## Stale statement found since GATE 1

`apparatus/README.md` says "none is depended on *by* core". GATE 1 found that upstream `core/11` relies on P-1. It is added to the GATE 4 list.

## Rulings requested

1. The local-basis amendment (`ID@status`): adopt before the pilot, or carry as a successor item?
2. The charters' readers and acts, as a whole or folder by folder.
3. Proposal 1 (`way-of-working.md` §5 and the post-split note): make it at GATE 4, or hold it?
4. Proposal 2 (`CLAUDE.md`): make it at GATE 4, or hold it?
5. Proceed to GATE 3, the pilot on `apparatus/tool-contract.md`?
