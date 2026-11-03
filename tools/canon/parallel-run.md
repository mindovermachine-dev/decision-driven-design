# Parallel run: canon against the Python validators

The ledger `DDD-dec-102` and `DDD-dec-103` require: every comparison of `canon check --compare`
with the Python validators, every disagreement with its cause and fix, and the Varve version each
agreement was measured against. **Rows are never deleted.** A disagreement is a defect in one of
the two implementations. It is recorded here and fixed, and never suppressed, skipped or allowed
to fail.

How to read a comparison. Each case is a fixture under `scripts/fixtures/` or a live tree
(`core/claims`, `core/decisions`, `releases`), validated by both implementations. Two things are
compared:
- **the verdict:** Python's exit code against canon having any error;
- **the findings:** the multiset of (file, rule code, warning or not). Python's messages are mapped
  to rule codes by `Checks/PythonOracle.cs`. A message nothing maps to becomes `PY-UNMAPPED`, and so
  is never silently equal.

A case agrees only when both match. Rules no case exercises are listed, because they are not
compared.

## Retirement status (`DDD-dec-103`)

| Validator | First agreement (Varve A) | Re-measured after a bump (Varve B) | Retired by |
|---|---|---|---|
| `validate-claims.py` (claims) | `0.1.0-preview.15`, Gate 3 (below) | — | — |
| `validate-claims.py --decisions` | `0.1.0-preview.15`, Gate 3 (below) | — | — |
| `validate-releases.py` | `0.1.0-preview.15`, Gate 3 (below) | — | — |

