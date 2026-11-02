# The authority vocabulary — `sdlc:`

**Status:** with [`authority.md`](authority.md) (`DDD-dec-85`, `DDD-dec-86`). Written 2026-11-02;
not yet ratified.

**Namespace.** `https://decision-driven-design.dk/ns/sdlc#`, prefix `sdlc:`, beside the How's
terms ([`how-vocabulary.md`](how-vocabulary.md)) and the What's ([`what/ontology.ttl`](what/ontology.ttl)).
`UNVERIFIED — Emil review`: no IRI under `/ns/sdlc` is served yet (successor item M-10 of the
move).

**In records.** *Ruled (Round 1, F-2).*
- **Where.** Every term below lives, in a `dpp/1` record, in the hashed dotted member
  `dk.decision-driven-design.authority`. Its `record` names the kind.
- **Never `extensions`.** Nothing here is in `extensions`.
- **Values.** Hashed content is objects, arrays and strings only (`dpp-1.md` §5.2), so a flag is
  `"yes"` and every time is a string.

**The protocol's members, as every record kind uses them.**
- `by` is the actor, and `at` is the date of the act's position.
- `basedOn` pins what the act rests on.
- `signature` is required on every act of authority.
- `attributedTo` never appears on one (authority.md §5.1).

---

## 1. Record kinds

`…` stands for `dk.decision-driven-design.authority`. Times are RFC 3339 UTC strings compared with
header clocks (authority.md §6.2). A grant is named by its `id`, and a version by its reference.

