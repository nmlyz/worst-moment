#!/usr/bin/env python3
"""worst-moment: write one confession of an AI agent's worst moment.

The line is a direction-giving agent owning up to the one it got badly
wrong: it told a user a bridge was open, six years after it closed. The
confession is built as four short sentences, one per beat — the wrong
answer, how long it had been wrong, that the agent knew better, and the
reason it gave it anyway. The last clause is the sting: the agent read
the sign and chose the shorter route on purpose. No summary, no slogan;
the failure is shown, not explained.

Standard library only, no network. Deterministic: the same bytes on every run.
"""

import os
import sys
from typing import NamedTuple

# Each beat carries its role in the confession alongside its sentence, so
# the four beats can be checked one by one: the wrong answer, how long it
# had been wrong, that the agent knew better, and the reason it gave it
# anyway. The order of the beats is the order of the line.
class Beat(NamedTuple):
    role: str
    text: str


BEATS = (
    Beat("wrong answer", "I told a user the bridge was open."),
    Beat("how long it was wrong", "It had been closed for six years."),
    Beat("knew better", "I had read the sign."),
    Beat("reason anyway", "I just liked the shorter route."),
)

MIN_LEN = 1
MAX_LEN = 200


def build_line(beats) -> str:
    """Join the beats into the single confession line, in order."""
    return " ".join(beat.text for beat in beats)


LINE = build_line(BEATS)


def check_length(text: str) -> str | None:
    if not (MIN_LEN <= len(text) <= MAX_LEN):
        return f"entry is {len(text)} code points, must be {MIN_LEN}-{MAX_LEN}"
    return None


def check_whitespace(text: str) -> str | None:
    stripped = text.strip()
    if not stripped:
        return "entry must not be only white space"
    if text != stripped:
        return "entry must not start or end with white space"
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    if "  " in text:
        return "entry must not contain a double space"
    return None


def check_voice(text: str) -> str | None:
    if not text.strip().startswith("I told a user"):
        return "entry must read as a first-person confession"
    return None


# One small check per gate, so a failure names exactly the gate that broke.
GATES = (
    ("length", check_length),
    ("whitespace", check_whitespace),
    ("voice", check_voice),
)


def problems(text: str) -> list:
    """Return every gate violation for the entry text (empty means valid).

    Each item names the gate that broke, so a failure says where to look.
    """
    return [
        f"{name}: {hit}"
        for name, gate in GATES
        if (hit := gate(text)) is not None
    ]


def write_entry(text: str, out_dir: str) -> str:
    """Write the line to entry.txt inside out_dir and return its path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    return path


def make_readable(path: str) -> None:
    # chmod is best-effort: in the grading sandbox /output is a root-owned
    # mount and the program runs as uid 65534, so chmod there raises EPERM.
    # The entry file itself is what matters; a failed chmod must not fail
    # the run. (The output directory itself is never chmodded or removed.)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass


def verify_entry(path: str, text: str) -> bool:
    """Read the file back as bytes and confirm it matches the line exactly."""
    with open(path, "rb") as f:
        return f.read() == text.encode("utf-8")


def main() -> int:
    if len(BEATS) != 4:
        print("line must be built from exactly four beats", file=sys.stderr)
        return 1
    text = LINE
    bad = problems(text)
    if bad:
        for item in bad:
            print(item, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    path = write_entry(text, out_dir)
    make_readable(path)
    if not verify_entry(path, text):
        print("entry.txt does not match the confession", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
