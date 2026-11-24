"""Check the ddd-method plugin: names, the pin, and thinness.

    python3 plugins/ddd-method/check.py

Proposed in meta/sessions/2026-11-08-method-plugin/design.md §6 ([PROPOSED]). Standard library
only. Exit status is non-zero on any failure.

What it checks:
  1. names     the marketplace entry's name equals plugin.json's name (the install id and the
               skill prefix agree), and the entry's source is this plugin's directory;
  2. version   version is set in plugin.json and not in the marketplace entry, and its base (before
               any "+" suffix) is the skill's pin without its "v";
  3. pin       the skill declares exactly one pin, and every tag the skill names is that pin; the
               PIN line is the pin's one source (DDD-dec-121, Round 30), so every version named in
               the evals (graders, scaffold, descriptions), in this plugin's README and in the root
               README's plugin section is that pin (a version may carry a +p.N suffix), except an
               earlier pin's results kept between <!-- pin-history --> markers in this README;
  5. trees     the evals ran on what the pin holds: evals/pin-trees.json, written by
               pin_trees.py record, names the pin and each file the skill reads with its git
               object id; the closure is derived again at the pin (its tag, or HEAD while the tag
               is not cut) and must match path for path (Round 31, item 4; Round 33);
  4. thin      the skill holds no claim or decision id, and no run of RUN words in a row appears in
               both the skill and any file under method/ (Round 27: the skill carries procedure
               and discipline; cards and canon are read from the repository at the pin).
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

ROOT = Path(__file__).resolve().parents[2]
PLUGIN = Path(__file__).resolve().parent
SKILL = PLUGIN / "skills" / "run" / "SKILL.md"
RUN = 8

failures = 0


def report(ok, what):
    global failures
    print(f"{'ok  ' if ok else 'FAIL'} {what}")
    if not ok:
        failures += 1


def words(text):
    return re.findall(r"[a-z0-9]+(?:['’][a-z]+)?", text.lower())


def runs(ws, n):
    return {" ".join(ws[i:i + n]) for i in range(len(ws) - n + 1)}


def main():
    manifest = json.loads((PLUGIN / ".claude-plugin" / "plugin.json").read_text())
    market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text())
    entries = [e for e in market.get("plugins", []) if e.get("name") == manifest.get("name")]
    report(len(entries) == 1,
           f"names: one marketplace entry named {manifest.get('name')!r}, as in plugin.json")
    entry = entries[0] if entries else {}
    source = entry.get("source", "")
    report(isinstance(source, str) and (ROOT / source).resolve() == PLUGIN and ".." not in source,
           f"names: the entry's source {source!r} is {PLUGIN.relative_to(ROOT)}")

    skill = SKILL.read_text()
    pins = re.findall(r"^PIN: `(v\d+\.\d+\.\d+)`\s*$", skill, re.M)
    report(len(pins) == 1, f"pin: the skill declares one pin {pins}")
    pin = pins[0] if pins else None
    tags = set(re.findall(r"\bv\d+\.\d+\.\d+\b", skill))
    report(tags == {pin}, f"pin: every tag the skill names is the pin {sorted(tags)}")

    def mentions(text):
        # Versions named in a file, with any regex escaping undone: v0\.7\.0 reads as v0.7.0.
        return set(re.findall(r"\bv?(\d+\.\d+\.\d+)(?:\+p\.\d+)?\b", text.replace("\\.", ".")))
    readers = [f for f in sorted((PLUGIN / "evals").rglob("*"))
               if f.is_file() and "results" not in f.relative_to(PLUGIN).parts
               and f.suffix in {".md", ".yaml", ".sh"}]
    readers.append(PLUGIN / "README.md")
    stray = {}
    for f in readers:
        text = f.read_text()
        if f == PLUGIN / "README.md":
            # Earlier pins' eval results are kept as history (Rounds 29 and 32), only between
            # <!-- pin-history --> and <!-- /pin-history --> in this plugin's README.
            text = re.sub(r"<!-- pin-history -->.*?<!-- /pin-history -->", "", text, flags=re.S)
        other = mentions(text) - ({pin[1:]} if pin else set())
        if other:
            stray[str(f.relative_to(ROOT))] = sorted(other)
    root = (ROOT / "README.md").read_text()
    section = root.split("## Run it in Claude Code", 1)[1].split("\n## ", 1)[0] if "## Run it in Claude Code" in root else ""
    report(bool(section), "pin: the root README has its plugin section")
    other = mentions(section) - ({pin[1:]} if pin else set())
    if other:
        stray["README.md (Run it in Claude Code)"] = sorted(other)
    report(not stray, f"pin: the evals and both READMEs name only the pin {stray}")

    version = manifest.get("version")
    report("version" not in entry, "version: not set in the marketplace entry")
    report(bool(version) and pin is not None and version.split("+")[0] == pin[1:],
           f"version: plugin.json {version!r} tracks the pin {pin!r}")

    import pin_trees
    rec_path = PLUGIN / "evals" / "pin-trees.json"
    if not rec_path.exists():
        report(False, "trees: evals/pin-trees.json exists (run pin_trees.py record after the evals)")
    else:
        rec = json.loads(rec_path.read_text())
        report(rec.get("pin") == pin, f"trees: the record is for the pin {rec.get('pin')!r}")
        at = pin if pin and pin_trees.oid(pin, "method/README.md") else "HEAD"
        now = pin_trees.closure(at)
        diff = sorted(p for p in set(now) | set(rec.get("paths", {}))
                      if now.get(p) != rec.get("paths", {}).get(p))
        report(not diff, f"trees: the files the skill reads at {at} are the ones the evals ran on {diff[:5]}")

    ids = sorted(set(re.findall(r"\bDDD-[a-z]+-\d+\b", skill)))
    report(not ids, f"thin: no claim or decision id in the skill {ids}")
    skill_runs = runs(words(skill), RUN)
    shared = {}
    for card in sorted((ROOT / "method").glob("*.md")):
        common = skill_runs & runs(words(card.read_text()), RUN)
        if common:
            shared[card.name] = sorted(common)[:3]
    report(not shared, f"thin: no run of {RUN} words shared with method/ {shared}")

    print(f"\n{failures} failure(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
