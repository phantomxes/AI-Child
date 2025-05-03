import json
import os
from datetime import datetime

LOG_FILE = "logs/game_history.json"

def init_log():
    """
    Ensure the log file exists.
    """
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            json.dump([], f)

def log_round(result, payout, multiplier, scatter_count):
    """
    Save details of one spin into the log file.
    Keeps only last 100 entries.
    """
    init_log()

    with open(LOG_FILE, "r") as f:
        try:
            data = json.load(f)
        except:
            data = []

    entry = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "result": result,
        "payout": payout,
        "multiplier": multiplier,
        "scatter": scatter_count
    }

    data.append(entry)

    with open(LOG_FILE, "w") as f:
        json.dump(data[-100:], f, indent=2)

    print(f"🧠 LOGGED: {entry}")

def get_trend():
    """
    Analyze the last 10 spins to detect hot mode and average behavior.
    """
    init_log()

    with open(LOG_FILE, "r") as f:
        try:
            data = json.load(f)
        except:
            return {
                "scatter_frequency": 0,
                "avg_payout": 0,
                "hot_mode": False
            }

    recent = data[-10:]
    scatter_hits = sum(1 for x in recent if x["scatter"] >= 3)
    avg_payout = sum(x["payout"] for x in recent) / len(recent) if recent else 0

    hot_mode = scatter_hits >= 3 or avg_payout > 10

    return {
        "scatter_frequency": scatter_hits,
        "avg_payout": avg_payout,
        "hot_mode": hot_mode
    }
