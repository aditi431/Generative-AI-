import streamlit as st

from utils.pdf_loader import extract_text_from_pdf
from utils.text_splitter import split_text
from utils.embeddings import create_embeddings
from utils.vector_store import (
    create_vector_store,
    search_vector_store
)
from utils.llm import generate_answer


st.set_page_config(
    page_title="AI PDF Assistant",
    page_icon="📄",
    layout="wide"
)


st.title("📄 AI PDF Summarizer & Q&A")

st.write(
    "Upload a PDF and ask questions about its contents."
)


uploaded_file = st.file_uploader(
    "Upload your PDF",
    type=["pdf"]
)


if uploaded_file is not None:

    if "processed_file" not in st.session_state:

        with st.spinner("Reading PDF..."):

            text = extract_text_from_pdf(uploaded_file)

        if not text.strip():
            st.error(
                "Could not extract text from this PDF."
            )
            st.stop()

        with st.spinner("Splitting document..."):

            chunks = split_text(text)

        with st.spinner("Creating embeddings..."):

            embeddings = create_embeddings(chunks)

        with st.spinner("Creating vector database..."):

            index = create_vector_store(embeddings)

        st.session_state.processed_file = uploaded_file.name
        st.session_state.chunks = chunks
        st.session_state.index = index

        st.success("PDF processed successfully!")


if "processed_file" in st.session_state:

    st.divider()

    st.subheader("💬 Ask a question")

    question = st.text_input(
        "What do you want to know about the PDF?"
    )

    if st.button("Ask AI"):

        if not question.strip():

            st.warning("Please enter a question.")

        else:

            with st.spinner("Searching the PDF..."):

                question_embedding = create_embeddings(
                    [question]
                )

                distances, indices = search_vector_store(
                    st.session_state.index,
                    question_embedding,
                    top_k=3
                )

                relevant_chunks = [
                    st.session_state.chunks[i]
                    for i in indices[0]
                ]

                context = "\n\n".join(
                    relevant_chunks
                )

            with st.spinner("Generating answer..."):

                answer = generate_answer(
                    question,
                    context
                )

            st.subheader("🤖 Answer")

            st.write(answer)