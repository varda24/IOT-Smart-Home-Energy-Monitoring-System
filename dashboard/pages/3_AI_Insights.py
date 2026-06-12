
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

score = 87

fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=score,
    title={"text":"Energy Score"},
    gauge={
        "axis":{"range":[0,100]},
        "bar":{"color":"#06b6d4"}
    }
))

st.plotly_chart(fig, use_container_width=True)

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
    page_title="AI Insights",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Energy Advisor")

df = pd.read_csv("../data/energy_log.csv")

latest = df.iloc[-1]

cost = latest["Cost"]

predicted_bill = round(cost * 30, 2)

if predicted_bill < 300:
    score = 95
elif predicted_bill < 600:
    score = 80
elif predicted_bill < 1000:
    score = 65
else:
    score = 40

st.metric(
    "🏆 Energy Efficiency Score",
    f"{score}/100"
)

st.metric(
    "📈 Predicted Monthly Bill",
    f"₹ {predicted_bill}"
)

st.metric(
    "💰 Potential Savings",
    "₹ 120/month"
)

st.divider()

st.subheader("🤖 Smart Recommendations")

if score > 80:

    st.success("""
    Excellent energy efficiency.

    Recommendations:
    - Continue current usage pattern
    - Schedule appliance maintenance
    - Monitor peak-hour loads
    """)

elif score > 60:

    st.warning("""
    Moderate energy efficiency.

    Recommendations:
    - Reduce standby loads
    - Use energy-efficient appliances
    - Turn off unused devices
    """)

else:

    st.error("""
    High energy consumption detected.

    Recommendations:
    - Reduce AC usage
    - Replace old appliances
    - Shift heavy loads to off-peak hours
    """)

    st.markdown("---")

st.markdown("""
<div style='text-align:center;color:gray;'>

Smart Home Energy Monitoring Platform

Built using ESP32 • Wokwi • PlatformIO • Streamlit • Python

</div>
""", unsafe_allow_html=True)