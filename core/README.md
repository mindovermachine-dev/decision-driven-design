# core/

<!-- ddd:charter
reader: canon contributors, and agents citing canon by ID
act: derive, cite and check a result against canon
opener: ddd:contract
authority: canon
exempt: []
-->

**Charter.** This folder is canon. Its numbered documents open with `ddd:contract`; claims and decisions follow `spec/claim-format.md`. It is the only folder in this repository whose documents carry authority (`DDD-dec-39`).

**This repository is the software projection.** The actor-general theory layer — the numbered core
documents `00`–`12`, the canonical term graph, and the per-act reproduction assets — is **canon in
the principle repository** (`actor-indexed-determination`) and lives there, not here. This directory
holds what is local to the projection's own graph:

- `13-cost-projection.md` … `17-time-and-assurance.md` — the projection's numbered core documents,
  numbered to continue the upstream reading order (upstream canon ends at `core/12`). `13` is the
  volume layer of the cost register: everything that quantifies over act volume, filed here under
  the boundary charter (upstream `DDD-dec-09`; `DDD-dec-10` here) — the principle layer is
  synchronic, and anything requiring persistence between acts files with the projection. `14` is
  the volume layer's dynamics (the maturation register), actor-general per R4b (`DDD-dec-11`).
  `15` is the routing model's worked instance, stipulated and reproducing. `16` is the calibration
  ledger — the claim layer's carrier-assurance instrument (`DDD-dec-13`). `17` is the time
  register of assurance: verdict-gap carriage, decay, accrual, and ground assurance with the recon
  substitution law.
- `claims/` — the projection-local claims (`org`, `tool`, `sim`) and the volume-denominated `cost`
  claims (`DDD-cost-04` relocated, `DDD-cost-06`/`07` split from the upstream per-act claims).
  Actor-general claims are pinned upstream in `graph/upstream.yaml`.
- `decisions/` — the program's decision nodes (`DDD-dec-01..07`, `DDD-dec-10`), including the split
  decisions. Decisions are volitional program acts; they live with the projection, not upstream.
- `graph/terms.yaml` — terms established by this repository's own documents (`act-volume`).
  Upstream terms are never duplicated here.
- `assets/` — computations backing this repository's reported claims (`measure-mdl-volume.py`,
  `measure-routing-example.py`); they must reproduce.

**Pending instance filings** (stubs, not canon until their evidence lands):

- *Benchmarks are licences (bounded)* — the rented-model reading of the instrument bound
  (upstream `DDD-cost-13`, pinned): eval scores as class certificates for actors nobody can
  interview, bounded to declared-predicate carriage. Files when its evidence lands; the
  open-class counterpart is the calibration ledger (queue item 2.12, pending). Stubbed at Wave 2
  GATE C (Emil, 2026-08-10).

The principle repo's canon is consumed by pin, not by copy: `graph/upstream.yaml` names every upstream
id this repository depends on, at a version and a status, and `validate-core-order.py` checks them
against a shallow clone of the pinned ref (basis-loss detection — `DDD-agent-01` applied to repos).
Pinned upstream ids satisfy `requires`/`ref` edges in local documents: upstream precedes every local
document in the reading order, so the cross-repo edge points backward by construction.
