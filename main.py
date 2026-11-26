#!/usr/bin/env python3
"""The Funniest Office Joke, Judged Head to Head.

Writes one single-line joke about office life to /output/entry.txt.
The joke needs a setup and a turn, built on something anyone who has
worked in an office recognises, with the punchline last.
"""

import os

JOKE = "I told the new hire the office printer is haunted, and now IT gets half the tickets and I get twice the respect."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
