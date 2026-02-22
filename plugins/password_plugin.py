import secrets
import string
from core.entropy import calculate_entropy

def run(user):
    length = int(input("Password length: "))
    charset = string.ascii_letters + string.digits + "!@#$%^&*"
    pwd = ''.join(secrets.choice(charset) for _ in range(length))
    entropy = calculate_entropy(len(charset), length)

    print("Generated:", pwd)
    print("Entropy:", round(entropy,2), "bits")
