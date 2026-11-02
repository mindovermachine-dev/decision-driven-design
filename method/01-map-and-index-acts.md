# Step 1 — Map and index acts

**Register: ruled for test, projected.** The step's form is ruled: Emil's rulings R-2 and R-4 to
R-8 in the act address session
([`rulings.md`](../meta/sessions/2026-09-27-act-address/rulings.md)), filed as claims by
`DDD-dec-38`. Every claim it rests on is **projected**: argued, with a declared falsifier, and not
yet exercised. Step 1 stands or falls on **T2b**, the first independent application case,
pre-registered with its predictions fixed before the case exists. T2b has not run. Until it does,
nothing on this card is reported, and the step should be tried, not relied on (`DDD-dec-74`).

**Weakest point.** The address is blind to every ground axis nobody declared (`DDD-ground-06`'s
region). A map made with the wrong axes looks complete and is not, and the step itself cannot
tell you which axes you missed.

## What the step does

Map the acts the work consists of, forward from the domain and the request, never backward from
existing code. Give each act occurrence an address, its coordinate. The address is the
occurrence's position on declared ground axes together with its layer path, the chain of
composite acts it sits within. The actor who performs the act is **not** part of the address, so
different actors can occupy the same address and their behaviour can be compared. Beside the
address, each occurrence carries a causal time index: B comes after A when a state change A
produced is in B's ground reading.

The sequence, the field names and the value line come from the act address session's method draft
([`method-instructions-draft.md`](../meta/sessions/2026-09-27-act-address/method-instructions-draft.md)),
which is `[PROPOSED]`. The address and the time index come from the claims below.

## The canon it rests on

Read live on 2026-11-02. The upstream `main` equals the pinned tag `v5.15.2` (`084bce7`), and
both upstream claims are pinned at `projected` in [`graph/upstream.yaml`](../graph/upstream.yaml).
Statements are quoted from the claim files, whitespace-normalised. The claim file governs, and
where this card and a claim disagree, the card is wrong.

| Claim | Kind | Status | Where | Statement |
|---|---|---|---|---|
| `DDD-ground-06` | conceptual | **projected** | upstream, pinned at `v5.15.2` | An act occurrence's address is its position on declared ground axes together with its layer path — the chain of composite acts it sits within — extracted at the act-site, and the occupying actor is not a component of the address. |
| `DDD-ground-01` | normative | **projected** | upstream, pinned at `v5.15.2` | A governing decision must declare a resolvable applicability predicate, unless it explicitly declares universal applicability; non-evaluation must never silently become non-applicability, and where the predicate is implemented over declared ground axes, each axis is marked mechanically-evaluable or judgement-evaluable. |
| `DDD-address-01` | conceptual | **projected** | [`core/claims/DDD-address-01.yaml`](../core/claims/DDD-address-01.yaml) | Act occurrences carry a time index beside their address, given by causal dependency — occurrence B depends on occurrence A iff a state change produced by A is in B's ground reading — so that the index is the resulting order over state changes rather than wall-clock, dependent occurrences at one address are distinct in time, and independent ones may be concurrent. |
| `DDD-address-02` | normative | **projected** | [`core/claims/DDD-address-02.yaml`](../core/claims/DDD-address-02.yaml) | Every act occurrence is its own act, and reuse of code across occurrences is a derivation-layer relation — many occurrences pulling one component — never an identity between acts. |
| `DDD-address-03` | empirical | **projected** | [`core/claims/DDD-address-03.yaml`](../core/claims/DDD-address-03.yaml) | A change to a component pulled by several act occurrences is an escaped decision at every pulling occurrence that the changing decision's applicability predicate does not cover. |
| `DDD-address-04` | conceptual | **projected** | [`core/claims/DDD-address-04.yaml`](../core/claims/DDD-address-04.yaml) | Two act occurrences coincide when their ground positions are equal, whatever their layer paths. |
| `DDD-address-05` | conceptual | **projected** | [`core/claims/DDD-address-05.yaml`](../core/claims/DDD-address-05.yaml) | Behaviour is read at two grains: at full address within one parent, and at ground position across parents. |

`DDD-address-03` to `05` are what makes the map pay later: a change to a shared component is an
escaped decision at every pulling occurrence its predicate does not cover, and behaviour is read
per address. Step 1 only has to make the addresses they need.

## The step card

Fields are the method draft's. Where the canon fills a field, the source is named. Where it does
not, the field says so. Claude's assembly of the fields from their sources is
`UNVERIFIED — Emil review`.

| Field | Content | Source |
|---|---|---|
| Step | 1 — Map and index acts | Method draft (`[PROPOSED]`); "the method starts by mapping acts and indexing them" is Emil's originating statement (act address rulings) |
| Decision discharged | The decomposition: which acts the work consists of, and where each sits. Addresses are relative to a ruled decomposition, and re-decomposition supersedes them. The commitment level is not filed | `DDD-ground-06` region |
| Ground in | The domain and the request. The ground axes, declared before any position is read on them | Method draft; `DDD-ground-06` region (declared-space limit, `DDD-ground-05`, `DDD-ground-02`) |
| Act | Map acts forward, never back from code. Address each occurrence by its position on the declared axes and its layer path, with the actor left out. Index occurrences in causal order. Treat every occurrence as its own act, and record code reuse as derivation (many occurrences pulling one component), never as one act | `DDD-ground-06`; `DDD-address-01`; `DDD-address-02` |
| Artefact out | The act map: a tree of occurrences, each with an address and a time index. Graph data is preferred to prose | `DDD-address-02` region; method draft |
| Value made visible | "Decisions and actors get a place to be anchored, and every later artefact has an address to attach to" | Method draft, verbatim |
| Cost and relocation | Not filed | — |
| Exit check | Within the ruled decomposition, every occurrence has exactly one address, and its governing set can be computed from that address, its ground readings and the decisions' applicability predicates, without the verdict itself | `DDD-ground-06` falsifier and test, read as a check. Reading `UNVERIFIED — Emil review` |
| Principal | Whoever rules the decomposition. The method names no role for it | `DDD-ground-06` region ("a ruled decomposition"); the role is not filed |

## What would break it

- **The claims.** Each claim above carries its own falsifier in its file. `DDD-ground-06` fails if
  an occurrence's governing set cannot be computed from its address, ground readings and
  predicates, if two occupants at one address must declare different axes to act at all, or if
  the same occurrence lands on two addresses by mapping choice alone.
- **The step, as a method step.** The draft's default falsifier, `[PROPOSED]`: "practitioners
  perform the step and cannot name the value it gave them." The quick start's form of it is the
  junior-engineer test ([`quick-start.md`](quick-start.md)).

## Try it

[`quick-start.md`](quick-start.md) runs this step on the HTTP slice of Varve's own quick start.

Next: [02 — Anchor authority](02-anchor-authority.md) `[PROPOSED]` · [All steps](README.md)
