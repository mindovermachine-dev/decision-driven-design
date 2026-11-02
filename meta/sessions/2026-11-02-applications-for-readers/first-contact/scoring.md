# Scoring

Verbatim report of the blind scorer.

---

## Scores

| Answer | K1 | K2 | K3 | K4 | K5 | K6 | K7 | K8 | Total |
|---|---|---|---|---|---|---|---|---|---|
| W | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 8 |
| X | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 8 |
| Y | 1 | 1 | 1 | 1 | 1 | 1 (borderline) | 1 | 1 | 8 |
| Z | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 8 |

None of the 32 cells scored 0. All four answers meet every criterion, so the rubric does not tell them apart. I applied the same reading to each answer. The quotes below support K3, K6 and K8, the criteria most likely to be borderline. They also include the one real borderline call, Y on K6.

**K3: narrowest existing anchor, and a new element is not its own anchor.**
- W: "An element being created can never anchor its own creating decision." Its Dec-1 is anchored to the "Ordering bounded context … the narrowest existing element containing everything created and changed".
- X: "A new element is never its own anchor." Its D-1 is anchored to the Ordering BC as "the narrowest existing element covering everything created". Its D-2, which creates scenarios, is anchored to the Decider as "the narrowest cover of the new scenarios".
- Y: "A new element is never its own creating decision's anchor." Its D1 is anchored to the `Ordering` BC, and the new field (D3) to the existing `Order` entity.
- Z: "A new element is never its own creating decision's anchor." Under that rule: "C, D … anchor to the Ordering bounded context. E and F anchor to the Order entity. H anchors to the Decider." Z applies the narrowest-element rule at the finest grain of the four.

**K6: both halves required (a human holder accepts, and a new What-version names the What in force).**
- W: "The decision is a proposal until a person whose scope covers it signs and accepts it." Also: "After acceptance, a new What-version record can pin every decision in force", and a What-version "confers no force … it only names the position".
- X: "A human principal must sign the acceptance. A tool never can." Also: "A new What-version record naming the new position … It confers no force."
- Y (borderline 1): "Each decision takes effect when its acceptance is valid." Also: "After the change, a new What-version record (`dpp/1`) pins all decisions in force", and the record "only names the new position". Y never writes the word "human". It does name the product owner or founder as signer, and says "A tool is a source, never an author." I took that as meeting the human-holder half.
- Z: "A **human principal** must sign the acceptance." Also: "It is **not** when a new What-version record is cut. A record 'confers none' … and only names the position afterwards."

**K8: customers cancel only their own orders, through the subject and claim rules.** All four add a `cancel-by-owner` invariant and a trigger with subject Customer.
- W: "the subject comes from the system, not the caller".
- X: "The existing Customer `customer_id` claim … is what B3 uses".
- Y: "add … the Customer `customer_id` claim to `reads`".
- Z: "the owner check comes from the subject's claim".

**The other criteria were clear passes for all four answers:**
- **K1:** each answer adds `Cancel order` and `Order cancelled` within the Ordering BC.
- **K2:** each adds a `cancel-only-unpaid` invariant to the Decider's `rejects`.
- **K4:**
  - W: "Nobody edits the `.ttl` directly … not a tool: I am only a source of proposals."
  - X: "Everything is a decision … only a proposal."
  - Y: "Nobody edits the What … A tool is a source, never an author."
  - Z: "A decision, not a direct edit … only a proposal."
- **K5:** each answer says the signer needs an authoring scope covering the element kinds, delegated from the genesis grant.
- **K7:** each says new elements get a new `P/what/<ULID>` IRI. Each says the Order definition change is "a property change", so Order keeps its IRI (W and X: "same IRI"; Y: "identity is kept").

## Item 5 (things not understood or unsure about), classified

Type (i) means the item is about the documents' presentation or format. Type (ii) means it is about the content of the specification or the example.

Every type (i) item across the four answers is about a referenced document that is missing or a status note. No answer raised anything about markers, labels, ids, section references or tables in the documents themselves.

