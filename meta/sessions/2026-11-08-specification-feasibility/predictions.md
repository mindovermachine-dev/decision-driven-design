# Predictions — specification feasibility, 2026-11-08

Written before each operation is run. Results are recorded against each prediction.

## P-1 — decision validation

`python3 scripts/validate-claims.py core/decisions/ --decisions` passes with `DDD-dec-116` and
`DDD-dec-117` added. Every `basedOn` entry names a file in `core/decisions/` or `core/claims/`
(checked by listing before writing), so `basis-resolves` raises nothing new. Warnings already on
`main` stay as they are.

**Result:** held. "valid: 93 decisions, ids unique, format rules satisfied".

## P-2 — the full gate

`python3 scripts/ci.py` passes. This session changes no claim, no What or How file and no fixture,
so every gate after decisions returns what it returns on `main` at `1ab1de0`.

**Result:** held for the repository; wrong about the environment. The first two runs failed before
any gate read this session's files:
- `preflight`: `ssh-keygen` was not on PATH. Installed (`openssh-client`).
- `releases`: the guard could not see `v0.5.0`'s commit, because the clone was shallow. Fixed by
  `git fetch --force --tags origin`, as the guard's message says.

The third run passed every gate (exit 0). Neither failure concerned a file this session changed.

## P-3 — the full gate after the rebase onto 80e9088

`python3 scripts/ci.py` passes. `main` gained `DDD-dec-114`, `DDD-dec-115` and the `lc:` lifecycle
graph; this session's two decisions cite neither, and no id collides.

**Result:** held. Every gate passed (exit 0).
