import streamlit as st
import pandas as pd

from src.model import ModelBuilder
from utils.sidebar import show_sidebar
from utils.theme import load_css
st.set_page_config(
    page_title="Model Builder",
    page_icon="🤖",
    layout="wide"
)
load_css()
show_sidebar()
st.title("🤖 Deep Learning Model Builder")

st.write(
    "Build and configure the Recurrent Neural Network used for forecasting."
)

# ------------------------
# Sidebar Configuration
# ------------------------

st.subheader("⚙️ Model Configuration")

model_type = st.selectbox(
    "Select Model",
    ["LSTM", "GRU", "RNN"]
)

timesteps = st.number_input(
    "Time Steps",
    value=12,
    min_value=1
)

features = st.number_input(
    "Features",
    value=1,
    min_value=1
)

# ------------------------
# Build Model
# ------------------------

if st.button("🚀 Build Model", use_container_width=True):

    builder = ModelBuilder(
        model_type=model_type.lower(),
        input_shape=(timesteps, features)
    )

    model = builder.build_model()

    st.success("✅ Model Built Successfully!")

    st.divider()

    st.subheader("📋 Model Configuration")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Model", model_type)

    with col2:
        st.metric("Time Steps", timesteps)

    with col3:
        st.metric("Features", features)

    st.divider()

    st.subheader("📊 Layer Information")

    layers = []

    for layer in model.layers:

        layers.append({

            "Layer Name": layer.name,

            "Layer Type": layer.__class__.__name__,

            "Output Shape": str(layer.output.shape),

            "Parameters": layer.count_params()

        })

    st.dataframe(
        pd.DataFrame(layers),
        use_container_width=True
    )

    st.divider()

    total_params = model.count_params()

    st.metric(
        "Total Trainable Parameters",
        f"{total_params:,}"
    )

    st.divider()

    st.info(
        """
        Architecture

        Input
            ↓
        LSTM / GRU / RNN
            ↓
        Dropout (20%)
            ↓
        Dense (32 Neurons)
            ↓
        Output (1 Neuron)
        """
    )