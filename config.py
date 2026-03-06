import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable not set")

if not NEWS_API_KEY:
    raise ValueError("NEWS_API_KEY environment variable not set")