# Worked example: an ADR directory, and a system that rests on it

*Non-normative.* Two systems. The first is a directory of architecture decision records in a
repository, made conformant with `dpp/1` by adding JSON files, with no code and no server. The
second is a pricing rules engine whose fee rule rests on one of those ADRs. Every file named here
is in this directory, and `suite/run.py` checks the walk at the end.

## 1. The ADR directory as it was

```
payments-service/docs/adr/
  0002-amounts-in-minor-units.md
  0003-fees-in-settlement-currency.md
```

Two Markdown ADRs in the usual form. ADR-0002 was proposed on 2026-05-04 and accepted on
2026-05-11. ADR-0003 builds on it.

## 2. Choose an identifier and write the descriptor

The team picks a system identifier. It is a name the team controls, and need not serve anything:

```
https://git.example.internal/payments-service/docs/adr
```

It has a path, so if the team ever serves the directory over HTTPS, the files go directly under
that URL (spec §6.5). Until then, readers reach it as files, from a clone (§6.7).

`system.json`, at the top of the directory:

```json
{ "protocol": "dpp/1",
  "system": "https://git.example.internal/payments-service/docs/adr",
  "name": "payments-service ADRs" }
```

## 3. One JSON file per ADR version

Each record goes at `<id>/<version>.json`. The id is `ADR-0002`. The version is any token the team
likes. Here it is a plain counter, because the ADR changed once, from proposed to accepted, and a
change of `status` is a new version (spec §3.4).

`ADR-0002/1.json`:

```json
{ "protocol": "dpp/1",
  "id": "ADR-0002", "version": "1",
  "system": "https://git.example.internal/payments-service/docs/adr",
  "statement": "Store every monetary amount as an integer count of the currency's minor unit.",
  "by": "mailto:maria@example.internal",
  "at": "2026-05-04",
  "status": "proposed",
  "why": { "href": "../0002-amounts-in-minor-units.md" },
  "basedOn": [] }
```

`ADR-0002/2.json` is the same with `"version": "2"`, `"at": "2026-05-11"` and
`"status": "accepted"`. Version 1 stays where it is: published versions never change (§3.8).

- `at` is a date, because that is what an ADR knows (§3.4).
- `why` points at the Markdown instead of repeating it. The `href` is resolved against the
  record's own location, so `../0002-amounts-in-minor-units.md` finds the ADR whether the directory
  is read as files or served over HTTPS.
- `basedOn` is empty: ADR-0002 is an origin.

`ADR-0003/1.json` rests on the accepted version of ADR-0002:

```json
{ "protocol": "dpp/1",
  "id": "ADR-0003", "version": "1",
  "system": "https://git.example.internal/payments-service/docs/adr",
  "statement": "Charge EU card fees in the merchant's settlement currency.",
  "by": "mailto:maria@example.internal",
  "at": "2026-06-20",
  "status": "accepted",
  "why": { "href": "../0003-fees-in-settlement-currency.md" },
  "basedOn": [ { "ref": "ADR-0002@2@https://git.example.internal/payments-service/docs/adr" } ] }
```

The reference carries no `hash`. A person writing JSON by hand cannot compute one, and the spec
allows the omission (§4.2). The cost is that a walker cannot check that ADR-0002 version 2 is
unchanged; it relies on the directory's immutability (§3.8) and the repository's history.

Optionally, `ADR-0002/index.json` lists the versions (§6.4):

```json
{ "protocol": "dpp/1", "system": "https://git.example.internal/payments-service/docs/adr",
  "id": "ADR-0002", "versions": ["1", "2"] }
```

The directory is now a conformant system:

```
payments-service/docs/adr/
  system.json
  0002-amounts-in-minor-units.md
  0003-fees-in-settlement-currency.md
  ADR-0002/1.json
  ADR-0002/2.json
  ADR-0002/index.json
  ADR-0003/1.json
```

Nothing was installed, and nothing runs. A review checklist for the next ADR is: add
`ADR-NNNN/1.json` beside the Markdown, and never edit a published JSON file — add the next
version instead.

## 4. A second system references the ADR

The pricing engine applies fee configuration automatically. Its operator exports one record per
configuration revision into a directory (`pricing-engine/`), with identifier
`https://pricing.example.internal`. That identifier has no path, so if the engine serves its
records over HTTPS they live at `https://pricing.example.internal/.well-known/decision-provenance/`.

`pricing-engine/eu-card-fees/r42.json`:

```json
{ "protocol": "dpp/1",
  "id": "eu-card-fees", "version": "r42",
  "system": "https://pricing.example.internal",
  "statement": "EU card fee: 1.4% of the amount plus 25 minor units, in settlement currency, rounded half-to-even.",
  "by": "spiffe://example.internal/pricing-engine",
  "attributedTo": "mailto:finance-ops@example.internal",
  "at": "2026-10-21T06:00:00Z",
  "why": "Fee schedule FS-2026-11 approved by finance; applied as configuration revision r42.",
  "basedOn": [ { "ref": "ADR-0003@1@https://git.example.internal/payments-service/docs/adr",
                 "hash": "sha256:40f981f90c5251270df4e7570fdd6112c1254b6ed21307fb06086601f7803bfa" } ],
  "supersedes": [ { "ref": "eu-card-fees@r41@https://pricing.example.internal" } ],
  "org.example.pricing.rule": { "percent": "1.4", "fixedMinorUnits": "25", "rounding": "half-even" },
  "extensions": { "org.example.pricing.deployedTo": ["eu-west-1", "eu-central-1"] } }
```

- `by` is the engine's own workload identity: software made this decision. `attributedTo` names
  the team responsible (spec Appendix A, Q1).
- The engine is software, so it resolved ADR-0003 when it wrote the record and pinned it. The pin
  is the record hash of `ADR-0003/1.json`:

  ```
  python3 -c "import sys; sys.path.insert(0, 'reference'); import dpp; \
    print(dpp.record_hash(dpp.parse(open('example/payments-service/docs/adr/ADR-0003/1.json', 'rb').read())))"
  ```

  (run from `spec/decision-provenance/`).
- The rule's parameters are in a dotted member, so the pin covers them. They are strings, because
  hashed content holds no numbers (§5.2). The regions the rule is deployed to change without the
  decision changing, so they sit in `extensions`, outside the hash.
- `supersedes` names r41 without a pin and is not walked.

## 5. Walk from the fee back to the origin

A reader configured with both locations (`locations.json`, under `locations`):

```json
{ "https://git.example.internal/payments-service/docs/adr": "payments-service/docs/adr",
  "https://pricing.example.internal": "pricing-engine" }
```

walks from `eu-card-fees@r42@https://pricing.example.internal`:

| From | To | Result |
|---|---|---|
| *(start)* | `eu-card-fees@r42@https://pricing.example.internal` | held |
| `eu-card-fees@r42@…pricing…` | `ADR-0003@1@…/docs/adr` | held (pin verified) |
| `ADR-0003@1@…/docs/adr` | `ADR-0002@2@…/docs/adr` | held (unpinned); origin |

That is `expected-walk.json`, and `python3 suite/run.py` reproduces it. Had the reader not had a
clone of the repository, the second hop would read **not reachable**, and the walk would stop
there and say so. Had someone deleted `ADR-0003/1.json`, it would read **not held**. Had someone
edited it in place, the pin would no longer match, and it would read **not reachable** (pin
mismatch) — the case the pin exists to catch.
