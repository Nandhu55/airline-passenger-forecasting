import streamlit as st
import pandas as pd
import plotly.express as px

from utils.sidebar import show_sidebar
from utils.theme import load_css

from src.data_loader import DataLoader

st.set_page_config(
    page_title="Dashboard",
    page_icon="✈️",
    layout="wide"
)

load_css()
show_sidebar()

st.markdown(
"""
# ✈ Airline Passenger Forecasting

### Deep Learning Forecasting Dashboard
"""
)

loader = DataLoader(
    "data/airline-passengers.csv"
)

df = loader.load_data()

# ----------------------------
# KPI Cards
# ----------------------------

c1,c2,c3,c4 = st.columns(4)

c1.metric(
    "📊 Records",
    len(df)
)

c2.metric(
    "🤖 Model",
    "LSTM"
)

c3.metric(
    "📅 Years",
    "1949 - 1960"
)

c4.metric(
    "🔮 Forecast",
    "12 Months"
)

st.divider()

# ----------------------------
# Passenger Trend
# ----------------------------

st.subheader("📈 Passenger Trend")

fig = px.line(
    df,
    y="Passengers",
    markers=True
)

fig.update_layout(

    template="plotly_dark",

    height=500,

    xaxis_title="Month",

    yaxis_title="Passengers"

)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ----------------------------
# Dataset Preview
# ----------------------------

st.subheader("📋 Dataset Preview")

st.dataframe(
    df.head(10),
    use_container_width=True
)

st.divider()

# ----------------------------
# Project Status
# ----------------------------

st.subheader("🟢 Project Status")

col1,col2,col3 = st.columns(3)

with col1:

    st.success("Dataset Loaded")

with col2:

    st.success("Scaler Ready")

with col3:

    st.success("Frontend Connected")

st.divider()

# ----------------------------
# Workflow
# ----------------------------

st.subheader("⚙ Workflow")

st.info("""

📂 Dataset

⬇

⚙ Preprocessing

⬇

🔄 Sequence Generator

⬇

🤖 Model Builder

⬇

🚀 Training

⬇

📊 Evaluation

⬇

🔮 Forecast

""")