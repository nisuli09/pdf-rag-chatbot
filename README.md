# 📄 PDF RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that lets you upload PDF documents and ask questions about their content. Answers are generated from the most relevant parts of your documents, so responses stay grounded in the source material.

Built with Python, Streamlit, ChromaDB and an LLM API.

## ✨ Features

- Upload one or more PDF files through a simple web interface
- Automatic text extraction and chunking
- Semantic search using vector embeddings
- Persistent local vector database (ChromaDB)
- Chat interface powered by Streamlit
- Answers based on retrieved document context

## 🧠 How It Works

```
PDF upload → Text extraction → Chunking → Embeddings → Vector store (ChromaDB)
                                                              ↓
                 User question → Embed query → Retrieve top chunks → LLM → Answer
```

1. **PDF loading**: text is extracted from the uploaded PDF (`pdf_loader.py`)
2. **Splitting**: text is divided into smaller overlapping chunks (`text_splitter.py`)
3. **Embeddings**: each chunk is converted into a vector (`embeddings.py`)
4. **Vector store**: vectors are stored and searched in ChromaDB (`vector_store.py`)
5. **Chatbot**: the most relevant chunks are passed to the LLM together with the question to generate an answer (`chatbot.py`)

## 📁 Project Structure

```
rag-chatbot/
├── .streamlit/
│   └── config.toml        # Streamlit configuration
├── utils/
│   ├── chatbot.py         # RAG chain / LLM answer generation
│   ├── embeddings.py      # Embedding model setup
│   ├── pdf_loader.py      # PDF text extraction
│   ├── text_splitter.py   # Text chunking
│   └── vector_store.py    # ChromaDB vector store handling
├── app.py                 # Streamlit app entry point
├── requirements.txt       # Python dependencies
└── .gitignore
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- An API key for the LLM provider used in this project (e.g. Groq)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/nisuli09/pdf-rag-chatbot.git
cd pdf-rag-chatbot

# 2. Create and activate a virtual environment
python -m venv venv

# Windows (PowerShell)
venv\Scripts\Activate.ps1
# macOS / Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_api_key_here
```

> Never commit your `.env` file. It is already listed in `.gitignore`.

### Run the App

```bash
streamlit run app.py
```

Then open the URL shown in the terminal (usually http://localhost:8501).

## 💬 Usage

1. Upload a PDF using the uploader
2. Wait for the document to be processed and indexed
3. Ask questions about the document in the chat box
4. Get answers based on the document's content

## 🛠️ Tech Stack

| Component        | Technology        |
| ---------------- | ----------------- |
| Language         | Python            |
| UI               | Streamlit         |
| Vector Database  | ChromaDB          |
| Embeddings       | Sentence embeddings |
| LLM              | Groq API          |

## 🔮 Future Improvements

- Support for multiple file types (DOCX, TXT)
- Source citations with page numbers
- Chat history memory
- Deployment on Streamlit Community Cloud

## 👤 Author

**Nisuli Kihansa**
GitHub: [@nisuli09](https://github.com/nisuli09)

