# The How, worked — three decisions, two targets each

Companion to [`../how.md`](../how.md) §8. **`[PROPOSED]` — nothing here is ruled.** Every record is
a `decprov/1` record (the token `DDD-dec-53` rules), pinned by the hash law of
`spec/decision-provenance/` and checked by [`check.py`](check.py).

```
python3 applications/sdlc/how-examples/check.py      # needs rdflib for the verdict step
```

At this commit the script prints 67 ok or note lines and 0 failures with rdflib installed. Without rdflib it
reports the verdict step as **SKIP** and exits non-zero. It never reports the skipped step as a
pass.

## The cast

| Who | Identity | Holds |
|---|---|---|
| A test vendor (standing in for a package vendor such as Context&) | `mailto:holder@vendor.example` | the genesis grant over the package product `https://vendor.example/packages/ref-arch` |
| The importing product's founder | `mailto:holder@acme.example` | the genesis grant over the product `acme:product` |
| The importing product's architect | `mailto:architect@acme.example` | a grant of the How scope, delegated from that genesis |
| A proposing agent | `spiffe://acme.example/agent/proposer` | nothing: it may propose, it never accepts |

All three human keys are throwaway ed25519 keys made for this example. The private keys are
not in the repository. Signatures are `ssh-sig` over the canonical form, namespace `decprov`.

## The three decisions, written once

Each is held once, in the package, with no target named in its statement or its violation
description. `check.py` checks that: no statement or violation text contains a target's name,
effect list, region list or native file kind.

| Kind | Package record | States | Anchored in the package | Imported as | Anchored in the importer |
|---|---|---|---|---|---|
| constraint | `LAYER@1` | four ranked layers; no upward dependency; a component in no layer is a violation (the no-orphans reading) | the package product (its What is empty) | `IMP-layer@1` | the product node — the narrowest element covering both systems' code |
| binding | `PURE@1` | every Decider is realised, in each language target of each system referencing its domain, by an element whose component uses no effect | the package product | `IMP-pure@1` (proposed by the agent) | `domain-ordering` |
| contract | `RESID@1` | every data store holding personal data is in an EU-jurisdiction region, as declared and as observed, read within a day | the package product | `IMP-resid@1` | `qd-residency-eu`, the Kind-2 quality demand it realises |

A fourth, `REST@1` (a binding: every Command at `POST /commands/{id}`), is the charter's third
"specified once" check. It is carried the same way and anchored at `domain-ordering`.

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
| declared reading | Bicep at a commit | Terraform at a commit |
| observed reading | Resource Graph | Resource Explorer |

## The facts, and what is hand-written

No fact projector or reporter edition exists. Writ's `code-facts.md` is "not written", and the
editions name their fact source with `"status": "not built"`. So the fact files under `facts/`
are hand-written: they are what an edition *would* emit. `facts/manifest.json` gives each one
its provenance: projector or reporter, files/declared/observed, the edition by pinned hash, the
subject (repository at commit, or deployable unit), and when it was read. The What graph in
`what/` is provisional too (`../how.md` §1.2). Each fact file contains one planted defect:

| Planted | Decision | Expected | Got |
|---|---|---|---|
| `Acme.Ordering.Domain` references `Acme.Ordering.Infrastructure` | `LAYER`, C# | 1 violation | 1 |
| `@acme/scratch` has no layer | `LAYER`, TypeScript | 1 violation (no orphans) | 1 |
| `ordering-domain` calls `Date.now` | `PURE`, TypeScript | 1 violation | 1 |
| refund registered at `/command/refund-order` | `REST`, TypeScript | 1 violation | 1 |
| personal-data bucket in `us-east-1` | `RESID`, AWS, declared and observed | 1 each | 1 each |
| no observed reading of the Azure unit | `RESID`, Azure, observed | **unknown**, not pass, not violation | unknown |
| none | `LAYER`/`PURE`/`REST` C#, `RESID` Azure declared | 0 | 0 |

The expectations were written as the defects were planted, before the first run, and are
in `expected.json`. They are **analytic**, not evidence: a fixture built to fire, fired. The run
shows that the violation descriptions execute as written in both targets, that one decision
text serves both targets, and that an absent reading comes out unknown. It shows nothing about
whether the How is right.

## What `check.py` checks

1. Every record is conformant under the reference implementation on `main`, with one
   substitution: its token literal `dpp/1` becomes `decprov/1` (`../how.md` §1.2).
2. The walk from the acceptance `ACC-1@1` and from `REL@2` holds at every hop, with every pin
   matching. A test edit of one word in `LAYER@1` turns the first walk red.
3. Every signature verifies over its record's canonical form.
4. The authority chain is a **test stand-in** for the unwritten authority profile. The
   acceptance's signer holds a grant. That grant was signed by the genesis holder. The genesis
   is an origin. All three are signed, and the acceptor is a human identity, not an agent.
5. Exactly six records are in force: those the acceptance pins.
6. Each imported decision is realisable in each declared target: every fact term its violation
   description reads is mapped by that target's edition.
7. Supersession across the import is shown and changes nothing in force.
8. The verdicts, per decision and per target, equal `expected.json`.
