# core/claims/

The claim graph as files: one YAML file per claim node, `DDD-<area>-<nn>.yaml`, each declaring
`format: 1` per `spec/claim-format.md`. These files **are** the graph and grep is the query engine.

Canon authority for a converted claim lives here, not in the prose it was extracted from. Where a
document and its claim disagree, the disagreement is a bug in the prose — flagged in the claim's
`notes:`, not silently harmonised (`meta/conversion-protocol.md`).

**Areas held here (the software projection):** `org` (organisation-design projection), `tool` (the
graph tool), `sim` (the tool's predictive models), `flow` (how demand arrives in a process and who
may order it, scoped to the PDLC: `DDD-flow-01`…`04`, `DDD-dec-118`), and the volume-denominated `cost` claims
(`DDD-cost-04` relocated whole, `DDD-cost-06`/`07` split from the upstream per-act claims — the
boundary charter, upstream `DDD-dec-09` / `DDD-dec-10` here). The actor-general areas — `measure`,
`frame`, `floor`, `agent`, and the per-act `cost` claims — are **canon in the principle repository**
(`actor-indexed-determination`) and are pinned, where this repo depends on them, in
`graph/upstream.yaml`. New areas are cheap; renumbering is forbidden; retired claims keep their IDs;
IDs travel with their claims when a claim relocates and are never reused.

**Flags awaiting Emil review.** The org and sim predictions and the tool claim are **projected**
and **session-authored** (`UNVERIFIED — Emil review` in `notes:`) — flagged, never struck, and never
presented as canon. The `flow` claims are the same: **projected**, **session-authored**,
`UNVERIFIED — Emil review` in `notes:`, and scoped by `region` to the PDLC only. Their generality is
not claimed; promoting any of them upstream waits on a second process mapped with method step 1b
(`DDD-dec-118`). The `cost` claims are not so flagged: they entered through the ratified canon
sessions (statuses as filed; `DDD-cost-06` reported as arithmetic).

**Validate:**
- `python3 scripts/validate-claims.py core/claims/`
- `python3 scripts/validate-claims.py core/decisions/ --decisions`
- `python3 validate-core-order.py core/` (resolves `graph/upstream.yaml` against the pinned ref)
