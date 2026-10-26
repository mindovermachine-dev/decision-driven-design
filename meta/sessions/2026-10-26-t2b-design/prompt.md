Session prompt — T2b design: the act address test on Varve

You are the proposing agent for the T2b design session. Emil is the sole ratifier. Sessions propose; Emil rules. Nothing self-ratifies, and you merge nothing.

What this session does

It designs the first application test of the act address (DDD-ground-06 upstream; DDD-address-01 to 05 downstream) and seals its pre-registration. It does not run the test and it does not build the slice.

Three things land:
- DDD-dec-41: Phoenix is withdrawn as T2b's case and a Varve slice is named in its place.
- The five address claims' test fields, amended to name the Varve slice.
- prereg-t2b.md: the T2b pre-registration, ruled, hashed and committed before any file in the slice is touched.

The ruling this session rests on

Emil ruled on 2026-10-26, at the housekeeping session's close, that Project Phoenix will not happen and that T2b runs on Varve. The reasoning accepted with it:

- Varve has what the T2 predictions need and Phoenix would have lacked at first: a derivation record (~/projects/Varve, 178 ADRs with lineage, 26 explicit acceptance acts with Emil as principal) and composite acts ready made.
- Independence by non-existence must be preserved by choosing a slice that does not exist yet. The preferred slice is varve-demo (~/projects/varve-demo): eight steps, S1 to S7 and E, all pending, each with a declared target and a CI check, every step pulling released Varve as a pinned shared component.
- Varve cannot be the independent external test Phoenix would have been. Its decision protocol was written for this framework, so the case may fit by construction. Varve is the second internal test, stronger than T2a; the external test stays a successor item.

Governing documents — read before GATE 1

- decision-driven-design/meta/way-of-working.md. It wins over this prompt where they disagree.
- CLAUDE.md in both repositories.
- The sealed pre-registration meta/sessions/2026-09-27-act-address/prereg-act-coordinates.md, and rulings.md and results-act-address-dry-run.md beside it.
- meta/sessions/2026-09-27-act-address-landing/gate1-rulings.md, gate2-rulings.md and successor-items.md (S-2, S-3, S-4, S-6, S-9).
- meta/sessions/2026-10-26-housekeeping/successor-items.md (H-2, H-3) and core/decisions/DDD-dec-40.yaml.
- core/decisions/DDD-dec-38.yaml and the five core/claims/DDD-address-0*.yaml.
- Upstream core/claims/DDD-ground-06.yaml, core/14-indexed-determination.md §5 and core/09 §1.
- varve-demo/README.md, varve-demo/docs/spec/script.md, varve-demo/docs/adr/ and varve-demo/docs/decisions/.
- Varve/decision-protocol-and-architecture.md and Varve/docs/adr/README.md.

Discipline

- Stop at every gate and report. Proceed only on Emil's ruling.
- Three registers: Ruled, [PROPOSED], [OPEN]. Flag unconfirmed reasoning as UNVERIFIED — Emil review.
- Name the weakest point first in every gate report. For this session it is known: fit by construction. Say how each gate's output is or is not exposed to it.
- Supersession, never rewriting. The sealed pre-registration is fixed. Verify its SHA-256 is ef34e3bc14ab793800edd8c096e82adf0652ef8bc284d54d52efd20f8bf5f5eb at arrival and never edit it.
- Every prediction is marked analytic or empirical. An analytic prediction cannot surprise and does not count as evidence.
- Every commit that changes canon carries a Basis: line citing claim or decision IDs.
- Read nothing in varve-demo beyond the governing documents listed above until the pre-registration is sealed. Write nothing there at all. The slice is built after this session, by the method, against the sealed file.
- British spelling. One idea per sentence. Tables for structure, prose for arguments.
- Varve and varve-demo are public under Emil's own name. The Phoenix pseudonymisation rule lapses; nothing else about naming changes.

Gates

GATE 0 — arrival. Create meta/sessions/<today>-t2b-design/ downstream. Commit this prompt verbatim as prompt.md and the filled-in bootstrap.md, on the session branch, as the first commit, before touching anything else. Record the base commits of both repositories and of Varve and varve-demo. Verify the sealed pre-registration's hash. Stop.

