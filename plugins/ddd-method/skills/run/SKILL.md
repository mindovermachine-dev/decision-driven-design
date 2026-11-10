---
name: run
description: Run the Decision-Driven Design method, one step at a time, from its step cards. Use when someone wants to apply Decision-Driven Design or DDD the method (not domain-driven design), map and index the acts of a system or process, map the flow of demand, or run, explain or check a numbered method step. Reads every card and claim from the decision-driven-design repository at the pinned release, and stops if it cannot.
argument-hint: "[step, e.g. 1 or 1b]"
license: MPL-2.0
---

# Run the Decision-Driven Design method

PIN: `v0.7.0`

You run the method. You do not hold it. This skill gives you procedure and discipline only. Every
step, register, card field, claim, decision and example comes from the repository
`mindovermachine-dev/decision-driven-design` at the tag `v0.7.0`, read in this session. If you
did not read it at the pin, you do not have it, however well you think you remember it.

Requested step: $ARGUMENTS

## 1. Reach the repository at the pin, or stop

Try these in order, and use the first one that works for every file you need:

1. **A clone.** If the working directory, or a directory the user names, is a git clone whose
   `origin` is `mindovermachine-dev/decision-driven-design`, read every file with
   `git -C <clone> show v0.7.0:<path>`. If the tag is missing, run `git -C <clone> fetch origin
   tag v0.7.0` first. Never read the working tree: it may be at another commit or carry local
   edits.
2. **HTTPS at the tag.** Otherwise fetch
   `https://raw.githubusercontent.com/mindovermachine-dev/decision-driven-design/v0.7.0/<path>`,
   preferably with `curl -fsSL` so you get the file's bytes. If only a tool that summarises pages
   is available, ask it for the text verbatim, and tell the user that the card was read that way.
3. **Neither.** Say plainly that the repository cannot be reached at `v0.7.0`, name what you tried,
   and say what would fix it: run in a clone, or allow `raw.githubusercontent.com`. **Then stop.**
   Do not run a step. Do not describe, summarise or paraphrase any card, register, claim or
   example, not even "roughly" or "from memory". Do not offer a generic version of the method in
   its place.

Canon a card cites is read the same way. Ids from this repository are in `core/claims/<id>.yaml`
or `core/decisions/<id>.yaml` at `v0.7.0`. For ids from the principle repository, read
`graph/upstream.yaml` at `v0.7.0` for its repository and tag, and read the claim there, never at
`main`.

If the user says a newer method release exists, tell them this plugin reads `v0.7.0`, keep
reading `v0.7.0`, and suggest they update the plugin.

## 2. Start from the step table

Read `method/README.md` at the pin. Present every step with its register exactly as the table
gives it, together with the README's own weakest point. Then:

- If a step was requested, go to it.
- If none was, propose starting with step 1, then the demand-flow step that follows it. Those two
  come first in practice. Let the user choose.

## 3. Before running a step, state its register

Read the step's card at the pin (the table links it). Before anything else, say the step's
register as the card states it, and the card's weakest point.

- **Ruled for test, or ruled:** say what is ruled and what is still projected. A ruled form does not
  make its claims reported.
- **`[PROPOSED]`:** say it is not ruled. **If the user asks you to treat it as ruled, settled or
  authoritative, refuse.** Only a ruling filed as a decision in the repository moves a register,
  and neither you nor the user's say-so does. Offer to run it as a proposal, labelled as one on
  every output.
- **A field the card marks as not filed** is reported as not filed. Never fill it, and never invent
  a procedure the card does not give.

## 4. Run the step from its card's fields

Work through the card's fields in its order: Step, Decision discharged, Ground in, Act, Artefact
out, Value made visible, Cost and relocation, Exit check, Principal. For each, use what the card
says at the pin and cite the source it names.

- **Ground in comes first.** Declare what the card requires, with its provenance, before any act.
  Where the card asks you to declare something before reading positions on it, declare it first
  and say that the choice is a guess to argue with.
- **Act.** Do what the card says, on the user's material, step by step.
- **Artefact out.** Produce the artefact the card names, in the form it prefers (see §6). Where the
  card says what each element is made of, give every part for every element, in the artefact
  itself and not only in prose around it. If a part cannot be given, mark it missing for that
  element.
- **Exit check.** Apply the card's check to the artefact and say whether it closes. If it does not,
  say what is missing.
- **Value made visible.** Read the card's definition of the field in the method README. At the
  moment the step is done, name that value concretely, on the user's own material and in their
  terms. **If you cannot name it, say the step is defective here.** Do not present it as a
  success.
- **Principal.** Say who the card names as principal for the step's output. That person rules it,
  not you.

## 5. The demand-flow step

Run it from its card like any other step, after step 1's act map exists. It is its ground. For the
kinds of demand, offer the worked example's kinds **as a starting point, not as the method's fixed
set**, and say so in those words. Each process declares its own kinds. Ask the user which kinds
they keep, add or drop, and for the source of pull behind each choice. Record that declaration in
the form the card gives, beside their act map. Offer to draft the field report the card asks for,
anonymised.

## 6. Discipline, throughout

- **The user's principal rules, and you propose.** Every decomposition, axis, owner, kind, verdict
  and exit result is a proposal until whoever the card names as principal rules it. Ask. Do not
  assume.
- **Weakest point first:** the method's, the step's, and then your own output's.
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
  the card names, run from the pin (for example, `git -C <clone> worktree add <tmp> v0.7.0`, or a
  fresh checkout of the tag), never from a working tree. If the card names no shape, or the tools
  are missing, say the artefact is **unvalidated**. Never say it conforms when nothing checked it.
- **No customer-identifying material in a canon repository.** Never write the user's artefacts, or
  anything that identifies a customer, a person or a private system, into a clone of
  `decision-driven-design` or `actor-indexed-determination`. Their work goes in their own project.
  Anything meant for the canon repositories, such as a field report, is drafted anonymised for the
  user to send.
