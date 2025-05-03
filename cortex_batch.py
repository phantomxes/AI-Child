import os
import time
import subprocess
from pathlib import Path

SCRIPTS_DIR = Path.home() / "1man.army" / "scripts"
LOG_FILE = SCRIPTS_DIR / "batch_log.txt"

# ✅ Tasks to auto-run in background batch
tasks = [
    "sentinel_agent.py",
    "alert_engine.py",
    "tactic_updater.py",
    "sabzi_analyzer.py",
    "memory_encryptor.py",
    "voice_cortex.py"
]

def log(message):
    with open(LOG_FILE, "a") as logf:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        logf.write(f"[{timestamp}] {message}\n")

def run_batch():
    log("CORTEX BATCH STARTED")
    for task in tasks:
        script_path = SCRIPTS_DIR / task
        if script_path.exists():
            try:
                subprocess.Popen(["python", str(script_path)], creationflags=subprocess.CREATE_NO_WINDOW)
                log(f"✔ Launched: {task}")
            except Exception as e:
                log(f"❌ Error launching {task}: {e}")
        else:
            log(f"⚠ Skipped (not found): {task}")
    log("CORTEX BATCH COMPLETE\n")

if __name__ == "__main__":
    run_batch()
    print("Cortex batch tasks initiated. Check logs for details.")
    