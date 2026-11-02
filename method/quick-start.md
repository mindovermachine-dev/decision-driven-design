# Quick start — step 1 on Varve's HTTP slice

This page runs [step 1, map and index acts](01-map-and-index-acts.md), on one small system you can
start on your own machine: the HTTP part of [Varve](https://github.com/Hafeok/varve)'s own quick
start, at its release tag **`v0.1.0-preview.15`** (`DDD-dec-77`).

> **What this example is, and is not.**
>
> - **Varve is the subject of design, not a dependency.** Nothing in Decision-Driven Design needs
>   Varve. It is simply a real system with a short, public quick start to practise on.
> - **This is exposition, not evidence.** Claude wrote the example inside the framework. It shows
>   how the step is done. It shows nothing about whether the step works. The claims under step 1
>   stay **projected** until the first independent application case (T2b) has run.
> - **The commands were not run while writing this page.** The session that wrote it had neither
>   .NET nor Docker. Every command is copied verbatim from Varve's README at the tag.

**Weakest point.** The ground axes in §3 are Claude's choice for exposition. A different choice
gives a different map, and step 1 cannot tell you which axes you missed (`DDD-ground-06`: an
address is blind to axes nobody declared). Treat the axes as a worked guess to argue with.

## 1. Start Varve

Follow Varve's README at the tag. You need either the .NET 10 runtime or Docker:

```bash
dotnet tool install --global Varve.Server --prerelease
docker pull ghcr.io/hafeok/varve:v0.1.0-preview.15
```

```bash
varve serve --anonymous --datasets-root "$PWD/data"
```

Then declare the dataset `people`, as Varve's README shows. Starting the server and declaring the
dataset are set-up, outside the slice. They are not mapped below.

## 2. The request, and the slice

Varve's README states the request in one line: "Then write, read, go back, and read the history".
The slice is the five HTTP operations that carry it out, in the README's order:

```bash
curl -X POST http://localhost:5000/datasets/people/sparql \
  -H 'Content-Type: application/sparql-update' \
  --data 'INSERT DATA { <http://example.org/ada> <http://xmlns.com/foaf/0.1/name> "Ada Lovelace" }'
curl -X POST http://localhost:5000/datasets/people/sparql \
  -H 'Content-Type: application/sparql-update' \
  --data 'DELETE DATA { <http://example.org/ada> <http://xmlns.com/foaf/0.1/name> "Ada Lovelace" }'
curl -G http://localhost:5000/datasets/people/sparql \
  -H 'Accept: application/sparql-results+json' \
  --data-urlencode 'query=SELECT ?name WHERE { ?person <http://xmlns.com/foaf/0.1/name> ?name }'
curl -G http://localhost:5000/datasets/people/sparql \
  -H 'Accept: application/sparql-results+json' -H 'Varve-As-Of: position:1' \
  --data-urlencode 'query=SELECT ?name WHERE { ?person <http://xmlns.com/foaf/0.1/name> ?name }'
curl 'http://localhost:5000/datasets/people/commits?to=2'
```

You do not need to read RDF or SPARQL to follow this. Each line is an HTTP request: write a name,
delete it, read the names now, read them as the first commit left them, and list both commits.

## 3. Declare the ground axes first

Step 1 maps **forward from the request**, never back from Varve's code. Before any act gets a
position, declare the axes the positions are read on. These axes are Claude's, for exposition:

| Axis | Values in this slice | Why it is an axis |
|---|---|---|
| Dataset | `people` | Every act reads and changes one dataset's state |
| Change requested | `insert`, `delete`, `none` | A decision that governs deletes alone must be able to tell a delete from a write |
| State read | `head`, `position 1`, `positions 1–2` | The as-of read and the commit feed read a named point or range of the log, not the latest state |

The **layer path** is the chain of composite acts each act sits within. Here every act sits in one
composite act, "keep the people dataset", with two parts: *change it* and *read it*.

## 4. The act map

Each row is one act occurrence. The **address** is its position on the three axes plus its layer
path. **The actor is not in the address.** Whether you, a script or an agent runs the `curl`, the
address is the same, which is what lets different actors at one address be compared later.

| Occurrence | What it does | Address: dataset · change · state read | Layer path |
|---|---|---|---|
| o1 | Write Ada's name | people · insert · head | keep people ▸ change it |
| o2 | Delete Ada's name | people · delete · head | keep people ▸ change it |
| o3 | Read the names now | people · none · head | keep people ▸ read it |
| o4 | Read the names as commit 1 left them | people · none · position 1 | keep people ▸ read it |
| o5 | List the commits | people · none · positions 1–2 | keep people ▸ read it |

**The time index is causal, not wall-clock** (`DDD-address-01`). B comes after A when a state
change that A produced is in B's ground reading:

| Occurrence | Depends on | Because its ground reading contains |
|---|---|---|
| o1 | — | — |
| o2 | o1 | the name o1 wrote, which is what o2 deletes |
| o3 | o2 (and o1) | the state after o2: no rows |
| o4 | o1 **only** | the state at position 1: "Ada Lovelace". o2's change is not in it |
| o5 | o1 and o2 | both commits |

o4 runs after o2 by the clock, but it does not depend on o2. In causal order the two are
concurrent. That is the difference between the time index and a timestamp. If you run o3 again
tomorrow, the new occurrence has o3's address and is told apart from it only by the time index:
two occurrences at one address, which is what behaviour is later read over (`DDD-address-05`).

## 5. What you can see now that you could not before

The value of step 1 is that **decisions and actors get a place to be anchored** (step 1's card).
Two decisions Varve's README states, placed on the map. This is Claude's reading of the README,
for exposition:

| Decision, as Varve's README states it | Where it anchors | Applicability, over the axes (`DDD-ground-01`) |
|---|---|---|
| "`--anonymous` is for development only: a real deployment takes OIDC bearer tokens" | The composite act "keep people", above all five | every occurrence, wherever the deployment is not development |
| An as-of read names a log position (`Varve-As-Of: position:1`) | o4 | state read = a named position |

Each decision's applicability is computed from the address alone, without running the act. That is
step 1's exit check: every occurrence has exactly one address, and its governing set can be
computed from the address, its ground readings and the decisions' predicates
(`DDD-ground-06`).

## 6. The falsifier: the junior-engineer test

This example is falsified by the **junior-engineer test**. A junior engineer, at first contact,
with only this page and Varve's README at `v0.1.0-preview.15`, performs step 1 on this slice. **It
fails if they cannot name the value the step gave them.** This is the method draft's default
falsifier for a step, together with its instruction to test steps against a junior engineer's
first contact. Both are `[PROPOSED]`
([`method-instructions-draft.md`](../meta/sessions/2026-09-27-act-address/method-instructions-draft.md)).

**Running it is Emil's act**, and it has not been run. Passing it would show that the page
teaches the step. It would not move step 1's claims from projected; only T2b can do that.

If you try this and want to tell us what happened, open an issue with the field-report template.
