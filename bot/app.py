from telegram import BotCommand
from telegram.ext import (
    Application,
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
)

from bot.config import settings
from bot.constants import BUTTON_PATTERN
from bot.handlers import handle_choice, handle_other, help_command, start_command


async def post_init(app: Application) -> None:
    await app.bot.set_my_commands(
        [
            BotCommand("start", "Start the game"),
            BotCommand("help", "How to play"),
        ]
    )


def main() -> None:
    app = (
        ApplicationBuilder()
        .token(settings.bot_token.get_secret_value())
        .post_init(post_init)
        .build()
    )

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(
        MessageHandler(filters.TEXT & filters.Regex(BUTTON_PATTERN), handle_choice)
    )
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_other))

    app.run_polling()


if __name__ == "__main__":
    main()
