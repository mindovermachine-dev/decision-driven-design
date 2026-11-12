# First-pass term index of the trial source

**Trial material. Nothing here is ruled.** Made on 2026-11-12 for issue #75, after Emil's ruling that a layer is inner by dependency: a concept explained in one place and used in the next must be read in that order.

## What this is

A pattern search for 40 candidate terms over `../product-definition.source.md` (the introduction and chapters 1 and 5). The term list was chosen by hand, from the terms the trial's models reported as unexplained.

| Column | Meaning |
|---|---|
| uses | Statements in the trial source that use the term |
| first | The first statement, in reading order, that uses it |
| definition chapters | Chapters of `../product-definition.md` where the term appears at all |
| what.md | Whether `applications/sdlc/what.md` has the term in a heading, in its text, or not at all |

**Appearing is not explaining.** No column says where a term is explained. That is a judgement this pass did not make.

## Index

```
term                         uses first   definition chapters    what.md
draft log                      10 W0.3    3,4,5,7,8              -
Decider                         7 P3.1    1,2,3,4,5,6,7          heading
author                          7 P1.2    1,2,3,4,5,6,7,8        text
the What                        6 P1.6    1,3,4,5,7,8            heading
scenario                        6 P3.1    1,2,3,4,5,6,7,8        text
trigger                         6 W3.3    3,4,5,8                text
step                            6 P1      1,2,3,4,5,7            heading
dpp/1                           5 P1.4    1,3,4,5,7,8            text
canonical export / document     5 P4.3    1,3,4,5,7              text
agent                           5 P1.1    1,2,3,4,5,6,8          -
Projector                       4 P3.1    1,2,4,5,6,7,8          heading
subject kind                    4 W3.3    4,5,7,8                text
proposal                        4 P1.3    1,2,3,4,5,6,7          text
decision record                 4 P1.4    1,3,4,5                -
Writ                            3 P4.4    1,2,3,4,5,6,7,8        text
finding                         3 P1.2    1,2,3,4,5,6,7          text
edition                         3 W0.4    3,4,5,6,7,8            text
shape                           3 P2      1,3,4,5,6,7,8          text
signature                       3 W2.1    2,3,4,5,6              text
position                        3 P4.4    1,4,5,8                -
What-version record             2 W6.2    4,5,7                  text
View                            2 W3.2    2,4,5,8                text
violation                       2 W0.4    3,4,5,6,7              text
aggregate                       2 W3.1    3,5                    text
scope rule / key                2 W3.4    4,5,7                  text
profile                         2 P4.2    1,3,4,5,8              text
grant                           2 P4.4    1,3,5,8                heading
head                            2 W12.1   5                      -
flow                            1 P3.1    1,2,3                  heading
change set                      1 W1.1    3,4,5                  -
warning                         1 W0.5    3,5,6,8                text
AIO                             1 W5.1    3,4,5                  text
Translation                     1 W5.6    5                      text
journey                         1 W5.6    3,4,5                  text
claim                           1 W4.3    4,5,8                  text
exporter                        1 W7.2    3,4,5,6,7              -
session transport               1 W9.2    5                      -
published triple                1 W11.6   5                      -
wire protocol                   1 P3.2    1,2,3,4,8              text
orphan                          0 -                              -
terms: 40 | used in trial source: 39
```

## What it shows

- **Chapter 1 uses terms it does not explain.** "The What" is first used in the headline of `P1`. `dpp/1` is first used at `P1.4`, Decider and Projector at `P3.1`, Writ at `P4.4`. No statement in the trial source explains any of them.
- **Some explanations live outside the document.** `what.md` §1.1 is headed "What the What is", and §3.3 and §3.4 are headed for the Decider and the Projector. By the ruling, a newcomer must read those before chapter 1 of the product definition.
- **Some terms appear only in chapter 5.** "Session transport", "published triple", "Translation" and "head" appear nowhere else in the definition.
- **One homonym.** "Claim" in `W4.3` is not a claim of this repository's claim graph.

## Limits

- The term list is hand-picked. Several entries are ordinary words used in a special sense (author, agent, step, flow), and whether those belong in an index is not settled.
- Matching is by pattern. It misses inflections it was not given and cannot tell senses apart.
