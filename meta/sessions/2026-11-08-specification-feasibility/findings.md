# Findings — specification feasibility, 2026-11-08

What the session found while filing. Nothing here is ruled.

## F-a. Feasibility had no home

At arrival, "feasibility" appeared in no file of `applications/sdlc/`, in product-cli's definition,
or on any branch's session record after 2026-10. The What had inbound external actors (external
subject kinds, What §3.7) and crossings to other products (Translations, §3.0.1), but nothing for
an outbound dependency on a source outside any product.

## F-b. The rulings touch an open question of DDD-dec-113

`DDD-dec-113` keeps Q-C2 open: "outside systems with no What". A ground-sourced bounded context
(DDD-dec-116, F-8) is a What-side answer for sources that are vetted. It does not decide whose What
holds the context when the source belongs to no product. That is rulings.md O-1, left open.

## F-c. product-cli's authority was removed, not missing

The Rust tool at `rust-final` had grants, grant acceptance, roles and authoring scopes. The rewrite
dropped them by `[D1.11]`. DDD-dec-117 restores the capability; it does not invent it. Emil's
remark that it is "already built into product-cli" matches `rust-final`, not the rewrite's `main`
at `4ce90e9`.

## F-d. A parallel branch touches the same ground

`claude/sdlc-pdlc-applications-0u6318` (session `2026-11-07-sdlc-and-pdlc`, unlanded) adds an
SDLC specification with demand kinds and entry points to `applications/sdlc/`. It holds
`DDD-dec-114` and `DDD-dec-115`. This session edits no file that branch edits, except
`meta/sessions/README.md` (one row each). Applying DDD-dec-116 to the What should be sequenced
after that branch lands, or reconciled with it. *It has since landed (F-g).*

## F-e. Id correction

Claude said in the conversation that the next free id looked like `DDD-dec-120`. `DDD-dec-116` to
`-119` appear on `main` only inside a range checked free in `2026-11-03-protect-main/bootstrap.md`.
The session took 116 and 117 (`bootstrap.md`).

## F-f. The CI environment

`scripts/ci.py` needs `ssh-keygen` and the release tags. This cloud workspace had neither at first.
See predictions.md P-2.

## F-g. Rebased onto main at 80e9088 (2026-11-09)

`2026-11-07-sdlc-and-pdlc` landed, with 23 commits after it, ending at `80e9088`. The branch was
rebased onto it. The only conflict was `meta/sessions/README.md`, resolved by keeping both rows.
No new decision id was filed on any branch, so `DDD-dec-116` and `DDD-dec-117` stand. On the new
`main`, `[D1.11]` still stands in `product-definition.md` at §1, W10 and §8, so DDD-dec-117's
supersession is unchanged.

## F-h. DDD-dec-114's owners meet DDD-dec-116 and DDD-dec-117 — UNVERIFIED — Emil review

DDD-dec-114, now landed, makes the What, When and How owners scopes under the genesis grant, each
held by a grant. Two readings follow, neither ruled:

- DDD-dec-117's role ("a named, reusable scope") fits these owner scopes. The three owners may be
  the first roles, not a separate mechanism.
- DDD-dec-116 F-2 says the How decides feasibility. The natural holder of the vetting grant is then
  the How owner, or a holder of a grant under the How scope.

Both go to S-5 and S-3 as input. The decisions themselves are not changed.
