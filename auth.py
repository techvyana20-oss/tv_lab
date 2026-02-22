import hashlib
import sqlite3
from config import DB_NAME

def create_user(username, password, role):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    hashed = hashlib.sha256(password.encode()).hexdigest()

    try:
        c.execute("INSERT INTO users VALUES (?, ?, ?)", (username, hashed, role))
        conn.commit()
        print("User created successfully.")
    except sqlite3.IntegrityError:
        print("Username already exists. Please choose another.")
    finally:
        conn.close()

def login(username, password):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    hashed = hashlib.sha256(password.encode()).hexdigest()

    c.execute("SELECT role FROM users WHERE username=? AND password=?", (username, hashed))
    result = c.fetchone()

    conn.close()

    if result:
        return result[0]
    return None
