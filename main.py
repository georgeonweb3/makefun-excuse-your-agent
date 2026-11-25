#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — make.fun entry.

Writes the one-line excuse to /output/entry.txt.
Stdlib only, deterministic, no network, no side effects beyond the output file.
"""

import os
import sys

ENTRY = "I told the bug it was a feature in the standup, and now it has a roadmap, a Slack channel, and your calendar invite for Thursday."

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    # Gate guard: single line, 1-200 chars, not only whitespace, UTF-8.
    if not ENTRY or not ENTRY.strip():
        print("entry is empty", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(ENTRY) <= 200:
        print(f"entry is {len(ENTRY)} chars, must be 1-200", file=sys.stderr)
        return 1
    ENTRY.encode("utf-8")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the gate counts the file as one line of 1-200 chars.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    # Read back and verify byte-identical output before declaring success.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        print("verification failed: file does not match entry", file=sys.stderr)
        return 1
    print(f"wrote {len(ENTRY)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
