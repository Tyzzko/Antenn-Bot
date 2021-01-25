from datetime import datetime, timedelta
from pyorbital.orbital import Orbital
from geocoder import ip
from os import curdir, chdir, getcwd
from os.path import abspath

Version = "0.8b"                                # версия приложения
coord = ip("me")                                # получение голокации     ЕСТЬ БЕДЫ БЕЗ ИНТЕРНЕТА
height = 161 * 0.001                            # высота на над уровнем моря, Хочешь автоматически - плати бабки
Sat = None                                      # отслеживаемый спутник
orb = None                                      # объект Orbital
passes = None                                   # список пролетов
TRACKOrbit = None                               # номер витка !  ФОРМИРОВАТЬ ТРЕК НЕ РАНЕЕ 15 МИНУТ, МОЖЕТ ВОЗНИКНУТЬ ОШИБКА С КОЛИЧЕСТВОМ ВИТКОВ
timeUTC = datetime.utcnow()                     # время UTС



Sats = ["NOAA-18", "NOAA-19", "METEOR-M 2", "METEOR-M2 2","METOP-A", "METOP-B", "METOP-C", "FENGYUN 3A", "FENGYUN 3B", "FENGYUN 3C"]   # список возможных к приему спутников



direct = ""
for i in range(len ( abspath(__file__).rsplit("\\", 50)) - 3 ):               # коректное определение текущей директории ! возможно уже не нужно
    direct += abspath(__file__).rsplit("\\", 50)[i] + "\\"


try:
    print (coord.latlng[0], coord.latlng[1])
except TypeError:                                                              # обработка ошибки подключения к интернету
    print ("No internet connection")
print ()