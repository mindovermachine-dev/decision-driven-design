#!/usr/bin/env bash
# Seed the run's workspace with a clone of decision-driven-design at ./decision-driven-design,
# cloned from the repository this suite lives in, so no network is needed. origin is set to the
# public URL, as in a practitioner's clone. The working tree is left at the branch head, not at
# the pin, so a case that reads the working tree instead of the pin can be told apart.
# The pin is read from its one source, the PIN line of skills/run/SKILL.md (DDD-dec-121).
# When the pin is not yet a tag (a re-pin made in the same change as a release, Round 31 item 4),
# the source's HEAD, the candidate, is tagged as the pin inside this throwaway clone only, and its
# commit is written to ./.pin-candidate. Nothing is pushed. check.py ties the evals to what the
# pin holds through evals/pin-trees.json.
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
top="$(git -C "$here" rev-parse --show-toplevel)"
pin="$(sed -n 's/^PIN: `\(v[0-9][0-9.]*\)`$/\1/p' "$here/../../skills/run/SKILL.md")"
[ -n "$pin" ] || { echo "no PIN line in SKILL.md" >&2; exit 1; }
git clone -q "$top" decision-driven-design
git -C decision-driven-design fetch -q "$top" 'refs/tags/*:refs/tags/*'
if ! git -C decision-driven-design rev-parse -q --verify "${pin}^{commit}" >/dev/null; then
  head="$(git -C "$top" rev-parse HEAD)"
  git -C decision-driven-design tag "$pin" "$head"
  echo "$head" > .pin-candidate
fi
git -C decision-driven-design remote set-url origin https://github.com/mindovermachine-dev/decision-driven-design
