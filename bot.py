from pyrogram import Client, filters
import asyncio
import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

SOURCE_CHANNEL = int(os.getenv("SOURCE_CHANNEL"))
TARGET_CHANNELS = list(map(int, os.getenv("TARGET_CHANNELS").split(",")))

app = Client(
    "forward_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.chat(SOURCE_CHANNEL))
async def auto_forward(client, message):

    for target in TARGET_CHANNELS:
        try:
            await message.copy(target)
            await asyncio.sleep(1)
        except Exception as e:
            print(e)

app.run()
