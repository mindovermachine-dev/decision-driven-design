# Rulings — the pull and the scope of a map, 2026-11-18

Emil's rulings and statements, in the order given. His words are in `prompt.md`, verbatim, by time. Nothing here is filed.

| # | Time | Status | Emil's words (short form; full text in `prompt.md`) | Reading |
|---|---|---|---|---|
| E-1 | 07:20 | Direction given | "the act map should be the central modelling artifact for decision-driven-design" | Every application starts from the act map. Claude proposed central as an index that other artefacts point at, not as a container. Not ruled |
| E-2 | 07:23 | Direction given | "we should start with North, only by declaring the determination pull can we properly map the acts and decisions" | Step 1 starts by declaring north. Supported by `core/00` §4a at `v5.15.2`: "declaring the determinable space precedes any determination over it" (`DDD-ground-05`, projected). Step 1 is ruled for test and T2b is pre-registered with acts first, so this is a supersession. Not ruled |
| E-3 | 08:43 | Asked for | "we need a definition of it so that it can be reproduced by practicitioners" | Claude proposed: a pull is an unresolved determinable that the world resolves whether or not anyone acts, declared by a pull statement whose fields each carry a test, and found by a trace-back with a stopping rule |
| R-1 | 08:50 | **Ruled** | "this should be two or more outcomes" | The determinable's test reads: name two or more outcomes that cannot all hold together |
| R-2 | 08:50, 09:08 | **Ruled** | "by setting the scope of the map we decide when the stopping rule comes into effect"; "scope must be the first else we cant place the pull, or we would end up far far from our area of influence" | Scope is the first declaration of a map. Everything outside the scope is world to the map, including other people's decisions. The trace-back stops where the answer lies outside the scope. Emil's example: with the How as the scope, the trace stops at the edge of the SDLC |
| R-3 | 08:57 | **Correction by Emil** | "if we started with the PDLC we wouldnt see the seam in the how because it wouldnt exist" | A seam exists only where a map splits the work into scopes. Claude's check is corrected: a pull of a narrow scope appears in a wider map as a dependency (`DDD-address-01`), and as a seam only if the wider map also declares that scope |
| R-4 | 08:57, 09:08 | **Ruled** | "a bug and a feature cant share ground because ground for a feature is by necessity that it hasnt been implemented and a bug must have been implemented"; "yes - it must be else it cant be pull if we cant determine […] the ground it pulls from" | A kind of demand is a position on a declared ground axis. Kinds differ by ground, not by where the demand came from. Consistent with `DDD-flow-01`, which defines the PDLC's kinds relative to the decisions in force |
| R-5 | 09:08 | **Ruled**, on four names only | "the states are all that i have, but i completely agree with your mapping to the canon, this is exactly what we need in order create a process for our practicationers" | The four states map to canon as in the table below, and a pull is a gap between two of them. The concept is a friend of Emil's. Only its four names are known. See "The four states" |
| E-4 | 09:08 | Statement | "This is kind a like looking at thermal dynamic laws, they also inspect a system and look at the input and output" | The pulls of a scope can be found by inspecting its edge, before any act inside it is mapped. Claude's reading, `UNVERIFIED — Emil review` |
| R-6 | 09:18 | **Ruled** | "his github handle is pjarnhus lets start with that" | Asked: "May the four states appear in the public repository, and how should your friend be credited?" The four states are credited to GitHub user `pjarnhus`. Claude reads "lets start with that" as leave to record the concept here under that credit, and as a first form of credit that may change. `UNVERIFIED — Emil review` |

## Corrections

- **Claude, on R-3.** Claude proposed that a pull of a narrow scope "must show up in any wider map as a seam". Wrong: the wider map need not split the work. Corrected by Emil.
- **Claude, on R-4.** Claude proposed an origin field on the pull statement (the world moving, or another scope's act) to keep failure demand visible in a narrow scope. Withdrawn: the kind is read from the ground position.
- **Claude, on R-2.** Claude wrote that "the pull itself is in the world, but where the trace stops depends on whose arrangement is being mapped". Emil's ruling is stronger: the scope defines what counts as world.

## The four states

The concept is not Claude's and not canon's. **Credit: GitHub user `pjarnhus`** (R-6), a friend of Emil's, who is working on the difference between four states of an implementation. The work is not published, and nothing here is his wording beyond the four names. Emil has the four names and no more. The mapping is Claude's, made from the names, and Emil agreed with it (R-5).

| State | Nearest thing in canon at `v5.15.2` |
|---|---|
| Specified | The governing decisions in force |
| Actual | The outcome: "the determinate as it lands in the world" (`term:outcome`) |
| Observed | The verdict: "the same determinate as assessed by a declared predicate" (`term:outcome`) |
| Expected | The tolerance held by whoever bears the outcome |

| Gap | What it is |
|---|---|
| Expected, with nothing specified | A need nobody has taken up: a feature |
| Specified, with nothing actual | An approved change not yet built |
| Specified against actual | A deviation: a bug, which needs an implementation to exist |
| Actual against observed | A deviation nobody has seen, or an alarm with nothing behind it |
| Expected against specified | The specification is wrong |

`UNVERIFIED — Emil review`, and open:
- The mapping is built from four words. The friend's own definitions may differ.
- "Implementation" is a software word. The four states have not been tested as states of any determinable.
- "Expected" has one holder per stakeholder, so it is not one state.
- "Observed" depends on scope: it is what someone inside the scope has seen.
- "Actual" is never read directly. The world renders outcomes and not verdicts, so a practitioner can fill "observed" and can only declare "actual" unknown. The fourth gap cannot be inspected, only suspected.
- Own-ground demand, such as a CVE, is about the arrangement and not about the product's implementation. Where it sits among the gaps is not worked out.
- The credit is a handle and no more (R-6). Whether `pjarnhus` has agreed to the concept appearing here, and how he wants it cited once it is published, is not recorded.
