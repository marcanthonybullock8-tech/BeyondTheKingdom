#!/usr/bin/env python3
"""Merge the numbered bible PDFs in pdf/ into one complete edition.

Usage: python3 tools/combine_pdfs.py   (requires: pip install pymupdf)
"""
from pathlib import Path

import pymupdf

PDF_DIR = Path(__file__).resolve().parent.parent / "pdf"
OUT = PDF_DIR / "Beyond_the_Kingdom_Complete_Series_Bible.pdf"

combined = pymupdf.open()
toc = []
for pdf in sorted(PDF_DIR.glob("[0-9][0-9]_*.pdf")):
    toc.append([1, pdf.stem.replace("_", " "), combined.page_count + 1])
    with pymupdf.open(pdf) as doc:
        combined.insert_pdf(doc)
combined.set_toc(toc)
combined.save(OUT)
print(OUT, combined.page_count, "pages")
