import streamlit as st
import pandas as pd

st.title("🤖 FAQ Chatbot")

data = pd.read_csv("faq.csv")

user_question = st.text_input("Ask a Question")

if st.button("Get Answer"):
    found = False

    for i in range(len(data)):
        if user_question.lower() == data["question"][i].lower():
            st.success("Answer")
            st.write(data["answer"][i])
            found = True
            break

    if not found:
        st.warning("Sorry, I don't know the answer.")