import os
import zipfile
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

def load_kb():
    zip_path = "app/FlowForma_Knowledge_Base.zip"
    extract_path = "app/FlowForma_KB"

    # Extract if not already
    if not os.path.exists(extract_path):
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(extract_path)

    # Debug print files
    print("Extracted files:")
    for root, _, files in os.walk(extract_path):
        for file in files:
            print("-", os.path.join(root, file))

    loader = DirectoryLoader(extract_path, glob="**/*.md")  # original
    # Change to accept markdown-in-.txt:
    loader = DirectoryLoader(extract_path, glob="**/*.md")  # legacy (ignored now)
    loader = DirectoryLoader(extract_path, glob="**/*.txt")  # or use this
    docs = loader.load()

    if not docs:
        raise ValueError("No Markdown documents found. Check your ZIP contents.")

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    if not chunks:
        raise ValueError("No chunks created from documents. Are the files empty or incorrectly formatted?")

    embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return FAISS.from_documents(chunks, embedding)