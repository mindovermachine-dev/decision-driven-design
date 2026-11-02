# Core contracts — proposed `ddd:contract` blocks for the reordered core

Derived from the forward-reference audit of `core/` at current main. Paste each block at the
top of its document. Term lists are drawn from actual definition sites and body usage; strike
anything that doesn't match your intent — especially the terms flagged ⚑, where the audit
required a judgment call.

**Format.** `term|alias1|alias2` — the first form is canonical, aliases feed the body linter.
Hyphens match spaces (`seam-demand` matches "seam demand"). Plurals are matched automatically.

---

## Reorder map

| new | old | change |
|---|---|---|
| 00 primitives | 00 §1–§5 | **shrinks** — keeps determination, two primitives, admission tests, the name; gains minimal actor + arrangement (from 04); loses §3 "stores restated", §6 ensemble, §7 immune system |
| 01 principle | 01 | canonical four-stores statement stays here; 00's "restated" table deleted |
| 02 completeness | 02 | unchanged |
| 03 floor | 03 | unchanged in position; "arrangement"/"actor" now legally backward |
| 04 actors | 04 minus §4 | §4 composite actors moves to 06 |
| 05 accountability | 05 | rephrase 2× "verdict" (est. 09) |
| 06 composition | 06 + 04 §4 | merge resolves the 04↔06 seam-demand cycle; single canonical seam definition |
| 07 det ≠ intelligence | 07 | rephrase 2× "verdict" |
| 08 projections | 08 | unchanged |
| 09 measure | 09 | unchanged |
| 10 floor mechanism | 10 | unchanged |
| 11 licensing instance | 00 §6–§7 | **new** — ensemble actors, diversity vs redundancy, swarm gate, immune system; the capstone worked instance, legal only after 10 |

Also: 04 §2 currently *duplicates* 03's floor claim verbatim. Keep 03 canonical; reduce 04 §2
to a one-line backward reference. Two canonical statements will drift.

---

## 00-primitives.md

```
<!-- ddd:contract
requires: []
establishes: [determination, decision, ground, tolerance, admission-test,
              actor, arrangement, last-decision|last decision in the chain]
status: settled
-->
```

⚑ `actor` and `arrangement` here are the *minimal* definitions only — the admission test
(alternatives, information-bearing pathway, selection) and "the composition through which a
resolution is produced." Pinning resolution, selection/training, and everything predictive
stays in 04. This is the standard layered move: define the noun early, earn the theory later.

## 01-the-principle.md

```
<!-- ddd:contract
requires: [decision, ground, tolerance, actor, arrangement]
establishes: [demand|determination demand, conservation|conservation principle,
              store, encoded, mechanical, judgment, escape|escaped, assurance]
status: settled
-->
```

⚑ `assurance` — the *level* is declared here (it's in the principle's statement); the
assurance *tower* is established in 05. Two terms, two homes.

## 02-completeness.md

```
<!-- ddd:contract
requires: [store, escape, decision, tolerance]
establishes: [exhaustiveness, governing-decision|governing decision]
status: settled
-->
```

## 03-the-floor.md

```
<!-- ddd:contract
requires: [arrangement, actor, ground, escape, assurance, decision]
establishes: [acceptance-predicate|acceptance predicate, closure|closes|closed|closing,
              floor|intrinsic floor, path-degeneracy|path degeneracy]
status: settled
-->
```

⚑ `closure` is established here as *effective/operational* closure ("closed for the
arrangement over ground it can inspect"). 00 line 160's "closes the encoded store" is a
different, colloquial sense — rephrase it in the new 00 ("fills the encoded store") so the
linter's closure alias doesn't fire and the reader doesn't collide two senses.

## 04-actors.md

```
<!-- ddd:contract
requires: [actor, arrangement, floor, closure, acceptance-predicate, store, escape]
establishes: [pinning-resolution|pinning resolution, selection, training]
status: settled
-->
```

## 05-accountability.md

```
<!-- ddd:contract
requires: [actor, arrangement, escape, assurance, pinning-resolution]
establishes: [accountability, attribution, answerability, liability,
              assurance-tower|assurance tower]
status: settled
-->
```

Edit note: two body uses of "verdict" — rephrase ("the outcome the check assigns" or
similar). Cheap; no restructuring.

## 06-composition.md  *(absorbs 04 §4)*

```
<!-- ddd:contract
requires: [actor, demand, store, conservation, decision]
establishes: [seam|seam demand, seam-identity|seam-demand identity,
              composite-actor|composite actor, seam-occupancy|seam occupancy,
              orchestrator]
status: settled
-->
```

The merge is the fix for the genuine cycle: composite actors and the seam identity are one
result stated from two ends. One doc, one canonical statement, seam occupancy (old 04 §4.1)
comes along.

## 07-determination-and-intelligence.md

```
<!-- ddd:contract
requires: [closure, acceptance-predicate, floor, determination]
establishes: [determination-intelligence-separation|determination is not intelligence]
status: settled
-->
```

Edit note: two body uses of "verdict" — rephrase. The doc's own point (the framework
*declines* the intelligence verdict) uses "verdict" colloquially; that's fine, but keep it
out of the technical sense or alias-collision will warn.

## 08-projections.md

```
<!-- ddd:contract
requires: [store, demand, judgment, escape]
establishes: [projection, funnel, maturation]
status: settled
-->
```

## 09-the-measure.md

```
<!-- ddd:contract
requires: [closure, acceptance-predicate, demand, conservation, seam, store, actor]
establishes: [verdict|verdict function, verdict-entropy|verdict entropy,
              chain-rule-identification, seam-information|I(V;S)]
status: settled
-->
```

## 10-the-floor-mechanism.md

```
<!-- ddd:contract
requires: [floor, closure, verdict, verdict-entropy, escape, judgment, demand]
establishes: [capacity, overflow, escape-mechanism|overflow ∩ open, p-err|p_err]
status: settled
-->
```

## 11-the-licensing-instance.md  *(new; old 00 §6–§7)*

```
<!-- ddd:contract
requires: [store, floor, closure, verdict, capacity, overflow, seam,
           composite-actor, escape, admission-test, demand]
instances: [immune-system|immune system]
establishes: [ensemble-actor|ensemble actor, diversity, redundancy,
              swarm-gate|the gate on swarms]
status: settled
-->
```

⚑ Ensemble theory ("diversity carries judgment demand exceeding any single actor's
capacity") is *real theory*, not just illustration — but it needs `capacity` (10), so this is
its earliest legal position regardless. If you'd rather ensemble-actor theory live in 06 with
composition, it can't: the capacity dependency pins it after 10. The audit's cleanest
argument for the reorder.

---

## What the old 00 loses, explicitly

Deleted or relocated, with destination:

- §3 "The four stores, restated" → delete; 01 is canonical (the {rule, check, actor,
  nothing} partition is 01's opening move now)
- summary table rows referencing seam-demand identity, assurance → trim to primitives-only
- line 13 "demand is conserved" → soften to forward *pointer* ("01 states the conservation
  principle") — passes the deletion test
- line 140 funnel/maturation → delete (08 owns these)
- §6 ensemble actors, §6.6 swarm gate → 11
- §7 immune system → 11
- lines 160–167 (verdict function, capacity overflow, predicate closure) → 11, where every
  term is legal

Estimated: new 00 is ~1,100 words of the current 2,749. The remaining ~1,650 words become 11
nearly verbatim — the material was never wrong, only early.
