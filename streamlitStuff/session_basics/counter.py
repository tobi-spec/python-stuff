import streamlit as st

st.title("Counter Example")
counter = 0

if "session_counter" not in st.session_state:
    st.session_state["session_counter"] = 0

increment = st.button("Increment non session counter")
if increment:
    counter += 1
st.write("Non session counter:" + str(counter))

session_increment = st.button("Increment session counter")
if session_increment:
    st.session_state["session_counter"] += 1
st.write("Non session counter:" + str(st.session_state["session_counter"]))



