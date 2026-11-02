# The How, worked — three decisions, two targets each

<!-- ddd:doc
reader: developers running, reading or extending the worked example of the What and the How
act: run the checker, read what each record shows, and add a decision or a target without breaking the example
pin: v5.15.2
basis: [DDD-dec-62, DDD-dec-63, DDD-dec-64, DDD-dec-65, DDD-dec-66, DDD-dec-67, DDD-dec-68, DDD-dec-69, DDD-dec-70, DDD-dec-71]
status: current
supersedes: e5a332d:applications/sdlc/how-examples/README.md
-->

This folder is the worked example behind [`../how.md`](../how.md) and
[`../what.md`](../what.md). A test product, Acme Shop, imports three How decisions from a test
vendor's package. Each decision is evaluated against two systems built in different languages and
deployed on different clouds. Every record is a signed decision record, and a checker verifies the
lot.

Use it to see the How working end to end, to check a change you make to the How or the What, or to
copy the pattern for your own product.

**How settled this is.** Acme Shop is a test product. Its records are fixtures with throwaway
keys, and nothing here could be accepted into a real product. The checker shows that the
decisions execute as written. It does not show that the How is right.

## Run it

```
python3 applications/sdlc/how-examples/check.py      # needs rdflib for the verdict step
```

When last run, on 2026-11-02 with rdflib 7.6.0, it printed 112 ok or note lines, 1 expected
warning (the anchor self-test below) and 0 failures. All 38 records are conformant under the
reference implementation of the decision record protocol on `main`, run unmodified. Without rdflib, the anchor and verdict
steps are reported as **SKIP**, never as passed.

[`build.py`](build.py) builds the records. It makes fresh throwaway keys on every run. It refuses to
build if it would change a record that is already published, or if the protocol token on `main`
and the one this repository has decided on ever disagree.

## The cast

| Who | Identity | Holds |
|---|---|---|
| A test vendor (standing in for a package vendor such as Context&) | `mailto:holder@vendor.example` | the genesis grant over the package product `https://vendor.example/packages/ref-arch` |
| The importing product's founder | `mailto:holder@acme.example` | the genesis grant over the product `acme:product` |
| The importing product's architect | `mailto:architect@acme.example` | a grant of the How scope, delegated from that genesis |
| The importing product's owner | `mailto:owner@acme.example` | a grant of the What scope, delegated from that genesis (`GRANT-what@1`) |
| A proposing agent | `spiffe://acme.example/agent/proposer` | nothing: it may propose, it never accepts |

All four human keys are throwaway ed25519 keys for the test product's declared test holders. No
real key is ever used for a fixture or held by a session. Signatures are `ssh-sig` over the
record's canonical form, namespace `decision-provenance`.

## The three decisions, written once

Each decision is held once, in the package, and names no target in its statement or its violation
description. The checker verifies that no statement or violation text contains a target's name,
effect list, region list or native file kind.

| Kind | Package record | States | Anchored in the package | Imported as | Anchored in Acme Shop |
|---|---|---|---|---|---|
| constraint | `LAYER@1` | four ranked layers; no upward dependency; a component in no layer is a violation (no orphans) | the package product (its What is empty) | `IMP-layer@2` | the product node, `https://acme.example/products/shop`: the narrowest element covering both systems' code |
| binding | `PURE@1` | every Decider is realised, in each language target of each system using its domain, by an element whose component uses no effect | the package product | `IMP-pure@2` (proposed by the agent) | the Ordering bounded context |
| contract | `RESID@1` | every data store holding personal data is in an EU-jurisdiction region, as declared and as observed, read within a day | the package product | `IMP-resid@2` | the residency quality demand in the What |

A fourth, `REST@2`, is a binding: every Command is served at `POST /commands/{wire name}`. It shows
"specified once" a third time. It reads each Command's wire name, and is anchored at the Ordering
bounded context.

`RESID@1` requires both kinds of deployment fact, declared and observed. The other two read code
facts only.

The package's version 2 (`REL@2`) supersedes the layer rule with `LAYER@2`, which adds a `test`
layer. Acme Shop still rests on version 1. The checker shows that through the versions listing,
and shows that nothing in force changed.

## The What, as decisions

Acme Shop's What is itself held as decisions:

- `GRANT-what@1` gives the product owner the What scope.
- `WHAT-found@1` founds the What: all 44 elements of
  [`../what/examples/acme-shop.ttl`](../what/examples/acme-shop.ttl), anchored at the product node.
