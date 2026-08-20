"""OpenAI-compatible answer generation."""

from __future__ import annotations

import os


def answer_question(question: str, matches: list[dict]) -> str:
    """Answer from retrieved context, with a useful offline fallback."""
    context = "\n\n".join(
        f"[Source: {item['metadata'].get('source', 'PDF')}, page {item['metadata'].get('page', '?')}]\n{item['text']}"
        for item in matches
    )
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "Set `OPENAI_API_KEY` in `.env` to generate an answer. Relevant excerpts:\n\n" + context

    from openai import OpenAI

    response = OpenAI(api_key=api_key).chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        temperature=0,
        messages=[
            {"role": "system", "content": "Answer only from the supplied PDF context. Say when the context does not contain the answer."},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"},
        ],
    )
    return response.choices[0].message.content or "I could not generate an answer."
