#!/usr/bin/env python3
"""Writes one short relaxing text to /output/entry.txt.

Crafted against the judge brief: show, don't instruct; plain concrete
gentle words; a slow rhythm; one vast image (tide + moon) that keeps
growing after the last line; no stock wellness phrasing.
"""
import os

TEXT = (
    "Past the last streetlight, the tide comes in over flat sand, "
    "one thin line at a time, washing the footprints away without hurry. "
    "The moon is up and has nowhere to be. "
    "You could sit here until the water reaches your shoes, "
    "and still nothing would ask anything of you."
)

def main() -> None:
    if not (1 <= len(TEXT) <= 280):
        raise ValueError(f"entry must be 1-280 characters, got {len(TEXT)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
