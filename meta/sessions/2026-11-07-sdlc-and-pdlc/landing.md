# Landing — the SDLC and PDLC applications, 2026-11-07

The session stops at a green head on `claude/sdlc-pdlc-applications-0u6318`. Nothing is landed.
Everything below is Emil's to run, after ruling the specs or deciding to land them as
`[PROPOSED]`. The head is named in the closing report on issue #61.

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
