# Reader B

Verbatim final answer, extracted from the reader's transcript. The mapping of labels to versions is in `mapping.md`, written after scoring.

---

I read only the three files in `/tmp/claude-0/-home-claude/70769e4f-e4ea-541c-84f7-1e813b8ddd6c/scratchpad/g3/B/`: `what.md`, `what-reference.md` and `acme-shop.ttl`. Everything below comes from them, and guesses are marked **[GUESS]**.

## The weakest point: the What has no unpaid orders

The What has no such thing as an order that has not been paid.
- The `Order` entity is defined as "A placed, paid order."
- `Order placed` already carries `paid_total`.
- No command or event records a payment separately from placing the order.

So "cancel an unpaid order" cannot be stated against the current What without first deciding what "unpaid" means. That is a product question for the product owner. I would not settle it myself.

I see two options:
- **(A) Placing an order and paying for it become separate.** This adds a `Pay order` command and an `Order paid` event. It is a larger change, and it alters what `Place order` and `Order placed` mean.
- **(B) Keep the current events and treat `paid_total = 0` as unpaid.** This is the cheapest option. It still needs the `Order` definition changed.

**[GUESS]** I use option B below to keep the change small. Under option A, add those two elements and a `paid` field to the domain changes, in the same way.

## 1. What to add or change, and where it belongs

The test for placement is "would two systems disagree about it?" Cancellation rules must agree in every system, so they go in the domain. The button and the trigger go in the system that offers them.

| # | Addition or change | Kind | Where it sits (`sdlc:within`) |
|---|---|---|---|
| D1 | `Cancel order` command, wire name `cancel-order`, `sdlc:targets` the Order entity, `sdlc:emits` D2. Probably no payload fields, because the subject comes from the system, not the caller | `sdlc:Command` | Ordering bounded context |
| D2 | `Order cancelled` event, wire name `order-cancelled`, `sdlc:changes` the Order entity. Payload: none, or a `reason` field **[GUESS]** | `sdlc:Event` | Ordering bounded context |
| D3 | `cancelled` field (boolean) on the Order aggregate. It belongs there because the Decider must read it to refuse a second cancellation, and refunds and payments after cancelling | `sdlc:Field` | Order entity |
| D4 | Invariant "cancel only unpaid", wire name `cancel-only-unpaid`, with a statement such as "an order may be cancelled only while paid_total = 0" | `sdlc:Invariant` | Order entity |
| D5 | Invariant "cancel by owner", wire name `cancel-by-owner`: only the order's customer may cancel it. The existing `refund-by-owner` statement only covers refunds | `sdlc:Invariant` | Order entity |
| D6 | Invariant "not cancelled", wire name `not-cancelled`: a cancelled order cannot be cancelled again or refunded **[GUESS that you want this]** | `sdlc:Invariant` | Order entity |
| D7 | Change the existing `Order` entity's `sdlc:definition` from "A placed, paid order." to something like "A placed order, paid or not yet paid." This is a property change, so the IRI stays the same | change to `sdlc:Entity` | stays where it is |
| D8 | Change the existing Order Decider: add `sdlc:handles` D1, add `sdlc:reads` D3, add `sdlc:rejects` D4, D5 and D6, and give `sdlc:logic` a new digest for the new handwritten logic. "Output containment" means it may only emit D2 for D1. The Decider's IRI stays the same | change to `sdlc:Decider` | stays where it is |
| D9 | New scenarios for the Order Decider, each naming the subject it is issued as: cancel an unpaid order (emits D2), cancel a paid order (rejected by D4), cancel another customer's order (rejected by D5), cancel twice (rejected by D6). Subject coverage needs one scenario per command and subject kind, so a Staff scenario is needed too, unless Staff simply has no cancel trigger **[UNCLEAR]** | `sdlc:Scenario` | the Decider |
| D10 | **[Optional, GUESS]** Have the `Order summary` view also `sdlc:projects` D2, give the Projector `sdlc:folds` D2 and a new logic digest, and maybe add a `status` view field so customers can see the order is cancelled. Event coverage then makes the fold handle D2 | change to `sdlc:View` and `sdlc:Projector` | stays where it is |
| S1 | Trigger "customer cancels an order": `sdlc:source sdlc:sourceUser`, `sdlc:subject` Customer, `sdlc:issues` D1 | `sdlc:Trigger` | `shop-bff` |
| S2 | Interaction "cancel the order", `sdlc:command` D1, `sdlc:typedAs sdlc:aioTriggerAction` | `sdlc:Interaction` | the `Order detail` UI step (or a new step, see item 5 in section 5) |
| S3 | Content key for the cancel action's label, with a declared `sdlc:role`, referenced from the UI step. I am not sure an action needs a content key; the example only has one for the heading | `sdlc:ContentKey` | `shop-bff` |
| S4 | If cancelling gets its own screen instead: a new UI step offered to Customer, its interactions, its state annotations, and a `navigate` edge or a new flow | `sdlc:UIStep` and related | `shop-bff` |

