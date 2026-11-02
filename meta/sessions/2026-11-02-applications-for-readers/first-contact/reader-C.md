# Reader C

Verbatim final answer, extracted from the reader's transcript. The mapping of labels to versions is in `mapping.md`, written after scoring.

---

I read only the two files in the folder: `what.md` (the rules) and `acme-shop.ttl` (the What). My answer comes from those two files. I mark my own guesses as **[GUESS]**.

## Main finding first

The current What has no such thing as an unpaid order. The Order entity is defined as "A placed, paid order." The `Order placed` event already carries `paid_total`, so placing an order and paying for it are one act. Before cancellation can be specified, the team must decide how "not yet paid" exists in the model. That decision has a wider effect than the cancel feature. It may change the `Order placed` wire contract, and §6 calls a change to a wire name "by definition a breaking change to the wire contract". Adding or removing a payload field is not named there, but it changes the same contract. **[GUESS]** I would split payment out of placement, but the owner of the Ordering domain must rule on this.

## 1. What to add or change, and where it belongs

The prefix `w:` stands for `https://acme.example/products/shop/what/`. "New" means a new element with a fresh `P/what/<ULID>` minted by `what/mint.py` (§2.2).

| # | Addition or change | New or changed | Where it is (`sdlc:within`) |
|---|---|---|---|
| A | **Payment state.** **[GUESS]** A new command `Pay order` (wire name `pay-order`) and event `Order paid` (`order-paid`). The `paid_total` payload field moves from `Order placed` to `Order paid`. Who pays is unknown; it may be an external payment subject kind. A minimal alternative is one boolean field `paid` on Order. | New elements, plus a change or retirement of the existing payload field `w:…959BR6Y50HZ3WME4` | Bounded context Ordering `w:…H5Y3FP9BFRZJ6QSS` |
| B | Order's `sdlc:definition`, for example "A placed order, paid or not yet paid, or cancelled" | Property change, same IRI (§2.2) | Order entity `w:…CAGMKBDKSY0GQ0S1` |
| C | Command `Cancel order`, wire name `cancel-order`. It `targets` Order and `emits` the event in D. Payload: none **[GUESS]**, because the owner check comes from the subject's claim. A `reason` field is optional. | New | Bounded context Ordering |
| D | Event `Order cancelled`, wire name `order-cancelled`, with `changes` Order | New | Bounded context Ordering |
| E | A field `cancelled` (boolean) on Order, plus the `paid` field if A is not done | New `sdlc:Field` | Order entity |
| F | Invariant `cancel only unpaid` (`cancel-only-unpaid`). Invariant `cancel by owner` (`cancel-by-owner`): only the order's customer may cancel it. Optionally `not already cancelled`, and a rule that a cancelled order cannot be paid. | New `sdlc:Invariant` | Order entity, beside the existing invariants |
| G | Decider `Order` `w:…MMP5V59XRNHD39R5A`: add the command from C to `handles`, the new fields to `reads`, and the new invariants to `rejects`. Its `sdlc:logic` gets a new digest because the logic artefact changes. | Property change | Decider (the Decider itself) |
| H | Scenarios. §3.7's subject-coverage check needs one per (command, subject kind) pair: Customer cancels own unpaid order → `Order cancelled`; Customer cancels a paid order → reject `cancel-only-unpaid`; Customer cancels someone else's order → reject `cancel-by-owner`. | New `sdlc:Scenario` | Decider `Order` |
| I | View `Order summary` `w:…FTV81M9FR1TXEN03` adds `Order cancelled` (and `Order paid`) to `projects`. It gets a new view field `status` or `cancelled` with a wire name (R-2). Projector `w:…D2PDDKQRCW18Z0E4` adds the event(s) to `folds` and gets a new logic digest. | Property changes, plus a new view field | The View and the Projector, both in Ordering |
| J | Trigger `customer cancels an order`: `source` `sourceUser`, `subject` Customer `w:…MMSAY8ZWD1TMMZ8HH`, `issues` the command from C | New `sdlc:Trigger` | System `shop-bff` `w:…8K9PG653537FE7EG` |
| K | Interaction `cancel the order` typed `aioTriggerAction`, with `command` the cancel command | New `sdlc:Interaction` | UI step `Order detail` `w:…76HYQ9AXTP6ZDY81` |
| L | The `Order detail` step's `intent` and `emphasis` (both now about refund only). If the button needs a label: a new `sdlc:ContentKey` (role **[GUESS]** "action") that the step `references`. | Property change; new content key | The UI step; the content key goes within `shop-bff` |
| M | Optional: the product's `sdlc:purpose` ("Sell … and refund them"), and the Ordering context's `ubiquitousTerm` gets "Cancellation" | Property change | Product node; bounded context |

