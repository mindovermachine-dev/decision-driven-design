# The How, worked — three decisions, two targets each

Companion to [`../how.md`](../how.md) §12. Every record is a `dpp/1` record (the token
`DDD-dec-62` rules, superseding `DDD-dec-53`), pinned by the hash law of `spec/decision-provenance/`. It was built by
[`build.py`](build.py) and is checked by [`check.py`](check.py).

**Superseded against the landed What (2026-10-28).** Ruling 4 of 2026-10-28 accepted the
version 1 records provisionally: they anchored to What identifiers fixed before the identity form
existed, and each was to be "superseded by a version against the real identifiers, never edited".
The What has landed ([`../what.md`](../what.md)) in the ruled identity form (`DDD-dec-63`), so:

- **Version 2 records.** Every version 1 record that anchors to a What element or names one now
  has a version 2 that supersedes it: `GEN`, `GRANT-how`, both `TGT-*`, all four `IMP-*` and
  `ACC-1`. So does the vendor's `REST`, which read the provisional `sdlc:localId`. A new package
  version, `REL@3`, ships it.
- **Nothing edited.** No version 1 record changed: `build.py` loads each published version and
  refuses to build if it would change one.
- **The landed What.** The What graph the checker reads is the landed example,
  [`../what/examples/acme-shop.ttl`](../what/examples/acme-shop.ttl). `what/acme-shop.ttl` here is
  the provisional graph, kept as history and no longer read.
- **New readings.** The projector readings are new (`facts/*.r2.ttl`): the same repositories at
  later commits, whose code cites the landed IRIs. The `r1` files stay, unread.
- **The decisions.** `DDD-dec-65` to `DDD-dec-71` supersede `DDD-dec-55` to `DDD-dec-61` on the
  same terms.
- **The What itself as decisions.** `GRANT-what@1`, `WHAT-found@1` (the founding decision,
  anchored at the product node), `ACC-what@1`, and `what@1`, the first What-version (`DDD-dec-63`
  §6).

Version 1's pins still hold and are still checked, as history. It is still a test product, and
nothing here is acceptable into a real product.

