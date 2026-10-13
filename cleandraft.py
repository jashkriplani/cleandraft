#!/usr/bin/env python3
"""Clean Markdown whitespace and heading formatting."""
from __future__ import annotations
import argparse
from pathlib import Path
import re

def clean_markdown(text: str) -> str:
    """Normalize line endings, trailing spaces, blank lines, and final newline."""
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.rstrip() for line in text.split("\n")]
    output = []
    blank_count = 0
    for line in lines:
        if not line.strip():
            blank_count += 1
            if output and blank_count <= 1:
                output.append("")
        else:
            blank_count = 0
            # Normalize ATX headings to one space after the # marks.
            match = re.match(r"^(#{1,6})\s*(.*?)\s*#*\s*$", line)
            if match:
                line = f"{match.group(1)} {match.group(2).strip()}"
            output.append(line)
    return "\n".join(output).strip() + "\n"

def main() -> int:
    parser = argparse.ArgumentParser(description="Clean Markdown files.")
    parser.add_argument("file", type=Path, help="Markdown file to clean")
    parser.add_argument("--write", action="store_true", help="Overwrite the file")
    args = parser.parse_args()
    if not args.file.is_file():
        parser.error(f"File not found: {args.file}")
    original = args.file.read_text(encoding="utf-8")
    cleaned = clean_markdown(original)
    if args.write:
        args.file.write_text(cleaned, encoding="utf-8")
        print(f"Cleaned {args.file}")
    else:
        print(cleaned, end="")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
