# Decision Provenance Protocol — `dpp/1`

**Specification version 1.0, draft of 2026-10-27.** Records conforming to this specification carry
the protocol token `dpp/1`. This text identifies the protocol by that token, not by any location;
it may be copied and hosted anywhere, and a conformance claim cites the token and the
specification version, never a URL.

---

## 1. Scope

### 1.1 Purpose

Decisions are made in many systems: an architecture decision record (ADR) in a repository, a
ticket in a tracker, a rule in a line-of-business application, a run in a model-training
pipeline, an act in a governance engine. An outcome in any one of them usually rests on decisions
held in several others. This specification defines how a system exposes the decisions it holds so
that

1. a decision recorded in one system can reference, by pinned version, the decisions in other
   systems it rests on; and
2. anyone with access can walk the chain from an outcome back to its origin, resolving each hop
   at the system that holds it, and learn at each hop one of exactly three things: the record is
   held, it is not held, or the system cannot be reached.

### 1.2 What this specification fixes

Three things, and only three:

1. **The record**: the shape of a decision record (§3) and of a reference to one (§4).
2. **The resolver**: how a record is obtained from the system that holds it, over HTTPS or as
   files (§6), and how a chain of records is walked (§7).
3. **The hash law**: the single canonical form of a record and the single function over it (§5).

### 1.3 Non-goals

This specification does not define, and a conformant system is not required to have, any of the
following. A system that has them documents them for itself as a **profile** (§9.4).

- Who may decide, propose, accept, review or approve anything.
- Whether a decision binds, on whom, from when, or in what scope ("force").
- What a system does when a decision it rests on is superseded or becomes unreachable.
- Acceptance, sign-off, verdicts, waivers, baselines, positions, sessions, or any clock other
  than the single time `at`.
- Any registry, directory, root resolver, discovery service, or party that must be reachable for
  two systems to interoperate. There is none.
- Search, query, subscription, or notification.
- How a system stores its records internally.

### 1.4 Conventions

The key words MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, NOT
RECOMMENDED, MAY and OPTIONAL are to be interpreted as described in BCP 14 (RFC 2119, RFC 8174)
when, and only when, they appear in all capitals. Sections and passages marked *non-normative*
contain no requirements.

---

## 2. Terms

**Decision.** A resolution made in order to act, by some agent, at some time, for some reason.

**System.** Anything that holds decision records and exposes them per §6: a ticket tracker, a
directory of ADRs, a rules engine, a pipeline, a governance engine.

**System identifier.** A URL chosen by a system's operator that names the system (§3.3). It is a
name first; how it is resolved is §6.

**Record.** The JSON object of §3 describing one version of one decision.

**Reference.** The string `id@version@system` naming exactly one version of one decision in one
system (§4).

**Pin.** The record hash (§5.3) of the referenced record, carried in every reference object so that a
reader can verify it received the content that was relied on.

**Record hash.** SHA-256 over the canonical form of a record (§5), written `sha256:<hex>`.

**Resolver.** The interface of §6 through which a system answers for its own records.

**Base.** The location under which a system's files are laid out (§6.2): a URL (§6.5) or a
directory (§6.6).

**Reader.** Software that obtains records from systems. **Walker.** A reader that performs the
walk of §7.

**Hop.** One edge of a walk: from a referring record (or from the starting point) to one
reference.

**Held / not held / not reachable.** The three results of a hop (§7.2).

**Origin.** A held record whose `basedOn` is empty.

**Profile.** A system's own documentation of semantics it adds on top of this protocol (§9.4).

---

## 3. The record

### 3.1 Encoding

A record MUST be a JSON object (RFC 8259) encoded in UTF-8 without a byte order mark, and MUST be
an I-JSON message (RFC 7493): no duplicate member names at any depth, and no string containing a
surrogate code point or a noncharacter. These input rules are restated, with the exact rejection
cases, in §5.1.

A record SHOULD NOT exceed 1 MiB. A reader MAY treat a larger record as not conformant.

### 3.2 Fields

| Member | Required | Hashed | Type | Meaning |
|---|---|---|---|---|
| `protocol` | yes | yes | string | The protocol token: `"dpp/1"` (§12). |
| `id` | yes | yes | token | The decision's identifier within its system (§3.3). |
| `version` | yes | yes | token | This version's identifier within the decision (§3.3). |
| `system` | yes | yes | system identifier | The system that holds this record (§3.3). |
| `statement` | yes | yes | string | What was decided. |
| `by` | yes | yes | string | The agent that made or recorded the decision (§3.4). |
| `at` | yes | yes | string | When, as the deciding system recorded it (§3.4). |
| `why` | yes | yes | string or object | The reason, as text or as a pointer to where it is written (§3.4). |
| `basedOn` | yes, may be empty | yes, as a set | array of reference objects | The decisions this one rests on (§3.5). |
| `attributedTo` | no | yes | string | The person or organisation responsible, where `by` is not (§3.4). |
| `supersedes` | no | yes, as a set | non-empty array of reference objects | The versions or decisions this one replaces (§3.5). |
| `status` | no | yes | string | One of `proposed`, `accepted`, `superseded`, `withdrawn` (§3.4). |
| *dotted names* | no | yes | any hashable value | System-defined content that must be pinned (§3.7). |
| `signature` | no | **no** | object | A signature over the canonical form (§3.7, §11.3). |
| `extensions` | no | **no** | object | System-defined content outside the hash (§3.7). |

"Hashed" means the member is part of the canonical form (§5). Every member of the record except
`signature` and `extensions` is hashed, including members the reader does not recognise.

### 3.3 Identity

`protocol` MUST be the string `dpp/1`.

`id` and `version` are **tokens**: strings of 1 to 128 ASCII characters matching

```
token     = alnum [ *126( alnum / "." / "_" / "-" ) alnum ]
alnum     = %x41-5A / %x61-7A / %x30-39        ; A-Z, a-z, 0-9
```

A token begins and ends with a letter or digit; the last rule keeps file systems that strip a
trailing `.` from opening a different file. Tokens are case-sensitive. In addition, an `id` MUST NOT end in `.json` and a `version` MUST NOT
be `index`, both compared ASCII case-insensitively; those names are taken by the layout (§6.2).
Because tokens become file names, a system MUST NOT hold two ids that are equal under ASCII case
folding, nor two versions of one id that are, and SHOULD avoid tokens that are reserved device
names on common file systems (`CON`, `NUL`, `COM1` and similar).

`id` names a decision within its system. A system MUST NOT reuse an id for an unrelated decision.

`version` names one version of that decision. It is chosen by the system: a revision number
(`3`), a configuration revision (`r42`), a commit identifier, a run identifier, or the record's own
hash. The protocol assigns versions no order; a system that orders them exposes the order through
`versions` (§6.4). A new version is a new record with the same `id`.

`system` is the identifier of the system that holds the record. It MUST be at most 1024
characters long and MUST match

```
system    = scheme "://" host [ ":" port ] *( "/" segment )
scheme    = %x68.74.74.70.73 / %x68.74.74.70   ; "https" or "http", lower case only
host      = label *( "." label ) / "[" 1*( HEXDIG / ":" / "." ) "]"
label     = 1*( alnum / "-" )
port      = 1*5DIGIT
segment   = 1*( alnum / "-" / "." / "_" / "~" / "!" / "$" / "&" / "'" / "(" / ")"
                / "*" / "+" / "," / ";" / "=" / ":" / "@" / pct-encoded )
            ; a segment MUST NOT be "." or ".."
pct-encoded = "%" HEXDIG HEXDIG
```

This is a strict subset of an RFC 3986 absolute URI: it has a host, no userinfo, no query, no
fragment, no empty path segment, no dot-segments, no trailing `/`, and only ASCII characters
(internationalised host names in their A-label form; other characters percent-encoded). `https` is
RECOMMENDED; `http` is for networks where the operator accepts its lack of transport security.

The identifier is chosen by the system's operator and need not be reachable from the public
Internet; an identifier inside an organisation's private network is as valid as a public one. It
is a name, not a promise of location: an operator that moves a system keeps its identifier and
arranges redirection (§6.5) or tells readers the new location (§6.7). A system MUST NOT change its
identifier; a system that does so is a new system.

The pair (`system`, `id`) identifies a decision; the triple (`system`, `id`, `version`) identifies
a record.

### 3.4 Content

`statement` MUST be a non-empty string stating what was decided.

