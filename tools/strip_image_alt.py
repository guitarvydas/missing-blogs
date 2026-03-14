#!/usr/bin/env python3
"""
strip_image_alt.py — Remove alt text from markdown image inclusions.

Transforms:  ![some caption](url)
Into:        ![](url)

Processes every .md file in the current directory (non-recursive).
Files are only written if changes are actually made.

Usage:
    python3 strip_image_alt.py           # apply changes
    python3 strip_image_alt.py --dry-run # preview without writing
"""

import re
import sys
import argparse
from pathlib import Path

IMAGE_RE = re.compile(r'!\[([^\]]*)\](\([^)]*\))')


def strip_alt(text):
    """Replace ![any text](url) with ![](url). Returns (new_text, count)."""
    count = 0
    def _replace(m):
        nonlocal count
        if m.group(1):   # only count/replace if there was actual alt text
            count += 1
        return f'![]{m.group(2)}'
    return IMAGE_RE.sub(_replace, text), count


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                  formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--dry-run', action='store_true',
                    help='Show what would change without writing files')
    args = ap.parse_args()

    md_files = sorted(Path('.').glob('*.md'))
    if not md_files:
        print("No .md files found in current directory.")
        return

    total_files  = 0
    total_images = 0

    for path in md_files:
        original = path.read_text(encoding='utf-8', errors='ignore')
        updated, count = strip_alt(original)

        if count == 0:
            continue

        total_files  += 1
        total_images += count

        if args.dry_run:
            print(f"[dry-run] {path}  ({count} image(s) would be updated)")
        else:
            path.write_text(updated, encoding='utf-8')
            print(f"  updated  {path}  ({count} image(s))")

    if total_files == 0:
        print("No image alt text found — nothing to do.")
    else:
        verb = "would update" if args.dry_run else "updated"
        print(f"\n{verb} {total_images} image(s) across {total_files} file(s).")


if __name__ == '__main__':
    main()
