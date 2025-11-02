import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="E-Commerce Insights", page_icon="🛍️", layout="wide")

st.title("🛒 E-Commerce Data Insights Dashboard")

df = pd.read_csv("exports/clean_data.csv")

categories = st.multiselect("Select categories:", df["category"].unique(), default=df["category"].unique())
filtered = df[df["category"].isin(categories)]

col1, col2, col3 = st.columns(3)
col1.metric("Products", len(filtered))
col2.metric("Average Price", f"${filtered['price'].mean():.2f}")
col3.metric("Total Profit", f"${filtered['adjusted_profit'].sum():,.2f}")

tab1, tab2 = st.tabs(["📈 Price and Profit", "⭐ Reviews"])

with tab1:
    fig = px.bar(filtered, x="title", y="price", color="profit", title="Price x Profit by Product")
    st.plotly_chart(fig, width="stretch")

with tab2:
    fig2 = px.scatter(filtered, x="price", y="rating_rate", size="rating_count", color="category", title="Price vs Review by Category")
    st.plotly_chart(fig2, width="stretch")