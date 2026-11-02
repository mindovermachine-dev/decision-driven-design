#!/usr/bin/env python3
"""validate-core-order.py — v2: SDP ordering + graph transclusion for core/.

Layer contract:
  graph/  (YAML)  canonical claims and term definitions — source of truth
  docs    (md)    prose arguments; carry ddd:contract blocks; EMBED canonical
                  objects in their one canonical home, REF them everywhere else

Doc markers:
  <!-- ddd:contract ... -->                       (see v1 header format)
  <!-- ddd:embed id=term:closure -->
  ...exact canonical_md from the graph...
  <!-- /ddd:embed -->
  <!-- ddd:ref id=DDD-core-floor-01 -->           (no content requirement)

Ordering errors (E1–E5) as in v1. Transclusion errors:
  E6  embedded content does not byte-match canonical_md (edges whitespace-trimmed)
  E7  embed appears outside the object's canonical home
  E8  same id embedded more than once
  E9  embed or ref names an unknown graph id
  E10 contract `establishes` disagrees with terms registry (established_by
      mismatch, or registry term no doc establishes)
  E11 unclosed ddd:embed block
Warnings:
  W1  possible undeclared forward use (body linter; apply the deletion test)
  W2  required term never appears in body (stale import)
  W3  graph object never embedded in any core doc (claims without
      canonical_md are exempt — they simply don't participate)
  W4  established term has no graph entry yet (migration gap)

Usage: python3 validate-core-order.py [core-dir]   (graph read from <core-dir>/graph/)
Exit 1 on any error. Requires PyYAML.
"""

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML required: pip install pyyaml --break-system-packages", file=sys.stderr)
    sys.exit(1)

CONTRACT_RE = re.compile(r"<!--\s*ddd:contract\s*(.*?)-->", re.DOTALL)
FIELD_RE = re.compile(r"^(requires|establishes|instances|status)\s*:\s*(.*)$")
EMBED_OPEN_RE = re.compile(r"<!--\s*ddd:embed\s+id=([^\s>]+)\s*-->")
EMBED_CLOSE = "<!-- /ddd:embed -->"
REF_RE = re.compile(r"<!--\s*ddd:ref\s+id=([^\s>]+)\s*-->")


def term_key(term: str) -> str:
    return term.split("|")[0].strip().lower()


def term_pattern(term: str) -> re.Pattern:
    alts = [re.escape(a.strip()) for a in term.split("|") if a.strip()]
    alts = [a.replace(r"\-", r"[-\s]") for a in alts]
    return re.compile(r"\b(?:" + "|".join(alts) + r")(?:e?s)?\b", re.IGNORECASE)


def parse_contract(text: str):
    m = CONTRACT_RE.search(text)
    if not m:
        return None
    fields = {"requires": [], "establishes": [], "instances": [], "status": ""}
    for line in m.group(1).splitlines():
        fm = FIELD_RE.match(line.strip())
        if not fm:
            continue
        key, val = fm.group(1), fm.group(2).strip()
        if key == "status":
            fields["status"] = val
        else:
            fields[key] = [t.strip() for t in val.strip("[]").split(",") if t.strip()]
    return fields


def strip_markers(text: str) -> str:
    text = CONTRACT_RE.sub("", text)
    text = REF_RE.sub("", text)
    return text


def load_graph(core: Path):
    """Return {id: obj} with obj = {canonical_md, home, kind, term?, aliases?}.

    Sources, in order:
      <core>/graph/*.yaml       registries (terms:, claims: lists)
      <core>/claims/*.yaml      one claim per file (claim-format v1+); a claim
                                participates iff it carries canonical_md
    """
    objects = {}
    cdir = core / "claims"
    if cdir.is_dir():
        for cf in sorted(cdir.glob("*.yaml")):
            obj = yaml.safe_load(cf.read_text(encoding="utf-8")) or {}
            if not isinstance(obj, dict) or "canonical_md" not in obj:
                continue
            objects[obj.get("id", cf.stem)] = {
                "canonical_md": (obj.get("canonical_md") or "").strip(),
                "home": obj.get("canonical_home", ""),
                "kind": "claims",
                "term": "",
                "aliases": [],
                "file": f"claims/{cf.name}",
            }
    gdir = core / "graph"
    if not gdir.is_dir():
        return objects
    for gf in sorted(gdir.glob("*.yaml")):
        data = yaml.safe_load(gf.read_text(encoding="utf-8")) or {}
        for kind, key_home in (("terms", "established_by"), ("claims", "canonical_home")):
            for obj in data.get(kind, []) or []:
                oid = obj.get("id", "")
                objects[oid] = {
                    "canonical_md": (obj.get("canonical_md") or "").strip(),
                    "home": obj.get(key_home, ""),
                    "kind": kind,
                    "term": obj.get("term", ""),
                    "aliases": obj.get("aliases", []) or [],
                    "file": gf.name,
                }
    return objects


def find_embeds(text: str):
    """Yield (id, content, line, ok_closed)."""
    pos = 0
    while True:
        m = EMBED_OPEN_RE.search(text, pos)
        if not m:
            return
        line = text[: m.start()].count("\n") + 1
        end = text.find(EMBED_CLOSE, m.end())
        if end == -1:
            yield m.group(1), "", line, False
            return
        yield m.group(1), text[m.end():end].strip(), line, True
        pos = end + len(EMBED_CLOSE)


