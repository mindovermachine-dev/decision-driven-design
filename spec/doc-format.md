# Document format

<!-- ddd:doc
reader: people and agents writing or changing a document outside canon in this repository
act: give a document the opener and shape its folder requires
pin: v5.15.2
basis: [DDD-dec-94, DDD-dec-95, DDD-agent-01]
status: current
supersedes: df9d05b:spec/doc-format.md
-->

Use this when you write or change a document anywhere outside canon. It says how a document
opens, what it records about its own basis, and how it treats status in its prose.

**The principle.** Only canon carries authority. Canon is the principle repository's `core/` and
this repository's `core/`. Every other folder exists for a named reader doing a named act. A
document there is ground for that act, and its shape follows from what that reader needs.

A document outside canon may explain, apply, teach or record canon. It may not be the only place a
result lives. A result that lives only outside canon is **held**, and says so.

## The opener — `ddd:doc`

A document opens with an HTML comment block directly under its title. It renders as nothing.

```
<!-- ddd:doc
reader: architects, developers and product owners specifying a software product
act: write a product's What, change it, and hand it to the people who build from it
pin: v5.15.2
basis: [DDD-dec-42, DDD-ground-06, DDD-address-01@projected]
status: current
supersedes: e5a332d:applications/sdlc/what.md
-->
```

| Field | Required | Meaning |
|---|---|---|
| `reader` | yes | Who the document is for. A role, not a person, unless the reader is the principal |
| `act` | yes | What they can do after reading it that they could not do before |
| `pin` | yes, unless `historical` | The upstream tag the document was written against |
| `basis` | yes; may be `[]` | What the document rests on: an upstream claim or term id pinned in `graph/upstream.yaml`; a local claim or term with the status it was read at, as `DDD-address-01@projected`; a local decision id; or a held result, `held:<session-dir>/<item-id>` |
| `status` | yes | `draft`, `current`, `held` or `historical` |
| `supersedes` | no | `<commit>:<path>` of the text this document replaced in place |

| `status` | Means |
|---|---|
| `draft` | Not yet accepted |
| `current` | Accepted, and every basis entry is canon or a decision |
| `held` | Accepted, but rests on at least one result not yet in canon; at least one `held:` entry |
| `historical` | Kept as a record; no live reader acts on it |

A reformatted document replaces its old text in place. The old text stays reachable through
`supersedes`, so nothing is lost.

## Status in running text

Say status in words the reader can use. Keep claim, term, decision and promotion ids out of the
prose; they belong in the `ddd:doc` block and the document's closing basis table.

- Decided is the default, and goes unmarked.
- Mark an unsettled point where it arises, in words: *(not settled yet)*. List it again, with
  what it would change if decided, in a "Not settled yet" section near the end.
- Say how settled the document is as a whole in its opening, for example "decided, and not yet
  tried on a real product".

Where a rule rests on a **projected** claim, an invisible `ddd:ref` marker may sit at the point of
use, so the pin check warns when the claim moves. Decisions get no marker.

## Folder formats

A folder may set a narrower format in its `README.md`. The one set so far is `applications/`
(`DDD-dec-95`): every document closes with "Where this comes from", reference material goes to its
own document, and deliberation stays in the session record.

## The check — not yet ported

The 2026-10-26 session built a warning-level check for these blocks (W8 to W15) against the old
history's validator. It has not been ported to `scripts/`. Until it is, the opener is a convention
that nothing enforces. Porting it is a successor item of
`meta/sessions/2026-11-02-applications-for-readers/`.

## Where this comes from

| Section | Rests on |
|---|---|
| The principle | `DDD-dec-94` (2026-10-26 pre-session ruling 1 and Gate 1 ruling 1, re-filed) |
| The opener | `DDD-dec-94` (pre-session ruling 2; Gate 1 rulings 3 and 4; Gate 2 ruling 1) |
| Status in running text | `DDD-dec-94` (the 2026-10-26 pilot's amendment); `DDD-dec-95` (the `ddd:ref` amendment) |
| Folder formats | `DDD-dec-95` |
| The check | `DDD-dec-94`, "Not re-filed" |

Ported from branch `claude/doc-format` at `df9d05b`, where the original carried the 2026-10-26
session's full text, including the check.
