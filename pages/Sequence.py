import streamlit as st
import pandas as pd

from src.data_loader import DataLoader
from src.preprocessing import Preprocessor
from src.sequence_generator import SequenceGenerator
from utils.sidebar import show_sidebar
from utils.theme import load_css
st.set_page_config(
    page_title="Sequence Generator",
    page_icon="🔄",
    layout="wide"
)
load_css()
show_sidebar()
st.title("🔄 Sequence Generator")

st.write(
    "Convert the scaled time-series data into sequences for training the LSTM model."
)

DATA_PATH = "data/airline-passengers.csv"

sequence_length = st.slider(
    "Sequence Length",
    min_value=3,
    max_value=24,
    value=12,
    step=1
)

if st.button("🚀 Generate Sequences", use_container_width=True):

    with st.spinner("Generating sequences..."):

        loader = DataLoader(DATA_PATH)
        df = loader.load_data()

        preprocessor = Preprocessor()
        scaled_df = preprocessor.scale_data(df)

        generator = SequenceGenerator(sequence_length)

        X, y = generator.create_sequences(scaled_df)

    st.success("✅ Sequence Generation Completed!")

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Sequence Length", sequence_length)

    with col2:
        st.metric("Input Samples", X.shape[0])

    with col3:
        st.metric("Target Samples", y.shape[0])

    st.divider()

    st.subheader("Input Shape")

    st.code(str(X.shape))

    st.subheader("Output Shape")

    st.code(str(y.shape))

    st.divider()

    index = st.number_input(
        "Choose Sequence Number",
        min_value=0,
        max_value=len(X)-1,
        value=0
    )

    st.subheader("Input Sequence")

    sequence_df = pd.DataFrame(
        X[index],
        columns=["Passengers"]
    )

    st.dataframe(sequence_df, use_container_width=True)

    st.subheader("Target Value")

    st.metric(
        "Next Passenger Value",
        round(float(y[index][0]),4)
    )

    st.divider()

    st.line_chart(sequence_df)

    st.caption("The next value after this sequence is the target.")