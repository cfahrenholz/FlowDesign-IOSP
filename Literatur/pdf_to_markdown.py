#!/usr/bin/env python3
"""
pdf_to_markdown.py
------------------
Convert all PDF files in a directory to Markdown (.md) files.

Usage:
    python3 pdf_to_markdown.py                              # current directory
    python3 pdf_to_markdown.py /path/to/folder              # specific folder
    python3 pdf_to_markdown.py --dry-run                    # preview only, no files written
    python3 pdf_to_markdown.py /path/to/folder --dry-run
    python3 pdf_to_markdown.py --images                     # also extract embedded images
    python3 pdf_to_markdown.py /path/to/folder --images --dry-run

Image filtering (optional, used together with --images):
    --min-width   Minimum image width  in pixels to extract (default: 100)
    --min-height  Minimum image height in pixels to extract (default: 100)
    --skip-top    Skip images whose top edge is within this % of page height from top    (default: 10)
    --skip-bottom Skip images whose bottom edge is within this % of page height from bottom (default: 10)

    Example — stricter filtering:
    python3 pdf_to_markdown.py . --images --min-width 200 --min-height 150 --skip-top 15 --skip-bottom 15
"""

import argparse
import logging
import sys
from pathlib import Path

try:
    import pdfplumber
except ImportError:
    sys.exit("ERROR: pdfplumber is required.  pip install pdfplumber")

try:
    import pypdf
except ImportError:
    sys.exit("ERROR: pypdf is required for image extraction.  pip install pypdf")


# ──────────────────────────────────────────────────────────────────────────────
# Logging
# ──────────────────────────────────────────────────────────────────────────────
logging.basicConfig(format="%(levelname)-8s %(message)s", level=logging.INFO)
log = logging.getLogger(__name__)


# ──────────────────────────────────────────────────────────────────────────────
# Image filtering helpers
# ──────────────────────────────────────────────────────────────────────────────
def is_header_footer_image(
    img_obj,
    page_height: float,
    skip_top_pct: float,
    skip_bottom_pct: float,
) -> bool:
    """
    Use pdfplumber image metadata to decide if an image sits in the
    header/footer zone (top or bottom margin of the page).
    Returns True if the image should be SKIPPED.
    """
    top    = img_obj.get("top",    None)   # distance from top of page
    bottom = img_obj.get("bottom", None)   # distance from top of page (bottom edge)

    if top is None or bottom is None or page_height <= 0:
        return False  # cannot determine position — keep image

    top_threshold    = page_height * (skip_top_pct    / 100.0)
    bottom_threshold = page_height * (1.0 - skip_bottom_pct / 100.0)

    # Skip if the image is entirely within the top or bottom margin zone
    if bottom <= top_threshold:
        return True   # entirely in header zone
    if top >= bottom_threshold:
        return True   # entirely in footer zone
    return False


def passes_size_filter(width: int, height: int, min_w: int, min_h: int) -> bool:
    """Return True if the image meets the minimum dimension requirements."""
    return width >= min_w and height >= min_h


def sanitize_name(name: str) -> str:
    """Replace spaces (and other problematic chars) with underscores so that
    Markdown image links work without URL-encoding."""
    return name.replace(" ", "_")


