import streamlit as st
from backend.loader import load_pdf
from backend.splitter import split_text
from backend.embeddings import get_embeddings
from backend.vector_store import create_vector_store
from backend.retriever import get_retriever
from backend.rag_pipeline import answer_question
from backend.llm import load_llm

st.title("📚 AI Study Assistant (RAG)")

uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file:
    with open("data/temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.success("PDF uploaded successfully!")

    docs = load_pdf("data/temp.pdf")
    chunks = split_text(docs)
    embeddings = get_embeddings()
    vectorstore = create_vector_store(chunks, embeddings)
    retriever = get_retriever(vectorstore)

    query = st.text_input("Ask a question")
    @st.cache_resource

    def get_llm():

        return load_llm()

    llm = get_llm()

    if query:
        answer = answer_question(query, retriever, llm)
        st.write("### 📖 Answer:")
        st.write(answer)