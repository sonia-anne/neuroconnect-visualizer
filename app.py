# neuroconnect_dashboard/app.py

import streamlit as st
import pydeck as pdk
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Page Configuration
st.set_page_config(page_title="NeuroConnect: Scientific Dashboard", layout="wide")

# Dark Theme Styling
st.markdown("""
<style>
body, .stApp {
    background-color: #0d1117;
    color: white;
    font-family: 'Roboto Mono', monospace;
}
h1, h2, h3, h4, h5, h6, p, span, div {
    color: white !important;
}
.plot-container, .element-container {
    background-color: #0d1117 !important;
    border: none !important;
}
</style>
""", unsafe_allow_html=True)

st.title("🚀 NeuroConnect: Global Scientific Visualization Platform")

# ------------------------------------------------------------------------------
# 📆 Life Cycle Timeline: From Activation to Self-Destruction
# ------------------------------------------------------------------------------
st.subheader("📆 Life Cycle Timeline: From Activation to Self-Destruction")

lifecycle_info = pd.DataFrame({
    "Phase": [
        "1. Nasal Activation",
        "2. Cerebral Arrival",
        "3. Synaptic Evaluation",
        "4. Adaptive Release",
        "5. Full Operation Cycle",
        "6. Self-Destruction"
    ],
    "Time Estimate": [
        "Day 0",
        "Minute 2",
        "Hour 1",
        "Days 3–7",
        "Weeks 1–8",
        "Year 10 or upon host death"
    ],
    "Description": [
        "Insertion via nasal cavity and activation by brain pH.",
        "Crosses cribriform plate avoiding vital structures.",
        "Piezoelectric sensors analyze neuronal activity.",
        "Releases BDNF/VEGF based on AI-guided analysis.",
        "Continuous modulation to emotional and circadian states.",
        "Biodegrades safely post-mission or after death."
    ]
})

fig_lifecycle = go.Figure(data=[go.Table(
    header=dict(values=list(lifecycle_info.columns),
                fill_color='#1f2937',
                align='left',
                font=dict(color='white', size=13)),
    cells=dict(values=[lifecycle_info[col] for col in lifecycle_info.columns],
               fill_color='#111827',
               align='left',
               font=dict(color='white', size=12))
)])
fig_lifecycle.update_layout(title="🧬 NeuroConnect Device Lifecycle Timeline", paper_bgcolor='#0d1117')
st.plotly_chart(fig_lifecycle, use_container_width=True)

# ------------------------------------------------------------------------------
# 🧠 Radar Chart 4D: Clinical Effectiveness
# ------------------------------------------------------------------------------
st.subheader("🧠 Clinical Effectiveness: NeuroConnect vs Traditional Therapies")

categories = ['Communication', 'Sensory Regulation', 'Side Effects (Inverted)']
data = {
    'Therapy': ['NeuroConnect', 'ABA', 'Pharmacotherapy'],
    'Communication': [85, 40, 30],
    'Sensory Regulation': [78, 35, 20],
    'Side Effects (Inverted)': [95, 32, 15]
}
radar_df = pd.DataFrame(data)

fig_radar = go.Figure()
for i in range(len(radar_df)):
    fig_radar.add_trace(go.Scatterpolar(
        r=radar_df.iloc[i, 1:].values,
        theta=categories,
        fill='toself',
        name=radar_df.iloc[i, 0]
    ))
fig_radar.update_layout(
    polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
    template='plotly_dark',
    paper_bgcolor='#0d1117',
    font=dict(color='white'),
    title={"text": "📊 Radar Chart: Communication, Sensory Gains & Safety", "font": {"color": "white"}}
)
st.plotly_chart(fig_radar, use_container_width=True)
