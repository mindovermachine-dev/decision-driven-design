#!/usr/bin/env python3
"""ci.py — every gate of this repository, in order, from one entry point.

The workflow runs this and nothing else (DDD-dec-81, item 3: pipelines runnable locally). Run it
from the repository root:

    python3 scripts/ci.py            # every gate
    python3 scripts/ci.py fixtures   # named gates only
    python3 scripts/ci.py --list     # the gates, in order

Exit 0 when every gate passes, 1 otherwise. Each gate's own output is printed only when it fails.
Dependencies: scripts/requirements.txt (Python), plus git and ssh-keygen on PATH, which are checked
before any gate runs. The pins gate shallow-clones the pinned upstream ref
(graph/upstream.yaml); set DDD_UPSTREAM_DIR to a local checkout to run offline.
"""

import hashlib
import os
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


# System tools the gates need, and which gate needs each. Checked before any gate runs, so a
# missing tool is named instead of surfacing as a traceback inside a checker.
SYSTEM_TOOLS = [
    ("git", "core-order (clones the pinned upstream ref), releases and fixtures (the guard)"),
    ("ssh-keygen", "how (the How examples mint throwaway signing keys, DDD-dec-62)"),
]


def preflight():
    missing = [(t, why) for t, why in SYSTEM_TOOLS if shutil.which(t) is None]
    for t, why in missing:
        print(f"FAIL preflight   {t} is not on PATH; needed by {why}. "
              f"Install it, or use the devcontainer.")
    return not missing


def git(*args, cwd):
    r = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)}: {r.stderr.strip()}")
    return r.stdout.strip()


def cut_tags(root: Path, versions):
    """Which versions are cut, and at which commit: {version: commit}, and a note saying how that
    was decided (correction of 2026-11-02, item 3(a)). The remote decides: a clone that has not
    fetched a tag, or holds a stale one (`git fetch` never overwrites a local tag), would otherwise
    re-guard a cut release at HEAD. Local tags decide only when origin cannot be reached, and the
    note says so."""
    try:
        r = subprocess.run(["git", "ls-remote", "--tags", "origin"], cwd=root, capture_output=True,
                           text=True, timeout=60)
        reached, why = r.returncode == 0, (r.stderr.strip().splitlines() or ["no origin"])[0]
    except subprocess.TimeoutExpired:
        reached, why = False, "git ls-remote timed out"
    if reached:
        refs = {}
        for line in r.stdout.splitlines():
            sha, ref = line.split("\t")
            name = ref.removeprefix("refs/tags/")
            if name.endswith("^{}"):
                refs[name[:-3]] = sha          # an annotated tag: the commit it points at
            else:
                refs.setdefault(name, sha)
        return {v: refs[v] for v in versions if v in refs}, "cut decided from origin (git ls-remote --tags origin)"
    local = {}
    for v in versions:
        q = subprocess.run(["git", "rev-parse", "--verify", "--quiet", f"refs/tags/{v}^{{commit}}"],
                           cwd=root, capture_output=True, text=True)
        if q.returncode == 0:
            local[v] = q.stdout.strip()
    return local, f"offline: origin not reachable ({why}); cut decided from LOCAL tags, which may be missing or stale"


def release_cuts(root: Path, descriptors):
    """For each descriptor: if its version is cut, its file at HEAD must equal the file at the tag
    (item 3(b)); if not cut, the release-head guard runs at HEAD (DDD-dec-84)."""
    cut, note = cut_tags(root, [d.stem for d in descriptors])
    code, out = 0, note
    for d in descriptors:
        v, rel = d.stem, d.relative_to(root).as_posix()
        if v not in cut:
            c, o = run(["scripts/check-release-head.py", rel, "--at", "HEAD"], cwd=root)
            out += "\n" + o
            code = code or c
            continue
        at = subprocess.run(["git", "show", f"{cut[v]}:{rel}"], cwd=root, capture_output=True)
        head = subprocess.run(["git", "show", f"HEAD:{rel}"], cwd=root, capture_output=True)
        if at.returncode != 0:
            out += (f"\n  {v}: cut at {cut[v][:7]}, but that commit or its {rel} is not in this clone; "
                    "run git fetch --force --tags origin")
            code = 1
        elif head.stdout != at.stdout:
            out += (f"\n  {v}: {rel} at HEAD differs from the file at the tag ({cut[v][:7]}): the descriptor "
                    "changed after it was cut. A cut release's descriptor is immutable")
            code = 1
        else:
            out += f"\n  {v}: cut at {cut[v][:7]}; {rel} at HEAD equals the file at the tag; immutable, not re-guarded"
    return code, out


