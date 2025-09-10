import pytest

from bot.constants import GAME_KEYBOARD, HELP_TEXT, Move
from bot.handlers import (
    handle_choice,
    handle_other,
    help_command,
    start_command,
)


@pytest.mark.asyncio
async def test_start_command(fake_update, fake_context):
    update = fake_update()
    await start_command(update, fake_context)

    update.message.reply_text.assert_called_once_with(
        "Choose your move", reply_markup=GAME_KEYBOARD
    )


@pytest.mark.asyncio
async def test_help_command(fake_update, fake_context):
    update = fake_update()
    await help_command(update, fake_context)

    update.message.reply_text.assert_called_once_with(HELP_TEXT)


@pytest.mark.parametrize(
    "user_move,bot_move,expected",
    [
        (Move.ROCK, Move.SCISSORS, "You win! 🎉"),
        (Move.ROCK, Move.PAPER, "Bot wins! 🤖"),
        (Move.ROCK, Move.ROCK, "It's a draw!"),
        (Move.SCISSORS, Move.PAPER, "You win! 🎉"),
        (Move.SCISSORS, Move.ROCK, "Bot wins! 🤖"),
        (Move.SCISSORS, Move.SCISSORS, "It's a draw!"),
        (Move.PAPER, Move.ROCK, "You win! 🎉"),
        (Move.PAPER, Move.SCISSORS, "Bot wins! 🤖"),
        (Move.PAPER, Move.PAPER, "It's a draw!"),
    ],
)
@pytest.mark.asyncio
async def test_handle_choice_outcomes(
    user_move, bot_move, expected, fake_update, fake_context, mocker
):
    mocker.patch("bot.constants.Move.random", return_value=bot_move)
    update = fake_update(user_move.value)

    await handle_choice(update, fake_context)

    first_call = update.message.reply_text.await_args_list[0]
    second_call = update.message.reply_text.await_args_list[1]

    assert first_call.args == (bot_move.value,)
    assert second_call.args == (expected,)
    assert second_call.kwargs.get("reply_markup") == GAME_KEYBOARD


@pytest.mark.parametrize(
    "user_input",
    [
        "invalid input",
        "🔥",
        "❤️",
        "rock",
        "123",
        "✈️",
        "🪨✂️",
        "",
        "   ",
    ],
)
@pytest.mark.asyncio
async def test_handle_other_with_invalid_inputs(user_input, fake_update, fake_context):
    update = fake_update(user_input)

    await handle_other(update, fake_context)

    update.message.reply_text.assert_called_once_with(
        "Please use the buttons 👇", reply_markup=GAME_KEYBOARD
    )
