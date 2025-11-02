import pandas as pd
from pandas import DataFrame
import sqlite3

def load_data() -> DataFrame:
    conn: sqlite3.Connection = sqlite3.connect("ecommerce.db")
    df: DataFrame = pd.read_sql_query("SELECT * FROM products", conn)
    
    conn.close()
    return df

def transform_data(df: DataFrame) -> DataFrame:
    df["total_value"] = df["price"] * df["rating_count"]
    df["adjusted_profit"] = df["profit"] * (df["rating_rate"] / 5)
    return df

def export_to_csv(df: DataFrame, path: str="exports/clean_data.csv") -> None:
    df.to_csv(path, index=False)
    print(f"✅ Data processed and exported to {path}")

if __name__ == "__main__":
    df = load_data()
    df = transform_data(df)
    export_to_csv(df)
    
