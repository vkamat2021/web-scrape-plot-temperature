import streamlit as st
import pandas as pd

# Plot temperature v/s date from the data.txt file using pandas and streamlit native line chart.
# Plotly is better for charts
df = pd.read_csv('data.txt')
# print(df)
st.line_chart(df, x='date', y='temperature')