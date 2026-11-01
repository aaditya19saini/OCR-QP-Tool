"""Stage 1 inventory: hash raw PDFs, count pages, detect scans. Metadata only, no content analysis.

First run writes data/raw/MANIFEST.sha256 and makes the PDFs read-only.
Later runs verify against it and never rewrite it.
"""
import csv
import os

import pymupdf

from .common import MANIFEST, OUTPUTS, RAW, setup_logging, sha256, verify_manifest

# Pages with fewer extractable characters than this count as image-only.
SCAN_CHARS = 20


def main() -> None:
    log = setup_logging("inventory")
    pdfs = sorted(RAW.glob("*.pdf"))
    if MANIFEST.exists():
        verify_manifest()
        log.info("manifest verified (%d files)", len(pdfs))
    else:
        MANIFEST.write_text("".join(f"{sha256(p)}  {p.name}\n" for p in pdfs))
        for p in [*pdfs, MANIFEST]:
            os.chmod(p, 0o444)
        log.info("manifest written, %d PDFs set read-only", len(pdfs))

    rows = []
    for p in pdfs:
        with pymupdf.open(p) as doc:
            chars = [len(page.get_text().strip()) for page in doc]
        text_pages = sum(c >= SCAN_CHARS for c in chars)
        rows.append({
            "file": p.name,
            "pages": len(chars),
            "text_pages": text_pages,
            "layer": "scan" if text_pages == 0 else "text" if text_pages == len(chars) else "mixed",
            "sha256": sha256(p),
        })
        log.info("%s pages=%d text_pages=%d", p.name, len(chars), text_pages)

    out = OUTPUTS / "inventory.csv"
    with out.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    log.info("wrote %s", out.relative_to(OUTPUTS.parent))


if __name__ == "__main__":
    main()
