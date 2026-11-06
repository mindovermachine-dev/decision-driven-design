# Bootstrap — sdlc edition 1, 2026-11-03

- **Invocation.** A cloud session started on 2026-11-06 with the prompt in `prompt.md`, verbatim.
  The folder keeps the date the prompt names (`2026-11-03-sdlc-edition-1/`).
- **Branch.** `claude/brave-planck-mdx1rs`, from `main` at `799cbe8`.
- **Principal.** Emil. Commits are signed as `Claude (Emil) <claude+emil@okkels-klein.dk>`.
- **Issues.** #49 (the validation regime; refusals and findings) and #50 (the five §3.4 and §3.7
  shapes).
- **Arrival checks.**
  - `applications/sdlc/what/ontology.ttl` and `shapes.ttl` are unchanged on `main` since
    `c7424ad` (`git diff c7424ad 799cbe8` over both files is empty; so is the diff over
    `applications/sdlc/what/` and `what.md`). The evidence in #49 and #50 stands.
  - PR #48 (`what.md` readers' edition) is open at `068cb23`, unmerged. Asked in Round 1.
  - Baseline: `python3 scripts/ci.py` prints "all gates passed" once `scripts/requirements.txt`
    is installed (the container had no rdflib at arrival). The edition hash at `799cbe8`, sha256
    over `ontology.ttl` then `shapes.ttl`, is
    `5b9878c011cbab9c939c931c01421f8c5710c0c24b1cc07579716601274184da`.
- **Gates.** `python3 scripts/ci.py`; CI's `pipeline (devcontainer)` and `agent review`.
