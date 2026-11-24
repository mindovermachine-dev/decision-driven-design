Outcome. The method is one thing: making an act map. It has four moves, all `[PROPOSED]`. What steps 2 to 10 held is recorded on the acts and decisions of the map. The method tells a practitioner how to describe an act fully enough to find its pull.

Depends on #80, landed as #84 (`main` at `dc8b737`). It supersedes the order of step 1's first part, which #84 filed. It does not change any claim's statement.

Ground. `AGENTS.md`. `meta/way-of-working.md`. `method/README.md`, `method/quick-start.md` and every card in `method/`. `core/claims/DDD-address-01` to `-11`, `DDD-ground-01`, `-05` and `-06`, and `DDD-frame-13`. `core/decisions/DDD-dec-74`, `-82`, `-114`, `-118` and `-122`. The pre-registration of T2b in `meta/sessions/2026-09-27-act-address/`. The session record `meta/sessions/2026-11-18-act-map-scope-and-pull/`. Canon at the tag in `graph/upstream.yaml`.

Ruled 2026-11-19, 13:54, in the planning project. Emil's words: "The method now is all proposed and the method as i envision it now is to create an act map. And that process is 1. scope the act map 2. place an act or decision 3. follow the determinable back to the edge and note the pull. 4. do it again untill all maps you can find or think of is mapped and your pull sources are identified."

Ruled 2026-11-19, 13:57, in the planning project. Emil's words: "The method should be updated as well. and steps 2 to 10 is recorded in the acts and decisions. We need to help people then describe the act fully or else they cant find the pull"

Read as, each `UNVERIFIED — Emil review`:
- Every part of the method is `[PROPOSED]`, step 1 included. Step 1 leaves "ruled for test".
- The practitioner starts from an act or a decision they can see, not from the edge. The pull is found by the trace back. This supersedes the wording of the ruling of 2026-11-18 that mapping starts with north, and the order of the five parts in `method/01`.
- Steps 2 to 10 stop being steps. Each becomes something recorded on an act or a decision.
- Move 4 means: repeat for every act and decision inside the scope, and then for each further scope the practitioner can map. A pull at one map's edge is a dependency in a wider map (ruling of 2026-11-18). Emil was asked whether "maps" or "acts" was meant and has not answered.

Not ruled, raised by Claude in the planning project:
- Starting from acts finds only the pulls that already have an act. Demand that nothing answers stays unseen. A second pass from the edge may be needed: for each state at the edge, who is waiting on it.
- Move 4 has no exit check. The states and gaps of #82 may be that check.
- T2b is pre-registered against step 1 as ruled for test, and its pre-registration is fixed.

Deliverable.
1. Survey. Every place the repository says the method has ten steps, names a step by number, or states step 1's register: `method/`, `README.md`, `applications/`, `core/`, `releases/` and the tooling. Exit: each row names file and line, and whether a ruled text or an exposition holds it.
2. Proposals, each with its weakest point first, a falsifier and what it breaks:
   - the four moves as step cards, or as one card, with every field of the step card filled, "Value made visible" first;
   - the act description: the fields a practitioner fills to describe an act or a decision, in two groups. First, the fewest that let the trace back run: the determinable it resolves with its outcomes, and the ground it reads with where each reading comes from (`DDD-address-01`). Second, what steps 2 to 10 held: authority, the decisions and their predicates, ground with provenance and tick rate, closure and assurance, the occupant, accountability, what is derived from it, the record of its occurrences, and what is observed. For each field: the value it shows when it is filled, and which claim or ruling it rests on, or that it rests on none. The occupant stays outside the address (`DDD-ground-06`);
   - the trace back as a procedure a junior engineer can follow: for each reading, either an act inside the scope produced it, and that act is placed next, or it comes from outside, and that is the edge and the pull is noted;
   - whether a pass from the edge is added, and how;
   - when the loop ends, and whether #82's gaps are the exit check;
   - what move 4 means, on the reading above or another;
   - what T2b tests once step 1 is `[PROPOSED]`, without touching its pre-registration;
   - where the content of `method/01b` and `method/02` to `10` goes, and what happens to those files. Ruled material changes by supersession, never by rewriting;
   - the decision or decisions that file this, with the ids checked free on every branch of both repositories.
   Exit: each says which ruling it rests on, or that it rests on none.
3. On the rulings: the decision is filed, and `method/` is changed. One worked example is carried through all four moves, with at least one act described fully and its pull found by the trace. Exit: the whole `validate` workflow passes, and a reader of `method/README.md` alone can name the four moves and the register of each.
4. What this breaks elsewhere, as a list with a draft issue for each: the plugin of #74, `quick-start.md`, the version under `DDD-dec-82`, #81, #82 and the cards' citations in `applications/`. Exit: nothing in the list is changed by this session.

Gates. G1 after step 2: the principal rules each reading above and each proposal. G2 after step 4. Then the merge.

Out of scope. Changing a claim's statement. Canon in the principle repository. Cutting a release. The plugin's files. The What and product-cli's definition (#81). Mantle. Any real organisation's data, name or code name.


---
_Generated by [Claude Code](https://claude.ai/code)_
