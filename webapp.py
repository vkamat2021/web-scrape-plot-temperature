import streamlit as st
import plotly.express as px
import sqlite3

# import pandas as pd. It is not used below

# Plot temperature v/s date from the sqlite db table and with streamlit plotly line chart.
# Plotly is better for charts
# Read date from DB.
with sqlite3.connect("data.db", timeout=10) as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT datetime, temperature FROM temperatures")
    rows = cursor.fetchall()
    # Data is returned as tuples hence converted to lists below
    datetime = []
    temperature = []
    for row in rows:
        datetime.append(row[0])
        temperature.append(float(row[1]))
# print(rows)
# Plot data
figure = px.line(x=datetime, y=temperature, labels={'x': 'DateTime', 'y': 'Temperature'})
st.plotly_chart(figure)
