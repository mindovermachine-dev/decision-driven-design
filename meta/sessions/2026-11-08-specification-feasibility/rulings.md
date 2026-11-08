# Rulings — specification feasibility, 2026-11-08

Emil's rulings, in the order given. Each quotes the message from `prompt.md` that gave it. Where a
message ruled on a proposal of Claude's, the proposal is stated here as it stood when it was
accepted. M-11 accepted every proposal then standing ("All proposed are accepted"), so those
proposals are rulings too. The proposals withdrawn or corrected during the conversation are listed
after them. They are **not** ruled.

The decisions are `DDD-dec-116` (specification feasibility: F-1 to F-4 and F-6 to F-12) and
`DDD-dec-117` (grants and roles: F-5).

## The request — M-1

> In the product framework we need to have specification constraints - what data can we use, what
> integrations are available etc so that we can do feasibility in product-cli

A request, not a ruling. Claude found no use of "feasibility" in the What, `how.md` or
product-cli's definition, and no branch of either repository working on it.

## F-1 — the constraint is organisational (M-2)

> This is primarily a problem in organizations because of the way Conway law says that system
> design is directly impacted by the organization design

**Accepted with M-11.** A specification's dependency on outside ground has three parts, with three
owners:

| Part | Says | Principal |
|---|---|---|
| Demand | which external reads and calls our What implies | our product |
| Source | what exists, and its shape | the owning unit |
| Permission | that we may use it, for what, under which terms | the owning unit, as a decision in its own space, referenced by `dpp/1` |

Grounds stated with the proposal: `authority.md` §1.1 gives force only within one product, and a
reference from another system confers none. So "we may use your data" cannot be a decision in our
product. Conway's law predicts where these constraints sit. It is an observation, not canon, and
it does not rule.

## F-2 — every dependency is loosely coupled, and the How decides (M-3)

> And since this is a dependency it has the same issue as with all dependencies. It must be
> loosely coupled. And this also means that there are two layers to each, the one in the what that
> you just described and the one in the how. And the how must dictate whether its feasible or not
> since a hard coupling will have a direct impact on the how systems ability to send features to
> production

**Ruled.** Every dependency on ground has a What layer and a How layer. The How layer decides
whether it is feasible, because a hard coupling impairs the ability to ship.

**Accepted with M-11.** "Loose" is checkable, by three conditions:

| Condition | How kind (`how.md` §4.2) | Gates `land`? |
|---|---|---|
| Our code reads only the provider's published wire contract, pinned at an edition, and none of its internals | constraint, over code facts | yes |
| Deploying our unit needs no deploy of theirs, and no ordering between the two | contract, over facts with provenance `deployment-declared` | yes |
| When the provider is unavailable, our unit degrades or queues; it does not fail | a What quality demand (architectural constraint), held by a contract | only in its declared part |

## F-3 — product-cli holds the full verdict (M-4)

> Product-cli must contain the full feasibility verdict in order to continue creating
> specifications that the how can actual land. The reason why its hard to do the split today is
> that we don't have a complete data model on a specification and so we rely on the human actors
> ability to infer alot of the information in order to complete a feature.

**Ruled.** product-cli carries the full feasibility verdict, so that it produces specifications the
How can land. The ground: the specification's data model is incomplete, and human actors infer the
missing information. F-4 rules how the verdict reaches product-cli.

## F-4 — vetting is decoupled from Writ (M-5)

> We must have a way to decouple writ here, it could be any actor doing the how. So we need to
> expose a non verified feature for feasibility and then allow it to be vetted by actors allowed to
> do that act in product-cli how do they that we don't care. We just want the decision that it is
> possible added in product-cli

**Ruled.** product-cli exposes a specification as not yet vetted for feasibility. Any actor allowed
to perform the vetting act vets it, by any means. product-cli records only the decision that it is
feasible. Writ is one possible actor, not the required one.

**Accepted with M-11.**
- The vetting decision is a `dpp/1` record, anchored to the specification, `basedOn` its pinned
  version, with a verdict (feasible or not) and a `why`.
- Staleness follows from the pin. A later change to an element the decision covers leaves it
  pinned to an old version, and product-cli shows that without re-evaluating anything.
- A feasibility decision is projected. Landing makes it reported. product-cli never shows the two
  as one.

## F-5 — product-cli and the framework carry grants and roles (M-6, item 1)

> 1. Needs to change we need to have the same grants, roles etc as the other systems. Its already
> built into product-cli and it should also have been added to the product FRAMEWORK.

**Ruled.** product-cli carries the same grants and roles as the other systems, and only a holder
of a grant may vet. The product framework carries roles. This supersedes product-cli's `[D1.11]`
("No authority, ever") and the row of `authority.md` Appendix B that dropped roles.

**Accepted with M-11.**
- A scope ranges over decision kinds as well as What element kinds. A grant to vet carries a scope
  over the vetting decision's kind (named in the proposal as `sdlc:FeasibilityVetting`).
- A role is a named, reusable scope. A grant may cite a role, and the role is evaluated wherever
  the grant is. This answers Appendix B's ground for dropping roles ("a name for a scope nobody
  evaluates").

## F-6 — the unit vetted (M-6, item 2)

> 2. Agreed a pinned version.

**Ruled.** The unit vetted is a proposed change to the What at a pinned version. It is not a
feature: features are retired Delivery (`DDD-dec-42`).

## F-7 — vetted ground carries forward (M-6, closing paragraph)

> Also the ruling on feasibility for ground is something that can be reused in the how. If it has
> been vetted in the how once, it should carry that forward if someone else wants to use the same
> ground.

**Ruled.** A vetting of ground, once made in the How, carries forward to anyone else who uses the
same ground.

