#!/usr/bin/env python3
# Ported from mindovermachine-dev/actor-indexed-determination at tag v5.15.2 (commit 084bce7;
# file last changed upstream at 1097055) under DDD-dec-84. Unchanged below this header.
# Upstream's history in the docstring (v5.14.0, v5.15.0) is the principle repository's.
"""The release-head guard (spec/release-format.md, format 2, rule 7).

A descriptor at format 2 records `ratified_head`: the commit whose canon the
release ratifies. The head that actually merges may differ from it only in the
descriptor file itself. Two releases (v5.14.0, v5.15.0) were cut from a head
that was not the head Emil had ratified, and nothing in the tooling could see
it, because the descriptor did not say which head that was.

Usage:
    check-release-head.py releases/v5.15.2.yaml --at <commit>
        Guard one descriptor at the commit under release (the merge commit on
        the default branch, or a pull request head). Exit 1 on a miss.

    check-release-head.py --hitlist [--assume v5.14.0=75cc767 ...]
        Run every descriptor under releases/ against its own tag. Descriptors
        without `ratified_head` are reported as unguarded unless --assume
        supplies a head for them (reconstruction from the record, for the
        retro-check the guard was asked to pass before its class was chosen).

Checks, in order, for descriptor V with ratified head R at commit A:
    1. R resolves to a commit.
    2. R is an ancestor of A  — the ratified canon is in the release.
    3. Let T = A^2 if A is a merge commit and R is an ancestor of A^2, else A.
       `git diff --name-only R T` is a subset of {releases/V.yaml} — nothing
       but the descriptor was added on top of the ratified head.
Check 2 catches the class that happened (cut from BEFORE the ratified head);
check 3 catches its mirror (unratified commits merged AFTER it).
"""

import argparse
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required: pip install pyyaml")

REPO = Path(__file__).resolve().parent.parent


def git(*args, check=True):
    r = subprocess.run(["git", *args], cwd=REPO, capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)}: {r.stderr.strip()}")
    return r.stdout.strip()


def resolve(ref):
    r = subprocess.run(["git", "rev-parse", "--verify", "--quiet", f"{ref}^{{commit}}"],
                       cwd=REPO, capture_output=True, text=True)
    return r.stdout.strip() or None


def is_ancestor(a, b):
    return subprocess.run(["git", "merge-base", "--is-ancestor", a, b],
                          cwd=REPO).returncode == 0


def guard(version, ratified_head, at):
    """Return (ok, lines). Pure report; the caller decides the exit code."""
    allowed = {f"releases/{version}.yaml"}
    lines = []
    r = resolve(ratified_head)
    if not r:
        return False, [f"ratified_head {ratified_head!r} is not a commit here"]
    a = resolve(at)
    if not a:
        return False, [f"commit under release {at!r} is not a commit here"]
    lines.append(f"ratified_head {r[:7]}  at {a[:7]}")
    if not is_ancestor(r, a):
        return False, lines + [
            f"MISS: ratified head {r[:7]} is not an ancestor of {a[:7]} — "
            f"the release would carry canon cut BEFORE the head that was ratified"]
    parents = git("log", "-1", "--format=%P", a).split()
    target = a
    if len(parents) >= 2 and is_ancestor(r, parents[1]):
        target = parents[1]
        lines.append(f"merge commit; comparing against its second parent {target[:7]}")
    changed = set(filter(None, git("diff", "--name-only", r, target).split("\n")))
    extra = sorted(changed - allowed)
    if extra:
        return False, lines + [
            f"MISS: {len(extra)} file(s) changed between the ratified head and the merged "
            f"head besides the descriptor — unratified commits merged AFTER it:"] + \
            [f"    {f}" for f in extra]
    lines.append("ok: the merged head is the ratified head plus at most the descriptor")
    return True, lines


def load(path):
    with open(path, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("descriptor", nargs="?")
    ap.add_argument("--at", help="the commit under release")
    ap.add_argument("--hitlist", action="store_true")
    ap.add_argument("--assume", action="append", default=[],
                    metavar="vX.Y.Z=SHA", help="reconstructed ratified head for an unguarded descriptor")
    args = ap.parse_args()

    if args.hitlist:
        assumed = dict(a.split("=", 1) for a in args.assume)
        misses = 0
        for p in sorted((REPO / "releases").glob("*.yaml")):
            d = load(p)
            v = d["version"]
            tag = resolve(v)
            head = d.get("ratified_head") or assumed.get(v)
            if not tag:
                print(f"  {v:10} not cut yet — nothing to check against")
                continue
            if not head:
                print(f"  {v:10} unguarded (format {d.get('format')}, no ratified_head)")
                continue
            ok, lines = guard(v, head, tag)
            src = "descriptor" if d.get("ratified_head") else "assumed"
            print(f"  {v:10} {'ok  ' if ok else 'MISS'} ({src})  " + lines[-1])
            misses += 0 if ok else 1
        print(f"hit-list: {misses} miss(es)")
        sys.exit(1 if misses else 0)

    if not args.descriptor or not args.at:
        sys.exit(__doc__)
    d = load(args.descriptor)
    v = d["version"]
    head = d.get("ratified_head")
    if not head:
        print(f"{v}: no ratified_head (format {d.get('format')}) — unguarded, nothing to check")
        sys.exit(0)
    ok, lines = guard(v, head, args.at)
    print(f"{v}:")
    for ln in lines:
        print("  " + ln)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
