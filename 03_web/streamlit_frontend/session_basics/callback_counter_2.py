import streamlit as st

st.title("Callback Counter Example 2")

if "counter" not in st.session_state:
    st.session_state["counter"] = 0

increment = st.number_input("Increment by", value=0, step=1)

def counter_callback(number: int) -> None:
    st.session_state["counter"] += number

def set_counter(number: int) -> None:
    st.session_state["counter"] = number

st.button("Increment", on_click=counter_callback, args=(increment,))
st.button("Set Value", on_click=set_counter, kwargs=dict(number=0))
st.write("Counter: " + str(st.session_state["counter"]))