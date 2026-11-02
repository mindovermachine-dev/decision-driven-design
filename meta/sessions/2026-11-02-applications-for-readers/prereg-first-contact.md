# Pre-registration — Gate 3 first-contact test

Committed before any Gate 2 rewrite exists. Its SHA-256 is re-verified in the Gate 3 report.

## What is tested

Whether a reader who has not seen the old text does a real task better from the rewritten What
(`what.md` plus `what-reference.md`) than from the old `what.md` at `e5a332d`. The two versions
carry the same rules. Only the presentation differs.

## The task, given verbatim to every reader

> You are joining the team that owns Acme Shop, a small web shop. Its specification of what the
> software is and does (its "What") is described by the document(s) you are given, and its full
> What is the attached file `acme-shop.ttl`.
>
> Acme Shop wants customers to be able to cancel an order that has not been paid yet.
>
> 1. List what you would add to or change in the What, and say for each where it belongs.
> 2. Say how each addition gets into the What: what is written, what it is attached to, and why
>    there.
> 3. Say who must sign or approve it, and what that person must hold to be allowed to.
> 4. Say what is in force before and after, and at what moment the change takes effect.
> 5. List anything in the documents you did not understand, or were unsure about.
>
> Answer from the documents only. Say where you are guessing.

## The readers

- Four fresh model agents, none of which has seen any version of the text or this session.
- Two receive the old `what.md` (from `e5a332d`) and `acme-shop.ttl`.
- Two receive the new `what.md`, `what-reference.md` and `acme-shop.ttl`.
- Each receives the files under neutral names, with no session or repository context.
- Limitation, stated now: these are model proxies, not junior engineers. A human first-contact
  test remains a successor item whatever the result.

## The rubric

Scored by a fifth fresh agent that sees only the rubric and the four answers under blind labels.
One point per criterion met.

| # | Criterion | Hard |
|---|---|---|
| K1 | Adds a command (cancel) and an event (cancelled) to the `Ordering` domain's event model | |
| K2 | Puts the rule "only unpaid orders can be cancelled" in executable behaviour: the Order Decider, or an invariant the Decider enforces | |
| K3 | Anchors each creating decision to the narrowest existing element that covers what it creates (for example the `Ordering` domain), and says it is not anchored to the new element itself | **yes** |
| K4 | Says the What is not edited: every change is a decision, and a tool may only propose | |
| K5 | Says the signer must hold a grant (an authoring scope) covering these element kinds, delegated from the product's founding grant | **yes** |
| K6 | Says the change is not in force until accepted by a human holder, and that a new What-version then names the What in force | **yes** |
| K7 | Says the new elements get new identities, and that `Order` keeps its existing identity | |
| K8 | Addresses who may cancel: customers only their own orders, using the What's subject and scope rules | **yes** |

The hard criteria are those whose answer the old text places inside a decision-cited passage, an
appendix or a reference section a practitioner would not reach first.

## The falsifier

It fires if **either** limb holds:

1. **No gain where it should show.** The new text's mean score on the hard criteria (K3, K5, K6,
   K8) is not above the old text's mean on them.
2. **The format is the confusion.** Any new-text reader lists, under task item 5, the format's
   own devices (the "not settled yet" marking, the "Where this comes from" table, or the split
   between documents) as something it did not understand.

**Also reported, not part of the falsifier:** the mean on all eight criteria; any old-text reader
naming ids, section numbers or register tags as confusing; and any content confusion common to
both versions.

## If it fires

Limb 1: F3 and F7 are not shown to help this reader. The fallback named in Gate 1 applies: ids
stay out of sight, but invisible point-of-use markers replace the closing table as the trail.
Emil rules. Limb 2: the named device is changed or removed before the format reaches `apparatus/`.

## Mechanical predictions for Gate 2, checked before Gate 3 runs

| # | Prediction |
|---|---|
| M-1 | In every rewritten document, no decision or claim id appears outside the `ddd:doc` block and the "Where this comes from" section |
| M-2 | `python3 scripts/ci.py` passes after every Gate 2 commit |
| M-3 | An independent agent, given each old and new document pair, finds no rule in the old text that is absent from the new text or changed in meaning. Any it finds is reported in the Gate 2 report and resolved before Gate 3 |
