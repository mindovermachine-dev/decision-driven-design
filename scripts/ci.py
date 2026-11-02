#!/usr/bin/env python3
"""ci.py — every gate of this repository, in order, from one entry point.

The workflow runs this and nothing else (DDD-dec-81, item 3: pipelines runnable locally). Run it
from the repository root:

    python3 scripts/ci.py            # every gate
    python3 scripts/ci.py fixtures   # named gates only
    python3 scripts/ci.py --list     # the gates, in order

Exit 0 when every gate passes, 1 otherwise. Each gate's own output is printed only when it fails.
Dependencies: scripts/requirements.txt. The pins gate shallow-clones the pinned upstream ref
(graph/upstream.yaml); set DDD_UPSTREAM_DIR to a local checkout to run offline.
"""

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PY = sys.executable
FIX = ROOT / "scripts" / "fixtures"


def run(args, cwd=ROOT):
    r = subprocess.run([PY, *args], cwd=cwd, capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr)


def gate_claims():
    return run(["scripts/validate-claims.py", "core/claims/"])


def gate_decisions():
    return run(["scripts/validate-claims.py", "core/decisions/", "--decisions"])


def gate_core_order():
    return run(["scripts/validate-core-order.py", "core/"])


def gate_what():
    return run(["applications/sdlc/what/check.py"])


def gate_how():
    return run(["applications/sdlc/how-examples/check.py"])


def expect_of(path: Path) -> str:
    """The expected error text: an `# expect:` first line, or an `expect` file beside a tree."""
    if path.is_dir():
        return (path / "expect").read_text(encoding="utf-8").strip()
    first = path.read_text(encoding="utf-8").splitlines()[0]
    return first.removeprefix("# expect:").strip()


def materialise(tree: Path, into: Path) -> Path:
    """Copy a core-order fixture tree, dropping the .fixture suffix, and return its core/."""
    dest = into / tree.name
    shutil.copytree(tree, dest)
    for f in dest.rglob("*.fixture"):
        f.rename(f.with_suffix(""))
    return dest / "core"


def gate_fixtures():
    lines, failed = [], 0

    def accept(label, code, out):
        nonlocal failed
        ok = code == 0
        failed += not ok
        lines.append(f"  {'ok  ' if ok else 'FAIL'} accept {label}" + ("" if ok else f"\n{out}"))

    def refuse(label, code, out, want):
        nonlocal failed
        ok = code != 0 and want in out
        failed += not ok
        why = "" if ok else (f" (exit {code}, expected text {want!r} "
                             f"{'found' if want in out else 'not found'})\n{out}")
        lines.append(f"  {'ok  ' if ok else 'FAIL'} refuse {label}{why}")

    accept("claims/accept", *run(["scripts/validate-claims.py", str(FIX / "claims/accept")]))
    for f in sorted((FIX / "claims/refuse").glob("*.yaml")):
        refuse(f"claims/refuse/{f.name}", *run(["scripts/validate-claims.py", str(f)]), expect_of(f))

    accept("decisions/accept",
           *run(["scripts/validate-claims.py", str(FIX / "decisions/accept"), "--decisions"]))
    for f in sorted((FIX / "decisions/refuse").glob("*.yaml")):
        refuse(f"decisions/refuse/{f.name}",
               *run(["scripts/validate-claims.py", str(f), "--decisions"]), expect_of(f))

    with tempfile.TemporaryDirectory(prefix="ddd-fixtures-") as tmp:
        tmp = Path(tmp)
        core = materialise(FIX / "core-order/accept", tmp)
        accept("core-order/accept", *run(["scripts/validate-core-order.py", str(core)]))
        for tree in sorted(p for p in (FIX / "core-order/refuse").iterdir() if p.is_dir()):
            core = materialise(tree, tmp)
            refuse(f"core-order/refuse/{tree.name}",
                   *run(["scripts/validate-core-order.py", str(core)]), expect_of(tree))

    return (1 if failed else 0), "\n".join(lines)


GATES = [
    ("claims", "core/claims/ against the claim format", gate_claims),
    ("decisions", "core/decisions/: no escaped decisions", gate_decisions),
    ("core-order", "core order, embeds, and upstream pins at the pinned ref", gate_core_order),
    ("what", "the What: shapes, identity form, hash vectors", gate_what),
    ("how", "the How examples: records, anchors, verdicts", gate_how),
    ("fixtures", "each checker accepts its accept tree and refuses its refuse cases", gate_fixtures),
]


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--list" in sys.argv:
        for name, what, _ in GATES:
            print(f"{name:11} {what}")
        return 0
    unknown = set(args) - {g[0] for g in GATES}
    if unknown:
        print(f"unknown gate(s): {', '.join(sorted(unknown))}; see --list", file=sys.stderr)
        return 2
    failed = []
    for name, what, fn in GATES:
        if args and name not in args:
            continue
        code, out = fn()
        print(f"{'ok  ' if code == 0 else 'FAIL'} {name:11} {what}", flush=True)
        if name == "fixtures":
            print(out, flush=True)
        elif code != 0:
            print(out.rstrip(), flush=True)
        if code != 0:
            failed.append(name)
    print(f"\n{'FAILED: ' + ', '.join(failed) if failed else 'all gates passed'}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
