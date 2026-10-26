# GATE 1 survey — doc format

Surveyed 2026-10-26 on `claude/doc-format`, against downstream `baec167` and upstream `v5.15.1` (`1cb3819`). Everything below is a finding or `[PROPOSED]`. Nothing has been moved, and nothing is ruled except where it says so.

## Weakest point first

**Ruling 1 does not yet say which canon.** "Only canon carries authority" was ruled with upstream in mind. But this repository holds canon of its own: `core/13`–`core/17` carry `ddd:contract` blocks and were filed as projection canon by `DDD-dec-10`, `-11` and `-13`, and `core/claims/` and `core/decisions/` are canon by `CLAUDE.md`. Two readings follow, and they give different charters:

| Reading | Canon is | Consequence |
|---|---|---|
| **A — both repositories' `core/`** | upstream `core/`, plus downstream `core/` (docs 13–17, claims, decisions, terms) | Software-specific results can be promoted here, into `core/claims/`. `core/13`–`17` keep the canon format. |
| **B — upstream only** | upstream `core/` | Every downstream result must go upstream or lose authority. `core/13`–`17` and the downstream claims would need a disposition of their own. |

**Recommendation: A.** It matches the split as filed (`DDD-dec-04`, `-10`), and it is the only reading under which software-specific results such as prompt-cache ordering have anywhere to go. `UNVERIFIED — Emil review`. Every disposition below assumes A, and says where B would change it.

## 1. Inventory

65 Markdown documents outside `meta/sessions/`, and 127 inside it.

| Folder | Docs | Opens with today | Implied reader | Status register | `ddd:ref` |
|---|---|---|---|---|---|
| root | 8 | title, prose | everyone arriving; contributors | none | none |
| `apparatus/` | 7 + README | title, then **Location:** or **Destination:**, **Status:** in prose, an "Upstream basis" paragraph | canon contributors, by tone | prose only: projected, derived, demonstrated | 1–4 each |
| `applications/` | 3 + README | as apparatus | practitioners, nominally | prose only | 3 each in `sdlc/` |
| `core/` | 5 + 3 READMEs | `ddd:contract` | canon readers, citing agents | contract `status:` and claim files | 0–5 |
| `meta/` | 18 + README | title, sometimes **Status:** | Emil and session agents | mixed: DRAFT, holding, erratum | none |
| `meta/sessions/` | 127 | prompt and bootstrap convention (`meta/sessions/README.md`) | Emil and session agents | Ruled, `[PROPOSED]`, `[OPEN]` | none |
| `migration/` + `migration-report.md` | 4 | title; one `ddd:contract` used as an example | nobody live | historical | 7 in the report |
| `papers/` | 9 | venue format, briefs, responses | external reviewers | in the paper | none |
| `projections/` | 3 + README | manifest (the track); pin line (the primer) | the audience in the manifest | flagged at point of use | 42 in the track |
| `spec/` | 1 | title, normative prose | validator authors, file-writing agents | format version | none |
| `.claude/skills/` | 1 | skill frontmatter | session agents | n/a | none |

Two findings from the inventory:
- **The projections already have the format.** The track's manifest and the primer's pin line are what `ddd:doc` generalises. They are the precedent, not the problem.
- **The primer is pinned at `v5.13.0`; the repository pins `v5.15.1`.** It is a stale projection under way-of-working §3. Its treatment (re-render, annotate or let stand) is out of this session's scope. It is a successor item.

## 2. Uninstrumented authority

No `apparatus/` or `applications/` document has a claim file behind it. The downstream claim areas are `address`, `cost`, `delivery`, `org`, `sim`, `tool` (`DDD-tool-01` is about the claim graph, not tools) and `track`. Each document's headline results, checked against the upstream claims and term registry at the pin:

