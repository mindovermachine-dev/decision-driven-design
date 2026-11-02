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
  W3  graph object WITH a canonical_md is embedded nowhere (registry-only
      objects — terms/claims without canonical_md — are exempt by design)
  W4  established term has no graph entry yet (migration gap)
  W6  a pinned upstream object's CONTENT moved while its status held — the
      statement-moved-silently case (DDD-dec-16, DDD-dec-18); also fires for a
      pin carrying no content_hash at all, which is an uninstrumented pin
  W7  a local term id shadows an id in the pinned upstream registry with no
      governing decision cited (DDD-dec-22); suppress by adding
      shadows_upstream: <decision-id> to the local entry

Usage: python3 validate-core-order.py [core-dir]   (graph read from <core-dir>/graph/)
Exit 1 on any error. Requires PyYAML.
"""

import hashlib
import os
import re
import subprocess
import sys
import tempfile
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


# ============================================================================
# DDD fork: cross-repo upstream resolution (E12 / E13 / W5)
#
# decision-driven-design is the software projection; the actor-general canon lives upstream in
# the principle repo. graph/upstream.yaml pins every upstream id this repo depends on, at a
# version (a tag) AND a status. Remote resolution is a SHALLOW CLONE of the pinned ref into a
# temp dir — never a live network fetch inside the checker — so the check is reproducible and
# offline-cacheable, and the checker has no opinion about network availability.
# ============================================================================

REF_RE_ID = re.compile(r"<!--\s*ddd:ref\s+id=([^\s>]+)\s*-->")


def load_upstream_graph(clone_dir: Path):
    """Index every upstream object by id: {id: {status, canonical_md}}.

    Unlike load_graph (which only indexes embed-participating claims), E12/W5 need *every*
    claim id and its status, whether or not it carries canonical_md. Terms come from the
    graph registry; claims from core/claims/*.yaml.
    """
    core = clone_dir / "core"
    objs = {}
    cdir = core / "claims"
    if cdir.is_dir():
        for cf in sorted(cdir.glob("*.yaml")):
            d = yaml.safe_load(cf.read_text(encoding="utf-8")) or {}
            if not isinstance(d, dict) or "id" not in d:
                continue
            objs[d["id"]] = {
                "status": str(d.get("status", "")),
                "canonical_md": (d.get("canonical_md") or "").strip(),
                "statement": (d.get("statement") or "").strip(),
                "region": (d.get("region") or "").strip(),
            }
    gdir = core / "graph"
    if gdir.is_dir():
        for gf in sorted(gdir.glob("*.yaml")):
            data = yaml.safe_load(gf.read_text(encoding="utf-8")) or {}
            for term in data.get("terms", []) or []:
                if "id" in term:
                    objs[term["id"]] = {
                        "status": str(term.get("status", "")),
                        "canonical_md": (term.get("canonical_md") or "").strip(),
                        "statement": (term.get("statement") or "").strip(),
                        "region": (term.get("region") or "").strip(),
                    }
            for claim in data.get("claims", []) or []:
                if "id" in claim:
                    objs[claim["id"]] = {
                        "status": str(claim.get("status", "")),
                        "canonical_md": (claim.get("canonical_md") or "").strip(),
                        "statement": (claim.get("statement") or "").strip(),
                        "region": (claim.get("region") or "").strip(),
                    }
    return objs


def pinned_content_digest(obj: dict) -> str:
    """sha256 over the fields a pin is instrumented on: statement, region, canonical_md.

    Status is NOT hashed — W5 already instruments it, and folding it in here would make one
    class fire twice for the same movement. What this covers is the case W5 cannot see: a
    pinned claim whose statement or region moves while its status holds, observed twice
    (DDD-dec-16 on DDD-floor-01 at v5.4, DDD-dec-18 on DDD-cost-09 at v5.5) and silent both
    times. Fields are joined with a separator that cannot occur in YAML block scalars, so
    moving text between fields changes the digest.
    """
    parts = [obj.get("statement", ""), obj.get("region", ""), obj.get("canonical_md", "")]
    return "sha256:" + hashlib.sha256("\x00".join(parts).encode("utf-8")).hexdigest()


def resolve_upstream(upstream_yaml: Path, errors, warnings):
    """Shallow-clone the pinned ref and return (graph, pins). graph is None if unavailable."""
    spec = yaml.safe_load(upstream_yaml.read_text(encoding="utf-8")) or {}
    up = spec.get("upstream", {})
    repo, ref = up.get("repo", ""), up.get("ref", "")
    pins = up.get("pins", []) or []
    if not repo or not ref:
        errors.append(f"E12 {upstream_yaml}: upstream repo/ref not specified")
        return None, pins
    # allow a pre-cloned dir (CI cache / offline) via env, else shallow-clone
    pre = os.environ.get("DDD_UPSTREAM_DIR")
    if pre and Path(pre).is_dir():
        return load_upstream_graph(Path(pre)), pins
    tmp = Path(tempfile.mkdtemp(prefix="ddd-upstream-"))
    # --branch resolves a tag or a branch; --depth 1 keeps it shallow
    r = subprocess.run(
        ["git", "clone", "--depth", "1", "--branch", ref, repo, str(tmp)],
        capture_output=True, text=True,
    )
    if r.returncode != 0:
        errors.append(
            f"E12 upstream clone failed for {repo}@{ref} — cannot resolve pins "
            f"(set DDD_UPSTREAM_DIR to a local checkout to check offline). "
            f"git: {r.stderr.strip().splitlines()[-1] if r.stderr.strip() else 'unknown'}"
        )
        return None, pins
    return load_upstream_graph(tmp), pins


def load_pinned_ids(repo_root: Path):
    """The pin ids from graph/upstream.yaml, read locally (no clone). Pinned upstream ids
    satisfy requires/refs in local docs: upstream precedes every local doc in the reading
    order, so the cross-repo edge points backward by construction."""
    upstream_yaml = repo_root / "graph" / "upstream.yaml"
    if not upstream_yaml.is_file():
        return set()
    spec = yaml.safe_load(upstream_yaml.read_text(encoding="utf-8")) or {}
    return {p.get("id", "") for p in (spec.get("upstream", {}).get("pins", []) or [])}


def check_upstream(repo_root: Path, errors, warnings, local_ids=frozenset()):
    """Run E12/E13/W5 over graph/upstream.yaml against a shallow clone of the pinned ref.
    local_ids: ids in this repo's own graph — embeds/refs of those are checked by the local
    passes (E6-E9), not against upstream."""
    upstream_yaml = repo_root / "graph" / "upstream.yaml"
    if not upstream_yaml.is_file():
        return
    graph, pins = resolve_upstream(upstream_yaml, errors, warnings)
    if graph is None:
        return

    pinned = {}
    for pin in pins:
        oid = pin.get("id", "")
        pinned[oid] = pin.get("status_at_pin", "")
        # E12: pinned id must still exist upstream at ref
        if oid not in graph:
            errors.append(f"E12 pinned id '{oid}' no longer exists upstream at the pinned ref")
            continue
        # W5: basis loss — upstream status moved since the pin was set
        up_status = graph[oid].get("status", "")
        if up_status and pin.get("status_at_pin") and up_status != pin["status_at_pin"]:
            warnings.append(
                f"W5 basis loss: '{oid}' is '{up_status}' upstream but pinned at "
                f"'{pin['status_at_pin']}' — a decision basedOn it is escaped until the pin "
                f"is consciously advanced"
            )
        # W6: content movement — the case status cannot see (DDD-dec-16, DDD-dec-18)
        pinned_digest = pin.get("content_hash", "")
        live_digest = pinned_content_digest(graph[oid])
        if not pinned_digest:
            warnings.append(
                f"W6 uninstrumented pin: '{oid}' carries no content_hash — its statement and "
                f"region can move at the pinned ref with nothing firing. Add "
                f"content_hash: {live_digest}"
            )
        elif pinned_digest != live_digest:
            warnings.append(
                f"W6 pinned content moved: '{oid}' is pinned at content_hash "
                f"{pinned_digest} but resolves to {live_digest} at the ref — the statement or "
                f"region moved while the status held. Read the change, then advance the pin "
                f"consciously (a governed decision, not a mechanical bump)"
            )

    # E13: any DDD doc that EMBEDS a pinned id must match upstream canonical_md byte-for-byte;
    #      any ddd:ref to an unpinned/unknown id is a dangling cross-repo reference.
    for p in sorted(repo_root.rglob("*.md")):
        if ".git" in p.parts or "migration" in p.parts:
            continue
        text = p.read_text(encoding="utf-8")
        for oid, content, line, closed in find_embeds(text):
            if oid in local_ids:
                continue  # local graph object — checked by the local passes
            if oid not in pinned:
                errors.append(f"E13 {p.relative_to(repo_root)}:{line}: embeds unpinned upstream id '{oid}'")
                continue
            if oid not in graph:
                continue  # already E12'd
            if content != graph[oid].get("canonical_md", ""):
                errors.append(
                    f"E13 {p.relative_to(repo_root)}:{line}: '{oid}' embed drifted from upstream "
                    f"canonical_md at the pinned ref — re-project from upstream, never edit here"
                )
        for m in REF_RE_ID.finditer(text):
            oid = m.group(1)
            if oid in local_ids:
                continue  # local graph object — checked by the local passes
            if oid not in pinned:
                line = text[: m.start()].count("\n") + 1
                warnings.append(
                    f"W5 {p.relative_to(repo_root)}:{line}: ddd:ref to '{oid}' is not pinned in "
                    f"graph/upstream.yaml — add a pin or the reference is unversioned"
                )

    # W7: local term ids that shadow the pinned upstream registry.
    #     Ranges over the WHOLE upstream registry, never the pin list — the instance that
    #     motivated this rule (term:maturation) is not pinned, so a pin-scoped check would
    #     miss the one case it exists for (DDD-dec-22, on Emil's ruling of 2026-08-10).
    shadowed = 0
    for gf in sorted((repo_root / "core" / "graph").glob("*.yaml")):
        data = yaml.safe_load(gf.read_text(encoding="utf-8")) or {}
        for entry in (data.get("terms", []) or []) + (data.get("claims", []) or []):
            oid = entry.get("id", "")
            if not oid or oid not in graph:
                continue
            shadowed += 1
            governing = entry.get("shadows_upstream", "")
            if not governing:
                warnings.append(
                    f"W7 undeclared shadow: '{oid}' is established locally "
                    f"({entry.get('established_by', 'unknown doc')}) and also exists in the "
                    f"upstream registry at the pinned ref, with no governing decision cited. "
                    f"Establishing an id that collides with pinned upstream requires an "
                    f"explicit decision — add shadows_upstream: <decision-id>, or rename"
                )

    print(
        f"  upstream  {len(pins)} pins resolved against the pinned ref, "
        f"{sum(1 for w in warnings if w.startswith('W5'))} basis-loss, "
        f"{sum(1 for w in warnings if w.startswith('W6'))} content-drift, "
        f"{shadowed} shadowed id(s)"
    )


def main() -> int:
    core = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("core")
    repo_root = core.parent if core.name == "core" else Path(".")
    docs = sorted(core.glob("[0-9][0-9]-*.md"))
    # DDD fork: no numbered core docs here (canon is upstream). Run upstream checks only.
    if not docs:
        errors, warnings = [], []
        check_upstream(repo_root, errors, warnings)
        for w in warnings:
            print(f"  warn  {w}")
        for e in errors:
            print(f"  FAIL  {e}")
        print(f"\nupstream-only mode: {len(errors)} errors, {len(warnings)} warnings")
        if errors:
            print("upstream: FAILED — pins do not resolve or embeds drifted")
            return 1
        print("upstream: OK — every pin resolves at the pinned ref; no drift")
        return 0

    graph = load_graph(core)
    pinned_ids = load_pinned_ids(repo_root)
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
                if f"term:{k}" in pinned_ids:
                    # established upstream, pinned — a backward edge by construction
                    if not term_pattern(raw).search(body):
                        warnings.append(f"W2 {p.name}: requires '{k}' but never uses it")
                    continue
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
            if m.group(1) not in graph and m.group(1) not in pinned_ids:
                line = raw_text[: m.start()].count("\n") + 1
                errors.append(f"E9 {p.name}:{line}: ref to unknown id '{m.group(1)}'")

    for gid, obj in graph.items():
        if gid not in embedded_ids and obj.get("canonical_md"):
            warnings.append(
                f"W3 graph object '{gid}' has a canonical_md but is embedded nowhere "
                f"(registry-only objects — no canonical_md — are exempt)"
            )

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

    # ---- pass 4: cross-repo upstream resolution (E12/E13/W5) ---------------
    check_upstream(repo_root, errors, warnings, local_ids=set(graph))

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
