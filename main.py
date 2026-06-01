from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters

API_ID = 39374484
API_HASH = "ea49c9543e97c063b99e1ae1ef5fd50b"
BOT_TOKEN = "8933730654:AAGHOkmhMRPiZ7ZvBRh8X20q-0k3EaB2N2s"

bot = Client(
    "KinochiBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@bot.on_message(filters.command("start"))
async def start(client, message: Message):
    await message.reply_text("🎬 Kinochi Uz Bot ishga tushdi!")

bot.run()
