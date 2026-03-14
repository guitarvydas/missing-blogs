#!/usr/bin/env python3
"""
escape_image_paths.py — Replace spaces with %20 in markdown image URLs.

Transforms:  ![](my image file.png)
Into:        ![](my%20image%20file.png)

Also handles alt text:  ![some caption](my file.png)
Becomes:                 ![some caption](my%20file.png)

Processes every .md file in the current directory (non-recursive).
Files are only written if changes are actually made.

Usage:
    python3 escape_image_paths.py           # apply changes
    python3 escape_image_paths.py --dry-run # preview without writing
"""

import re
import argparse
from pathlib import Path

# Matches ![alt](path) — captures alt and path separately
IMAGE_RE = re.compile(r'(!\[[^\]]*\]\()([^)]*?)(\))')


def escape_spaces(text):
    """Replace spaces with %20 inside image URL parens. Returns (new_text, count)."""
    count = 0

    def _replace(m):
        nonlocal count
        prefix, url, suffix = m.group(1), m.group(2), m.group(3)
        if ' ' in url:
            count += 1
            url = url.replace(' ', '%20')
        return f'{prefix}{url}{suffix}'

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
        updated, count = escape_spaces(original)

        if count == 0:
            continue

        total_files  += 1
        total_images += count

        if args.dry_run:
            # Show the affected lines
            for i, (orig_line, new_line) in enumerate(
                    zip(original.splitlines(), updated.splitlines()), 1):
                if orig_line != new_line:
                    print(f"  {path}:{i}")
                    print(f"    - {orig_line.strip()}")
                    print(f"    + {new_line.strip()}")
        else:
            path.write_text(updated, encoding='utf-8')
            print(f"  updated  {path}  ({count} path(s) escaped)")

    if total_files == 0:
        print("No image paths with spaces found — nothing to do.")
    else:
        verb = "would update" if args.dry_run else "updated"
        print(f"\n{verb} {total_images} image path(s) across {total_files} file(s).")


if __name__ == '__main__':
    main()