Some things you do not write:
- The view states are derived, so no scope covers them.
- The accessibility obligations of the new trigger-action are inherited from the interaction type.
- The design-system and content pairs to cover (S2 in the `web` context, S3 in `en-GB` and `da-DK`) are computed from the What. Their bindings are How work.

`shop-api` needs no new element: it uses the whole Ordering domain, so it gets D1 to D10 automatically. Every new element gets an IRI of the form `P/what/<ULID>`, minted by `what/mint.py`.

## 2. How each addition gets into the What

Nobody edits the `.ttl` directly. Each change is a decision record that says what changes, and is attached to an anchor. The decision sits beside the What, not inside it.

The anchor rule for new elements is "the narrowest part that already exists and contains everything you are adding." An element being created can never anchor its own creating decision. The anchor link is `sdlc:anchor`, from the How vocabulary, which I was not given.

| Decision | Written content | Anchor | Why there |
|---|---|---|---|
| **Dec-1: domain** | Create D1, D2, D3, D4, D5, D6, D9 (and the D10 field); change D7, D8 (and D10) | the **Ordering bounded context** | It is the narrowest existing element containing everything created and changed. `what.md` gives this exact case: a `Cancel order` command "would anchor to the `Ordering` bounded context, where the other commands sit." |
| **Dec-1a: field (if split out)** | Create D3 | the **Order entity** | `what.md`: "Adding a field is a decision of its own, because a field is something other parts name: a wire contract changed." I do not know whether that forces D3 out of Dec-1 (see section 5). |
| **Dec-2: system** | Create S1, S2, S3 (S4) | **`shop-bff`** | The trigger and content key sit in `shop-bff`, and the interaction sits in `Order detail`, which is inside `shop-bff`. It must come after Dec-1, because S1 and S2 point at D1, and behaviour may only refer to structure that exists. |

Dec-1 and Dec-2 could be one decision anchored to the product, the narrowest element containing both. I would split them anyway, because:
- the domain part and the system part may fall under different scopes or different signers;
- they keep "what does this touch" readable.

**[GUESS]** I do not know the exact format of a decision record. What I can see:
- it is a `dpp/1` record;
- it carries an anchor;
- it uses `supersedes` when it replaces a decision.

After acceptance, a new What-version record can pin every decision in force (the founding decision, Dec-1 and Dec-2), with new element hashes and a new graph hash. The Decider's hash changes because its logic digest changes. The founding decision stays on record.

## 3. Who signs, and what they must hold

- **Who:** someone whose authoring scope covers every element kind the decision creates, changes or retires, inside the subtree the scope is limited to. In Acme Shop that is the **product owner**, who holds a What scope delegated from the genesis grant. The **founder**, who holds the genesis grant, covers everything in the product and could also sign.
- **What they must hold for Dec-1:** a scope that includes the kinds `sdlc:Command`, `sdlc:Event`, `sdlc:Field`, `sdlc:Invariant`, `sdlc:Scenario`, `sdlc:Entity` and `sdlc:Decider` (plus `sdlc:View` and `sdlc:Projector` if D10 is in). If the scope is limited to a subtree, that subtree must contain the Ordering bounded context.
- **What they must hold for Dec-2:** a scope that includes `sdlc:Trigger`, `sdlc:Interaction` and `sdlc:ContentKey` (plus `sdlc:UIStep` and `sdlc:Flow` for S4), with a subtree containing `shop-bff`.
- **Split scopes:** if no single scope covers a decision, it needs an acceptance under each scope, from the same person or different people.
- **Not the architect:** the architect's How scope covers How kinds, so it cannot accept these decisions.
- **Not me, and not a tool:** I am only a source of proposals. The decision is a proposal until a person whose scope covers it signs and accepts it, the same way the product owner accepted the founding decision with a second record.

