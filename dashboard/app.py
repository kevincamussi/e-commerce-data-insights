import streamlit as st
import pandas as pd
from pandas import DataFrame
import plotly.express as px
from plotly.graph_objs import Figure
from typing import List

def load_csv(path: str = "exports/clean_data.csv") -> DataFrame:
    return pd.read_csv(path)

def create_price_profit_chart(df: DataFrame) -> Figure:
    return px.bar(df, x="title", y="price", color="profit", title="Price x Profit by Product ")

def create_rating_chart(df: DataFrame) -> Figure:
    return px.scatter(df, x ="price", y="rating_rate", size="rating_count",color="category", title="Price x Review by Category")

st.set_page_config(page_title="E-Commerce Insights", page_icon="🛍️", layout="wide")
st.title("🛒 E-Commerce Data Insights Dashboard")

df: DataFrame = load_csv()
categories: List[str] = st.multiselect("Selecione categorias:", df["category"].unique().tolist(), default=df["category"].unique().tolist())
filtered: DataFrame = df[df["category"].isin(categories)]

col1, col2, col3 = st.columns(3)
col1.metric("Produtos", len(filtered))
col2.metric("Preço Médio", f"${filtered['price'].mean():.2f}")
col3.metric("Lucro Total", f"${filtered['adjusted_profit'].sum():,.2f}")

tab1, tab2 = st.tabs(["📈 Preço e Lucro", "⭐ Avaliações"])
with tab1:
    st.plotly_chart(create_price_profit_chart(filtered), width='stretch')
with tab2:
    st.plotly_chart(create_rating_chart(filtered), width='stretch')