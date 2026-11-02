# Reader A

Verbatim final answer, extracted from the reader's transcript. The mapping of labels to versions is in `mapping.md`, written after scoring.

---

Answer: "customers can cancel an unpaid order" for Acme Shop. I used only the two files in g3/A: `what.md` and `acme-shop.ttl`. Below, w: is short for `https://acme.example/products/shop/what/`, and I shorten keys to their last 4 characters (for example, the Order entity is w:…0S1).

## The weakest point first

**The current What has no unpaid order.** The rest of this answer depends on how this is resolved.
- The Order entity (w:…0S1) is defined as "A placed, paid order."
- The only creating event, "Order placed" (w:…RJQ5), carries `paid_total`. Placing an order and paying for it are the same act.
- No field, event or state says an order is unpaid.

So "cancel an order that has not been paid yet" has no ground to be read against. Before cancellation can be specified, payment has to be split from placement. The documents do not settle how to do that. My proposal below is a guess, and I mark it as one.

---

## 1. What to add or change, and where each belongs

Where each item lives follows the domain/system test in §3: "the domain owns meaning and rules; a system owns surface and journey."

**A. Payment as a separate fact (Ordering domain). Guess, needs a ruling.**

| # | Item | New or changed | Within (`sdlc:within`) |
|---|---|---|---|
| A1 | Order entity definition: "A placed, paid order." becomes something like "A placed order, paid or not yet paid." | change, same IRI (§2.2: a property change keeps identity) | Order entity w:…0S1 (it stays in the Ordering context w:…QSS) |
| A2 | A new event, "Order paid", wire name `order-paid`, `sdlc:changes` Order, with a `paid_total` payload field (an `sdlc:Field` with its own wire name) | new | Ordering bounded context w:…QSS. The field sits within the event |
| A3 | Remove `paid_total` from "Order placed"'s `fieldOrder` | change | w:…RJQ5. §6 says changing the wire contract is a breaking change |
| A4 | A command that produces "Order paid", for example "Pay order" / `pay-order`, and a trigger for it, with the subject that issues it | new | context w:…QSS, and a system |

On A4, I do not know who pays or how. It might be an external payment provider, which would mean an `external` trigger with an external subject kind, or it might be automated. The documents give no ground for this. **This is a guess.**

**B. Cancellation rules and behaviour (Ordering domain, because both systems must agree on them)**

| # | Item | New or changed | Within |
|---|---|---|---|
| B1 | A state field on Order, for example `paid` (boolean) and `cancelled` (boolean), or one status field. Each is an `sdlc:Field` with `fieldType` from the datatype vocabulary | new | Order entity w:…0S1 |
| B2 | Invariant "cancel only unpaid", for example wire name `cancel-only-unpaid` with statement "An order may be cancelled only while it is unpaid." | new | Order entity w:…0S1 |
| B3 | Invariant "cancel by owner", wire name `cancel-by-owner`, mirroring the existing `refund-by-owner` | new | Order entity |
| B4 | Probably also "not already cancelled", and "a cancelled order cannot be paid". The second only applies if A2/A4 exist | new | Order entity |
| B5 | Command "Cancel order", wire name `cancel-order`, `sdlc:targets` Order, `sdlc:emits` B6. Its payload is possibly empty (an empty `fieldOrder`) | new | context w:…QSS |
| B6 | Event "Order cancelled", wire name `order-cancelled`, `sdlc:changes` Order | new | context w:…QSS |
| B7 | Ubiquitous term "Cancel" or "Cancellation" added to the bounded context. Optional | change | context w:…QSS |

Notes on B1, B2 and B3:
- B1: §3.4 says "A field belongs on an aggregate if and only if some Decider reads it". The Decider will read this field.
- B2: §3.3 says rejections are the aggregate's invariants. Invariants carry a wire name because they appear in rejections (§6, R-2).
- B3: alternatively, B3 could reuse one generic "by owner" invariant. I would keep a separate one, because the existing invariant's statement names refunds.

**C. The Order Decider (w:…R5A)**