`by` MUST be a non-empty string identifying the agent that made or recorded the decision, in one
identification scheme, and SHOULD be a URI (for example `mailto:`, `acct:`, `https:`, `spiffe:`,
or an OpenID Connect issuer-and-subject rendered as a URI). Where the decision was made by
software — a rules engine applying configuration, a pipeline gating a model, an automated policy —
`by` MUST be that software's own identity, not the identity of a person who did not perform the
act. `by` is required in every case (Appendix A, Q1).

`attributedTo`, if present, MUST be a non-empty string identifying the person or organisation
responsible for the decision where that is not the agent in `by`, in the same manner. Its absence
means the system did not record one; it does not mean nobody is responsible.

`at` MUST be a string matching

```
at        = date [ %x54 hour ":" minute ":" second [ "." 1*DIGIT ] %x5A ]   ; "T" ... "Z", upper case
date      = 4DIGIT "-" 2DIGIT "-" 2DIGIT
hour      = ( "0" / "1" ) DIGIT / "2" %x30-33                             ; 00-23
minute    = %x30-35 DIGIT                                                 ; 00-59
second    = %x30-35 DIGIT                                                 ; 00-59
```

where `DIGIT` is ASCII `0`–`9` only, and `date` MUST be a valid date of the proleptic Gregorian
calendar (year 0001–9999, month 01–12, day within that month's length, 29 February only in
leap years). This is a
calendar date, or a date and time in UTC, in the form of RFC 3339, with two restrictions: `T` and
`Z` are upper case, and there is no leap second (`60`), whose validity needs a table every reader
would have to carry. A system records the precision it has; a hand-written ADR knows a date. `at` is the time the deciding
system attributes to the decision; this specification defines no other clock and does not say
how `at` relates to any other time.

`why` MUST be present and MUST be either

- a non-empty string: the reason, as text; or
- an object with exactly one of the members `href` and `ref`:
  - `href`: a non-empty string, a URI-reference (RFC 3986) to a document containing the reason,
    resolved against the location from which the record was obtained (so `../0007-use-tokens.md`
    in a record at `<base>ADR-0007/1.json` names `<base>0007-use-tokens.md`). It MAY be accompanied
    by `hash`: `sha256:` followed by the 64 lowercase hexadecimal digits of the SHA-256 of the
    target's bytes. A reader checks only that `href` is a non-empty string; it is not walked.
  - `ref`: a reference (§4.1) to the decision that is the reason, which MUST also be the `ref` of
    an entry in `basedOn`. `hash` MUST NOT accompany `ref`; the pin is on the `basedOn` entry.

  Other members of the object are ignored by readers (§9.1) and hashed.

A record without `why`, or with an empty one, is not a record. This is the requirement that makes
the record decision provenance rather than an audit entry.

`status`, if present, is one of `proposed`, `accepted`, `superseded`, `withdrawn`: a writer MUST
NOT use any other value under `dpp/1`. **A status value means what the system that
wrote it says it means**, in its profile; this specification attaches no force, permission or
obligation to any value, and a reader MUST NOT infer any from the value alone. Absent `status`
means the system does not track it. Because `status` is hashed, changing it is a new version.
A reader MUST NOT treat a record as invalid solely because its `status` is a string it does not
recognise.

### 3.5 Edges

`basedOn` MUST be present and MUST be an array, possibly empty, of reference objects (§4.2). It
lists the decisions this one rests on. It is a set: entries MUST have distinct `ref` values, its
order carries no meaning, and the canonical form sorts it (§5.2). No entry may reference the record
itself. An empty `basedOn` declares an origin.

`supersedes`, if present, MUST be a non-empty array of reference objects with distinct `ref`
values, none referencing the record itself. It lists the records this one replaces, in this system
or another. It is a set and is sorted like `basedOn`. Supersession is stated only by the
successor; there is no forward link (Appendix A, Q2).

### 3.6 Record validity

A record is **conformant** when all of the following hold. A reader MUST check them before
treating a record as held (§6.8).

1. It satisfies §3.1, and the hash law (§5) yields a hash for it.
2. `protocol` is `dpp/1`.
3. `id`, `version` and `system` satisfy §3.3, and `id@version@system` is a reference by §4.1.
4. `statement` and `by` are non-empty strings; `attributedTo` and `status`, if present, are non-empty
   strings.
5. `at` satisfies §3.4.
6. `why` satisfies §3.4.
7. `basedOn` and `supersedes` satisfy §3.5, and every entry is a reference object by §4.2.
8. `extensions`, if present, is an object; `signature`, if present, satisfies §3.7.

### 3.7 System-defined content: dotted members, `extensions`, `signature`

A system often holds content the protocol does not define. It has two places for it.

**Dotted members (hashed).** A top-level member whose name contains a `.` (for example
`com.example.pricing.rule`) is system-defined. It is part of the canonical form, so it is pinned
by the record hash and cannot change without a new version. Its value MUST satisfy the hash law
(objects, arrays and strings only). Names SHOULD be reverse domain names under the operator's
control. This is the place for content another system's pin must cover: the rule's parameters,
the dataset's digest, the model card's hash.

**`extensions` (not hashed).** An object the protocol does not read and does not hash. A system
MAY add to or change `extensions` after publication without creating a new version. It may hold
any I-JSON value, including numbers and booleans. Member names SHOULD be reverse domain names.

A system MUST NOT put information that the protocol defines a member for only in a dotted member
or in `extensions`: who decided goes in `by`, what was relied on in `basedOn`, and so on.

**Undotted members.** Top-level member names without a `.` are reserved for this specification.
A writer MUST NOT emit an undotted member this specification does not define. A reader MUST
ignore undotted members it does not recognise, and MUST still include them in the canonical form;
this is what lets a later minor version add optional members without changing any hash (§12).

**`signature` (not hashed).** An object with members `scheme` (string, REQUIRED), `value`
(string, REQUIRED) and `key` (string, OPTIONAL): a signature over the canonical form (§11.3).

### 3.8 Immutability

Once a system has exposed a record, the hashed content of (`system`, `id`, `version`) MUST NOT
change, and the system MUST NOT later expose different hashed content under the same triple, even
after it has ceased to hold the record. Only `extensions` and `signature` may change.

A system MAY cease to hold a record (retention, legal erasure, withdrawal of access). It then
answers "not held" for it (§6.8). It MUST NOT reuse the version.

---

## 4. References

### 4.1 Syntax

```
reference = id "@" version "@" system
```

where `id` and `version` are tokens (§3.3) subject to the reserved-name rules of §3.3, and
`system` is a system identifier (§3.3). Because tokens contain no `@`, a reference is split at
its first two `@` characters; anything after the second is the system identifier, which may itself
contain `@` in its path.

**A reference always carries a version.** A string without one — `ADR-0007@https://…`,
`ADR-0007`, a bare URL — is not a reference, and a record containing one in a reference position is
not conformant.

References are always complete. There are no relative references and no implied system: a
reference to another record in the same system names that system in full.

### 4.2 Reference objects and pins

Wherever a record holds references (`basedOn`, `supersedes`), each is a **reference object**:

```json
{ "ref": "ADR-0007@1@https://git.example.internal/payments/docs/adr",
  "hash": "sha256:3c1f…" }
```

- `ref` (REQUIRED): a reference by §4.1.
- `hash` (REQUIRED): the pin, the record hash (§5.3) of the referenced record as the writer of
  the reference obtained it: `sha256:` followed by 64 lowercase hexadecimal digits.

A reference object without `hash` is not a reference object, and a record containing one is not
conformant (§3.6).

**Who computes the pin.** The writer of the reference computes it: it resolves the referenced
record (§6), applies the hash law to what it received (§5), and records the result. The walker
recomputes it at every hop and compares (§7.3). The referenced system never computes it, stores it,
or serves it: nothing in the resolver (§6) or in conformance (§8) involves a hash, so a directory
of hand-written files remains a conformant system. A writer that cannot compute a hash itself (an
author editing an ADR) uses any implementation of §5, such as the reference implementation, to
obtain it.

The pin is what makes a reference a reference to *content*: a walker detects any difference
between the record it receives and the record that was relied on (§7.3), whether the referenced
system broke §3.8, a mirror substituted a record, or the reference was mistyped.

A reader MUST ignore members of a reference object other than `ref` and `hash`, and MUST include
them in the canonical form.

### 4.3 Equality

Two references are equal if and only if they are equal as strings, character for character. No
normalisation (case, percent-encoding, default ports, trailing characters) is applied. The
operator of a system publishes one spelling of its identifier; records and references use it.

