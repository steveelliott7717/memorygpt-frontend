import streamlit as st
import requests
import uuid

API_URL = "https://memorygpt-backend.fly.dev/"

if "user_id" not in st.session_state:
    st.session_state["user_id"] = str(uuid.uuid4())

user_id = st.session_state["user_id"]
user_input = st.text_input("Ask MemoryGPT:")

if user_input:
    try:
        response = requests.post(API_URL, json={"user_id": user_id, "message": user_input})
        response.raise_for_status()  # raise exception for 403, 500, etc.
        st.write(response.json())
    except requests.exceptions.RequestException as e:
        st.error("Backend request failed")
        st.code(str(e))
        st.code(response.text)
