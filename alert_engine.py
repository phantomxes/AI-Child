import json
from pathlib import Path
from datetime import datetime
import pyttsx3

# Voice setup
engine = pyttsx3.init()
def speak(msg):
    print(f"[🔊] {msg}")
    engine.say(msg)
    engine.runAndWait()

# Memory file
MEMORY_FILE = Path.home() / "1man.army" / "memory" / "experience_log.json"

# Critical items to flag
danger_ports = {"21", "23", "445", "3389", "5900", "22"}
hot_keywords = {"vulnerable", "exploit", "ransomware", "malware", "unauthorized", "critical"}

# Load memory
with open(MEMORY_FILE, "r") as f:
    memory = json.load(f)

# Analyze last 10 logs
alerts = []
for m in memory[-10:]:
    output = m.get("output_snippet", "").lower()
    label = m.get("label", "")
    ts = m.get("timestamp", "")
    found = []

    for port in danger_ports:
        if f"{port}/tcp" in output and "open" in output:
            found.append(f"⚠️ Port {port}/tcp OPEN")

    for keyword in hot_keywords:
        if keyword in output:
            found.append(f"🚨 Word found: {keyword}")

    if found:
        alerts.append({
            "timestamp": ts,
            "label": label,
            "flags": found
        })

# Report
if alerts:
    for alert in alerts:
        speak(f"Threat found in {alert['label']} at {alert['timestamp']}")
        for flag in alert['flags']:
            print(f" - {flag}")
else:
    speak("No threats detected.")
    print("✅ All clear. No critical alerts.")
