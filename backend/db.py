import sqlite3
from sqlite3 import Connection, Cursor

def get_connection() -> Connection:
    conn = sqlite3.connect("ecommerce.db")
    return conn

def create_table() -> None:
    conn: Connection = get_connection()
    cursor: Cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        title TEXT,
        category TEXT,
        price REAL,
        rating_rate REAL,
        rating_count INTEGER,
        profit REAL,
        profit_margin REAL
    )
    """)
    conn.commit()
    conn.close()
    print("✅ Table created (or already exists).")