#!/usr/bin/env python3
"""Check that local Markdown links and image targets resolve in this repository."""

from __future__ import annotations

import json
import re
import sys

from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", ".codex", "graphify-out", ".venv", "__pycache__"}
LINK_RE = re.compile(r"(?P<image>!)?\[(?P<label>[^\]]*)\]\((?P<target><[^>]*>|[^)\n]*)\)")
HTML_IMAGE_RE = re.compile(
    r"<img\b[^>]*\bsrc\s*=\s*([\"'])(?P<target>.*?)\1",
    re.IGNORECASE,
)
WINDOWS_PATH_RE = re.compile(r"^[A-Za-z]:[\\/]")


def markdown_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if not any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts)
    )


def notebook_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.ipynb")
        if not any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts)
    )


def local_target(source: Path, raw_target: str) -> Path | None:
    target = raw_target.strip()
    angle_target = target.startswith("<") and target.endswith(">")
    if angle_target:
        target = target[1:-1]
    else:
        target = target.split("\t", 1)[0].split(" ", 1)[0]
    target = unquote(target)
    if not target or target.startswith(("#", "//")):
        return None
    if WINDOWS_PATH_RE.match(target):
        return ROOT / "__non_portable__" / target

    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc:
        return None
    target = parsed.path
    if not target:
        return None
    if target.startswith("/"):
        return ROOT / target.lstrip("/")
    return (source.parent / target).resolve()


def check_file(path: Path) -> list[tuple[int, str]]:
    issues: list[tuple[int, str]] = []
    in_fence = False
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    for line_number, line in enumerate(lines, 1):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for match in LINK_RE.finditer(line):
            label = match.group("label").strip().lower()
            if label.startswith("mathjax"):
                continue
            target = local_target(path, match.group("target"))
            if target is not None and not target.exists():
                issues.append((line_number, match.group("target")))
        for match in HTML_IMAGE_RE.finditer(line):
            target = local_target(path, match.group("target"))
            if target is not None and not target.exists():
                issues.append((line_number, match.group("target")))
    return issues


def check_notebook(path: Path) -> list[tuple[int, str]]:
    try:
        notebook = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        return [(1, f"invalid JSON: {error.msg}")]

    issues: list[tuple[int, str]] = []
    for cell in notebook.get("cells", []):
        source = "".join(cell.get("source", []))
        if cell.get("cell_type") == "markdown" and "[mathjax" in source:
            issues.append((1, "unsupported exported MathJax tag in Markdown cell"))
        if cell.get("cell_type") != "code":
            continue
        for line_number, line in enumerate(source.splitlines(), 1):
            if WINDOWS_PATH_RE.match(line.strip()) or "/Users/" in line or "/home/" in line:
                issues.append((line_number, "non-portable absolute path in code cell"))
    return issues


def main() -> int:
    issues: list[tuple[Path, int, str]] = []
    for path in markdown_files():
        issues.extend((path, line, target) for line, target in check_file(path))
    for path in notebook_files():
        issues.extend((path, line, target) for line, target in check_notebook(path))

    if issues:
        print(f"content check: {len(issues)} unresolved local target(s)")
        for path, line, target in issues:
            print(f"{path.relative_to(ROOT)}:{line}: {target}")
        return 1

    print(
        f"content check: ok ({len(markdown_files())} Markdown files and "
        f"{len(notebook_files())} notebooks scanned)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
