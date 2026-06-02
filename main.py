from pyrogram import Client, filters
from pyrogram.types import Message
from database import *

API_ID = 39374484
API_HASH = "ea49c9543e97c063b99e1ae1ef5fd50b"
BOT_TOKEN = "8933730654:AAGR9BP8Tnaqk-GuxAe97BsNbn74jmRxDEw"

ADMIN_ID = 5078457964

bot = Client(
"KinochiBot",
api_id=API_ID,
api_hash=API_HASH,
bot_token=BOT_TOKEN
)

@bot.on_message(filters.command("start"))
async def start(client, message: Message):
add_user(message.from_user.id)

await message.reply_text(
    "🎬 Kino botga xush kelibsiz!\n\nKino kodini yuboring."
)

@bot.on_message(filters.command("stat"))
async def stat(client, message: Message):
if message.from_user.id != ADMIN_ID:
return

users = get_users_count()

await message.reply_text(
    f"👥 Foydalanuvchilar: {users}"
)

@bot.on_message(filters.command("add"))
async def addfilm(client, message: Message):
if message.from_user.id != ADMIN_ID:
return

if not message.reply_to_message:
    await message.reply_text(
        "Videoga reply qilib:\n/add 555"
    )
    return

if not message.reply_to_message.video:
    await message.reply_text(
        "Faqat videoga reply qiling."
    )
    return

try:
    code = message.text.split()[1]
    file_id = message.reply_to_message.video.file_id

    add_movie(code, file_id)

    await message.reply_text(
        f"✅ Kino qo'shildi\nKod: {code}"
    )
except:
    await message.reply_text(
        "Misol:\n/add 555"
    )

@bot.on_message(filters.command("del"))
async def delfilm(client, message: Message):
if message.from_user.id != ADMIN_ID:
return

try:
    code = message.text.split()[1]

    delete_movie(code)

    await message.reply_text(
        "🗑 Kino o'chirildi"
    )
except:
    await message.reply_text(
        "Misol:\n/del 555"
    )

@bot.on_message(filters.text)
async def search(client, message: Message):
add_user(message.from_user.id)

code = message.text.strip()

movie = get_movie(code)

if movie:
    await message.reply_video(movie)
else:
    await message.reply_text(
        "❌ Kino topilmadi"
    )

bot.run()
