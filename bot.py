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
    # satellite.current_photos
    for i in passes:
        for j in passes[i]:
            while j[2] + timedelta(minutes=2) != datetime.now():
                await bot.send_message(message.chat.id, 'есть контакт!')
                break
            break
            # path = f'C:/Program Files (x86)/WXtoImg/Images/"{i}'
            # day, month, minute, second = str(j[0].day), str(j[0].month), str(j[0].minute), str(j[0].second)
            # if len(day) == 1:
            #     day = '0' + day
            # if len(month) == 1:
            #     month = '0' + month
            # if len(minute) == 1:
            #     minute = '0' + minute
            # if len(second) == 1:
            #     second = '0' + second
            # path += f'-{month}{day}{minute}{second}"'
            # con = sqlite3.connect('data_base.sql')
            # cur = con.cursor()
            # result = cur.execute("""SELECT file_name FROM photos
            #             WHERE year = 2010""").fetchall()
            # current_files = os.listdir('C:/Program Files (x86)/WXtoImg/images')
            # satellite.get_current_photos(list(set(current_files).intersection(set(result))))
            # for k in satellite.current_photos:
            #     cur.execute(f'INSERT INTO photos file_name {k}')
            # cap = f'{satellite.current_photos[0].split("-"[:2]), datetime.now()}'
            # await bot.send_photo(message.chat.id, path, cap)


if __name__ == '__main__':
    executor.start_polling(dp)
