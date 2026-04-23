import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.set_page_config(page_title="Smart Campus Dashboard", layout="wide")

st.title("🏫 Smart Campus Management Dashboard")

# Load data
data = pd.DataFrame({
    "hour": list(range(24)),
    "energy": [12,15,13,20,22,25,30,35,40,38,32,30,28,25,22,20,18,16,14,12,11,10,9,8],
    "water": [80,78,75,72,70,68,65,62,60,58,55,52,50,48,45,42,40,38,35,32,30,28,27,25],
    "classroom": [10,12,15,20,25,30,35,40,45,50,48,46,44,42,40,38,35,30,25,20,18,15,12,10],
    "parking": [5,6,8,10,15,20,25,30,35,40,38,36,34,32,30,28,25,20,18,15,12,10,8,6]
})

# Layout
col1, col2 = st.columns(2)

# Energy Graph
with col1:
    st.subheader("⚡ Energy Consumption")
    st.line_chart(data.set_index("hour")["energy"])

# Water Graph
with col2:
    st.subheader("💧 Water Level")
    st.line_chart(data.set_index("hour")["water"])

col3, col4 = st.columns(2)

# Classroom
with col3:
    st.subheader("🏫 Classroom Occupancy")
    st.area_chart(data.set_index("hour")["classroom"])

# Parking
with col4:
    st.subheader("🚗 Parking Usage")
    st.bar_chart(data.set_index("hour")["parking"])

# KPIs
st.markdown("## 📌 Key Metrics")
k1, k2, k3, k4 = st.columns(4)

k1.metric("Total Energy", data["energy"].sum())
k2.metric("Peak Hour", data["hour"][data["energy"].idxmax()])
k3.metric("Max Classroom", data["classroom"].max())
k4.metric("Max Parking", data["parking"].max())
