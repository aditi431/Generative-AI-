# 📄 AI PDF Summarizer & Q&A

A beginner-friendly Generative AI project that allows users to upload a PDF, extract its content, and interact with the document using AI.

This project is being built step by step to understand how **Retrieval-Augmented Generation (RAG)** applications work from the ground up.

## 🎥 Project Demo

https://github.com/aditi431/Generative-AI-/issues/1#issue-6058779028

https://lnkd.in/p/ggz4GfwV

> 🚧 **Project Status:** In Development — Day 1

## 🎯 Project Goal

The goal of this project is to build an AI-powered PDF assistant that can:

- 📄 Accept PDF documents
- 🔍 Extract text from PDFs
- ✂️ Split documents into smaller chunks
- 🧠 Convert text into embeddings
- 🗂️ Store embeddings in a vector database
- 🔎 Retrieve relevant information based on user questions
- 🤖 Generate answers using a Large Language Model
- 📝 Summarize uploaded documents

## 🏗️ Planned Architecture

```text
                    PDF
                     │
                     ▼
              Text Extraction
                     │
                     ▼
               Text Chunking
                     │
                     ▼
                Embeddings
                     │
                     ▼
              Vector Database
                 (FAISS)
                     │
                     ▼
             User's Question
                     │
                     ▼
          Semantic Similarity Search
                     │
                     ▼
            Relevant PDF Chunks
                     │
                     ▼
                  Gemini
                     │
                     ▼
               AI Generated
                  Answer
