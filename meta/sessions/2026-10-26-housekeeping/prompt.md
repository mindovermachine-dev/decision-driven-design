# Prompt — housekeeping session, 2026-10-26

The session had no bundled prompt. Its charter is the exchange below, verbatim: Emil's four
messages, and the recommendations Emil agreed to with the fourth. Per `DDD-dec-20`, this file is
committed before any canon edit so the session's scope is fixed at arrival.

## Emil, message 1

> give me a rundown of the canon and what needs accepting

## Emil, message 2

> list all proposed

## Emil, message 3

> give me your recommendations

## Claude's recommendations (the charter)

> My recommendation, in the order I would do it.
>
> **1. Strike the Track 1 banners in one housekeeping commit, now.** DDD-dec-27, DDD-dec-28,
> DDD-track-01, the two projection READMEs, the track file, and the five stale pin-group comments
> in `graph/upstream.yaml`. Every one of them records a ratification that already happened.
> Leaving them standing means the repo's own register lies about its state, which is exactly the
> basis-loss the framework warns about. No canon content changes, so it is a ruled edit with
> `Basis: DDD-dec-27; DDD-dec-28`. I can do this today if you say so.
>
> **2. Open a tiny upstream PR for DDD-dec-26 and DDD-frame-02.** Strike the two banners and fix
> the "One / One" duplication. Ship it as v5.15.2, and use it as the first release under the
> release-head guard below. Then the pin advance is a near-zero firing, a good dry run for the
> guard.
>
> **3. Build S-1, the release-head guard, before any other upstream release.** Two consecutive
> releases cut from the wrong head is a class. The remedy is small: an additive `ratified_head`
> field in the release format, and a workflow check that the merge commit's parent matches it.
> Run it against the existing thirteen descriptors first so you know which ones would have
> failed.
>
> **4. Fix S-7 in the same housekeeping pass.** The repo URL still points at the old owner. A
> redirect that lapses fires E12 on all 74 pins at once. One line, one ruling.
>
> **5. Close upstream PR #3 rather than rebase it.** It is eleven weeks stale and rewrites the
> document that establishes the act term. Anything still worth keeping from it should be
> re-proposed against current canon, not merged from a branch that predates seven releases.
>
> **6. Then rule the nine review flags, batched by kind.** The six session-authored org and sim
> claims have no canon document behind them. Either ratify them as projected with a note that the
> exposition is the claim file itself, or demote them to a holding note. They have sat flagged
> since the scaffolding session, and a flag nobody rules on is just noise. The two address-01
> flags and the address-03 seam-decay flag wait on S-3 and S-4, so file the behaviour term and
> the seam-decay home first, then rule all three together.
>
> **7. Write the T2b pre-registration, S-2, as its own session.** It is the only path that moves
> any address claim out of projected. Hash it before the slice exists, and fold in F-1, the
> escalation-rule anchoring, and the reading/verdict-input line. Do not start it until items 1
> through 4 are done, so the test runs against a repo whose register is clean.
>
> **8. Decide F-3 explicitly.** It is accepted as proposed but filed nowhere. Either file it as
> DDD-address-06 or record in DDD-address-03's notes that the replication case is excluded by
> design. The fastest clean answer is the second, pending what T2b shows.
>
> What I would leave alone: DDD-dec-14 stays open on purpose, S-8 is low priority by your own
> ruling, and the glossary pass S-5 can ride along with whichever upstream release comes next.

## Emil, message 4 (the ruling)

> agreed on all execute it
