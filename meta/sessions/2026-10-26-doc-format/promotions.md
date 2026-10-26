# Promotions — doc format

Results stated in `apparatus/` and `applications/` that have no claim behind them, as ruled at GATE 1 (ruling 2). Each is `[OPEN]` until a later session files it and Emil rules. None is filed in this session.

A document resting on one of these names it in its `ddd:doc` block as `basis: [held:2026-10-26-doc-format/P-n]`. The `ddd:doc` check resolves the reference against this file. The warning clears when the `basis` entry is replaced by the filed claim's ID.

| ID | Result | From | Target canon | Priority | Note |
|---|---|---|---|---|---|
| P-1 | An actor's own output is not ground. | `apparatus/closure-principle.md` | upstream | 1 | Upstream `core/11` already relies on it in prose. It carries its own falsification section. |
| P-2 | Control decides the side of the encode/verify split. An observation of uncontrolled ground cannot be amortised across acts. | `apparatus/encode-verify.md` | upstream, extending `term:encode-verify-split` | 2 | Three documents rest on it. |
| P-3 | A tool call reallocates demand: exporter, resolver, verifier. The class belongs to ⟨tool, task, consumption⟩. Choosing tools is choosing the floor. | `apparatus/tool-surfaces.md` | here, `tool` area | 3 | `UNVERIFIED — Emil review`: may be actor-general. |
| P-4 | A skill without a per-invocation verifier is floor-exposed. | `apparatus/the-skill-floor.md` | here, `tool` area | 4 | A consequence of `DDD-floor-01`. |
| P-5 | A prompt prefix is a dependency chain; order by re-derivation rate over length. A prefix segment that keeps invalidating flags mislocated encoding. | `apparatus/prefix-stability.md` | here, new area | 5 | The ordering is arithmetic and its asset reproduces. The detector reading is the modelling claim. |
| P-6 | Pre-production predicates close over substitute ground. Progressive delivery should outperform fidelity. | `applications/sdlc/production-as-ground.md` | here, `delivery` area | 6 | Its §7 prediction is falsifiable and has nowhere to live. |
| P-7 | Poisoned ground can be a relation between true facts, not only a false fact. | `apparatus/adversarial-ground.md` | upstream, later | 7 | Held. The headline result is already canon in `term:poisoned-ground`. |
| P-8 | Tool classes (exporter, resolver, verifier) are meaningful only over pinned ground; unpinned, every class collapses toward exporter. | `apparatus/tool-contract.md` §1 | here, `tool` area | 3 (with P-3) | Registered at GATE 3, as pre-registered (prediction P1). Rests on P-3. |
| P-9 | A model that selects tools mid-run is structurally escape-exposed: the selection is an open decision, made under load, with no verifier. | `apparatus/tool-contract.md` §3.1 | here, `tool` area | 3 (with P-3) | Registered at GATE 3 (P1). An application of `DDD-floor-01`. |
| P-10 | A toolset fixed before the run makes the open decision set computable before the run. | `apparatus/tool-contract.md` §3.1 | here, `tool` area | 3 (with P-3) | Registered at GATE 3 (P1). |