---

## 5. The hash law

The hash law is the only behaviour every implementation shares. It is the function of §5.2 and
§5.3: from a parsed record to its canonical form and record hash. It is executed by the writers of
references, to compute pins (§4.2), and by walkers, to check them (§7.3); a system that only holds
and serves records never executes it. §5.1 states the input on which the
function is defined; checking it is the reader's parser's job, and its results are the same in
every language.

### 5.1 Input

The input is the bytes of a record as obtained from its system, in any JSON formatting. A reader
MUST reject the input, and treat it as not conformant, if

1. it begins with a UTF-8 byte order mark (`EF BB BF`);
2. it is not well-formed UTF-8;
3. it is not a JSON text by RFC 8259 (for example it contains `NaN` or `Infinity`);
4. its top-level value is not an object;
5. any object, at any depth, has two members with the same name (compared after decoding
   escapes); or
6. any string, at any depth, contains a surrogate code point (U+D800 to U+DFFF, which in JSON can
   only arise from an unpaired `\uD8xx`-style escape) or a noncharacter (U+FDD0 to U+FDEF, or any
   code point whose low 16 bits are FFFE or FFFF).

These rules apply to the whole input, `extensions` and `signature` included. Some JSON parsers
accept duplicate names or unpaired surrogates silently (JavaScript's `JSON.parse`; Go's
`encoding/json`, which keeps the last duplicate and replaces an unpaired surrogate with U+FFFD); an
implementation built on one MUST add the check, which for those two means a parser that reports
member names as it reads them.

A number anywhere in the input is acceptable to §5.1 whatever its magnitude or precision. A reader
MUST NOT reject a record because a number in `extensions` or `signature` is outside its native
numeric range (`1e400`); numbers elsewhere are rejected by §5.2 regardless of form.

### 5.2 Canonical form

Given a record that passed §5.1:

1. **Exclude.** Remove the top-level members `extensions` and `signature`, if present. Nothing
   else is removed.
2. **Restrict values.** Every remaining value, at every depth, MUST be an object, an array or a
   string. If any is a number, `true`, `false` or `null`, the record has no canonical form and is
   not conformant. (Values inside `extensions` are unrestricted, because they were removed in
   step 1.)
3. **Sort the sets.** If `basedOn` is present it MUST be an array whose every element is an
   object with a string member `ref`; if any two elements have the same `ref`, the record has no
   canonical form. Sort its elements by `ref`. Do the same for `supersedes`. No other array is
   reordered.
4. **Serialise** the resulting object with no insignificant whitespace:
   - an object as `{`, its members separated by `,`, then `}`; each member as its name
     (serialised as a string), `:`, its value; members in ascending order of name;
   - an array as `[`, its elements in order separated by `,`, then `]`;
   - a string as `"`, its characters, then `"`, where only these characters are escaped:

     | Character | Written as |
     |---|---|
     | U+0022 `"` | `\"` |
     | U+005C `\` | `\\` |
     | U+0008 | `\b` |
     | U+0009 | `\t` |
     | U+000A | `\n` |
     | U+000C | `\f` |
     | U+000D | `\r` |
     | any other U+0000 to U+001F | `\u00` followed by two **lowercase** hexadecimal digits |

     Every other character, including `/`, U+007F, U+2028, U+2029 and every non-ASCII character,
     is written as itself.
5. **Encode** the serialisation as UTF-8. These bytes are the canonical form.

**Order.** "Ascending order" for member names, and for `ref` values in step 3, is lexicographic
order of Unicode code points, which is the same as the byte order of the strings' UTF-8 encodings.
Implementations whose strings are UTF-16 (JavaScript, Java, C#) MUST NOT compare by code unit:
U+FF61 sorts before U+1F600 by code point and after it by UTF-16 code unit. The suite has a
vector for this.

**No normalisation.** Strings are hashed exactly as given. In particular no Unicode normalisation
is applied: `é` written as U+00E9 and as U+0065 U+0301 are different strings and give different
hashes. Writers SHOULD write NFC. A reader never needs to normalise, because the record it hashes
is the record the system served, not a retyping of it.

### 5.3 Record hash

The **record hash** is the SHA-256 (FIPS 180-4) of the canonical form, written as the string
`sha256:` followed by the 64 lowercase hexadecimal digits of the digest.

The record hash covers `protocol`, `id`, `version` and `system`, so the same content held by two
systems, or under two versions, has two different hashes. A copy of a record is not the record.

### 5.4 Implementation notes (non-normative)

- The law is a restriction of the JSON Canonicalization Scheme (RFC 8785) chosen so that no part of
  it needs more than a standard library: there are no numbers to format and no Unicode tables to
  consult. On the inputs the law accepts, its output equals RFC 8785's, except for the sorting of
  `basedOn` and `supersedes` and RFC 8785's UTF-16 member order, which this law replaces by code
  point order.
- In Python, `json.dumps(obj, ensure_ascii=False, separators=(",", ":"), sort_keys=True)` produces
  step 4 exactly. In Go, `encoding/json` escapes `<`, `>`, `&`, U+2028 and U+2029, and cannot be
  used for step 4 unmodified. In JavaScript, `JSON.stringify` cannot be used for objects at all:
  JavaScript enumerates integer-like member names (`"9"`, `"10"`) first in numeric order whatever
  the insertion order, so `{"10":…,"9":…}` cannot be produced. A JavaScript implementation
  serialises objects itself; `JSON.stringify` remains correct for a single string. The suite has a
  vector for this.
- **Size budget.** The budget is stated as the size of the reference implementation
  (`reference/dpp.py`, Python, standard library only): the hash law, with the input checks of
  §5.1, is under fifty lines (30 non-blank lines: 19 for §5.2–5.3, 7 for §5.1 parsing, 4 for the error helper), and the whole
  implementation, hash law, file-based resolver and walk, is under a hundred (99 lines). The
  suite's JavaScript and Go programs are hash-only cross-checks (Appendix C); their sizes are not
  a claim of this specification.

---

## 6. The resolver

### 6.1 Operations

A system answers for its own records, and only its own. It is never required to fetch another
system's records on a reader's behalf.

| Operation | Required | Answer |
|---|---|---|
| `describe()` | yes | the system's descriptor (§6.3) |
| `get(id, version)` | yes | the record, or "not held" |
| `versions(id)` | no | the versions of `id` the system holds (§6.4) |

All operations are read-only. Every binding expresses them as files at fixed paths under the
system's base (§6.2), so a static file server, a directory, and an application endpoint are
interchangeable.

### 6.2 Layout

Relative to a system's base:

| Path | Content | Required |
|---|---|---|
| `system.json` | the descriptor (§6.3) | yes |
| `<id>/<version>.json` | the record `id@version@<system>` | for every record held |
| `<id>/index.json` | the versions listing for `id` (§6.4) | no |

`<id>` and `<version>` are the tokens themselves; tokens need no escaping. The reserved names of
§3.3 keep these paths from colliding: no id ends in `.json`, so no `<id>/` directory is confused
with `system.json`, and no version is `index`, so no record is confused with a listing.

A base MAY contain other files and directories (an ADR directory's Markdown, for instance); readers
ignore them.

### 6.3 Descriptor

`system.json` is a JSON object (I-JSON) with members

- `protocol` (REQUIRED): `dpp/1`;
- `system` (REQUIRED): the system identifier, exactly as it appears in the system's records;
- `name` (OPTIONAL): a human-readable name;
- `profile` (OPTIONAL): a URI-reference to the system's profile document (§9.4);
- `features` (OPTIONAL): an array of strings; `versions` means the system offers §6.4.

Only `protocol` and `system` decide whether a descriptor is conformant: a descriptor is
conformant when it is an I-JSON object (§5.1) whose `protocol` is `dpp/1` and whose `system` is
exactly the identifier being resolved. Readers MUST ignore other members, and MUST ignore an
optional member whose value is malformed (a `features` that is not an array, a `name` that is not a
string). The descriptor is not hashed and may change.

The descriptor is what makes an answer of "not held" meaningful: it tells a reader that the place
it is looking is the system it means, and that the system implements this protocol (§6.8).

### 6.4 Versions listing

`<id>/index.json`, if offered, is a JSON object with members `protocol` (`dpp/1`), `system`, `id`,
and `versions`: an array of the version tokens the system holds for `id`, oldest first in the
system's own recording order. The listing is the only forward view the protocol has: from it a
reader can find versions recorded after the one it holds. It does not show successors in other
systems or under other ids (Appendix A, Q2). A missing listing means the system does not offer
one, not that it holds no versions.

### 6.5 HTTPS binding

**Base.** The HTTPS base of a system is derived from its identifier:

- if the identifier has an empty path (`https://decisions.example.org`), the base is the
  identifier followed by `/.well-known/decision-provenance/`
  (`https://decisions.example.org/.well-known/decision-provenance/`), a well-known URI (RFC 8615,
  §13);
