# 🎲 Dice Roller Telegram Bot

A simple Telegram bot built with **Python** and **python-telegram-bot** that simulates rolling a six-sided dice. The bot responds with custom dice stickers when available and falls back to text output if the sticker pack cannot be loaded.

## Features

* `/start` command to greet users.
* `/roll` command to roll a random dice (1–6).
* Uses a custom Telegram sticker pack for dice faces.
* Falls back to text-based results if stickers are unavailable.
* Environment variable support for secure bot token storage.

## Project Structure

```text
.
├── bot.py           # Main bot application
├── requirements     # Python dependencies
└── .env             # Environment variables
```

## Requirements

* Python 3.9+
* Telegram Bot Token from BotFather

### Dependencies

```text
python-telegram-bot
python-dotenv
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/dice-roller-bot.git
cd dice-roller-bot
```

### 2. Install Dependencies

```bash
pip install -r requirements
```

### 3. Configure Environment Variables

Create a `.env` file in the project root:

```env
API_TOKEN=your_telegram_bot_token
```

Replace `your_telegram_bot_token` with the token received from BotFather.

## Running the Bot

Start the bot with:

```bash
python bot.py
```

Once running, open Telegram and interact with your bot.

## Commands

| Command  | Description                              |
| -------- | ---------------------------------------- |
| `/start` | Displays a welcome message               |
| `/roll`  | Rolls a dice and returns a random result |

## How It Works

1. The bot loads the Telegram API token from the `.env` file.
2. On startup, it fetches stickers from the `DiceRollBot` sticker pack.
3. Each sticker is mapped to a dice value from 1 to 6.
4. When a user sends `/roll`, a random number between 1 and 6 is generated.
5. The corresponding sticker is sent back to the user. If the sticker is unavailable, the bot sends the result as text.

## Environment Variables

| Variable    | Description            |
| ----------- | ---------------------- |
| `API_TOKEN` | Telegram Bot API token |

## License

This project is open source and available under the MIT License.
