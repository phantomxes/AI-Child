import pyautogui

def detect_glow_color(glow_rgb=(0, 255, 255), region=(700, 400, 500, 300)):
    """
    Detects if a specific glow color exists in a screen region.
    Default color: aqua/cyan (0, 255, 255)
    """
    screenshot = pyautogui.screenshot(region=region)

    for x in range(screenshot.width):
        for y in range(screenshot.height):
            if screenshot.getpixel((x, y)) == glow_rgb:
                print(f"✨ Glow Detected at ({x}, {y})")
                return True
    return False

# Test Run
if __name__ == "__main__":
    result = detect_glow_color()
    if result:
        print("🎉 Confirmed: WIN Glow Present")
    else:
        print("❌ No Glow Detected")
