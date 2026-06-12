import streamlit as st
import plotly.express as px
import pandas as pd

st.title("🏠 Appliance Energy Monitoring")

devices = {
    "Air Conditioner": 1200,
    "Refrigerator": 350,
    "TV": 180,
    "Lights": 120,
    "WiFi Router": 25
}

df = pd.DataFrame({
    "Device": devices.keys(),
    "Power": devices.values()
})

st.subheader("Current Device Consumption")

st.dataframe(df, use_container_width=True)

fig = px.pie(
    df,
    names="Device",
    values="Power",
    hole=0.5,
    title="Power Distribution"
)

st.plotly_chart(fig, use_container_width=True)

top_device = max(devices, key=devices.get)

st.success(
    f"Highest Consumer: {top_device} ({devices[top_device]} W)"
)