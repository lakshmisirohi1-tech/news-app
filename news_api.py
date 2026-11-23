
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")

def get_news(category="technology"):

    if not API_KEY:
        print("API key not found!")
        return []

    url = "https://newsapi.org/v2/top-headlines"

    params = {
        "country": "us",
        "category": category,
        "apiKey": API_KEY
    }

    try:
        response = requests.get(url, params=params, timeout=15)
        data = response.json()

        if response.status_code == 200:
            return data.get("articles", [])
        else:
            print("API Error:", data.get("message"))
            return []

    except requests.exceptions.RequestException as e:
        print("Connection Error:", e)
        return []

