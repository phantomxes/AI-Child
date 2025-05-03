import subprocess
import time
from datetime import datetime
import pyttsx3

engine = pyttsx3.init()
def speak(text):
    print(f"[🧠] {text}")
    engine.say(text)
    engine.runAndWait()

# 🔁 Run core modules in sequence
def run_agent():
    speak("Starting scan.")
    subprocess.run(["python", "sentinel_agent.py"])

def run_updater():
    speak("Updating tactics from memory.")
    subprocess.run(["python", "tactic_updater.py"])

def run_analyzer():
    speak("Analyzing intelligence.")
    subprocess.run(["python", "sabzi_analyzer.py"])

def run_alerts():
    speak("Scanning for threats.")
    subprocess.run(["python", "alert_engine.py"])

def run_report():
    speak("Generating mission report.")
    subprocess.run(["python", "report_generator.py"])

# 🎯 EXECUTE
if __name__ == "__main__":
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    speak(f"Auto-sentinel activated. Time: {now}")

    run_agent()
    time.sleep(2)
    run_updater()
    time.sleep(1)
    run_analyzer()
    time.sleep(1)
    run_alerts()
    time.sleep(1)
    run_report()

    speak("Mission cycle complete. Standing by for next deployment.")
