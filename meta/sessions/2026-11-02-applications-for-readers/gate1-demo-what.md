# The What — writing down what your software is and does

<!-- ddd:doc
reader: architects, developers and product owners specifying a software product
act: write a product's What, change it, and hand it to the people and agents who build from it
pin: v5.15.2
basis: [DDD-dec-41, DDD-dec-42, DDD-dec-43, DDD-dec-44, DDD-dec-45, DDD-dec-46, DDD-dec-51, DDD-dec-52, DDD-dec-55, DDD-dec-57, DDD-dec-63, DDD-dec-64, DDD-dec-73]
status: draft
supersedes: e5a332d:applications/sdlc/what.md
-->

> **Gate 1 demonstration.** This is the proposed format applied to the opening of `what.md`:
> its first two sections and the start of the third. It is `[PROPOSED]` and changes no rule.
> The "Where this comes from" table at the end shows where the decision trail goes.

Use this when you are about to build, change or take over a piece of software, and you need one
place that says what it is and does before anyone decides how to build it.

After reading it you can:
- write down a product's What: its domains, its systems, and the behaviour and screens they carry;
- change the What, and know who may make each change and when it comes into force;
- hand the What to the people and agents who build from it, and check what they build against it.

**How settled this is.** Everything here is decided, and none of it has yet been tried on a real
product beyond the worked example. Try it; do not rely on it yet. The few points that are not
settled are marked *(not settled yet)* where they come up, and listed at the end.

**The worked example** is a small web shop, Acme Shop. Customers place orders and staff refund
them. You can read the whole of its What in
[`what/examples/acme-shop.ttl`](what/examples/acme-shop.ttl), and every example below comes from
it.

---

## What a What is

A What describes what a piece of software is and does, in the language of the people who own it.
It says nothing about how the software is built: which language, which framework, which cloud.
That is the How, and it is written against the What afterwards ([`how.md`](how.md)).

Three things make a What more than a requirements document:

1. **It is one connected graph, not a set of pages.** Every part has a stable identity and
   explicit links to the parts it depends on. "Describe this system" is a query, and "what does
   this change touch?" is a walk along the links.
2. **It changes only by signed decisions.** Nobody edits the What. Every change is a short
   record, signed by a person with the right to make that change. So at any moment you can ask
   what the software should do, and who decided each part of it.
3. **It is what the software is checked against.** The What's rules for behaviour are executable,
   so an implementation's behaviour can be checked against them over a defined wire, in any
   language. It is not checked against what someone remembers the What to be. (Checking production
   data against the What is possible too, but it is an add-on, not part of this framework.)

In this framework's own terms, the What is the software's declared ground and its tolerance. It is
what every act in the software reads, and the bar each act must meet. Step 1 of the method reads
its map of acts off the What instead of inventing one ([`../../method/`](../../method/)).

---

## Changing the What

### Every change is a decision

You never edit the What directly. To change it, you write a decision: a record that says what
changes, and points at the part of the What it changes. That part is its **anchor**.

A decision is not itself part of the What. It sits beside the What, attached to its anchor. The
current form of any part of the What is the result of the decisions anchored to it, so the What's
history is its decision history.

*In Acme Shop:* the whole What, 44 elements, arrived in one founding decision, and the product owner
signed a second record accepting it. The rule "a refund cannot exceed what was paid" came in with
that founding decision. If someone later loosened the rule, that would be a new decision anchored
to the `Order` entity. The founding decision would stay on record.

### Adding something new

Something you are about to create does not exist yet, so it cannot be the anchor of the decision
that creates it. Anchor that decision to the **narrowest part that already exists and contains
everything you are adding**.

*In Acme Shop:* if you added a `Cancel order` command, its decision would anchor to the `Ordering`
domain. A whole new `Shipping` domain would anchor to the product itself. So did the founding
decision, which created `Ordering`. Anchoring to the product is the normal case for a new domain,
not a loophole.

### Gathering what already exists elsewhere

Parts of a What usually exist already: in a Figma file, an Event Modeling board, an old database
schema, a Jira board. You can gather them from there. What you gather is a **proposal**. It enters
the What only when a person who holds the right to change that part signs and accepts it. Tools
supply material; they never change the What themselves.

Who holds which right, and how a signature brings a decision into force, is the authority profile
([`authority.md`](authority.md), which lands with pull request #45). The short version is this. Every product has one founding grant,
held by the person who brought the product into being. Every other right over the product is
delegated from that grant, directly or through others.

---

## How the What is organised

A product owns **domains** and **systems**:

- A **domain** owns meaning and rules: what an `Order` is, that a refund cannot exceed what was
  paid, which events an order emits.
- A **system** owns a surface and its journeys: which screens exist, how you move between them,
  and which platform it runs on.

A system uses whole domains; it never owns one. When you are unsure where something belongs, ask:
**would two systems disagree about it?** If they must agree, it belongs in the domain. If they may
differ, it belongs in the system. A refund is a refund in the customer app and in the staff tool,
so refund rules live in the domain. The two apps navigate differently, so navigation lives in each
system.

*In Acme Shop:* the product owns one domain, `Ordering`, and two systems, `shop-api` and
`shop-bff`. Both systems use `Ordering`, so both enforce the same refund rule without restating it.

The product node itself carries little: a name, a purpose, and the things that span the whole
product. Those are product-wide quality demands, journeys that cross systems, and targets that
serve every system, such as a shared design system. A second product is a separate product with
its own founding grant. It may use a domain from this one across a declared boundary, but it never
absorbs it.

*(The rest of `what.md` continues in this format: domains, behaviour, screens, who may act,
quality demands, the targets the What declares, and authoring scopes. Identity, version hashes, the
conformance wire and the encoding move to a reference document for tool builders.)*

---

## Not settled yet

*(In the full document, each open point is listed here in plain words, with what it would change
if decided.)*

## Where this comes from

For reviewers and auditors. The decisions are in [`core/decisions/`](../../core/decisions/), and
the sessions that made them are in [`meta/sessions/`](../../meta/sessions/).

| Section | Rests on |
|---|---|
| What a What is | `DDD-dec-41` (the opinionated What; a system is ground and tolerance), `DDD-dec-42` (only the What moved), `DDD-dec-51` (one graph, stable identity, one conformance level) |
| Every change is a decision | `DDD-dec-42` (decisions anchor to What elements; every change is a decision), `DDD-dec-55` |
| Adding something new | `DDD-dec-63` §8 (Round 6: the narrowest existing element) |
| Gathering what already exists | `DDD-dec-43` (tools never change the What; a human principal signs) |
| The founding grant | `DDD-dec-46` (the genesis grant), `DDD-dec-47` (the authority profile) |
| How the What is organised | `DDD-dec-64` P-2 (one containment edge); Product Framework v1.10.0 §3, §3.0 |

The text adapts the Product Framework, github.com/Hafeok/product-framework, v1.10.0 at `c895652`
and v1.11.0 at `55c9281`. The full record of the move, including where every source section went,
is the earlier text of this file at `e5a332d` and the session
`meta/sessions/2026-10-28-product-framework-what-move/`.
