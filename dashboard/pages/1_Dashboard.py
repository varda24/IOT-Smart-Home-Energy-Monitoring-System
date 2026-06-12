


import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from streamlit_autorefresh import st_autorefresh

st.markdown("""
<div style="
background:#16a34a;
padding:15px;
border-radius:12px;
text-align:center;
font-weight:bold;
color:white;
">
🟢 SYSTEM ONLINE | Monitoring Active | AI Analytics Running
</div>
""", unsafe_allow_html=True)

with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/1048/1048953.png",
        width=80
    )

    st.title("Smart Home")

    st.success("System Online")

    st.markdown("---")

    st.write("⚡ Live Monitoring")
    st.write("📊 Analytics")
    st.write("🤖 AI Advisor")
    st.write("📄 Reports")


st.set_page_config(
    page_title="Dashboard",
    page_icon="⚡",
    layout="wide"
)

st_autorefresh(interval=5000, key="refresh")

# Load Data
df = pd.read_csv("../data/energy_log.csv")
latest = df.iloc[-1]

voltage = latest["Voltage"]
current = latest["Current"]
power = latest["Power"]
energy = latest["Energy"]
cost = latest["Cost"]
status = latest["Status"]

# Hero Section
st.markdown("""
# ⚡ Smart Home Energy Command Center

Real-Time Monitoring & Energy Optimization
""")

# KPI Cards
c1, c2, c3, c4, c5 = st.columns(5)

c1.metric("Voltage", f"{voltage} V")
c2.metric("Current", f"{current} A")
c3.metric("Power", f"{power} W")
c4.metric("Energy", f"{energy:.4f} kWh")
c5.metric("Cost", f"₹ {cost}")

# Alert Banner
if power > 1500:
    st.error("🚨 High Energy Consumption Detected")
else:
    st.success("✅ Energy Consumption Normal")

left, right = st.columns([2, 1])

# Power Gauge
with left:

    gauge = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=power,
            title={"text": "Power Usage (W)"},
            gauge={
                "axis": {"range": [0, 3000]},
                "bar": {"color": "#ff9800"},
                "steps": [
                    {"range": [0, 1000], "color": "green"},
                    {"range": [1000, 2000], "color": "yellow"},
                    {"range": [2000, 3000], "color": "red"},
                ],
            },
        )
    )

    st.plotly_chart(gauge, use_container_width=True)

# Smart Home Status
with right:

    st.subheader("🏠 Smart Home")

    st.success("💡 Living Room Light ON")
    st.success("📺 TV ON")
    st.success("🧊 Refrigerator ON")
    st.error("❄ Air Conditioner OFF")
    st.success("📶 WiFi Router ON")

# Energy Score
st.subheader("🏆 Energy Efficiency Score")

if power < 700:
    score = 95
elif power < 1500:
    score = 80
elif power < 2200:
    score = 60
else:
    score = 35

st.progress(score)
st.write(f"Score: {score}/100")

st.markdown("---")

st.markdown("""
<div style='text-align:center;color:gray;'>

Smart Home Energy Monitoring Platform

Built using ESP32 • Wokwi • PlatformIO • Streamlit • Python

</div>
""", unsafe_allow_html=True)