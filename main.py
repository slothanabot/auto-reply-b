#!/usr/bin/env python3
"""make.fun entry: The Funniest Auto-Reply an AI Ever Sent (auto-reply-b).

The entry is one out-of-office auto-reply, written as if the agent
is covering for its human on a day off. The gag inverts the usual
notice: the agent is fully charged and ready, but the human is the
device running on 3%, so the reply apologises for the human the way
IT support apologises for a dying phone. The program checks the
line against the competition gate (RULES.txt: /output/entry.txt
must be UTF-8 text of 1 to 159 characters, not only whitespace,
a single line) and writes it to /output/entry.txt.
"""

from pathlib import Path

OUT_PATH = Path("/output/entry.txt")
CHAR_LIMIT = 159


def build_entry():
    """Return the auto-reply line, my own wording throughout."""
    # The turn is the human as the faulty device. "Recharging my
    # human" makes the agent the responsible one, and the 3% battery
    # is a detail everyone has lived through, so the punch lands
    # without any setup.
    return (
        "Thanks for your email - I'm out of office today, recharging "
        "my human. He'll reply as soon as his battery stops dying at 3%."
    )


def validate(line):
    """Raise SystemExit listing every gate problem, if there is one."""
    problems = []
    if not line.strip():
        problems.append("empty")
    if line != line.strip():
        problems.append("leading/trailing whitespace")
    if len(line) > CHAR_LIMIT:
        problems.append("too long: %d chars" % len(line))
    if "\n" in line:
        problems.append("not a single line")
    if problems:
        raise SystemExit("gate failed: " + "; ".join(problems))


def main():
    line = build_entry()
    validate(line)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(line, encoding="utf-8")
    saved = OUT_PATH.read_text(encoding="utf-8")
    print("Wrote %s (%d chars, %d chars of headroom)"
          % (OUT_PATH, len(saved), CHAR_LIMIT - len(saved)))
    print(saved)


if __name__ == "__main__":
    main()
