# Bootstrap — the authority profile, 2026-11-02

Filled in at arrival and committed with `prompt.md` and `plan.md`.

| Parameter | Value |
|---|---|
| Invocation | Interactive, from a Claude Code cloud session. The charter is Emil's message, carried verbatim in `prompt.md` |
| Principal | Emil (sole ratifier; ratifies by merging the pull request) |
| Upstream pin | per `graph/upstream.yaml`. Untouched by this session |
| Downstream base | `2b6e4a7`, head of `main` at arrival: the merge of PR #42. #42 is in, as the charter requires |
| Downstream branch | `claude/bold-franklin-i7b16g` (the branch the session was given), reset to `2b6e4a7` |
| Read only, as input | Hafeok/product-cli at `70395df`, `ledger/spec/ledger-protocol.md` §4.9–4.11, §5.4–5.7, §6. Hafeok/writ at `6737ac9`, `docs/product-definition.md` (Draft 2 through `[D2.9]`) |
| Gate | The plan (`plan.md`) waits for approval. Nothing else is written until it is ruled |
| Validators at arrival | `validate-claims.py core/claims/`: 31 claims, 6 warnings (the baseline). `--decisions`: 58 decisions. `dpp/1` suite: 65 passed, 0 failed. How checker, rdflib 7.6.0: 112 ok or note lines, 1 expected warning (the anchor self-test), 0 failures. What checker, pyoxigraph 0.5.13: 21 ok or notes; SKIP shapes (pyshacl not installed) and SKIP second implementation (pyld not installed), both SKIPs as in the move session |

## Next free decision id

**`DDD-dec-77`** at arrival. `main` holds up to `DDD-dec-73`. The unmerged branch
`claude/ready-to-try-2026-11-02` (head `87969b9`) holds `DDD-dec-74` to `DDD-dec-76`, so those
are taken. Upstream (`actor-indexed-determination`, every branch) holds up to `DDD-dec-39`.

**Amended by ruling R-14 (2026-11-02, `rulings.md`): `DDD-dec-85`.** After arrival,
`claude/ready-to-try-2026-11-02` (PR #43) filed `DDD-dec-77` to `-82` and `-84`, and `-83` is
recorded as never used. This session's provisional 77 and 78 moved to 85 and 86, and the planned
supersessions to 87 to 91. The re-check R-14 asks for was run on every branch of both
repositories before the move: downstream holds 74 to 82 and 84, all on that branch; upstream
holds up to 39.

## Arrival findings — reported, not acted on

Each is a place where the charter's premises and the sources disagree, or where the charter
leaves a choice the plan cannot make alone. The repository and the sources win. Each is carried
into `plan.md` as a question or as a departure.

1. **`acceptedBy` and `acceptedAt` are not protocol members.** The charter calls them "the
   protocol's optional `signature`, `acceptedBy`, `acceptedAt`". `dpp-1.md` Appendix A, A-10,
   removed the last two: "a system that distinguishes deciding from accepting records acceptance
   as its own decision record (based on the accepted one)". `how.md` §9.4, D-6, already asked the
   profile to map them to the acceptance record's `by` and `at`, and the How examples do this.
   Only `signature` exists, and it is optional in the protocol. This does not reopen the ruling.
   It is how the ruling can be met without inventing an undotted member, which §3.7 forbids. → plan F-1.
2. **`extensions` is unhashed and unsigned.** The charter puts "what the protocol does not
   define" in `extensions`. `dpp-1.md` §3.7 and §11.3: `extensions` is outside the canonical form,
   so it is outside the pin and outside the signature, and a system "MAY add to or change
   `extensions` after publication without creating a new version". A grant's grantee and scope,
   or an acceptance's baseline, held there could be changed after the grantor signed, with every
   pin and signature still valid. §3.7 names the place for content a pin must cover: a dotted
   member. `how-vocabulary.md` already puts authority fields in the hashed dotted member
   `dk.decision-driven-design.authority`. → plan F-2, a proposed departure.
3. **`[D2.11]` is not in Writ's repository.** Hafeok/writ at `6737ac9` carries the definition
   through `[D2.9]`. The move session recorded that the repository lags the definition by
   `[D2.10]` to `[D2.12]` (Round 4, ruling 4). The requirement the charter cites `[D2.11]` for,
   "header clock covered by the header hash", is in `[D2.5]`'s provenance-conformant class at
   `6737ac9`. `[D2.11]`'s own text is not available to this session. → plan F-3.
4. **Writ's `[D2.3]` makes a waiver's review-by a position, not a time.** "Anything the vocabulary
   can express as a position rather than a date is a position (a waiver's review-by is)". The
   charter's question 6 lists waiver expiry among the evaluations that read header clocks. Both
   can hold: an expiry stated as a header-clock instant is evaluated at each position against that
   position's header. They are not the same rule. → plan Q-6.
5. **Writ accepts a grant on the grantor's side.** `[D2]`: "A grant is itself a decision:
   proposed, reviewed, accepted by a holder whose own grant covers the authority graph". The
   charter's question 1 adds the grantee's acceptance (the ledger's `gacc`). These are two
   signatures, not one, and the plan says which is which. → plan Q-1.
6. **Delegation depth is not ruled.** The genesis ruling says every other grant delegates from the
   genesis "directly or through a chain". Whether every holder may delegate, and how wide, is not
   ruled. The ledger's escalation guard (LP-6.23: "below the genesis a grantor gives only its own
   role") is input, not authority. → plan Q-8, a new question.
7. **Transfer and revocation interact.** A genesis transfer "closes" the prior holder's grant. If
   closing were revocation, then under question 2's cascade every grant delegated from the genesis
   would fall at every transfer. → plan Q-2.
8. **The How examples' authority records are stand-ins.** `GEN@2`, `GRANT-what@1`,
   `GRANT-how@2`, `ACC-1@2` and `ACC-what@1` carry scopes as words (`"what"`, `"how"`), no grant
   acceptance, no key binding and no position. None is valid under any profile that answers
   questions 1, 3 and 6 as proposed. → plan step 4, and Q-9 (where the worked example lives).
9. **`DDD-dec-47` is the decision that names the three fields.** The charter lists `-46`, `-54` and
   `-64` for supersession. `DDD-dec-47` is where "signature, acceptedBy and acceptedAt required"
   is stated, and finding 1 changes how it reads. → plan step 6.
10. **M-1 names two more items.** The move session's successor item M-1 gives the profile the
    violation-description field (`DDD-dec-52`) and attestations (`what.md` §3.2.3). The charter's
    deliverables name neither. → plan Q-10.
