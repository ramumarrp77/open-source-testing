# LangGraph PDF-Based RAG Agent

## Project Description
The **LangGraph PDF-Based RAG Agent** is a local application designed to assist users in retrieving information from PDF documents. It leverages semantic embedding generation and natural language processing to provide efficient and contextually relevant responses to user queries. The main features include:

- **PDF Loading and Processing**: Users can upload PDF documents for analysis.
- **Semantic Embedding Generation**: The application generates and stores embeddings locally to optimize performance.
- **Semantic Search**: Users can perform natural language queries to retrieve relevant sections from the PDFs.
- **Contextual Response Generation**: The agent combines retrieved passages with language model capabilities to generate informative responses, citing sources accurately.

## Code Structure

```
project-root/
│
├── frontend.py          # Streamlit UI for user interaction
├── backend.py           # Backend logic for PDF processing and response generation
├── requirements.txt     # List of dependencies required for the project
└── embeddings/           # Directory for storing generated embeddings

```

### Key Files and Modules
- **frontend.py**: Contains the Streamlit application code, handling user input, PDF uploads, and displaying results.
- **backend.py**: Implements the core functionality for loading PDFs, generating embeddings, searching documents, and generating responses.
- **requirements.txt**: Lists the necessary Python packages for the project.

## Setup and Installation

### Prerequisites
- Python 3.7 or higher
- An OpenAI API key (for using OpenAI models)

### Installation Steps
1. **Clone the repository**:
   <bash>
   git clone https://github.com/yourusername/langgraph-pdf-rag-agent.git
   cd langgraph-pdf-rag-agent
   </bash>

2. **Set up the development environment**:
   It is recommended to use a virtual environment. You can create one using:
   <bash>
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`
   </bash>

3. **Install dependencies**:
   <bash>
   pip install -r requirements.txt
   </bash>

4. **Run the application**:
   <bash>
   streamlit run frontend.py
   </bash>

## Dependencies
- `langgraph==0.2.53`
- `streamlit`
- `PyPDF2`
- `numpy`
- `langchain`

## Configuration Instructions
- Set your OpenAI API key in your environment variables:
  <bash>
  export OPENAI_API_KEY=\'your_openai_api_key\'  # On Windows use `set OPENAI_API_KEY=your_openai_api_key`
  </bash>

## Usage Examples
1. **Upload PDF Files**: Use the file uploader in the sidebar to upload one or more PDF documents.
2. **Enter a Query**: Type your question in the query input box.
3. **Search for Relevant Passages**: Click the "Search" button to retrieve relevant sections from the uploaded PDFs.
4. **Generate a Response**: Click the "Generate Response" button to receive a contextual answer based on the retrieved passages.

## Troubleshooting Tips
- Ensure that your OpenAI API key is correctly set in the environment variables.
- If you encounter issues with PDF loading, check the format and ensure the files are not corrupted.
- For any errors related to dependencies, ensure that all packages are installed as specified in `requirements.txt`.

This README provides a comprehensive overview of the LangGraph PDF-Based RAG Agent, guiding users through setup, usage, and troubleshooting.