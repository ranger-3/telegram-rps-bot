from bot.constants import Move


def get_verdict(user: Move, bot: Move) -> str:
    if user == bot:
        return "It's a draw!"
    if user.beats(bot):
        return "You win! 🎉"
    return "Bot wins! 🤖"
