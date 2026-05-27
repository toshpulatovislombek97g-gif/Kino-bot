from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes
import sqlite3

TOKEN = "8933730654:AAGHOkmhMRPiZ7ZvBRh8X20q-0k3EaB2N2s"

# DATABASE
conn = sqlite3.connect("movies.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS movies (
    code TEXT PRIMARY KEY,
    file_id TEXT
)
""")
conn.commit()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎬 Kino botga xush kelibsiz!\nKod yuboring:")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    cursor.execute("SELECT file_id FROM movies WHERE code=?", (text,))
    movie = cursor.fetchone()

    if movie:
        await update.message.reply_video(movie[0])
    else:
        await update.message.reply_text("❌ Kino topilmadi")

async def add_movie(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.reply_to_message and update.message.reply_to_message.video:
        code = context.args[0]
        file_id = update.message.reply_to_message.video.file_id

        cursor.execute("INSERT INTO movies VALUES (?, ?)", (code, file_id))
        conn.commit()

        await update.message.reply_text(f"✅ Kino qo‘shildi: {code}")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("add", add_movie))
app.add_handler(MessageHandler(filters.TEXT, handle_message))

print("Bot ishlayapti 🚀")
app.run_polling()