**W** (2 type i, 1 mixed, 11 type ii)
1. "Unpaid" does not exist in the model: "The definition says 'paid'…" (ii)
2. Is a field always its own decision: "'Adding a field is a decision of its own' is unclear on whether…" (ii)
3. The authority profile is missing: "`authority.md` (pull request #45) is not provided." This is about a missing document, though the unknowns it causes (the product owner's scope, how acceptance is recorded) are content. (i), mixed.
4. Decision record format: "neither the How vocabulary nor the protocol was given". (i), missing document.
5. Intent only shrinks: "Adding cancel there seems to need broader intent". (ii)
6. Subject coverage is ambiguous: "'Every pair of command and subject kind' could mean…" (ii)
7. The scenario passes the subject's claim like a payload field. (ii), about the example.
8. No meaning for the `present` state. (ii), about the example.
9. "Should cancelling also stop refunds?" (ii)
10. Content keys for actions. (ii)
11. "Decider logic is held only by digest. I could not see the actual logic." (i), missing file.
12. Smaller points:
    - Ordering between decisions: (ii).
    - Whether a system decision may point at a domain element: (ii).
    - "The element count of 44 matches the file": this is a confirmation, not a doubt. (i)

**X** (3 type i, 10 type ii)
1. Paid versus unpaid: "the request therefore conflicts with the current What". (ii)
2. Who pays, and through which channel. (ii)
3. Order identity on the wire: "No command carries an order id." (ii)
4. Subject claims inside `with`. (ii)
5. "May Staff cancel?" (ii)
6. Anchoring a mixed decision: "The rule in §2.1 only covers pure creation." (ii)
7. Dependencies and ordering between decisions. (ii)
8. The decision record's format and the authority profile: "not in these documents … does not exist yet (Q-4)". (i), mixed.
9. Who holds grants at Acme: "No principals or grants are named." (ii)
10. Flows: can a UI step be in more than one flow? (ii)
11. Content keys. (ii)
12. The test product: "The `.ttl` header says it is 'a test product only…'". (i), status note.
13. Undefined vocabulary: "`ontology.ttl`, `shapes.ttl`, `how.md` and `mint.py` are referenced but were not provided." (i)

**Y** (2 type i, 11 type ii)
1. Payment: "The documents never model an unpaid order." (ii)
2. One anchor or many: the anchor rule covers creation and change separately, "but not for a mix of the two". (ii)
3. "Adding a field is a decision of its own", including for a field of a new event. (ii)
4. Supersession: "`supersedes` is mentioned only as a protocol edge, without rules." (ii)
5. Order identity: "No command carries an order id." (ii)
6. Claim inside the command contradicts "never inside its `with`". (ii), about the example.
7. Subject coverage: "all subject kinds, or only those the Decider serves?" (ii)
8. Staff: "Should staff be able to cancel?" (ii)
9. `shop-api`: should cancellation appear there? (ii)
10. Content keys: "Does a `trigger-action` need its own content key?" (ii)
11. Authority profile: "not available (PR #45)". (i), mixed.
12. Test product: "The `.ttl` header says this is a test product". (i), status note.
13. Intent: "intent 'never grows'". (ii)

**Z** (2 type i, 9 type ii)
1. "Unpaid orders do not exist." (ii)
2. Force does not yet exist: the authority profile is "deferred (Q-4)", the `.ttl` says "nothing here is acceptable into a real product", and the document is "moved … not yet ratified". (i), status notes, mixed.
3. Decisions that both create and change: "The text gives a rule for each case, not for the mix." It also mentions "`DDD-dec-55`, which I did not have", but the doubt itself is about content. (ii)
4. Derived or authored: "a Decider's signature … is derived", "Yet the ttl asserts `handles`…" (ii)
5. Claim placement conflict in the example. (ii)
6. Scopes and fields: "`sdlc:Field` is one kind for attributes, payload fields, view fields and claims." (ii)
7. Wire changes: moving `paid_total`. (ii)
8. Missing Projector scenarios. (ii), about the example.
9. Content key role: "only 'heading' appears". (ii)
10. Flow membership. (ii)
11. Unknown references: "`what/shapes.ttl`, `what/ontology.ttl`, `how.md`, Writ's [D2] conjunction and the `dpp/1` record format. They were not in the folder." (i)

## Patterns across the four answers

All four answers raise the same content doubts: the What has no unpaid order, the example scenario puts the Customer claim inside the command's `with`, it is unclear how to anchor a decision that both creates and changes elements, and it is unclear whether staff may cancel.