# ──────────────────────────────────────────────────────────────────────────────
# Image extraction
# ──────────────────────────────────────────────────────────────────────────────
def extract_images(
    pdf_path: Path,
    images_dir: Path,
    dry_run: bool,
    min_width: int = 100,
    min_height: int = 100,
    skip_top_pct: float = 10.0,
    skip_bottom_pct: float = 10.0,
) -> dict[int, list[Path]]:
    """
    Extract embedded images from a PDF using pypdf + pdfplumber for position info.

    Filtering applied (all configurable):
      1. Minimum size  — skips tiny decorative images (logos, dividers)
      2. Position zone — skips images in the top/bottom margin (header/footer area)

    Returns a dict mapping page_number (1-based) → list of saved image paths.
    In dry-run mode nothing is written; the dict contains hypothetical paths.
    """
    import io
    from pypdf import PdfReader
    from PIL import Image

    page_images: dict[int, list[Path]] = {}
    reader = PdfReader(str(pdf_path))
    img_counter = 0
    safe_stem = sanitize_name(pdf_path.stem)  # spaces → underscores

    # Build a position lookup from pdfplumber: page_num → list of image dicts
    plumber_imgs: dict[int, list[dict]] = {}
    with pdfplumber.open(pdf_path) as doc:
        for pn, pg in enumerate(doc.pages, start=1):
            plumber_imgs[pn] = pg.images or []
            # Store page height for percentage calculations
            plumber_imgs[pn + 10000] = pg.height  # crude but avoids a second dict

    for page_num, page in enumerate(reader.pages, start=1):
        page_images[page_num] = []

        page_height = plumber_imgs.get(page_num + 10000, 0) or 0
        position_infos = plumber_imgs.get(page_num, [])

        try:
            resources = page.get("/Resources")
            if resources is None:
                continue
            xobjects = resources.get("/XObject")
            if xobjects is None:
                continue
            xobjects = xobjects.get_object()
        except Exception:
            continue

        pos_index = 0  # align pdfplumber image list with pypdf XObjects
        for name, obj_ref in xobjects.items():
            try:
                obj = obj_ref.get_object()
            except Exception:
                continue

            if obj.get("/Subtype") != "/Image":
                continue

            img_counter += 1
            width  = int(obj.get("/Width",  0))
            height = int(obj.get("/Height", 0))

            # ── Filter 1: minimum size ────────────────────────────────────
            if not passes_size_filter(width, height, min_width, min_height):
                log.debug(
                    "  Skipped (too small %dx%d): page %d image #%d",
                    width, height, page_num, img_counter,
                )
                pos_index += 1
                continue

            # ── Filter 2: header/footer zone ──────────────────────────────
            pos_info = position_infos[pos_index] if pos_index < len(position_infos) else {}
            if is_header_footer_image(pos_info, page_height, skip_top_pct, skip_bottom_pct):
                log.debug(
                    "  Skipped (header/footer zone): page %d image #%d", page_num, img_counter
                )
                pos_index += 1
                continue

            pos_index += 1

            img_filename = f"{safe_stem}_p{page_num}_{img_counter:03d}.png"
            img_path = images_dir / img_filename

            if dry_run:
                log.info(
                    "  [DRY-RUN] Would extract image (%dx%d) → %s",
                    width, height, img_path.relative_to(pdf_path.parent),
                )
                page_images[page_num].append(img_path)
                continue

            try:
                data = obj.get_data()
                color_space = obj.get("/ColorSpace", "/DeviceRGB")
                mode = "RGB"
                if str(color_space) == "/DeviceGray":
                    mode = "L"
                elif str(color_space) == "/DeviceCMYK":
                    mode = "CMYK"

                try:
                    img = Image.open(io.BytesIO(data))
                except Exception:
                    img = Image.frombytes(mode, (width, height), data)

                images_dir.mkdir(parents=True, exist_ok=True)
                img.save(str(img_path), "PNG")
                page_images[page_num].append(img_path)
                log.info("  Extracted image (%dx%d) → %s", width, height, img_path.name)

            except Exception as exc:
                log.warning("  Could not save image %s: %s", img_filename, exc)

    return page_images


# ──────────────────────────────────────────────────────────────────────────────
# Markdown extraction
# ──────────────────────────────────────────────────────────────────────────────
def extract_markdown(
    pdf_path: Path,
    page_images: dict[int, list[Path]] | None = None,
) -> str:
    """
    Extract text from a PDF and return it as a Markdown string.

    - Tables are converted to Markdown pipe tables.
    - Each page is separated by a horizontal rule.
    - If page_images is provided, image references are inserted per page.
    """
    lines = []

    with pdfplumber.open(pdf_path) as doc:
        total = len(doc.pages)
        for page_num, page in enumerate(doc.pages, start=1):

            # ── Tables ────────────────────────────────────────────────────
            tables = page.extract_tables()
            table_md_blocks = []

            for table in tables:
                if not table:
                    continue
                header, *rows = table
                header = [cell or "" for cell in header]
                md_table = "| " + " | ".join(header) + " |\n"
                md_table += "| " + " | ".join(["---"] * len(header)) + " |\n"
                for row in rows:
                    row = [str(cell) if cell is not None else "" for cell in row]
                    md_table += "| " + " | ".join(row) + " |\n"
                table_md_blocks.append(md_table)

            # ── Plain text ────────────────────────────────────────────────
            raw_text = page.extract_text(x_tolerance=2, y_tolerance=2) or ""

            # ── Page separator ────────────────────────────────────────────
            if page_num > 1:
                lines.append("\n---\n")

            lines.append(f"<!-- Page {page_num} of {total} -->\n")

            if raw_text.strip():
                lines.append(raw_text.strip())

            for block in table_md_blocks:
                lines.append("\n" + block)

            # ── Images for this page ──────────────────────────────────────
            if page_images:
                imgs = page_images.get(page_num, [])
                for img_path in imgs:
                    # Use a relative path from the .md file's location
                    rel = img_path.relative_to(pdf_path.parent)
                    lines.append(f"\n![{img_path.stem}]({rel.as_posix()})\n")

    return "\n\n".join(lines)


