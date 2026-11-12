"""Project a canon Markdown file: inputs for the summary and glossary steps, and brief assembly.

usage:
  canon.py tree     <index.yaml> <root>
  canon.py leaves   <index.yaml> <root> <first-chapter> <last-chapter>   -> leaf input (stdout)
  canon.py glossin  <index.yaml> <root>                                  -> glossary input (stdout)
  canon.py topin    <index.yaml> <root> <summaries.yaml> <audience.md>   -> audience-top input
  canon.py check    <index.yaml> <root> <summaries.yaml>
  canon.py brief    <index.yaml> <root> <summaries.yaml> <glossary.yaml> <top.yaml> <audience-id> <projections.yaml>
  canon.py opening  <index.yaml> <root> <file.md> ...
"""
import re
import subprocess
import sys

import yaml

cmd, idx_path, root = sys.argv[1], sys.argv[2], sys.argv[3]
idx = yaml.safe_load(open(idx_path, encoding="utf-8"))
files = {m["id"]: m["path"] for m in idx["members"]}
imports = {m["id"]: m["path"] for m in idx["imports"]}
canon_path = files[idx["canon"]]


def read(path):
    return open(f"{root}/{path}", encoding="utf-8").read()


def parse_canon():
    """Document intro C0, chapters C<n> (CX when unnumbered), subsections C<n>.<i>."""
    doc = {"headline": None, "intro": [], "chapters": []}
    chap = sub = None
    fence = False
    for line in read(canon_path).splitlines():
        if line.startswith("```"):
            fence = not fence
        if not fence and line.startswith("# ") and doc["headline"] is None:
            doc["headline"] = line[2:].strip()
        elif not fence and line.startswith("## "):
            m = re.match(r"## (\d+)\. (.+)$", line)
            key, head = (f"C{m.group(1)}", m.group(2)) if m else ("CX", line[3:].strip())
            chap = {"key": key, "heading": line[3:].strip(), "title": head, "intro": [], "subs": []}
            doc["chapters"].append(chap)
            sub = None
        elif not fence and line.startswith("### ") and chap is not None:
            sub = {"key": f"{chap['key']}.{len(chap['subs']) + 1}", "heading": line[4:].strip(), "text": []}
            chap["subs"].append(sub)
        elif sub is not None:
            sub["text"].append(line)
        elif chap is not None:
            chap["intro"].append(line)
        else:
            doc["intro"].append(line)
    j = lambda ls: "\n".join(ls).strip()
    doc["intro"] = j(doc["intro"])
    for c in doc["chapters"]:
        c["intro"] = j(c["intro"])
        for s in c["subs"]:
            s["text"] = j(s["text"])
    return doc


doc = parse_canon()


def leaves():
    out = []
    for c in doc["chapters"]:
        if c["subs"]:
            for s in c["subs"]:
                rel = c["intro"] or doc["intro"]
                out.append({"key": s["key"], "heading": s["heading"], "chapter": c, "text": s["text"],
                            "relevance": rel, "limit": "at most 2 sentences and 50 words"})
        else:
            out.append({"key": c["key"], "heading": c["heading"], "chapter": c, "text": c["intro"],
                        "relevance": doc["intro"], "limit": "at most 3 sentences and 75 words"})
    return out


def blob(path):
    return subprocess.run(["git", "-C", root, "hash-object", path], capture_output=True, text=True).stdout.strip()


def heading_sections(path):
    out, name, buf, fence = {}, None, [], False
    for line in read(path).splitlines():
        if line.startswith("```"):
            fence = not fence
        m = None if fence else re.match(r"#{1,4} (.+)$", line)
        if m:
            if name:
                out[name] = "\n".join(buf).strip()
            name, buf = m.group(1).strip(), []
        else:
            buf.append(line)
    if name:
        out[name] = "\n".join(buf).strip()
    return out


def key_of_heading(h):
    for c in doc["chapters"]:
        if c["heading"] == h:
            return c["key"]
        for s in c["subs"]:
            if s["heading"] == h:
                return s["key"]
    return None


if cmd == "tree":
    print("C0 (introduction)", len(doc["intro"].split()), "words")
    for c in doc["chapters"]:
        print(c["key"], c["heading"], "| intro", len(c["intro"].split()), "w |", [s["key"] for s in c["subs"]])
    print("leaves:", len(leaves()))

