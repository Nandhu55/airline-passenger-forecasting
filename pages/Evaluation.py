import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from src.evaluate import Evaluator
from src.predict import Predictor
from utils.sidebar import show_sidebar
from utils.theme import load_css
st.set_page_config(
    page_title="Model Evaluation",
    page_icon="📊",
    layout="wide"
)
load_css()
show_sidebar()
st.title("📊 Model Evaluation")

st.write(
    "Evaluate the performance of the trained deep learning model."
)

if st.button("📈 Evaluate Model", use_container_width=True):

    with st.spinner("Evaluating Model..."):

        evaluator = Evaluator()

        mae, mse, rmse = evaluator.evaluate()

        predictor = Predictor()

        actual, predicted = predictor.predict()

    st.success("✅ Evaluation Completed Successfully!")

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("MAE", f"{mae:.4f}")

    with col2:
        st.metric("MSE", f"{mse:.4f}")

    with col3:
        st.metric("RMSE", f"{rmse:.4f}")

    st.divider()

    st.subheader("📈 Actual vs Predicted")

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
        title="Actual vs Predicted Passenger Count",
        xaxis_title="Sample",
        yaxis_title="Passengers",
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    st.subheader("Prediction Table")

    results = pd.DataFrame({
        "Actual": actual.flatten(),
        "Predicted": predicted.flatten()
    })

    results["Error"] = (
        results["Actual"] - results["Predicted"]
    ).round(2)

    st.dataframe(
        results,
        use_container_width=True
    )

    st.download_button(
        "📥 Download Predictions",
        results.to_csv(index=False).encode(),
        "predictions.csv",
        "text/csv"
    )