| Provisional (version 1) | Landed (version 2) |
|---|---|
| `…/shop/what#product` | `https://acme.example/products/shop`, the product IRI and product node |
| `…/what#domain-ordering` (the `PURE`, `REST` anchor) | the Ordering bounded context, `…/what/01M610JNAMH5Y3FP9BFRZJ6QSS`. In the landed What, Deciders and Commands sit in the domain's one bounded context, which is the narrowest element covering them (ruling 1) |
| `…/what#system-shop-api`, `#system-shop-bff` | `…/what/01M610JNAMV23W7Y9YQKZPJ4ZA`, `…/what/01M610JNAM8K9PG653537FE7EG` |
| `…/what#qd-residency-eu` | `…/what/01M610JNAMGQQ2DJENWGA6MWCK` |
| `…/what#decider-order`, `#command-*` (in the code's citations) | `…/what/01M610JNAMMP5V59XRNHD39R5A`, `…/what/01M610JNAMCQ2R6MG31Q07DWMX`, `…/what/01M610JNAMC74SDA3DVDE332WB` |

```
python3 applications/sdlc/how-examples/check.py      # needs rdflib for the verdict step
```

At this commit, with rdflib 7.6.0, the script prints 105 ok or note lines, 1 expected warning
(its anchor self-test) and 0 failures. All 36 records (21 of version 1, 15 written on 2026-10-28)
are conformant under the reference implementation on `main`, run unmodified. The records were rebuilt with `dpp/1` and fresh test
keys on 2026-10-28 (Round 3). The `decprov/1` set they replace was never conformant to any
protocol on `main`; it remains in this branch's history at `d11df86`. `build.py` still refuses to
build if the token on `main` and `DDD-dec-62` ever disagree. Without rdflib, the anchor and verdict
steps are reported as **SKIP**, never as passed.

## The cast

| Who | Identity | Holds |
|---|---|---|
| A test vendor (standing in for a package vendor such as Context&) | `mailto:holder@vendor.example` | the genesis grant over the package product `https://vendor.example/packages/ref-arch` |
| The importing product's founder | `mailto:holder@acme.example` | the genesis grant over the product `acme:product` |
| The importing product's architect | `mailto:architect@acme.example` | a grant of the How scope, delegated from that genesis |
| The importing product's owner | `mailto:owner@acme.example` | a grant of the What scope, delegated from that genesis (`GRANT-what@1`) |
| A proposing agent | `spiffe://acme.example/agent/proposer` | nothing: it may propose, it never accepts |

All four human keys are throwaway ed25519 keys for the test genesis's declared test holders.
`build.py` makes fresh ones on every run and discards them when it ends. No real key is ever used
for a fixture or held by a session (Round 3, ruling 1). Signatures are `ssh-sig` over the
canonical form, namespace `decision-provenance`.

## The three decisions, written once

Each is held once, in the package, with no target named in its statement or its violation
description. `check.py` checks that: no statement or violation text contains a target's name,
effect list, region list or native file kind.

| Kind | Package record | States | Anchored in the package | Imported as | Anchored in the importer |
|---|---|---|---|---|---|
| constraint | `LAYER@1` | four ranked layers; no upward dependency; a component in no layer is a violation (the no-orphans reading) | the package product (its What is empty) | `IMP-layer@2` | the product node, `https://acme.example/products/shop` — the narrowest element covering both systems' code |
| binding | `PURE@1` | every Decider is realised, in each language target of each system referencing its domain, by an element whose component uses no effect | the package product | `IMP-pure@2` (proposed by the agent) | the Ordering bounded context |
| contract | `RESID@1` | every data store holding personal data is in an EU-jurisdiction region, as declared and as observed, read within a day | the package product | `IMP-resid@2` | the residency quality demand (what.md §3.6), Kind 2 |

A fourth, `REST@2` (a binding: every Command at `POST /commands/{wire name}`, what.md §6), is the
charter's third "specified once" check. It supersedes `REST@1`, which read the provisional local
id, and is anchored at the Ordering bounded context. It reads the wire name, ruled in Round 2
(`DDD-dec-64`, P-1: "REST@2 stands").

What-version 2 (`what@2`) supersedes `what@1`. The graph is the same. Round 2 amended the
ontology and shapes before sdlc edition 1 was tagged, and `what@2` names the edition by the hash
of the files as held. `what@1`'s pin stays the hash of the files at `2c4f276`.

The package's version 2 (`REL@2`) supersedes the layer rule with `LAYER@2`, which adds a `test`
layer. The importer still rests on version 1. `check.py` shows that through the versions
listing, and shows that nothing in force changed.

## Two targets each

The importer declares two systems. `shop-api` is realised in **C#** and deployed on **Azure**.
`shop-bff` is realised in **TypeScript** and deployed on **AWS** (`TGT-shop-api@1`,
`TGT-shop-bff@1`). Each decision is therefore evaluated in two targets. The per-target shape
lives only in the vocabulary edition records (`VOC-csharp@1`, `VOC-typescript@1`, `VOC-azure@1`,
`VOC-aws@1`). Adding the second language touched no decision: it is one more edition record and
one more target declaration.

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

No fact projector or reporter edition exists. Writ's `code-facts.md` is "not written", and the
editions name their fact source with `"status": "not built"`. So the fact files under `facts/`
are hand-written: they are what an edition *would* emit. `facts/manifest.json` gives each one
its provenance: projector or reporter; Writ's value (`file`, `deployment-declared`, `deployment-observed`); the edition by pinned hash; the
subject (repository at commit, or deployable unit), and when it was read. The What graph in
`what/` is provisional too (`../how.md` §1.2). Each fact file contains one planted defect:

| Planted | Decision | Expected | Got |
|---|---|---|---|
| `Acme.Ordering.Domain` references `Acme.Ordering.Infrastructure` | `LAYER`, C# | 1 violation | 1 |
| `@acme/scratch` has no layer | `LAYER`, TypeScript | 1 violation (no orphans) | 1 |
| `ordering-domain` calls `Date.now` | `PURE`, TypeScript | 1 violation | 1 |
| refund registered at `/command/refund-order` | `REST`, TypeScript | 1 violation | 1 |
| personal-data bucket in `us-east-1` | `RESID`, AWS, `deployment-declared` and `deployment-observed` | 1 each | 1 each |
| no `deployment-observed` facts about the Azure unit | `RESID`, Azure, `deployment-observed` | **open question**: gap reported, absent reporter named as a candidate | open question |
| none | `LAYER`/`PURE`/`REST` C#, `RESID` Azure `deployment-declared` | 0 | 0 |

The expectations were written as the defects were planted, before the first run, and are
in `expected.json`. They are **analytic**, not evidence: a fixture built to fire, fired. The run
shows that the violation descriptions execute as written in both targets, that one decision
text serves both targets, and that an absent reading comes out as an open question. It shows nothing about
whether the How is right.

`RESID@1` requires both provenance values, `deployment-declared` and `deployment-observed`, in its
`factSources`. The `dpp/1` rebuild issued it with them.

## What `check.py` checks

1. Every record is conformant under the reference implementation on `main`, **unmodified**.
2. Every reference reachable from `ACC-1@2`, `ACC-what@1`, `what@1` and `REL@3` (and, as history, from `ACC-1@1` and `REL@2`) names a record held
   here whose hash matches its pin. A test edit of one word in `LAYER@1` turns both lines
   red.
3. Every signature verifies over its record's canonical form.
4. The authority chain is a **test stand-in** for the unwritten authority profile. The
   acceptance's signer holds a grant. That grant was signed by the genesis holder. The genesis
   is an origin. All three are signed, and the acceptor is a human identity, not an agent.
5. Exactly six How records are in force, all version 2: those `ACC-1@2` pins. `ACC-1@1` is
   superseded and puts nothing in force. No record in force names a provisional identifier. One
   What decision is in force, the founding `WHAT-found@1`. `what@1`'s graph hash and element list
   equal `../what/vectors.json`, and `../what/check.py` recomputes those from the graph.
6. Each imported decision is expressible in each declared target: every fact term its violation
   description reads is mapped by that target's edition.
7. Supersession across the import is shown and changes nothing in force. There are four notes:
   `IMP-layer@2` on `LAYER@1` and `REL@1`; `IMP-pure@2` and `IMP-resid@2` on `REL@1`.
8. Anchors (ruling 1). Each import's anchor is the narrowest element covering what it governs
   today. Otherwise the checker prints a warning, which is not a failure. A self-test re-anchors
   `PURE` at the product and expects the warning. The ruling calls that anchor legitimate for an
   "every Decider" rule, so the warning is advisory.
9. The verdicts, per decision and per target, equal `expected.json`.
