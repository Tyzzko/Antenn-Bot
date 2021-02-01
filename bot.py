from aiohttp.web_routedef import get
from main import satellite
from config import TOKEN
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram import Bot, Dispatcher, executor


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['help'])
async def send_photos(message: types.Message):
    await bot.send_photo(message.chat.id, get("img/kot1.png").content)



if __name__ == '__main__':
    executor.start_polling(dp)


