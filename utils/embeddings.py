"""Embedding configuration for Chroma."""

from __future__ import annotations

import chromadb


def get_embedding_function():
    """Return Chroma's built-in local embedding function.

    The model is downloaded by Chroma on first use, so no API key is required
    for document search.
    """
    return chromadb.utils.embedding_functions.DefaultEmbeddingFunction()