def gate_releases():
    """spec/release-format.md under DDD-dec-84: every descriptor validates; a descriptor not yet cut
    satisfies the release-head guard at HEAD; a cut one is unchanged since its tag."""
    rel = ROOT / "releases"
    descriptors = sorted(rel.glob("*.yaml")) if rel.is_dir() else []
    if not descriptors:
        return 0, "no release descriptors"
    code, out = run(["scripts/validate-releases.py", "releases/"])
    if code != 0:
        return code, out
    c, o = release_cuts(ROOT, descriptors)
    return c, out + "\n" + o


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

    accept("releases/accept",
           *run(["scripts/validate-releases.py", str(FIX / "releases/accept")]))
    for tree in sorted(p for p in (FIX / "releases/refuse").iterdir() if p.is_dir()):
        refuse(f"releases/refuse/{tree.name}",
               *run(["scripts/validate-releases.py", str(tree)]), expect_of(tree))

    with tempfile.TemporaryDirectory(prefix="ddd-guard-") as tmp:
        for name, want, code, out in guard_scenarios(Path(tmp)):
            (accept if want is None else lambda l, c, o: refuse(l, c, o, want))(
                f"release-head/{name}", code, out)

    with tempfile.TemporaryDirectory(prefix="ddd-pins-") as tmp:
        for name, ok, why, out in pin_scenarios(Path(tmp)):
            failed += not ok
            lines.append(f"  {'ok  ' if ok else 'FAIL'} upstream-pins/{name}"
                         + ("" if ok else f" ({why})\n{out}"))

    return (1 if failed else 0), "\n".join(lines)


