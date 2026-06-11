import streamlit as st
from deep_translator import GoogleTranslator

st.title("🌍 Language Translation Tool")

text = st.text_area("Enter Text")

source = st.selectbox(
    "Source Language",
    ["english", "telugu", "hindi", "french", "spanish"]
)

target = st.selectbox(
    "Target Language",
    ["telugu", "english", "hindi", "french", "spanish"]
)

if st.button("Translate"):
    translated = GoogleTranslator(
        source=source,
        target=target
    ).translate(text)

    st.success("Translated Text")
    st.write(translated)