- `ACC-what@1` is the owner's acceptance of it.
- `what@3` is the What-version now in force. It supersedes `what@2`, which superseded `what@1`.
  All three name the same graph. Each later version names the vocabulary edition by the hash of the
  ontology and shapes as amended before edition 1 was tagged. `what@1`'s pin stays the hash of the
  files at `2c4f276`, and `what@2`'s the hash of the files at `655db92`.

## Two targets each

Acme Shop declares two systems. `shop-api` is realised in **C#** and deployed on **Azure**.
`shop-bff` is realised in **TypeScript** and deployed on **AWS** (`TGT-shop-api`,
`TGT-shop-bff`). Each decision is therefore evaluated in two targets.

The per-target shape lives only in the vocabulary edition records (`VOC-csharp@1`,
`VOC-typescript@1`, `VOC-azure@1`, `VOC-aws@1`). Adding the second language touched no decision.
It was one more edition record and one more target declaration. To add a third target, do the
same.

| Fact term the decisions read | C# (edition 1) | TypeScript (edition 1) |
|---|---|---|
| `sdlc:Component` | a `*.csproj` | a workspace package |
| `sdlc:inLayer` | `<Layer>domain</Layer>` in the project | `"sdlc": {"layer": "domain"}` in `package.json` |
| `sdlc:dependsOn` | `<ProjectReference>` | a dependency on another workspace package |
| `sdlc:realises` | `[Realises("…#decider-order")]` on a type | `/** @realises …#decider-order */` on an export |
| `sdlc:usesApi` + effect list | `System.DateTime.UtcNow`, `HttpClient`, … | `Date.now`, `node:http`, `fetch`, … |
| `sdlc:handlesRoute` | `app.MapPost("/commands/place-order", …)` | `server.post("/commands/place-order", …)` |

| Fact term | Azure (edition 1) | AWS (edition 1) |
|---|---|---|
| `sdlc:DataStore` | `Microsoft.Sql/servers/databases`, storage accounts, Cosmos DB | `aws_db_instance`, `aws_s3_bucket`, DynamoDB |
| `sdlc:inRegion` + jurisdiction | `westeurope` → EU, `eastus` → US | `eu-central-1` → EU, `us-east-1` → US |
| `deployment-declared` facts | Bicep at a commit | Terraform at a commit |
| `deployment-observed` facts | Resource Graph | Resource Explorer |

## The facts, and what is hand-written

No fact projector or reporter exists yet. Writ's code-facts specification is not written, and the
editions name their fact source as `"status": "not built"`. So the fact files under
[`facts/`](facts/) are hand-written: they are what an edition *would* emit.
[`facts/manifest.json`](facts/manifest.json) gives each one its provenance: projector or reporter;
the kind of fact (`file`, `deployment-declared` or `deployment-observed`); the edition, by pinned
hash; the subject (a repository at a commit, or a deployable unit); and when it was read. The
projector readings the checker uses are `facts/*.r2.ttl`, the same repositories at later commits
whose code cites the What's real identifiers.

Each fact file contains one planted defect:

| Planted | Decision | Expected | Got |
|---|---|---|---|
| `Acme.Ordering.Domain` references `Acme.Ordering.Infrastructure` | `LAYER`, C# | 1 violation | 1 |
| `@acme/scratch` has no layer | `LAYER`, TypeScript | 1 violation (no orphans) | 1 |
| `ordering-domain` calls `Date.now` | `PURE`, TypeScript | 1 violation | 1 |
| refund registered at `/command/refund-order` | `REST`, TypeScript | 1 violation | 1 |
| personal-data bucket in `us-east-1` | `RESID`, AWS, declared and observed | 1 each | 1 each |
| no observed deployment facts about the Azure unit | `RESID`, Azure, observed | **open question**: gap reported, absent reporter named as a candidate | open question |
| none | `LAYER`/`PURE`/`REST` C#, `RESID` Azure declared | 0 | 0 |

The expectations were written as the defects were planted, before the first run, and are in
[`expected.json`](expected.json). They are **analytic**, not evidence: a fixture built to fire,
fired. The run shows that the violation descriptions execute as written in both targets, that one
decision text serves both targets, and that a missing reading comes out as an open question, never
as a pass.

## What the checker checks

1. Every record is conformant under the reference implementation on `main`, **unmodified**.
2. Every reference reachable from `ACC-1@2`, `ACC-what@1`, `what@1` and `REL@3` (and, as history,
   from `ACC-1@1` and `REL@2`) names a record held here whose hash matches its pin. A test edit of
   one word in `LAYER@1` turns both lines red.
