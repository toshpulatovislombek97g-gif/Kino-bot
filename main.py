from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters

API_ID = 123456
API_HASH = "API_HASH"
BOT_TOKEN = "TOKEN"

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
