"""Check the ddd-method plugin: names, the pin, and thinness.

    python3 plugins/ddd-method/check.py

Proposed in meta/sessions/2026-11-08-method-plugin/design.md §6 ([PROPOSED]). Standard library
only. Exit status is non-zero on any failure.

What it checks:
  1. names     the marketplace entry's name equals plugin.json's name (the install id and the
               skill prefix agree), and the entry's source is this plugin's directory;
  2. version   version is set in plugin.json and not in the marketplace entry, and its base (before
               any "+" suffix) is the skill's pin without its "v";
  3. pin       the skill declares exactly one pin, and every tag the skill names is that pin;
  4. thin      the skill holds no claim or decision id, and no run of RUN words in a row appears in
               both the skill and any file under method/ (Round 27: the skill carries procedure
               and discipline; cards and canon are read from the repository at the pin).
"""
import json
import re
import sys
from pathlib import Path

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

    version = manifest.get("version")
    report("version" not in entry, "version: not set in the marketplace entry")
    report(bool(version) and pin is not None and version.split("+")[0] == pin[1:],
           f"version: plugin.json {version!r} tracks the pin {pin!r}")

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
