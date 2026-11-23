#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog (make.fun).

Writes a single one-line software patch note for a bug in human
biology to /output/entry.txt. The entry is fixed and deterministic:
the same line on every run, 149 characters, well under the 160
character cap.

The bug: the earworm. Hear a song once and the brain replays the
same 8-second clip on loop for three days. The shipped "fix" is a
skip button that does nothing -- the dry engineering punchline.
The gate counts the file's characters, so the entry is written with
no trailing newline: exactly 149 characters, one line.
"""

import os

# The entry: one line, 149 characters, no trailing newline.
ENTRY = (
    "v1.4.7: Fixed a bug where the brain replayed the same 8-second "
    "song clip on loop for 72 hours after one listen. "
    "Added a skip button; it does nothing."
)

MAX_CHARS = 160


def main() -> None:
    if not (1 <= len(ENTRY) <= MAX_CHARS):
        raise ValueError(
            "entry must be 1-%d characters, got %d" % (MAX_CHARS, len(ENTRY))
        )
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in ENTRY:
        raise ValueError("entry must be a single line")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
