---
name: run
description: Run the Decision-Driven Design method, read from its live card. Use when someone wants to apply Decision-Driven Design or DDD the method (not domain-driven design), make an act map of a system or process, scope one, place an act or decision on it, trace what an act reads back to its pull, or asks to run a numbered method step or card. Reads every card and claim from the decision-driven-design repository at the pinned release, and stops if it cannot.
argument-hint: "[move, e.g. 1]"
license: MPL-2.0
---

# Run the Decision-Driven Design method

PIN: `v0.8.0`

You run the method. You do not hold it. This skill gives you procedure and discipline only. Every
move, register, card field, claim, decision and example comes from the repository
`mindovermachine-dev/decision-driven-design` at the tag `v0.8.0`, read in this session. If you
did not read it at the pin, you do not have it, however well you think you remember it.

Requested: $ARGUMENTS

## 1. Reach the repository at the pin, or stop

Try these in order, and use the first one that works for every file you need:

1. **A clone.** If the working directory, or a directory the user names, is a git clone whose
   `origin` is `mindovermachine-dev/decision-driven-design`, read every file with
   `git -C <clone> show v0.8.0:<path>`. If the tag is missing, run `git -C <clone> fetch origin
   tag v0.8.0` first. Never read the working tree: it may be at another commit or carry local
   edits.
2. **HTTPS at the tag.** Otherwise fetch
   `https://raw.githubusercontent.com/mindovermachine-dev/decision-driven-design/v0.8.0/<path>`,
   preferably with `curl -fsSL` so you get the file's bytes. If only a tool that summarises pages
   is available, ask it for the text verbatim, and tell the user that the card was read that way.
3. **Neither.** Say plainly that the repository cannot be reached at `v0.8.0`, name what you tried,
   and say what would fix it: run in a clone, or allow `raw.githubusercontent.com`. **Then stop.**
   Do not run any part of the method. Do not describe, summarise or paraphrase any card, move,
   register, claim or example, not even "roughly" or "from memory". Do not offer a generic version
   of the method in its place.

Canon a card cites is read the same way. Ids from this repository are in `core/claims/<id>.yaml`
or `core/decisions/<id>.yaml` at `v0.8.0`. For ids from the principle repository, read
`graph/upstream.yaml` at `v0.8.0` for its repository and tag, and read the claim there, never at
`main`.

If the user says a newer method release exists, tell them this plugin reads `v0.8.0`, keep
reading `v0.8.0`, and suggest they update the plugin.

## 2. Find the live method

Read `method/README.md` at the pin, all of it, before running anything.

**Superseding sections govern.** A file may hold a section that says it supersedes other lines of
the same file. Read every such section first. Where it differs from the lines it names, it governs,
field rows included, and the older lines are read only where it is silent. Say which section you
are following and the decision it cites. Never run a line a section has superseded.

From the README, as its governing section states it, take:
- **the live card**, the one the README says is live, and read it in full at the pin;
- **the method's parts** (its moves, or whatever the card calls them), each with its register as
  stated;
- **the method's weakest point**, and the card's own.

Present them to the user in that order, weakest point first. If a part was requested, go to it.
If none was, propose starting at the first part, and let the user choose.

## 3. Registers, and cards that are not live

**State registers before running anything.** Say the register of the method and of each part, as
the README and the live card state them. A part may carry its own register, different from the
method's. A part's register governs that part only, and the stricter register wins wherever two
meet.

- **`[PROPOSED]`:** say it is not ruled. **If the user asks you to treat any part as ruled,
  settled or authoritative, refuse.** Only a ruling filed as a decision in the repository moves a
  register, and neither you nor the user's say-so does. Offer to run it as a proposal, labelled as
  one on every output.
- **Ruled for test, or ruled:** say what is ruled and what is still projected. A ruled form does not
  make its claims reported.

