# FlowForma AI Support Assistant
title: FlowForma Chatbot
emoji: 💬
colorFrom: indigo
colorTo: purple
sdk: streamlit
sdk_version: "1.32.2"
app_file: app/main.py
pinned: false
---
# FlowForma AI Support Assistant

The FlowForma AI Support Assistant is a lightweight, fully offline question-answering application designed to assist users in retrieving information from a custom knowledge base. It is particularly useful for internal documentation support, product education, and self-service troubleshooting without requiring internet access or third-party APIs.

The system utilizes state-of-the-art open-source language models to understand user queries and generate relevant answers based on preloaded documents. It offers an intuitive browser-based interface through Streamlit and can be deployed locally or in a containerized environment.

---

## Key Features

- Offline operation using locally available models
- Fast semantic search powered by FAISS and SentenceTransformers
- Context-aware answer generation using FLAN-T5
- Flexible document ingestion from plain text files
- Streamlit web interface for ease of use
- Docker support for easy deployment and portability

---

## How It Works

1. **Knowledge Base Ingestion**: Text documents are loaded from a folder or zip archive. These are used as the source of truth for answering questions.
2. **Embedding Generation**: Each document is converted into a vector using the `all-MiniLM-L6-v2` model from SentenceTransformers.
3. **Vector Search**: When a question is asked, it is embedded and matched against the stored vectors using FAISS to retrieve the most relevant chunks of text.
4. **Answer Generation**: Retrieved chunks and the user’s question are passed to the `google/flan-t5-base` model to generate a concise and relevant answer.
5. **User Interface**: A Streamlit front-end allows for user-friendly interaction and displays the question, sources, and AI-generated answer.

---

## Installation

1. Clone the repository or download the project files.
2. Install Python dependencies:

```bash
pip install -r requirements.txt
"# Customer-Support-Chatbot-FlowForma" 
