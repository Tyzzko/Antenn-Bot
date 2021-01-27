TOKEN = '1428277794:AAFPUnZh5fKmrhVtditxzE9ojsbOuVE-WHA'



'''
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
'''
#from pyorbital import tlefile
from datetime import datetime
from pyorbital.orbital import Orbital
from requests import get

from config import TOKEN
hou = 24
pitch = 20
long_poz = 43.8399 
lat_poz= 55.3948
height_poz = 0

def update_tle():
    file = open("tle.txt", "ab")
    file.write(get("http://www.celestrak.com/NORAD/elements/weather.txt").content)  #
    # print("get tle successfull")
    file.close()


# bot = Bot(token=TOKEN)
# dp = Dispatcher(bot)

tle_file = update_tle()

noaa_18 = Orbital("NOAA-18")
noaa_19 = Orbital("NOAA-19")
noaa_15 = Orbital("NOAA-15")
meteor_m2 = Orbital("METEOR-M 2")
'''
tle_noaa18 = tlefile.read('NOAA 18', tle_file)
tle_noaa19 = tlefile.read('NOAA 19', tle_file)
tle_noaa15 = tlefile.read('NOAA 15', tle_file)
tle_meteor_m2 = tlefile.read('METEOR-M 2', tle_file)
'''
utc_time = datetime.utcnow()
'''
noaa_15_lon, noaa_15_lat, noaa_15_alt = noaa_15.get_lonlatalt(utc_time)
noaa_18_lon, noaa_18_lat, noaa_18_alt = noaa_18.get_lonlatalt(utc_time)
noaa_19_lon, noaa_19_lat, noaa_19_alt = noaa_19.get_lonlatalt(utc_time)
meteor_m2_lon, meteor_m2_lat, meteor_m2_alt = meteor_m2.get_lonlatalt(utc_time)
'''
print(utc_time)
passes = {'noaa15': noaa_15.get_next_passes(utc_time, hou, long_poz, lat_poz, height_poz, tol=0.001, horizon=pitch),
          'noaa18': noaa_18.get_next_passes(utc_time, hou, long_poz, lat_poz, height_poz, tol=0.001, horizon=pitch),
          'noaa19': noaa_19.get_next_passes(utc_time, hou, long_poz, lat_poz, height_poz, tol=0.001, horizon=pitch),
          'meteor_m2': meteor_m2.get_next_passes(utc_time, hou, long_poz, lat_poz,
                                                 height_poz, tol=0.001, horizon=pitch)}
print()
for i in (passes['noaa15']):
    for a in i:
        print(a)
    print()



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
