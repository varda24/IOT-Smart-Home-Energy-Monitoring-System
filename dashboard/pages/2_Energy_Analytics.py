
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parents[2]
csv_file = BASE_DIR / "data" / "energy_log.csv"

df = pd.read_csv(csv_file)

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
    page_title="Energy Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Energy Analytics Center")

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

csv_file = BASE_DIR / "data" / "energy_log.csv"

df = pd.read_csv(csv_file)
# -----------------------------
# SUMMARY CARDS
# -----------------------------

total_energy = df["Energy"].max()
avg_power = round(df["Power"].mean(), 2)
max_power = round(df["Power"].max(), 2)
total_cost = round(df["Cost"].max(), 2)

c1, c2, c3, c4 = st.columns(4)

c1.metric("⚡ Total Energy", f"{total_energy:.4f} kWh")
c2.metric("🔥 Avg Power", f"{avg_power} W")
c3.metric("🚀 Peak Power", f"{max_power} W")
c4.metric("💰 Total Cost", f"₹ {total_cost}")

st.divider()

# -----------------------------
# POWER TREND
# -----------------------------

left, right = st.columns(2)

with left:

    fig1 = px.line(
        df,
        x="Timestamp",
        y="Power",
        title="⚡ Power Consumption Trend",
        markers=True
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

with right:

    fig2 = px.line(
        df,
        x="Timestamp",
        y="Cost",
        title="💰 Cost Trend",
        markers=True
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

# -----------------------------
# ENERGY AREA CHART
# -----------------------------

fig3 = px.area(
    df,
    x="Timestamp",
    y="Energy",
    title="🔋 Energy Consumption Growth"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# -----------------------------
# DONUT CHART
# -----------------------------

st.subheader("🏠 Appliance Power Distribution")

appliance_data = pd.DataFrame({
    "Appliance": [
        "Refrigerator",
        "Fan",
        "TV",
        "WiFi Router",
        "Lighting"
    ],
    "Usage": [
        35,
        20,
        15,
        10,
        20
    ]
})

fig4 = px.pie(
    appliance_data,
    names="Appliance",
    values="Usage",
    hole=0.65,
    title="Power Distribution"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

# -----------------------------
# STATUS ANALYSIS
# -----------------------------

st.subheader("📈 Usage Categories")

status_counts = df["Status"].value_counts()

fig5 = px.bar(
    x=status_counts.index,
    y=status_counts.values,
    labels={
        "x":"Status",
        "y":"Count"
    },
    title="Energy Usage Status Distribution"
)

st.plotly_chart(
    fig5,
    use_container_width=True
)

st.markdown("---")

st.markdown("""
<div style='text-align:center;color:gray;'>

Smart Home Energy Monitoring Platform

Built using ESP32 • Wokwi • PlatformIO • Streamlit • Python

</div>
""", unsafe_allow_html=True)