**[UNCLEAR]** The documents do not list which kinds the product owner's What scope contains, or whether it is limited to a subtree. How grants are held and recorded is the authority profile (`authority.md`, pull request #45), which has not landed and which I was not given.

## 4. What is in force before and after, and when the change takes effect

**Before:** what is in force is the founding decision.
- The Order is "a placed, paid order".
- The commands are `place-order` and `refund-order`.
- The Decider can reject `order-has-lines`, `refund-by-owner` and `refund-within-paid`.
- A customer cannot cancel anything, and an unpaid order cannot be expressed.

**After:** the founding decision plus Dec-1 (and Dec-1a) and Dec-2.
- The What contains the cancel command, its event, the new field and invariants, the changed definition and Decider, the scenarios, and the `shop-bff` trigger and interaction.
- Earlier elements keep their IRIs. Their history is their decision history.

**When it takes effect:** the moment the decision's required acceptances are all valid ("in force only while all of those acceptances stand"). If it spans scopes, that is the moment the last required acceptance is given. It drops out of force if any of them stops standing. It does not take effect:
- when the decision is written; until accepted it is a proposal;
- when a What-version record is made ("A What-version confers no force", it only names the position);
- when code is deployed.

Dec-2 cannot meaningfully be in force before Dec-1, because it refers to D1.

Two cautions:
- The "in force" half of conformance, an accepted chain back to the genesis grant under the authority profile, "cannot be claimed until the profile exists". So today the change can only be *described* and accepted, not formally shown to be in force.
- Implementations are judged separately. Once Dec-1 is in force, the current implementation will fail the new scenarios on the conformance wire until it is built. That judgement is computed at a position and never stored.

## 5. What I did not understand or was unsure about

1. **"Unpaid" does not exist in the model.** The definition says "paid", and placing an order already carries `paid_total`. Whether `paid_total = 0` means unpaid, or payment becomes a separate step, is a product decision I cannot make from the documents.
2. **Is a field always its own decision?** "Adding a field is a decision of its own" is unclear on whether D3, or the payload fields of a brand-new command or event, must be separate decisions or may ride with their owner's creating decision.
3. **The authority profile is missing.** `authority.md` (pull request #45) is not provided. I do not know the product owner's actual scope, how a grant or acceptance is recorded, or whether one person may both author and accept.
4. **Decision record format.** It is a `dpp/1` record with `sdlc:anchor` and `supersedes`, but neither the How vocabulary nor the protocol was given, so I cannot write a real record.
5. **Intent only ever shrinks.** `Order detail`'s intent is "checks an order and asks for part of it back." Adding cancel there seems to need broader intent, which conflicts with the rule that intent never grows. The alternative is a separate UI step (S4). I do not know which is right.
6. **Subject coverage is ambiguous, and possibly already unmet.** "Every pair of command and subject kind" could mean all subject kinds (Customer and Staff) or only those the Decider serves. The existing What has one scenario, Refund as Customer, so it looks incomplete already unless the narrower reading is meant. Nothing says whether staff should be able to cancel.
7. **The scenario passes the subject's claim like a payload field.** The existing scenario puts the Customer claim `customer_id` inside the command's `sdlc:with`, beside `amount`. This sits oddly with "the subject is never a payload field" and with the wire's separate subject block. I am not sure how a cancel scenario should supply the claim.
8. **No meaning for the `present` state.** `Order detail` gives a meaning for `empty` but not for `present`, although "it must give a meaning to every state the projection can be in." Perhaps `present` is exempt, but that is not stated. If D10 adds a cancelled status to the view, the step may need a meaning for it.
9. **Should cancelling also stop refunds?** `refund-within-paid` already blocks refunds when `paid_total = 0`. Whether D6 is needed, and whether cancelling a paid order should ever be possible, is a product question.
10. **Content keys for actions.** The example only has a heading key. I do not know whether every trigger-action needs its own content key for its label.
11. **Decider logic is held only by digest.** I could not see the actual logic in `what/examples/logic/`, so I cannot say how much it must change.
12. **Smaller points:**
    - The ordering between Dec-1 and Dec-2 is my inference from "behaviour may not refer to structure that does not exist"; it is not stated for decisions.
    - Whether a system decision may point at a domain element under the same anchor rules is not spelled out.
    - The element count of 44 matches the file.
