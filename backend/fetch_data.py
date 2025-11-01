import requests
from db import get_connection, create_table

create_table()

url = "https://fakestoreapi.com/products"
response = requests.get(url)
data = response.json()

conn = get_connection()
cursor = conn.cursor()

cursor.execute("DELETE FROM products")

for item in data:
    profit = item["price"] * 0.25
    profit_margin = 25

    cursor.execute("""
    INSERT INTO products (id, title, category, price, rating_rate, rating_count, profit, profit_margin)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        item["id"],
        item["title"],
        item["category"],
        item["price"],
        item["rating"]["rate"],
        item["rating"]["count"],
        profit,
        profit_margin
    ))

conn.commit()
conn.close()
print("✅ API data saved succesfully in SQLite.")