import streamlit as st
import plotly.graph_objects as go

from src.train import ModelTrainer
from utils.sidebar import show_sidebar
from utils.theme import load_css
st.set_page_config(
    page_title="Model Training",
    page_icon="🚀",
    layout="wide"
)
load_css()
show_sidebar()
st.title("🚀 Train Deep Learning Model")

st.write("Train the Airline Passenger Forecasting Model")

st.subheader("Training Configuration")

col1, col2 = st.columns(2)

with col1:
    epochs = st.slider(
        "Epochs",
        10,
        200,
        100
    )

with col2:
    batch_size = st.selectbox(
        "Batch Size",
        [4,8,16,32],
        index=1
    )

st.info(
    """
Current backend uses:

• Model : LSTM

• Epochs : 100

• Batch Size : 8

(UI customization will be connected in the next backend update.)
"""
)

if st.button("🚀 Start Training", use_container_width=True):

    with st.spinner("Training Model..."):

        trainer = ModelTrainer()

        model, history = trainer.train()

    st.success("✅ Training Completed Successfully!")

    st.divider()

    st.subheader("Training Result")

    col1,col2,col3=st.columns(3)

    with col1:
        st.metric(
            "Epochs",
            len(history.history["loss"])
        )

    with col2:
        st.metric(
            "Final Training Loss",
            round(history.history["loss"][-1],5)
        )

    with col3:
        st.metric(
            "Final Validation Loss",
            round(history.history["val_loss"][-1],5)
        )

    st.divider()

    st.subheader("Training Loss")

    fig=go.Figure()

    fig.add_trace(
        go.Scatter(
            y=history.history["loss"],
            mode="lines",
            name="Training Loss"
        )
    )

    fig.add_trace(
        go.Scatter(
            y=history.history["val_loss"],
            mode="lines",
            name="Validation Loss"
        )
    )

    fig.update_layout(
        height=500,
        xaxis_title="Epoch",
        yaxis_title="Loss"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    st.success("✔ Model Saved Successfully")

    st.code("models/lstm_model.keras")