- otherwise (`https://git.example.internal/payments/docs/adr`), the base is the identifier
  followed by `/`.

A system that has a host to itself thus keeps its files out of the host's root namespace; a system
that shares a host lives under its own path, which is what a static file server or a repository
host's page service can offer without configuration.

**Requests.** Each operation is an HTTP `GET` (RFC 9110) of the corresponding path under the
base, for example `GET <base>ADR-0007/1.json`. A reader SHOULD send `Accept: application/json`.
A system SHOULD respond with `Content-Type: application/json`; a reader MUST NOT reject a response
solely for its content type.

**Responses.**

| Response | Meaning |
|---|---|
| `200` with a body | the file; for a record, see §6.8 |
| `404` or `410` | the file does not exist: for a record, "not held" provided the descriptor was obtained (§6.8) |
| `401`, `403`, `407` | refusal: not reachable |
| `301`, `302`, `303`, `307`, `308` | redirection: a reader MUST follow up to 5 in sequence, to `https` URLs (or, if the identifier is `http`, `https` or `http`), and the outcome is that of the final response; more than 5, or a redirection to another scheme, is not reachable |
| `304` | only in answer to a conditional request: the reader's cached copy is current |
| anything else, or no response | not reachable |

**Caching.** A record's hashed content never changes (§3.8), so a system SHOULD serve records with
long cache lifetimes, and a reader MAY cache a held record indefinitely, keyed by reference. A
reader that caches MAY show stale `extensions`. A cached descriptor MAY be reused within its HTTP
cache lifetime.

**Authentication.** A system MAY require authentication by any HTTP mechanism (bearer tokens,
mutual TLS, cookies, network position). This specification does not define one. How a reader
obtains credentials is between the reader and the system. A refusal is "not reachable" (§11.1).

### 6.6 File binding

A directory is a conformant system, with no server and no code, when it contains the layout of
§6.2 directly: `system.json` at its top, and one `<id>/<version>.json` per record. Its base is the
directory. A Git repository, a shared network drive, an archive and an object-store prefix are all
directories for this purpose: a reader only opens files by path and never lists a directory.

A reader resolving a record in a directory

- opens `<base>system.json`; if it is absent, unreadable, or not a conformant descriptor naming the
  identifier being resolved, the system is **not reachable**;
- opens `<base><id>/<version>.json`; if that path does not exist, the record is **not held**; if it
  exists but cannot be read, **not reachable**; otherwise see §6.8.

A reader MUST check that `<id>` and `<version>` are tokens (§3.3) before it builds a path from
them, so that no reference can name a path outside the base.

On a file system that folds case, a lookup of `adr-7/1.json` may open `ADR-7/1.json`. If the
record found has an `id` or `version` that equals the requested one only under ASCII case folding,
the requested record is **not held** (§3.3 forbids the system to hold both).

### 6.7 Locations configured by the reader

A reader MAY be configured with a location for a system identifier: a directory (a clone, a mount,
an unpacked archive) or a URL to use as the base instead of the one §6.5 derives (a mirror, an
internal proxy). When it has one, it resolves that system there. This is how a reader reaches an
ADR directory in a repository that no web server publishes, and how a system that has moved stays
resolvable under its unchanged identifier.

A configured location is the reader's own; it does not change any identifier, reference or hash,
and it involves no third party. A record obtained from a configured location is held only if its
`system` member is the identifier being resolved (§6.8). The security consequences of mirrors are
in §11.2.

### 6.8 Outcome of a get

Resolving `id@version@system` has exactly one of three outcomes:

| Outcome | When |
|---|---|
| **held** | The descriptor was obtained and names `system`; the record file was obtained; it is conformant (§3.6); and its `id`, `version` and `system` are exactly those requested. |
| **not held** | The descriptor was obtained and names `system`, and the system answered that the record file does not exist (HTTPS `404` or `410`; no such path in a directory), or the case-folding rule of §6.6 applies. |
| **not reachable** | Anything else: no location for the system; no answer; a refusal; a descriptor that is missing, not conformant, or names another system; a record that is not I-JSON, has no canonical form, is not conformant, declares a protocol major version the reader does not implement, or names a different `id`, `version` or `system`. |

"Not held" requires an answer from a conformant system. A `404` from a host whose descriptor
cannot be obtained says nothing about decisions, and is "not reachable".

### 6.9 Signalling "not held"

A system signals "not held" in exactly one way per binding, and in no other:

- **HTTPS:** status `404 Not Found` (or `410 Gone`) for `<base><id>/<version>.json`, while
  `<base>system.json` answers `200` with its descriptor. The response body is ignored.
- **Files:** no file at `<base><id>/<version>.json`, while `<base>system.json` is present.

There is no "not held" record, error document, or field. A system MUST NOT signal "not held" with
`200` and a body describing an error; a reader treats such a body as a record, finds it not
conformant, and reports not reachable. A system that once held a record and has ceased to
(§3.8) SHOULD answer `410`; a reader treats `404` and `410` alike. An application that is not a
static file server (a tracker's plugin, a governance engine's endpoint) answers the same paths
with the same status codes.

An exchange in which ADR-0004 version 2 is not held by
`https://git.example.internal/payments/docs/adr`:

```
GET /payments/docs/adr/system.json HTTP/1.1
Host: git.example.internal
Accept: application/json

HTTP/1.1 200 OK
Content-Type: application/json

{"protocol":"dpp/1","system":"https://git.example.internal/payments/docs/adr"}

GET /payments/docs/adr/ADR-0004/2.json HTTP/1.1
Host: git.example.internal
Accept: application/json

HTTP/1.1 404 Not Found
```

The same system as files, with the same answer:

```
docs/adr/system.json          present: {"protocol":"dpp/1","system":"https://git.example.internal/payments/docs/adr"}
docs/adr/ADR-0004/1.json      present
docs/adr/ADR-0004/2.json      absent      -> ADR-0004@2 is not held
```

How the same `404` reads in other circumstances:

| Descriptor request | Record request | Outcome |
|---|---|---|
| `200`, names the system | `404` / `410` | **not held** |
| `200`, names another system | `404` | not reachable |
| `404`, or not JSON | `404` | not reachable: no conformant system answered |
| `401` / `403` | (not sent) | not reachable: refusal |
| `200`, names the system | `403` | not reachable: refusal (or, if the system prefers not to disclose existence, it answers `404`, §11.6) |
| no answer | (not sent) | not reachable |

The chain fixture of the suite (Appendix C) contains this case as files.

---

## 7. The walk

### 7.1 Definition

A **walk** from a starting reference object follows `basedOn`, hop by hop, across systems, until
every reachable branch ends. Each hop gets exactly one result. The walk follows `basedOn` and
nothing else: not `supersedes`, not `why.href`, not anything in `extensions`. (A `why.ref` is
always also in `basedOn`, §3.4.)

### 7.2 Results

| Result | Meaning — fixed |
|---|---|
| **held** | The system holding the reference answered with the record, it is conformant, and its record hash equals the hop's pin. |
| **not held** | The system answered, as a conformant system, that it does not hold the record. |
| **not reachable** | No conformant answer was obtained: the system did not answer, refused, is not conformant, or answered with content that does not match the hop's pin. |

The meanings are fixed by this specification; their presentation is not. A walker MAY show the
reason within a result (refused, timed out, pin mismatch, unknown protocol version), and MAY use
any words, colours or layout, but MUST NOT merge two results, split one into results with other
meanings, or report a hop as any other result. In particular a walker MUST NOT report "unknown",
and MUST NOT present a not-reachable hop as not held, or the reverse.

A result describes the answer obtained during this walk, at that time, with the walker's access.
"Not held" is the system's statement that it does not hold the record for this reader; it is not a
statement that the decision never existed (§11.6).

### 7.3 Procedure

1. Let *Q* be a queue containing one hop: from nothing to the starting reference object. Let *R*
   be an empty map from reference strings to outcomes, and *X* an empty set.
