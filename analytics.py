import sqlite3
from config import DB_NAME

def show_analytics():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT tool, COUNT(*) FROM activity GROUP BY tool")
    results = c.fetchall()
    conn.close()

    print("\n=== Tool Usage Analytics ===")
    for tool, count in results:
        print(f"{tool}: {count} runs")
