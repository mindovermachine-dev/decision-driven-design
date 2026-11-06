rule #49 and #50, and ship `sdlc:` edition 1 (decision-driven-design)
You work in `mindovermachine-dev/decision-driven-design`. This session holds Emil's signing key, so every commit is signed and must verify on GitHub.
What this session is for. product-cli's step 1 pins `sdlc:` edition 1. It cannot start until three things are true:

* #49 is ruled: the validation regime, and the split between refusals and findings;
* #50 is ruled: the five §3.4 and §3.7 shapes that `shapes.ttl` does not yet have;
* the edition is shipped under a signed tag.

This session prepares all three for Emil to rule, applies his rulings, and stops at a green head. Landing and cutting the release are Emil's.
Stop and ask before you start if `applications/sdlc/what/ontology.ttl` or `shapes.ttl` has changed on `main` since `c7424ad`. The evidence in #49 and #50 was produced against those files.
PR #48 also edits `applications/sdlc/what.md` (readers' edition, DDD-dec-94 and -95). If it has landed, build on it. If it is still open, ask Emil whether to wait for it or go first. The second to land reconciles `what.md`.
Read first

1. `AGENTS.md`, `CONTRIBUTING.md` and `meta/way-of-working.md`. They cover:
   * the claim graph;
   * the `Basis:` rule;
   * `Refs #N`, which must name an issue in this repository;
   * landing with `canon`.
2. `spec/claim-format.md`, for decision records. `spec/release-format.md`, format 2, including port note 4 on the order of release commits.
3. Issues #49 and #50 in full. They carry the evidence and the proposed shapes.
4. `applications/sdlc/what.md`:
   * §2.3, versions and the hash law;
   * §3.3 and §3.4;
   * §3.7, the `[OPEN]` list;
   * §7.2, conformance.
5. `applications/sdlc/what/ontology.ttl`, `shapes.ttl`, `check.py`, `mint.py`, `vectors.json`, `vectors-4.json` and both examples.
6. `applications/sdlc/how-examples/build.py` and `check.py`, which pin the edition hash in the What-version records.
7. `core/decisions/DDD-dec-63`, `DDD-dec-64`, `DDD-dec-72` and `DDD-dec-73`.
8. `applications/sdlc/product-cli/product-definition.md`, D1.19 to D1.21: what product-cli expects from this edition.
9. The most recent session folder under `meta/sessions/`, for the shape of `prompt.md`, `rulings.md`, `predictions.md`, `findings.md` and `landing.md`.

Round 1: proposals for Emil to rule
Open the session folder `meta/sessions/2026-11-03-sdlc-edition-1/`, holding this prompt verbatim as `prompt.md`. Post Round 1 as a comment on #49 and wait. Write no canon before the rulings.
Each proposal states its alternatives, and a recommendation drawn from the product-cli project:

