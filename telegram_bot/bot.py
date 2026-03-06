from telegram.ext import Updater, MessageHandler, Filters
from config import BOT_TOKEN
from telegram_bot.handler import handle_message

def run_bot():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Listen for text messages
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Also listen for channel posts
    dp.add_handler(MessageHandler(Filters.update.channel_posts, handle_message))

    updater.start_polling()
    updater.idle()