# Landing — the SDLC and PDLC applications, 2026-11-07

The session stops at a green head on `claude/sdlc-pdlc-applications-0u6318`. Nothing is landed.
Everything below is Emil's to run, after ruling the specs or deciding to land them as
`[PROPOSED]`. The head is the branch's last commit, reported to Emil when the session closed.

**No pull request is open.** The session was not asked to open one. `canon land` lands a pull
request, so one is opened first, on the branch above, by Emil or by a session he asks. Its number
is `<pr>` below.

From a checkout without canon installed, use `dotnet run --project tools/canon/src/Canon --` in
place of `canon`.

## 1. Approve the head (`DDD-dec-109`)

By hand, on the pull request, as a comment whose whole text is:

```
approve <head sha>
```

`agent review` goes green on it, and only on an unedited comment made by hand.

## 2. Land (`DDD-dec-101`, `DDD-dec-108`)

```bash
canon land <pr> --print   # fetch, show the pushes, make none
canon land <pr>           # push the head to land/pr-<pr>
```

Wait for `pipeline (devcontainer)` to go green on `land/pr-<pr>`. Then:

```bash
canon land <pr> --main    # fast-forward main, delete land/pr-<pr>
```

The branch is a fast-forward of `main` at `1ab1de0`. If `main` has moved, canon refuses, and the
branch is rebased first. A rebase changes every SHA, so the head is then approved again.

No release is cut by this session.

## After the continuation (Rounds 16 to 22), 2026-11-07

Add-only. The steps above are unchanged. Only the head moved.

- **The amended content** is at `eb8102c2e570819e979bf0259b13190196487590`, green on CI (run
  42411491433). It holds the rulings of Rounds 16 to 22, `DDD-dec-114` and `-115` amended in place
  (Round 21), the amended specs and the graph data.
- **The head to approve and land** is this file's commit, the branch's last. It changes only
  `landing.md` and `predictions.md` under `meta/sessions/`. Its full SHA is given in the closing
  report to Emil, and CI runs on it as on every push.
- **Still no pull request.** One is opened first, and its number is `<pr>` in the commands above.
  `main` is still at `1ab1de0`, so the branch fast-forwards it.

## After Round 26, 2026-11-08

Add-only. The steps above are unchanged.

- **Round 26's content** is at `b79e3346529e94907f2a8c6ac8bd3e87c331bea5`, green on CI.
- **The head to approve and land** is this file's commit, the branch's last. It changes only
  `landing.md` and `predictions.md`. Its full SHA is in the closing report to Emil.
- **Still no pull request.** `main` is still at `1ab1de0`.

## After Round 27, 2026-11-09

Add-only. The steps above are unchanged.

- **Round 27's content** (flow time ruled, `DDD-dec-114` P-14) is at
  `9b24f26d72a10bb0cb2f6eaea867cf28d100fc59`, green on CI (run 42588904271).
- **The head to approve and land** is this file's commit, the branch's last. It changes only this
  file and `predictions.md`. Its full SHA is in the closing report to Emil.
- **Landing ratifies `DDD-dec-114` and `-115`** as amended through Round 27. The specs stay
  `[PROPOSED]`, with their remaining open items unruled.
