# Landing and releasing — sdlc edition 1, 2026-11-03

The session stops at a green head. Everything below is Emil's to run, in this order.

- **The pull request** is #59, on the branch `claude/brave-planck-mdx1rs`.
- **The head** is its last commit, the `ratified_head` fill. It is named in the closing report on
  issue #49.
- **The ratified head** is the commit before it, which adds `releases/v0.6.0.yaml` and its
  `CHANGELOG.md` section (`spec/release-format.md`, port note 4).

From a checkout without canon installed, use `dotnet run --project tools/canon/src/Canon --` in
place of `canon`.

## 1. Approve the head (`DDD-dec-109`)

By hand, on #59, as a comment whose whole text is:

```
approve <head sha>
```

`<head sha>` is the full SHA reported on #49. `agent review` goes green on it, and only on an
unedited comment made by hand.

## 2. Land (`DDD-dec-101`, `DDD-dec-108`)

The head adds `releases/v0.6.0.yaml`, so canon names the landing branch `land/release-v0.6.0`:

```bash
canon land 59
```

Wait for `pipeline (devcontainer)` to go green on `land/release-v0.6.0`. CI runs
`canon release v0.6.0 --plan` there. Then:

```bash
canon land 59 --main
```

The branch is a fast-forward of `main` at `ca23241`. If `main` has moved, canon refuses, and the
branch is rebased first. A rebase changes every SHA, so the descriptor's `ratified_head` must then
be refilled, and the head approved again.

## 3. Cut the release (`DDD-dec-84`, `DDD-dec-113` E-6)

```bash
canon release v0.6.0 --plan
```

Then:

```bash
canon release v0.6.0
```

canon refuses if `v0.6.0` exists locally, on the remote or as a GitHub Release. It then checks the
guard: `ratified_head` is an ancestor, and only the descriptor changed after it. It runs every gate
at the commit, writes the signed tag `v0.6.0`, pushes it, and creates the GitHub Release as a
pre-release. `GH_TOKEN` must be set for the Release.

## 4. Checks after the cut

**Check 1: the tag verifies.**

```bash
git fetch origin tag v0.6.0
```

```bash
git tag -v v0.6.0
```

Expected: a good signature by Emil's key. The tag object names the commit `main` was
fast-forwarded to.

**Check 2: the edition hash at the tag equals the descriptor's.**

```bash
git show v0.6.0:applications/sdlc/what/ontology.ttl > /tmp/o.ttl
```

```bash
git show v0.6.0:applications/sdlc/what/shapes.ttl > /tmp/s.ttl
```

```bash
cat /tmp/o.ttl /tmp/s.ttl | sha256sum
```

Expected: `a2006d9da588586bbf7ac19b3eec4861ff5a1aec0006a61784e9e0d842672f29`. That is the hash in
`releases/v0.6.0.yaml`'s summary, and in `what@5`'s record
(`applications/sdlc/how-examples/records/acme/what/5.json`). If they differ, the edition is not the
one product-cli pins. Report it on #49 before product-cli's step 1 starts.

**Check 3: no marker in the edition.**

```bash
git grep -n -e PROPOSED -e UNVERIFIED v0.6.0 -- applications/sdlc/what/ontology.ttl applications/sdlc/what/shapes.ttl
```

Expected: no output.

## 5. Product-cli's pin

After the cut, comment on #49 and #50 with the four things product-cli's step 1 pins:
- the tag, `v0.6.0`;
- its commit;
- `owl:versionIRI <https://decision-driven-design.dk/ns/sdlc/1>`;
- the edition hash.

The session posts this once the tag exists. If the session has ended, Emil posts it.
