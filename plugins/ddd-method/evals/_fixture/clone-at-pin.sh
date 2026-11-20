#!/usr/bin/env bash
# Seed the run's workspace with a clone of decision-driven-design at ./decision-driven-design,
# cloned from the repository this suite lives in, so no network is needed. origin is set to the
# public URL, as in a practitioner's clone. The working tree is left at the branch head, not at
# the pin, so a case that reads the working tree instead of the pin can be told apart.
# The pin is read from its one source, the PIN line of skills/run/SKILL.md (DDD-dec-121).
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
top="$(git -C "$here" rev-parse --show-toplevel)"
pin="$(sed -n 's/^PIN: `\(v[0-9][0-9.]*\)`$/\1/p' "$here/../../skills/run/SKILL.md")"
[ -n "$pin" ] || { echo "no PIN line in SKILL.md" >&2; exit 1; }
git clone -q "$top" decision-driven-design
git -C decision-driven-design fetch -q "$top" 'refs/tags/*:refs/tags/*'
git -C decision-driven-design rev-parse -q --verify "${pin}^{commit}" >/dev/null \
  || { echo "the pin $pin is not a tag in $top" >&2; exit 1; }
git -C decision-driven-design remote set-url origin https://github.com/mindovermachine-dev/decision-driven-design
