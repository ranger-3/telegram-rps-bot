from telegram import Update
from telegram.ext import ContextTypes

from bot.constants import GAME_KEYBOARD, HELP_TEXT, Move
from bot.utils import get_verdict


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Choose your move", reply_markup=GAME_KEYBOARD)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(HELP_TEXT)


async def handle_choice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_choice = Move(update.message.text)
    bot_choice = Move.random()
    verdict = get_verdict(user_choice, bot_choice)
    await update.message.reply_text(bot_choice.value)
    await update.message.reply_text(verdict, reply_markup=GAME_KEYBOARD)


async def handle_other(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Please use the buttons 👇", reply_markup=GAME_KEYBOARD
    )
