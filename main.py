import os
import requests

api_key = os.getenv("API_KEY")
response = requests.get(f"https://api.example.com/data?apikey={api_key}")
print(response.status_code)
