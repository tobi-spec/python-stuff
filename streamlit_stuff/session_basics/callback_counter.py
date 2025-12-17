import streamlit as st

st.title("Callback Counter Example")
if "counter" not in st.session_state:
    st.session_state["counter"] = 0

def counter_callback():
    st.session_state["counter"] += 1

st.button("Increment", on_click=counter_callback)
st.write("Counter: " + str(st.session_state["counter"]))