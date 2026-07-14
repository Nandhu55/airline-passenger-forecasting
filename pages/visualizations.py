import streamlit as st
import plotly.graph_objects as go

from src.train import ModelTrainer
from src.predict import Predictor
from src.forecast import Forecaster
from utils.sidebar import show_sidebar
from utils.theme import load_css
st.set_page_config(
    page_title="Visualizations",
    page_icon="📈",
    layout="wide"
)
load_css()
show_sidebar()
st.title("📈 Model Visualizations")

st.write(
    "Visualize model training, prediction performance, and future forecasts."
)

tab1, tab2, tab3 = st.tabs([
    "📉 Training Loss",
    "📊 Predictions",
    "🔮 Forecast"
])

# ----------------------------------------------------
# Training Loss
# ----------------------------------------------------

with tab1:

    st.subheader("Training Loss vs Validation Loss")

    if st.button("Generate Training Graph"):

        with st.spinner("Loading..."):

            trainer = ModelTrainer()

            model, history = trainer.train()

        fig = go.Figure()

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
            title="Training Loss",
            xaxis_title="Epoch",
            yaxis_title="Loss",
            template="plotly_dark"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

# ----------------------------------------------------
# Prediction Graph
# ----------------------------------------------------

with tab2:

    st.subheader("Actual vs Predicted")

    if st.button("Generate Prediction Graph"):

        predictor = Predictor()

        actual, predicted = predictor.predict()

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                y=actual.flatten(),
                mode="lines",
                name="Actual"
            )
        )

        fig.add_trace(
            go.Scatter(
                y=predicted.flatten(),
                mode="lines",
                name="Predicted"
            )
        )

        fig.update_layout(
            title="Prediction Comparison",
            xaxis_title="Sample",
            yaxis_title="Passengers",
            template="plotly_dark"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

# ----------------------------------------------------
# Forecast Graph
# ----------------------------------------------------

with tab3:

    st.subheader("Future Forecast")

    months = st.slider(
        "Forecast Months",
        1,
        24,
        12
    )

    if st.button("Generate Forecast Graph"):

        forecaster = Forecaster()

        future = forecaster.forecast(months)

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=list(range(1, months + 1)),
                y=future.flatten(),
                mode="lines+markers",
                name="Forecast"
            )
        )

        fig.update_layout(
            title="Future Passenger Forecast",
            xaxis_title="Months",
            yaxis_title="Passengers",
            template="plotly_dark"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )