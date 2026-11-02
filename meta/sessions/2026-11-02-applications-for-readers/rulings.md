# Rulings — applications/ for readers, 2026-11-02

Recorded when given.

## Round 1 — on Gate 1, recorded as `DDD-dec-94` and `DDD-dec-95`

Emil asked for Claude's recommendations on the five rulings `gate1-proposal.md` requested
("give me your recommendations"), then ruled:

> agreed go with your recommendations

Claude's recommendations, as given:

> **1. Format: adopt F1–F8, with one amendment.** Add invisible `ddd:ref` markers at the point of
> use, but only where a rule rests on a projected claim, not on every decision.
> - **Why:** readers see clean prose, and tooling still warns when a claim moves.
> - **Weakest point:** I'm adding a rule to the format before Gate 3 has tested it. If the
>   first-contact test fires, drop the markers along with F3.
>
> **2. Re-file the 26 October rulings: yes, as `DDD-dec-94`, before Gate 2.** Include the pilot's
> "keep ids out of prose" amendment in it.
> - **Why:** this session rests on a ruling that exists only on an orphaned branch. That is basis
>   loss, and the fix is cheap.
> - **How:** record the doc-format principle and the `ddd:doc` opener. Leave the validator check
>   (W8–W15) as a later item. That code was written against the old history and needs porting to
>   `scripts/`, which is a separate job.
> - **Weakest point:** without the check, the `ddd:doc` block is unchecked for now.
>
> **3. Split: yes, for both `what.md` and `how.md`.** Practitioners and tool builders want
> different things from them.
> - **Practitioner documents:** what a product's What is, how to change it, and who signs.
> - **Reference documents:** identity, hashes, the wire, encoding, and the vocabulary.
> - **Merge `how-vocabulary.md` into `how-reference.md`.** It is already reference material, and
>   one reference per model is easier to find.
> - **Weakest point:** that is two more files to keep in step. Each document gets one line at the
>   top linking to its other half.
>
> **4. Example: keep Acme Shop for the What and How, beside Varve for the method.**
> - **Why:** Acme Shop has a full What, decision records and a checker that runs. Varve has none of
>   these, and building them is a session of its own, not a formatting job.
> - **What to add:** one paragraph in `sdlc/README.md` saying why there are two examples. Record an
>   `[OPEN]` successor item to write Varve's What later, so one example can carry the whole method.
> - **Weakest point:** until then, a reader moving from the method into the What switches examples.
>
> **5. Scope: `applications/` only, and `apparatus/` next.**
> - **Why:** Gate 3's reader test tells us whether the format works. Rolling it out to `apparatus/`
>   first would copy an untested pattern into a second folder.
> - **Weakest point:** `apparatus/` keeps reading like canon a little longer.
>
> **Sequence:** your rulings, then `DDD-dec-94`, then the Gate 3 pre-registration, then the Gate 2
> rewrite (one commit per document, each with its equivalence table), then the Gate 3 reader test,
> then your review. Do `authority.md` after #45 merges, in the same format.

| Item | Ruling | Decision |
|---|---|---|
| The 2026-10-26 doc-format rulings, re-filed on `main`, with the pilot's amendment | Agreed | `DDD-dec-94` |
| Format F1–F8, with point-of-use `ddd:ref` markers for projected claims only | Agreed | `DDD-dec-95` |
| Split `what.md` and `how.md`; `how-vocabulary.md` merged into `how-reference.md` | Agreed | `DDD-dec-95` |
| Acme Shop for the What and How, Varve for the method; Varve's What an `[OPEN]` successor item | Agreed | `DDD-dec-95` |
| Scope `applications/` only; `apparatus/` next | Agreed | `DDD-dec-95` |
| Sequence through Gate 3, then Emil's review | Agreed | `DDD-dec-95` |