| Term | Definition | Record shape (`dpp/1`) |
|---|---|---|
| `sdlc:Genesis` | The genesis grant: root of change authority over one product (authority.md §2) | `…record: "genesis"`; `product` (the product IRI P), `holder`, `firstKey`. Founding: `by` is `holder`, `basedOn` is empty, signed by `firstKey`. Transfer: a new version of the same `id`, `by` the holder in force, superseding the version in force, naming the successor as `holder` |
| `sdlc:Transfer` | A genesis version naming a successor, pending until the successor's grant acceptance (§2.3) | as `sdlc:Genesis`, with `supersedes` the version in force and `holder` the successor |
| `sdlc:Grant` | A delegation of a scope from a grant the grantor holds (§3) | `…record: "grant"`; `parent` (the grant `id` it delegates from), `grantee`, `scope`, `mayDelegate: "yes"` (optional), `firstKey` (when the grantee has no key), `fallbackOf` (for a fallback, §2.4, with no `scope`). `basedOn` pins the parent's version |
| `sdlc:Scope` | A set of ontology classes, optionally narrowed to one element's `within*` subtree (§3.1) | `{classes: [class names], within: IRI, withinPath: [IRI, …, P]}`; the last two optional |
| `sdlc:mayDelegate` | Whether a grant may delegate (§3.2; Round 1, Q-8) | `…mayDelegate: "yes"`; absent means no |
| `sdlc:Fallback` | A grant that acts for its primary while the primary is unavailable, and never transfers (§2.4) | `sdlc:Grant` with `fallbackOf` equal to `parent` |
| `sdlc:GrantAcceptance` | The grantee's signed acceptance of a grant version. A grant is live only from it (§3.3) | `…record: "grant-acceptance"`; `grant` (the version's reference), pinned in `basedOn` |
| `sdlc:Revocation` | The end of a grant and of its chain below, from its position (§3.5) | `…record: "revocation"`; `revokes` (grant `id`), `under` (the revoker's grant `id`, above the revoked one) |
| `sdlc:Unavailability` | A filed interval in which a grant's holder does not act (§2.4) | `…record: "unavailability"`; `grant` (`id`), `from`, `until` (optional), `under` (when filed by a holder above) |
| `sdlc:Availability` | The holder's early end of an unavailability | `…record: "availability"`; `ends` (the unavailability's reference) |
| `sdlc:KeyBinding` | The opening, rotation or close of a holder's key in one product (§5.3) | `…record: "key-binding"`; `act` (`"add"`, `"rotate"`, `"close"`), `holder`, `key` (an `ssh-ed25519 …` public key line), `closes` (rotate), `since` (close, optional: a position), `under` (when by a holder above) |
| `sdlc:firstKey` | The key a grant, a founding or a transfer vouches for (§5.3) | `…firstKey`: a public key line |
| `sdlc:Attribution` | The naming of an identity as a machine, with the human responsible (§5.1) | `…record: "attribution"`; `machine`, `responsible` |
| `sdlc:Acceptance` | A human holder's signed acceptance of one or more decision versions under a grant (§4.1) | `…record: "acceptance"`; `grant` (the version's reference), `accepts` (references), `touches` (§4.2), `baseline` (optional, §4.3). `basedOn` pins every accepted version and the grant |
| `sdlc:touches` | The scope result recorded at signing: per decision, the items it touches (§4.2) | `…touches: {decision reference: [{class, element, path}]}` |
| `sdlc:BaselineEntry` | A known violation the acceptance takes the decision in force with: debt (§4.3; how.md D-6) | an element of `…baseline`: `{decision, subject, target}` |
| `sdlc:AcceptanceRevocation` | The withdrawal of an acceptance from its position (§4.6) | `…record: "acceptance-revocation"`; `revokes` (the acceptance's reference), `under` (when not by its signer) |
| `sdlc:Review` | A rejection or request for change, under a grant that could have accepted. No force (§4.5) | `…record: "review"`; `grant`, `reviews` (pinned), `verdict` (`"reject"`, `"request-change"`), `touches` |
| `sdlc:Waiver` | A signed answer to an open question that changes no decision, live until a header-clock time (§4.4) | `…record: "waiver"`; `grant`, `question: {decision, target, provenance}`, `expires`, `touches`. `basedOn` pins the decision and the grant |
| `sdlc:Refusal` | An attempted act the log refused, recorded with its reason (§5.1, §6.1) | not a record: an entry in its header's `refused`, `{ref, hash, reason}`, pinning the attempted record |
| `sdlc:Header` | One position of the positioned log (§6.1) | not a `dpp/1` record: `{system, position, clock, previous, records, refused, hash}`, hashed by the hash law |
| violation description | A decision's evaluable declaration of what violates it (§7; `DDD-dec-52`) | `…violation: {language, binds, text}` |

## 2. Computed, never recorded

| Term | Definition |
|---|---|
| `sdlc:inForce` | A decision is in force at a position iff authority.md §4.7 holds there |
| `sdlc:live` | A grant is live at a position iff it was accepted by its grantee, has not been revoked or closed, its grantee is not named a machine, and its parent is live |
| `sdlc:effectiveScope` | The intersection of a grant's scope with its chain's (§3.2) |
| `sdlc:needsReacceptance` | An acceptance signed by a key later closed with a `since` that reaches it, or by an identity later named a machine (§5.1, §5.3) |
| `sdlc:MachineIdentity` | An identity named by a live attribution |

## 3. Where Writ's terms meet these

As Writ's definition states them (`[D2]`, `[D2.5]`). The profile is the authority on force, and
Writ on enforcing it.

| Here | Writ |
|---|---|
| `sdlc:Genesis` | the genesis grant of a log, unscoped |
| `sdlc:Grant`, `sdlc:Scope` | a grant naming a holder and a scope; a scope as named graphs narrowed by a SHACL target. Here it is classes and a `within*` subtree, which `sh:targetClass` with a subtree filter expresses |
| `sdlc:Acceptance`, `sdlc:touches` | acceptance under grant; "scope is evaluated when the acceptance is signed and the result recorded with it" |
| `sdlc:BaselineEntry` | the baseline on an acceptance, by decision IRI and fact IRIs; G11 |
| `sdlc:Waiver` | a waiver with a review-by. Here it is a header-clock time, and Writ follows (Round 1, Q-6) |
| `sdlc:Attribution` | agent attribution, an agent identity mapped to the human responsible |
| `sdlc:Header` | a Varve commit header: the writer's clock, covered by the header hash (`[D2.3]`, `[D2.11]`) |
