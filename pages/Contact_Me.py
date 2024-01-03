import streamlit as st
import numpy as np

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")
    button = st.form_submit_button()
    if button:
        print("Button pressed")

table = np.array([
    [1, 3],
    [2, 4]
])
print(table.max(axis=1))