Nothing is needed for:
- **New subject kinds.** Customer already exists and its `customer_id` claim is what the owner rule reads.
- **New View states.** Cancelled is data, not a state; the closed set is present, loading, empty and failed.
- **`shop-api`.** It has no triggers today. **[GUESS]** Cancelling through the API would need an external subject kind.

The How side is out of scope (§1.2, §4.2). It has two follow-ons:
- reification coverage for the new interaction in the `web` context;
- content coverage for any new content key in `en-GB` and `da-DK`.

## 2. How each addition gets into the What

- **What is written.** A decision, not a direct edit. The What changes only through decisions, and a decision is not itself a What element (§2.1). Each decision carries the triples it creates or changes. New elements get fresh ULIDs and authored wire names. Wire names must be unique product-wide for commands, events and invariants, and unique within their owner for fields (§6, R-1).
- **What it is attached to.**
  - A decision that changes elements anchors to the elements it changes (§2.1). That gives B → Order entity, G and H → Decider, I → View and Projector, L → UI step, and M → product or bounded context.
  - A decision that creates elements anchors to "the narrowest element that exists at the position it is proposed and covers every element it creates" (§2.1, `DDD-dec-63` §8). A new element is never its own creating decision's anchor.
  - So C, D and the new payment elements anchor to the Ordering bounded context. E and F anchor to the Order entity. H anchors to the Decider. J anchors to `shop-bff`. K anchors to the `Order detail` step.
- **Why there.** Anchoring narrowly keeps each decision inside the subtree that a grant's scope can cover (§5.1). It also keeps blast radius a single `within*` walk. If I bundled everything into one decision, the only element covering every created element would be the product node. That is allowed but coarse, and it pulls every scope into one acceptance. **[GUESS]** I would split the work into:
  1. a domain decision (A–I);
  2. a system decision (J–L).
- **Gathered material.** If a design tool or ticket supplies any of this, it is only a proposal. It enters the What only when a human signs it (§2.1, §5.2).

## 3. Who must sign, and what they must hold

- A **human principal** must sign the acceptance. Tools never change the What (`DDD-dec-43`).
- That person must hold either:
  - **the genesis grant** for `https://acme.example/products/shop`, which is unscoped within the product (`DDD-dec-46`); or
  - **a grant delegated from the genesis** whose scope contains the kind of every element the decision creates, changes or retires, and covers that element's subtree.
- Grants and scopes the decisions need:

  | Decision | Scope must contain | Subtree |
  |---|---|---|
  | Domain decision | `sdlc:Command`, `sdlc:Event`, `sdlc:Field`, `sdlc:Invariant`, `sdlc:Entity`, `sdlc:Decider`, `sdlc:Scenario`, `sdlc:View`, `sdlc:Projector` (and `sdlc:BoundedContext` if M is done) | the Ordering domain or bounded context |
  | System decision | `sdlc:Trigger`, `sdlc:Interaction`, `sdlc:UIStep`, `sdlc:ContentKey` | `shop-bff` |
  | Purpose change (M) | `sdlc:Product` | needs the genesis holder or a grant at product level |

