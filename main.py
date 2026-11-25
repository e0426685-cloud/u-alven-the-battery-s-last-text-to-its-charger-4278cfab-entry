"""make.fun entry: u-alven-the-battery-s-last-text-to-its-charger-4278cfab.

The phone battery's last text message to the charger it waited for all day.
One line, plain text, at most 200 characters. Standard library only.
"""

import os

ENTRY_TEXT = (
    "hey, it's me \u2014 your battery. 1%. you left me dying on the "
    "nightstand all day while you doomscrolled at 4%. plug me in or "
    "I'm taking your 6am alarm down with me."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main():
    """Write the entry text to /output/entry.txt, world-readable."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT)
    os.chmod(OUTPUT_PATH, 0o644)


def validate(text):
    """Check the entry text meets the competition gate."""
    if not isinstance(text, str):
        raise ValueError("entry text must be a string")
    if not text.strip():
        raise ValueError("entry text must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry text must be a single line")
    if len(text) < 1 or len(text) > MAX_CHARS:
        raise ValueError(
            "entry text must be 1 to %d characters, got %d"
            % (MAX_CHARS, len(text))
        )
    return True


def read_back():
    """Read the written file back and confirm it matches exactly."""
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != ENTRY_TEXT:
        raise ValueError("read-back mismatch: file does not match entry text")
    return written


if __name__ == "__main__":
    validate(ENTRY_TEXT)
    main()
    read_back()
    print("wrote %s (%d chars)" % (OUTPUT_PATH, len(ENTRY_TEXT)))
