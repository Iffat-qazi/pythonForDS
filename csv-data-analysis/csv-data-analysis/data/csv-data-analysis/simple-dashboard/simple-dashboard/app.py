import pandas as pd
import streamlit as st

st.title("Sales Dashboard")


df = pd.read_csv("../csv-data-analysis/salesData.csv")

st.subheader("Raw Data")
st.dataframe(df.head())

st.subheader("Sales by Category")
category_sales = df.groupby("Category")["Sales"].sum()
st.bar_chart(category_sales)

st.subheader("Monthly Sales Trend")
df["Order Date"] = pd.to_datetime(df["Order Date"])
monthly_sales = df.groupby(df["Order Date"].dt.month)["Sales"].sum()
st.line_chart(monthly_sales)
