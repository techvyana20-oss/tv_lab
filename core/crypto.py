from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_file(filepath, key):
    fernet = Fernet(key)
    with open(filepath, "rb") as f:
        data = f.read()
    encrypted = fernet.encrypt(data)
    with open(filepath, "wb") as f:
        f.write(encrypted)

def decrypt_file(filepath, key):
    fernet = Fernet(key)
    with open(filepath, "rb") as f:
        data = f.read()
    decrypted = fernet.decrypt(data)
    with open(filepath, "wb") as f:
        f.write(decrypted)