2. While *Q* is not empty, take a hop (*f*, *e*) from it, where *e* is a reference object.
   1. If *R* has no outcome for *e*.`ref`, resolve it (§6.8) and store the outcome in *R*.
   2. The hop's result is the outcome in *R*, except that if the outcome is held and the record
      hash of the held record (§5.3), computed by the walker, differs from *e*.`hash`, the hop's
      result is not reachable.
   3. Report the hop (*f*, *e*.`ref`, result).
   4. If the result is held and *e*.`ref` is not in *X*, add it to *X* and add to *Q* one hop
      (*e*.`ref`, *b*) for each entry *b* of the record's `basedOn`.

The starting reference object is the only one that may lack `hash` (a walker may be asked to start
from `id@version@system` alone); its hop is then held without verification, and the walker SHOULD
show the record hash it computed so that the start can be pinned. Every other hop comes from a
record's `basedOn` and so carries a pin.

Each reference is resolved at most once per walk and each held record expanded at most once, so a
record reached along several paths appears once per referring record, all with the same outcome,
and the pin is checked per hop. A held record with an empty `basedOn` is an origin. The order in
which hops are reported is not significant.

### 7.4 Termination and limits

Every reference in a record is pinned, so the references between records cannot form a cycle: a
cycle would need a record hash to depend, through the pins, on itself. A walk therefore terminates
whenever the set of records it can reach is finite. Resolving each reference once (§7.3) is for
efficiency, and guards against a non-conformant system that serves records whose pins do not hold.

A walker MAY bound a walk by depth, number of hops, total bytes or time. A walk so bounded is
**truncated**: the walker MUST say so, and MUST list the references it reached but did not resolve
separately from the hops, as *not walked*. Not walked is not a hop result: it records that the
walker stopped, not anything a system answered, and those references carry none of the three
results.

### 7.5 What the walk does not do

A walk contacts only the systems named in the references it follows, at the locations §6.5
derives or §6.7 configures, and only at the paths of §6.2. It needs no third party, so a chain
across systems inside one organisation's network is walked without any request leaving it.

A walk reports provenance. It does not evaluate whether any decision binds, is current, was
authorised, or was right. A result of held for a record whose `status` is `accepted` says only
that the system holds that record with that value.

### 7.6 Walk report (non-normative)

The suite records walks as

```json
{ "start": { "ref": "PAY-142@3@https://tickets.example.internal" },
  "hops": [ { "from": null, "to": "PAY-142@3@https://tickets.example.internal", "result": "held" },
            { "from": "PAY-142@3@https://tickets.example.internal",
              "to": "ADR-0007@1@https://git.example.internal/payments/docs/adr", "result": "held" } ] }
```

with `result` one of `held`, `not-held`, `not-reachable`, and hops sorted by `from` (the starting
hop, `null`, first) then `to`. Walkers MAY use this shape for interchange.

---

## 8. Conformance

There is one conformance class: **a conformant system**. It has no levels, tiers or optional
parts other than those marked OPTIONAL above. A system is conformant when

1. it exposes the descriptor of §6.3 at the base of §6.5 (HTTPS) or §6.6 (files), or both;
2. every record it exposes is at the path of §6.2, is conformant (§3.6), and has `system` equal to
   its identifier;
3. it honours immutability (§3.8): no hashed content changes under a published triple, and no
   version is reused;
4. it answers "not held" (HTTPS `404`/`410`, or an absent file) for every record it does not hold,
   and for a record it holds only where it declines to disclose the record's existence to the
   reader (§11.6); and
5. if it offers `versions` (§6.4), the listing is accurate.

Conformance asks nothing of a system's ability to compute hashes: a system that only holds and serves
records, such as a directory of hand-written files, never executes the hash law. The pins in its
records are computed by whoever wrote them (§4.2).

A claim of conformance names the protocol token and the specification version (`dpp/1`,
specification 1.0) and, where a suite was run, the suite version.

Readers and walkers are not a conformance class. Their correctness is defined by §5, §6.8 and §7,
and checked by the conformance suite (Appendix C): the canonicalisation vectors, the resolver
fixture and the chain fixture have exactly one correct result each.

---

## 9. Extensibility

### 9.1 Readers ignore what they do not know

A reader MUST ignore members it does not recognise — undotted record members (§3.7), dotted record
members it does not understand, members of reference objects other than `ref` and `hash`,
descriptor and listing members — and MUST NOT treat a record as not conformant because of them.
Ignoring a member never removes it from the canonical form.

### 9.2 Where systems put their own content

Content that must be pinned goes in dotted members; content that may change goes in
`extensions` (§3.7). Nothing else is open to systems.

### 9.3 Where the protocol grows

New optional undotted members, new descriptor members and `features` values, and new optional
files under the base are added by minor versions of this specification (§12). Anything that would
change a hash, a required member, the reference syntax, the layout of an existing path, or the
meaning of a walk result is a new major version.

### 9.4 Profiles

A **profile** is a system's own document stating what it adds: who may decide, what its `status`
values mean, whether and how its decisions bind, what clocks it keeps, what its dotted members and
`extensions` contain. A system SHOULD publish its profile and MAY name it in its descriptor
(`profile`). Profiles are not part of this specification, are not checked by its suite, and cannot
change the meaning of anything this specification defines. A reader that does not know a profile
loses nothing this specification promises. Appendix B is a non-normative example.

---

## 10. PROV-O rendering (non-normative)

The wire format is the JSON of §3. For systems that keep RDF, a record renders into the W3C PROV
Ontology (PROV-O) as follows. The rendering is lossy, and it is a rendering, not an alternative
wire format.

**IRIs.** A record has no IRI of its own on the wire. A renderer needs one, and this rendering uses
`<system>#<id>@<version>` — the system identifier with the rest of the reference as fragment —
which is deterministic, needs no registry, and is a valid IRI because system identifiers have no
fragment. A renderer MAY instead use the record's HTTPS location. Terms PROV-O lacks are written
here with the prefix `dpp:`; this specification mints no namespace for them, and a renderer binds
the prefix to a namespace it controls.

