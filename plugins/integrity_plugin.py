import hashlib

def run(user):
    path = input("File path: ")
    with open(path, "rb") as f:
        data = f.read()
    print("SHA256:", hashlib.sha256(data).hexdigest())
