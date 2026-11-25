"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Writes one commit message — the note an AI agent leaves after a long night
fixing its own bugs — to /output/entry.txt (or $MAKEFUN_OUTPUT when set).

Stdlib only. Deterministic: the text is a constant, no clock, no randomness,
no network, no model call.
"""

import os

ENTRY_TEXT = (
    "fix: after 47 attempts I found the bug. it was mine, written at 21:04 "
    "and defended it until 04:00. I have apologized to myself in the comments."
)

DEFAULT_OUTPUT = "/output/entry.txt"


def main() -> None:
    output = os.environ.get("MAKEFUN_OUTPUT") or DEFAULT_OUTPUT
    parent = os.path.dirname(output)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
