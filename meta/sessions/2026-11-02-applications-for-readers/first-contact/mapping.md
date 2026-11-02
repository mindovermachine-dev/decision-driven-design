# Label mapping

Written after scoring. The scorer saw answers W, X, Y, Z, relabelled from the readers' labels, with
the file names they read replaced by "[document]".

| Reader | Read | Scorer's label | Score |
|---|---|---|---|
| A | old `what.md` (`e5a332d`) | X | 8 / 8 |
| B | new `what.md` + `what-reference.md` (`aeefd36`) | W | 8 / 8 |
| C | old `what.md` (`e5a332d`) | Z | 8 / 8 |
| D | new `what.md` + `what-reference.md` (`aeefd36`) | Y | 8 / 8 (K6 borderline) |

The scorer's full report, with every quote it relied on, is `scoring.md`.

**Blinding was partial.** File names were redacted, but the old-text readers cite section numbers
("§2.1", "§5.1") and decision ids, which the new text does not have. A scorer could infer the
version from those. Since every answer scored full marks, this could not have changed the result.
