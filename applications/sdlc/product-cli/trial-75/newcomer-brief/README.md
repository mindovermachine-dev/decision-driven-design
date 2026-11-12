# Fifth run: a brief for the reader Emil has in mind

With a reader who wants to know what the product is and how it works, the brief stopped framing the product as promises and refusals and dropped its history. What still differs from what Emil expects now traces to the canon.

## What Emil expected

On reading the brief written for an authoriser, Emil said he would expect it to say that Product is a deterministic specification of what a software system does, that it tracks all decisions per change to the product, and that it exposes this to other systems. He does not care that it is rewritten. He wants it to say what it is and how it works.

## What changed

- A new reader's description, `audiences/newcomer.md`, in those terms.
- `formats/brief.md` (version 7): the summary says first what the subject is, then how it works, and the brief does not tell the subject's history.
- The canon was not changed.

The weights moved accordingly: the surface chapter rose from 40 words to 60, the formats chapter from 0 to 40, and the guarantees fell from 60 to 20.

## Results against predictions

The predictions were recorded on issue #75 before the run.

| Prediction | Result |
|---|---|
| 1. The opening no longer says the product is rewritten or what it replaces. | **Held.** |
| 2. The opening says that every change is a decision, tracked. | **Failed.** The opening says an agent proposes and the author adopts or rejects. That every step is a decision is said one paragraph later. |
| 3. The opening still does not say "deterministic specification of what a software system does". | **Held.** The canon's promise does not say it. |
| 4. The check finds at most one sentence the cited sections do not support. | **Held.** 15 sentences and 12 explanations: 26 supported, 1 partly, none unsupported. |

The falsifier did not fire: the framing as promises and refusals is gone, so the reader's description was its cause.

## What still differs from Emil's expectation, and where it comes from

| Emil expects | The brief says | The canon |
|---|---|---|
| The name "Product" | "product-cli" | The title says "Product". The introduction says "product-cli". |
| "A deterministic specification of what a software system does" | "A machine-checkable statement of what a product does" | The promise uses those words. Determinism is stated in chapter 4 and one guarantee, not in the promise. |
| "Tracks all decisions per change", up front | Said in the second paragraph, not the first | Stated in the promise, as the first of four consequences. |
| "Exposes it to other systems" | Not said | Stated in chapter 4 and one guarantee, as a property of the draft log. Not in the promise. |

## One sentence to correct

The check marked one sentence as partly supported. The opening says "An agent proposes each step in conversation". The canon says every step is a decision, and that the author may also write directly, with no proposal. The sentence was left as the model wrote it; a projection is not edited by hand.

---

*Trial material; nothing here is ruled. Run on 2026-11-12. The brief written for an authoriser is kept in `../weighted-brief/`. Both briefs would be named `product-definition.en.brief.md`: the file name has no place for the reader, and that is not settled.*
