import subprocess
import datetime
import json
import os
from pathlib import Path

# Config
BASE_DIR = Path.home() / "1man.army"
SCAN_DIR = BASE_DIR / "scans"
LOG_DIR = BASE_DIR / "logs"
MEMORY_FILE = BASE_DIR / "memory" / "experience_log.json"

class SentinelAgent:
    def __init__(self, codename="1man.army"):
        self.codename = codename
        self.log_path = LOG_DIR / f"log_{self._timestamp()}.txt"
        self._init_dirs()

    def _init_dirs(self):
        for path in [SCAN_DIR, LOG_DIR, MEMORY_FILE.parent]:
            os.makedirs(path, exist_ok=True)
        if not MEMORY_FILE.exists():
            print("[!] Memory file not found. Creating...")
            with open(MEMORY_FILE, 'w') as f:
                json.dump([], f)

    def _timestamp(self):
        return datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    def run_tool(self, cmd_list, label="custom_tool"):
        print(f"[+] Running {label}: {' '.join(cmd_list)}")
        try:
            result = subprocess.run(cmd_list, capture_output=True, text=True, timeout=300)
            output = result.stdout
            print("[✓] Tool executed.")
            self._log_event(label, cmd_list, output)
            self._store_experience(label, cmd_list, output)
            return output
        except Exception as e:
            print(f"[✗] Tool failed: {e}")
            self._log_event(label, cmd_list, str(e))
            return str(e)

    def _log_event(self, label, cmd, output):
        print("[+] Logging event...")
        with open(self.log_path, 'a') as log:
            log.write(f"\n[{self._timestamp()}] [{label}]\n")
            log.write(f"CMD: {' '.join(cmd)}\n")
            log.write(f"OUT:\n{output}\n")
        print("[✓] Log written.")

    def _store_experience(self, label, cmd, output):
        print("[+] Storing experience...")
        try:
            entry = {
                "timestamp": self._timestamp(),
                "label": label,
                "command": cmd,
                "output_snippet": output[:500]
            }
            with open(MEMORY_FILE, 'r+') as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    print("[!] JSON broken — resetting memory file.")
                    data = []
                data.append(entry)
                f.seek(0)
                json.dump(data, f, indent=2)
                print("[✓] Experience saved.")
        except Exception as e:
            print(f"[✗] Failed to store experience: {e}")

# Test run
if __name__ == "__main__":
    agent = SentinelAgent()
    output = agent.run_tool(["nmap", "-F", "127.0.0.1"], label="quick_scan")
    print("[✓] Scan complete.")