elif cmd == "leaves":
    lo, hi = sys.argv[4], sys.argv[5]
    keys = [c["key"] for c in doc["chapters"]]
    sel = keys[keys.index(lo): keys.index(hi) + 1]
    p = print
    p("# Leaf input\n")
    p("Each part below is one leaf of the canon. Summarise each from its own text only.\n")
    for lf in leaves():
        if lf["chapter"]["key"] not in sel:
            continue
        p(f"\n---\n\n## PART {lf['key']} — {lf['heading']}\n")
        p(f"**Limit:** {lf['limit']}.\n")
        p("**Relevance (the introduction of the part that contains this one):**\n")
        p("> " + lf["relevance"].replace("\n", "\n> ") + "\n")
        p("**Text of the part:**\n")
        p(lf["text"] + "\n")

elif cmd == "glossin":
    p = print
    p("# Glossary input\n")
    p("For each term below, write its gloss from the text given for it and nothing else.\n")
    cache = {}
    for t in idx["terms"]:
        h = t.get("home")
        if not h or not (files.get(h["in"]) or imports.get(h["in"])):
            continue
        path = files.get(h["in"]) or imports[h["in"]]
        cache.setdefault(path, heading_sections(path))
        text = cache[path][h["heading"]]
        if len(text.split()) < 12 and path == canon_path:  # a chapter heading whose text sits in the chapter intro
            for c in doc["chapters"]:
                if c["heading"] == h["heading"]:
                    text = c["intro"]
        p(f"\n---\n\n## TERM: {t['term']}\n")
        if t.get("note"):
            p(f"Note from the index: {t['note']}\n")
        p(f"Explained in `{path.split('/')[-1]}`, section \"{h['heading']}\". Text of that section:\n")
        p(text + "\n")

elif cmd == "topin":
    sums = yaml.safe_load(open(sys.argv[4], encoding="utf-8"))["leaves"]
    aud = re.sub(r"\A---\n.*?\n---\n", "", open(sys.argv[5], encoding="utf-8").read(), flags=re.S).strip()
    p = print
    p("# Audience-top input\n")
    p("## Relevance (a reader)\n")
    p(aud + "\n")
    p("## The document's introduction (C0)\n")
    p(doc["intro"] + "\n")
    p("## Chapters, with the shared summaries of their leaves\n")
    for c in doc["chapters"]:
        p(f"### {c['key']} — {c['heading']}\n")
        if c["subs"]:
            if c["intro"]:
                p(f"Chapter introduction ({c['key']}): {c['intro']}\n")
            for s in c["subs"]:
                p(f"- {s['key']} ({s['heading']}): {sums[s['key']]['summary']}")
            p("")
        else:
            p(f"- {c['key']}: {sums[c['key']]['summary']}\n")

elif cmd == "check":
    sums = yaml.safe_load(open(sys.argv[4], encoding="utf-8"))["leaves"]
    problems = []
    for lf in leaves():
        e = sums.get(lf["key"])
        if not e:
            problems.append(f"{lf['key']}: missing")
            continue
        w = len(e["summary"].split())
        n = len(re.findall(r"[.!?](?:\s|$)", e["summary"].strip()))
        mw, ms = (50, 2) if "." in lf["key"] else (75, 3)
        if w > mw or n > ms:
            problems.append(f"{lf['key']}: {n} sentences, {w} words (limit {ms}, {mw})")
    extra = sorted(set(sums) - {lf["key"] for lf in leaves()})
    if extra:
        problems.append(f"unknown keys: {extra}")
    print("leaves:", len(leaves()), "summaries:", len(sums), "problems:", problems or "none")

