import asyncio
from telegram import Bot
from config import BOT_TOKEN

async def main():
    bot = Bot(token=BOT_TOKEN)
    updates = await bot.get_updates()  # await the coroutine

    for u in updates:
        print(u)  # look for chat.id for your channel

asyncio.run(main())