| Record | PROV-O |
|---|---|
| the record | a `prov:Entity` |
| the act of deciding | a `prov:Activity` that generated the entity (`prov:wasGeneratedBy`) |
| `by` | a `prov:Agent` (`prov:SoftwareAgent` where the system knows it is software) associated with the activity (`prov:wasAssociatedWith`) |
| `attributedTo` | a `prov:Agent` the entity `prov:wasAttributedTo`; the `by` agent `prov:actedOnBehalfOf` it |
| `at` | `prov:generatedAtTime` of the entity, as `xsd:dateTime`, when `at` has a time; a date-only `at` cannot be rendered there (the property's range is `xsd:dateTime`) and is rendered as `dpp:at` typed `xsd:date` |
| `basedOn` entry | `prov:wasDerivedFrom` from the entity, and `prov:used` from the activity, to the referenced entity |
| `supersedes` entry | `prov:wasRevisionOf` |
| `statement`, `why`, `status` | no PROV-O term: `dpp:statement`, `dpp:why`, `dpp:status` |

```turtle
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix dpp:  <https://renderer.example/terms#> .   # the renderer's own namespace, not the protocol's

<https://pricing.example.internal#eu-card-fees@r42>
    a prov:Entity ;
    prov:wasGeneratedBy _:decide ;
    prov:generatedAtTime "2026-10-21T06:00:00Z"^^xsd:dateTime ;
    prov:wasAttributedTo <mailto:finance-ops@example.internal> ;
    prov:wasDerivedFrom <https://git.example.internal/payments-service/docs/adr#ADR-0003@1> ;
    prov:wasRevisionOf <https://pricing.example.internal#eu-card-fees@r41> ;
    dpp:why "Fee schedule FS-2026-11 approved by finance; applied as configuration revision r42." .

_:decide a prov:Activity ;
    prov:wasAssociatedWith <spiffe://example.internal/pricing-engine> ;
    prov:used <https://git.example.internal/payments-service/docs/adr#ADR-0003@1> .

<spiffe://example.internal/pricing-engine> a prov:SoftwareAgent ;
    prov:actedOnBehalfOf <mailto:finance-ops@example.internal> .
```

What the rendering loses is the point of the protocol: PROV-O records what was derived from what,
by whom, when; it has no term for the reason. `dpp:why` carries it, outside PROV-O. Pins, the
three walk results, and `extensions` are not rendered.

---

## 11. Security considerations

### 11.1 Authentication and refusal

A system MAY require authentication for any operation. This specification defines no mechanism,
no credential format, and no delegation. A refusal (HTTPS `401`, `403`, `407`; a file the reader may
not open) is "not reachable" for that hop, which is an answer: the walk reports where it was
stopped, and continues on other branches.

A reader MUST NOT send credentials configured for one system to another, including when following
a redirection to a different origin.

### 11.2 Integrity

- **Pins** detect any change to a referenced record's hashed content, whether by the system, a
  mirror, a cache or an attacker on the path. They detect nothing about `extensions`, and nothing
  about the starting reference of a walk if it was given without a hash.
- **Transport.** HTTPS protects records in transit from the system or mirror that served them. It
  says nothing about whether that party served the true record. `http` identifiers have no
  transport protection.
- **Files.** A record read from a directory is as trustworthy as the directory: its file system
  permissions, its repository's history, and whoever produced the clone.
- **Mirrors and configured locations** (§6.7) cannot substitute a record without the pin failing.
  They can withhold records (which reads as not held or not reachable) and can serve a forged
  starting record when the start is unpinned.
- **Hash strength.** The protocol assumes SHA-256 collision and second-preimage resistance. The
  `sha256:` prefix lets a later major version name another function.

### 11.3 Signatures

Signatures are OPTIONAL. A `signature` (§3.7) is computed over the canonical form (§5.2), which
covers every hashed member including `id`, `version` and `system`, and does not cover `extensions`.
`scheme` names the scheme (for example `ed25519`, `ecdsa-p256-sha256`, `jws-detached`, `ssh-sig`,
`openpgp`, `x509-cms`); `value` is the signature in that scheme's usual text encoding; `key`, if
present, identifies the key in that scheme's terms. This specification registers no schemes and
defines no key distribution or trust. A valid signature shows that the holder of a key signed this
canonical content. It does not show that the signer was entitled to decide, that the decision
binds, or that `by` and `at` are true — those are profile matters.

### 11.4 What the protocol does not protect against

- A system that records something false when it first publishes it: a wrong `by`, a back-dated
  `at`, an invented `why`. The protocol reports what a system says; it cannot check it.
- A system that ceases to hold records (deletion appears as "not held"), or that serves an
  unpinned starting reference differently to different readers.
- A compromised system, or a compromised key.
- Denial of service against a system: it appears as "not reachable".
- Disclosure of record content to anyone the system lets read it. The protocol has no
  confidentiality mechanism of its own.

### 11.5 Walkers follow attacker-supplied locations

A record from one system names other systems, and a walker contacts them. A record crafted by an
untrusted party can therefore make a walker send requests to hosts of the attacker's choosing,
including hosts on the walker's internal network (server-side request forgery), or make it walk an
unbounded chain. A walker

- MUST request only the paths of §6.2, built only from tokens that pass §3.3;
- MUST NOT follow redirections to schemes other than those of §6.5;
- SHOULD apply an operator-set policy on which system identifiers it will contact, and SHOULD by
  default not contact private, loopback or link-local addresses on behalf of a walk that started
  from an untrusted record;
- SHOULD bound walks (§7.4) and record sizes (§3.1).

A file resolver MUST validate tokens before building paths (§6.6); the token grammar admits no
`/`, `\`, `..` or leading `.`.

### 11.6 Existence and privacy

A system distinguishes "not held" (`404`) from refusal (`403`). Some systems do not wish to reveal
that a record exists to a reader who may not see it; such a system MAY answer "not held" instead
of refusing, and a reader cannot tell the difference. "Not held" is therefore the system's answer
to this reader, never proof of absence.

A walk reveals to each system which of its records the walker is interested in, and when.

`by` and `attributedTo` commonly identify people, and they are hashed and immutable. A system with
erasure obligations SHOULD use pseudonymous identifiers in them, resolvable to people only inside
the system, and MAY cease to hold records it must erase (§3.8). Personal data that may need to
change belongs in `extensions`.

---

## 12. Versioning of the protocol

The protocol token has the form `dpp/<major>`; this specification defines major version `1`.
Records carry the token in `protocol`; descriptors and listings carry it too. The specification
text has versions `<major>.<minor>` (this is `1.0`).

**Minor versions** of the specification MAY add optional undotted record members, optional
reference-object members, descriptor members, `features` values, and optional files under the
base, and MAY clarify text. They MUST NOT change the hash law, the required members, the reference
syntax, the paths of §6.2, the outcomes of §6.8 or the results of §7.2, and MUST NOT make a
previously conformant record or system non-conformant. Records written under any `1.x`
specification carry `dpp/1`, and every `dpp/1` reader computes the same hash for them.

**A new major version** is required for anything else. A reader that receives a record whose
`protocol` names a major version it does not implement treats it as not conformant: the hop is not
reachable. A system conformant to `dpp/1` exposes only `dpp/1` records under the layout of §6.2;
how a system exposes records of two major versions at once is for the later major version to
define.

No version of the protocol is identified by a URL, and no party has to be consulted to implement
or claim one.

---

## 13. IANA considerations

This specification uses the well-known URI suffix `decision-provenance` (§6.5). As of 2026-10-27
the IANA "Well-Known URIs" registry contains no entry named `decision-provenance`, `decisions` or
`dpp`, and no entry that collides with this use. A registration request under RFC 8615 §3.1 would
read:

- URI suffix: `decision-provenance`
- Change controller: the maintainers of this specification *(to be named — see Appendix A.3)*
- Specification document: this document, `dpp/1` specification 1.0
- Status: provisional until this specification is final; then permanent
- Related information: the suffix is followed by the layout of §6.2

Registration reserves the name against a different use. It is not a runtime dependency: no system
or reader consults IANA, and systems whose identifiers have a path do not use the well-known URI
at all.

No media type is registered; records are `application/json`.

---

## 14. References

**Normative.** RFC 2119 and RFC 8174 (requirement key words); RFC 3339 (date and time); RFC 3986
(URI); RFC 7493 (I-JSON); RFC 8259 (JSON); RFC 8615 (well-known URIs); RFC 9110 (HTTP semantics);
FIPS 180-4 (SHA-256).

**Informative.** RFC 8785 (JSON Canonicalization Scheme); W3C PROV-O (PROV Ontology); M. Nygard,
"Documenting Architecture Decisions" (2011), the ADR form.

---

## Appendix A. Decisions

This specification was drawn from Part 1 of *The Decision Provenance Protocol, Writ's authority
profile, and the architecture*, Draft 3 (2026-10-22), under seven fixed constraints: no central
point; three things only; a reference always carries a version; three walk results; files as a
first-class transport; one canonical form, one function; `why` required. Draft 3 was treated as
input, not authority. Where it was right it is kept and not listed; every departure is listed
here with its reason. Parts 2 and 3 of Draft 3 appear only as the non-normative Appendix B.

### A.1 Departures from Draft 3

**A-1. `id` is a token local to its system, not a global IRI.** Draft 3 made `id` an IRI under a
namespace the system owns *and* put `system` in every reference, giving each decision two global
identities with no rule for which wins when they disagree. Its file binding then needed a
URL-encoded IRI as a directory name: long, full of `%`, and unsafe on case-folding file systems.
Here identity is (`system`, `id`) and `id` is a short token that is its own file name. A system
whose native ids are IRIs keeps them in a dotted member.

**A-2. `version` is chosen by the system; the content hash is a required pin beside it.** This is
the largest change. Draft 3 made `version` the record hash. That gave three real properties: every
reference was a content pin; a system could not rewrite a version under its referrers; and chains
could not cycle. It also cost three things the constraints do not allow. (i) The referenced system
had to compute hashes: every record's file name was a SHA-256, so an ADR directory could not be
made conformant with no code, and correcting a typo renamed the file. (ii) No system could use its
native version (a ticket revision, a configuration revision `r42`, a commit, a run id); each would
carry two versions, its own and the protocol's. (iii) References became illegible in the places
people write them: tickets, commit messages, ADR prose. Here `version` is a token the system
chooses, and the hash is REQUIRED in every reference object as `hash` (§4.2), computed by the
writer of the reference and checked by the walker, never by the referenced system. All three of
Draft 3's properties are kept: every reference is a content pin, rewriting is detected at every
hop (§7.3), and references between records cannot cycle (§7.4). *Cost accepted:* writing a
reference needs one execution of the hash law by its writer; an ADR author who references another
ADR runs an implementation of §5 once, while the referenced directory itself needs nothing.

**A-3. The record carries `system`.** Draft 3's record had no `system`; only references did, so a
record read from a file or a mirror did not say where it belonged, and the same content in two
systems had the same hash. Here `system` is required and hashed: a record is self-describing, a
mirror serving another system's record is caught (§6.8), and a copy is not the record (§5.3). The
consequence is that a system cannot change its identifier (§3.3); relocation is handled by
redirection or reader-configured locations, which do not touch identifiers.

**A-4. One reference form, `id@version@system`, with a reference object around it.** Draft 3 had
an object `{id, version, system}` and called the string `id@version` "equivalent". It is not:
it drops the system, which violates constraint 3 in spirit (a reference must say what was relied
on, and where). Here the string is always complete, and the object is `{ref, hash}` so that
the string, the sort key (§5.2) and the walk key (§7.3) are the same thing.

**A-5. No Unicode normalisation in the hash law.** Draft 3 required NFC. NFC needs the Unicode
normalisation tables, which the standard libraries of Go, Rust and C do not include, so the law
could not be "implementable in under fifty lines in any language" (constraint 6). It is also
unnecessary: a reader hashes the bytes the system served, not a retyping, so both sides always
hash the same string. Here strings are hashed as given, writers SHOULD write NFC, and the suite
proves that NFC and NFD forms hash differently. RFC 8785 makes the same choice.

**A-6. No numbers, booleans or null in hashed content.** Draft 3 required "numbers in their
shortest round-trip form", which is the ECMAScript double-formatting algorithm (Ryu, Grisu or
equivalent): hundreds of lines outside JavaScript, and a source of disagreement between parsers
that read `1` and `1.0` as different types. No member the protocol defines needs a number. Here
hashed content is objects, arrays and strings only; a system pins numeric content as decimal
strings in a dotted member, and numbers remain free in `extensions`. `true`, `false` and `null` go
with them, for the same reason at smaller scale: every one is a value two systems can spell
differently in their native types. The suite has vectors for each.

**A-7. `basedOn` sorts by the full reference; duplicates are rejected; `supersedes` sorts too.**
Draft 3 sorted `basedOn` "by `id` then `version`", ignoring `system`. Two references with the same
id and version in different systems (`D-7@2` in two trackers) then had no defined order, and two
correct implementations could produce different hashes for the same record. That is a defect in
the one shared function. Here the sort key is the complete `ref`, compared by code point;
duplicate refs make a record unhashable rather than letting implementations choose which to keep;
and `supersedes` (now a list, A-9) is a set sorted the same way.

**A-8. `version` is inside the hash.** In Draft 3 `version` was the hash and so was excluded from
it. With A-2 it is an ordinary identifying member and is hashed, so the pin also pins the label.
`signature` and `extensions` stay outside, as in Draft 3.

**A-9. `supersedes` is a set, not "at most one".** A decision that consolidates several earlier
ones (one ADR replacing two) is ordinary, and Draft 3 could not record it. The forward direction
is unchanged: there is none (Q2).

**A-10. `acceptedBy` and `acceptedAt` are removed.** They define a second agent and a second clock
for acceptance, which constraint 2 places out of scope. A system that distinguishes deciding from
accepting records acceptance as its own decision record (based on the accepted one), in a dotted
member, or in `extensions`, and documents it in its profile. Appendix B shows the first.

**A-11. `attributedTo` is defined.** Draft 3 used `attributedTo` in the description of `by` but did
not list it as a field. It is now an optional hashed member (§3.4).

**A-12. Systems may not add undotted top-level members; dotted members are theirs.** Draft 3
allowed a system to "expose more fields", all hashed, in a namespace shared with the protocol, so
a field one system invented could collide with one a later protocol version defines, or with
another system's field of the same name and different meaning. Here undotted names belong to the
protocol and dotted names to systems. Draft 3's own advice for pinned extension content ("put a
hash of it in a regular field") becomes: put it in a dotted member.

**A-13. The well-known URI is used only at an origin, and is named `decision-provenance`.**
Draft 3 placed `.well-known/decisions/` under any base URL. RFC 8615 defines well-known URIs only at
the root of an origin; below a path they are not well-known URIs and gain nothing. And a static
host serving an ADR directory under a path cannot place files at its origin's root. Here (§6.5) an
identifier with no path uses the well-known URI, and an identifier with a path uses itself as the
base. `decisions` is replaced because it is too generic for a shared registry and would invite a
collision with an unrelated use; see Q4.

**A-14. The versions listing has its own path.** Draft 3 put the record at `…/<id>/<version>` and
the listing at `…/<id>`. On a file system `<id>` cannot be both a file and a directory, so Draft 3's
file binding could not hold a listing at all, which breaks constraint 5. Here the listing is
`<id>/index.json` and `index` is a reserved version.

**A-15. File names end in `.json`.** Static file servers and repository hosts choose content types
by extension; with `.json` an unconfigured static host serves records correctly.

**A-16. A descriptor is required, and "not held" requires it.** Draft 3 had no way to tell "this
system does not hold the record" from "this host is not a decision system at all": both returned
`404`, and the second would have been reported as not held, which falsifies the result's fixed
meaning (constraint 4). Here `system.json` is required, and "not held" is only reported when it
was obtained and names the system (§6.8).

**A-17. A file-based system declares its identifier; it is not "the repository's URL".** Draft 3
said a repository's identifier is its URL. That fails when a repository holds more than one system
(two ADR directories, or ADRs beside exported tickets), when the layout is not at the repository
root, and when the repository URL serves a web page rather than the layout. Here the directory's
`system.json` declares the identifier, and readers reach unpublished directories by configured
location (§6.7).

**A-18. `at` may be a date.** Draft 3 required an RFC 3339 UTC date-time. A hand-written ADR knows a
date, and padding it to `T00:00:00Z` asserts a precision the system does not have.

**A-19. `why` as a reference is defined.** Draft 3 allowed "a reference to where it is written"
without saying what that is. Here it is either `href` (a document, resolved against the record's
location so that an ADR's Markdown beside its record works over files and HTTPS alike, optionally
pinned by `hash`) or `ref` (another decision, which must also be in `basedOn` so the walk sees
it).

**A-20. Content that does not match its pin is "not reachable".** Draft 3 did not say what a hop
reports when the record obtained differs from the one referenced. It is not "not held" (the system
answered with something under that triple), so it is the third result: no conformant answer
matching the reference was obtained. The walker may show "pin mismatch" as the reason.

**A-21. Walk termination rests on the pins, not on versions being hashes.** Draft 3 argued
termination from versions being hashes. With A-2 the argument moves to the required pins, which
make cycles between records impossible (§7.4); the walk also resolves each reference once, for
efficiency and against non-conformant systems.

**A-22. PROV-O: `by` is associated with the activity; `attributedTo` is attribution.** Draft 3 mapped
`by` to `prov:wasAttributedTo`. That conflates the agent that acted with the party responsible,
which is exactly what `by` and `attributedTo` separate. Here `by` is `prov:wasAssociatedWith` on the
generating activity and `attributedTo` is `prov:wasAttributedTo`, with `prov:actedOnBehalfOf` between
them. The rendering also says what PROV-O cannot carry: `why`.

**A-23. The chain fixture spans three systems.** Draft 3's suite had two; the deliverables for this
specification call for three,
so a chain crosses a system boundary twice and the unreachable hop is not adjacent to the start.
The fixture also contains a "not held" hop, so all three results occur in one walk.

**A-24. Limits and walker safety are specified.** Draft 3 had no security section. Record size, walk
bounds, path validation, redirection and credential rules (§11) are added because a walker follows
locations taken from other parties' records.

**A-25. The versions listing is in recording order, not "supersession order".** Supersession can
branch (two successors of one version), can cross ids and systems (A-9), and is stated only by
successors; a single system-local list cannot be in supersession order in general. Recording order
is a fact every system has.

**A-26. "Unauthenticated by default" is dropped.** Draft 3 made unauthenticated access the
default and authentication an option. A protocol that names a default invites readers to treat a
refusal as an anomaly; here the protocol takes no position (§6.5), and a refusal is an ordinary
answer (§11.1). Most internal systems will require authentication, and nothing changes for those
that do not.

**A-27. `attributedTo` is optional and may name an organisation.** Draft 3 said that where the agent
is a machine, `attributedTo` "names the human responsible", which reads as required. It is
optional here (§3.4), because many systems do not know the responsible person for an automated act
and a mandatory field would be filled with a placeholder, which is worse than absence; and it may
name an organisation (a team, a role), because that is often the honest answer.

**A-28. `at` excludes leap seconds and lower-case `t`/`z`.** RFC 3339 admits both. Leap-second
validity depends on a published table that a reader would have to carry and update, and lower-case
separators double the forms two implementations must agree on. Neither is needed to record when a
decision was made.

**A-29. The hash law is the function; input checking is the parser's.** Draft 3 called the
canonical form "one function". Here the function (§5.2–5.3) is separated from the input rules
(§5.1), so it is plain that in JavaScript and Go the input rules need more than the standard parser
(§5.1). The budget of constraint 6 is stated as the size of the reference implementation (§5.4,
A.3); the suite's JavaScript and Go programs are hash-only cross-checks.

### A.2 The five questions

**Q1. Must `by` be present when a system decides without a human?** Yes — the proposal is
adopted. `by` is required in every record and, for an automated decision, is the identity of the
software that acted (`spiffe://example.internal/pricing-engine`). `attributedTo` names the person or
organisation responsible where it is known. Putting a person in `by` who did not act would make
the record false; leaving `by` empty would make an automated decision unattributable. Absent
`attributedTo` states that the system did not record a responsible party, nothing more.

**Q2. Is `supersedes` enough, or is `supersededBy` needed?** `supersedes` is enough — the proposal is
adopted. A forward link can only be added by rewriting the earlier record, which breaks
immutability (§3.8) and every pin on it, or by keeping an index of successors across systems,
which is a central point (constraint 1). Within one system, the optional versions listing (§6.4) is
the forward view; across systems, a successor is found only by walking from it. This
specification states the limit rather than hiding it: a reader holding an old record cannot learn
from the protocol that another system has superseded it.

**Q3. Is `status` useful, or does it invite systems to encode force?** Kept, as an optional member
with Draft 3's four values (`proposed`, `accepted`, `superseded`, `withdrawn`). It is useful because
nearly every source system already has the field (ADRs, tickets), and a walk that cannot show it
loses information people look for. The risk is real, so §3.4 states it plainly: a value means what
the writing system says it means, in its profile; the protocol attaches no force to it; a reader
must not infer any. `status` is hashed, so a change of status is a new version, which is the
honest record of it. Readers tolerate other values so that a later minor version could add one.

**Q4. Does the well-known path collide with anything at IANA; should the protocol register one?**
Checked against the IANA Well-Known URIs registry on 2026-10-27: no entry named
`decision-provenance`, `decisions` or `dpp`, and no collision. Draft 3's `decisions` is free today
but generic enough to be wanted by an unrelated protocol; `dpp` is already the common abbreviation
of at least two unrelated efforts (the Wi-Fi Easy Connect "Device Provisioning Protocol" and the
EU Digital Product Passport) and is a poor registry name. The suffix is therefore
`decision-provenance`. The protocol should register it, provisionally now and permanently when the
specification is final (§13): registration only reserves the name; nothing at runtime consults it,
so it is consistent with constraint 1.

**Q5. Name and version prefix.** The name is **Decision Provenance Protocol**; the token is
**`dpp/1`**, carried in `protocol`, both kept from Draft 3. A token in a named field cannot collide
with anything in practice, so the abbreviation's other meanings (Q4) do not matter there; they
matter only where names are shared, which is why the well-known suffix is spelled out. The token
carries the major version only (§12): every `1.x` record says `dpp/1`, because minor versions never
change the hash.

### A.3 Open items

Flagged for review; none is asserted as settled.

- **Who controls the specification.** §13 needs a named change controller for the IANA
  registration, and §12 needs a named party that issues minor versions. Neither is decided.
  *(UNVERIFIED — Emil review.)*
- **A-2 is a reversal of Draft 3's central choice.** Versions are system-chosen and the pin is
  required, so Draft 3's integrity properties are kept; the remaining cost is one hash computation
  per reference, by its writer. That the reversal stands is a principal's call. *(UNVERIFIED —
  Emil review.)*
