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

# cycles: strongly connected components (Tarjan)
index, low, on, stack, sccs, counter = {}, {}, set(), [], [], [0]


def strong(v):
    index[v] = low[v] = counter[0]
    counter[0] += 1
    stack.append(v)
    on.add(v)
    for w in edges[v]:
        if w not in index:
            strong(w)
            low[v] = min(low[v], low[w])
        elif w in on:
            low[v] = min(low[v], index[w])
    if low[v] == index[v]:
        comp = []
        while True:
            w = stack.pop()
            on.discard(w)
            comp.append(w)
            if w == v:
                break
        sccs.append(comp)


for v in order:
    if v not in index:
        strong(v)
cycles = [sorted(c, key=pos.get) for c in sccs if len(c) > 1]
comp_of = {v: i for i, c in enumerate(sccs) for v in c}

# depth over the condensed graph
depth_c = {}


def depth(ci):
    if ci in depth_c:
        return depth_c[ci]
    depth_c[ci] = 0
    outs = {comp_of[w] for v in sccs[ci] for w in edges[v]} - {ci}
    depth_c[ci] = 1 + max((depth(o) for o in outs), default=-1)
    return depth_c[ci]


d = {v: depth(comp_of[v]) for v in order}
fan_in = {v: sum(1 for k in order if v in edges[k]) for v in order}

p = print
p(f"# Computed from `{idx_path.split('/')[-1]}`\n")
p("**Computed, never edited by hand.** Regenerate it when the index or a listed file changes. "
  "The index model is accepted; the index content is proposed, so these results are provisional.\n")
p("## Files and hashes\n")
p("| Role | File | Git blob |\n|---|---|---|")
for fid, path in files.items():
    p(f"| member | `{path}` | `{blob(path)}` |")
for iid, path in imports.items():
    p(f"| import | `{path}` | `{blob(path)}` |" if path else f"| import | {iid} (outside this repository) | n/a |")
ih = hashlib.sha256(open(idx_path, 'rb').read()).hexdigest()[:16]
p(f"\nIndex content hash (sha256, first 16): `{ih}`\n")

p("## Checks\n")
p("| Check | Result |\n|---|---|")
p(f"| Every home resolves to a heading | {'yes' if not problems else '; '.join(problems)} |")
nohome = sorted(t for t, h in home.items() if h is None and uses[t])
p(f"| Terms used with no explanation found | {len(nohome)}: {', '.join(nohome) or 'none'} |")
writ = sorted(t for t, h in home.items() if h and h[0] == 'import' and h[1] == 'writ')
p(f"| Terms whose home is outside this repository | {len(writ)}: {', '.join(writ)} |")
p(f"| Cycles between sections | {len(cycles)} |")
p(f"| Forward references (used before the home, in reading order) | {len(forward)} |")
unused = sorted(t for t in uses if not uses[t])
p(f"| Indexed terms never used in the member files | {', '.join(unused) or 'none'} |\n")

if cycles:
    p("## Cycles\n")
    p("Each group of sections below needs every other section in the group to be read first.\n")
    for c in cycles:
        p("- " + " ⇄ ".join(k[1] for k in c))
        for a in c:
            for b in c:
                if b in edges[a]:
                    ts = sorted(t for t, ks in uses.items() if a in ks and home[t] and home[t][0] == 'member' and home[t][1] == b)
                    p(f"  - \"{a[1]}\" needs \"{b[1]}\" for: {', '.join(ts)}")
    p("")

p("## Sections in reading order\n")
p("Depth 0 needs no other section of the set. A higher depth needs more read first. "
  "Fan-in is how many sections need this one.\n")
p("| # | Section | Depth | Fan-in | Needs (in the set) | Imports | No explanation found |\n|---|---|---|---|---|---|---|")
for i, k in enumerate(order):
    needs = ", ".join(x[1] for x in sorted(edges[k], key=pos.get)) or "–"
    p(f"| {i+1} | {k[1]} | {d[k]} | {fan_in[k]} | {needs} | {', '.join(sorted(ext[k])) or '–'} | {', '.join(sorted(unexplained[k])) or '–'} |")

p("\n## Forward references\n")
p("| Term | Used in | Explained later in |\n|---|---|---|")
for term, a, b in sorted(forward, key=lambda x: (pos[('definition', x[1])], x[0])):
    p(f"| {term} | {a} | {b} |")

p("\n## Paths\n")
p("A path is a term's home, then every section that uses the term, in reading order.\n")
for term in ("draft log", "proposal", "What-version record", "canonical document", "scenario"):
    h = home[term]
    p(f"- **{term}**: home \"{h[1][1]}\" → " + " → ".join(k[1] for k in uses[term] if k != h[1]))
