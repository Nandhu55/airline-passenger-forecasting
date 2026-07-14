import streamlit as st
import pandas as pd
import plotly.express as px

from src.data_loader import DataLoader
from src.preprocessing import Preprocessor
from utils.sidebar import show_sidebar
from utils.theme import load_css
st.set_page_config(
    page_title="Preprocessing",
    page_icon="⚙️",
    layout="wide"
)
load_css()
show_sidebar()
st.title("⚙️ Data Preprocessing")

st.write("Scale the passenger data using MinMaxScaler.")

DATA_PATH = "data/airline-passengers.csv"

if st.button("🚀 Run Preprocessing", use_container_width=True):

    with st.spinner("Processing dataset..."):

        # Load Dataset
        loader = DataLoader(DATA_PATH)
        df = loader.load_data()

        # Scale Dataset
        preprocessor = Preprocessor()
        scaled_df = preprocessor.scale_data(df)

    st.success("✅ Preprocessing Completed Successfully!")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📋 Original Dataset")

        st.dataframe(df.head(10), use_container_width=True)

    with col2:

        st.subheader("📋 Scaled Dataset")

        st.dataframe(scaled_df.head(10), use_container_width=True)

    st.divider()

    st.subheader("📊 Original Passenger Trend")

    fig1 = px.line(
        df,
        y="Passengers",
        title="Original Passenger Count"
    )

    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("📊 Scaled Passenger Trend")

    fig2 = px.line(
        scaled_df,
        y="Passengers",
        title="Scaled Passenger Count"
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.divider()

    st.subheader("📈 Scaling Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Original Minimum",
            int(df["Passengers"].min())
        )

    with col2:
        st.metric(
            "Original Maximum",
            int(df["Passengers"].max())
        )

    with col3:
        st.metric(
            "Scaled Range",
            "0 → 1"
        )

    st.divider()

    st.download_button(
        "📥 Download Scaled Dataset",
        scaled_df.to_csv().encode("utf-8"),
        "scaled_dataset.csv",
        "text/csv"
    )