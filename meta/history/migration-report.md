# Migration report — decision-driven-design (software projection)

Execution of the repo split (`DDD-dec-04..07`), DDD-repo side. Work is on branch
`claude/repo-split-execution-j46b1q`; **nothing is merged** — this report is for Emil's review before
merge. The principle-repo side is `migration-report.md` in `actor-indexed-determination`.

## Validation gate — status

| Gate | Result |
|---|---|
| DDD validator exit 0 including upstream checks against the `v5.0.0` ref | **PASS** (0 errors, 0 warnings; 7 pins resolved, 0 basis-loss) |
| Local claim/decision schema | **PASS** (7 claims, 7 decisions valid) |
| No file in both repos except intentional forks | **PASS with classification** (see the principle report §7) |
| `git log` shows moves + listed edits only | **PASS** |

Verbatim validator output is in §6.

## 1. Files removed (moved to the principle repo)

- `core/00-determination.md` … `core/10-the-floor-mechanism.md` (the numbered core docs) and
  `core/README.md` (replaced with a slim projection note).
- `core/assets/` (all reproduction scripts and figures).
- `core/claims/DDD-frame-*`, `DDD-measure-*`, `DDD-floor-01`, `DDD-agent-01` (the actor-general areas).
- `meta/lineage-and-limits.md`, `meta/CANON-PATCH-REGISTER.md`.
- `assets/conservation-principle.{html,svg}`, `i18n/ordliste-dansk.md` (moved whole).

## 2. Files kept (the software projection)

- `apparatus/` (all 7 docs + `assets/prefix-stability-check.py`), `applications/sdlc/`.
- `core/claims/`: `DDD-org-01..04`, `DDD-tool-01`, `DDD-sim-01..02` (projection-local areas).
- `core/decisions/`: `DDD-dec-01..07` (all — decisions are program acts and stay with the projection).
- `meta/`: `way-of-working.md`, `conversion-protocol.md`, `graph-tool-ontology.md`,
  `graph-tool-mvp.md`, `README.md`, `seed/`, and `consolidated-state.md` (rewritten — §3).
- `spec/claim-format.md`, `scripts/validate-claims.py`, `.claude/skills/claim-conversion/`,
  `CHANGELOG.md`, `PATCH-REPORT.md`, `RECONCILIATION-REPORT.md`, `LICENSE.md`, `.gitignore`,
  `migration/`.

## 3. Files created / reworked beyond pure removal

