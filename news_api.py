
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")

def get_news(category="technology"):
    print("Fetching news...")

    if not API_KEY:
        print("Error: API key not found!")
        return

    url = "https://newsapi.org/v2/top-headlines"

    params = {
        "country": "us",
        "category": category,
        "apiKey": API_KEY
    }

    try:
        response = requests.get(url, params=params, timeout=15)

        print("Status Code:", response.status_code)

        data = response.json()
       
        if response.status_code == 200:

            articles = data.get("articles", [])

            if not articles:
                print("No articles found!")
                return

            for article in articles[:5]:
                print("\nHeadline:", article.get("title"))
                print("Source:", article.get("source", {}).get("name"))
                print("URL:", article.get("url"))

        else:
            print("API Error:", data.get("message", "Unknown error"))

    except requests.exceptions.RequestException as e:
        print("Connection Error:", e)

print("News API program started!")

get_news("technology")
get_news("sports")
get_news("business")