elif cmd == "brief":
    sums = yaml.safe_load(open(sys.argv[4], encoding="utf-8"))
    gloss = yaml.safe_load(open(sys.argv[5], encoding="utf-8"))["glosses"]
    top = yaml.safe_load(open(sys.argv[6], encoding="utf-8"))
    audience = sys.argv[7]
    known = {c["key"] for c in doc["chapters"]} | {s["key"] for c in doc["chapters"] for s in c["subs"]} | {"C0"}
    KEYS = r"\[((?:C[\dX]+(?:\.\d+)?)(?:,\s*C[\dX]+(?:\.\d+)?)*)\]"
    sentences = []  # what the checker needs, kept beside the file and out of it

    def strip_keys(text, where):
        """Remove the citation keys from the text; record each sentence with the keys it rests on."""
        pos = 0
        for m in re.finditer(r"\s*" + KEYS, text):
            sent = text[pos:m.start()].strip().lstrip(".;, ").strip()
            sentences.append({"in": where, "sentence": sent, "cites": [k.strip() for k in m.group(1).split(",")]})
            pos = m.end()
        return re.sub(r"\s*" + KEYS, "", text).strip()

    lines = [f"# {top.get('headline') or doc['headline']}", "", strip_keys(top["document"]["summary"], "summary"), ""]
    lines += ["## Chapter by chapter", ""]
    left = []
    for c in doc["chapters"]:
        e = top["chapters"].get(c["key"])
        if e and e.get("summary"):
            lines.append(f"- **{c['title']}.** {strip_keys(e['summary'], c['key'])}")
        else:
            left.append(c["key"])
    body = "\n".join(lines)

    # terms: link the first use, then list what is used, each with its gloss and nothing else
    used = []
    for t in idx["terms"]:
        m = re.search(t["pattern"], body)
        if m:
            used.append((m.start(), t))
    used.sort(key=lambda x: x[0])
    offset, entries, sources = 0, [], []
    for start, t in used:
        m = re.compile(t["pattern"]).search(body, start + offset)
        anchor = "term-" + re.sub(r"[^a-z0-9]+", "-", t["term"].lower()).strip("-")
        if m and body[max(0, m.start() - 1)] != "[" and "`" not in body[max(0, m.start() - 1): m.end() + 1]:
            rep = f"[{m.group(0)}](#{anchor})"
            body = body[: m.start()] + rep + body[m.end():]
            offset += len(rep) - len(m.group(0))
        h = t.get("home")
        g = gloss.get(t["term"])
        if g and g.get("gloss"):
            path = files.get(h["in"]) or imports[h["in"]]
            entries.append(f"- <a id=\"{anchor}\"></a>**{t['term']}**: {g['gloss']}")
            sources.append({"term": t["term"], "from": path.split("/")[-1], "section": h["heading"]})
        else:
            entries.append(f"- <a id=\"{anchor}\"></a>**{t['term']}**: not explained in this definition.")
            why = "its home is Writ, outside this repository" if h and h["in"] == "writ" else "no explanation was found"
            sources.append({"term": t["term"], "from": None, "why": why})
    body += "\n\n## Terms used here\n\n" + "\n".join(entries) + "\n"

    cited = sorted({k for s in sentences for k in s["cites"]},
                   key=lambda k: [int(p) if p.isdigit() else 99 for p in re.split(r"\.", k[1:])])
    entry = {
        "file": f"{idx['set']}.en.brief.md", "format": "brief", "format-version": 4, "culture": "en",
        "reader": "human", "audience": audience,
        "derived-from": canon_path.split("/")[-1], "canon-blob": blob(canon_path),
        "summaries-of-canon-blob": sums["canon-blob"],
        "assembled-by": "script, from stored summaries, an audience top and the glossary",
        "cites": cited,
        "unknown-citations": [c for c in cited if c not in known],
        "chapters-left-out": left,
        "sentences": sentences,
        "terms": sources,
    }
    reg = ("# Everything about the files derived from this set's canon that their readers do not need: where each\n"
           "# came from, what each sentence rests on, where each gloss was taken from, what was left out.\n"
           "# Written by the script that assembles the files. A file for a human carries none of this (Emil, 2026-11-12).\n"
           + yaml.safe_dump({"set": idx["set"], "projections": [entry]}, sort_keys=False, allow_unicode=True, width=1000))
    open(sys.argv[8], "w", encoding="utf-8").write(reg)
    sys.stdout.write(body)

elif cmd == "opening":
    bad_start = re.compile(r"^(this (document|file|page|brief|report|description|is|was)|status\b|draft\b|trial\b|note\b|version\b|generated\b|derived\b|computed\b|last updated\b|current state\b|retired\b)", re.I)
    for path in [a for a in sys.argv[4:] if a != "--strict"]:
        lines = open(path, encoding="utf-8").read().splitlines()
        problems = []
        if lines and lines[0].strip() == "---":
            problems.append("starts with frontmatter")
        content = [l for l in lines if l.strip()]
        if not problems and (not content or not content[0].startswith("# ")):
            problems.append("first line is not a headline")
        first = next((l for l in content[1:] if not l.startswith("#")), "") if not problems else ""
        plain = re.sub(r"^[>*_\s\-|]+", "", first)
        if first.startswith(">") or first.startswith("|"):
            problems.append("opens with a note or a table, not with a sentence about the subject")
        elif bad_start.match(plain):
            problems.append(f"opens with information about the content: \"{plain[:60]}\"")
        text = "\n".join(lines)
        if re.search(r"\[C[\dX]+(\.\d+)?(,\s*C[\dX]+(\.\d+)?)*\]", text):
            problems.append("carries citation keys")
        if "--strict" in sys.argv and re.search(r"(?im)^\*?(derived from|provenance|computed from|generated by)", text):
            problems.append("carries provenance")
        print(("ok   " if not problems else "FAIL ") + path.split("/product-cli/")[-1] + ("" if not problems else "  — " + "; ".join(problems)))
