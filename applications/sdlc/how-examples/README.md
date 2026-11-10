# The How, worked — three decisions, two targets each

<!-- ddd:doc
reader: architects and tool builders who want to see the What, the How and the authority profile working end to end on one test product, and run the checker
act: run check.py, read what each record shows, and know what the run does and does not prove
pin: v5.15.2
basis: [DDD-dec-62, DDD-dec-53, DDD-dec-63, DDD-dec-64, DDD-dec-65, DDD-dec-66, DDD-dec-67, DDD-dec-68, DDD-dec-69, DDD-dec-70, DDD-dec-71, DDD-dec-86, DDD-dec-93, DDD-dec-113, DDD-dec-119]
status: current
supersedes: 84aa466:applications/sdlc/how-examples/README.md
-->

Companion to [`../how.md`](../how.md) §12. This folder is a worked example: a test vendor ships a
package of How decisions, and a test product, Acme Shop, imports them, holds them under the
authority profile and checks them in two targets. Every record is a `dpp/1` record, pinned by the
hash law of `spec/decision-provenance/`. It was built by [`build.py`](build.py) and is checked by
[`check.py`](check.py).

**How settled this is.** It is a test product, and nothing here is acceptable into a real product.
The rules it exercises are the ruled What, How and authority profile. The fact files are
hand-written, so the run shows that the rules execute as written; it shows nothing about whether
the How is right.

## Run it

```
python3 applications/sdlc/how-examples/check.py      # needs rdflib for the verdict step
```

At this commit, with rdflib 7.6.0, the script prints 238 ok or note lines, 1 expected warning (its
anchor self-test) and 0 failures. All 67 records are conformant under the reference implementation
on `main`, run unmodified. Without rdflib, the anchor and verdict steps are reported as **SKIP**,
never as passed.

The records were rebuilt with `dpp/1` and fresh test keys on 2026-10-28. The `decprov/1` set they
replace was never conformant to any protocol on `main`; it remains in this branch's history at
`d11df86`. `build.py` still refuses to build if the token on `main` and the ruled token ever
disagree.

## The cast

| Who | Identity | Holds |
|---|---|---|
| A test vendor (standing in for a package vendor such as Context&) | `mailto:holder@vendor.example` | the genesis grant over the package product `https://vendor.example/packages/ref-arch` |
| The importing product's founder | `mailto:holder@acme.example` | the genesis grant over the product `acme:product` |
| The importing product's architect | `mailto:architect@acme.example` | a grant of the How scope, delegated from that genesis |
| The importing product's owner | `mailto:owner@acme.example` | a grant of the What scope, delegated from that genesis (`GRANT-what@1`) |
| A proposing agent | `spiffe://acme.example/agent/proposer` | nothing: it may propose, it never accepts |

The four human keys of the version 1 and 2 records were throwaway ed25519 keys, made fresh on each
build and discarded when it ended. Since 2026-11-02 the authority history's keys are kept in
[`test-keys/`](test-keys/) instead. No real key is ever used for a fixture or held by a session.
Signatures are `ssh-sig` over the canonical form, namespace `decision-provenance`.

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
id, and is anchored at the Ordering bounded context. It reads the wire name, as ruled ("REST@2
stands"). So Acme Shop imports four How decisions: `IMP-layer`, `IMP-pure`, `IMP-resid` and
`IMP-rest`.

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
its provenance: projector or reporter; Writ's value (`file`, `deployment-declared`,
`deployment-observed`); the edition by pinned hash; the subject (repository at commit, or
deployable unit), and when it was read. The What graph in `what/` is provisional too
(`../how.md` §1.2). Each fact file contains one planted defect:

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
text serves both targets, and that an absent reading comes out as an open question. It shows
nothing about whether the How is right.

`RESID@1` requires both provenance values, `deployment-declared` and `deployment-observed`, in its
`factSources`. The `dpp/1` rebuild issued it with them.

## What `check.py` checks

1. Every record is conformant under the reference implementation on `main`, **unmodified**.
2. Every reference reachable from `ACC-1@2`, `ACC-what@1`, `what@1` and `REL@3` (and, as history,
   from `ACC-1@1` and `REL@2`) names a record held here whose hash matches its pin. A test edit of
   one word in `LAYER@1` turns both lines red.
