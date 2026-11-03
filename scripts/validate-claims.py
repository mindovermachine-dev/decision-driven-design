#!/usr/bin/env python3
"""Validate claim files against the claim format spec (spec/claim-format.md).

Usage:
    validate-claims.py meta/seed/claims-seed.yaml     # single seed file with a claims: list
    validate-claims.py core/claims/                    # directory of per-claim YAML files
    validate-claims.py core/decisions/ --decisions     # directory of decision files (minimal checks)

The seed is a frozen pre-conversion snapshot and it FAILS these checks, by design
and not by oversight: it carries DDD-measure-06 at `established` with no falsifier,
which is the defect that produced these checks and which survived five minor
versions in canon. Run against the seed, falsifier-presence catches it on the first
try. The seed is history and is not repaired -- supersession, never rewriting -- so
its exit 1 is a true report about v4.5 and not a regression. CI validates
core/claims/ and core/decisions/ only.

Exit code 0 = valid; 1 = violations printed to stderr.
Implements format version 1. New format versions extend SUPPORTED_FORMATS
with their own rule set; claims validate against their declared version.

Two classes of finding, and the difference is a ruling rather than a taste:

  error    the claim is invalid. Exit 1. A check is error class only when its
           hit list against the existing corpus is empty or already migrated --
           a check that fires on ratified claims needs a migration plan, not a
           merge.
  warning  printed, exit unaffected. Either a rule with a known backlog, or a
           heuristic that locates candidates for a human rather than deciding.

CHECK_CLASS below is the whole of that policy, one line per check, so promoting
a check is a one-word reviewable change and never a silent one.
"""

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required: pip install pyyaml")

SUPPORTED_FORMATS = {1}
STATUSES = {"projected", "reported", "established", "retired"}
LIVE_STATUSES = {"projected", "reported", "established"}
KINDS = {"formal", "empirical", "conceptual", "normative"}
TEST_KINDS = {"conceptual", "normative"}
RETIRED_FROM = {"established", "reported", "projected", "unrecoverable"}
ID_RE = re.compile(r"^DDD-[a-z]+-\d{2}$")

# Every mutual-information term carries a semicolon -- I(V;X) -- and each one is a
# false positive for a clause-joining detector. Parentheticals are stripped before
# any limb counting; without this the detector fires on six claims for their
# notation alone, two of them established.
PARENTHETICAL = re.compile(r"\([^()]*\)")

# The class of each non-mandatory check. See the module docstring; changing a value
# here is a ruling and should arrive with the hit list that justifies it.
CHECK_CLASS = {
    # Rule 2 extended from projected to every live status. Hit list: 0 of 89.
    # Rule 2 required a falsifier for `projected` and said nothing above it, so THE
    # STRONGEST STATUS CANON OFFERS CARRIED THE WEAKEST EVIDENTIAL REQUIREMENT --
    # which is exactly how DDD-measure-06 sat at established from v4.5 to v5.9 with
    # no stated observation that would fire against it. The rule now binds where the
    # defect was.
    "falsifier-presence": "error",
    # Every live claim carries a falsifier, `test` no substitute. Hit list: 7 of 89,
    # all conceptual or normative, all carrying a test. Warning until those seven
    # are written; the ruling that promotes it is the one that lands the last of them.
    "falsifier-strict": "warning",
    # Rule 1. Not mechanically decidable -- see single_limb(). Hit list: 34 of 89
    # with an inspected false-positive rate around a third. A drafting prompt, and
    # NEVER an error: it fires on DDD-measure-16, the claim built to cure
    # DDD-measure-06's compoundness.
    "single-limb": "warning",
    # A retired claim records the maturity it held. Hit list: 0 of 89 -- the four
    # retired claims carry the field, and `unrecoverable` is always available, so
    # the rule can never be unsatisfiable.
    "retired-from": "error",
    # DDD-dec-111: a decision's basedOn and basis entries resolve to a file in core/claims/ or
    # core/decisions/, a pin in graph/upstream.yaml, or a term in core/graph/terms.yaml. Hit list
    # 2026-11-03: 14 entries in 12 of 86 decisions, all upstream ids not pinned here. They are
    # recorded in graph/unresolved-basis.yaml, the migration, and report at the warning class
    # below; every other unresolved entry is an error.
    "basis-resolves": "error",
    "basis-resolves-recorded": "warning",
}

errors = []
warnings = []


def err(where, msg):
    errors.append(f"  {where}: {msg}")


def flag(check, where, msg):
    """Record a finding at the class CHECK_CLASS gives it."""
    line = f"  {where}: [{check}] {msg}"
    (errors if CHECK_CLASS[check] == "error" else warnings).append(line)