3. Every signature verifies over its record's canonical form.
4. The authority chain holds. The acceptance's signer holds a grant. That grant was signed by the
   genesis holder. The genesis is an origin. All three are signed, and the acceptor is a human, not
   an agent. This is a stand-in check for the authority profile, which the checker does not yet
   implement.
5. Exactly six How records are in force, all version 2: the ones `ACC-1@2` pins. `ACC-1@1` is
   superseded and puts nothing in force. No record in force names a provisional identifier. One
   What decision is in force, the founding `WHAT-found@1`. `what@1`'s graph hash and element list
   equal [`../what/vectors.json`](../what/vectors.json), and `../what/check.py` recomputes those
   from the graph.
6. Each imported decision can be expressed in each declared target: every fact term its violation
   description reads is mapped by that target's edition.
7. Supersession across the import is shown and changes nothing in force. There are four notes:
   `IMP-layer@2` on `LAYER@1` and `REL@1`; `IMP-pure@2` and `IMP-resid@2` on `REL@1`.
8. Each import's anchor is the narrowest element covering what it governs today. Otherwise the
   checker prints a warning, which is not a failure. A self-test re-anchors `PURE` at the product
   and expects the warning. Anchoring an "every Decider" rule at the product is legitimate, so the
   warning is advisory.
9. The verdicts, per decision and per target, equal `expected.json`.

## Two versions of the records

The records exist in two versions. Version 1 was written before the What's identity form existed,
against provisional identifiers, and was accepted on the condition that each record would be
superseded against the real identifiers, never edited. Version 2 does that:

- Every version 1 record that anchors to or names a What element has a version 2 that supersedes
  it: `GEN`, `GRANT-how`, both `TGT-*`, all four `IMP-*` and `ACC-1`. So does the vendor's `REST`,
  which read a provisional local id. A new package version, `REL@3`, ships it.
- No version 1 record changed. Their pins still hold, and are still checked, as history.
- [`what/acme-shop.ttl`](what/acme-shop.ttl) in this folder is the provisional What graph, kept as
  history and no longer read. The `facts/*.ttl` readings without `r2` are kept the same way.

| Provisional (version 1) | Real (version 2) |
|---|---|
| `…/shop/what#product` | `https://acme.example/products/shop`, the product IRI and product node |
| `…/what#domain-ordering` (the `PURE`, `REST` anchor) | the Ordering bounded context, `…/what/01M610JNAMH5Y3FP9BFRZJ6QSS`. Deciders and Commands sit in the domain's one bounded context, which is the narrowest element covering them |
| `…/what#system-shop-api`, `#system-shop-bff` | `…/what/01M610JNAMV23W7Y9YQKZPJ4ZA`, `…/what/01M610JNAM8K9PG653537FE7EG` |
| `…/what#qd-residency-eu` | `…/what/01M610JNAMGQQ2DJENWGA6MWCK` |
| `…/what#decider-order`, `#command-*` (in the code's citations) | `…/what/01M610JNAMMP5V59XRNHD39R5A`, `…/what/01M610JNAMCQ2R6MG31Q07DWMX`, `…/what/01M610JNAMC74SDA3DVDE332WB` |

## Where this comes from

| Section | Rests on |
|---|---|
| Records are `dpp/1` records, pinned by the protocol's hash law | `DDD-dec-62` (token `dpp/1`, superseding `DDD-dec-53`); `spec/decision-provenance/` |
| The three kinds; anchoring; targets; import | `DDD-dec-65` to `DDD-dec-71`, superseding `DDD-dec-55` to `DDD-dec-61` on the same terms |
| Narrowest anchor; the advisory warning | Ruling 1 of 2026-10-28 (the How session, `meta/sessions/2026-10-27-product-framework-how/`) |
| Version 2 supersedes version 1, never edited | Ruling 4 of 2026-10-28 |
| The What as decisions; What-versions | `DDD-dec-63` §6; `DDD-dec-64` (Round 5, `what@3`) |
| `REST@2` reads the wire name | `DDD-dec-64`, P-1 ("REST@2 stands") |
| Throwaway keys; no real key held by a session | Round 3, ruling 1 of 2026-10-28 |
| The `decprov/1` set the records replaced | Never conformant to any protocol on `main`; kept in history at `d11df86` |

The earlier text of this page is at `e5a332d`. It repeated its paragraph on `what@2` twice; the
facts are stated once here.
