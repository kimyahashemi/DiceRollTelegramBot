from telegram import Update
from telegram.ext import (Application,CommandHandler,ContextTypes)
from telegram.request import HTTPXRequest
import os
from dotenv import load_dotenv
from random import randint

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

PACK_NAME = "DiceRollBot"
DICE_STICKERS = {}

EMOJI_TO_NUMBER = {
    "1⃣": 1,
    "2⃣": 2,
    "3⃣": 3,
    "4⃣": 4,
    "5⃣": 5,
    "6⃣": 6,}


async def load_stickers(app: Application):
    global DICE_STICKERS

    pack = await app.bot.get_sticker_set(PACK_NAME)

    for sticker in pack.stickers:
        if sticker.emoji in EMOJI_TO_NUMBER:
            DICE_STICKERS[
                EMOJI_TO_NUMBER[sticker.emoji]
            ] = sticker.file_id


async def post_init(app: Application):
    await load_stickers(app)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    await update.message.reply_text(
        f"Hello {user.first_name or ''}, "
        f"Welcome Dice Roller Bot!\n"
        f"Type /roll to roll a dice!")

async def roll_dice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    dice_number = randint(1, 6)

    sticker_id = DICE_STICKERS.get(dice_number)

    if sticker_id:
        await update.message.reply_sticker(sticker=sticker_id)
    else:
        await update.message.reply_text(
            f"🎲 You rolled: {dice_number}"
        )


if __name__ == "__main__":

    request = HTTPXRequest(connect_timeout=30,read_timeout=30)

    app = (Application.builder().token(API_TOKEN).request(request).post_init(post_init).build())

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("roll", roll_dice))

    app.run_polling(poll_interval=3)
