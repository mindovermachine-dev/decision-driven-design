# Bootstrap — applications/ for readers, redone, 2026-11-09

Filled in at arrival and committed with `prompt.md` as the session's first commit.

| Parameter | Value |
|---|---|
| Invocation | Interactive, gated. Emil's two rulings are verbatim in `prompt.md`, and `rulings.md` records them as Round 1 |
| Principal | Emil (sole ratifier; ratifies by landing the branch) |
| Issue | [#71](https://github.com/mindovermachine-dev/decision-driven-design/issues/71). Every commit of the session carries `Refs #71` |
| Predecessor | PR #48, closed and not merged. Its branch `claude/applications-for-readers-2026-11-02` at `068cb23` is kept as the record and is read here, not merged |
| Precondition | PR #64 (the PDLC and the SDLC) **has landed**: merged 2026-11-09T13:54Z, head `a53d02d` |
| Upstream pin | `graph/upstream.yaml`, unchanged by this session |
| Downstream base | `84aa466` (`84aa4665b4b0392ef4bb08ac042e42ae9fc6d12c`), the head of `main` at arrival (2026-11-10). It is after #64 and after the v0.7.0 release descriptor (#69/#70) |
| Downstream branch | `claude/zealous-ptolemy-3txf8k`, from `main` at `84aa466` |
| Date | The prompt names the session 2026-11-09, and the folder keeps that name. The work starts on 2026-11-10 |

## Gates

| Gate | What | Who |
|---|---|---|
| G0 | This charter committed before any other change | Claude |
| A | `DDD-dec-94` filed on `main` from #48's file; `spec/doc-format.md` ported; the validators run | Claude; **stops for Emil** |
| Q | #48's ruling requests 2 to 4 put to Emil; answers recorded verbatim before anything they affect is written | **Emil** |
| B | The rewrite of `applications/` to `spec/doc-format.md`; `DDD-dec-95` filed; the independent equivalence check; A-4 pre-registered | Claude; **stops for Emil** |
| Land | CI green, head reported, land commands given | **Emil** |

## Decision ids at arrival (prompt step 2)

Checked on all 59 remote branches after unshallowing, on 2026-11-10.

- `core/decisions/DDD-dec-94.yaml` and `DDD-dec-95.yaml` exist only on
  `claude/applications-for-readers-2026-11-02` (`068cb23`). No branch holds a file for `DDD-dec-96`
  to `-99`. `main` holds up to `DDD-dec-93`, then `DDD-dec-100` to `-118`.
- Other text that names the ids is headroom bookkeeping and claims no use. On `main`, this is
  `DDD-dec-100` (notes), `DDD-dec-103` (notes), `meta/sessions/2026-11-02-canon-cli/bootstrap.md`
  and its `successor-items.md` S-6, and `meta/sessions/2026-11-03-sdlc-edition-1/prompt.md`. A
  canon test fixture uses `DDD-dec-99` as a string, in `tools/canon/tests/Canon.Tests/IssueRefsTests.cs`.
  Other branches carry copies of the same lines.
- **Stale note, reported and not changed:** S-6 in the canon-cli session left `94` to `99` to the
  authority-profile session (`claude/bold-franklin-i7b16g`). That branch uses none of them. The
  note is a session record and stays as written.

This session uses `DDD-dec-94` and `DDD-dec-95`. If another id is needed, it takes the next free
one above `DDD-dec-118`, checked again when it is needed.

## Scope

In scope: `core/decisions/DDD-dec-94.yaml` and `-95.yaml`; `spec/doc-format.md`; every document
under `applications/`, for presentation only; this session record; and the session's row in
`meta/sessions/README.md`.

Out of scope: any claim's statement, status or evidence; any rule in `applications/`, since a
rewrite that changes a rule is reported, not made; hashed vocabulary files (`what/ontology.ttl`,
`what/shapes.ttl`); `apparatus/` (successor A-2); landing.
