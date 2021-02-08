from main import satellite
from config import TOKEN
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram import Bot, Dispatcher, executor
import sqlite3
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['help'])
async def send_photos(message: types.Message):
    for i in satellite.current_photos:
        path = f'C:/cartinki/cartinki/mcir/{i}'
        cap = f'{satellite.current_photos[0].split("-"[:2]), datetime.now()}'
        await bot.send_photo(message.chat.id, path, cap)


if __name__ == '__main__':
    executor.start_polling(dp)