| Document | Headline result (the doc's own words, shortened) | At the pin |
|---|---|---|
| `encode-verify` | Encode ground you control; verify ground you don't. An observation of uncontrolled ground cannot be amortised. Verify on a schedule. | **Partly.** `term:encode-verify-split` defines the split. The *selector* (control decides which side) and the irreducibility are not canon. |
| `closure-principle` | An actor's own output is not ground. `plan = f(config, state)`, not `f(config, reality)`. | **No.** And upstream `core/11` line 12 already depends on it in prose: "the closure principle (an actor's own prior output is not ground)". **Canon leans on an unfiled result.** |
| `adversarial-ground` | The attack surface of an actor is its ground, not its logic. Poison can be a relation, not a fact. Three fields converged. | **Headline yes:** `term:poisoned-ground` says "the ground is the attack surface". The fact/relation refinement and the convergence evidence are not filed. |
| `the-skill-floor` | A skill without a per-invocation verifier is floor-exposed. P(as intended) ≈ 1 − overflow × open. | **No.** It applies `DDD-floor-01` (reported), but the skill result is unfiled. |
| `prefix-stability` | A prefix is a dependency chain; order by rate over length (SDP, derived); a prefix segment that keeps invalidating flags mislocated encoding. | **No.** The asset `apparatus/assets/prefix-stability-check.py` was re-run and reproduces (four cases, all orderings match the brute-force optimum). The ordering is arithmetic (Smith's rule); the detector reading is the modelling claim. |
| `tool-surfaces` | A call reallocates demand. Exporter, resolver, verifier. Class belongs to ⟨tool, task, consumption⟩. Choosing tools is choosing the floor. | **No.** |
| `tool-contract` | Pin the ground first. The harness binds the toolset; the model never picks. A fixed toolset makes the open set computable. | **No**, and it is mostly normative design, not result. It rests on `tool-surfaces`. |
| `production-as-ground` | Pre-production predicates close over substitute ground. AI raises unverified demand in flight. Progressive delivery should beat fidelity. | **No.** It states its own status as "reported, partially" (a retrodiction against published DORA findings). |

**The apparatus is a chain of unfiled results.** `tool-contract` rests on `tool-surfaces`, which rests on `the-skill-floor` and `encode-verify`. `closure-principle` restates `encode-verify`. Reformatting any one of them will surface the chain.

## 3. Disposition proposal `[PROPOSED]`

Under reading A, **promote** means filing claims in whichever canon fits: upstream if the result is actor-general, `core/claims/` here if it is software-specific. Promotions are not filed in this session.

| Document | Move | Target canon | Reason | Priority |
|---|---|---|---|---|
| `closure-principle` | **promote** | upstream | Actor-general. Canon already depends on it. It carries its own falsification section, so it is ready to file. | 1 |
| `encode-verify` | **promote** (selector, irreducibility); project the rest | upstream, extending `term:encode-verify-split` | Actor-general. Three other documents rest on it. | 2 |
| `tool-surfaces` | **promote** | here, `tool` area | Tools are an arrangement concern, but the MCP mapping is software-specific. `UNVERIFIED — Emil review`: could be read as actor-general. | 3 |
| `the-skill-floor` | **promote** | here, `tool` area | A direct consequence of `DDD-floor-01` for skills. | 4 |
| `prefix-stability` | **promote** | here, new area | Software-specific. The asset reproduces, so it can file as reported for the arithmetic and projected for the detector. | 5 |
| `production-as-ground` | **promote** | here, `delivery` area | Its novel prediction (§7) is a falsifiable claim with nowhere to live. | 6 |
| `adversarial-ground` | **project** the headline; **hold** the refinement | upstream for the refinement, later | The headline is already canon. The refinement can wait. | 7 |
| `tool-contract` | **project** | — | Normative. It is a design for implementers, not a result. Its basis is the open question, see item 6 below. | pilot |

Under reading B, the four "here" rows become upstream promotions, and `prefix-stability` and `production-as-ground` would likely be **held**, because they are not actor-general.

## 4. Stale structure statements

| Where | What is stale |
|---|---|
| `meta/way-of-working.md` §5 | Shows `core/09` and `papers` under this repository's tree and `projections/`; predates the split. Proposal only, per the prompt. |
| `apparatus/README.md` | "All three are instances of one discipline" — it lists seven. |
| `apparatus/tool-contract.md` | "Location: proposed `apparatus/…` or `applications/`" — it was filed long ago. |
| `applications/sdlc/production-as-ground.md` | "Location: proposed …" — likewise. |
| `apparatus/adversarial-ground.md` | "Destination: `core/`" — never landed. |
| `core/README.md` | Decisions listed as `DDD-dec-01..07, DDD-dec-10`; there are 38. Claim areas listed as `org`, `tool`, `sim`, `cost`; `address`, `delivery` and `track` are missing. |
| `CLAUDE.md` | "Do not add or edit core theory documents in this repo" — contradicted by `core/13`–`17`, filed under `DDD-dec-10`. |
| `README.md` | Upstream links point to `github.com/Hafeok/…`. Same class as S-7. |

## 5. Core prose downstream

`core/13`–`core/17` are not strays. `core/README.md` records them as projection canon: `13` and `14` under the boundary charter (`DDD-dec-10`, `-11`), `16` under `DDD-dec-13`, and all five continue the upstream reading order. **Proposal:** under reading A they keep `ddd:contract` and the canon format unchanged. The stale statement is `CLAUDE.md`'s sentence, which should say "do not add *actor-general* core documents". The wording change is proposed at GATE 2, not made here.

## 6. Retention of the old text

Apparatus documents are not ruled canon, so supersession-not-rewriting does not bind them strictly. Two options:

| Option | For | Against |
|---|---|---|
| **In place**, with `supersedes: <commit>:<path>` in the `ddd:doc` block | One document per subject. The old text is one `git show` away and named in the file. | The old argument leaves the tree. |
| **Superseded file** kept beside the new | The old argument stays readable. | Two documents per subject, and the reader must know which governs. |

**Recommendation: in place.** The `supersedes` field makes the record explicit rather than relying on history alone.

**One schema question this raises for GATE 2.** Most apparatus bases are unfiled results (item 2). If `basis` may only name IDs that resolve at the pin, the pilot will drop its dependency on `tool-surfaces`, and falsifier limb 2 fires by construction. **Proposal:** `basis` may also name a **held result**, as `held:<successor-item-id>`. The check reports these as their own warning class. The dependency is recorded, not dropped, and the warning clears when the promotion lands.

## 7. ID check

| ID | Free |
|---|---|
| `DDD-dec-39` | **Yes** in both repositories (highest is `DDD-dec-38` in each) |

## Also found

- **Upstream relies on an unfiled downstream-held result** (item 2, `closure-principle`). Upstream names the concept, not the file, so it does not break the no-dependents rule. But it is an uninstrumented edge in canon. It is a successor item, and the reason `closure-principle` is priority 1.
- **`meta/sessions/README.md` index** does not yet list `2026-10-25-harness-guide` or this session. Both are added at GATE 4, per the landing session's precedent.

## Rulings requested

1. Canon under ruling 1: reading A or B.
2. The disposition table (item 3), row by row or as a whole.
3. Retention: in place with `supersedes`, or superseded files.
4. Whether `basis` may name `held:<successor-item>`.
5. The `CLAUDE.md` wording change, as a GATE 2 proposal.
