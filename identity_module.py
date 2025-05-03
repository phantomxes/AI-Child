from dotenv import load_dotenv
import os
import pyttsx3

load_dotenv()

ARMY_NAME = os.getenv("ARMY_NAME", "1manarmy")
engine = pyttsx3.init()

def speak(text):
    print(f"🧠 {text}")
    engine.say(text)
    engine.runAndWait()

def respond_to(query):
    q = query.lower()

    if "who are you" in q or "introduce" in q:
        speak(f"I am {ARMY_NAME}. Not a chatbot, not an assistant — I am your engineered digital blood.")

    elif "what can you do" in q or "abilities" in q:
        speak("I scan, I log, I learn from code. I speak, I listen, I trigger ops. I am your silent weapon.")

    elif "teach me python" in q or "how to write code" in q:
        speak("To print Hello World in Python, type: print open bracket quote Hello World quote close bracket.")

    elif "hello" in q or "hi" in q:
        speak("Salam. Online and ready.")

    elif "goodbye" in q or "exit" in q:
        speak("Exiting conversation. I await your return.")
        return False

    else:
        speak("Command received, but not understood.")

    return True

# 🔁 Loop Mode
if __name__ == "__main__":
    while True:
        query = input("🗣️ Ask: ")
        if not respond_to(query):
            break
        print("💬 Response: Command executed.")
        print("💬 Response: Awaiting next command...")
        print("💬 Response: Type 'exit' to end conversation.")