def single_limb(statement):
    """Rule 1's proxy: clause-joining punctuation outside mathematical notation.

    There is no mechanical test for "one proposition", and the gap between that
    and what is counted here is the reason this check cannot be an error. It
    reports candidates; a human rules. Two known kinds of miss, both inspected:
    a semicolon following a colon usually separates two glosses of one
    proposition rather than two propositions, and a scoping clause reads as a
    second limb without asserting beside the first.

    RETIRED CLAIMS ARE EXEMPT, and the reason is here rather than at the call
    site because the next person to widen a rule will read it here. A retired
    claim's `statement` is a retirement record, not a proposition -- canon
    rewrites it as RETIRED -- "<the dead claim>" (DDD-frame-09 and
    DDD-measure-08 are the exemplars). DDD-measure-06's epitaph quotes VERBATIM
    the compound statement that killed it, so running rule 1 over it flags the
    record of the defect as though it were the defect. Rule 1 governs
    propositions, and an epitaph is not one.
    """
    s = " ".join(str(statement).split())
    prev = None
    while prev != s:
        prev, s = s, PARENTHETICAL.sub(" ", s)
    s = re.sub(r"^RETIRED — ", "", s)
    return s.count(";")


def check_claim(c, where, default_format=None):
    fmt = c.get("format", default_format)
    if fmt not in SUPPORTED_FORMATS:
        err(where, f"format missing or unsupported: {fmt!r}")
        return
    cid = c.get("id", "<no id>")
    where = cid
    if not ID_RE.match(cid):
        err(where, f"id does not match DDD-<area>-<nn>: {cid!r}")
    if c.get("kind") not in KINDS:
        err(where, f"kind missing or illegal: {c.get('kind')!r}")
    status = c.get("status")
    if status not in STATUSES:
        err(where, f"status missing or illegal: {status!r}")
        return
    if not c.get("statement"):
        err(where, "statement missing")
    if not c.get("region"):
        err(where, "region missing (rule 5: 'everywhere' must be written to be claimed)")
    if not c.get("changed"):
        err(where, "changed missing (staleness pin)")

    evidence = c.get("evidence") or []
    # Rule 2: status entry conditions
    if status in ("reported", "established") and not evidence:
        err(where, f"status '{status}' requires at least one evidence entry")
    if status == "established" and not any(
        e.get("kind") in ("derivation",) for e in evidence if isinstance(e, dict)
    ):
        err(where, "status 'established' requires a derivation evidence entry "
                   "(credits filled if the theorem is borrowed)")
    if status == "retired" and not (c.get("supersedes") or c.get("notes")):
        err(where, "retired claim requires supersedes or a notes entry naming what killed it")

    # Rule 2's falsifier condition, held for every live status rather than for
    # projected alone. A definition's falsifier is its `test` -- the spec's three
    # test forms (counterexamples, coding reliability, explanatory utility) are the
    # three definitional failure modes -- so `test` satisfies this for the kinds the
    # spec gives it to, and for no others.
    if status in LIVE_STATUSES:
        if not c.get("falsifier") and not (c.get("kind") in TEST_KINDS and c.get("test")):
            flag("falsifier-presence", where,
                 f"status '{status}' requires falsifier"
                 + (" (or test, for conceptual/normative kinds)"
                    if c.get("kind") in TEST_KINDS else ""))
        elif not c.get("falsifier"):
            flag("falsifier-strict", where,
                 f"{c.get('kind')} claim at '{status}' carries test and no falsifier; "
                 "every claim carries one, with no near-definitional exception")

    # Rule 1, as a drafting prompt. Never promote this to error without an
    # adjudication of its hit list: it fires on sound claims.
    # Retired claims are exempt -- see single_limb()'s docstring for why.
    limbs = single_limb(c.get("statement", "")) if status in LIVE_STATUSES else 0
    if limbs:
        flag("single-limb", where,
             f"statement joins ~{limbs + 1} limbs (rule 1: one proposition per claim). "
             "Candidate for adjudication, not a verdict")

    # Retirement provenance. `unrecoverable` is a value and not a gap, so the rule
    # is always satisfiable and nothing here licenses inferring a status.
    rf = c.get("retired_from")
    if status == "retired" and not rf:
        flag("retired-from", where,
             "retired claim requires retired_from "
             f"({' | '.join(sorted(RETIRED_FROM))}); use 'unrecoverable' where the "
             "prior maturity cannot be established, and record the search in notes")
    if rf is not None:
        if status != "retired":
            flag("retired-from", where,
                 f"retired_from is legal only on a retired claim (status is '{status}')")
        if rf not in RETIRED_FROM:
            flag("retired-from", where, f"retired_from illegal: {rf!r}")
        if rf == "unrecoverable" and not c.get("notes"):
            flag("retired-from", where,
                 "retired_from 'unrecoverable' requires a notes entry recording what was "
                 "searched (that the notes do record it is not mechanically checkable)")


