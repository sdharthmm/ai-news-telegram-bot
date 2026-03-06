import requests
from config import NEWS_API_KEY

def fetch_news(query: str) -> str:
    """
    Fetches the first news article for a given query using NewsAPI.
    Returns a combined string of title, description, and content.
    """
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    data = response.json()

    if data.get("status") != "ok" or not data.get("articles"):
        return "No articles found."

    article = data["articles"][0]
    text = f"{article.get('title', '')}\n\n{article.get('description', '')}\n\n{article.get('content', '')}"
    return text