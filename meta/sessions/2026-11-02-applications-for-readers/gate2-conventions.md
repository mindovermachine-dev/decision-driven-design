# Gate 2 — conventions for the rewrite

The working rules every Gate 2 rewrite follows, so the documents read as one set. They apply the
ruled format (`DDD-dec-95`, F1–F8) and `spec/doc-format.md`. They add no rule of their own.

## Shape of every document

```
# <Title naming the reader's task>

<!-- ddd:doc
reader: ...
act: ...
pin: v5.15.2
basis: [ ... ]
status: current            # or held / draft, per spec/doc-format.md
supersedes: e5a332d:<path> # the text this replaces
-->

<One line linking the other half, for split documents.>

<Two to four sentences: who uses this, what they can do after reading it.>

**How settled this is.** <One or two sentences, in words.>

<Body, in the order of the reader's task. Examples from Acme Shop, set as *In Acme Shop:* ...>

## Not settled yet
<Each open point in plain words: the question, and what deciding it would change.>

## Where this comes from
<Table: section -> decisions and claims. Then source attribution and the supersedes pointer.>
```

## Words

| Instead of | Write |
|---|---|
| `Ruled (DDD-dec-NN)` | nothing: decided is the default |
| `[PROPOSED]`, `[OPEN]` | *(not settled yet)* at the point, and an entry in "Not settled yet" |
| `UNVERIFIED — Emil review` | *(not settled yet)*, and say in the entry that it is a reading not yet confirmed |
| `PF §3.1`, "the old §4.2" | nothing in the body; the source goes in "Where this comes from" |
| Session paths, round numbers, gate numbers | nothing in the body |
| Quoted Product Framework text | the same rule in plain statements; quote only a short test the reader applies verbatim |
| "the genesis grant" | "the product's founding grant (its genesis grant)" at first use, then "the genesis grant" |
| `P/what/<ULID>`, hash laws, wire messages, RDF terms | the reference document; the practitioner document links to it |

Settledness in the opening, for documents on `main` whose rules are decided:
"Everything here is decided, except the points marked *(not settled yet)*. None of it has yet
been tried on a real product beyond the worked example, so try it before you rely on it."

## The worked example

Acme Shop, `applications/sdlc/what/examples/acme-shop.ttl`, with its decision records under
`applications/sdlc/how-examples/records/acme/`. Every statement about the example is checked
against those files before it is written. Facts verified so far:

- One domain, `Ordering`; two systems, `shop-api` and `shop-bff`.
- Entity `Order` with fields `customer_id`, `paid_total`, `refunded_total`.
- Commands `Place order` and `Refund order`; events `Order placed` and `Order refunded`; view
  `Order summary`.
- Invariants include "refund within paid" and "order has lines"; scenario "refund beyond what was
  paid".
- Subject kinds `Customer` and `Staff`; scope rules "customers see their own orders" and "staff
  see every order".
- The whole What (44 elements) arrived in one founding decision, `WHAT-found`, anchored to the
  product, accepted by `ACC-what`. Nothing in the example was added by a later What decision.

A hypothetical extension of the example is written as one ("if you added ..."), never as fact.

## Content does not change (F8)

- Every rule in the old text appears in the new pair, with the same meaning and the same strength
  (MUST stays must; "may" stays may).
- A point the old text marks `[PROPOSED]`, `[OPEN]` or `UNVERIFIED` stays unsettled in the new
  text, whatever its history. It is not upgraded to decided, and not downgraded either.
- A rule stated only inside a deliberative passage is extracted into the body, and the equivalence
  table says so.
- A rule that cannot be restated without changing it is left as close to the old wording as
  possible and reported in the equivalence table under "Could not restate".

## The equivalence table

One file per old document: `meta/sessions/2026-11-02-applications-for-readers/equivalence/<name>.md`.

| # | Old: section and rule, in brief | New: document and section | Note |
|---|---|---|---|

Notes use one of: `same`; `extracted from deliberation`; `moved to reference`; `removed:
deliberation` (with the old section); `removed: history` (with the old section); `could not
restate` (with why). Every normative sentence of the old text gets a row. Deliberation and history
may be grouped one row per section.
