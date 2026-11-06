# Predictions — sdlc edition 1, 2026-11-03

Written after Round 1 was ruled (`rulings.md`) and before any file it governs was changed. Each
outcome is appended under its prediction afterwards, never edited into it.

Not predicted: the reads at arrival and the Round 1 measurements (`bootstrap.md`, and the
Round 1 comment on #49). They changed nothing.

## P-0 — the rebase onto `main` at `ca23241`

`main` moved from `799cbe8` to `ca23241` (the canon CLI branch: DDD-dec-112, the upstream decision
pins, `scripts/ci.py` and `validate-core-order.py`). Nothing under `applications/sdlc/` changed, so
the session does not stop. Prediction: the charter commit rebases cleanly, `scripts/ci.py` prints
"all gates passed", and the edition hash is unchanged at
`5b9878c011cbab9c939c931c01421f8c5710c0c24b1cc07579716601274184da`.

## P-1 — `DDD-dec-113`, the decision record

One new file, `core/decisions/DDD-dec-113.yaml`, holding E-1 to E-8 as ruled, with
`basedOn` DDD-dec-63, -64, -73 and -91. Nothing it names is superseded: E-3 keeps DDD-dec-73
unchanged. Prediction: `validate-claims.py core/decisions/ --decisions` passes over 91 files
(90 on `main`). Falsifier: any error, or a count other than 91.

## P-2 — `ontology.ttl` (E-8)

One term added, `sdlc:mapsFrom`: an `owl:ObjectProperty`, domain `sdlc:ContextMapping`,
`dct:source "move"`. Prediction: `check.py`'s closure step reports one more term with its
`dct:source`, and its provenance note shows `move` up by one. The header names DDD-dec-113 beside
DDD-dec-64 for the "move" provenance. `owl:versionIRI` is unchanged (`…/sdlc/1`).

## P-3 — `shapes.ttl` (E-1, E-2, E-4, E-7, E-8)

- **The header** states the regime of E-1: the data graph is the What graph merged with
  `ontology.ttl`, in the default graph. Validation uses SHACL Core class semantics with
  SHACL-SPARQL, and no RDFS or OWL entailment. The header also states E-2's rule and its clause.
- **Severities (E-2).** `sh:severity sh:Warning` goes on the seven charted constraints:
  - pattern conformance;
  - `emits` min 1;
  - `projects` min 1;
  - command coverage;
  - `rejects` min 1;
  - the surface half of subject coverage;
  - scope coverage at the seam.

  The three property constraints carry the severity on the property shape itself, because
  `sh:severity` does not reach a node shape's property shapes. Every other existing constraint
  stays a Violation (Round 1's table), System `purpose` included (E-7).
- **The five shapes of #50 (E-4)**, as written there, at `sh:Warning`, each message citing its
  section.
- **E-7, three shapes at `sh:Warning`:**
  - Domain `purpose`;
  - Bounded Context `definition`;
  - Subject Kind `definition`.
- **E-8.**
  - `ContextMappingShape`'s `mapsTo` minimum of 2 becomes a SPARQL Violation over `mapsFrom`
    and `mapsTo` together: "connects two concepts".
  - Three Warnings (R-b): `mapsFrom` at most once; exactly one `mapsTo` when `mapsFrom` is
    present; "direction undeclared" when it is absent.
- **The edition hash** changes from `5b9878c0…`. Its new value is recorded in the outcome.

## P-4 — `check.py` (what)

- **Validation** runs `pyshacl.validate(what ∪ ontology, shacl_graph=shapes, inference="none",
  advanced=True)`: no `ont_graph`, and no RDFS.
- **"Conforms"** means no result of severity Violation. Warnings are collected as
  (shape message prefix, focus node) and compared, by name, with an expected set per example:
  - `acme-shop.ttl`: 5 warnings. They are the pair (Place order `…MCQ2R6MG31Q07DWMX`, Customer),
    Domain purpose (Ordering `…MYTKTBXP8KD0BQ2G0`), and Bounded Context definition (Ordering
    `…MH5Y3FP9BFRZJ6QSS`). The other two are Subject Kind definition, for Customer
    (`…MMSAY8ZWD1TMMZ8HH`) and Staff (`…MHKDH8MYYBGG3DBMA`).
  - `acme-shop-4.ttl`: the same 5.
  - `acme-shop-5.ttl`: none.
- **The planted defects** move to `acme-shop-5.ttl`, the one example with no findings. So a plant
  is caught by a result that the unplanted graph does not have, at the severity ruled for its
  shape. The seven existing plants are kept. Two of them, "a Decider with no rejection" and "a
  command no trigger issues", are now caught as Warnings, and the graph still conforms. The new
  plants:
  - five for E-4: #50's four, and a pair with no scenario;
  - three for E-7;
  - four for E-8.

  That makes 19 self-tests in all.
- **The M-12 note** no longer names `Hafeok/varve#192`. It says the route is Varve's published
  vectors (`vectors-varve.json`, DDD-dec-73). It records that product-cli's slice 0 found Varve
  `0.1.0-preview.15` reproducing `acme-shop.ttl`'s graph hash, and that product-cli's element-hash
  vectors would be a further cross-check.
- **`EXAMPLES`** gains `("examples/acme-shop-5.ttl", "vectors-5.json", …)`.
- Falsifier: an expected warning set that differs from the measured one, or a plant not caught.

## P-5 — the examples and vectors (E-5, E-7)

- **`acme-shop.ttl` and `acme-shop-4.ttl`**: not edited, byte for byte.
- **`vectors.json` and `vectors-4.json`**: not rewritten, because their graphs did not change.
  `--write-vectors` is written so that it writes only `vectors-5.json` (the charter: "only for the
  files E-5 changes").
- **New `acme-shop-5.ttl`** is `acme-shop-4.ttl` plus the following:
  - one scenario, minted with `mint.py`, within the Order Decider: "place an order as a
    customer". It has `sdlc:given ()`, a `when` of Place order as Customer with
    `lines 2`, `currency "DKK"` and the claim `customer_id "c-1"`, and
    `sdlc:thenEmit ( [ sdlc:event Order placed ] )`;
  - Ordering domain `purpose`;
  - Ordering bounded context `definition`;
  - Customer and Staff `definition`.
- **New `vectors-5.json`**: 47 elements (46 plus the scenario), and a new graph hash. These element
  hashes change: the Domain, the Bounded Context, Customer, Staff and the new scenario. The other
  42 equal `vectors-4.json`'s. The logic artefacts are unchanged, so the Decider's element hash is
  unchanged.
- The pyld cross-check stays open: no language tag, no control character.

## P-6 — the How examples

- **`build.py`.**
  - `what@3`'s edition hash, computed today from the files as held, is frozen as the literal
    `sha256:5b9878c0…84da` with a comment, as `what@2`'s was. Otherwise the published record would
    change, and `put` refuses that. `what@4` copies `what@3`'s edition and is unchanged.
  - New records:
    - `SCN@1`, a What change by the owner, anchored at the Ordering domain (the narrowest element
      covering the new scenario and the four elements that gain text). It `creates` the scenario,
      `changes` the Domain, Bounded Context, Customer and Staff, and carries a `delta` from
      `acme-shop-4.ttl` to `acme-shop-5.ttl` by sha256.
    - `ACC-scn-what@1`, accepted under `GRANT-what@2`, with its scope result read from the -5
      graph.
    - `what@5`, superseding `what@4`. It is based on WHAT-found@1, CUR@1 and SCN@1, carries
      `vectors-5.json`'s graph and element hashes, and names the edition hash as held.
  - One position is appended, p16, clocked `2026-11-13T09:00:00Z`, landing the three. The
    containment paths come from the -5 graph, which has the same parents for every existing element.
  - Written this run: those three records, and `log/acme.json` gains one header. Every published
    record is unchanged.
- **`check.py` (how).**
  - The What-version in force is `what@5`, checked against `vectors-5.json`.
  - "What in force" is WHAT-found@1, CUR@1 and SCN@1.
  - A delta check for SCN@1, as for CUR@1: it creates exactly the scenario and changes exactly the
    four elements.
  - The pins list gains `what@5` and `ACC-scn-what@1`.
  - The waiver line reads p15 explicitly rather than "the last position".
  - Scope results and the verdict base read the What in force (-5).
- **Verdicts and `expected.json`**: unchanged, because neither the scenario nor the descriptions are
  read by a How fact.
- **The log**: 16 positions.

## P-7 — `what.md` (E-1, E-2, E-4, E-7, E-8)

- §7.2 states the regime and the severity rule. "Described" counts violations only and reports
  warnings.
- §3.7's `[OPEN]` list is replaced by the shapes that now carry each check.
- §3.4 cites the state-justification and event-coverage shapes.
- §3.1 gains a paragraph on `sdlc:mapsFrom`, and a sentence on E-7's descriptions.
- §2.3 names `vectors-5.json` beside the others, and says the ontology never enters a hash.
- No section moves (#48 reconciles).

## P-8 — product-cli's definition (E-5), its own commit

`applications/sdlc/product-cli/product-definition.md` D1.21 item 3: the behaviour fixture becomes
`acme-shop-5.ttl` and `vectors-5.json`, with the amendment dated and cited (DDD-dec-113, E-5). No
other line changes.

## P-9 — the gates

`python3 scripts/ci.py` prints "all gates passed". CI's `pipeline (devcontainer)` passes on the
pushed head. `agent review` stays pending until Emil's `approve <sha>`: it cannot be green from
this session.

## P-10 — the release

- **Commit 1:** `releases/v0.6.0.yaml`, with `format: 2`, `prerelease: true`, no `ratified_head`,
  and basis DDD-dec-113, -63, -64, -72, -73 and -91. It goes with its `CHANGELOG.md` section,
  written by `canon changelog`.
- **Commit 2:** `canon ratify v0.6.0` fills `ratified_head` with commit 1.
- Between the two, the `releases` gate is red by design, because an unratified descriptor is
  refused. After commit 2 it is green.
- The summary's edition hash equals sha256 over `ontology.ttl` then `shapes.ttl` at that head.