- **A decision spanning scopes** needs a valid acceptance under each scope, from one holder or several. It is in force only while all of those acceptances are live (§5.1, Round 5).
- **Not stated anywhere:** who actually holds these grants for Acme Shop. The documents say the genesis grant, grants and acceptance belong to the authority profile, which is a later pull request (Q-4). The ttl declares no grants. §5.1 offers only one illustration: "the product owner's What scope and the architect's How scope".

## 4. What is in force before and after, and when the change takes effect

- **Before.**
  - The What in force is every element with an accepted decision chain back to the genesis (§7.2).
  - A What-version record pins those decisions (§2.3).
  - Behaviour in force: a customer can place and refund orders. Orders are paid when placed. No cancel command, event, invariant or trigger exists.
- **After.**
  - The new and changed elements are in force, together with the decisions that created or changed them.
  - Changed elements keep their IRIs.
  - If payment is split (A), a moved field is a new element. §2.2 suggests old and new would be linked with `sdlc:succeeds`. That would change the graph hash.
- **The moment it takes effect.**
  - It is when the required acceptance is signed by a holder whose grant covers it.
  - For a decision spanning scopes, it is when the last required acceptance is live, and only for as long as all of them stay live.
  - It is **not** when a new What-version record is cut. A record "confers none" (§2.3) and only names the position afterwards.
  - It is **not** when the code ships. Whether a realisation conforms is a verdict computed at the gate and never stored (§7.2, §6). The What can require cancellation before any code does it, and the gap shows up as a computed verdict.

## 5. Things I did not understand or was unsure about

1. **Unpaid orders do not exist.** "Not paid yet" contradicts the Order definition and the `Order placed` payload. How payment enters the model is a prerequisite ruling, and I could not settle it from the documents.
2. **Force does not yet exist.** The authority profile, grants and acceptance mechanics are deferred (Q-4). The "in force" half of conformance "cannot be claimed until it exists". The ttl also says "nothing here is acceptable into a real product", and `what.md` is "moved … not yet ratified". So sections 3 and 4 above are the intended rule, not something that can be done today.
3. **Decisions that both create and change.** One decision that creates elements and changes others (for example, adding the cancel command and changing the Decider's `handles`) has two possible anchors. The text gives a rule for each case, not for the mix. It refers to "How ruling 1 (`DDD-dec-55`)", which I did not have.
4. **Derived or authored?** §3.3 says a Decider's signature (handles, emits, rejections) is derived and "only the logic is authored". Yet the ttl asserts `handles`, `reads` and `rejects` on the Decider. I am unsure whether a change to these is authored, and therefore needs a decision, or is recomputed.
5. **Claim placement conflict in the example.** The existing scenario puts the Customer's `customer_id` claim (`w:…QHZ7H4Y0GVEQAWBG`) inside the command's `sdlc:with`. §6 says the subject is supplied "beside the command, never inside its `with`". I could not tell which is right, so I am unsure how to write the cancel scenarios.
6. **Scopes and fields.** Scopes are sets of element kinds, but `sdlc:Field` is one kind for attributes, payload fields, view fields and claims. A grant can only tell them apart by subtree. Whether that is intended is unclear.
7. **Wire changes.** §6 says changing a wire name is a breaking change. Whether moving `paid_total` out of `Order placed` needs any extra handling, beyond being a What decision, is not stated.
8. **Missing Projector scenarios.** The example's Projector has no scenarios. §3.4 says Projectors are "simulated before realisation", so I am unsure whether the view-field change also needs projection scenarios. I assume yes.
9. **Content key role.** I do not know the allowed values for `sdlc:role` on a content key; only "heading" appears. Nor do I know whether a button label needs a content key at all.
10. **Flow membership.** The `Order detail` step is `inFlow` "refund". Adding cancel there may mean the step belongs to a broader flow, or that "cancel" needs its own flow. The text does not say.
11. **Unknown references.** I could not resolve several things the text names: `what/shapes.ttl`, `what/ontology.ttl`, `how.md`, Writ's [D2] conjunction and the `dpp/1` record format. They were not in the folder, so anything they add is outside this answer.