- **Constraint 6 is stated as reference-implementation size.** "Implementable in under fifty
  lines in any language" is restated, in this revision, as: the hash law in the reference
  implementation, input checks included, is under fifty lines (30), and the whole reference
  implementation is under a hundred (99) (§5.4). No claim is made about other languages. The
  suite's JavaScript and Go programs are hash-only: they implement §5.2–5.3 and rely on standard
  parsers that do not perform §5.1's checks.
- **`status` value set.** Draft 3's four values are kept. Nygard's ADR form uses `deprecated` where
  this has `withdrawn`; an ADR directory maps it in its profile. Whether to add `rejected` (common
  in ticket systems) in a minor version is open.

---

## Appendix B. Example profile (non-normative)

This appendix shows what a profile looks like, using the governance engine of Draft 3 Part 2. It
is one system's design, adds nothing to the protocol, and is not required of anyone.

A governance engine that distinguishes deciding from accepting, and makes force depend on
acceptance, might publish a profile stating:

1. **Records.** Every decision, grant and acceptance in its log is a `dpp/1` record. `at` is the
   time its own log assigned. `by` is the authenticated identity that committed it; machine
   identities appear as `by` with the responsible person in `attributedTo`.
2. **Acceptance is a record.** An acceptance of decision `D@v` is a separate record whose
   `basedOn` contains `D@v` (pinned) and the grant under which it was made, and whose
   `statement` says what was accepted. A walk therefore shows who accepted and under what grant,
   using only the protocol.
