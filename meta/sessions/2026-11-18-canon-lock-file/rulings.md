# Rulings — canon's lock file

Emil's rulings, in his words, with the time Claude received them. Nothing here is paraphrased;
Claude's notes, where any, follow a ruling and are marked as Claude's.

## G1 — received 2026-11-18 13:17 UTC (14:17 Europe/Berlin)

> My G1 rulings on #83. Record this message in rulings.md, in my words, with the time you
> receive it. Then do deliverable 3 and stop at G2.
>
> The fix. Option B with your two corrections: pin the SDK exactly in global.json with
> rollForward "disable", pin the same version in devcontainer.json, and regenerate the lock file
> once. agent-review.yml does not change.
>
> Q-3. Pin 10.0.404.
>
> Q-2. Yes. Pass CI into the devcontainer so validate restores in locked mode.
> Directory.Build.props already rules that a CI restore is locked, so this closes a gap in an
> existing rule. It is not a new check. Say so in the record.
>
> Q-1. I will lift the "agent review" requirement on the trunk ruleset for this one landing and
> restore it straight after. You do not touch the ruleset. Draft a decision record for the
> waiver and stop for my ruling on its text before filing it: what was waived, why no other path
> exists (the check is posted by the gates app, and the job builds main's canon), the head that
> landed, and the times lifted and restored, which I will give you. Check every branch of both
> repositories for the next free decision id. DDD-dec-122 is on #84's branch.
>
> The throwaway workflow. Allowed, on these terms: it runs on push to this branch only, has
> read-only permissions and no secrets, does the agent review job's build steps and nothing
> else, and is removed in its own commit before the head to ratify. Report its run.
>
> Check one thing and report it: with rollForward "disable", does dotnet refuse to run when the
> installed SDK differs from global.json? If it does, a drift between global.json and
> devcontainer.json fails validate loudly, and the weakest point you named for B is milder than
> stated. Record whichever you find.
>
> Corrections to record, with attribution: #83's statement that validate passes because the
> devcontainer holds an older SDK was wrong, and it was Claude's in the planning conversation.
> You found the real cause and the deadlock.
>
> Successor items to record, without acting on them:
> - a scheduled check that says when a newer .NET patch exists, since B makes security patches
>   wait for a manual bump;
> - the deadlock itself: a required check that builds main's canon, with no bypass, means a
>   broken main can only be repaired by suspending the rule.
>
> Deliverable 3's exit changes, because it cannot be met as written. It is now: the validate
> workflow passes on the head with locked restore; your three pre-landing proofs pass; every
> commit carries "Refs #83". The first agent review run after landing is the final proof, and I
> will have #84 re-run it.
>
> Stop at G2 with a pull request against main, and name the head to ratify. Out of scope stays
> as in the issue.

## G2 — received 2026-11-18 13:37 UTC (14:37 Europe/Berlin)

> My rulings at G2 on #83. Record this message in rulings.md, in my words, with the time you
> receive it.
>
> W-1. The waiver takes DDD-dec-123. Check every branch of both repositories once more when you
> file it.
>
> W-2. The draft's text is accepted, with two additions:
> - say that the record is filed after the waiver was used, because it needs the landed head and
>   the two times, and that my ruling was recorded first in this session's rulings.md, which
>   lands with #85;
> - say that .github/repo-standard.yaml was not changed and still requires "agent review"
>   throughout: only the live trunk rule departed from it, between the two times.
>
> I will now lift "agent review" on trunk, land 1bf7e56, and restore it with its binding to the
> gates app (integration 5594102). Change nothing and push nothing until I give you the landed
> head and the two times.
>
> When I do:
> 1. Branch from the new main. File core/decisions/DDD-dec-123.yaml with the fields filled, and
>    move nothing else.
> 2. Open a pull request against main with "Refs #83" on every commit. It is the first change
>    through the restored gate, so report both required checks on its head.
> 3. Fill the "first agent review run after the landing" field with whichever run completes
>    first, this pull request's or #84's. If that run fails for any reason other than the
>    decision's own content, report it and stop.
>
> Stop there. Merging is mine.

Claude's note: received while `1bf7e56` awaited landing. Under "change nothing and push
nothing", this was held outside the repository and is recorded here, on the filing branch
(`claude/canon-lock-file-waiver-2026-11-18`, from `main` at `1bf7e56`), not with #85.

## Landing facts — given by Emil, 2026-11-18

> restored - lifted 14:20, restored 14:29 UTC

Landed head: `1bf7e56` (`1bf7e56af31cd19e004def678c163ccf224c134f`). Claude confirmed `main` at
that commit, signed (`G`), at 14:27 UTC by its own clock. Before the landing, Emil reported one
push refused with GH013, "Required status check "agent review" is expected"; Claude does not know
whether that was before or after 14:20, so the decision does not place it.

## The landing and the three times — received 2026-11-19 07:51 UTC (08:51 Europe/Berlin)

> #85 is landed. The head on main is 1bf7e56, merged at 15:25 Europe/Berlin.
>
> Three times for DDD-dec-123, all Europe/Berlin:
> - lifted: <your time>
> - restored at 15:28, but with the wrong check name: "agent review (judge)", bound to the gates
>   app. That is the workflow job's name, which the gates app never posts, so the rule could not
>   have been satisfied by any pull request.
> - corrected at 15:39 to "agent review" from the gates app (integration 5594102), which matches
>   .github/repo-standard.yaml.
>
> Record all three. The live rule departed from the written standard from the first time to the
> third, not to the second. Say in the decision that nothing landed between 15:25 and 15:39
> other than 1bf7e56, and check that against main's history before you write it.
>
> Go ahead with DDD-dec-123 as ruled.

Claude's notes.

- **The lift time.** "<your time>" is read as the time Emil gave earlier: "lifted 14:20 … UTC"
  (Landing facts, above), which is 15:20 Europe/Berlin. Confirmed by Emil, 2026-11-19 10:47 UTC
  (below): "The lift time is 15:20 Europe/Berlin, as you have it."
- **The restore time.** Emil's earlier message said "restored 14:29 UTC" (15:29 Europe/Berlin).
  This message says 15:28 and corrects what was restored. The decision follows this message.
- **The check against main's history,** made before writing it into the decision:
  - `main` moved once since `84aa466`: a fast-forward to `1bf7e56`, and it is still there at
    2026-11-19 07:51 UTC.
  - The only push-triggered run on `main` since 2026-11-10 is validate run 392 (44324064146) on
    `1bf7e56`, created 14:25:20 UTC (15:25 Europe/Berlin), which matches the merge time.
  - So nothing but `1bf7e56` landed between 15:25 and 15:39, nor since.
- **Agent review runs 89 (14:34–14:35 UTC) and 90 (14:38 UTC)** ran while the live rule required
  "agent review (judge)". The rule's name does not change what the workflow runs: both built
  main's canon and posted an `agent review` check from the gates App. Neither verdict could have
  satisfied that rule; both were `failure`, for want of approval.

## The lift and restore times confirmed — received 2026-11-19 10:47 UTC (11:47 Europe/Berlin)

> The lift time is 15:20 Europe/Berlin, as you have it. Clear the UNVERIFIED flag on it in
> rulings.md with the next change. The restore time is 15:28: GitHub recorded that edit at
> 15:28:11. My earlier "14:29 UTC" was a minute off and stays in the record as I wrote it.
>
> I am approving and landing 41c85f5 as it stands. Do not push before I say it has landed.
> After that, commit P-9's score and the cleared flag in one small pull request, or tell me if
> you would rather leave them for the session's close.

## #86 landed — received 2026-11-19 10:50 UTC (11:50 Europe/Berlin)

> its landed you can push and create a new pr

Claude's note: `main` at receipt is `29cead8`, "Merge pull request #86", committed by GitHub at
11:45:33 Europe/Berlin. Its parents are `1bf7e56` and `41c85f5`, and its tree is identical to
`41c85f5`'s, so what landed is exactly the approved head's content. It is a merge, not the
fast-forward `canon land` makes. That is recorded here as an observation, not judged.
