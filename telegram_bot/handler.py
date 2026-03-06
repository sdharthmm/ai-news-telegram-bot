from ai_simplifier.llm import generate_title_and_description
from news_fetcher.fetcher import fetch_news
from datetime import datetime

def handle_message(update, context):
    text = None
    if update.message and update.message.text:
        text = update.message.text
    elif update.channel_post and update.channel_post.text:
        text = update.channel_post.text

    if text:
        timestamp = datetime.now().strftime("[%d-%m-%Y %I:%M %p]")
        print(f"{timestamp} User Input: {text}")

        article = fetch_news(text)
        print(f"{timestamp} Stage: Article fetched (first 200 chars):")
        print(article[:200], "...")

        result = generate_title_and_description(article)

        print(f"{timestamp} Stage: AI generated result:")
        print(f"📰 {result['title']}")
        print(result['description'])

        reply = f"📰 <b>{result['title']}</b>"
        if result["description"]:
            reply += f"\n\n{result['description']}"
        if update.message:
            update.message.reply_text(reply, parse_mode="HTML")
        elif update.channel_post:
            context.bot.send_message(chat_id=update.channel_post.chat_id, text=reply, parse_mode="HTML")