| # | Change |
|---|---|
| C1 | `sdlc:handles` adds Cancel order (and Pay order if A4 is adopted). This satisfies "command coverage" and "no foreign commands". |
| C2 | `sdlc:reads` adds the B1 field or fields. The existing Customer `customer_id` claim (w:…AWBG) is already read, and it is what B3 uses. |
| C3 | `sdlc:rejects` adds B2, B3 and B4. |
| C4 | The new events go into its output alphabet, through the commands' `emits` ("output-alphabet containment"). Its evolve now folds Order cancelled (and Order paid). |
| C5 | `sdlc:logic` gets a new digest. The authored logic is a new artefact, and both hashes cover it (§2.3). |
| C6 | New `sdlc:Scenario` elements within the Decider. |

The C6 scenarios:
- Placed, unpaid, cancelled by its customer: emits order-cancelled.
- Placed and paid, then a cancel: rejects cancel-only-unpaid.
- Cancel by a customer whose `customer_id` differs: rejects cancel-by-owner.
- Already cancelled: rejects, if B4 is adopted.

Subject coverage (§3.7) needs a scenario for every (command, subject kind) pair in the alphabet. If Staff may also cancel, that pair needs its own scenario. If Staff may not, Staff is not in the cancel command's subject alphabet. That is a product choice the request does not state.

**D. Read side: the Order summary View (w:…N03) and its Projector (w:…AD2…E4)**

| # | Change |
|---|---|
| D1 | The View `sdlc:projects` adds Order cancelled (and Order paid). |
| D2 | A new view field, for example `status` or `cancelled`, with a wire name, so the customer can see that the order is cancelled. It is within the View. |
| D3 | The Projector `sdlc:folds` adds the same events (event coverage), and gets a new `sdlc:logic` digest. Projector scenarios are needed: §3.4 says "it is simulated before realisation". |
| D4 | Scope rules are unchanged. The fold stays keyed by `customer_id`. |

**E. The surface (system shop-bff, w:…7EG; system level because it is surface and journey)**

| # | Item | New or changed | Within |
|---|---|---|---|
| E1 | Trigger "customer cancels an order": `source` `sdlc:sourceUser`, `sdlc:subject` Customer (w:…Z8HH), `sdlc:issues` Cancel order. Source user is consistent with nature human (§3.2.0). | new | shop-bff |
| E2 | Interaction "cancel the order", `typedAs sdlc:aioTriggerAction`, `sdlc:command` Cancel order | new | UI step "Order detail" (w:…Y81) |
| E3 | The "Order detail" step's `sdlc:intent` (today "…asks for part of it back") and possibly its `emphasis` widened to cover cancelling | change, same IRI | w:…Y81 |
| E4 | Possibly a new `sdlc:ContentKey` (for example a cancel confirmation or cancelled notice, with a role) that the step `sdlc:references` | new | shop-bff |
| E5 | Possibly a new `sdlc:Flow` "cancel", or a rename of the "refund" flow (w:…BTH). The step can be the entry page. | new or change | shop-bff |

On E3, §3.2.1 says intent is debt. The meaning must be promoted into the model, which is what E2 and B2 do.

Consequences outside the What (§4.2), not authored here:
- E2 creates a new (interaction, web context) reification pair.
- E4 creates (key, en-GB) and (key, da-DK) content pairs.

Both are How bindings and coverage (how.md §8), anchored to the interaction or content key. I mention them only because the What computes these pairs.

shop-api (w:…ZA) has no triggers today. I would change nothing there. **This is a guess**, since "the ordering service other systems call" might need to expose cancellation.

---

## 2. How each addition gets into the What

- **Everything is a decision.** "The What changes only through decisions anchored to the elements they change" (§2.1, ruled). A decision is not itself a What element.
- **What is written.** For each new element:
  - a new IRI `P/what/<ULID>`, minted once with `what/mint.py` (§2.2);
  - an `rdfs:label`;
  - its kind (which can never change afterwards, §5.1);
  - its single `sdlc:within`;
  - its properties;
  - an authored `sdlc:wireName` for every kind that appears on the wire: commands, events, payload fields, invariants, view fields (§6).

  For changed elements, new property values are written under the same IRI. Decider and Projector logic is written as an artefact and recorded by digest.
