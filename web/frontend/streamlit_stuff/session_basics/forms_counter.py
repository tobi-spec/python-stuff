import datetime

import streamlit as st

st.title("Form Counter")

if "counter" not in st.session_state:
    st.session_state["counter"] = 0
    st.session_state["last_update"] = datetime.time(0,0)

def update_counter() -> None:
    st.session_state["counter"] += st.session_state["increment_value"]
    st.session_state["last_update"] = st.session_state["update_time"]

with st.form(key="my_form"):
    st.number_input("Enter a value", value=0, step=1, key="increment_value")
    st.time_input(label="Enter the time", value=datetime.datetime.now(), key="update_time")
    submit = st.form_submit_button(label="Update", on_click=update_counter)

st.write('Current Count = ', st.session_state["counter"])
st.write('Last Updated = ', st.session_state["last_update"])
