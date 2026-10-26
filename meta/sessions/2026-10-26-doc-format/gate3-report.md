# GATE 3 report — the `tool-contract` pilot

2026-10-26, branch `claude/doc-format`.

| Item | Value |
|---|---|
| Pre-registration | `prereg-pilot.md`, committed at `d72b844`, before the new text existed |
| Its SHA-256 | `6f7bda09d343842e7929867c9e62e9e44813345b897ca0c056af4930cdc6f56c`, re-verified at this report; the file is unchanged |
| New text | `apparatus/tool-contract.md` at `b1846cd`, committed before any reader result was read |
| Evidence | `pilot-evidence/`: the old text, the four answers verbatim under blind labels, the label mapping and the readers' usage |

## Weakest point first

**The test could not tell the versions apart.** All four readers scored 8 of 8. The rubric has a ceiling, and a capable reader hits it from either text. So the result shows that the new format **lost nothing** that a reader needs to bind a toolset. It does not show that the new format **helps**. The speed difference is 6%, which is inside the noise of two runs per version. "Not falsified" is the honest reading. "Confirmed" would overclaim.

A second limit compounds it. The readers are model proxies, not junior engineers (pre-registration §4). A human first-contact test is a successor item, whatever the result.

## The falsifier

| Limb | Rule, as pre-registered | Observed | Fires |
|---|---|---|---|
| 1, score | New mean below old mean | Old 8.0 (W 8, Y 8). New 8.0 (X 8, Z 8). | **No** |
| 1, speed | New mean duration more than 10% above old | Old 49.5 s (45.6, 53.3). New 46.6 s (52.3, 40.9). Ratio 0.94. | **No** |
| 2, lost result | Any of R1–R11 absent from the new text and from canon and `promotions.md` | R2–R7, R10 and R11 are in the new text. R1, R8 and R9 are in it **and** registered as P-8, P-9 and P-10. | **No** |

**Scorer sensitivity.** The scorer was a fresh agent with the rubric and the four unlabelled answers only. It flagged one criterion it read generously: K6, "the model does not pick tools". Only one answer says it in words. Read strictly, old scores 7 and 7 and new scores 7 and 8. Limb 1 still does not fire.

## Predictions

| # | Prediction | Outcome |
|---|---|---|
| P1 | R1, R8 and R9 are unregistered results; the pilot registers them as P-8 to P-10 | **Held.** GATE 1's "project: normative design, not result" was partly wrong for this document, and the pre-registration said so before the rewrite. |
| P2 | W13 on P-3 and each new held item | **Held.** W13 fired five times: P-2, P-3, P-8, P-9, P-10. |
| P3 | W10 on `term:poisoned-ground` and `term:encode-verify-split` | **Held.** Both are canon and unpinned. |
| P4 | Limb 2 does not fire | **Held.** |
| P5 | New scores at least as well and is no slower | **Held, weakly.** See the weakest point. |

## What first contact did show

The scores could not discriminate, but the readers' answers and unsure points (task item 4) did. They separate into findings about the **format** and findings about the **document's content**.

### About the format

1. **The format's own markup became reader burden.** Both new-text readers listed "held", the P-numbers and `DDD-floor-01` among the things they did not understand. One wrote: "many of the rules are marked held (not yet settled), so I don't know how firm they are." The old text had no such markup, and its readers did not raise it. Flagging status at the point of use is right. Flagging it with IDs is not, for this reader.
2. **The reorder helped on one point.** Both old-text readers declared workspace reads *uncontrolled*, against the document's intent. Both new-text readers declared them *controlled*. The new table states "a controlled response is the source of truth, so it cannot be stale" where the reader is deciding, and the old text did not. This is the clearest behavioural difference in the test.
3. **The old text's self-description confused its readers.** One old-text reader noted that the document "marks itself as proposed, and its location is undecided". That is the stale "Location: proposed" line from GATE 1's survey item 4, seen from the reader's side.
4. **Pointing to another document cost the old-text readers.** One said it could not compute tool classes because the definitions are in `tool-surfaces.md`, which it did not have. The new text names the classes and says the harness computes them, so its readers did not stall there. It still does not define them (see content finding 5).

### About the content (true of both versions)

1. **Write tools are not covered.** All four readers said so. The declaration fields are written for tools that read or check.
2. **"Controlled" conflicts with "revalidate by default".** Three of four readers flagged it. A controlled response "cannot be stale", but the agent's own writes make earlier reads stale, and rule 2 asks local tools to re-stat. The contract needs to say what controlled means for ground the agent itself mutates.
3. **Partial verification has no category.** All four split decisions into a verified part and an open part, because the contract offers only resolved, verified or open.
4. **Assurance level and tolerance are used but not set.** All four raised it. The reader is told to list governing decisions "at the declared assurance level" with no way to declare one.
5. **The vocabulary is undefined for this reader.** Judgment and encoded stores, escape, seam and the tool classes appear in both versions without a definition the reader can use.
6. **The open set has no next step.** Readers asked what happens after the open set is shown: may the owner add a tool and rebind? Does the run wait until the set is empty? What happens to writes already made when the agent stops?
7. **All four found the same real gap in the task: no install step.** No bound tool installs the new version, so a passing test run may be a verdict on the old one. Two readers recognised this as the "overstated verdict scope" the contract warns about. The contract worked here, in both versions.

The content findings are not the format's to fix. They are recorded for the harness guide, which designs exactly this kind of harness.

## Proposed amendment to the format `[PROPOSED]`

From format finding 1. Add to `spec/doc-format.md` §4:

> **In running text, say "held" in words the reader can use, and keep IDs out.** The first time a held basis is used, say what held means in one sentence: "not yet part of the framework's canon; this rests on an argument made here, which is registered to be filed". After that, mark held statements with a plain marker, such as "(not yet canon)". Claim, term and promotion IDs belong in the `ddd:doc` block and the basis table, not in the prose.

Then apply it to the pilot before roll-out, so the roll-out copies the corrected pattern.

**Falsifier for the amendment.** If a human first-contact reader of the amended pilot still lists the status markers as a source of confusion, the markers are wrong for this reader in any form.

## Successor items arising

| Item | From |
|---|---|
| A human first-contact test of `tool-contract.md` | Pre-registration §4 |
| A rubric that discriminates: at least one criterion the ceiling does not reach (for example, catching the missing install step, or the controlled/revalidate conflict) | Weakest point |
| Pin `term:poisoned-ground` and `term:encode-verify-split` in `graph/upstream.yaml` | Prediction P3 |
| `tool-contract.md` content findings 1–6, for the harness guide and a later content revision | First contact |

## Rulings requested

1. Accept the pilot as **not falsified**, with the ceiling and proxy limits recorded as above?
2. The format amendment (held in words, IDs out of prose): adopt, and apply to the pilot before roll-out?
3. The content findings: carry them as successor items for the harness guide, rather than fixing `tool-contract.md` in this session?
4. Proceed to GATE 4, in this order: the six remaining apparatus documents, `applications/`, `spec/`, `projections/`, `papers/`, `meta/`, `migration/`, root. Then the stale statements, then `CLAUDE.md`, then `way-of-working.md` §5 last?
