import hashlib
import base64
import os
from logger import log_info

def hash_text(text, algorithm):
    h = hashlib.new(algorithm)
    h.update(text.encode())
    return h.digest()

def hash_file(path, algorithm):
    h = hashlib.new(algorithm)
    with open(path, "rb") as f:
        while chunk := f.read(4096):
            h.update(chunk)
    return h.digest()

def run(user):
    print("\n=== Advanced Hash Tool ===")

    print("1 - Hash Text")
    print("2 - Hash File")
    choice = input("Select: ")

    algorithm = input("Algorithm (sha256/md5/sha1): ").lower()

    if algorithm not in ["sha256", "md5", "sha1"]:
        print("Unsupported algorithm.")
        return

    if choice == "1":
        text = input("Enter text: ")
        raw = hash_text(text, algorithm)

    elif choice == "2":
        path = input("Enter file path: ")
        if not os.path.exists(path):
            print("File not found.")
            return
        raw = hash_file(path, algorithm)

    else:
        print("Invalid choice.")
        return

    hex_output = raw.hex()
    b64_output = base64.b64encode(raw).decode()

    print("\nHEX:", hex_output)
    print("Base64:", b64_output)

    log_info(f"{user} used hash tool ({algorithm})")