def main() -> int:
    core = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("core")
    docs = sorted(core.glob("[0-9][0-9]-*.md"))
    if not docs:
        print(f"no numbered core documents found under {core}/", file=sys.stderr)
        return 1

    graph = load_graph(core)
    errors, warnings = [], []
    contracts, established_by, order = {}, {}, {}
    embedded_ids = {}  # id -> doc name

    # ---- pass 1: contracts and term registry -------------------------------
    for i, p in enumerate(docs):
        order[p] = i
        c = parse_contract(p.read_text(encoding="utf-8"))
        if c is None:
            errors.append(f"E1 {p.name}: no ddd:contract block")
            continue
        contracts[p] = c
        for raw in c["establishes"]:
            k = term_key(raw)
            if k in established_by:
                errors.append(
                    f"E2 term '{k}' established by both "
                    f"{established_by[k][1].name} and {p.name}"
                )
            else:
                established_by[k] = (i, p, raw)
            if graph:
                gid = f"term:{k}"
                if gid not in graph:
                    warnings.append(
                        f"W4 {p.name}: establishes '{k}' with no graph entry {gid} "
                        f"yet (migration gap)"
                    )
                elif graph[gid]["home"] != p.name:
                    errors.append(
                        f"E10 {p.name}: establishes '{k}' but graph says "
                        f"established_by {graph[gid]['home'] or '(unset)'}"
                    )
        both = {term_key(t) for t in c["requires"]} & {term_key(t) for t in c["establishes"]}
        for k in sorted(both):
            errors.append(f"E5 {p.name}: '{k}' in both requires and establishes")

    if graph:
        declared = set(established_by)
        for gid, obj in graph.items():
            if obj["kind"] == "terms" and gid.removeprefix("term:") not in declared:
                errors.append(
                    f"E10 graph {obj['file']}: {gid} has no establishing doc contract"
                )

    # ---- pass 2: ordering + embeds/refs per doc ----------------------------
    for p, c in contracts.items():
        i = order[p]
        raw_text = p.read_text(encoding="utf-8")
        body = strip_markers(raw_text)

        for raw in c["requires"] + c["instances"]:
            k = term_key(raw)
            if k not in established_by:
                errors.append(f"E3 {p.name}: requires '{k}', established nowhere")
                continue
            j, q, _ = established_by[k]
            if j > i:
                errors.append(
                    f"E4 {p.name}: forward edge — requires '{k}' "
                    f"established later, in {q.name}"
                )
            elif j == i:
                errors.append(f"E5 {p.name}: '{k}' required from itself")
            if not term_pattern(raw).search(body):
                warnings.append(f"W2 {p.name}: requires '{k}' but never uses it")

        for oid, content, line, closed in find_embeds(raw_text):
            if not closed:
                errors.append(f"E11 {p.name}:{line}: unclosed ddd:embed ({oid})")
                continue
            if oid not in graph:
                errors.append(f"E9 {p.name}:{line}: embed of unknown id '{oid}'")
                continue
            if oid in embedded_ids:
                errors.append(
                    f"E8 {p.name}:{line}: '{oid}' already embedded in {embedded_ids[oid]}"
                )
                continue
            embedded_ids[oid] = p.name
            obj = graph[oid]
            if obj["home"] and obj["home"] != p.name:
                errors.append(
                    f"E7 {p.name}:{line}: '{oid}' embedded outside its "
                    f"canonical home {obj['home']}"
                )
            if content != obj["canonical_md"]:
                errors.append(
                    f"E6 {p.name}:{line}: '{oid}' drifted from graph — "
                    f"edit {obj['file']} and re-project, never the doc"
                )

        for m in REF_RE.finditer(raw_text):
            if m.group(1) not in graph:
                line = raw_text[: m.start()].count("\n") + 1
                errors.append(f"E9 {p.name}:{line}: ref to unknown id '{m.group(1)}'")

    for gid in graph:
        if gid not in embedded_ids:
            warnings.append(f"W3 graph object '{gid}' never embedded in any core doc")

    # ---- pass 3: body linter for undeclared forward use --------------------
    for k, (j, q, raw) in sorted(established_by.items(), key=lambda kv: kv[1][0]):
        gid = f"term:{k}"
        alias_raw = raw
        if gid in graph and graph[gid]["aliases"]:
            alias_raw = "|".join([graph[gid].get("term") or k] + graph[gid]["aliases"])
        pat = term_pattern(alias_raw)
        for p, c in contracts.items():
            if order[p] >= j:
                continue
            declared = {term_key(t) for t in c["requires"] + c["establishes"] + c["instances"]}
            if k in declared:
                continue
            body = strip_markers(p.read_text(encoding="utf-8"))
            m = pat.search(body)
            if m:
                line = body[: m.start()].count("\n") + 1
                warnings.append(
                    f"W1 {p.name}:{line}: uses '{m.group(0)}' before {q.name} "
                    f"establishes it — forward pointer or escaped edge? "
                    f"(apply the deletion test)"
                )

    for w in warnings:
        print(f"  warn  {w}")
    for e in errors:
        print(f"  FAIL  {e}")
    print(
        f"\n{len(docs)} documents, {len(established_by)} terms, "
        f"{len(graph)} graph objects, {len(embedded_ids)} embedded, "
        f"{len(errors)} errors, {len(warnings)} warnings"
    )
    if errors:
        print("core: FAILED — forward edges and drifted embeds are escaped seams")
        return 1
    print("core: OK — edges point backward, embeds match the graph")
    return 0


if __name__ == "__main__":
    sys.exit(main())
