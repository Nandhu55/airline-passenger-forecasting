import streamlit as st


def show_sidebar():

    with st.sidebar:

        st.image(
            "assets/logo.jpg",
            width=140
        )

        st.title("✈ Airline Forecast")

        st.caption(
            "Deep Learning Dashboard"
        )

        st.divider()

        st.success("Version 1.0")

        st.info(
            "TensorFlow • Streamlit"
        )

        st.divider()

        st.markdown("### 👨‍💻 Developer")

        st.write("**G. Nandhishwar Reddy**")

        st.caption("B.Tech CSE (Data Science)")