- **What it is attached to (the anchor).**
  - A creating decision anchors "to the narrowest element that exists at the position it is proposed and covers every element it creates" (§2.1, `DDD-dec-63` §8). A new element is never its own anchor.
  - A changing decision anchors to the element it governs or changes.
  - The edge is the How vocabulary's `sdlc:anchor` (§7.1).

| Decision (my proposed split) | Creates or changes | Anchor, and why |
|---|---|---|
| D-1 domain facts: A1 to A3, B1 to B7 | creates fields, invariants, command, events; changes Order and Order placed | Ordering bounded context (w:…QSS). It is the narrowest existing element covering everything created, because the command and events sit directly in it and the fields and invariants sit within Order, which is within it. |
| D-2 Decider: C1 to C6 | changes the Decider, creates scenarios within it | the Decider (w:…R5A), which is both the changed element and the narrowest cover of the new scenarios |
| D-3 read side: D1 to D3 | changes View and Projector, creates a view field and scenarios | the bounded context if done as one decision (it covers both View and Projector). Alternatively split it: one anchored to the View, one to the Projector. |
| D-4 surface: E1 to E5 | creates trigger, interaction, maybe content key or flow; changes the step | shop-bff (w:…7EG), the narrowest cover of a trigger within the system and an interaction within the step |

**Why split.** One decision covering both the domain and shop-bff would have the product node as its narrowest cover. An anchor that broad blurs blast radius. §2.1 says the product anchor is only the "empty-What / new domain" case. A split also lets each decision fall within a single authoring scope (§5.1).

**Uncertainty.** I could not find how D-2 and D-4 declare that they depend on D-1, for example because they name D-1's command. See section 5.

- **Gathered material.** If any of this comes from a tool (Figma, a ticket system, an agent like me), it is only a proposal. It enters only when a human signs (§2.1, §5.2, `DDD-dec-43`). This answer is itself such a proposal.

---

## 3. Who must sign or approve

- **A human principal** must sign the acceptance. A tool never can (`DDD-dec-43`).
- **What they must hold:** either the genesis grant for Acme Shop, which is unscoped within the product (`DDD-dec-46`), or a grant delegated from the genesis whose scope covers the decision. Coverage means:
  - every element kind the decision creates, changes or retires is in the scope's set of kinds;
  - every such element is inside the scope's subtree, if the scope is narrowed by `within*` (§5.1).
- **The kinds each decision touches:**

| Decision | Kinds touched |
|---|---|
| D-1 | `sdlc:Entity`, `sdlc:Field`, `sdlc:Invariant`, `sdlc:Command`, `sdlc:Event`, and `sdlc:BoundedContext` if B7 is included |
| D-2 | `sdlc:Decider`, `sdlc:Scenario` |
| D-3 | `sdlc:View`, `sdlc:Field`, `sdlc:Projector`, `sdlc:Scenario` |
| D-4 | `sdlc:Trigger`, `sdlc:Interaction`, `sdlc:UIStep`, possibly `sdlc:ContentKey` or `sdlc:Flow` |

- **Spanning scopes.** If a decision spans scopes, it needs a valid acceptance under each one, from the same holder or different holders. It is in force only while all of those acceptances are live (§5.1, Round 5).
- **Not the subject kinds.** Being a "Customer" or "Staff" subject kind gives no authority over the specification. "A subject kind is never a grant" (§3.7).
- **Who that is at Acme is not in the documents.** No grant holders are named. §5.1 only gives the example of "the product owner's What scope". The authority profile, which defines grants and acceptance, does not exist yet (Q-4).

---

## 4. What is in force before and after, and when the change takes effect

- **Before.**
  - The decisions pinned by Acme Shop's current What-version (a `dpp/1` record listing every element by IRI and hash, §2.3) are in force.
  - In that What, an Order is placed-and-paid, and the only customer actions are place and refund.
  - No cancel command, event, invariant or trigger exists. A cancellation request is a foreign command to the Decider.
