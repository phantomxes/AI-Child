import subprocess
import threading
import time

def run_script(path):
    subprocess.Popen(["python", path])

def trigger_scan():
    print("[🔁] Triggering Sentinel Scan...")
    run_script("sentinel_agent.py")

def trigger_voice():
    print("[🎙️] Activating Voice Cortex...")
    run_script("voice_cortex.py")

def trigger_ui():
    print("[🖥️] Launching Cortex UI...")
    run_script("cortex_ui.py")

def trigger_brain():
    print("[🧠] Query Mode: Chroma Brain")
    run_script("chroma_brain.py")

if __name__ == "__main__":
    print("=== Relay Engine Online ===")
    while True:
        print("\n[1] Scan\n[2] Voice\n[3] Cortex UI\n[4] Ask Memory\n[5] Exit")
        choice = input("⚙️ Select: ")

        if choice == "1": trigger_scan()
        elif choice == "2": trigger_voice()
        elif choice == "3": trigger_ui()
        elif choice == "4": trigger_brain()
        elif choice == "5": break
        else: print("Invalid.")
