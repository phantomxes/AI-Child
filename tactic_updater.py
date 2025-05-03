import json
from pathlib import Path
from collections import Counter
from datetime import datetime

MEMORY_FILE = Path.home() / "1man.army" / "memory" / "experience_log.json"
LESSONS_FILE = Path.home() / "1man.army" / "intel" / "learned_tactics.json"

def load_memory():
    if not MEMORY_FILE.exists():
        return []
    with open(MEMORY_FILE, 'r') as f:
        return json.load(f)

def analyze_patterns(entries):
    ports = []
    labels = []
    for entry in entries:
        output = entry.get("output_snippet", "")
        labels.append(entry.get("label", "unknown"))
        if "open" in output:
            for line in output.splitlines():
                if "/tcp" in line and "open" in line:
                    ports.append(line.split("/")[0].strip())

    return {
        "timestamp": datetime.utcnow().isoformat(),
        "top_ports": Counter(ports).most_common(5),
        "frequent_tasks": Counter(labels).most_common(3)
    }

def write_lessons(insights):
    lesson = {
        "timestamp": insights["timestamp"],
        "insights": {
            "most_scanned_ports": insights["top_ports"],
            "most_used_tasks": insights["frequent_tasks"],
            "recommendation": "Automate defense on frequent ports."
        }
    }

    if LESSONS_FILE.exists():
        with open(LESSONS_FILE, 'r+') as f:
            data = json.load(f)
            data.append(lesson)
            f.seek(0)
            json.dump(data, f, indent=2)
    else:
        with open(LESSONS_FILE, 'w') as f:
            json.dump([lesson], f, indent=2)

if __name__ == "__main__":
    entries = load_memory()
    if entries:
        insights = analyze_patterns(entries)
        write_lessons(insights)
        print("[✓] Tactical insights written to learned_tactics.json.")
    else:
        print("[!] No memory data found.")