3. Every signature verifies over its record's canonical form.
4. The authority profile, over the positioned log: every header's position, chain, monotone clock
   and pins; every act judged by `../authority/evaluate.py` as the header records it (landed
   valid, or refused with the header's reason); the multi-scope decision not in force at p5 and in
   force at p6; the revoked chain falling at p11 while `CURFMT@1` stays in force; the rotated key
   still verifying `ACC-1@3`; the waiver live at p14 and expired at p15. Against the What graph:
   every recorded scope item's class and path, `CUR@1`'s and `SCN@1`'s deltas, every reported
   violation in the baseline, and the waived question being an open question.
5. Six How records are in force at the last position, all version 2, re-accepted by `ACC-1@3`. The
   What decisions in force are `WHAT-found@1`, `CUR@1` and `SCN@1`. No record in force names a
   provisional identifier. The What-version in force, `what@5`, equals `../what/vectors-5.json`.
6. Each imported decision is expressible in each declared target: every fact term its violation
   description reads is mapped by that target's edition.
7. Supersession across the import is shown and changes nothing in force. There are four notes:
   `IMP-layer@2` on `LAYER@1` and `REL@1`; `IMP-pure@2` and `IMP-resid@2` on `REL@1`.
8. Anchors. Each import's anchor is the narrowest element covering what it governs today.
   Otherwise the checker prints a warning, which is not a failure. A self-test re-anchors `PURE`
   at the product and expects the warning. The anchor rule calls that anchor legitimate for an
   "every Decider" rule, so the warning is advisory.
9. The verdicts, per decision and per target, equal `expected.json`.

## How the records came to be

### Superseded against the landed What (2026-10-28)

The version 1 records were accepted provisionally: they anchored to What identifiers fixed before
the identity form existed, and each was to be "superseded by a version against the real
identifiers, never edited". The What has landed ([`../what.md`](../what.md)) in the ruled identity
form, so:

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
- **The decisions.** The How's decisions were superseded on the same terms.
- **The What itself as decisions.** `GRANT-what@1`, `WHAT-found@1` (the founding decision,
  anchored at the product node), `ACC-what@1`, and `what@1`, the first What-version.

Version 1's pins still hold and are still checked, as history.

| Provisional (version 1) | Landed (version 2) |
|---|---|
| `…/shop/what#product` | `https://acme.example/products/shop`, the product IRI and product node |
| `…/what#domain-ordering` (the `PURE`, `REST` anchor) | the Ordering bounded context, `…/what/01M610JNAMH5Y3FP9BFRZJ6QSS`. In the landed What, Deciders and Commands sit in the domain's one bounded context, which is the narrowest element covering them (the anchor rule) |
| `…/what#system-shop-api`, `#system-shop-bff` | `…/what/01M610JNAMV23W7Y9YQKZPJ4ZA`, `…/what/01M610JNAM8K9PG653537FE7EG` |
| `…/what#qd-residency-eu` | `…/what/01M610JNAMGQQ2DJENWGA6MWCK` |
| `…/what#decider-order`, `#command-*` (in the code's citations) | `…/what/01M610JNAMMP5V59XRNHD39R5A`, `…/what/01M610JNAMCQ2R6MG31Q07DWMX`, `…/what/01M610JNAMC74SDA3DVDE332WB` |

### What-versions 2 and 3

`what@2` supersedes `what@1`. The graph is the same. The ontology and shapes were amended before
sdlc edition 1 was tagged, and `what@2` names the edition by the hash of the files as held.
`what@1`'s pin stays the hash of the files at `2c4f276`. `what@3` supersedes `what@2` when the
move's own choices were ruled. It too kept the same graph and renamed the edition by the hash of
the ontology and shapes as amended before edition 1 was tagged. `what@2`'s pin is held to the
files at `655db92`.

### Under the authority profile (2026-11-02)

The product's authority history is a positioned log, [`log/acme.json`](log/acme.json), judged by
the profile's reference evaluator ([`../authority.md`](../authority.md) §9). On 2026-11-02 it had
15 positions, and 25 records were added, none edited:

- `GEN@3` founds the log. The stand-ins' keys were discarded, so no act under them can be signed.
  It is the acme fixture's one re-founding, as a test fixture and not as a transfer (authority.md
  §2.6). The vendor package is re-founded the same way by its `GEN@2`, in `log/vendor.json`.
- Two class-scoped grants and their acceptances.
- Re-acceptances of the founding What decision and the six How records, with a baseline.
- `CUR@1`, one decision under two scopes: a new What field and a binding. `what@4` names the graph
  after it ([`../what/examples/acme-shop-4.ttl`](../what/examples/acme-shop-4.ttl), with hashes in
  `../what/vectors-4.json`).
- Two levels of delegation and a revocation that takes the lower one down.
- A key rotation.
- A waiver that expires by header clock.
- A review.
- Two refused attempts, recorded in their headers.

The stand-in authority records (`GEN@1`, `GEN@2`, `GRANT-*@1/2`, `ACC-1@1/2`, `ACC-what@1`) stay as
history, landed at no position, and under the profile they put nothing in force. `build.py` needs
rdflib, because each acceptance records its scope result read from the What graph. It refuses to
rewrite a landed header. The history's keys are kept for the fixture's life in
[`test-keys/`](test-keys/): test keys of the declared test holders, never used outside the fixture.
A rebuild reproduces every record, and a later session can extend the history.

### sdlc edition 1 (2026-11-06)

`SCN@1` at p16, the log's sixteenth position: a What change that creates the scenario for (Place
order, Customer) and fills four descriptions, so that the What carries no findings under sdlc
edition 1. It is accepted by `ACC-scn-what@1`. `what@5` names the graph after it
([`../what/examples/acme-shop-5.ttl`](../what/examples/acme-shop-5.ttl), with hashes in
`../what/vectors-5.json`) and the edition as completed. `what@3` and `what@4` keep the edition hash
they were published with.