| File | What | Licence |
|---|---|---|
| `graph/upstream.yaml` | Cross-repo pins: `DDD-frame-01`, `DDD-measure-01`, `DDD-floor-01`, `term:closure/floor/conservation/seam-identity`, at `ref: v5.0.0` and each at its current upstream status (no drift). | package §3 (pinning spec, ids reconciled to the live graph per Emil's reply) |
| `validate-core-order.py` (fork) | Adds remote upstream resolution: shallow-clone the pinned ref into a temp dir (or `DDD_UPSTREAM_DIR` for offline/CI cache), then **E12** (pinned id missing upstream), **E13** (embedded canonical_md drift), **W5** (upstream status moved since `status_at_pin`). No live network fetch inside the checker. In this repo there are no numbered core docs, so it runs upstream-only. | kickoff step 5 (E12/E13/W5, remote resolution by shallow clone) |
| `applications/organizations/README.md` | Seeded from `DDD-org-01..04` — statements and falsifiers only, no new prose. | kickoff step 5; `DDD-dec-05` |
| `apparatus/the-skill-floor.md` | A representative `ddd:ref` block to the pinned upstream ids (`DDD-floor-01`, `term:floor`, `term:seam-identity`); the two dangling `apparatus/…` path refs in the opening line dropped. | kickoff step 5 ("convert in-text core references to `ddd:ref` markers") — see §5 |
| `meta/consolidated-state.md` | Rewritten to projection-local: org projection, the LinkedIn corrections (verbatim), the product backlog (verbatim), and a split note; shared/framework claims now resolve upstream. | package §2 (`consolidated-state` is `split`; each repo gets its own) |
| `core/README.md`, `core/claims/README.md` | Rewritten for the projection posture (areas `org`/`tool`/`sim`; canon is upstream and pinned). | the split |
| `README.md`, `CONTRIBUTING.md`, `CLAUDE.md` | Split banner; the where-issues-go split (falsification of core claims → principle repo; software/domain → here); agents told not to edit upstream core here. | kickoff step 7 (pointer updates, CONTRIBUTING split) |
| `.github/workflows/validate.yml` | On push to `core/`/`graph/`/`apparatus/`/`applications/`: local claim+decision schema, then upstream pins (needs a token for the private principle repo — §5). | kickoff step 6 (CI) |

## 4. The `ddd:ref` conversion — scope landed and flagged

Step 5 asks to "convert in-text core references to `ddd:ref` markers." The upstream **pins** and the
**checker** (E12/E13/W5) are fully in place and green, and a **representative** `ddd:ref` block is
landed (`apparatus/the-skill-floor.md`) so the doc-side path is exercised. **Not yet done, flagged:**
the many prose `core/NN` citations across `apparatus/`, `applications/`, and `meta/` were left as
prose. Converting every one to a pinned `ddd:ref` (and pinning any newly-referenced upstream id) is a
larger mechanical follow-up that does not affect the gate — the checker passes, and the pins that
carry the load-bearing dependencies (the floor, the measure, the split decision's basis) are in place.
**Recommend** a follow-up pass that walks every DDD doc's `core/NN` references and pins+marks them,
once the term-embed set upstream is completed (principle report §5).

## 5. Flags awaiting Emil

- **CI needs a secret for the private principle repo.** The upstream-check job clones
  `actor-indexed-determination`, which is **private**. GitHub Actions' default token cannot reach
  another private repo, so the workflow reads a secret `UPSTREAM_TOKEN` (a PAT / fine-grained token
  scoped to the principle repo, contents:read) and **skips with a warning** if it is absent (so the
  local schema checks still run). **Action:** add `UPSTREAM_TOKEN` as a repo secret, or make the
  principle repo readable to this repo's Actions (or make it public).
- **`v5.0.0` is currently a branch, not a tag** (the tag push is proxy-blocked — see the principle
  report). `graph/upstream.yaml` pins `ref: v5.0.0`, which resolves against the branch today. Once the
  real tag is pushed and the branch stand-in deleted, the pin resolves against the tag with no change
  here. The pin discipline ("tag, never a branch") is satisfied on paper and must be made true by the
  tag push.
- **Full `ddd:ref` conversion** is partial — §4.
- **`measure-paper-context.md` does not exist** in this repo (nor a `projections/` directory), so
  kickoff step 7's "measure-paper-context.md canon-source line" update is **not applicable**. Flagged
  in case the file lives outside the repo (a projection artifact); if so its canon-source line should
  point at `actor-indexed-determination@v5.0.0`.
- **Claim/decision placement** (which claims went upstream vs stayed here) is my call beyond the §2
  table — reasoning in the principle report §6.

## 6. Validator output, verbatim

### `validate-core-order.py core/` (upstream checks against v5.0.0)
```
  upstream  7 pins resolved against the pinned ref, 0 basis-loss warnings

upstream-only mode: 0 errors, 0 warnings
upstream: OK — every pin resolves at the pinned ref; no drift
```

E12 and W5 were verified to fire (a fake pinned id → `E12 … no longer exists upstream`; a mismatched
`status_at_pin` on `DDD-floor-01` → `W5 basis loss … pinned at 'projected'`), then reverted — the
check is not vacuous.

### Local schema
```
core/claims/      : valid: 7 claims, ids unique, format rules satisfied
core/decisions/   : valid: 7 decisions, ids unique, format rules satisfied
```

## Do not merge

Delivered on a branch for Emil's review. Nothing is merged.
