# 2. Amounts are integers in minor units

Date: 2026-05-11

## Status

Accepted (proposed 2026-05-04).

## Context

Two services stored amounts as binary floating point and disagreed by one cent on 0.3% of
reconciliations.

## Decision

Store every monetary amount as an integer count of the currency's minor unit (cents, øre, yen).
The currency's exponent comes from ISO 4217.

## Consequences

Arithmetic is exact. Display code formats; storage never does. Currencies whose exponent changes
need a migration.
