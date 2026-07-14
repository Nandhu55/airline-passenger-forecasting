import streamlit as st

st.set_page_config(
    page_title="Airline Passenger Forecasting",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

def load_css():
    with open("assets/styles.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

st.logo("assets/logo.jpg")

st.sidebar.title("✈️ Airline Forecast AI")

st.sidebar.markdown("---")

st.title("✈️ Airline Passenger Forecasting System")

st.markdown("""
### Welcome

An AI-powered dashboard for forecasting airline passenger traffic using
Deep Learning (RNN, LSTM & GRU).

Use the navigation menu on the left to explore each stage of the
forecasting pipeline.
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Models", "3", "RNN • LSTM • GRU")

with col2:
    st.metric("Forecast", "Future Ready")

with col3:
    st.metric("Framework", "TensorFlow")

st.info("👈 Select a module from the sidebar to begin.")
