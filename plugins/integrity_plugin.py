import hashlib
import os
from logger import log_info

def calculate_hash(filepath, algorithm="sha256"):
    h = hashlib.new(algorithm)
    with open(filepath, "rb") as f:
        while chunk := f.read(4096):
            h.update(chunk)
    return h.hexdigest()

def run(user):
    print("\n=== File Integrity Verification Tool ===")

    path = input("Enter file path: ")

    if not os.path.exists(path):
        print("File not found.")
        return

    size = os.path.getsize(path)

    sha256_hash = calculate_hash(path, "sha256")
    md5_hash = calculate_hash(path, "md5")

    print("\nFile Size:", size, "bytes")
    print("SHA256:", sha256_hash)
    print("MD5   :", md5_hash)

    verify = input("\nDo you want to verify against known SHA256? (y/n): ")

    if verify.lower() == "y":
        known = input("Enter expected SHA256: ")
        if known == sha256_hash:
            print("✅ Hash matches. File integrity verified.")
        else:
            print("❌ Hash mismatch. File may be modified.")

    log_info(f"{user} checked integrity of {path}")
