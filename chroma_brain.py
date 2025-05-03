import pyttsx3
import chromadb
import time
from chromadb.utils import embedding_functions
import json
from pathlib import Path

# 🔊 Voice setup
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

# 📁 Memory source + DB name
MEMORY_FILE = Path.home() / "1man.army" / "memory" / "experience_log.json"
COLLECTION_NAME = "1manarmy_memory"

# 🧠 Setup Chroma client + embeddings
client = chromadb.Client()
embed = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
collection = client.get_or_create_collection(name=COLLECTION_NAME, embedding_function=embed)

# 📥 Load saved experiences
def load_memories():
    with open(MEMORY_FILE, 'r') as f:
        return json.load(f)

# 📤 Add memories to vector DB
def feed_to_chroma(memories):
    for i, mem in enumerate(memories):
        doc = mem.get("output_snippet", "")[:512]
        metadata = {
            "label": mem.get("label"),
            "timestamp": mem.get("timestamp")
        }
        collection.add(documents=[doc], metadatas=[metadata], ids=[f"mem_{i}"])

# 🔍 Ask + voice response
def ask(question):
    results = collection.query(query_texts=[question], n_results=3)
    print("\n🧠 Query:", question)
    speak(f"Results for: {question}")

    for i in range(len(results["documents"][0])):
        ts = results['metadatas'][0][i]['timestamp']
        label = results['metadatas'][0][i]['label']
        snippet = results['documents'][0][i][:150].replace('\n', ' ')
        
        print(f"\n📌 Match #{i+1}:")
        print("🕓", ts)
        print("🔖", label)
        print("🧾", results['documents'][0][i])
        
        speak(f"Match {i+1}. From {ts}. Labeled {label}. Summary: {snippet}")

# 🎯 Start session
if __name__ == "__main__":
    data = load_memories()
    feed_to_chroma(data)
    print("[✓] Memory embedded into vector DB.")

    while True:
        q = input("\n🧠 Ask something (or type 'exit'): ")
        if q.lower() == "exit":
            speak("Session closed.")
            break

        ask(q)
        print("\n[✓] Query completed.")
        time.sleep(1)  # Adds natural pause
        speak("Query completed.")
        print("[✓] Ready for next question.")
        speak("Ready for next question.")
        print("--------------------------------------------------")
        time.sleep(1)
        speak("Standing by for next command.")