No validator can be retired yet. Each needs a second full agreement after a Varve bump, and a
decision naming both versions. The release-head guard and the cut checks (`check-release-head.py`,
`ci.py`'s `release_cuts`) are git code in both implementations, not validators of the graph. They
are not in this comparison, and canon's tests cover them (`ReleaseTests`).

## Disagreements

| # | Found | Case | Python | canon | Wrong side | Cause | Fix |
|---|---|---|---|---|---|---|---|
| D-01 | 2026-11-03, run 2 | `releases/accept` (`v9.9.1.yaml`, `date: 2026-1-2`) | refuse: REL-DATE | accept | **canon** (and the fixture, which encoded the same belief) | canon's YAML typing read `2026-1-2` as a date and rendered it `2026-01-02`. PyYAML's implicit resolver reads a date without a time only with two-digit month and day; `2026-1-2` is a string, and fails `YYYY-MM-DD` | `Graph/YamlJson.cs` no longer types dates; a date PyYAML accepts reads as written. The accept fixture uses `2026-01-02`; a new refuse fixture `date-one-digit` pins the case; `GraphTests.PlainScalarsAreTypedAsPyYamlTypesThem` checks 30 scalars against PyYAML itself |
| D-02 | 2026-11-03, run 4 | `releases/refuse/duplicate-version` (two descriptors declaring `v9.9.27`) | REL-FILENAME on `v9.9.27-again.yaml`; one global REL-DUPLICATE-VERSION | REL-FILENAME, REL-TITLE-MISSING and REL-SUMMARY on `v9.9.27.yaml`; REL-DUPLICATE-VERSION | **canon** (its design, DESIGN.md §5.2) | The mapping gave each file the IRI of its id, so two files with one id merged into one node. That node had two titles, two summaries and two stems, and broke rules neither file breaks | Each file is its own (blank) node. The ruled IRI is kept as `canon:names` (`DDD-dec-107`). Duplicates are a SHACL-SPARQL constraint (another node of the class with the same id; for releases, both passing the header, as Python counts them). Repeats collapse to one `*` finding, as Python prints one line. `GraphTests` checks repeated claim and decision ids against Python |

## Runs

### Gate 3, final run: 2026-11-03

Varve `0.1.0-preview.15` (`Varve.Rdf`, `Varve.Turtle`, `Varve.JsonLd`, `Varve.Shacl`,
`Varve.Shacl.Sparql`). .NET SDK 10.0.403. Python 3.13 with PyYAML 6.0.3 (CI uses 3.11).
Base `1690418` plus the Gate 3 work, the commit that adds this file. Produced by
`canon check --compare --markdown`. **47 cases, every case agrees.**

| case | python | canon | findings (python / canon) | agree |
|---|---|---|---|---|
| `claims/accept` | accept | accept | 1 / 1 | yes |
| `claims/refuse/changed-zero.yaml` | refuse | refuse | 1 / 1 | yes |
| `claims/refuse/established-no-derivation.yaml` | refuse | refuse | 1 / 1 | yes |
| `claims/refuse/format-quoted.yaml` | refuse | refuse | 1 / 1 | yes |
| `claims/refuse/format-unsupported.yaml` | refuse | refuse | 1 / 1 | yes |
| `claims/refuse/id-malformed.yaml` | refuse | refuse | 1 / 1 | yes |
| `claims/refuse/kind-illegal.yaml` | refuse | refuse | 1 / 1 | yes |
| `claims/refuse/no-region.yaml` | refuse | refuse | 1 / 1 | yes |
| `claims/refuse/projected-no-falsifier.yaml` | refuse | refuse | 1 / 1 | yes |
| `claims/refuse/reported-no-evidence.yaml` | refuse | refuse | 1 / 1 | yes |
| `claims/refuse/retired-from-illegal.yaml` | refuse | refuse | 1 / 1 | yes |
| `claims/refuse/retired-from-on-live.yaml` | refuse | refuse | 1 / 1 | yes |
| `claims/refuse/retired-no-provenance.yaml` | refuse | refuse | 1 / 1 | yes |
| `claims/refuse/retired-no-retired-from.yaml` | refuse | refuse | 1 / 1 | yes |
| `claims/refuse/statement-empty.yaml` | refuse | refuse | 1 / 1 | yes |
| `claims/refuse/status-illegal.yaml` | refuse | refuse | 1 / 1 | yes |
| `claims/refuse/unrecoverable-no-notes.yaml` | refuse | refuse | 1 / 1 | yes |
| `claims (live: core/claims)` | accept | accept | 6 / 6 | yes |
| `decisions/accept` | accept | accept | 0 / 0 | yes |
| `decisions/refuse/empty-basedon.yaml` | refuse | refuse | 1 / 1 | yes |
| `decisions/refuse/no-basedon.yaml` | refuse | refuse | 1 / 1 | yes |
| `decisions/refuse/no-made.yaml` | refuse | refuse | 1 / 1 | yes |
| `decisions/refuse/no-principal.yaml` | refuse | refuse | 1 / 1 | yes |
| `decisions/refuse/no-resolution.yaml` | refuse | refuse | 1 / 1 | yes |
| `decisions (live: core/decisions)` | accept | accept | 0 / 0 | yes |
| `releases/accept` | accept | accept | 0 / 0 | yes |
| `releases/refuse/basis-empty` | refuse | refuse | 1 / 1 | yes |
| `releases/refuse/basis-entry-malformed` | refuse | refuse | 1 / 1 | yes |
| `releases/refuse/basis-not-list` | refuse | refuse | 1 / 1 | yes |
| `releases/refuse/commit-octal` | refuse | refuse | 1 / 1 | yes |
| `releases/refuse/date-malformed` | refuse | refuse | 1 / 1 | yes |
| `releases/refuse/date-one-digit` | refuse | refuse | 1 / 1 | yes |
| `releases/refuse/draft-null` | refuse | refuse | 1 / 1 | yes |
| `releases/refuse/duplicate-version` | refuse | refuse | 2 / 2 | yes |
| `releases/refuse/filename-disagrees` | refuse | refuse | 1 / 1 | yes |
| `releases/refuse/format-unsupported` | refuse | refuse | 1 / 1 | yes |
| `releases/refuse/format1-with-head` | refuse | refuse | 1 / 1 | yes |
| `releases/refuse/no-ratified-head` | refuse | refuse | 1 / 1 | yes |
| `releases/refuse/not-a-mapping` | refuse | refuse | 1 / 1 | yes |
| `releases/refuse/prerelease-quoted` | refuse | refuse | 1 / 1 | yes |
| `releases/refuse/summary-missing` | refuse | refuse | 1 / 1 | yes |
| `releases/refuse/title-blank` | refuse | refuse | 1 / 1 | yes |
| `releases/refuse/title-two-lines` | refuse | refuse | 1 / 1 | yes |
| `releases/refuse/title-version-prefix` | refuse | refuse | 1 / 1 | yes |
| `releases/refuse/unresolved-basis` | refuse | refuse | 1 / 1 | yes |
| `releases/refuse/version-malformed` | refuse | refuse | 1 / 1 | yes |
| `releases (live: releases)` | accept | accept | 0 / 0 | yes |
compare: rules exercised by the corpus: 39 of 45. Not exercised, so not compared: CLAIM-DUPLICATE-ID, DEC-DUPLICATE-ID, LOAD-JSONLD, LOAD-NOT-MAPPING, LOAD-YAML, REL-NO-CANON
compare: every case agrees

**Rules not exercised, so not compared** (6 of 45):
- `CLAIM-DUPLICATE-ID` and `DEC-DUPLICATE-ID`: the claims and decisions refuse cases are single
  files, so no case can hold two files with one id. Both are compared against Python instead by
  `GraphTests` (`ARepeated…IdIsOneFindingAboutTheSetAsInPython`), in temporary directories.
- `LOAD-YAML` and `LOAD-NOT-MAPPING`: Python's answer to a claim file that does not parse, or is
  not a mapping, is a traceback (exit 1), not a finding. The verdicts would agree, but there is no
  rule to compare. For releases, the non-mapping case is a finding in both (`REL-NOT-MAPPING`,
  exercised).
- `LOAD-JSONLD`: canon's own mapping failure; Python has no counterpart.
- `REL-NO-CANON`: needs a repository with no claims or decisions at all.

### Gate 3, earlier runs, kept

| Run | Cases | Agree | Notes (counts from the saved outputs of each run) |
|---|---|---|---|
| 1 | 13 (the corpus as it was) | 13 | Every case agreed. The fixtures exercised 7 of the 42 rules, so the agreement said little (predictions, P-16) |
| 2 | 43 (per-rule fixtures added) | 42 | D-01 |
| 3 | 44 | 44 | D-01 fixed; `date-one-digit` added |
| 4 | 47 | 46 | Fixtures for the empty basis, a duplicate version, a non-mapping descriptor; D-02 |
| 5 | 47 | 47 | D-02 fixed. A SPARQL escaping error in the new duplicate constraint made the release shapes fail to load once ("could not run", exit 2) before this run; it was fixed before any comparison ran |
