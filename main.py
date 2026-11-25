#!/usr/bin/env python3
"""Invent a Word We Need — a make.fun bounty entry.

The program writes a single invented English word together with its
one-line definition to /output/entry.txt. The whole entry is one line of
at most 140 characters, so the word and the definition have to do all the
work by themselves: no examples, no second sentence, no explaining after.

The word: tabnesia. The gap it fills is the one everybody knows and nobody
has named — opening a fresh browser tab and, before the page has even
loaded, forgetting entirely why you opened it. It is built the way English
actually grows new words, by welding two familiar parts together: tab +
amnesia. Sayable in one breath, spellable on first hearing, and memorable
because the reader has lived it a dozen times today already.
"""

import os

ENTRY = (
    "tabnesia \u2014 the act of opening a new tab and instantly "
    "forgetting why you opened it."
)


def main() -> None:
    # The sealed scorer only accepts UTF-8 text of 1 to 140 characters,
    # so refuse to write anything that would fail the gate instead of
    # producing an entry the judge will never see.
    if not 1 <= len(ENTRY) <= 140 or not ENTRY.strip():
        raise SystemExit("entry does not fit the 1-140 character gate")
    if ENTRY.count("\n"):
        raise SystemExit("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
