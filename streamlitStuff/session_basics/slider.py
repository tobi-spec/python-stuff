import streamlit as st

if "celsius" not in st.session_state:
    st.session_state["celsius"] = 0

st.slider(
    "Temprature in Celsius",
    min_value=-100,
    max_value=100,
    key="celsius"
)

st.write(st.session_state.celsius)