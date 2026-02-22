import hashlib

def run(user):
    text = input("Enter text: ")
    print("SHA256:", hashlib.sha256(text.encode()).hexdigest())
    print("MD5:", hashlib.md5(text.encode()).hexdigest())
