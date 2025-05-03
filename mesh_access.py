import json
import time
import os
from pathlib import Path
from datetime import datetime

# 🗂 Shared drop directory for mesh communication
MESH_DIR = Path.home() / "1man.army" / "mesh"
MESH_DIR.mkdir(parents=True, exist_ok=True)

def send_mesh(task_name, payload):
    timestamp = datetime.utcnow().isoformat()
    packet = {
        "task": task_name,
        "timestamp": timestamp,
        "payload": payload
    }
    filename = f"{task_name}_{int(time.time())}.json"
    with open(MESH_DIR / filename, "w") as f:
        json.dump(packet, f)
    print(f"[🔁] Mesh message sent: {filename}")

def read_mesh():
    for file in sorted(MESH_DIR.glob("*.json")):
        with open(file, "r") as f:
            data = json.load(f)
            print(f"\n[📡] Message from: {data['task']}")
            print(f"⏱  At: {data['timestamp']}")
            print(f"📦 Payload: {data['payload']}")
        os.remove(file)  # auto-clear after read

if __name__ == "__main__":
    # 🔧 Example mesh test (can remove in prod)
    send_mesh("sabzi_analyzer", {"status": "Sabzi scanned", "targets": 3})
    time.sleep(1)
    read_mesh()
