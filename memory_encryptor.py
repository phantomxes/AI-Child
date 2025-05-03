import os
from cryptography.fernet import Fernet
from pathlib import Path
import json
import getpass

BASE = Path.home() / "1man.army" / "memory"
SRC = BASE / "experience_log.json"
ENC = BASE / "experience_log.enc"
KEY_FILE = BASE / "vault.key"

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    return key

def load_key():
    if not KEY_FILE.exists():
        return generate_key()
    with open(KEY_FILE, "rb") as f:
        return f.read()

def encrypt_file():
    key = load_key()
    fernet = Fernet(key)
    with open(SRC, "rb") as f:
        data = f.read()
    encrypted = fernet.encrypt(data)
    with open(ENC, "wb") as f:
        f.write(encrypted)
    os.remove(SRC)
    print("[🔐] Memory encrypted successfully.")

def decrypt_file():
    key = load_key()
    fernet = Fernet(key)
    with open(ENC, "rb") as f:
        encrypted = f.read()
    decrypted = fernet.decrypt(encrypted)
    with open(SRC, "wb") as f:
        f.write(decrypted)
    print("[🔓] Memory decrypted and ready.")

if __name__ == "__main__":
    print("🔐 Memory Vault")
    action = input("Type 'lock' to encrypt or 'unlock' to decrypt: ").strip().lower()

    if action == "lock":
        encrypt_file()
    elif action == "unlock":
        decrypt_file()
    else:
        print("[✖] Invalid command.")
