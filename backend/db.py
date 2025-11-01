import sqlite3

def get_connection():
    conn = sqlite3.connect("ecommerce.db")
    return conn

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
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