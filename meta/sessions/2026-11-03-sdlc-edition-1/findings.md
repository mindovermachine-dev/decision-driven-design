# Findings — sdlc edition 1, 2026-11-03

What happened against `predictions.md`, and what the work found. Readings not confirmed by Emil
are marked `UNVERIFIED — Emil review`.

## Predictions against outcomes

| # | Predicted | Outcome |
|---|---|---|
| P-0 | rebase onto `ca23241` clean; gates green; edition hash unchanged | **Held.** The charter commit was re-signed as `9287073`. "all gates passed", and the hash stayed `5b9878c0…84da` |
| P-1 | `DDD-dec-113` valid; 91 decisions | **Held.** "valid: 91 decisions, ids unique, format rules satisfied" |
| P-2 | `sdlc:mapsFrom` with `dct:source "move"`; closure one term up | **Held.** "every class and property carries its dct:source (122 terms)"; provenance `move 13, schema/ 33, § 76` |
| P-3 | the regime and the rule in the header; seven warnings; #50's five, E-7's three and E-8's three warnings; new edition hash | **Held, with one unpredicted split** (F-2). The edition hash is `sha256:a2006d9da588586bbf7ac19b3eec4861ff5a1aec0006a61784e9e0d842672f29` |
| P-4 | no violation anywhere; warnings 5, 5, 0; 19 self-tests | **Held, with 20 self-tests, not 19.** One self-test was added that P-4 did not list: "a directed context mapping, one source and one target raises nothing". It is the positive case for E-8, and a mapping shape that over-fires would fail it. The warning sets are exactly as predicted, by message and focus |
| P-5 | pinned graphs and vectors byte-identical; `vectors-5.json` 47 elements; the Domain, BC, Customer and Staff changed, plus one new element | **Held.** `git diff` is empty over `acme-shop.ttl`, `acme-shop-4.ttl`, `vectors.json` and `vectors-4.json`. `vectors-5.json` has 47 elements and graph hash `sha256:d5c54779062d2a8c6a7f60e38df496c415b19c3c0d09c177df3c4d41c49d1a97`. The changed hashes are exactly `…H5Y3FP9BFRZJ6QSS`, `…HKDH8MYYBGG3DBMA`, `…MMSAY8ZWD1TMMZ8HH` and `…YTKTBXP8KD0BQ2G0`; the one new element is `01M6R528AR7NHDH4S9NBMDRXR5` |
| P-6 | `what@3` frozen; `SCN@1`, `ACC-scn-what@1` and `what@5` written; one header; nothing published changes; 16 positions | **Held.** build.py: "67 records held, 3 written this run: SCN@1, ACC-scn-what@1, what@5". `put` refused nothing, so every published record is byte-identical. The log has 16 positions, and the verdicts are unchanged. **Not predicted:** `how-examples/README.md` and `authority.md` §9 stated "15 positions" and "61 items". They now say 16 and 66, `authority.md` §9 gains a row for p16, and both name `SCN@1`'s delta check |
| P-7 | `what.md` §7.2, §3.7, §3.4, §3.1, §2.3 | **Held.** Also the companions list and §1.3's table gained `acme-shop-5.ttl` and `DDD-dec-113`, which P-7 did not list |
| P-8 | product-cli's definition, D1.21 item 3, own commit | **Held** (`139fdb7`) |
| P-9 | `scripts/ci.py` green; CI `pipeline (devcontainer)` green; `agent review` pending on Emil | `scripts/ci.py`: "all gates passed". canon's C# gates were run locally and all pass: 66 tests, `changelog --check`, `issue-refs --basis` ("5 commits … Refs checked on 5") and `check --compare` ("every case agrees"). CI is recorded in `landing.md`'s report on #49 |
| P-10 | the descriptor commit, then the ratify commit; `releases` red between them, green after | **Failed at the first attempt** (F-7): after the ratify commit, `releases` stayed red, on the basis id pattern. After the fix the two commits were made again; their SHAs are in the report on #49 |

## Findings

- **F-1. pyshacl's `conforms` is false on warnings.** pyshacl reports `conforms: False` when the
  only results are `sh:Warning`. SHACL defines conformance over all results, whatever their
  severity. So "Described" (§7.2) cannot be read off a SHACL engine's `conforms` flag. It is "no
  result of severity `sh:Violation`". `what/check.py` computes it that way. product-cli's W1
  ("refuses on violations only") and Writ must do the same. This is stated in `what.md` §7.2 and
  in the `shapes.ttl` header.
