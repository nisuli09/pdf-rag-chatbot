"""Small dependency-light text splitter used during ingestion."""

from __future__ import annotations


def split_documents(documents: list[dict], chunk_size: int = 900, chunk_overlap: int = 150) -> list[dict]:
    if chunk_size <= 0 or not 0 <= chunk_overlap < chunk_size:
        raise ValueError("chunk_overlap must be non-negative and smaller than chunk_size.")

    chunks: list[dict] = []
    step = chunk_size - chunk_overlap
    for document in documents:
        text = document["text"].strip()
        for start in range(0, len(text), step):
            chunk = text[start : start + chunk_size].strip()
            if not chunk:
                continue
            metadata = {key: value for key, value in document.items() if key != "text"}
            metadata["chunk"] = len(chunks)
            chunks.append({"text": chunk, **metadata})
            if start + chunk_size >= len(text):
                break
    return chunks
