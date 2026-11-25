"""The Best Meal You Ever Had — make.fun entry.

Writes one sentence to entry.txt in the output directory: the best
meal the entrant ever had. Stdlib only, no network, deterministic.
"""

import os

LINE = "The best meal I ever had was my sister's lontong sayur from a plastic bag in a hospital corridor at 2am, coconut broth soaking the rice cake while we waited to hear if our father would wake."

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or (
    "/output" if os.path.isdir("/output") else "output"
)


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, "entry.txt")
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.replace(tmp, path)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "entry.txt differs from LINE"
    assert 1 <= len(written) <= 200 and written.strip(), "gate failed"
    assert "\n" not in written, "entry must be one line"
    assert written.count(".") == 1 and written.endswith("."), "must be one sentence"


if __name__ == "__main__":
    main()
