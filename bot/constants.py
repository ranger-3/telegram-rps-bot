import re
import secrets
from enum import StrEnum
from re import Pattern
from typing import Final, Self

from telegram import ReplyKeyboardMarkup


class Move(StrEnum):
    ROCK = "🪨"
    PAPER = "📄"
    SCISSORS = "✂️"

    def beats(self, other: Self) -> bool:
        return WINS_OVER[self] == other

    @classmethod
    def random(cls) -> Self:
        return secrets.choice(list(cls))


WINS_OVER: Final = {
    Move.ROCK: Move.SCISSORS,
    Move.SCISSORS: Move.PAPER,
    Move.PAPER: Move.ROCK,
}

GAME_KEYBOARD: Final = ReplyKeyboardMarkup(
    [[move.value] for move in Move], resize_keyboard=True
)

BUTTON_PATTERN: Final[Pattern[str]] = re.compile(
    rf"^({'|'.join(re.escape(move.value) for move in Move)})$"
)

HELP_TEXT: Final = (
    f"{Move.ROCK.value}  beats  {Move.SCISSORS.value}\n\n"
    f"{Move.SCISSORS.value}  beats  {Move.PAPER.value}\n\n"
    f"{Move.PAPER.value}  beats  {Move.ROCK.value}"
)
