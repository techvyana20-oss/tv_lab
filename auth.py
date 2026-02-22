import hashlib
import sqlite3
from config import DB_NAME

def create_user(username, password, role):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    hashed = hashlib.sha256(password.encode()).hexdigest()
    c.execute("INSERT INTO users VALUES (?, ?, ?)", (username, hashed, role))
    conn.commit()
    conn.close()

def login(username, password):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    hashed = hashlib.sha256(password.encode()).hexdigest()
    c.execute("SELECT role FROM users WHERE username=? AND password=?", (username, hashed))
    result = c.fetchone()
    conn.close()
    return result[0] if result else None
