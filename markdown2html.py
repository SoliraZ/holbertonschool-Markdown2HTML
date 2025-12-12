#!/usr/bin/python3
"""Minimal Markdown to HTML converter entrypoint."""

import os
import sys


def main():
    """Validate arguments and prepare output file."""
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    md_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(md_file):
        print(f"Missing {md_file}", file=sys.stderr)
        sys.exit(1)

    with open(md_file, "r", encoding="utf-8") as f_md:
        content = f_md.read()

    with open(output_file, "w", encoding="utf-8") as f_out:
        f_out.write(content)

    sys.exit(0)


if __name__ == "__main__":
    main()
