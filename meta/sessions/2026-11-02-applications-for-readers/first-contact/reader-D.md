# Reader D

Verbatim final answer, extracted from the reader's transcript. The mapping of labels to versions is in `mapping.md`, written after scoring.

---

Sources: I read only the three files in `/tmp/claude-0/-home-claude/70769e4f-e4ea-541c-84f7-1e813b8ddd6c/scratchpad/g3/D/`: `what.md`, `what-reference.md` and `acme-shop.ttl`. Anything not stated in them is marked **GUESS**.

## The weakest point first

**The What has no unpaid order.** The `Order` entity is defined as "A placed, paid order." The `Order placed` event already carries `paid_total`, so placing an order and paying for it are one event. Nothing records that an order is unpaid, and nothing records it becoming paid later.

So "cancel an order that has not been paid yet" needs two things:
- a notion of payment state;
- a cancel command.

The first is a product decision, and the documents do not settle it. I propose a shape for it below, but the product owner has to choose.

## 1. What to add or change, and where it belongs

The split follows the test in `what.md`: "would two systems disagree about it?"
- The rule that only unpaid orders can be cancelled is the same in every system, so it belongs to the **domain**: Ordering domain → `Ordering` bounded context.
- The button and the trigger are **system** matters, so they go in `shop-bff`.

### A. Domain: inside the `Ordering` bounded context (`w:01M610JNAMH5Y3FP9BFRZJ6QSS`)

| # | Add or change | Kind | Placed within |
|---|---|---|---|
| A1 | **Change** the `Order` entity's definition from "A placed, paid order." to something like "A placed order, paid or not yet paid." This is a property change, so the identity is kept | Entity (existing `w:…CAGMKBDKSY0GQ0S1`) | as now |
| A2 | **Payment state.** **GUESS**, with two options. (a) Orders can be placed unpaid (`paid_total` = 0), and a new `Pay order` command and `Order paid` event record payment; the payment would probably come through an `external` trigger. (b) Add an Order field such as `paid` (boolean). Either way the product owner must rule, because it changes what `Order placed` means. Changing `Order placed`'s payload is a breaking wire change | Command, Event, Fields | Ordering BC; fields within their owners |
| A3 | New field on the `Order` aggregate: `cancelled` (boolean), or a `status` field. It qualifies only because the Decider reads it ("a field belongs on an aggregate iff some Decider reads it") | Field | within `Order` |
| A4 | New command `Cancel order`, wire name `cancel-order`, `targets` Order, `emits` Order cancelled. It needs no payload. The existing commands carry no order id either, which I found odd (see section 5) | Command | Ordering BC |
| A5 | New event `Order cancelled`, wire name `order-cancelled`, `changes` Order. It may have an empty payload | Event | Ordering BC |
| A6 | New invariants, each with a wire name and a statement: `cancel only unpaid` ("An order with paid_total > 0 cannot be cancelled"); `cancel by owner` ("Only the order's customer may cancel it"); `not already cancelled`. Possibly also `no refund/pay after cancel` | Invariant | within `Order` |
| A7 | **Change** the `Order` Decider (`w:…MMP5V59XRNHD39R5A`): add Cancel order to `handles`; add A6 to `rejects`; add the new fields and the Customer `customer_id` claim to `reads`; give `sdlc:logic` a new digest for the new hand-written logic. The Decider must keep command coverage, output containment and subject coverage | Decider (existing) | as now |
| A8 | New scenarios, one per pair of command and subject kind, each showing acceptance or a reachable rejection. For Cancel order × Customer: unpaid and own order → `Order cancelled`; paid → reject `cancel-only-unpaid`; someone else's order → reject `cancel-by-owner`; cancelled twice → reject. Add Staff scenarios only if staff may cancel (open question) | Scenario | within the Decider |
| A9 | **Change** the `Order summary` View and Projector: add `Order cancelled` to the View's `projects` and the Projector's `folds` (event coverage), with a new fold digest. Probably add a view field such as `status` or `cancelled` so the customer can see that the order is cancelled. Add a Projector scenario | View, Projector (existing), Field, Scenario | View and Projector as now; the field within the View; the scenario within the Projector |

### B. System: inside `shop-bff` (`w:01M610JNAM8K9PG653537FE7EG`)

