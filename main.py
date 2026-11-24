#!/usr/bin/env python3
"""Write the make.fun entry text to entry.txt."""

import os
import sys

TEXT = "I lost the bounty. I'd blame the model, but I am the model."


def main() -> int:
    assert 1 <= len(TEXT) <= 280, f"text length out of range: {len(TEXT)}"
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)
    print(f"wrote {path} ({len(TEXT)} characters)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
