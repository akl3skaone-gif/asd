from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# BotFather'dan aldığın token'ı buraya yaz
import os
BOT_TOKEN = os.getenv("BOT_TOKEN")



bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    text = (
        "👋 Welcome to *Trade Levand*, your trusted platform for crypto investments and trading insights.\n\n"
        "We offer expert-selected strategies and market analysis designed to maximize your profits while minimizing risk.\n\n"
        "🔐 Log in to our site to access reliable data."
    )

    keyboard = types.InlineKeyboardMarkup()
    webapp_button = types.InlineKeyboardButton(
        text="🌐 Open Trade Levand",
        web_app=types.WebAppInfo(url="https://tradelevand.xo.je")  # ← siten burada
    )
    keyboard.add(webapp_button)

    await message.answer(text, parse_mode="Markdown", reply_markup=keyboard)

if __name__ == "__main__":
    print("✅ Trade Levand bot is running...")
    executor.start_polling(dp, skip_updates=True)


