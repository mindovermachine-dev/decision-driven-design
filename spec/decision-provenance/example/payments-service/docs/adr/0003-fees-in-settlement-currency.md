# 3. EU card fees are charged in the settlement currency

Date: 2026-06-20

## Status

Accepted.

## Context

Merchants settled in SEK and DKK were charged fees in EUR and converted at a different rate than
their settlement, so their statements never balanced. Amounts follow ADR-0002.

## Decision

Charge EU card fees in the merchant's settlement currency, computed in minor units.

## Consequences

The pricing engine needs the settlement currency at fee time. Fee schedules are stated per
currency or as a percentage plus a fixed minor-unit amount.
