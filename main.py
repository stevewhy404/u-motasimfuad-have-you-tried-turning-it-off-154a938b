#!/usr/bin/env python3
"""Have You Tried Turning It Off? — one funny line from a hopeless tech
support agent to a desperate customer. Writes entry.txt deterministically."""

import os

LINE = (
    "Have you tried turning it off and on again? Take your time — I'll hold "
    "the line until your deadline quietly turns itself off first."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
