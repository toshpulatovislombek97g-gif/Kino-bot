from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8933730654:AAGHOkmhMRPiZ7ZvBRh8X20q-0k3EaB2N2s"

movies = {
    "101": "FILE_ID_1",
    "102": "FILE_ID_2"
}

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if text in movies:
        await update.message.reply_video(movies[text])
    else:
        await update.message.reply_text("❌ Kino topilmadi")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, handle_message))

app.run_polling()
