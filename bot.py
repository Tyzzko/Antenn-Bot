from config import TOKEN
import logging
from aiogram import Bot, Dispatcher, executor, types
from datetime import datetime, timedelta
from main import passes, satellite
import os
import sqlite3

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def send_photos(message: types.Message):
    while True:
        for i in passes:
            for j in passes[i]:
                if j[1] + timedelta(minutes=2) == datetime.now():
                    day, month, minute, second = str(j[0].day), str(j[0].month), str(j[0].minute), str(j[0].second)
                    if len(day) == 1:
                        day = '0' + day
                    if len(month) == 1:
                        month = '0' + month
                    if len(minute) == 1:
                        minute = '0' + minute
                    if len(second) == 1:
                        second = '0' + second
                    path = f'C:/Program Files (x86)/WXtoImg/Images/"{i}-{month}{day}{minute}{second}"'
                    con = sqlite3.connect('data_base.sql')
                    cur = con.cursor()
                    sql_req = f'SELECT file_name FROM photos WHERE file_name = "{i}-{month}{day}{minute}{second}"'
                    result = cur.execute(sql_req).fetchall()
                    current_files = os.listdir('C:/Program Files (x86)/WXtoImg/imagels')
                    file = list(set(current_files).intersection(set(result)))
                    cur.execute(f'INSERT INTO photos file_name {file[0]}')
                    await bot.send_message(message.chat.id, j)
                    await bot.send_photo(message.chat.id, path, file[0])
                else:
                    await bot.send_message(message.chat.id, 'спутников нема(')


if __name__ == '__main__':
    executor.start_polling(dp)
