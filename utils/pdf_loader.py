"""PDF ingestion helpers."""

from __future__ import annotations

from pathlib import Path
from typing import BinaryIO

from pypdf import PdfReader


def load_pdf(file: BinaryIO | str | Path, source_name: str | None = None) -> list[dict]:
    """Extract non-empty pages from a PDF as text records with page metadata."""
    reader = PdfReader(file)
    name = source_name or Path(getattr(file, "name", "document.pdf")).name
    pages: list[dict] = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = (page.extract_text() or "").strip()
        if text:
            pages.append({"text": text, "source": name, "page": page_number})

    if not pages:
        raise ValueError("No extractable text was found in this PDF.")
    return pages
