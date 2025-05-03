import os
import tkinter as tk
from tkinter import messagebox
import subprocess

# Paths to core modules
MODULES = {
    "Start AI Engine": "main_engine.py",
    "Glow Detection Test": "glow_detector.py",
    "Voice Test": "voice_alert.py",
    "Trainer Log Reader": "trainer_engine.py",
    "Bet Optimizer": "bet_optimizer.py"
}

def run_module(module_name):
    script = MODULES[module_name]
    try:
        subprocess.Popen(["python", script], shell=True)
        print(f"🚀 Running: {script}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run {script}:\n{e}")

def build_gui():
    root = tk.Tk()
    root.title("🎮 1ManArmy AI - Mission Control Panel")
    root.geometry("400x400")
    root.configure(bg="black")

    title = tk.Label(root, text="AI Mission Control", font=("Consolas", 18, "bold"), fg="lime", bg="black")
    title.pack(pady=20)

    for module in MODULES:
        btn = tk.Button(root, text=module, width=30, font=("Consolas", 12), fg="white", bg="#222", command=lambda m=module: run_module(m))
        btn.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    build_gui()
    print("🚀 1ManArmy AI Mission Control UI Initialized")