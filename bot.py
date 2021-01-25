from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from pyorbital import tlefile
from datetime import datetime
from pyorbital.orbital import Orbital
from requests import get

from config import TOKEN

def update_tle():
    file = open("tle.txt", "ab")
    file.write(get("http://www.celestrak.com/NORAD/elements/weather.txt").content)                      #
    # print("get tle successfull")
    file.close()

# bot = Bot(token=TOKEN)
# dp = Dispatcher(bot)

tle_file = update_tle()

tle_noaa18 = tlefile.read('NOAA 18', tle_file)
tle_noaa19 = tlefile.read('NOAA 19', tle_file)
tle_noaa15 = tlefile.read('NOAA 15', tle_file)
tle_meteor_m2 = tlefile.read('METEOR-M 2', tle_file)

orb = Orbital()
now = datetime.utcnow()
lon, lat, alt = Orbital.get_lonlatalt(now)


passes = {'noaa15': Orbital.get_next_passes(datetime.time(), 1, lon, lat, alt, tol=0.001, horizon=0),
          'noaa18': Orbital.get_next_passes(datetime.time(), 24, lon, lat, alt, tol=0.001, horizon=0),
          'noaa19': Orbital.get_next_passes(datetime.time(), 24, lon, lat, alt, tol=0.001, horizon=0),
          'meteor_m2': Orbital.get_next_passes(datetime.time(), 24, lon, lat, alt, tol=0.001, horizon=0)}

print(passes)


# @dp.message_handler(commands=['start'])
# async def process_start_command(message: types.Message):
#     await message.reply("Привет!\nНапиши мне что-нибудь!")
#
#
# @dp.message_handler(commands=['help'])
# async def process_help_command(message: types.Message):
#     await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")
#
#
# @dp.message_handler()
# async def echo_message(msg: types.Message):
#     await bot.send_message(msg.from_user.id, msg.text)
#
#
# if __name__ == '__main__':
#     executor.start_polling(dp)

# print(help(pyorbital))