**Accepted with M-11.** What carries forward:

| Part of a vetting | Carries forward? |
|---|---|
| Source side: a published contract at an edition, versioning, behaviour when unavailable | yes |
| Permission | no; the owner grants it per consumer |
| Consumer-side coupling | no; it belongs to our realisation |
| Shape fit to our demand | no; the demand is ours |

F-8 and F-9 refine where the carried part lives and how far it reaches.

## F-8 — vetted ground becomes What (M-7)

> We add it to the domain entities if its feasible from the how side. Then they become whats
> reusable

**Ruled.** Once ground is vetted feasible from the How side, it enters the domain model as
entities, and from then on it is What.

**Accepted with M-11.**
- The entities sit in a **ground-sourced bounded context**: a bounded context whose meaning is the
  source's. Our contexts map from it with direction declared (`sdlc:mapsFrom` is the source; What
  §3.1, `DDD-dec-113` E-8).
- A holder of a grant scoped over the entity kinds adds them by a What decision (F-5). No tool adds
  them (`DDD-dec-43`).
- That decision is `basedOn` the How's vetting, pinned to the source's edition.
- A new edition of the source is a What change that supersedes the entities.
- Being in the What does not grant permission to use the source (F-12).

## F-9 — vetting is per system (M-8)

> Agreed we cant do it by domain only because the vetting happens pr system. So we need to be able
> to specify that the domain entity has been vetted for the specific system and can be reused in
> decides only in that system

**Ruled.** Vetting holds per system. The What records that ground has been vetted for a specific
system, and its use is admitted only in that system.

**Accepted with M-11.**
- An **admission** is a What element within a system. It names what it admits (F-11) and is
  `basedOn` the How's vetting for that system.
- An admission sits within the system so that a grant narrowed to the system's subtree (What §5.1)
  can add it without the domain owner's scope.
- The check: an element within system S that reaches ground-sourced ground with no admission for it
  within S is a violation. It is closed over the What, so product-cli computes it.
- The admission is a new element kind. This corrects Claude's statement at M-7 that "no ontology is
  added" (W-4).

## F-10 — what admissions gate (M-9, item 1)

> 1. All three

**Ruled.** Admissions gate Deciders, Projectors and Views.

**Accepted with M-11.** The What records each path:

| Element | Reaches a ground-sourced context C through |
|---|---|
| Decider | `sdlc:reads` a field within an entity in C |
| Projector | `sdlc:folds` an event that `sdlc:changes` an entity in C, or `sdlc:keyedBy` a field in C |
| View | `sdlc:projects` an event that `sdlc:changes` an entity in C |

## F-11 — the unit of admission (M-9, item 2)

> 2. Pr ground-sourced context if we can get one data entity from the integration we can get all
> of them

**Ruled.** An admission admits a ground-sourced context as a whole, not entity by entity.

## F-12 — permission is the owner's, not the How's (M-10)

> Good catch - each integration is of course behind some sort of OAuth2 so it depends on our
> access. But that should be the data owner decision on what we can use not if the feasibility in
> the how

**Ruled.** What we may use from an integration, for example through its OAuth2 scopes, is the data
owner's decision, not part of feasibility in the How. Feasibility stays per ground-sourced context.

**Accepted with M-11.**

| Check | Grain | Principal |
|---|---|---|
| Admission (feasibility) | ground-sourced context × system | a How vetter holding a grant |
| Permission | the grain the owner decides: context, entity or field | the data owner |

- An element passes only if its context is admitted for its system *and* every field it reaches is
  covered by the owner's permission.
- An unresolvable reference to the owner's decision is `Unknown`, never a pass.
- The map from the owner's access scopes (OAuth2 scopes) to fields is part of the owner's decision,
  so the owner signs the grain they grant.

## Withdrawn or corrected during the conversation — not ruled

| | Proposal | Withdrawn by |
|---|---|---|
| W-1 | product-cli reports the What side only; Writ computes the feasibility verdict | M-4 (F-3) |
| W-2 | Two evaluators over one rule set: product-cli's projected verdict over declared facts, Writ's reported verdict at `land`; product-cli reads How decisions as packages | M-5 (F-4) |
| W-3 | Permission held in the source declaration, or in our authority profile | Claude, at M-2, by F-1 |
| W-4 | "No ontology is added" for ground-sourced entities | Claude, at M-8, by F-9 (correction) |
| W-5 | A source with field-level restrictions is split into two ground-sourced contexts | M-10 (F-12) |

## Not ruled — open

- **O-1. Whose What holds a ground-sourced context when the source belongs to no product?** Absorb
  it into ours, or require the owner to found a product. This is `DDD-dec-113`'s Q-C2 ("outside
  systems with no What"), still open.
- **O-2. Where the owners come from.** Whether the map of who owns which ground is the
  Decision-Driven Organisations grant map. Asked at M-2, not answered.

## How the rulings are read — `UNVERIFIED — Emil review`

These readings are the session's, not Emil's.

- **R-a. M-11's reach.** "All proposed are accepted" is read as accepting every proposal standing at
  M-11, as stated above, and none of W-1 to W-5. Questions Claude asked (O-1, O-2) are not
  proposals and stay open.
- **R-b. M-3 and M-4 together.** M-3 says the How dictates feasibility; M-4 says product-cli holds
  the full verdict. They are read together through M-5: the How's actor decides, and product-cli
  records the decision.
- **R-c. M-6's "product FRAMEWORK".** Read as `applications/sdlc/` (the What and the authority
  profile), the framework's home since the move (`DDD-dec-41`).
- **R-d. M-8's "decides".** Read as Deciders; M-9 then extends the gate to Projectors and Views.
