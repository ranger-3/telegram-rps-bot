from telegram.ext import ApplicationBuilder, CommandHandler
from bot.config import settings


async def start(update, context):
    await update.message.reply_text("Hi there!")


def main():
    app = ApplicationBuilder().token(settings.bot_token.get_secret_value()).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()


main()
