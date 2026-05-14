import sqlite3

def get_connection():
    conn = sqlite3.connect("ecommerce.db")
    return conn


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        username TEXT,
        email TEXT
    )
    """)

    conn.commit()
    conn.close()
