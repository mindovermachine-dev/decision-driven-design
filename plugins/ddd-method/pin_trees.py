"""The files the skill reads at its pin, and their git object ids (DDD-dec-121; Round 31, item 4).

    python3 plugins/ddd-method/pin_trees.py show   [<commit>]   # print the closure
    python3 plugins/ddd-method/pin_trees.py record <commit>     # write evals/pin-trees.json

The list is derived, not fixed (Round 33). From the commit it starts at method/README.md and takes:
  - the README's governing part: everything above its first line that is exactly "---";
  - every method/*.md file that part links (the live card), and that card's own links;
  - every relative link in those files, resolved, anchors dropped (a directory link is kept as a
    tree, a file link as a blob);
  - every claim or decision file they cite by id that exists at the commit;
  - graph/upstream.yaml, through which upstream ids are read.
Links to a not-live card are followed like any other: the skill reads a section of one when the
live card cites it. The closure is one level deep from the live card, as the skill reads.

`record` writes the commit the evals ran on and each path's object id. check.py recomputes the
closure at the pin (its tag if it exists, otherwise HEAD, the candidate a release branch carries)
and fails when a path or an id differs: then the evals did not run on what the pin holds.
Standard library and git only.
"""
import json
import posixpath
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RECORD = Path(__file__).resolve().parent / "evals" / "pin-trees.json"
LINK = re.compile(r"\]\(([^)\s]+)\)")
ID = re.compile(r"\bDDD-[a-z]+-\d+\b")


def git(*args):
    r = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True)
    return r.returncode, r.stdout


def show(commit, path):
    code, out = git("show", f"{commit}:{path}")
    return out if code == 0 else None


def oid(commit, path):
    code, out = git("rev-parse", "--verify", "-q", f"{commit}:{path.rstrip('/')}")
    return out.strip() if code == 0 else None


def links(text, base):
    found = set()
    for target in LINK.findall(text):
        target = target.split("#", 1)[0]
        if not target or re.match(r"^[a-z]+:", target):
            continue
        resolved = posixpath.normpath(posixpath.join(base, target))
        if not resolved.startswith(".."):
            found.add(resolved + ("/" if target.endswith("/") else ""))
    return found


def ids(commit, text):
    found = set()
    for i in ID.findall(text):
        for path in (f"core/claims/{i}.yaml", f"core/decisions/{i}.yaml"):
            if oid(commit, path):
                found.add(path)
    return found


def closure(commit):
    readme = show(commit, "method/README.md")
    if readme is None:
        raise SystemExit(f"method/README.md is not at {commit}")
    governing = re.split(r"(?m)^---\s*$", readme, maxsplit=1)[0]
    paths = {"method/README.md", "graph/upstream.yaml"}
    first = links(governing, "method")
    live = sorted(p for p in first if p.startswith("method/") and p.endswith(".md"))
    paths |= first | ids(commit, governing)
    for card in live:
        text = show(commit, card) or ""
        paths |= links(text, posixpath.dirname(card)) | ids(commit, text)
    return {p: oid(commit, p) for p in sorted(paths)}


def main(argv):
    mode = argv[1] if len(argv) > 1 else "show"
    commit = argv[2] if len(argv) > 2 else "HEAD"
    code, sha = git("rev-parse", "--verify", f"{commit}^{{commit}}")
    if code:
        raise SystemExit(f"not a commit: {commit}")
    found = closure(commit)
    if mode == "show":
        for p, o in found.items():
            print(f"{o or 'MISSING':40}  {p}")
    elif mode == "record":
        skill = (Path(__file__).resolve().parent / "skills" / "run" / "SKILL.md").read_text()
        pin = re.search(r"^PIN: `(v\d+\.\d+\.\d+)`\s*$", skill, re.M).group(1)
        RECORD.write_text(json.dumps({"pin": pin, "evaluated_commit": sha.strip(), "paths": found},
                                     indent=2) + "\n")
        print(f"recorded {len(found)} paths at {sha.strip()[:12]} for {pin}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
