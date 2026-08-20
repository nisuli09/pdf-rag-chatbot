"""Streamlit PDF retrieval-augmented chatbot."""

from __future__ import annotations

import streamlit as st
from dotenv import load_dotenv

from utils.chatbot import answer_question
from utils.pdf_loader import load_pdf
from utils.text_splitter import split_documents
from utils.vector_store import add_chunks, clear_store, search

load_dotenv()
st.set_page_config(page_title="PDF RAG Chatbot", page_icon="📄")
st.title("📄 PDF RAG Chatbot")
st.caption("Upload PDFs, then ask questions grounded in their contents.")

with st.sidebar:
    uploads = st.file_uploader("PDF files", type=["pdf"], accept_multiple_files=True)
    if st.button("Index uploaded PDFs", type="primary", disabled=not uploads):
        try:
            with st.spinner("Extracting and indexing documents…"):
                documents = [page for upload in uploads for page in load_pdf(upload, upload.name)]
                count = add_chunks(split_documents(documents))
            st.success(f"Indexed {count} text chunks.")
        except Exception as exc:
            st.error(f"Could not index the PDFs: {exc}")
    if st.button("Clear document index"):
        clear_store()
        st.success("Document index cleared.")

question = st.chat_input("Ask a question about your PDFs")
if question:
    with st.chat_message("user"):
        st.write(question)
    try:
        matches = search(question)
        if not matches:
            st.warning("No indexed PDF content was found. Upload and index a PDF first.")
        else:
            with st.chat_message("assistant"):
                st.write(answer_question(question, matches))
                with st.expander("Retrieved sources"):
                    for match in matches:
                        metadata = match["metadata"]
                        st.caption(f"{metadata.get('source', 'PDF')} — page {metadata.get('page', '?')}")
                        st.write(match["text"])
    except Exception as exc:
        st.error(f"Unable to answer the question: {exc}")
