import json
from pathlib import Path
from collections import Counter

memory_path = Path.home() / "1man.army" / "memory" / "experience_log.json"

try:
    with open(memory_path, "r") as file:
        data = json.load(file)
except Exception as e:
    print(f"Memory load error: {e}")
    exit()

# Track tool usage and outcomes
tool_stats = Counter()
recommendation = "[!] Not enough memory to recommend."

for entry in data[-10:]:
    label = entry.get("label", "unknown")
    snippet = entry.get("output_snippet", "").lower()

    if any(x in snippet for x in ["open", "granted", "success", "rooted", "found"]):
        tool_stats[label] += 1

if tool_stats:
    top_tool, count = tool_stats.most_common(1)[0]
    recommendation = f"✅ Use '{top_tool}' — success observed in {count} of last 10 logs."

print("\\n🧠 SUGGESTED ACTION:")
print(recommendation)
