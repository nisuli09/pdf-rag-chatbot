"""Persistent Chroma vector-store operations."""

from __future__ import annotations

from pathlib import Path
from uuid import uuid4

import chromadb

from .embeddings import get_embedding_function

DB_PATH = Path(__file__).resolve().parents[1] / "chroma_db"
COLLECTION_NAME = "pdf_chunks"


def _collection():
    client = chromadb.PersistentClient(path=str(DB_PATH))
    return client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=get_embedding_function(),
    )


def add_chunks(chunks: list[dict]) -> int:
    if not chunks:
        return 0
    collection = _collection()
    collection.add(
        ids=[str(uuid4()) for _ in chunks],
        documents=[chunk["text"] for chunk in chunks],
        metadatas=[{key: value for key, value in chunk.items() if key != "text"} for chunk in chunks],
    )
    return len(chunks)


def search(query: str, limit: int = 4) -> list[dict]:
    results = _collection().query(query_texts=[query], n_results=limit)
    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]
    distances = results.get("distances", [[]])[0]
    return [
        {"text": text, "metadata": metadata or {}, "distance": distance}
        for text, metadata, distance in zip(documents, metadatas, distances)
    ]


def clear_store() -> None:
    client = chromadb.PersistentClient(path=str(DB_PATH))
    try:
        client.delete_collection(COLLECTION_NAME)
    except ValueError:
        pass
