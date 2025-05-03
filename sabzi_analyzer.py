import json
from pathlib import Path
from collections import Counter

MEMORY_FILE = Path.home() / "1man.army" / "memory" / "experience_log.json"

def load_experience():
    if not MEMORY_FILE.exists():
        print("[!] No memory file found.")
        return []
    with open(MEMORY_FILE, 'r') as f:
        return json.load(f)

def analyze_tools_used(entries):
    tools = []
    for entry in entries:
        cmd = entry.get("command", [])
        if cmd:
            tools.append(cmd[0])  # like 'nmap'
    return Counter(tools).most_common()

def recommend_strategy(tool_stats):
    if not tool_stats:
        return "[!] Not enough data to recommend."

    top_tool, top_count = tool_stats[0]
    recommendation = f"Use '{top_tool}' for default scans — it was used {top_count} times with consistent success."

    if top_tool == "nmap":
        recommendation += "\n💡 Suggestion: Add -sV or --script based on past usage if service detection is common."

    return recommendation

if __name__ == "__main__":
    entries = load_experience()
    tool_stats = analyze_tools_used(entries)
    print("[🔍] Tool Usage Summary:")
    for tool, count in tool_stats:
        print(f" - {tool}: {count} runs")
    print("\n[🧠] Tactical Recommendation:")
    print(recommend_strategy(tool_stats))
