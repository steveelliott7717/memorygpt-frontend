import requests

API_URL = "https://memorygpt-backend.fly.dev/"  # Replace with your actual Fly.io backend URL

# Later in your code...
response = requests.post(API_URL, json={"user_id": user_id, "message": user_input})