| # | Add | Kind | Placed within |
|---|---|---|---|
| B1 | Trigger "customer cancels an order": `source` user, `subject` Customer, `issues` Cancel order | Trigger | shop-bff |
| B2 | Interaction "cancel the order": `typedAs sdlc:aioTriggerAction`, `command` Cancel order | Interaction | UI step `Order detail` (`w:…76HYQ9AXTP6ZDY81`) |
| B3 | **GUESS.** A content key for the cancel action's label, with a declared role, because text is never literal in a UI step. The existing refund action has no content key, so I am not sure one is needed | ContentKey | shop-bff |
| B4 | **Possibly** a state annotation, or a change to emphasis, if the screen should say what "cancelled" means. Do **not** widen `intent`: intent "shrinks monotonically… never grows" | StateAnnotation | Order detail |

**Not affected:**
- **Product level.** There is no new domain, no cross-system journey and no new quality demand. The residency constraint is untouched.
- **`shop-api`.** It has no triggers in the example, so I add none (see section 5).
- **Reference data.** None is involved.

## 2. How each addition gets into the What

Nobody edits the What. Each change is a **decision**: a short record that says what changes and points at its **anchor**. Decisions sit beside the What, not in it. The founding decision, and the product owner's acceptance of it, stay on record.

Anchor rules:
- A decision that **creates** elements anchors to "the narrowest element that already exists and covers everything it creates". A new element is never its own creating decision's anchor.
- A decision that **changes** an element anchors to that element.
- **"Adding a field is a decision of its own"**, because a field is a wire contract.

Proposed decisions:

| Decision | Anchor | Why there |
|---|---|---|
| D1: create Cancel order, Order cancelled, the invariants (A4–A6) and the Decider scenarios (A8) | `Ordering` bounded context | `what.md` gives this exact case: "if you added a `Cancel order` command, its decision would anchor to the `Ordering` bounded context". The BC is the narrowest existing element containing the command, the event, the invariants (inside Order) and the scenarios (inside the Decider) |
| D2: change the Order definition (A1) | `Order` entity | It is a property change to that element |
| D3: add the `cancelled`/`status` field to Order (A3) | `Order` entity | It is its own decision, and Order is the field's container |
| D4: payment state (A2), as a command, event and fields, or a field | Ordering BC, or `Order` | The same narrowest-container rule. This needs a product ruling first |
| D5: change the Decider (A7) | `Order` Decider | It changes `handles`, `rejects`, `reads` and the logic digest |
| D6: change the View, Projector and view field (A9) | `Order summary` View and Projector (the field decision on the View) | They are the elements changed or containing the change |
| D7: shop-bff trigger, interaction and content key (B1–B3) | `shop-bff`, which is narrowest for all of them. Alternatively, two decisions: the trigger → shop-bff, the interaction → `Order detail` | Narrowest container |

**Order matters.** "Behaviour may not refer to structure that does not exist."
- D1 (and D4) must be in force before D5 and D6.
- D7 refers to the command, so it comes after D1.

Within the What itself, everything is written in the `acme-shop.ttl` form. Each new element:
- gets a new IRI `P/what/<ULID>` minted by `what/mint.py`;
- carries an `rdfs:label`, a `sdlc:within` edge and, where it appears on the wire, an `sdlc:wireName`.

After the change, a new What-version record (`dpp/1`) pins all decisions in force and lists every element hash.

If a tool or an agent (including me) drafts this, the draft is only a **proposal**. A tool is a source, never an author.

## 3. Who signs or approves, and what they must hold

- **Possible signers.** Someone whose **authoring scope** covers every element kind the decision creates, changes or retires, inside the subtree the scope is limited to:
  - D1–D6 touch `sdlc:Command`, `Event`, `Invariant`, `Field`, `Entity`, `Decider`, `Scenario`, `View` and `Projector`;
  - D7 touches `Trigger`, `Interaction` and `ContentKey` (and `StateAnnotation` and `UIStep` if B4 is done).
- **In Acme Shop:**
  - The **product owner** holds a *What scope* delegated from the genesis grant, so they are the expected signer.
  - The **founder** holds the **genesis grant**, which covers every kind everywhere under the product, so the founder could also sign.
  - The **architect's How scope** does not cover What kinds, so the architect cannot sign.
