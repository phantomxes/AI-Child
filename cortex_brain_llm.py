import chromadb
from chromadb.utils import embedding_functions
import json, time
from pathlib import Path
import subprocess

# LLM + Memory Integration
from openai import OpenAI
client = chromadb.Client()
embed = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

MEMORY_FILE = Path.home() / "1man.army" / "memory" / "experience_log.json"
COLLECTION_NAME = "1manarmy_memory"
collection = client.get_or_create_collection(name=COLLECTION_NAME, embedding_function=embed)

def ask_brain(question):
    results = collection.query(query_texts=[question], n_results=3)
    docs = results["documents"][0]

    context = "\n\n".join(docs)
    prompt = f"You are a memory-embedded code AI. Based on the following memory, answer the user's query:\n\n{context}\n\nQ: {question}\nA:"

    print("\n🧠 Thinking...")

    # Use local Ollama model
    response = subprocess.run(["ollama", "run", "mistral"], input=prompt, text=True, capture_output=True)
    print("\n🤖", response.stdout)

if __name__ == "__main__":
    while True:
        q = input("\n💬 Ask (or type 'exit'): ")
        if q.lower() == "exit":
            break
        ask_brain(q)
