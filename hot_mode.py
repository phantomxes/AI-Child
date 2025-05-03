import time
import pyautogui
import random

def hot_mode_boost():
    print("🔥 HOT MODE ACTIVATED")
    boost_count = random.randint(3, 7)
    for i in range(boost_count):
        pyautogui.moveTo(1000 + i * 5, 600)
        pyautogui.click()
        print(f"⚡ Boost Spin {i+1}")
        time.sleep(0.8)

if __name__ == "__main__":
    hot_mode_boost()
