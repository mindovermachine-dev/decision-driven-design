# Successor items — housekeeping session, 2026-10-26

Carried forward from the act address landing's list, renumbered nowhere: the S-numbers are the
landing session's and stay stable. Items this session closed are marked; the rest are `[OPEN]`.

| # | Item | State after this session |
|---|---|---|
| S-1 | Release-head guard | **Closed.** Built upstream as `DDD-dec-39` (format 2, `ratified_head`, rule 7, `scripts/check-release-head.py`, both workflow hooks). First instance: `v5.15.2`. |
| S-2 | T2b, the first Phoenix slice | `[OPEN]`. Its own session, after the bump to `v5.15.2`. Carries F-1, the escalation-rule anchoring, the reading/verdict-input line. The address flags and F-3's provisional ruling wait on it. |
| S-3 | Seam decay's canonical home | `[OPEN]`. Unchanged. `DDD-address-03`'s flag waits on it. |
| S-4 | The behaviour term | `[OPEN]`. Unchanged. `DDD-address-05`'s dependency and `DDD-address-01`'s K5 rationale wait on it. |
| S-5 | Glossary pass (act, act occurrence, act-site, ground axis) | `[OPEN]`. Not taken: Emil's act, and no release this session needed it. Rides with the next upstream release that touches the glossary. |
| S-6 | Held dry-run findings F-1, F-2 | `[OPEN]`. F-1 carried into S-2; F-2 ruled after T2b. |
| S-7 | The `repo:` URL | **Closed.** `graph/upstream.yaml` names `mindovermachine-dev`; 74 pins verified through the new URL. |
| S-8 | Decision pinning for `basedOn` | `[OPEN]`. Low priority, unchanged. `DDD-dec-40`'s basedOn `DDD-dec-39` is the third unpinned upstream decision reference. |
| S-9 | The `term:act` relation in `DDD-ground-06` | `[OPEN]`. Unchanged. |
| S-10 | Stale upstream PR #3 | **Closed.** Closed 2026-10-26 with the ruling in its comment; branch left in place. |

New this session:

| # | Item | What it needs |
|---|---|---|
| H-1 | **The bump.** | **Closed.** PR #26 merged (`084bce7`), `v5.15.2` cut under the guard, ref → `v5.15.2` with hashes untouched. Observed: 74 pins resolved against the pinned ref, 0 basis-loss, 0 content-drift, 1 shadowed id(s). Prediction held in every limb; recorded in `DDD-dec-40`. |
| H-2 | **The three address review flags.** `DDD-address-01` (two), `DDD-address-03` (one). | Ruled together when S-3 and S-4 land. |
| H-3 | **The org-03 / org-04 two-limb warnings.** The validator flags both statements as joining two limbs. | Adjudicate (split or keep) at the next canon session that touches the org set; not a housekeeping edit, since a split mints an id. |
