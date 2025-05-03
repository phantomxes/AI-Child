import speech_recognition as sr
import pyttsx3
import subprocess
import time

engine = pyttsx3.init()
r = sr.Recognizer()

def speak(text):
    print(f"[🧠] {text}")
    engine.say(text)
    engine.runAndWait()

def listen_command():
    with sr.Microphone() as source:
        print("\n🎙 Listening...")
        audio = r.listen(source, phrase_time_limit=5)
    try:
        command = r.recognize_google(audio)
        print(f"[🔊] You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("professor johnny i didn't catch that.")
    except sr.RequestError:
        speak("Speech recognition error.")
    return ""

def process_command(cmd):
    if "run scan" in cmd:
        speak("Running sentinel scan.")
        subprocess.run(["python", "sentinel_agent.py"])
    elif "check memory" in cmd:
        speak("Reading recent memory.")
        subprocess.run(["python", "sabzi_analyzer.py"])
    elif "check alerts" in cmd:
        speak("Launching alert check.")
        subprocess.run(["python", "alert_engine.py"])
    elif "generate report" in cmd:
        speak("Generating report.")
        subprocess.run(["python", "report_generator.py"])
    elif "shutdown" in cmd or "exit" in cmd:
        speak("Voice console terminated.")
        return False
    else:
        speak("Command not recognized.")
    return True

if __name__ == "__main__":
    speak("Voice Cortex online. Awaiting command.")
    while True:
        cmd = listen_command()
        if not cmd:
            continue
        if not process_command(cmd):
            break
        time.sleep(1)
