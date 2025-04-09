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

timeline_info = pd.DataFrame({
    "Phase": [
        "1. Nasal Activation",
        "2. Cerebral Arrival",
        "3. Synaptic Evaluation",
        "4. Adaptive Release",
        "5. Full Operation Cycle",
        "6. Self-Destruction"
    ],
    "Time Marker": [
        "Day 0",
        "Minute 2",
        "Hour 1",
        "Days 3–7",
        "Weeks 1–8",
        "Year 10 or upon host death"
    ],
    "Key Actions": [
        "Nanobot is activated in nasal cavity and guided by fMRI",
        "Reaches brain via cribriform plate, avoiding critical neural structures",
        "Analyzes synaptic activity using piezoelectric sensors",
        "Releases BDNF/VEGF based on AI-analyzed brain patterns",
        "Operates continuously, adapting to patient’s circadian and emotional states",
        "Fully degrades into non-toxic components after mission ends"
    ],
    "Scale Comparison": [
        "Size: 10 μm (1/5 human hair)",
        "Neuron body: 10–50 μm", 
        "Red blood cell: 7–8 μm",
        "Synaptic cleft: 20–40 nm",
        "Reservoirs hold nanogram-scale therapeutic agents",
        "Degrades via pH-activated polymer response"
    ]
})

fig_timeline = go.Figure(data=[go.Table(
    header=dict(values=list(timeline_info.columns),
                fill_color='#1f2937',
                align='left',
                font=dict(color='white', size=13)),
    cells=dict(values=[timeline_info[col] for col in timeline_info.columns],
               fill_color='#111827',
               align='left',
               font=dict(color='white', size=12))
)])
fig_timeline.update_layout(title={"text": "📆 Life Cycle Timeline: From Activation to Self-Destruction", "font": {"color": "white"}}, paper_bgcolor='#0d1117')
st.plotly_chart(fig_timeline, use_container_width=True)

# ------------------------------------------------------------------------------
# 💸 Cost vs Effectiveness Chart
# ------------------------------------------------------------------------------
st.subheader("💸 Cost vs Effectiveness")

data = {
    "Treatment": ["NeuroConnect", "ABA Therapy", "Pharmacotherapy"],
    "Cost per Patient (USD)": [2500, 1200000, 12500],
    "Patients per 100K USD": [83, 1.6, 8],
    "Effectiveness (%)": [90, 35, 45]
}
df = pd.DataFrame(data)

fig_cost = go.Figure()
fig_cost.add_trace(go.Bar(x=df['Treatment'], y=df['Patients per 100K USD'], name='Patients per $100K'))
fig_cost.add_trace(go.Bar(x=df['Treatment'], y=df['Effectiveness (%)'], name='Effectiveness (%)'))

fig_cost.update_layout(
    title={"text": "🧠 Cost vs Effectiveness (per $100,000)", "font": {"color": "white"}},
    barmode='group',
    template='plotly_dark',
    paper_bgcolor='#0d1117',
    plot_bgcolor='#0d1117',
    font=dict(color='white')
)
st.plotly_chart(fig_cost, use_container_width=True)

# ------------------------------------------------------------------------------
# 🌍 Choropleth Map: Autism Prevalence
# ------------------------------------------------------------------------------
st.subheader("🌍 Autism Prevalence by Country")

country_data = pd.DataFrame({
    "Country": ["United States", "United Kingdom", "South Korea", "Ecuador", "Nigeria", "Bangladesh"],
    "Prevalence": [27.8, 20.0, 17.5, 2.0, 1.2, 1.0]  # per 1,000 children
})
fig_map = px.choropleth(
    country_data,
    locations="Country",
    locationmode="country names",
    color="Prevalence",
    color_continuous_scale="Viridis",
    title="🌍 Autism Prevalence per 1,000 Children",
    template='plotly_dark'
)
fig_map.update_layout(
    paper_bgcolor="#0d1117",
    plot_bgcolor="#0d1117",
    font=dict(color='white'),
    geo=dict(bgcolor='#0d1117')
)
st.plotly_chart(fig_map, use_container_width=True)

# ------------------------------------------------------------------------------
# 🌐 Bubble Map: Inequity in Diagnosis
# ------------------------------------------------------------------------------
st.subheader("🌐 Inequity in Diagnosis Access")

bubble_df = pd.DataFrame({
    "Country": ["Nigeria", "Peru", "India", "Ghana", "UK", "USA"],
    "Undiagnosed": [950000, 320000, 1500000, 500000, 45000, 70000],
    "Access": ["No", "No", "Partial", "No", "Yes", "Yes"],
    "lat": [9.082, -9.19, 20.59, 7.9465, 55.3781, 37.0902],
    "lon": [8.6753, -75.0152, 78.96, -1.0232, -3.4360, -95.7129]
})
fig_bubble = px.scatter_geo(
    bubble_df,
    lat="lat",
    lon="lon",
    size="Undiagnosed",
    color="Access",
    hover_name="Country",
    title="🔴 Undiagnosed Children + NeuroConnect Access",
    template='plotly_dark',
    projection="natural earth"
)
fig_bubble.update_layout(
    paper_bgcolor="#0d1117",
    plot_bgcolor="#0d1117",
    font=dict(color='white'),
    geo=dict(bgcolor='#0d1117')
)
st.plotly_chart(fig_bubble, use_container_width=True)

# ------------------------------------------------------------------------------
# 📡 Radar Chart: Accessibility
# ------------------------------------------------------------------------------
st.subheader("📡 Accessibility to Autism Care: USA vs Nigeria")

radar = pd.DataFrame({
    'Factor': ['Diagnostics', 'Therapy Innovation', 'Trained Staff', 'Infrastructure', 'Funding'],
    'USA': [10, 9, 9, 10, 9],
    'Nigeria': [2, 1, 2, 3, 2]
})
fig_radar = go.Figure()
for country in radar.columns[1:]:
    fig_radar.add_trace(go.Scatterpolar(
        r=radar[country],
        theta=radar['Factor'],
        fill='toself',
        name=country
    ))
fig_radar.update_layout(
    polar=dict(radialaxis=dict(visible=True, range=[0,10])),
    title={"text": "🛰️ Equity in Autism Diagnosis & Treatment", "font": {"color": "white"}},
    template='plotly_dark',
    paper_bgcolor='#0d1117',
    font=dict(color='white')
)
st.plotly_chart(fig_radar, use_container_width=True)

# ------------------------------------------------------------------------------
# ✅ Conclusion
# ------------------------------------------------------------------------------
st.markdown("""
✅ **Conclusion:**  
> NeuroConnect is not just frontier science. It's global medical justice.
""")
