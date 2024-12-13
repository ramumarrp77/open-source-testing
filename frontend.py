import streamlit as st
import os
from backend import load_pdf, generate_embeddings, search_documents, generate_response

# Streamlit UI
st.title("LangGraph PDF-Based RAG Agent")

# Sidebar for OpenAI API Key
openai_api_key = st.sidebar.text_input("Enter your OpenAI API Key:")

# PDF Upload
uploaded_files = st.file_uploader("Upload PDF files", type=['pdf'], accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        # Load PDF
        pdf_text = load_pdf(uploaded_file)
        st.write(f"Loaded {uploaded_file.name}")

        # Generate embeddings
        embeddings = generate_embeddings(pdf_text)
        st.write("Embeddings generated and stored.")

# Query Input
query = st.text_input("Enter your query:")

if st.button("Search"):
    if query:
        # Search documents
        results = search_documents(query)
        st.write("Search Results:")
        for result in results:
            st.write(result)

# Response Generation
if st.button("Generate Response"):
    if query:
        response = generate_response(query)
        st.write("Response:")
        st.write(response)