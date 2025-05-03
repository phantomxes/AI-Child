from flask import Flask, request, jsonify, render_template
import subprocess
import pyttsx3
import os

app = Flask(__name__)
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# === ROUTES ===

@app.route("/")
def home():
    return jsonify({"status": "CORTEX ONLINE"})

@app.route("/scan", methods=["POST"])
def scan():
    subprocess.Popen(["python", "sentinel_agent.py"])
    speak("Scan started.")
    return jsonify({"status": "Scan triggered"})

@app.route("/voice", methods=["POST"])
def voice():
    subprocess.Popen(["python", "voice_cortex.py"])
    speak("Voice command system online.")
    return jsonify({"status": "Voice activated"})

@app.route("/alerts", methods=["POST"])
def alerts():
    subprocess.Popen(["python", "alert_engine.py"])
    speak("Alert engine activated.")
    return jsonify({"status": "Alerts triggered"})

@app.route("/memory", methods=["POST"])
def memory():
    subprocess.Popen(["python", "chroma_brain.py"])
    speak("Memory query online.")
    return jsonify({"status": "Memory brain loaded"})

@app.route("/speak", methods=["POST"])
def speak_api():
    msg = request.json.get("text", "")
    speak(msg)
    return jsonify({"spoken": msg})

@app.route("/panel")
def panel():
    return render_template("cortex_panel.html")

if __name__ == "__main__":
    from eventlet import wsgi
    import eventlet
    wsgi.server(eventlet.listen(('0.0.0.0', 5000)), app)
