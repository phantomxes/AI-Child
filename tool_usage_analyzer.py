
import json
from pathlib import Path
from collections import Counter

memory_path = Path.home() / "1man.army" / "memory" / "experience_log.json"

# Load experience log
try:
    with open(memory_path, "r") as file:
        data = json.load(file)
except Exception as e:
    print(f"Failed to read memory: {e}")
    exit()

# Count tool usage
tool_counts = Counter()
for entry in data:
    label = entry.get("label", "unknown")
    tool_counts[label] += 1

# Show sorted result
print("\n🧠 TOOL USAGE STATS")
for tool, count in tool_counts.most_common():
    print(f" - {tool}: {count} times")
