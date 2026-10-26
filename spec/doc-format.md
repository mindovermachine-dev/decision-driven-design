# Document format specification

<!-- ddd:doc
reader: validator authors, and agents and people writing a document in this repository
act: give a new or changed document the opener its folder requires
pin: v5.15.1
basis: [DDD-agent-01, DDD-dec-39]
status: draft
-->

**Every document in this repository is written for a named reader doing a named act, and opens by saying so.** This file defines how. It is the schema; each folder's `README.md` holds the instance, its charter.

> **[PROPOSED] — 2026-10-26, doc format session, GATE 2 (`DDD-dec-39`).** Nothing here is in force until Emil accepts the session's PR.

## 1. The principle

Ruled before the session opened and refined at its GATE 1:

> **Only canon carries authority. Canon is upstream `core/` and this repository's `core/`. Every other folder exists for a named reader doing a named act. A document there is ground for that act, and its format follows from what that reader needs.**

"Authority" here means authority over what the framework holds true. A document outside canon may explain, apply, teach or record canon. It may not be the only place a result lives. A result that lives only outside canon is **held**, and must say so (§4).

Format rules, such as this file, are not canon either. Their force comes from the decision that ruled them.

## 2. Scope

| Documents | Opener | Checked for `ddd:doc` |
|---|---|---|
| Canon: everything under `core/` | `ddd:contract` (`core/NN-*.md`), or the claim and decision formats (`spec/claim-format.md`) | No. Canon has its own checks. |
| A folder `README.md` that carries a `ddd:charter` block | The charter (§3) | No. The README *is* the charter. |
| Documents in a folder whose charter sets `opener: convention:<path>` | The convention at that path | No. `meta/sessions/` is the case. |
| Files a charter lists under `exempt` | Their own fixed format | No. `LICENSE.md`, `CHANGELOG.md` and `CLAUDE.md` are the cases. |
| Paths under a directory whose name starts with `.` | Tool configuration | No. |
| **Every other Markdown document** | **`ddd:doc` (§4)** | **Yes** |

A README without a `ddd:charter` block is an ordinary document. It needs `ddd:doc`.

## 3. The folder charter — `ddd:charter`

A folder's `README.md` opens with its charter, directly under the title:

```
<!-- ddd:charter
reader: implementers building tooling or a harness on the framework
act: build a mechanism the canon licenses
opener: ddd:doc
authority: none
exempt: []
-->
```

| Field | Required | Values |
|---|---|---|
| `reader` | yes | Who reads this folder's documents. A role, not a person, except where the reader is the principal. |
| `act` | yes | What the reader is doing when they read one. A verb phrase. |
| `opener` | yes | `ddd:contract` (canon), `ddd:doc`, or `convention:<path>` (a folder-specific convention, defined at that path) |
| `authority` | yes | `canon` or `none` |
| `exempt` | no | File names in this folder that keep a fixed format of their own |

**Inheritance.** A document is governed by the nearest charter at or above its folder. A subfolder needs its own charter only when its reader or act differs.

Below the block, the README says the same in prose for a human arriving in the folder: who this folder is for, what they can do with it, and what it does not carry.

## 4. The document opener — `ddd:doc`

A governed document opens with its block, directly under the title:

```
<!-- ddd:doc
reader: implementer of a local-agent harness
act: bind a toolset to a task
pin: v5.15.1
basis: [DDD-floor-01, term:floor, held:2026-10-26-doc-format/P-3]
status: held
supersedes: baec167:apparatus/tool-contract.md
-->
```

| Field | Required | Meaning |
|---|---|---|
| `reader` | yes | Who this document is for. Narrower than the folder's reader, or the same. |
| `act` | yes | What they can do after reading it that they could not do before. |
| `pin` | yes, unless `status: historical` | The upstream tag the document was written against. |
| `basis` | yes; may be `[]` | What the document rests on. Each entry is one of: an upstream claim or term ID pinned in `graph/upstream.yaml`; a local claim or term, written with the status it was read at, as `DDD-cost-04@projected`; a local decision ID; or a held result, `held:<session-dir>/<item-id>`. |
| `status` | yes | `draft`, `current`, `held` or `historical` (below) |
| `supersedes` | no | `<commit>:<path>` of the text this document replaced in place. |

| `status` | Means | Must hold |
|---|---|---|
| `draft` | `[PROPOSED]` content; not yet accepted | — |
| `current` | Accepted, and every basis entry is canon | No `held:` entry in `basis` |
| `held` | Accepted, but rests on at least one result not yet in canon | At least one `held:` entry in `basis` |
| `historical` | Kept as a record. No live reader acts on it. | `pin` may be omitted |

**Below the block**, before the body, the document says in prose who it is for, what they will be able to do, and what it rests on. A basis entry that is projected or held is flagged where it is used, not only in the block. This is the status floor rule of `projections/tracks/README.md`, applied to every folder.

## 5. The check

`validate-core-order.py` checks every governed document. All findings, W8 to W15, are **warnings**. A move to errors is a later ruling, after roll-out.

| Code | Fires when |
|---|---|
| W8 | A governed document has no `ddd:doc` block. |
| W9 | The block is malformed: a required field is missing or empty; `status` is not a registered value; `current` with a `held:` basis; `held` without one. |
| W10 | A `basis` entry resolves nowhere: it is not pinned upstream and not a local claim, decision or term. An upstream *decision* fires this too, because decisions cannot yet be pinned (successor item S-8 of `2026-09-27-act-address-landing`). |
| W11 | **The document rests on a moved basis.** Either a `basis` entry is pinned upstream and its pin fires W5 (status moved) or W6 (content moved) at the ref, or it is local canon written `ID@status` and the claim or term file now holds a different status. |
| W12 | The document's `pin` is not the repository's pin. |
| W13 | A `basis` entry is `held:`. The warning names the held item, or says that no such item exists in that session's directory. |
| W14 | No `ddd:charter` governs the document's folder. |
| W15 | A `basis` entry names a local claim or term without `@status`, so W11 cannot see it move. |

**Why local entries carry a status (GATE 2 ruling 1).** Upstream pins record a status and a content hash, so W11 sees an upstream basis move. Local canon records neither. `@status` gives a local entry the status half of a pin. Local *content* movement while the status holds (the W6 case) is not covered; it would need a hash per entry. Local decisions carry no status, and need no `@`.

**W11 is what the opener adds over `ddd:ref`.** A `ddd:ref` marks a citation. W11 says which documents *rest* on a basis that moved. Pre-session ruling 2's falsifier tests exactly this: if, after roll-out, W11 stays silent on a document whose basis claim moved, the opener adds nothing and should become prose only.

## 6. Writing a new document

1. Find the charter governing the folder. If none fits, the document is in the wrong folder, or the folder needs a charter first.
2. Name the reader and the act. If you cannot name the act, the document has no reason to exist yet.
3. List the basis. If a result you need is not in canon, either cite the promotion that holds it or write the claim first.
4. Set the status. Write the prose intro. Flag every projected or held basis where it is used.
5. Run `python3 validate-core-order.py core/` and read the W8–W15 lines for your file.
