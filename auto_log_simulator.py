import json, random, time
from pathlib import Path
from datetime import datetime
import pyttsx3

tools = ["nmap", "sqlmap", "gobuster", "hydra", "nikto", "whois"]
ports = ["22", "80", "443", "445", "3389", "5900"]
keywords = ["vulnerable", "exploit", "malware", "unauthorized", "access granted", "rooted"]

path = Path.home() / "1man.army" / "memory"
path.mkdir(parents=True, exist_ok=True)
file = path / "experience_log.json"

try:
    with file.open("r") as f:
        memory = json.load(f)
except:
    memory = []

engine = pyttsx3.init()
def speak(text):
    print(f"[🎙️] {text}")
    engine.say(text)
    engine.runAndWait()

print("🔁 Auto log simulator started... CTRL+C to stop.")

while True:
    now = datetime.utcnow().isoformat()
    label = random.choice(tools)
    command = [label, "-r", "127.0.0.1"]
    keyword = random.choice(keywords)
    port = random.choice(ports)
    output = f"{port}/tcp open\n{keyword}\nPort {random.choice(ports)} active"

    memory.append({
        "timestamp": now,
        "label": label,
        "command": command,
        "output_snippet": output
    })
    with file.open("w") as f:
        json.dump(memory, f, indent=2)
    
    speak(f"{label.upper()} triggered. Alert: {keyword}")
    time.sleep(5)