REPO = Path(__file__).resolve().parent.parent
_RESOLVABLE = None


def resolvable():
    """What a basedOn entry may name (DDD-dec-111), from the live repository, as validate-releases.py
    resolves a release's basis: claim and decision file stems, upstream pins, local terms; and the
    (decision, entry) pairs recorded in graph/unresolved-basis.yaml."""
    global _RESOLVABLE
    if _RESOLVABLE is None:
        ids = {p.stem for d in ("core/claims", "core/decisions") for p in (REPO / d).glob("*.yaml")}
        upstream = REPO / "graph" / "upstream.yaml"
        if upstream.exists():
            ids |= {p["id"] for p in ((load(upstream) or {}).get("upstream") or {}).get("pins") or []}
        terms = REPO / "core" / "graph" / "terms.yaml"
        if terms.exists():
            ids |= {t["id"] for t in (load(terms) or {}).get("terms") or []}
        recorded = REPO / "graph" / "unresolved-basis.yaml"
        pairs = set()
        if recorded.exists():
            pairs = {(e["decision"], e["entry"]) for e in (load(recorded) or {}).get("entries") or []}
        _RESOLVABLE = (ids, pairs)
    return _RESOLVABLE


def check_decision(d, where):
    """Minimal decision checks per ontology rule 1: no escaped decisions; and, by DDD-dec-111, a
    basedOn that resolves."""
    did = d.get("id", where)
    if not d.get("principal"):
        err(did, "decision has no accountable principal (escaped decision)")
    basis = d.get("basis") or d.get("basedOn") or []
    if not basis:
        err(did, "decision has no basedOn edges (escaped decision)")
    if not d.get("resolution"):
        err(did, "decision has no resolution")
    if not d.get("made"):
        err(did, "decision has no made timestamp/context")
    ids, recorded = resolvable()
    for key in ("basedOn", "basis"):
        entries = d.get(key)
        if entries is None:
            continue
        for e in entries if isinstance(entries, list) else [entries]:
            if e in ids:
                continue
            if (d.get("id"), e) in recorded:
                flag("basis-resolves-recorded", did,
                     f"{key} {e!r} does not resolve; recorded in graph/unresolved-basis.yaml "
                     "for Emil's ruling (DDD-dec-111)")
            else:
                flag("basis-resolves", did,
                     f"{key} {e!r} resolves to no file in core/claims/ or core/decisions/, no pin in "
                     "graph/upstream.yaml and no term in core/graph/terms.yaml (DDD-dec-111)")


def load(path):
    with open(path) as f:
        return yaml.safe_load(f)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    as_decisions = "--decisions" in sys.argv
    if not args:
        sys.exit(__doc__)
    target = Path(args[0])

    items, default_format = [], None
    if target.is_dir():
        for p in sorted(target.glob("*.yaml")):
            data = load(p)
            items.append((data, str(p)))
    else:
        data = load(target)
        if isinstance(data, dict) and "claims" in data:
            default_format = data.get("format")
            items = [(c, target.name) for c in data["claims"]]
        elif isinstance(data, dict) and "decisions" in data:
            items = [(d, target.name) for d in data["decisions"]]
            as_decisions = True
        else:
            items = [(data, target.name)]

    ids = []
    for item, where in items:
        if as_decisions:
            check_decision(item, where)
        else:
            check_claim(item, where, default_format)
        if isinstance(item, dict) and item.get("id"):
            ids.append(item["id"])

    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        err("global", f"duplicate ids: {sorted(dupes)}")

    kind = "decisions" if as_decisions else "claims"
    if warnings:
        print(f"{len(warnings)} warning(s) across {len(items)} {kind} "
              "— reported, not fatal:", file=sys.stderr)
        print("\n".join(warnings), file=sys.stderr)
    if errors:
        print(f"INVALID — {len(errors)} violation(s) across {len(items)} {kind}:",
              file=sys.stderr)
        print("\n".join(errors), file=sys.stderr)
        sys.exit(1)
    tail = f", {len(warnings)} warning(s)" if warnings else ""
    print(f"valid: {len(items)} {kind}, ids unique, format rules satisfied{tail}")


if __name__ == "__main__":
    main()