def pin_scenarios(tmp: Path):
    """Pinning upstream decisions in validate-core-order.py (DDD-dec-112), in throwaway
    repositories: a local upstream with a tag, and a downstream graph/upstream.yaml that pins it.

    Yields (name, ok, why, output). W5 and W6 are warnings, so each scenario asserts the exact
    findings, not the exit code alone. The expected content_hash is computed here, independently
    of the checker: sha256 over statement, region and canonical_md joined by NUL, where a decision
    has only a statement. Before DDD-dec-112 the checker did not read upstream decisions, so every
    decision pin was an E12 and every scenario below failed."""
    env = dict(os.environ, GIT_AUTHOR_NAME="fixture", GIT_AUTHOR_EMAIL="fixture@invalid",
               GIT_COMMITTER_NAME="fixture", GIT_COMMITTER_EMAIL="fixture@invalid")
    env.pop("DDD_UPSTREAM_DIR", None)

    up = tmp / "upstream"
    decisions = {
        "DDD-dec-01": ("One: in force.", None),
        "DDD-dec-02": ("Two: supersedes DDD-dec-03, as a string.", "DDD-dec-03"),
        "DDD-dec-03": ("Three: superseded by DDD-dec-02.", None),
        "DDD-dec-04": ("Four: supersedes DDD-dec-05, as a list.", ["DDD-dec-05"]),
        "DDD-dec-05": ("Five: superseded by DDD-dec-04.", None),
    }
    for did, (statement, supersedes) in decisions.items():
        f = up / "core" / "decisions" / f"{did}.yaml"
        f.parent.mkdir(parents=True, exist_ok=True)
        body = f"format: 1\nid: {did}\nkind: decision\nstatement: |\n  {statement}\n"
        if isinstance(supersedes, str):
            body += f"supersedes: {supersedes}\n"
        elif supersedes:
            body += "supersedes:\n" + "".join(f"  - {x}\n" for x in supersedes)
        f.write_text(body, encoding="utf-8")
    subprocess.run(["git", "init", "-q", "-b", "main"], cwd=up, check=True, env=env)
    subprocess.run(["git", "add", "-A"], cwd=up, check=True, env=env)
    subprocess.run(["git", "-c", "commit.gpgsign=false", "commit", "-q", "-m", "upstream"],
                   cwd=up, check=True, env=env)
    subprocess.run(["git", "-c", "tag.gpgsign=false", "tag", "v1.0.0"], cwd=up, check=True, env=env)

    def digest(statement):
        return "sha256:" + hashlib.sha256("\x00".join([statement, "", ""]).encode()).hexdigest()

    def check(name, pins):
        d = tmp / name
        (d / "core").mkdir(parents=True)
        (d / "graph").mkdir()
        text = f"format: upstream/v1\nupstream:\n  repo: file://{up}\n  ref: v1.0.0\n  pins:\n"
        for pid, status, h in pins:
            text += f"    - id: {pid}\n      status_at_pin: {status}\n      content_hash: {h}\n"
        (d / "graph" / "upstream.yaml").write_text(text, encoding="utf-8")
        r = subprocess.run([PY, str(ROOT / "scripts/validate-core-order.py"), str(d / "core")],
                           cwd=d, capture_output=True, text=True, env=env)
        out = r.stdout + r.stderr
        found = lambda code: [l for l in out.splitlines() if l.strip().split("  ")[-1].startswith(code)]
        return r.returncode, out, found

    one = ("DDD-dec-01", "in-force", digest(decisions["DDD-dec-01"][0]))

    code, out, found = check("resolves", [one])
    yield ("accept/decision-resolves", code == 0 and not found("E12") and not found("W5")
           and not found("W6"), "expected exit 0 and no E12, W5 or W6", out)

    code, out, found = check("missing", [one, ("DDD-dec-09", "in-force", digest("Nine."))])
    e12 = found("E12")
    yield ("refuse/decision-missing", code == 1 and len(e12) == 1 and "DDD-dec-09" in e12[0],
           "expected exit 1 and exactly one E12, on DDD-dec-09", out)

    code, out, found = check("superseded", [
        ("DDD-dec-03", "in-force", digest(decisions["DDD-dec-03"][0])),
        ("DDD-dec-05", "in-force", digest(decisions["DDD-dec-05"][0]))])
    w5 = found("W5")
    yield ("warn/decision-superseded", code == 0 and len(w5) == 2
           and any("DDD-dec-03" in w and "'superseded'" in w for w in w5)
           and any("DDD-dec-05" in w and "'superseded'" in w for w in w5) and not found("E12"),
           "expected exit 0 and W5 on DDD-dec-03 (string supersedes:) and DDD-dec-05 (list)", out)

    code, out, found = check("drift", [("DDD-dec-01", "in-force", digest("One: as it once read."))])
    w6 = found("W6")
    yield ("warn/decision-statement-drift", code == 0 and len(w6) == 1 and "DDD-dec-01" in w6[0]
           and not found("E12") and not found("W5"),
           "expected exit 0 and exactly one W6, on DDD-dec-01", out)


