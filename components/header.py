import streamlit as st


def show_header():

    st.markdown(
        """
        <h1 style="
        font-size:42px;
        margin-bottom:0px;
        ">
        ✈ Airline Passenger Forecasting
        </h1>

        <p style="
        color:gray;
        font-size:18px;
        margin-top:0px;
        ">
        Deep Learning Forecasting Dashboard
        </p>
        """,
        unsafe_allow_html=True
    )