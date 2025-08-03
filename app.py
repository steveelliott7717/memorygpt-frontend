import streamlit as st
import requests

st.title("🧠 MemoryGPT")

user_id = st.text_input("User ID", value="demo_user")
message = st.text_area("Type your message")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if st.button("Send"):
    if user_id and message:
        st.session_state.chat_history.append(("You", message))

        try:
            response = requests.post(
                "https://memorygpt-backend.fly.dev",  # ✅ Correct port for FastAPI
                json={"user_id": user_id, "message": message}
            )
            if response.status_code == 200:
                reply = response.json()["reply"]
                st.session_state.chat_history.append(("MemoryGPT", reply))
            else:
                st.session_state.chat_history.append(("MemoryGPT", "[Error]"))
        except Exception as e:
            st.session_state.chat_history.append(("MemoryGPT", f"[Exception: {e}]"))

# Display chat history
for sender, msg in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {msg}")
