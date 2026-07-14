import streamlit as st
import os


def show_status():

    st.subheader("🟢 Project Health")

    c1,c2,c3,c4=st.columns(4)

    dataset=os.path.exists("data/airline-passengers.csv")

    model=os.path.exists("models/lstm_model.keras")

    scaler=os.path.exists("models/scaler.pkl")

    outputs=os.path.exists("outputs")

    c1.success("Dataset") if dataset else c1.error("Dataset")

    c2.success("Model") if model else c2.warning("Model")

    c3.success("Scaler") if scaler else c3.warning("Scaler")

    c4.success("Outputs") if outputs else c4.warning("Outputs")