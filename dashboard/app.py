import streamlit as st

st.set_page_config(
    page_title="Smart Home Energy Platform",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
    background-color:#050B18;
}

section[data-testid="stSidebar"]{
    background-color:#111827;
}

.hero{
    background: linear-gradient(
        135deg,
        #2563EB,
        #06B6D4
    );
    padding:50px;
    border-radius:25px;
    color:white;
    box-shadow:0px 10px 40px rgba(0,0,0,0.4);
}

.feature-card{
    background:#0F172A;
    padding:25px;
    border-radius:18px;
    border:1px solid #1E293B;
    min-height:220px;
}

.metric-card{
    background:#0F172A;
    padding:25px;
    border-radius:18px;
    text-align:center;
    border:1px solid #1E293B;
}

.device-card{
    background:#0F172A;
    padding:18px;
    border-radius:12px;
    margin-bottom:10px;
}

.status-online{
    background:#14532d;
    color:#4ade80;
    padding:12px;
    border-radius:10px;
}

.status-offline{
    background:#4c1d1d;
    color:#f87171;
    padding:12px;
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================

with st.sidebar:

    st.markdown("## 🏠 Smart Home")

    st.success("🟢 System Online")

    st.markdown("---")

    st.markdown("### ⚡ Live Energy Monitoring")
    st.markdown("### 📊 Analytics Dashboard")
    st.markdown("### 🤖 AI Energy Advisor")
    st.markdown("### 📄 Smart Reports")
    st.markdown("### 🏠 Device Monitoring")
    st.markdown("### 🌱 Carbon Tracking")

    st.markdown("---")

    st.markdown("### 💡 Smart Home Status")

    st.success("System Online")

# =========================
# HERO SECTION
# =========================

st.markdown("""
<div class="hero">

<h1>⚡ Smart Home Energy Platform</h1>

<h3>Monitor • Analyze • Predict • Optimize</h3>

<br>

Industry-grade IoT Energy Management Platform powered by
ESP32, AI Analytics, Smart Reporting and Sustainability Tracking.

</div>
""", unsafe_allow_html=True)

st.write("")

# =========================
# KPI CARDS
# =========================

col1,col2,col3,col4 = st.columns(4)

cards = [
    ("⚡","230V","Voltage"),
    ("🔥","1766W","Power"),
    ("💰","₹845","Monthly Bill"),
    ("🏆","87/100","Efficiency")
]

for col,card in zip([col1,col2,col3,col4],cards):

    icon,value,title = card

    with col:
        st.markdown(f"""
        <div class="metric-card">
            <h1>{icon}</h1>
            <h2>{value}</h2>
            <p>{title}</p>
        </div>
        """, unsafe_allow_html=True)

st.write("")

# =========================
# FEATURES
# =========================

st.markdown("## 🚀 Platform Features")

c1,c2,c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="feature-card">

    <h3>⚡ Real-Time Monitoring</h3>

    Monitor Voltage, Current,
    Power and Energy Consumption
    in Real Time.

    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="feature-card">

    <h3>🤖 AI Energy Advisor</h3>

    Predict Bills, Detect Wastage
    and Recommend Optimizations.

    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="feature-card">

    <h3>📄 Smart Reports</h3>

    Generate PDF Reports,
    CSV Exports and Analytics.

    </div>
    """, unsafe_allow_html=True)

st.write("")

c4,c5 = st.columns(2)

with c4:
    st.markdown("""
    <div class="feature-card">

    <h3>🏠 Appliance Monitoring</h3>

    Monitor Individual Device
    Consumption and Identify
    Power Hungry Appliances.

    </div>
    """, unsafe_allow_html=True)

with c5:
    st.markdown("""
    <div class="feature-card">

    <h3>🌱 Carbon Footprint Tracking</h3>

    Monitor Environmental Impact,
    CO₂ Emissions and Sustainability.

    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# =========================
# SMART HOME COMMAND CENTER
# =========================

st.markdown("## 🏠 Smart Home Command Center")

left,right = st.columns(2)

with left:

    st.markdown("""
    <div class="status-online">
    💡 Living Room Lights Active
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="status-online">
    📺 Smart TV Active
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="status-online">
    📶 WiFi Router Online
    </div>
    """, unsafe_allow_html=True)

with right:

    st.markdown("""
    <div class="status-online">
    ⚡ Refrigerator Running
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="status-offline">
    ❄ Air Conditioner Offline
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="status-online">
    🖥 Workstation Active
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# =========================
# PLATFORM OVERVIEW
# =========================

st.markdown("## 📈 Platform Overview")

col1,col2,col3 = st.columns(3)

with col1:
    st.info("""
    🔌 ESP32 Powered

    Real-time IoT monitoring
    using simulated smart sensors.
    """)

with col2:
    st.info("""
    🧠 AI Analytics

    Smart prediction and
    optimization engine.
    """)

with col3:
    st.info("""
    🌍 Sustainability

    Carbon footprint and
    environmental impact tracking.
    """)

st.write("")
st.write("")

# =========================
# TECH STACK
# =========================

st.markdown("## 🛠 Technology Stack")

st.code("""
ESP32
Wokwi Simulation
PlatformIO
Python
Streamlit
Plotly
ReportLab
Machine Learning
IoT Analytics
""")

st.success(
    "🚀 Navigate using the sidebar to explore Dashboard, Analytics, AI Insights, Reports, Device Monitoring and Carbon Tracking."
)