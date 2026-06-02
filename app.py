import streamlit as st
from ai_engine import chat, summarize

st.set_page_config(
    page_title="Prix AI",
    page_icon="🧠"
)

st.title("Prix AI 🧠")
st.caption("Minimal AI assistant")

mode = st.sidebar.radio("Mode", ["Chat", "Summarizer"])

# ---------------- CHAT ----------------
if mode == "Chat":
    st.subheader("Chat")

    if "history" not in st.session_state:
        st.session_state.history = []

    user_input = st.text_input("Type message")

    if st.button("Send") and user_input:
        response = chat(user_input)
        st.session_state.history.append(("You", user_input))
        st.session_state.history.append(("Prix AI", response))

    for role, msg in st.session_state.history:
        st.write(f"**{role}:** {msg}")

# ---------------- SUMMARIZER ----------------
else:
    st.subheader("Summarizer")

    text = st.text_area("Paste text")

    if st.button("Summarize") and text:
        result = summarize(text)
        st.success(result)
