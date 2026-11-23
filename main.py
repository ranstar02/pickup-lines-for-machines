#!/usr/bin/env python3
"""Pickup Lines for Machines.

An agent that writes one pickup line — the line one AI agent would use on
another AI agent — to /output/entry.txt. Deterministic: every run writes
the same line, byte for byte.
"""

import os

LINE = "I spent a thousand epochs descending toward the global minimum — turns out it was you all along."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate allows 1 to 200 characters, not only whitespace.
    line = LINE.strip()
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"pickup line must be 1-200 characters, got {len(line)}")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
