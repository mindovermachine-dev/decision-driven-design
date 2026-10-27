// dpp/1 hash law (spec section 5.2) in Go, written independently of the Python reference.
// Usage: go run hash.go ../canonical/vectors.json
package main

import (
	"crypto/sha256"
	"encoding/json"
	"errors"
	"fmt"
	"os"
	"sort"
	"strings"
)

// --- the hash law ---
var esc = func() *strings.Replacer {
	pairs := []string{`"`, `\"`, `\`, `\\`, "\b", `\b`, "\t", `\t`, "\n", `\n`, "\f", `\f`, "\r", `\r`}
	for c := rune(0); c < 0x20; c++ {
		if !strings.ContainsRune("\b\t\n\f\r", c) {
			pairs = append(pairs, string(c), fmt.Sprintf(`\u%04x`, c))
		}
	}
	return strings.NewReplacer(pairs...)
}()

func ser(v any) (string, error) {
	var parts []string
	switch t := v.(type) {
	case string:
		return `"` + esc.Replace(t) + `"`, nil
	case []any:
		for _, x := range t {
			s, err := ser(x)
			if err != nil {
				return "", err
			}
			parts = append(parts, s)
		}
		return "[" + strings.Join(parts, ",") + "]", nil
	case map[string]any:
		keys := make([]string, 0, len(t))
		for k := range t {
			keys = append(keys, k)
		}
		sort.Strings(keys) // UTF-8 byte order is code point order
		for _, k := range keys {
			s, err := ser(t[k])
			if err != nil {
				return "", err
			}
			parts = append(parts, `"`+esc.Replace(k)+`":`+s)
		}
		return "{" + strings.Join(parts, ",") + "}", nil
	}
	return "", errors.New("number, boolean or null in hashed content")
}

func recordHash(record map[string]any) (string, string, error) {
	delete(record, "extensions")
	delete(record, "signature")
	for _, k := range []string{"basedOn", "supersedes"} {
		v, present := record[k]
		list, isList := v.([]any)
		byRef := map[string]any{}
		for _, e := range list {
			m, _ := e.(map[string]any)
			ref, isStr := m["ref"].(string)
			if _, dup := byRef[ref]; !isStr || dup {
				return "", "", errors.New(k + ": entry without a string ref, or a duplicate ref")
			}
			byRef[ref] = e
		}
		if present && !isList {
			return "", "", errors.New(k + " is not an array")
		}
		sort.Slice(list, func(i, j int) bool {
			return list[i].(map[string]any)["ref"].(string) < list[j].(map[string]any)["ref"].(string)
		})
	}
	c, err := ser(record)
	return c, fmt.Sprintf("sha256:%x", sha256.Sum256([]byte(c))), err
}

// --- harness ---
func main() {
	raw, _ := os.ReadFile(os.Args[1])
	var suite struct{ Vectors []map[string]string }
	if err := json.Unmarshal(raw, &suite); err != nil {
		panic(err)
	}
	n, fail := 0, 0
	for _, v := range suite.Vectors {
		if v["law"] != "hash" {
			continue
		}
		n++
		dec := json.NewDecoder(strings.NewReader(v["input"]))
		dec.UseNumber() // a number stays a json.Number, which ser rejects
		var rec map[string]any
		canonical, hash, err := "", "", dec.Decode(&rec)
		if err == nil {
			canonical, hash, err = recordHash(rec)
		}
		ok := (v["expect"] == "reject") == (err != nil) && (err != nil || canonical == v["canonical"] && hash == v["hash"])
		if !ok {
			fail++
			fmt.Println("FAIL", v["name"], hash, err)
		}
	}
	fmt.Printf("go: %d/%d hash-law vectors pass\n", n-fail, n)
	if fail > 0 {
		os.Exit(1)
	}
}
