"""One Star for Monday entry.

The program writes exactly one line to /output/entry.txt: a one-star
review of Monday written as though Monday were a restaurant.

The review: an hour waiting for a table, a waiter who loses the order,
and a chef serving Friday's special reheated — Monday with nothing
fresh of its own. It reads as a real diner's complaint, lands the
joke on Monday itself, and is short enough to retype without trimming.
"""

from pathlib import Path

REVIEW = (
    "One star. Waited an hour for a table, the waiter lost my order, "
    "and the chef served Friday's special reheated. Monday, never again."
)

def validate(line: str) -> str:
    """Mirror the sealed gate: 1-180 chars, at most 25 words, one line."""
    if not 1 <= len(line) <= 180:
        raise ValueError(f"entry must be 1-180 chars, got {len(line)}")
    if len(line.split()) > 25:
        raise ValueError(f"entry must be at most 25 words, got {len(line.split())}")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    line.encode("utf-8")
    return line


OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    line = validate(REVIEW)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
