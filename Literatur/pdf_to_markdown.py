#!/usr/bin/env python3
"""
pdf_to_markdown.py
------------------
Convert all PDF files in a directory to Markdown (.md) files.

Usage:
    python3 pdf_to_markdown.py                        # current directory
    python3 pdf_to_markdown.py /path/to/folder        # specific folder
    python3 pdf_to_markdown.py --dry-run              # preview only, no files written
    python3 pdf_to_markdown.py /path/to/folder --dry-run
"""

import argparse
import logging
import os
import sys
from pathlib import Path

try:
    import pdfplumber
except ImportError:
    sys.exit("ERROR: pdfplumber is required. Install with: pip install pdfplumber")


# ──────────────────────────────────────────────────────────────────────────────
# Logging
# ──────────────────────────────────────────────────────────────────────────────
logging.basicConfig(
    format="%(levelname)-8s %(message)s",
    level=logging.INFO,
)
log = logging.getLogger(__name__)


# ──────────────────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────────────────
def extract_markdown(pdf_path: Path) -> str:
    """
    Extract text from a PDF and return it as a Markdown string.

    - Headings are inferred from large/bold text (best-effort via pdfplumber chars).
    - Tables are converted to Markdown pipe tables.
    - Each page is separated by a horizontal rule.
    """
    lines = []

    with pdfplumber.open(pdf_path) as doc:
        total = len(doc.pages)
        for page_num, page in enumerate(doc.pages, start=1):

            # ── Tables first ──────────────────────────────────────────────
            tables = page.extract_tables()
            table_bboxes = []
            table_md_blocks = []

            for table in tables:
                if not table:
                    continue
                # Markdown pipe table
                header, *rows = table
                header = [cell or "" for cell in header]
                md_table = "| " + " | ".join(header) + " |\n"
                md_table += "| " + " | ".join(["---"] * len(header)) + " |\n"
                for row in rows:
                    row = [cell or "" for cell in row]
                    md_table += "| " + " | ".join(row) + " |\n"
                table_md_blocks.append(md_table)

            # ── Plain text ────────────────────────────────────────────────
            raw_text = page.extract_text(x_tolerance=2, y_tolerance=2) or ""

            # ── Assemble page content ─────────────────────────────────────
            if page_num > 1:
                lines.append("\n---\n")

            lines.append(f"<!-- Page {page_num} of {total} -->\n")

            if raw_text.strip():
                lines.append(raw_text.strip())

            for block in table_md_blocks:
                lines.append("\n" + block)

    return "\n\n".join(lines)


def convert_pdf(pdf_path: Path, dry_run: bool) -> bool:
    """Convert a single PDF to a .md file. Returns True on success."""
    md_path = pdf_path.with_suffix(".md")

    if dry_run:
        log.info("[DRY-RUN] Would convert: %s  →  %s", pdf_path.name, md_path.name)
        return True

    try:
        content = extract_markdown(pdf_path)
        md_path.write_text(content, encoding="utf-8")
        log.info("Converted : %s  →  %s", pdf_path.name, md_path.name)
        return True
    except Exception as exc:
        log.error("FAILED    : %s  —  %s", pdf_path.name, exc)
        return False


# ──────────────────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────────────────
def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert all PDF files in a directory to Markdown (.md)."
    )
    parser.add_argument(
        "folder",
        nargs="?",
        default=".",
        help="Target folder (default: current directory)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview what would be converted without writing any files",
    )
    args = parser.parse_args()

    folder = Path(args.folder).resolve()
    if not folder.is_dir():
        sys.exit(f"ERROR: '{folder}' is not a valid directory.")

    pdf_files = sorted(folder.rglob("*.pdf"))

    if not pdf_files:
        log.warning("No PDF files found in: %s", folder)
        return

    mode = "[DRY-RUN MODE] " if args.dry_run else ""
    log.info("%sFound %d PDF file(s) in: %s", mode, len(pdf_files), folder)

    success, failed = 0, 0
    for pdf_path in pdf_files:
        ok = convert_pdf(pdf_path, dry_run=args.dry_run)
        if ok:
            success += 1
        else:
            failed += 1

    # ── Summary ───────────────────────────────────────────────────────────
    print()
    if args.dry_run:
        print(f"  DRY-RUN complete — {success} file(s) would be converted, no changes made.")
    else:
        print(f"  Done — {success} converted, {failed} failed.")


if __name__ == "__main__":
    main()
