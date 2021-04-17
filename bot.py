from datetime import timedelta
from config import TOKEN
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram import Bot, Dispatcher, executor
from datetime import datetime
from main import passes

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def send_photos(message: types.Message):
    for _ in range(1):          #satellite.current_photos
        positively = 0
        for i in passes:
            for j in passes[i]:
                while j[2] + timedelta(minutes=2) != datetime.now():
                    positively = 1
                if positively != 0:
                    await bot.send_message(message.chat.id, 'есть контакт!')
        # path = f'C:/cartinki/cartinki/mcir/{i}'
        # cap = f'{satellite.current_photos[0].split("-"[:2]), datetime.now()}'
        # await bot.send_photo(message.chat.id, path, cap)


if __name__ == '__main__':
    executor.start_polling(dp)