## Where this comes from

| Section | Rests on |
|---|---|
| `dpp/1` records | `DDD-dec-62`, superseding `DDD-dec-53` (the token, ruled 2026-10-28, Round 3) |
| Run it: the counts | Re-run on `84aa466` on 2026-11-10 by `meta/sessions/2026-11-09-applications-for-readers-redo/`: 238 ok or note lines, 1 expected warning, 0 failures; "67 of 67 records conformant". The earlier text said 225 lines and 64 records. The three records added since are `SCN@1`, `ACC-scn-what@1` and `what@5` (commit `8a5b4e9`, 2026-11-06). Of the 67, 27 were added on 2026-11-02 (25 under the authority profile, `308c9a8`; `what@3`, `d994a8d`; the vendor's `GEN@2`, `e120251`); the earlier text said 26 |
| The cast; no real key | The 2026-10-28 How session, Round 3, ruling 1; the test keys, the authority-profile session, Round 2, P-6 |
| The three decisions; `REST@2` | `DDD-dec-55` to `-61`, superseded on the same terms by `DDD-dec-65` to `-71`; `DDD-dec-119`; `REST@2` stands, `DDD-dec-64` P-1 (Round 2 of the What move) |
| Acme Shop imports four How decisions | `records/acme/IMP-layer`, `IMP-pure`, `IMP-resid`, `IMP-rest`; `check.py`: "6 records (two target declarations, four imports)" |
| Anchors | The anchor rule: ruling 1 of 2026-10-28, `DDD-dec-55` |
| Superseded against the landed What | Ruling 4 of 2026-10-28; the identity form, `DDD-dec-63`; `what@1`, `DDD-dec-63` §6; `DDD-dec-65` to `-71` supersede `DDD-dec-55` to `-61` |
| What-versions 2 and 3 | Round 2 of the What move (the ontology and shapes amended); `what@3`, Round 5, when `DDD-dec-64` was ruled |
| Under the authority profile | `DDD-dec-86` (Round 1, Q-9: the worked example); `GEN@3` as the one re-founding, A-5, ruled; the vendor's `GEN@2`, Round 3, P-9 (`DDD-dec-93`); test keys, Round 2, P-6 |
| sdlc edition 1 | `DDD-dec-113`, E-5 |

The earlier text of this page is at `84aa466:applications/sdlc/how-examples/README.md`.
