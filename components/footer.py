import streamlit as st


def show_footer():

    st.divider()

    st.markdown(
        """
        <center>

        Developed by <b>G. Nandhishwar Reddy</b>

        <br>

        TensorFlow • Streamlit • Plotly

        </center>
        """,
        unsafe_allow_html=True
    )