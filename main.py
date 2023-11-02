import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Andrew Moore")
    content = """
    I am a software engineer from California. I like cats and guitars.
    """
    st.info(content)

st.write("Below you can find some of the apps I have built in Python. This text should not be bound to the width of one column.")