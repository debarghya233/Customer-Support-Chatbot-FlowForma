from transformers import pipeline
from fallback import fallback_response

qa_model = pipeline("text2text-generation", model="google/flan-t5-base")

def get_response(query, vectordb, k=3):
    docs = vectordb.similarity_search(query, k=k)
    context = "\n".join([doc.page_content for doc in docs])
    prompt = f"Context:\n{context}\n\nQuestion: {query}"
    raw = qa_model(prompt, max_new_tokens=100)[0]["generated_text"]
    return fallback_response(raw)
