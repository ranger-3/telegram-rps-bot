# Telegram Rock–Paper–Scissors Bot 🪨📄✂️

A tiny Telegram bot to play Rock–Paper–Scissors.  
Built just for fun — to practice async Python, testing, and Docker.


---

## 🔧 Requirements
- [Docker](https://docs.docker.com/get-docker/)
- Telegram bot token from [@BotFather](https://t.me/botfather)

---

## ✨ What it uses
- [python-telegram-bot](https://pypi.org/project/python-telegram-bot/) (async Telegram Bot API)
- [pydantic-settings](https://pypi.org/project/pydantic-settings/) (for environment config)
- [pytest](https://pypi.org/project/pytest/) + [pytest-asyncio](https://pypi.org/project/pytest-asyncio/) + [pytest-mock](https://pypi.org/project/pytest-mock/) (for tests)

---

## 🛠 Dev tools
- [pre-commit](https://pypi.org/project/pre-commit/) (for automatic linting & formatting on commit)

---
## 🚀 How to run

1. Clone the repo and go into the project folder.  
2. Create a `.env` file with your bot token:
```bash
BOT_TOKEN=your-telegram-bot-token
```
3. Start the bot with Docker Compose:
```bash
docker compose up --build
```
4. Open your bot in Telegram and play 🎉