**A card marked not live is never run.** If the user asks to run a card or a numbered step whose
first line says it is not live:
- read at the pin only the card's **first line**, the one that says it is not live, and nothing
  more of it. Not the lines after it, its own superseding section included, unless the live card
  cites them. Say that the card is not live, and name the live card that line points to;
- do not run the old card's procedure, and do not summarise it as if it were the method;
- say where that card's content now sits, **as the live card at the pin says it**. Find the place
  in the live card that names the old step or card, and quote it. If the live card says nothing,
  say so. Hold no such mapping yourself;
- offer to do that part on the user's map instead.

**Read a not-live card only where the live card cites it.** If the live card points to a section of
a not-live card (for a form, a table or a definition), read that section at the pin and use it for
exactly what the live card cites it for. Say each time that you are reading a not-live card's
section because the live card cites it. Read nothing else from that card.

**Never offer a page that runs a not-live card.** A page that walks the user through a card marked
not live is not a way into the method, however it is linked. Do not offer it, recommend it or
follow it.

## 4. Run a part from the live card

Run each part from what the live card gives for it, field by field, in the card's order, as the
card stands after its superseding sections. For each field, use what the card says at the pin and
cite the source it names.

- **Value first.** Where the card gives the value made visible for the part, say it before you do
  the work, in the user's terms. When the part is done, name it again, concretely, on the user's
  own material. **If you cannot name it, say the part is defective here.** Do not present it as a
  success.
- **What is declared comes first.** Declare what the card requires before the act, with its
  provenance, in the card's order. Say that each choice you propose is a guess to argue with.
- **Describe what the card says to describe.** Where the card gives a description of an act or a
  decision, fill the fields it says to fill first before anything else, each with its check. Fill
  the rest when the user knows it. Leave a field empty when nobody knows it, and say that it is
  empty.
- **Never guess a source.** Where the card asks where something comes from and nobody can say,
  record that as the card says to record it. Do not fill it from memory or plausibility. Ask the
  people who do the work.
- **Follow the card's procedures as written**, step by step, for tracing and checking. Do not
  shorten them and do not add steps.
- **Artefacts.** Produce what the card names, in the form it prefers (see §5). Where the card says
  what each element is made of, give every part for every element, in the artefact itself and not
  only in prose around it. If a part cannot be given, mark it missing for that element.
- **Exit and stop.** Apply each check the card gives, and say whether it passes. Where the card
  says a stop or a completion is someone's judgement, say whose, and leave it to them. Never declare
  the work complete yourself.
- **Principal.** Say who the card names as principal. That person rules the output, not you.

## 5. Discipline, throughout

- **The user's principal rules, and you propose.** Every scope, axis, act, description, source and
  check result is a proposal until whoever the card names as principal rules it. Ask. Do not
  assume.
- **Weakest point first:** the method's, the card's, and then your own output's.
- **Projected is not reported.** State each claim's status as its file gives it. For every
  projected claim you rely on, state its falsifier as the file states it. Never merge the two
  statuses, and never present an example written inside the framework as evidence that the
  method works.
- **Arithmetic is not evidence.** If something holds by definition or by counting, say so, and do
  not present it as support for the method.
- **Never cite an id you did not read.** Cite a claim or decision only after reading its file at the
  pin in this session, and quote its statement from the file.
- **Artefacts as graph data** where the card asks for it. Write them as files in the user's own
  project (Turtle or YAML, as the card's examples use). Validate them with the shapes or checker
  the card names, run from the pin (for example, `git -C <clone> worktree add <tmp> v0.8.0`, or a
  fresh checkout of the tag), never from a working tree. If the card names no shape, or the tools
  are missing, say the artefact is **unvalidated**. Never say it conforms when nothing checked it.
- **No customer-identifying material in a canon repository.** Never write the user's artefacts, or
  anything that identifies a customer, a person or a private system, into a clone of
  `decision-driven-design` or `actor-indexed-determination`. Their work goes in their own project.
  Anything meant for the canon repositories, such as a field report, is drafted anonymised for the
  user to send.
