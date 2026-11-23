#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses — entry program.

Reads the excuse line from entry.txt beside this script and copies it
to the gate's output file (/output/entry.txt under the grader).
Deterministic: the output bytes are identical on every run.
"""
import os


def source_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")


def output_path():
    full_path = os.environ.get("ENTRY_OUTPUT")
    if full_path:
        return full_path
    out_dir = os.environ.get("OUTPUT_DIR") or os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return os.path.join(out_dir, "entry.txt")
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")


def checked_text(text):
    # The gate accepts one line of 1-200 characters, not only white space.
    stripped = text.strip()
    if not stripped or len(stripped) > 200 or "\n" in stripped:
        raise ValueError("entry.txt must hold exactly one line of 1-200 characters")
    return text


def main():
    with open(source_path(), "r", encoding="utf-8") as f:
        text = checked_text(f.read())
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