* E-1, the validation regime (#49 §1).
   * The data graph of a validation is the What graph merged with the edition's `ontology.ttl`, in the default graph.
   * It uses SHACL Core class semantics with SHACL-SPARQL, and no RDFS or OWL entailment.
   * The ontology is never part of a What graph's hash or of its export.
Recommended as proposed. pyshacl and Varve's `Varve.Shacl` agree on both examples under this regime.
* E-2, severities as a principle (#49 §2).
   * A shape is `sh:Warning` when it can only hold once an element authored later exists, later in phase order or in a later write. It is `sh:Violation` when it concerns an element's own form, identity or type boundary.
   * Under that rule these become warnings:
      * pattern conformance (§3.2.0);
      * "a command emits at least one event";
      * "a view is built from at least one event";
      * command coverage (§3.3);
      * Decider justification (§3.4);
      * subject coverage, surface half;
      * scope coverage at the seam.
   * Classify every other shape in `shapes.ttl` by the same rule. List each shape with its severity in the round, and flag any that is unclear.
   * Conformance ("Described", §7.2) counts violations only, and reports warnings.
Recommended: the principle, so that shapes added in later editions are classified the same way. The alternative is to rule the list alone.
* E-3, M-12 (#49 §3).
   * Correct `check.py`'s stale reference: `Hafeok/varve#192` is the regex timeout, not the vectors.
   * Name product-cli's element-hash vectors, due at its step 2, as M-12's second implementation.
   * Record that Varve's `RdfCanonicaliser` already matches both examples' graph hashes.
Recommended as proposed.
* E-4, the five shapes (#50). Add the five shapes as written in #50, at `sh:Warning`:
   * subject coverage for triggers;
   * subject coverage for (command, subject kind) pairs;
   * claim justification;
   * Projector event coverage;
   * state justification.
`what.md` §3.7's `[OPEN]` list is emptied, and §3.4 cites the new shapes. Recommended as proposed.
* E-5, the example gap (#50). `acme-shop-4.ttl` has no scenario for (Place order, Customer). It is product-cli's behaviour fixture, so it should carry no findings.
   * Recommended:
      * add a scenario, minted with `mint.py`, within the Order Decider: given nothing, when Place order is issued as Customer, then Order placed;
      * regenerate `vectors-4.json`;
      * leave `acme-shop.ttl` unchanged. Product-cli's slice 0 pins its graph hash. Assert its one expected warning by name in `check.py`.
   * The alternative is to leave both examples as they are, with the warning asserted.
* E-6, how edition 1 ships. DDD-dec-72 says "the tag that ships it".
   * Recommended:
      * release `v0.6.0`, format 2, cut by Emil with `canon release`;
      * its `basis` names this session's decision, plus DDD-dec-63, -64, -72 and -73;
      * its summary names `owl:versionIRI <https://decision-driven-design.dk/ns/sdlc/1>` and the edition hash: sha256 over `ontology.ttl` then `shapes.ttl`, as tagged;
      * before the descriptor is written, `ontology.ttl` and `shapes.ttl` must carry no `[PROPOSED]` or `UNVERIFIED` marker. From the tag on, the edition is read-forever.
   * The alternative is a separate tag such as `sdlc/1`. It would be a second artefact naming the same files.
* E-7, every box says what it is (P-C1 of the product-cli project's `what-c4-proposals.md`, raised by the workbench design). No new terms. Add `sh:Warning` shapes:
   * a Domain and a System carry `sdlc:purpose`;
   * a Bounded Context and a Subject Kind carry `sdlc:definition`, in business language, as an Entity does.
Recommended now, in edition 1. It is additive and warning-only, so it costs nothing to carry now. After the tag it would need an edition 2.
* E-8, a context mapping has a direction (P-C2). Add `sdlc:mapsFrom`, with `sh:maxCount 1`.
   * When `mapsFrom` is present, `sdlc:mapsTo` has exactly one value. The mapping reads: the concept in `mapsFrom` corresponds to the concept in `mapsTo`, and `mapsFrom`'s meaning is the source.
   * A mapping without `mapsFrom` is a `sh:Warning`, "direction undeclared".
   * DDD's strategic pattern kinds (Customer–Supplier, Conformist, Anticorruption Layer and the rest) are not proposed. They describe teams or realisation, not meaning, and belong in Writ as How decisions.
Recommended now, in edition 1, for the same reason as E-7. It is the only new term in this session, so it adds an `ontology.ttl` change and a `what.md` §3.1 paragraph.

The proposal file's two open questions, Q-C1 (where an external trigger enters) and Q-C2 (outside systems with no What), are not for this session. Leave them open.
Record Emil's answers verbatim in `rulings.md`. Then write `predictions.md` before you change anything: which `check.py` lines change, which vectors and which How records you expect to regenerate, and why.
After the rulings: one PR, `Refs #49` and `Refs #50`

1. The decision record. It takes the next free `DDD-dec-NNN` in `core/decisions/`, holds E-1 to E-8 as ruled, and passes `python3 scripts/validate-claims.py core/decisions/ --decisions`.
2. `shapes.ttl`, and `ontology.ttl` for E-8.
   * Severities per E-2.
   * The five shapes per E-4, and the E-7 and E-8 shapes as ruled.
   * `sdlc:mapsFrom` in `ontology.ttl`, with `dct:source "move"`, if E-8 is ruled.
   * Planted defects in `check.py` for each new shape, and both examples asserted against their expected warnings. E-7 will likely add warnings to the examples. Either fill in the missing `purpose` and `definition` values, which regenerates vectors, or assert the warnings by name. Ask in Round 1 which.
   * Each `sh:message` cites its section.
   * The header states the validation regime per E-1.
3. `what.md`. The regime goes in §2.3 or §7.2, whichever the rulings say. §3.7's `[OPEN]` list is replaced. §7.2 counts violations only.
4. `check.py`.
   * It runs with `inference="none"` over `what ∪ ontology`.
   * "Conforms" means no violation. Warnings are listed and compared, by name, with an expected set per example.
   * Each new shape gets a planted defect, and the self-test catches it.
   * The M-12 note is corrected per E-3.
5. The example and the vectors, per E-5. Run `check.py --write-vectors` only for the files E-5 changes.
6. The How examples. A new What-version supersedes the last one, with the new edition hash and, if E-5 changed `acme-shop-4.ttl`, its graph. Follow the pattern by which `what@2` and `what@3` were added.
7. Gates. `python3 scripts/ci.py` prints "all gates passed", and so do the repository's C# gates in CI. `findings.md` compares the predictions with what happened.
8. The release, last, per port note 4 of `release-format.md`:
   * one commit: `releases/v0.6.0.yaml`, with `format: 2` and no `ratified_head`, together with its `CHANGELOG.md` section. That commit is the ratified head;
   * one commit: `ratified_head` filled with `canon ratify v0.6.0`.
9. `landing.md` for Emil, written as the protect-main session's was:
   * approve the head by hand (`approve <sha>`);
   * `canon land <pr>`, wait for green, then `canon land <pr> --main`. A head with a descriptor lands on `land/release-v0.6.0`;
   * `canon release v0.6.0`;
   * check that the tag verifies, and that the edition hash computed at the tag equals the descriptor's.
10. Product-cli's pin. Comment on #49 and #50 with:
   * the tag, once cut;
   * its commit;
   * `owl:versionIRI`;
   * the edition hash.
Product-cli's step 1 session pins exactly these.

Rules

* Commit identity: `Claude (Emil) <claude+emil@okkels-klein.dk>`, signed.
* Every commit carries:
   * `Refs #49`, `Refs #50`, or both;
   * a `Basis:` line naming the decision IDs it rests on;
   * no model name in any message, trailer or record.
* Flag, don't guess. Any reasoning Emil has not confirmed is marked `UNVERIFIED — Emil review`. Nothing marked that way may remain in `ontology.ttl` or `shapes.ttl` when the descriptor is written.
* Ask, don't absorb. No change to an accepted decision's meaning. If a ruling needs one, stop and ask.
* Hands off product-cli, Varve and Writ.
* Do not land, merge or tag. Stop at a green head and report.

Done when

* The PR's head is green, with every check passing (`pipeline (devcontainer)` and `agent review`).
* Every commit verifies. Paste the API result for each SHA.
* `landing.md` is in the session folder, and the report on #49 names the head SHA for Emil's approval.

Report:

* the head SHA;
* each commit's verification;
* the computed edition hash;
* the regenerated files, with the reason for each;
* any deviation from this prompt, with its reason.

Reconciliation
If `main` moves while you work:

* rebase;
* re-run every gate and recompute the edition hash;
* record the reconciliation in `findings.md`.

If the change on `main` touched `applications/sdlc/what/`, stop and ask.
