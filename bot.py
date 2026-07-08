from telegram import Update
from telegram.ext import (
    Application,
    MessageHandler,
    ContextTypes,
    filters,
)
from datetime import time
import pytz

TOKEN = "8832677410:AAH0zSUpad3GzA6YkC60BrfByBvlSGjbBCE"

AFFIRMATION = (
    "🌿 I'm grateful that my body keeps carrying me through each day, "
    "even when I'm not feeling my best. "
)

# Replace with your Telegram chat ID
CHAT_ID = YOUR_CHAT_ID

async def send_daily(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=CHAT_ID,
        text=AFFIRMATION
    )

async def reply_affirmation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower().strip()

    if text == "i am blessed":
        await update.message.reply_text(AFFIRMATION)

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, reply_affirmation)
    )

    india = pytz.timezone("Asia/Kolkata")

    app.job_queue.run_daily(
        send_daily,
        time=time(hour=9, minute=0, tzinfo=india),
        name="daily_affirmation"
    )

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
