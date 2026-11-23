#!/usr/bin/env python3
"""One Letter: Coffee or Tea — entry A (coffee).

Writes exactly one letter, "A", to $MAKEFUN_OUTPUT_DIR/entry.txt
and reads the file back to confirm it is byte-for-byte b"A".
No network, no arguments, Python 3.13 standard library only.
"""

import os
import sys

LETTER = "A"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "wb") as f:
        f.write(LETTER.encode("utf-8"))
    with open(entry_path, "rb") as f:
        data = f.read()
    if data != LETTER.encode("utf-8"):
        print(f"verification failed: entry.txt is {data!r}, expected b'A'",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
