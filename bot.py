from aiogram import Dispatcher, Bot
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import asyncio

import payments
from config import BOT_TOKEN

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Hello! Want to buy product? /buy")

@dp.message(Command("buy"))
async def buy(message: Message):
    await payments.buy_product(message)

if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
    print("Bot is running!")