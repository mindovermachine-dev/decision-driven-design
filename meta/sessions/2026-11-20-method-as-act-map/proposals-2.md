# Proposal for G2 — what a ruling that moves a move to ruled rests on

Asked by Emil at G1 (P-7): "since nothing in the method now waits on T2b, what evidence should a
ruling that moves a move from [PROPOSED] to ruled rest on." Claude's, `UNVERIFIED — Emil review`.

## P-10. A field report per move, from a case outside the framework

**Weakest point.** One case is thin evidence. A ruling is a decision, and decisions are made, not
tested (`meta/way-of-working.md` §4). Nothing stops a principal from ruling with no evidence at
all. This proposal only says what the ruling should cite in its `basedOn`, so the gap shows when it
is missing.

**Two things are kept apart.** The old register "ruled for test" fused them, and that is why
nothing waits on T2b now.

| | What moves it | What it rests on |
|---|---|---|
| A claim's status (projected → reported) | A test its falsifier could have failed | The claim's own test. T2b, for the address claims |
| A move's register (`[PROPOSED]` → ruled) | A ruling by the principal | The evidence below, cited in the ruling's `basedOn` |

**Proposal.** A ruling that moves a move to ruled rests on, and cites:

1. **A case outside the framework's own data.** Not the acme shop, not Varve's slice as Claude
   mapped it. The same standard T2b sets for independence: the map is made after the predictions
   are fixed.
2. **The card at a named commit.** The field report says which version of the card was run.
3. **The move's default falsifier, asked and not fired.** The practitioner names the value the
   move gave them, in the words of its "Value made visible" field, or the report says they could
   not.
4. **For move 3, reproducibility.** `DDD-address-09`'s test: two practitioners trace the same
   scope without conferring, and their entry acts are compared.
5. **For move 2, sufficiency.** Whether any pull needed a group B field (T-7). If one did, group A
   is not enough, and the ruling says so.
6. **Recorded as a field report**, under the issue template, linked from the ruling.

T2b can be the first such case for all four moves at once, if its pre-registration carries T-7
and T-8 (draft D-10 in `breaks.md`).

| Option | What a ruling rests on | For | Against |
|---|---|---|---|
| **A (recommended)** | The six points above, per move | Every ruled move points at a case. Moves can be ruled one at a time | Slow: a move waits for a case |
| B | The claims the move rests on reach reported first | Strongest | Ties the method to claim tests again, the coupling that left nothing waiting on T2b |
| C | The principal's ruling alone, with a register "ruled, untested" | Fast | Restores "ruled for test" under another name |

**Rests on.** None ruled. The method draft's default falsifier and its instruction to test against
a junior engineer's first contact (`[PROPOSED]`). `DDD-address-09`'s test. `DDD-dec-74`'s "ready to
try, not ready to use".

**Falsifier.** A move ruled on this evidence that the next independent case breaks: a practitioner
who cannot name its value, or two who trace to different entry acts.

**What it breaks.** Nothing filed. If ruled, `method/README.md`'s register table gains a "ruled"
row whose meaning is this evidence, and D-3's version decision can count ruled moves.
