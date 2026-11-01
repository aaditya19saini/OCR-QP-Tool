"""Render a paper's pages to PNG (for vision reading) plus a raw text-layer dump (cross-check only).

Usage: python -m pyq.render 2023
Output: data/pages/<year>/p001.png, p001.txt, ...  (regenerable, gitignored)
"""
import sys

import pymupdf

from .common import PAGES, RAW, load_yaml, setup_logging, verify_manifest

DPI = 200  # fixed so re-renders are pixel-identical


def render(year: int) -> None:
    log = setup_logging(f"render-{year}")
    verify_manifest()
    paper = load_yaml("papers.yaml")["papers"][year]
    out = PAGES / str(year)
    out.mkdir(parents=True, exist_ok=True)
    with pymupdf.open(RAW / paper["file"]) as doc:
        for i, page in enumerate(doc, 1):
            page.get_pixmap(dpi=DPI).save(out / f"p{i:03d}.png")
            (out / f"p{i:03d}.txt").write_text(page.get_text())
        log.info("%s: %d pages rendered at %d dpi to %s", paper["file"], len(doc), DPI, out)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: python -m pyq.render <year>")
    render(int(sys.argv[1]))
