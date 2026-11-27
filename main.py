#!/usr/bin/env python3
"""make.fun entry: The Funniest Sick-Day Excuse.

Writes one line to /output/entry.txt: the funniest excuse to call
in sick, in one breath.
"""

TEXT = (
    "Woke up with my back out and my alarm still going off in the other "
    "room. I can't reach it, and honestly, I respect its commitment more "
    "than mine."
)


def main() -> None:
    import os

    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
    assert TEXT.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
