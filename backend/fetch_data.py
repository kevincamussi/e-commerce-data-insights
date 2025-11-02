import requests
from typing import Any, Dict, List
from db import get_connection, create_table

create_table()

url: str = "https://fakestoreapi.com/products"
response = requests.get(url)
data: List[Dict[str, Any]] = response.json()

conn = get_connection()
cursor = conn.cursor()

cursor.execute("DELETE FROM products")

for item in data:
    profit: float = item["price"] * 0.25
    profit_margin: float = 25

    cursor.execute("""
    INSERT INTO products (id, title, category, price, rating_rate, rating_count, profit, profit_margin)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        int(item["id"]),
        str(item["title"]),
        str(item["category"]),
        float(item["price"]),
        float(item["rating"]["rate"]),
        int(item["rating"]["count"]),
        float(profit),
        float(profit_margin)
    ))

conn.commit()
conn.close()
print("✅ API data saved succesfully in SQLite.")