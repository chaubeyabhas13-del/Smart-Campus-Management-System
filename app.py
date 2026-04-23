import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Page settings
st.set_page_config(page_title="Smart Campus Dashboard", layout="wide")

# --------- CUSTOM STYLE ----------
st.markdown("""
<style>
body {
    background: linear-gradient(to right, #1f0036, #3b0a45);
    color: white;
}
h1, h2, h3 {
    color: white;
}
</style>
""", unsafe_allow_html=True)

# --------- TITLE ----------
st.title("🏫 SMART CAMPUS MANAGEMENT DASHBOARD")

# --------- DATA ----------
data = pd.DataFrame({
    "hour": list(range(24)),
    "energy": [12,15,13,20,22,25,30,35,40,38,32,30,28,25,22,20,18,16,14,12,11,10,9,8],
    "water": [80,78,75,72,70,68,65,62,60,58,55,52,50,48,45,42,40,38,35,32,30,28,27,25],
    "classroom": [10,12,15,20,25,30,35,40,45,50,48,46,44,42,40,38,35,30,25,20,18,15,12,10],
    "parking": [5,6,8,10,15,20,25,30,35,40,38,36,34,32,30,28,25,20,18,15,12,10,8,6]
})

# --------- SIDEBAR FILTER ----------
st.sidebar.header("⚙ Filters")
selected_hour = st.sidebar.slider("Select Hour", 0, 23, 12)

# --------- KPIs ----------
st.markdown("## 📌 Key Metrics")

k1, k2, k3, k4 = st.columns(4)

k1.metric("Total Energy (kWh)", int(data["energy"].sum()))
k2.metric("Peak Hour", int(data.loc[data["energy"].idxmax(), "hour"]))
k3.metric("Max Classroom Occupancy", int(data["classroom"].max()))
k4.metric("Max Parking Usage", int(data["parking"].max()))

# --------- GRAPHS ----------
st.markdown("## 📊 Analytics Dashboard")

col1, col2 = st.columns(2)

# Energy
with col1:
    st.subheader("⚡ Energy Consumption by Hour")
    fig, ax = plt.subplots()
    ax.plot(data["hour"], data["energy"], color="red", linewidth=3)
    ax.set_xlabel("Hour")
    ax.set_ylabel("Energy (kWh)")
    st.pyplot(fig)

# Water
with col2:
    st.subheader("💧 Water Level Monitoring")
    fig, ax = plt.subplots()
    ax.plot(data["hour"], data["water"], color="blue", linewidth=3)
    ax.set_xlabel("Hour")
    ax.set_ylabel("Water Level (%)")
    st.pyplot(fig)

col3, col4 = st.columns(2)

# Classroom
with col3:
    st.subheader("🏫 Classroom Occupancy")
    fig, ax = plt.subplots()
    ax.fill_between(data["hour"], data["classroom"], color="cyan")
    ax.set_xlabel("Hour")
    ax.set_ylabel("Students")
    st.pyplot(fig)

# Parking
with col4:
    st.subheader("🚗 Parking Usage")
    fig, ax = plt.subplots()
    ax.bar(data["hour"], data["parking"], color="purple")
    ax.set_xlabel("Hour")
    ax.set_ylabel("Vehicles")
    st.pyplot(fig)

# --------- COMBINED BAR ----------
st.markdown("## 📊 Combined Analysis")

fig, ax = plt.subplots(figsize=(10,5))
ax.barh(data["hour"], data["classroom"], color="orange", label="Classroom")
ax.barh(data["hour"], data["parking"], color="green", alpha=0.6, label="Parking")
ax.set_xlabel("Count")
ax.set_ylabel("Hour")
ax.legend()
st.pyplot(fig)

# --------- LINEAR REGRESSION (PREDICTION) ----------
st.markdown("## 🤖 Prediction (Linear Regression)")

X = data[["hour"]]
y = data["energy"]

model = LinearRegression()
model.fit(X, y)

future_hour = st.slider("Select Future Hour for Prediction", 0, 30, 25)

prediction = model.predict([[future_hour]])

st.success(f"Predicted Energy at hour {future_hour}: {prediction[0]:.2f} kWh")

# --------- FOOTER ----------
st.markdown("---")
st.write("Developed by Abhas Chaubey 🚀")
