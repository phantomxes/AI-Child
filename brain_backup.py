import zipfile, os
from pathlib import Path

SRC = Path.home() / "1man.army"
OUT = Path.home() / "Desktop" / "1manarmy_Backup.zip"

with zipfile.ZipFile(OUT, 'w') as zipf:
    for root, _, files in os.walk(SRC):
        for f in files:
            path = os.path.join(root, f)
            zipf.write(path, arcname=os.path.relpath(path, SRC))

print("🧠 Backup complete:", OUT)