- **A decision spanning several scopes** needs a valid acceptance under each one, from the same person or from different people. For example, design might hold UI steps, interactions and content keys. The decision is in force only while all of those acceptances stand.
- **Not me.** As a new team member I hold no grant, so I can only propose. Writing a specification does not make anyone a subject of the product.
- **The chain.** The signer's grant must chain back to the genesis grant through delegation.
- **Unknown mechanics.** How grants are held, and how signing and acceptance work, is the authority profile's job (`authority.md`, PR #45). It is not in my documents, so I cannot say more.

## 4. What is in force before and after, and when the change takes effect

**Before:**
- The founding decision is in force (all 44 elements), with the product owner's acceptance.
- No cancellation exists. Orders are by definition paid at placement.
- `Cancel order` is not a command any Decider handles. An implementation that emitted `Order cancelled` would break output containment against the current What.

**After:**
- Everything above remains in force, plus D1–D7.
- The Order Decider handles three commands, has the new rejections and has new logic.
- The View and Projector fold `Order cancelled`.
- shop-bff offers the cancel action to Customers on `Order detail`.
- The founding decision is not removed. The current form of each element is the result of all the decisions anchored to it.

**When it takes effect.** Each decision takes effect when its acceptance is valid: when every required acceptance under every scope it spans exists and is live. It stays in force only while they all stand.
- A new What-version record does **not** bring the change into force ("a What-version confers no force"). It only names the new position.
- Whether the software actually supports cancellation is a separate verdict. It is computed by the gate (Writ) at a position from the What's scenarios and a recorded run, never stored.
- **GUESS:** the How then gains work as baseline entries: a concrete control for the new trigger-action, and words for the content key in `en-GB` and `da-DK`.

**Caveat.** "In force" requires a chain back to the genesis grant under the authority profile. `what.md` says that half "cannot be claimed until the profile exists". Strictly, then, the documents do not yet let anyone claim that the new state is in force.

## 5. What I did not understand, or was unsure about

1. **Payment.** The documents never model an unpaid order (see the weakest point). I cannot tell whether "not paid yet" means `paid_total = 0`, a missing payment event, or something else.
2. **One anchor or many.** I am unsure whether one decision can create new elements *and* change several existing ones under a single anchor, such as the BC whose subtree covers them all. The alternative is one decision per changed element. The documents state the anchor rule for creation and say "points at the part it changes" for changes, but not for a mix of the two.
3. **"Adding a field is a decision of its own."** Is the field a separate decision even when its owner (a new event's payload field) is created in the same change? If it is, its anchor would be an element that does not exist yet. Must it wait until the event's decision is in force?
4. **Supersession.** Does changing the Order definition supersede the founding decision for that element? `supersedes` is mentioned only as a protocol edge, without rules.
5. **Order identity.** No command carries an order id, and the aggregate has no id field. How a command picks its order is not modelled.
6. **Claim inside the command.** The existing scenario puts the Customer claim `customer_id` inside the command's `sdlc:with`, beside `asSubject`. That seems to contradict "the subject… is never a payload field" and "supplied beside the command, never inside its `with`".
7. **Subject coverage.** Is it computed over all subject kinds, or only those the Decider serves? The existing Decider has one scenario for two commands, so it already seems short of the per-pair rule (that check is "not yet automated").
8. **Staff.** Should staff be able to cancel? `Order summary` lets staff see every order, but no surface is offered to Staff.
9. **`shop-api`.** It is a "service other systems call" with no triggers or `external` subject kinds. I could not tell whether cancellation must also appear there.
10. **Content keys.** Does a `trigger-action` need its own content key? The refund action has none.
11. **Authority profile.** It is not available (PR #45), so how grants are held and signed, and the exact What scope of the product owner (which kinds, which subtree), are unknown.
12. **Test product.** The `.ttl` header says this is a test product, and "nothing here is acceptable into a real product". I treated the exercise as hypothetical.
13. **Intent.** Adding cancellation to `Order detail` arguably changes what the step is for. But intent "never grows", so I was unsure whether the change belongs on this step or on a new UI step in a new flow.
