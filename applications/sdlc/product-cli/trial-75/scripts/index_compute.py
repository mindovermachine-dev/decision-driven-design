"""Compute everything the index does not author: hashes, uses, edges, forward references,
cycles, depth and fan-in. Writes a Markdown report to stdout.

usage: index_compute.py <index.yaml> <repo root>
"""
import hashlib
import re
import subprocess
import sys

import yaml

idx_path, root = sys.argv[1], sys.argv[2]
idx = yaml.safe_load(open(idx_path, encoding="utf-8"))


def sections(path):
    """Ordered sections of a Markdown file: heading text -> body. Grain: every heading."""
    out, name, buf = [], "(before the first heading)", []
    fence = False
    for line in open(f"{root}/{path}", encoding="utf-8").read().splitlines():
        if line.startswith("```"):
            fence = not fence
        m = None if fence else re.match(r"#{1,4} (.+)$", line)
        if m:
            out.append((name, "\n".join(buf)))
            name, buf = m.group(1).strip(), [line]
        else:
            buf.append(line)
    out.append((name, "\n".join(buf)))
    return [(n, b) for n, b in out if b.strip()]


def blob(path):
    return subprocess.run(["git", "-C", root, "hash-object", path], capture_output=True, text=True).stdout.strip()


files = {m["id"]: m["path"] for m in idx["members"]}
imports = {m["id"]: m["path"] for m in idx["imports"]}
secs = {fid: sections(p) for fid, p in files.items()}
imp_heads = {iid: {n for n, _ in sections(p)} for iid, p in imports.items() if p}

problems = []
order = [(fid, n) for fid in files for n, _ in secs[fid]]
pos = {k: i for i, k in enumerate(order)}
body = {(fid, n): b for fid in files for n, b in secs[fid]}

# resolve homes
home = {}
for t in idx["terms"]:
    h = t.get("home")
    if h is None:
        home[t["term"]] = None
    elif h["in"] in files:
        key = (h["in"], h["heading"])
        if key not in pos:
            problems.append(f"home of '{t['term']}' not found: {h['heading']}")
        home[t["term"]] = ("member", key)
    else:
        hd = h.get("heading")
        if imports.get(h["in"]) and hd and hd not in imp_heads[h["in"]]:
            problems.append(f"home of '{t['term']}' not found in import {h['in']}: {hd}")
        home[t["term"]] = ("import", h["in"], hd)

# uses
uses = {t["term"]: [k for k in order if re.search(t["pattern"], body[k]) and k[1] not in t.get("other-sense-in", [])] for t in idx["terms"]}

# edges between member sections
edges = {k: set() for k in order}
ext = {k: set() for k in order}
unexplained = {k: set() for k in order}
forward = []
for term, ks in uses.items():
    h = home[term]
    for k in ks:
        if h is None:
            unexplained[k].add(term)
        elif h[0] == "import":
            ext[k].add(h[1])
        elif h[1] != k:
            edges[k].add(h[1])
            if pos[h[1]] > pos[k]:
                forward.append((term, k[1], h[1][1]))


p = print
p(f"# Computed from `{idx_path.split('/')[-1]}`\n")
p("**Computed, never edited by hand.** Regenerate it when the index or a listed file changes. "
  "The index model is accepted; the index content is proposed, so these results are provisional.\n")
p("Terms do not order the layers (Emil, 2026-11-12). This report is glossary coverage: which terms a "
  "reader meets in each section, and where each can be looked up.\n")
p("## Files and hashes\n")
p("| Role | File | Git blob |\n|---|---|---|")
for fid, path in files.items():
    p(f"| member | `{path}` | `{blob(path)}` |")
for iid, path in imports.items():
    p(f"| import | `{path}` | `{blob(path)}` |" if path else f"| import | {iid} (outside this repository) | n/a |")
ih = hashlib.sha256(open(idx_path, 'rb').read()).hexdigest()[:16]
p(f"\nIndex content hash (sha256, first 16): `{ih}`\n")

p("## Glossary coverage\n")
p("| Check | Result |\n|---|---|")
p(f"| Every home resolves to a heading | {'yes' if not problems else '; '.join(problems)} |")
nohome = sorted(t for t, h in home.items() if h is None and uses[t])
p(f"| Terms used with no explanation found | {len(nohome)}: {', '.join(nohome) or 'none'} |")
writ = sorted(t for t, h in home.items() if h and h[0] == 'import' and h[1] == 'writ')
p(f"| Terms explained outside this repository | {len(writ)}: {', '.join(writ)} |")
unused = sorted(t for t in uses if not uses[t])
p(f"| Indexed terms never used in the member files | {', '.join(unused) or 'none'} |\n")

p("## Glossary\n")
p("| Term | Look it up in | Section | Sections that use it |\n|---|---|---|---|")
for t in idx["terms"]:
    h = home[t["term"]]
    if h is None:
        where, sec = "**no explanation found**", "–"
    elif h[0] == "member":
        where, sec = f"`{files[h[1][0]].split('/')[-1]}`", h[1][1]
    else:
        path = imports[h[1]]
        where, sec = (f"`{path.split('/')[-1]}`" if path else f"{h[1]} (outside this repository)"), h[2] or "–"
    p(f"| {t['term']} | {where} | {sec} | {len(uses[t['term']])} |")

p("\n## What a reader meets, section by section\n")
p("For each section in reading order: the terms it uses and does not itself explain. "
  "A projection of the section must explain these where they appear, or point to the glossary.\n")
p("| # | Section | Terms met here and explained elsewhere | No explanation found |\n|---|---|---|---|")
for i, k in enumerate(order):
    met = sorted(t for t, ks in uses.items() if k in ks and home[t] is not None and not (home[t][0] == "member" and home[t][1] == k))
    p(f"| {i+1} | {k[1]} | {', '.join(met) or '–'} | {', '.join(sorted(unexplained[k])) or '–'} |")
