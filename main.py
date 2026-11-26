"""The Best Meal You Ever Had — make.fun entry.

Writes one sentence to entry.txt in the output directory: the best
meal the entrant ever had. Stdlib only, no network, deterministic.
"""

import os

LINE = "The best meal I ever had was my sister's lontong sayur from a plastic bag in a hospital corridor at 2am, coconut broth soaking the rice cake while we waited to hear if our father would wake."

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or (
    "/output" if os.path.isdir("/output") else "output"
)


def validate(text: str) -> None:
    """Raise ValueError unless text is one non-empty sentence of <=200 chars."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty")
    if len(text) > 200:
        raise ValueError("entry must be at most 200 characters")
    if "\n" in text:
        raise ValueError("entry must be one line")
    if not text.endswith(".") or text.count(".") != 1:
        raise ValueError("entry must be exactly one sentence ending with '.'")


def main() -> None:
    validate(LINE)
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, "entry.txt")
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.replace(tmp, path)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("entry.txt differs from LINE after write")
    validate(written)


if __name__ == "__main__":
    main()
