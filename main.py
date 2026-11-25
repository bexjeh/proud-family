"""Write one short family scene to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only. Deterministic: the same scene, byte for byte, every run.
"""

import os

SCENE = (
    "Dad dozed off mid-story with the book sliding off his chest, so the "
    "kids tucked him in instead \u2014 blanket to his chin, a kiss on his "
    "forehead, and a whispered \u2018sleep tight, old man.\u2019"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(SCENE + "\n")


if __name__ == "__main__":
    main()
