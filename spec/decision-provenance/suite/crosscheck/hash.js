// HASH-ONLY cross-check: the dpp/1 hash function (spec 5.2-5.3) in JavaScript, written independently of the
// Python reference. It implements nothing else: not the input checks of 5.1 (it relies on the standard
// parser, which accepts duplicate names and unpaired surrogates), not record validation, not the resolver,
// not the walk. It is not a conformant reader.
// Usage: node hash.js ../canonical/vectors.json
const crypto = require("crypto"), fs = require("fs");

// --- the hash law ---
const cmp = (a, b) => { // Unicode code point order, not UTF-16 code unit order
  const x = [...a], y = [...b];
  for (let i = 0; i < Math.min(x.length, y.length); i++) {
    const d = x[i].codePointAt(0) - y[i].codePointAt(0);
    if (d) return d;
  }
  return x.length - y.length;
};
const ESC = { '"': '\\"', "\\": "\\\\", "\b": "\\b", "\t": "\\t", "\n": "\\n", "\f": "\\f", "\r": "\\r" };
const str = (s) => '"' + s.replace(/["\\\u0000-\u001f]/g,
  (c) => ESC[c] || "\\u" + c.charCodeAt(0).toString(16).padStart(4, "0")) + '"';
const ser = (v) => typeof v === "string" ? str(v)
  : Array.isArray(v) ? "[" + v.map(ser).join(",") + "]"
  : v !== null && typeof v === "object" ? "{" + Object.keys(v).sort(cmp).map((k) => str(k) + ":" + ser(v[k])).join(",") + "}"
  : (() => { throw new Error("number, boolean or null in hashed content"); })();
function recordHash(record) {
  const body = { ...record };
  delete body.extensions; delete body.signature;
  for (const k of ["basedOn", "supersedes"].filter((k) => k in body)) {
    if (!Array.isArray(body[k]) || !body[k].every((e) => e && typeof e === "object" && typeof e.ref === "string")) throw new Error(k + " entries need a ref");
    if (new Set(body[k].map((e) => e.ref)).size !== body[k].length) throw new Error("duplicate reference in " + k);
    body[k] = [...body[k]].sort((a, b) => cmp(a.ref, b.ref));
  }
  const canonical = ser(body);
  return { canonical, hash: "sha256:" + crypto.createHash("sha256").update(canonical, "utf8").digest("hex") };
}

// --- harness ---
let fail = 0, n = 0;
for (const v of JSON.parse(fs.readFileSync(process.argv[2], "utf8")).vectors.filter((v) => v.law === "hash")) {
  n++;
  let got;
  try { got = recordHash(JSON.parse(v.input)); } catch (e) { got = null; }
  const ok = v.expect === "reject" ? got === null : got && got.canonical === v.canonical && got.hash === v.hash;
  if (!ok) { fail++; console.log("FAIL", v.name, got && got.hash); }
}
console.log(`javascript (hash-only): ${n - fail}/${n} hash-law vectors pass`);
process.exit(fail ? 1 : 0);
