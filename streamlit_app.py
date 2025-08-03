import streamlit as st
import requests

API_URL = "https://memorygpt-backend.fly.dev/"  # Replace with your actual Fly.io backend URL

import uuid

if "user_id" not in st.session_state:
    st.session_state["user_id"] = str(uuid.uuid4())

user_id = st.session_state["user_id"]

user_input = st.text_input("Ask MemoryGPT:")

if user_input:
    response = requests.post(API_URL, json={"user_id": user_id, "message": user_input})
    st.write(response.json())