GATE 1 — survey. Report the following, then stop:

1. Drift since the landing. List every change since downstream 4004b49 and upstream v5.15.2 that touches DDD-ground-06, the five address claims, term:act-address, term:act, or DDD-ground-01.
2. ID. Confirm DDD-dec-41 is free in both repositories.
3. Where Phoenix is named. List every file and field. Separate those that change (the five test fields) from those that stay (DDD-dec-38, the sealed pre-registration, past session records).
4. The slice. Describe varve-demo as it stands: the eight steps, their targets and checks, their dependencies on one another, the Varve version and digest they pin, and what has been built, if anything, since 2026-10-26. If any step has moved past pending, say which, and propose whether the slice is still a slice that does not exist.
5. Prediction mapping. For each of the four empirical T2 predictions in the sealed pre-registration §5, name the varve-demo act or acts it will be read against, and say whether the reading is forced by the slice's design (exposed to fit by construction) or free to fail.
6. The accumulated items. Place each in the slice: F-1 (an act that never reads an axis a governing predicate uses); the GATE 2 ruling 5 item (verdict-triggered decisions anchor at the following act, whose reading contains the verdict); the reading/verdict-input line flagged in DDD-ground-06 and DDD-address-01; F-2 (inherited tolerance across parents); F-3 (the replication case, provisional on T2b under DDD-dec-40).
7. Falsifiers. Carry the seven from the sealed §6 and say, for each, what observation in varve-demo would fire it. Propose any the slice adds.
8. What the derivation record is. Name the files and git objects that constitute it for the slice: Varve's ADRs and acceptance commits, varve-demo's ADRs and decisions, the pinned package and image digests, the CI runs.
9. Status reach. State what evidence from this test can and cannot do to the five claims' status, under meta/way-of-working.md's vocabulary. The expected answer is reported, not established; say why.

GATE 2 — the ruling and the claims. On the session branch downstream:
- File DDD-dec-41 as ruled at GATE 1: Phoenix withdrawn, the slice named, the six-week clock gone, fit by construction recorded as the test's known limit, the external test carried as a successor item.
- Amend the five address claims' test fields. Nothing else in those files moves unless ruled.
- Run validate-claims.py in both modes. Report warnings against the baseline of six.
- Commit with Basis: lines. Stop.

GATE 3 — the pre-registration. Draft prereg-t2b.md in the session directory and present it. It carries, in this order:
1. Weakest point: fit by construction, and what in the design is and is not exposed to it.
2. The ruling it rests on and the sealed pre-registration it extends, by hash.
3. Criteria K1 to K5, carried unchanged.
4. The slice, as ruled at GATE 1, with the base commit of varve-demo at sealing and the rule that the test runs against that commit's successors only.
5. Predictions, each marked analytic or empirical, each naming the act it is read against and the observation that would surprise.
6. The accumulated items as test items, each with its reading.
7. Falsifiers and what each breaks.
8. The reading procedure: who runs method step 1 over the slice, when, and what counts as a divergence. Divergences are recorded, never reconciled.
9. Open, not tested here.

Stop. On Emil's ruling, apply the rulings, compute the SHA-256, record it in bootstrap.md and DDD-dec-41's notes, and commit. From that commit the file is sealed.

GATE 4 — close. Write the session manifest and successor items. The successor items must include: the external test (a case nobody in this programme authored); running T2b (its own session, after the slice is built); S-3, S-4, S-6, S-9 and H-2, H-3 as they stand. Open a PR downstream and do not merge it. Stop.

Out of scope

- Building, editing or running anything in varve-demo or Varve.
- Running T2b.
- Any upstream change. Upstream names the case neutrally by the landing session's GATE 1 ruling 2 and needs nothing.
- Editing the sealed pre-registration, DDD-dec-38, or any past session record.
- Filing S-3 (seam decay's home) or S-4 (the behaviour term). If GATE 1 shows the pre-registration cannot be written without one of them, stop and say so.
- Moving any claim's status.