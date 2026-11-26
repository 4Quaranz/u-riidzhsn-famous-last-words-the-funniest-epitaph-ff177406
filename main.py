#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph.

Writes one original tombstone epitaph, a single line of famous last
words, to /output/entry.txt. Deterministic: the same line every run.
"""
import os

# One fixed line, no randomness and no network: the output is identical
# on every run, so the two sandbox runs match byte for byte.
ENTRY = (
    "Here lies Greg. He finally read the terms and conditions "
    "\u2014 all 47 pages \u2014 and died of old age on page three."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