def guard_scenarios(tmp: Path):
    """The release-head guard in throwaway repositories (scripts/fixtures/README.md).

    Yields (name, expected refusal text or None for accept, exit code, output). Each scenario
    copies scripts/check-release-head.py into a fresh repository, because the guard runs git in
    the repository it lives in."""
    env = dict(os.environ, GIT_AUTHOR_NAME="fixture", GIT_AUTHOR_EMAIL="fixture@invalid",
               GIT_COMMITTER_NAME="fixture", GIT_COMMITTER_EMAIL="fixture@invalid")

    def repo(name):
        d = tmp / name
        (d / "scripts").mkdir(parents=True)
        shutil.copy(ROOT / "scripts/check-release-head.py", d / "scripts")
        subprocess.run(["git", "init", "-q", "-b", "main"], cwd=d, check=True, env=env)
        return d

    def commit(d, path, text, msg):
        f = d / path
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(text, encoding="utf-8")
        subprocess.run(["git", "add", "-A"], cwd=d, check=True, env=env)
        subprocess.run(["git", "-c", "commit.gpgsign=false", "commit", "-q", "-m", msg],
                       cwd=d, check=True, env=env)
        return git("rev-parse", "HEAD", cwd=d)

    def descriptor(head):
        return f"format: 2\nversion: v9.9.0\nratified_head: {head}\n"

    def guard(d, at):
        r = subprocess.run([PY, "scripts/check-release-head.py", "releases/v9.9.0.yaml",
                            "--at", at], cwd=d, capture_output=True, text=True)
        return r.returncode, r.stdout + r.stderr

    # Accept: the descriptor is the only change on top of the ratified head.
    d = repo("ratified-plus-descriptor")
    commit(d, "canon.md", "one\n", "canon")
    r = commit(d, "canon.md", "two\n", "ratified canon")
    at = commit(d, "releases/v9.9.0.yaml", descriptor(r), "descriptor")
    yield ("accept/ratified-plus-descriptor", None, *guard(d, at))

    # Refuse: cut BEFORE the ratified head (the v5.14.0 class upstream).
    d = repo("cut-before")
    base = commit(d, "canon.md", "one\n", "canon")
    r = commit(d, "canon.md", "two\n", "ratified canon, on a branch")
    git("checkout", "-q", "-b", "cut", base, cwd=d)
    at = commit(d, "releases/v9.9.0.yaml", descriptor(r), "descriptor, cut from the old head")
    yield ("refuse/cut-before", "is not an ancestor", *guard(d, at))

    # Refuse: an unratified commit merged AFTER the ratified head (its mirror).
    d = repo("merged-after")
    commit(d, "canon.md", "one\n", "canon")
    r = commit(d, "canon.md", "two\n", "ratified canon")
    commit(d, "canon-extra.md", "unratified\n", "a change after ratification")
    at = commit(d, "releases/v9.9.0.yaml", descriptor(r), "descriptor")
    yield ("refuse/merged-after", "changed between the ratified head", *guard(d, at))

    # The releases gate on a cut release (correction of 2026-11-02, item 3). Each case clones a bare
    # origin that holds the tag, the way GitHub holds it, or has no origin at all.
    def cut_origin(name):
        w = repo(name + "-src")
        commit(w, "canon.md", "one\n", "canon")
        r = commit(w, "canon.md", "two\n", "ratified canon")
        x = commit(w, "releases/v9.9.0.yaml", descriptor(r), "descriptor")
        git("-c", "user.name=fixture", "-c", "user.email=fixture@invalid", "-c", "tag.gpgsign=false",
            "tag", "-a", "-m", "v9.9.0", "v9.9.0", x, cwd=w)
        bare = tmp / (name + ".git")
        git("clone", "-q", "--bare", str(w), str(bare), cwd=tmp)
        c = tmp / name
        git("clone", "-q", "--no-tags", str(bare), str(c), cwd=tmp)
        return c, r

    def gate(d):
        return release_cuts(d, [d / "releases" / "v9.9.0.yaml"])

    # F-1, accept: the tag is on origin and not in the clone; later work on top; descriptor unchanged.
    # The old gate re-guarded this at HEAD and refused it ("changed between the ratified head").
    d, r = cut_origin("cut-tag-only-on-origin")
    commit(d, "later.md", "after the cut\n", "later work")
    code, out = gate(d)
    if "from origin" not in out:
        code = 1
    yield ("accept/cut-tag-only-on-origin", None, code, out)

    # F-2, refuse: as F-1, but ratified_head is changed after the cut (023c2c4, c7424ad).
    d, r = cut_origin("cut-descriptor-edited")
    commit(d, "later.md", "after the cut\n", "later work")
    commit(d, "releases/v9.9.0.yaml", descriptor(git("rev-parse", "HEAD", cwd=d)), "ratified_head moved after the cut")
    yield ("refuse/cut-descriptor-edited", "changed after it was cut", *gate(d))

    # F-3, accept: no origin; a local tag decides, and the output says so.
    d = repo("cut-offline")
    commit(d, "canon.md", "one\n", "canon")
    r = commit(d, "canon.md", "two\n", "ratified canon")
    x = commit(d, "releases/v9.9.0.yaml", descriptor(r), "descriptor")
    git("-c", "tag.gpgsign=false", "tag", "v9.9.0", x, cwd=d)
    commit(d, "later.md", "after the cut\n", "later work")
    code, out = gate(d)
    if "offline" not in out:
        code = 1
    yield ("accept/cut-offline-local-tag", None, code, out)


GATES = [
    ("claims", "core/claims/ against the claim format", gate_claims),
    ("decisions", "core/decisions/: no escaped decisions", gate_decisions),
    ("core-order", "core order, embeds, and upstream pins at the pinned ref", gate_core_order),
    ("what", "the What: shapes, identity form, hash vectors", gate_what),
    ("how", "the How examples: records, anchors, verdicts", gate_how),
    ("releases", "release descriptors valid; the release-head guard for each not yet cut",
     gate_releases),
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
    if not preflight():
        print("\nFAILED: preflight")
        return 1
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
