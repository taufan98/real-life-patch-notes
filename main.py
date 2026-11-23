# Real-Life Patch Notes — writes one funny patch note to /output/entry.txt.
# Python 3.13, standard library only, no network, no secrets.

import os
from pathlib import Path

LINE = (
    "v2.4.1: fixed a bug where the brain replayed your most embarrassing "
    "moment from 2009 every time you tried to fall asleep."
)

# The gate requires 1-160 characters of non-whitespace UTF-8 text,
# a single line, and the entry must stand alone as one patch note.
# A release note ends on a full stop and carries no trailing space.
if not 1 <= len(LINE.strip()) <= 160:
    raise SystemExit(f"entry line must be 1-160 characters, got {len(LINE)}")
if LINE != LINE.strip() or LINE.count("\n") != 0:
    raise SystemExit("entry line must be a single line with no stray whitespace")
if not LINE.endswith("."):
    raise SystemExit("entry line must end with a full stop")

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")
print(f"Wrote {len(LINE)} characters to {out_dir / 'entry.txt'}")