- **F-2. Splitting the three property-shape warnings.** `emits`, `projects` and `rejects` each
  held a minimum and a type in one property shape. The minimum moves to `sh:Warning` under E-2.
  The type (`sh:class Event`, `sh:class Event`, `sh:class Invariant`) is a type boundary, and
  "existing violations are not demoted". So each became two property shapes: the minimum as a
  Warning with the old message, and the type as a Violation with a new message ("§3.2.0 A command
  emits only events.", "§3.2 A view projects only declared events.", "§3.3 A Decider's
  rejections are invariants."). The four SPARQL warnings became node shapes of their own, because
  a SPARQL constraint takes its shape's severity: `PatternConformanceShape`,
  `CommandCoverageShape`, `SurfaceCoverageShape`, and `ScopedViewShape` (already alone). Their
  messages are unchanged. `UNVERIFIED — Emil review`: the three new messages are the session's
  wording.
- **F-3. The context mapping under E-2's clause (reading R-b).** The directed form (one
  `mapsFrom`, one `mapsTo`) would violate the old `mapsTo` minimum of 2. That minimum is
  therefore counted over both edges, as a SPARQL Violation with the same meaning and its message
  extended. The new cardinalities are Warnings under the clause. `UNVERIFIED — Emil review`, as
  in `rulings.md`.
- **F-4. The test keys are checked out world-readable.** `ssh-keygen -Y sign` refuses a private
  key file with mode 0644, and git does not keep 0600. `how-examples/build.py` therefore fails in a
  fresh clone at the first new signature. Nothing was signed before this session, so no session
  met it. The keys were set to 0600 locally, which leaves no diff in git. The fix is not made
  here. Either `build.py` copies each key to a 0600 temporary file before signing, or the
  devcontainer sets the mode. Either is a successor item.
- **F-5. product-cli's definition still says what E-3 ruled otherwise.** Its dependency table
  lists "element hashes | product-cli's element-hash vectors offered as M-12's second
  implementation". E-3 rules them a further cross-check, not a substitute. The rows for #49 and
  #50 also read "open". Round 1 ruled only the fixture line for this PR, so neither is edited:
  they are product-cli's lines. Flagged for Emil.
- **F-6. #48 reconciles `what.md`.** This PR goes first, as ruled. Its `what.md` edits are local
  paragraphs:
  - §1.3, one table row;
  - the companions list;
  - §2.3, two paragraphs;
  - §3.1, two paragraphs;
  - §3.4 and §3.7, the shape citations;
  - §7.2, the regime and severities.

  #48 moves sections into `what-reference.md`, so whichever file holds each section on #48's side
  takes these.

- **F-7. The release validators refused a basis id of three digits.** Both
  `scripts/validate-releases.py` and canon's `release.shapes.ttl` matched a basis entry against
  `^DDD-[a-z]+-\d{2}$`. Decision ids passed 99 at DDD-dec-100, but no release had cited one, so
  `v0.6.0`'s basis (`DDD-dec-113`) was the first to meet the pattern. It was found after the
  descriptor and ratify commits (`2a0c778`, `4e7a019`): `scripts/ci.py` reported "v0.6.0: basis
  entry is not a DDD-<area>-<nn> id: 'DDD-dec-113'", and `canon check` failed with it.
  - **The fix.** `\d{2,}` in both implementations, and an accept fixture
    (`releases/accept/v9.9.2.yaml`, basis `DDD-dec-100`). With the old pattern restored, the
    fixture is refused; with the new one, it is accepted. `check --compare` reports "every case
    agrees". Claim ids keep their two-digit pattern, which `claim-format.md` and both validators
    share, and no claim id has passed 99.
  - **The history.** Rule 7 lets nothing but the descriptor change after the ratified head. So
    the branch was reset to `33bcd90`, before the descriptor, and force-pushed (this session's
    own branch, unapproved). The fix was committed there, and the two release commits were made
    again after it. `2a0c778` and `4e7a019` are not on the branch.

## Reconciliation

- **`main` moved once, before any canon change**, from `799cbe8` to `ca23241`. That is the canon
  CLI branch: DDD-dec-112, `graph/upstream.yaml`, `scripts/ci.py` and `validate-core-order.py`.
  Nothing under `applications/sdlc/` changed, so the session did not stop.
- **The rebase.** The charter commit was rebased and re-signed. `scripts/ci.py` was re-run ("all
  gates passed"), and the edition hash recomputed: unchanged at `5b9878c0…84da`.
- **Any later move of `main`** is recorded in the report on #49.

## The charter commit's first push

The first charter commit (`adaea45`) carried a co-author trailer naming a model. The charter
forbids that. It was amended to `f698a50` before anything built on it, and force-pushed to this
session's own branch. No other commit carries one.
