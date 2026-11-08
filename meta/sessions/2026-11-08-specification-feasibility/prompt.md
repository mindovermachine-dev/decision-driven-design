# Prompt — specification feasibility, 2026-11-08

The session prompt, verbatim. Per `DDD-dec-20`, this file is committed before any other file
changes, so the session's scope is fixed at arrival.

This session did not start from a written prompt. It grew out of a conversation in the claude.ai
project "Decision Driven Design", on 2026-11-08, between 08:25 and 13:11 Copenhagen time. Emil's
eleven messages are reproduced below, verbatim and in order. Claude's replies between them are not
reproduced here. What they proposed is recorded in `rulings.md`, against the message that ruled it.

The last message is the instruction that opened this session.

---

**M-1 (08:25).**

> In the product framework we need to have specification constraints - what data can we use, what integrations are available etc so that we can do feasibility in product-cli

**M-2 (12:06).**

> This is primarily a problem in organizations because of the way Conway law says that system design is directly impacted by the organization design

**M-3 (12:10).**

> And since this is a dependency it has the same issue as with all dependencies. It must be loosely coupled. And this also means that there are two layers to each, the one in the what that you just described and the one in the how. And the how must dictate whether its feasible or not since a hard coupling will have a direct impact on the how systems ability to send features to production

**M-4 (12:14).**

> Product-cli must contain the full feasibility verdict in order to continue creating specifications that the how can actual land. The reason why its hard to do the split today is that we don't have a complete data model on a specification and so we rely on the human actors ability to infer alot of the information in order to complete a feature.

**M-5 (12:27).**

> We must have a way to decouple writ here, it could be any actor doing the how. So we need to expose a non verified feature for feasibility and then allow it to be vetted by actors allowed to do that act in product-cli how do they that we don't care. We just want the decision that it is possible added in product-cli

**M-6 (12:33).**

> 1. Needs to change we need to have the same grants, roles etc as the other systems. Its already built into product-cli and it should also have been added to the product FRAMEWORK. 2. Agreed a pinned version.
>
> Also the ruling on feasibility for ground is something that can be reused in the how. If it has been vetted in the how once, it should carry that forward if someone else wants to use the same ground.

**M-7 (12:48).**

> We add it to the domain entities if its feasible from the how side. Then they become whats reusable

**M-8 (12:52).**

> Agreed we cant do it by domain only because the vetting happens pr system. So we need to be able to specify that the domain entity has been vetted for the specific system and can be reused in decides only in that system

**M-9 (12:54).**

> 1. All three 2. Pr ground-sourced context if we can get one data entity from the integration we can get all of them

**M-10 (12:56).**

> Good catch - each integration is of course behind some sort of OAuth2 so it depends on our access. But that should be the data owner decision on what we can use not if the feasibility in the how

**M-11 (13:11).**

> All proposed are accepted.  Let's file it
