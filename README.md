# 📄 AI PDF Summarizer

An AI-powered application that helps users understand lengthy PDF documents by generating concise summaries. It uses text extraction, intelligent text chunking, embeddings, and vector search to process documents and retrieve relevant information for summarization.

## ✨ Features

- **PDF Upload:** Upload PDF documents for processing.
- **Text Extraction:** Extract readable text from PDF files.
- **Smart Text Chunking:** Split long documents into smaller, manageable sections.
- **Semantic Embeddings:** Convert text chunks into numerical representations to capture their meaning.
- **Vector Search:** Use FAISS to find relevant document chunks efficiently.
- **AI-Powered Summarization:** Generate concise summaries using Google Gemini.
- **Modular Design:** Keep text processing, embeddings, vector storage, and AI operations organized into separate components.

## ⚙️ How It Works

1. **Upload PDF:** The user provides a PDF document.
2. **Extract Text:** Text is extracted from the uploaded document.
3. **Split into Chunks:** The extracted text is divided into smaller sections for processing.
4. **Generate Embeddings:** Text chunks are converted into embeddings using Sentence Transformers.
5. **Store and Retrieve:** FAISS stores the vector representations and helps retrieve relevant chunks.
6. **Generate Summary:** Google Gemini processes the relevant document content to produce a concise summary.
7. **View Results:** The user can access the generated summary through the application interface.

## 🎥 Project Demo

Watch the AI PDF Summarizer demonstration on LinkedIn: https://lnkd.in/p/ggz4GfwV

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Streamlit | User interface |
| PyPDF | PDF text extraction |
| Google Gemini | AI-powered summarization |
| Sentence Transformers | Text embeddings |
| FAISS | Vector storage and similarity search |

## 📁 Project Structure

```text
AI-PDF-Summarizer/
├── app.py
├── requirements.txt
├── test_chunks.py
└── utils/
    ├── embeddings.py
    ├── llm.py
    ├── text_splitter.py
    └── vector_store.py
```




## 🎯 Project Objective

The goal of this project is to make lengthy PDF documents easier to understand by combining document processing, semantic search, and generative AI. It demonstrates how different AI components can work together to turn unstructured document text into concise, useful information.

---

**Built with Python, Streamlit, and Generative AI.**