3. **`status`.** `accepted` means "accepted under a grant, in this system's log, at the version's
   position". `superseded` means a later version in this log replaced it.
4. **Force is local.** A `basedOn` reference into another system carries provenance and never
   force. A decision here that rests on a ticket in another system is in force only under an
   acceptance in this system. The protocol does not say this; this profile does.
5. **Dotted members.** `com.example.engine.predicate` holds an evaluable rule as a string and
   `com.example.engine.level` its level as a decimal string, both pinned. `extensions` holds log
   positions and session identifiers, which change nothing about the decision.
6. **What other systems see.** Everything above is readable by any `dpp/1` reader as records and
   references. Nothing in it is required of, or checked for, any other system.

---

## Appendix C. Conformance suite

The suite accompanies this specification and is versioned with it. It has no network dependency
and no required implementation language.

| Part | Content |
|---|---|
| `suite/canonical/vectors.json` | 36 vectors. **parse** vectors (8): inputs that are not I-JSON and must be rejected before hashing — duplicate member names (top level and inside `extensions`), unpaired surrogate, noncharacter, `NaN`, top-level array, byte order mark, invalid UTF-8. **hash** vectors (28): canonical form and hash, or rejection, covering key order, input escapes, NFC versus NFD, the escape table including U+007F and U+2028, code point versus UTF-16 key order, integer-like member names, numbers of any magnitude inside `extensions`, numbers (integer, decimal, exponent, nested, as string), booleans and null, `extensions` and `signature` excluded, `basedOn` order across systems, duplicate refs, entries without `ref`, `supersedes` order, other arrays not reordered, unknown members hashed. |
| `suite/resolver/` | A file-based resolver fixture: a conformant system directory with held, superseding and listed records and with records that are invalid, mismatched, of another major version, not JSON, or unhashable; a directory without a descriptor; a directory whose descriptor names another system. `cases.json` gives 20 resolutions and their expected results, including a pin that matches despite changed `extensions`, a pin mismatch, a record with an unpinned reference, a version token that collides with nothing (`system`), a `why` with an empty `ref`, a date that is not a calendar date, and a descriptor whose optional members are malformed. |
| `suite/chain/` | Three systems — a ticket tracker, an ADR directory, a governance engine — of which the reader can reach two. Starting from `PAY-142@3` in the tracker, the expected walk (`expected-walk.json`) has five hops: three held (one an origin), one not held (a version the ADR directory does not have, signalled as in §6.9), one not reachable (the governance engine). Every reference in it is pinned, including the two whose targets the walker cannot obtain. |
| `suite/run.py` | Runs all of the above against any Python module exposing `parse`, `canonical`, `record_hash`, `walk` and `Invalid`. |
| `suite/crosscheck/` | **Hash-only** cross-checks: independent implementations of §5.2–5.3 in JavaScript and Go, checked against the hash vectors. They do not implement §5.1, record validation, the resolver or the walk, are not conformant readers, and are not part of the size budget. |
| `reference/dpp.py` | The reference implementation, Python, standard library only, and the measure of the size budget (§5.4): hash law with input checks in 30 non-blank lines; with the file-based resolver and walk, 99 lines. |
| `example/` | The worked example: an ADR directory made conformant with no code, and a rules engine referencing one of its ADRs. |