- **After.**
  - D-1 to D-4 (or whatever split is ruled) are also in force, with their new elements and changed properties.
  - The Decider accepts cancel-order from the order's customer while the order is unpaid. It rejects with `cancel-only-unpaid` or `cancel-by-owner` otherwise.
  - The Order detail step offers the action.
  - The previous property values of changed elements (the Order definition, the Decider's logic digest, the step's intent, the Order placed payload) are replaced under the same IRIs, and the decision history records them.
- **The moment.** By §5.1, a decision is in force when its acceptance is valid, and for a spanning decision only from the moment the last required acceptance is live. "In force" also requires an accepted decision chain back to the genesis (§7.2).
  - A new What-version record naming the new position, with a new graph hash, is needed to name and version that position. It confers no force (§2.3).
  - **My reading:** force begins at acceptance, not at the version record. The documents do not state the exact instant, for example signature time against a log position. See section 5.
- **The What is not the running shop.** Customers can actually cancel only once the How realises it: Decider code, the reification binding for the new interaction, content for any new keys. Whether a realisation conforms is a verdict computed from the scenarios and a recorded run, never stored (§6, §7.2).

---

## 5. What I did not understand, or was unsure about

1. **Paid versus unpaid.** The Order definition and the Order placed payload assume payment at placement. The request therefore conflicts with the current What, not just extends it. Splitting payment out (A2 to A4) is my guess, and it breaks the `order-placed` wire contract. It also touches the existing scenario (w:…YC), whose given event supplies `paid_total`. That scenario would then need changing, or a "paid" event added to its given.
2. **Who pays, and through which channel.** If A4 is adopted, I do not know whether the payer is the customer, an external payment provider (an external subject kind with an external trigger) or an automated process.
3. **Order identity on the wire.** No command carries an order id. How a cancel command (or any command) names its order is not stated. The Decider "decides for one aggregate", but the addressing is implicit.
4. **Subject claims inside `with`.** The example scenario puts the Customer claim field (w:…AWBG) inside the `when`'s `sdlc:with`. §6 says the subject is "supplied beside the command, never inside its `with`". I was unsure which pattern to follow for new scenarios.
5. **May Staff cancel?** The request names customers only. Subject coverage then requires either a (cancel, Staff) scenario, or that Staff is not in the cancel command's alphabet. I could not tell which, because the alphabet is "the subject kinds its commands are offered to or issued as".
6. **Anchoring a mixed decision.** One decision both creating elements and changing existing ones (D-2): I assumed it anchors to the narrowest element covering both. The rule in §2.1 only covers pure creation.
7. **Dependencies and ordering between decisions.** How D-2 and D-4 depend on D-1 being in force is not described. Nor is what happens if D-1's acceptance lapses while D-4's stays live.
8. **The decision record's format.** Decisions are pinned by a `dpp/1` What-version, and the anchor edge is `sdlc:anchor`. The decision's own fields, its signature and its acceptance format are not in these documents. They belong to the authority profile, which does not exist yet (Q-4). For the same reason, the "in force" half of conformance "cannot be claimed until it exists" (§7.2). I cannot say how an acceptance is technically recorded or checked today.
9. **Who holds grants at Acme.** No principals or grants are named, so I cannot name the signer.
10. **Flows.** I do not know whether a UI step can be in more than one flow. That decides whether cancelling needs a new flow or should widen "refund".
11. **Content keys.** I do not know whether a cancel action needs its own content key (E4), or whether the action's label is How or design-system material.
12. **The test product.** The `.ttl` header says it is "a test product only: nothing here is acceptable into a real product (ruling 4 of 2026-10-28)". I treated the question as hypothetical. I am unsure whether that header means no real acceptance of these changes is possible at all.
13. **Undefined vocabulary.** `ontology.ttl`, `shapes.ttl`, `how.md` and `mint.py` are referenced but were not provided. So I could not check:
    - exact property names, for example whether a payload-less command still needs `sdlc:fieldOrder ()`;
    - whether a boolean field shape exists;
    - whether my additions would pass the shapes.
