import pandas as pd
import sqlite3

conn = sqlite3.connect("ecommerce.db")
df = pd.read_sql_query("SELECT * FROM products", conn)
conn.close()

df["total_value"] =  df["price"] * df["rating_count"]
df["adjusted_profit"] = df["profit"] * (df["rating_rate"] / 5)

df.to_csv("exports/clean_data.csv", index = False)
print("✅ Data processed and exported to exports/clean_data.csv")