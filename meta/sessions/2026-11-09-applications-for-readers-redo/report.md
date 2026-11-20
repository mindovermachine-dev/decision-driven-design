# Report — applications/ for readers, redone

Branch `claude/zealous-ptolemy-3txf8k`, from `main` at `84aa466` (`main` has not moved). Issue #71.
The session stops here for Emil. Nothing is landed.

## Weakest point first

**Whether the format helps people is still not shown.** Emil ruled that a human first-contact
test decides it (Round 1). That test is pre-registered as A-4 and not run, because model readers
are not a substitute (`prereg-a4-human-first-contact.md`, committed at `ebf84a5` before any
rewrite, SHA-256 `54344db1d6671aa65d71194b7685b4f9a7f01cc50ff681d00db9112cb715b58e`). It is
Emil's to schedule.

The second weakest point: **the rewrite again produced the failure class #48 named.** 13 serious
points before the independent check, every one of them fixed or kept with a recorded reason. The
writers' own equivalence tables caught none of them (`independent-check.md`).

## What landed on the branch

| Gate | What | Commits |
|---|---|---|
| G0 | `prompt.md`, `bootstrap.md` | `70abfa2` |
| — | Round 1 verbatim | `eb52cda` |
| A | `DDD-dec-94` re-filed from #48's file, with what `main` made wrong; `spec/doc-format.md` ported | `1378851` |
| Q | Round 2 verbatim (Emil's answers to #48's requests 2 to 4, and the register phrases) | `4a4b864` |
| — | `DDD-dec-119`: #41's merge ratified the How's "not ruled separately" parts | `0ea1376`, `6536d9c` |
| B | Conventions; the A-4 pre-registration; 15 documents rewritten, one commit per document group; `DDD-dec-95` and the spec's folder line | `cdae9bf` … `b489627` |
| 7 | The independent check, and its fixes | `f61ca44` |

## Decisions filed

- **`DDD-dec-94`**: the 2026-10-26 doc-format rulings re-filed, with #48's text unchanged except
  its `made` line and a re-filing note (findings F-1).
- **`DDD-dec-95`**: the reader format as applied. It differs from #48's version in the following
  ways, each with its reason in the decision.
  - No split, merge or rename: sections are cited by number in hashed and signed files (F-6, F-8).
  - F4 adapted and F5 not applied.
  - Four registers in words (Round 2).
  - No new point-of-use markers.
  - Scope: all 15 documents.
  - The human test decides.
- **`DDD-dec-119`**: Emil's Round 2 answer on #41. The §5.2 term list and §11's level are reached
  only through the document's banner. That reading is Claude's, flagged in the decision and in
  `how.md`.

## Predictions

| # | Prediction | Outcome |
|---|---|---|
| 1 | #64 has landed | Held: merged 2026-11-09 |
| 2 | `DDD-dec-94`/`-95` held only by #48's branch | Held. No other branch holds `94` to `99` (`bootstrap.md`) |
| 3 | #48's two files need only what `main` made wrong changed | Held. Only the `made` line and one pointer (F-1) |
| 4 | Anchors constrain the split | Held, more than predicted. 157 citations, and the split was dropped (F-8) |
| 5 | The independent check finds points the tables missed | Held: 89 points, 13 serious |
| 6 | CI stays green after every commit | Held at every pushed head |

## Rulings and questions for Emil

1. **Confirm or correct `DDD-dec-119`'s reading** that the merge reached `how.md` §5.2's term list
   and §11, which only the banner covers. If rejected, both return to proposed.
2. **F-13**: the stale `UNVERIFIED` mark on `how.md` §2's anchor row was dropped, because
   `DDD-dec-55`'s statement holds the reading. Say if the mark was meant for the row's other
   sentence.
3. **F-10**: `pdlc.md` §2.1's seam rows 1 to 8 are kept as not ruled, as `DDD-dec-114` says,
   although the register line says the tables were ruled.
4. **A-4**: schedule the human test.
5. **A-8 first** (Round 2): the example's claim inside `with`, against the wire rule. It needs a
   new What-version.

## Not done, and why

- **`DDD-dec-117`'s amendments are not worked into `authority.md` §3.1–§3.2 or
  `product-definition.md`'s "no authority" passages.** That changes content, which this session does not,
  and belongs to the specification-feasibility session's successor work. Each passage is now marked, and listed
  under "Not settled yet".
- **`what/ontology.ttl`, `shapes.ttl`** (A-6) and **`pdlc/graph/ontology.ttl` line 160** (F-11):
  graph files, not in scope.
- **The `ddd:doc` check** (A-1) is not ported, so the blocks are a convention.

## To land

The approval (`DDD-dec-109`) is a comment on a pull request. No pull request is open, since none
was asked for. Either Emil opens one (or asks Claude to) and lands it the usual way:

```
approve <head sha>        # by hand, on the pull request
canon land <PR> --print
canon land <PR>
canon land <PR> --main    # after pipeline (devcontainer) is green on land/pr-<PR>
```

or, while `agent review` is not yet required, lands the head without a pull request:

```
canon land --commit <head sha> --print
canon land --commit <head sha>
canon land --commit <head sha> --main
```
