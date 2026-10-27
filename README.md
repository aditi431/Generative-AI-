# AI PDF Summarizer & Q&A

An AI-powered application that helps users understand PDF documents without having to read every page manually. Users can upload a PDF, generate a summary, and ask questions about its content to get relevant answers based on the information available in the document.

## Features

- **PDF Summarization:** Get a concise summary of an uploaded PDF.
- **Question Answering:** Ask questions about the document and receive answers based on its content.
- **Text Extraction:** Extract text from PDF documents for further processing.
- **Text Chunking:** Split long documents into smaller sections for efficient retrieval.
- **Semantic Search:** Find relevant information using text embeddings.
- **Vector Search with FAISS:** Retrieve document sections related to a user's question.
- **Gemini Integration:** Generate summaries and answers using Google's Gemini model.
- **Interactive UI:** Upload documents and interact with them through a Streamlit application.

## Project Demo

Watch the Project Demo on LinkedIn - https://lnkd.in/p/ggz4GfwV

## How It Works

The application follows a Retrieval-Augmented Generation (RAG) pipeline to answer questions using information from the uploaded PDF.

<escape>
PDF Upload → Text Extraction → Text Chunking → Embeddings → FAISS Retrieval → Gemini LLM → Answer
</escape>

1. **Upload PDF:** The user uploads a document.
2. **Extract Text:** Text is extracted from the PDF.
3. **Split into Chunks:** The extracted text is divided into smaller sections.
4. **Create Embeddings:** Text chunks are converted into numerical representations.
5. **Retrieve Relevant Information:** FAISS searches for the chunks most relevant to the user's question.
6. **Generate an Answer:** Gemini uses the retrieved information to generate a relevant response.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Streamlit | Interactive user interface |
| Google Gemini (`gemini-3.6-flash`) | AI-generated summaries and answers |
| Sentence Transformers | Text embeddings |
| FAISS | Similarity search and information retrieval |
| pypdf | PDF text extraction |

## Example Use Case

A user uploads their resume and asks:

**“What are the technical skills?”**

The application retrieves the relevant information from the resume and provides an answer based on the document's content.

The same approach can be used to explore research papers, study materials, reports, and other PDF documents.

## What I Learned

Building this project gave me practical experience with:

- PDF text extraction and preprocessing
- Text chunking and embeddings
- Semantic search and vector databases
- Retrieval-Augmented Generation (RAG)
- LLM integration and prompt engineering
- Building interactive AI applications with Streamlit
- Debugging errors and connecting different components into one working pipeline

## Project Demo

[Watch the Project Demo on LinkedIn](https://lnkd.in/p/ggz4GfwV)

## Future Scope

I plan to explore more advanced RAG systems, improve answer quality, and build AI agents and LLM-powered applications that solve real-world problems.
