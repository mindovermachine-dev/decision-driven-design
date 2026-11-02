# Prompt — ready to try, 2026-11-02

The session had no bundled prompt. Its charter is the exchange below, verbatim: Emil's two
messages and the proposal his second message answers. Per `DDD-dec-20`, this file is committed
before any other file changes, so the session's scope is fixed at arrival.

## Emil, message 1

> So the repo decision driven design is not looking very professional. Right now there is a lot of
> basics missing, if we take a look at my hafeok/varve repo it presents as something thats ready
> to use. I want the same for Decision Driven Design how do we achieve that ?

## Claude's proposal (the charter)

Claude compared the repository with Varve (`Hafeok/varve` at its default branch on 2026-11-02)
and proposed three layers, `[PROPOSED]`:

> **Weakest point first.** Varve looks ready to use because its product is ready to use. The
> product of Decision-Driven Design is the method, and today only step 1 is ruled (for test, not
> reported); steps 2 to 10 are `[PROPOSED]`. Polishing the repository to look ready to use would
> overclaim. The honest target is "ready to try", the way Varve presents its preview releases.
>
> **Layer 1: stewardship hygiene.** Mechanical; almost no canon. Governance adopting the Mind Over
> Machine stewardship standard; SECURITY, CODE_OF_CONDUCT, issue and PR templates;
> `repo-standard.yaml`; build debris out of the root; stale `Hafeok/` links fixed; the stale
> "private" comment in CI fixed; the `validate-core-order.py .` defect fixed or filed.
>
> **Layer 2: the front door.** Needs rulings. A README for practitioners (what it is, what it
> gives you, where it is the wrong tool, honest status per step, a quick start); theory moved to a
> `why.md`; `method/` with one step card per step, each carrying its register; a quick start that
> carries one worked example through step 1.
>
> **Layer 3: releases and a site.** One version scheme; release notes that say what each release
> ruled; a release workflow under the release-head guard (`DDD-dec-39`); optionally a rendered
> site.
>
> **Rulings asked.** 1. Positioning: "ready to try (preview)"? 2. The worked example (not
> Phoenix). 3. Versioning: method, claim graph, or upstream pin? 4. Stewardship: in full, or with
> recorded deviations?
>
> Once you rule, I'll charter the session: `prompt.md` and `bootstrap.md` committed first, then
> Layer 1 as its own PR, because it can land without touching canon.

## Emil, message 2 (the ruling)

> 1. yes ready to try 2. could Varve work ? 3. The method 4. we adopt the full as it applies to us.
