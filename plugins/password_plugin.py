import secrets
import string
from core.entropy import calculate_entropy
from logger import log_info

def run(user):
    print("\n=== Secure Password Research Tool ===")

    length = int(input("Password length: "))
    count = int(input("How many passwords to generate: "))

    use_symbols = input("Include symbols? (y/n): ").lower() == "y"

    charset = string.ascii_letters + string.digits
    if use_symbols:
        charset += "!@#$%^&*"

    entropy = calculate_entropy(len(charset), length)

    print(f"\nCharset size: {len(charset)}")
    print(f"Entropy per password: {round(entropy,2)} bits\n")

    with open("generated_passwords.txt", "a") as f:
        for i in range(count):
            pwd = ''.join(secrets.choice(charset) for _ in range(length))
            print(f"{i+1}: {pwd}")
            f.write(pwd + "\n")

    log_info(f"{user} generated {count} passwords (length={length})")

    print("\nSaved to generated_passwords.txt")
