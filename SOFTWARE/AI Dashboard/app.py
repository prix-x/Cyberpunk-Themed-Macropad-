import streamlit as st
from ai_engine import chat, summarize

st.set_page_config(page_title="AI Dashboard", page_icon="🤖")

st.title("🤖 AI Dashboard")

mode = st.sidebar.radio("Mode", ["Chat", "Summarizer"])

if mode == "Chat":
    st.subheader("Chat with AI")

    if "history" not in st.session_state:
        st.session_state.history = []

    user_input = st.text_input("Say something")

    if st.button("Send"):
        if user_input:
            response = chat(user_input)
            st.session_state.history.append(("You", user_input))
            st.session_state.history.append(("AI", response))

    for role, msg in st.session_state.history:
        st.write(f"**{role}:** {msg}")

elif mode == "Summarizer":
    st.subheader("Text Summarizer")

    text = st.text_area("Paste text")

    if st.button("Summarize"):
        if text:
            result = summarize(text)
            st.success(result)
