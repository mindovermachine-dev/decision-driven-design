"""Mint What element keys: ULIDs (DDD-dec-63, ruled 2026-10-28).

    python3 applications/sdlc/what/mint.py [n]

A key is minted once, when its element is created, and is never changed or reused. Nothing in it
carries meaning: the 48-bit time prefix only orders keys minted by one writer, and is not read by
anything in the framework. The human name of an element is its rdfs:label.
"""
import os, sys, time

ALPHABET = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"   # Crockford base32

def ulid(ms=None):
    n = ((int(time.time() * 1000) if ms is None else ms) << 80) | int.from_bytes(os.urandom(10), "big")
    return "".join(ALPHABET[(n >> (5 * i)) & 31] for i in range(25, -1, -1))

if __name__ == "__main__":
    for _ in range(int(sys.argv[1]) if len(sys.argv) > 1 else 1):
        print(ulid())
