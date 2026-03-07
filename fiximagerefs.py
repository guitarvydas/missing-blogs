#!/usr/bin/env python3
"""
Strips _<digits> suffixes from image file references in all .md files
in the current directory.

e.g.  diagram_42.png  ->  diagram.png
      figure_1.svg    ->  figure.svg
      photo_007.jpg   ->  photo.jpg
"""

import re
import glob
import sys

# Matches the _<digits> part immediately before a .png / .svg / .jpg extension
PATTERN = re.compile(r'(_\d+)(\.(?:png|svg|jpg))', re.IGNORECASE)

def fix_image_refs(text: str) -> tuple[str, int]:
    """Return (modified_text, number_of_substitutions_made)."""
    count = 0

    def replacer(m: re.Match) -> str:
        nonlocal count
        count += 1
        return m.group(2)           # keep only the extension, drop _<digits>

    result = PATTERN.sub(replacer, text)
    return result, count


def process_files(pattern: str = "*.md") -> None:
    md_files = sorted(glob.glob(pattern))

    if not md_files:
        print("No .md files found in the current directory.")
        return

    for path in md_files:
        try:
            original = path_read(path)
        except OSError as exc:
            print(f"  ERROR reading {path}: {exc}", file=sys.stderr)
            continue

        updated, n = fix_image_refs(original)

        if n == 0:
            print(f"  {path}: no changes")
            continue

        try:
            path_write(path, updated)
        except OSError as exc:
            print(f"  ERROR writing {path}: {exc}", file=sys.stderr)
            continue

        print(f"  {path}: {n} reference(s) updated")


def path_read(path: str) -> str:
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def path_write(path: str, text: str) -> None:
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    process_files()
