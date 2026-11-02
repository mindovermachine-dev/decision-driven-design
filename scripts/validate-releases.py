#!/usr/bin/env python3
# Ported from mindovermachine-dev/actor-indexed-determination at tag v5.15.2 (commit 084bce7;
# file last changed upstream at 1097055) under DDD-dec-84. Unchanged below this header.
# Upstream's example versions in the docstring (v5.5.0) are the principle repository's.
"""Validate release descriptors against the release format spec (spec/release-format.md).

Usage:
    validate-releases.py releases/              # directory of per-release YAML files
    validate-releases.py releases/v5.5.0.yaml   # a single descriptor

Exit code 0 = valid; 1 = violations printed to stderr.
Implements format versions 1 and 2. Format 2 adds the mandatory `ratified_head`
(spec §4, rule 7); the guard itself runs in scripts/check-release-head.py.
Descriptors validate against their declared version.
"""

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required: pip install pyyaml")

SUPPORTED_FORMATS = {1, 2}
VERSION_RE = re.compile(r"^v(\d+)\.(\d+)\.(\d+)$")
ID_RE = re.compile(r"^DDD-[a-z]+-\d{2}$")
SHA_RE = re.compile(r"^[0-9a-f]{7,40}$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

REPO = Path(__file__).resolve().parent.parent
CANON_DIRS = (REPO / "core" / "claims", REPO / "core" / "decisions")

errors = []


def err(where, msg):
    errors.append(f"  {where}: {msg}")


def known_canon_ids():
    """Every claim and decision ID the repo actually carries, by filename stem."""
    ids = set()
    for d in CANON_DIRS:
        if d.is_dir():
            ids.update(p.stem for p in d.glob("*.yaml"))
    return ids


def check_release(r, path, canon_ids):
    where = path.name
    if not isinstance(r, dict):
        err(where, "descriptor is not a YAML mapping")
        return None

    fmt = r.get("format")
    if fmt not in SUPPORTED_FORMATS:
        err(where, f"format missing or unsupported: {fmt!r}")
        return None

    # Rule 1: the version is the identity
    version = r.get("version")
    if not isinstance(version, str) or not VERSION_RE.match(version or ""):
        err(where, f"version missing or not v<major>.<minor>.<patch>: {version!r}")
        return None
    where = version
    if path.stem != version:
        err(where, f"filename {path.name!r} disagrees with version {version!r} "
                   f"(expected {version}.yaml)")

    # Rule 2: the title carries no version prefix
    title = r.get("title")
    if not isinstance(title, str) or not title.strip():
        err(where, "title missing")
    else:
        title = title.strip()
        if "\n" in title:
            err(where, "title must be one line")
        first = title.split(" ", 1)[0].rstrip(":—-").lower()
        if VERSION_RE.match(first):
            err(where, f"title starts with a version ({first}); the tag message is "
                       f"composed as '{version} — <title>', which would double it")

    # Rule 3: commit is optional; when present it must look like a SHA
    commit = r.get("commit")
    if commit is not None:
        if not isinstance(commit, str) or not SHA_RE.match(commit.strip().lower()):
            err(where, f"commit is not a hex SHA of 7-40 chars: {commit!r} "
                       "(omit it to tag wherever this file lands)")

    date = r.get("date")
    if date is not None and not DATE_RE.match(str(date)):
        err(where, f"date is not YYYY-MM-DD: {date!r}")

    # Rule 4: basis is mandatory and must resolve against the live repo
    basis = r.get("basis")
    if not basis:
        err(where, "basis missing or empty (a release cites the canon it pins)")
    elif not isinstance(basis, list):
        err(where, f"basis must be a list, got {type(basis).__name__}")
    else:
        for b in basis:
            if not isinstance(b, str) or not ID_RE.match(b):
                err(where, f"basis entry is not a DDD-<area>-<nn> id: {b!r}")
            elif b not in canon_ids:
                err(where, f"basis {b} does not resolve to core/claims/ or core/decisions/")

    # Rule 5: summary is mandatory
    summary = r.get("summary")
    if not isinstance(summary, str) or not summary.strip():
        err(where, "summary missing (release notes are written, not generated)")

    # Format 2, rule 7: ratified_head is mandatory and must look like a SHA.
    # The guard (ancestry and diff) needs git and runs in check-release-head.py.
    head = r.get("ratified_head")
    if fmt >= 2:
        if not isinstance(head, str) or not SHA_RE.match(head.strip().lower()):
            err(where, f"ratified_head missing or not a hex SHA of 7-40 chars: {head!r} "
                       "(format 2 records the head the principal ratified)")
    elif head is not None:
        err(where, "ratified_head is a format 2 field; declare format: 2 to use it")

    for flag in ("draft", "prerelease"):
        if flag in r and not isinstance(r[flag], bool):
            err(where, f"{flag} must be a boolean, got {r[flag]!r}")

    return version


def load(path):
    with open(path) as f:
        return yaml.safe_load(f)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        sys.exit(__doc__)
    target = Path(args[0])

    if target.is_dir():
        paths = sorted(target.glob("*.yaml"))
    elif target.exists():
        paths = [target]
    else:
        sys.exit(f"no such path: {target}")

    canon_ids = known_canon_ids()
    if not canon_ids:
        err("global", f"no claims or decisions found under {CANON_DIRS[0]} "
                      f"or {CANON_DIRS[1]} — cannot resolve basis")

    versions = []
    for p in paths:
        v = check_release(load(p), p, canon_ids)
        if v:
            versions.append(v)

    # Rule 1: versions are never reused
    dupes = {v for v in versions if versions.count(v) > 1}
    if dupes:
        err("global", f"duplicate versions: {sorted(dupes)}")

    if errors:
        print(f"INVALID — {len(errors)} violation(s) across {len(paths)} descriptor(s):",
              file=sys.stderr)
        print("\n".join(errors), file=sys.stderr)
        sys.exit(1)
    print(f"valid: {len(paths)} release descriptor(s), "
          "versions unique, basis resolves, format rules satisfied")


if __name__ == "__main__":
    main()
