import streamlit as st

# MUST BE THE FIRST STREAMLIT COMMAND
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

# Load CSS AFTER set_page_config
load_css()

st.title("✈️ Airline Passenger Forecasting")

st.markdown("""
Welcome to the **Airline Passenger Forecasting Dashboard**.

Use the sidebar to navigate through the complete forecasting pipeline.

### Features
- 📂 Load Dataset
- ⚙️ Data Preprocessing
- 🔄 Sequence Generation
- 🤖 Deep Learning Model (LSTM/RNN/GRU)
- 🚀 Train Model
- 📈 Evaluate Model
- 🔮 Forecast Future Passengers
""")

st.success("Select a page from the sidebar to begin.")
