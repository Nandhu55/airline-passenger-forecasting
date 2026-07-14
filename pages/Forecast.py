import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from utils.sidebar import show_sidebar
from utils.theme import load_css

from src.forecast import Forecaster

st.set_page_config(
    page_title="Future Forecast",
    page_icon="🔮",
    layout="wide"
)
load_css()
show_sidebar()
st.title("🔮 Future Passenger Forecast")

st.write(
    "Predict future airline passenger counts using the trained LSTM model."
)

forecast_months = st.slider(
    "Forecast Months",
    min_value=1,
    max_value=24,
    value=12
)

if st.button("🚀 Generate Forecast", use_container_width=True):

    with st.spinner("Generating Future Forecast..."):

        forecaster = Forecaster()

        future = forecaster.forecast(
            future_months=forecast_months
        )

    st.success("✅ Forecast Generated Successfully!")

    st.divider()

    future_df = pd.DataFrame({
        "Month": range(1, forecast_months + 1),
        "Predicted Passengers": future.flatten()
    })

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Minimum",
            int(future_df["Predicted Passengers"].min())
        )

    with col2:
        st.metric(
            "Maximum",
            int(future_df["Predicted Passengers"].max())
        )

    with col3:
        st.metric(
            "Average",
            int(future_df["Predicted Passengers"].mean())
        )

    st.divider()

    st.subheader("Forecast Table")

    st.dataframe(
        future_df,
        use_container_width=True
    )

    st.divider()

    st.subheader("Forecast Chart")

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=future_df["Month"],
            y=future_df["Predicted Passengers"],
            mode="lines+markers",
            name="Forecast"
        )
    )

    fig.update_layout(
        title="Future Passenger Forecast",
        xaxis_title="Future Months",
        yaxis_title="Passengers",
        template="plotly_dark",
        height=550
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    csv = future_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "📥 Download Forecast",
        csv,
        "future_forecast.csv",
        "text/csv"
    )