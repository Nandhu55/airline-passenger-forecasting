import streamlit as st

from utils.sidebar import show_sidebar
from utils.theme import load_css


st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

load_css()
show_sidebar()

st.title("ℹ️ About This Project")

st.markdown("""
# ✈️ Airline Passenger Forecasting using Deep Learning

This project predicts future airline passenger traffic using Deep Learning
models like **LSTM**, **GRU**, and **Simple RNN**.

The application provides a complete pipeline from dataset loading to future forecasting through an interactive Streamlit dashboard.
""")

st.divider()

st.header("🎯 Project Objectives")

st.markdown("""
- Load Airline Passenger Dataset
- Preprocess Data
- Generate Time-Series Sequences
- Split Dataset into Training & Testing
- Build Deep Learning Models
- Train Model
- Evaluate Performance
- Predict Passenger Count
- Forecast Future Passengers
""")

st.divider()

st.header("⚙️ Technologies Used")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
### Programming

- Python

### Data Processing

- Pandas
- NumPy

### Machine Learning

- TensorFlow
- Keras
- Scikit-Learn
""")

with col2:

    st.markdown("""
### Visualization

- Plotly
- Streamlit

### Tools

- Joblib
- VS Code
- Git & GitHub
""")

st.divider()

st.header("📁 Project Workflow")

st.code("""
Dataset
    ↓
Data Loader
    ↓
Preprocessing
    ↓
Sequence Generator
    ↓
Train-Test Split
    ↓
Model Builder
    ↓
Training
    ↓
Prediction
    ↓
Evaluation
    ↓
Forecast
""")

st.divider()

st.header("🧠 Deep Learning Architecture")

st.code("""
Input (12 Months)
        │
        ▼
LSTM / GRU / RNN
        │
        ▼
Dropout (20%)
        │
        ▼
Dense Layer (32)
        │
        ▼
Output Layer (1)
""")

st.divider()

st.header("📂 Dataset")

st.markdown("""
**Dataset:** Airline Passengers Dataset

- Total Records : 144
- Features : 2
- Monthly Passenger Data
- Time Series Dataset
""")

st.divider()

st.header("📈 Features")

st.markdown("""
✅ Dataset Loading

✅ Data Preprocessing

✅ Sequence Generation

✅ Train/Test Split

✅ LSTM / GRU / RNN Models

✅ Model Training

✅ Model Evaluation

✅ Future Forecasting

✅ Interactive Charts

✅ Download Results
""")

st.divider()

st.header("🚀 Future Improvements")

st.markdown("""
- Hyperparameter Tuning
- Attention Mechanism
- Transformer Models
- Multivariate Forecasting
- Real-Time Data Integration
- Cloud Deployment
- REST API
- Model Monitoring
""")

st.divider()

st.success("🎉 Airline Passenger Forecasting Dashboard Developed using Streamlit & TensorFlow")