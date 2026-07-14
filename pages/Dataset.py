import streamlit as st
import pandas as pd
from utils.sidebar import show_sidebar
from utils.theme import load_css

from src.data_loader import DataLoader

st.set_page_config(
    page_title="Dataset",
    page_icon="📂",
    layout="wide"
)

load_css()
show_sidebar()
st.title("📂 Dataset")

st.write("Load and inspect the Airline Passenger dataset.")

DATA_PATH = "data/airline-passengers.csv"

try:
    loader = DataLoader(DATA_PATH)
    df = loader.load_data()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    with col3:
        st.metric("Missing Values", df.isnull().sum().sum())

    st.divider()

    st.subheader("Dataset Preview")

    st.dataframe(df, use_container_width=True)

    st.divider()

    st.subheader("Dataset Information")

    info = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str),
        "Missing Values": df.isnull().sum().values
    })

    st.dataframe(info, use_container_width=True)

    st.divider()

    st.subheader("Statistical Summary")

    st.dataframe(df.describe(), use_container_width=True)

    st.divider()

    st.download_button(
        label="📥 Download Dataset",
        data=df.to_csv().encode("utf-8"),
        file_name="airline-passengers.csv",
        mime="text/csv"
    )

except Exception as e:
    st.error(f"Error : {e}")