# ──────────────────────────────────────────────────────────────────────────────
# Single-file conversion
# ──────────────────────────────────────────────────────────────────────────────
def convert_pdf(
    pdf_path: Path,
    dry_run: bool,
    with_images: bool,
    min_width: int = 100,
    min_height: int = 100,
    skip_top_pct: float = 10.0,
    skip_bottom_pct: float = 10.0,
) -> bool:
    """Convert a single PDF to a .md file. Returns True on success."""
    md_path = pdf_path.with_suffix(".md")
    images_dir = pdf_path.parent / f"{sanitize_name(pdf_path.stem)}_images"

    if dry_run:
        log.info("[DRY-RUN] Would convert: %s  →  %s", pdf_path.name, md_path.name)
        if with_images:
            log.info("          Images would be saved to: %s/", images_dir.name)
            log.info(
                "          Filter: min %dx%d px, skip top %.0f%% / bottom %.0f%%",
                min_width, min_height, skip_top_pct, skip_bottom_pct,
            )
            extract_images(
                pdf_path, images_dir, dry_run=True,
                min_width=min_width, min_height=min_height,
                skip_top_pct=skip_top_pct, skip_bottom_pct=skip_bottom_pct,
            )
        return True

    try:
        page_images = None
        if with_images:
            page_images = extract_images(
                pdf_path, images_dir, dry_run=False,
                min_width=min_width, min_height=min_height,
                skip_top_pct=skip_top_pct, skip_bottom_pct=skip_bottom_pct,
            )

        content = extract_markdown(pdf_path, page_images=page_images)
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
    parser.add_argument(
        "--images",
        action="store_true",
        help="Extract embedded images and reference them in the Markdown output",
    )
    # ── Image filter arguments ─────────────────────────────────────────────
    parser.add_argument(
        "--min-width",
        type=int,
        default=100,
        metavar="PX",
        help="Minimum image width in pixels to extract (default: 100). "
             "Smaller images (icons, logos in headers) are skipped.",
    )
    parser.add_argument(
        "--min-height",
        type=int,
        default=100,
        metavar="PX",
        help="Minimum image height in pixels to extract (default: 100). "
             "Smaller images (decorative lines, icons) are skipped.",
    )
    parser.add_argument(
        "--skip-top",
        type=float,
        default=10.0,
        metavar="PCT",
        help="Skip images whose bottom edge sits within this %% of the page "
             "height from the top (header zone). Default: 10.",
    )
    parser.add_argument(
        "--skip-bottom",
        type=float,
        default=10.0,
        metavar="PCT",
        help="Skip images whose top edge sits within this %% of the page "
             "height from the bottom (footer zone). Default: 10.",
    )
    args = parser.parse_args()

    # Validate PIL availability early when --images is requested
    if args.images and not args.dry_run:
        try:
            from PIL import Image  # noqa: F401
        except ImportError:
            sys.exit("ERROR: Pillow is required for image extraction.  pip install Pillow")

    folder = Path(args.folder).resolve()
    if not folder.is_dir():
        sys.exit(f"ERROR: '{folder}' is not a valid directory.")

    pdf_files = sorted(folder.rglob("*.pdf"))

    if not pdf_files:
        log.warning("No PDF files found in: %s", folder)
        return

    mode = "[DRY-RUN] " if args.dry_run else ""
    img_note = " (with images)" if args.images else ""
    log.info("%sFound %d PDF file(s) in: %s%s", mode, len(pdf_files), folder, img_note)

    success, failed = 0, 0
    for pdf_path in pdf_files:
        ok = convert_pdf(
            pdf_path,
            dry_run=args.dry_run,
            with_images=args.images,
            min_width=args.min_width,
            min_height=args.min_height,
            skip_top_pct=args.skip_top,
            skip_bottom_pct=args.skip_bottom,
        )
        if ok:
            success += 1
        else:
            failed += 1

    print()
    if args.dry_run:
        print(f"  DRY-RUN complete — {success} file(s) would be converted, no changes made.")
    else:
        print(f"  Done — {success} converted, {failed} failed.")


if __name__ == "__main__":
    main()
