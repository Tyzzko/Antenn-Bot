from datetime import datetime  # импорт внешних модулей
import dp as dp
import asyncio
from aiogram.types import message
from pyorbital.orbital import Orbital
from requests import get




def update_tle():  # функция обнавления tle файлов
    file = open("tle.txt", "ab")
    file.write(get("http://www.celestrak.com/NORAD/elements/weather.txt").content)
    file.close()


class Satellite_Bot:
    hou = 24  # кол-во часов для расчета пролетов
    pitch = 11  # мин высота
    long_poz = 43.8399  # долгота широта высота
    lat_poz = 55.3948
    height_poz = 0
    update_time = 0

    # Функция для расчета пролетов для спутников работающих в укв диапазоне
    def calculation_satellite(self):
        ###
        # тут надо написать условие обнавления tle (померить время и если разница больше чем три дня то обнавляем)
        if Satellite_Bot.update_time == 0 or \
                str((Satellite_Bot.update_time - (datetime.date(datetime.now())))).split('-')[-1] == '03':
            Satellite_Bot.update_time = (datetime.date(datetime.now()))
            update_tle()
        self.utc_time = datetime.utcnow()
        self.noaa_18 = Orbital("NOAA-18", tle_file='tle.txt')
        self.noaa_19 = Orbital("NOAA-19", tle_file='tle.txt')
        self.noaa_15 = Orbital("NOAA-15", tle_file='tle.txt')
        self.meteor_m2 = Orbital("METEOR-M 2", tle_file='tle.txt')

        self.plans_noaa15 = self.noaa_15.get_next_passes(self.utc_time, Satellite_Bot.hou, Satellite_Bot.long_poz,
                                                         # расчет пролетов
                                                         Satellite_Bot.lat_poz, Satellite_Bot.height_poz, tol=0.001,
                                                         horizon=Satellite_Bot.pitch)
        self.plans_noaa18 = self.noaa_18.get_next_passes(self.utc_time, Satellite_Bot.hou,
                                                         Satellite_Bot.long_poz, Satellite_Bot.lat_poz,
                                                         Satellite_Bot.height_poz, tol=0.001,
                                                         horizon=Satellite_Bot.pitch)
        self.plans_noaa19 = self.noaa_19.get_next_passes(self.utc_time, Satellite_Bot.hou, Satellite_Bot.long_poz,
                                                         Satellite_Bot.lat_poz, Satellite_Bot.height_poz, tol=0.001,
                                                         horizon=Satellite_Bot.pitch)
        self.plans_meteor_m2 = self.meteor_m2.get_next_passes(self.utc_time, Satellite_Bot.hou, Satellite_Bot.long_poz,
                                                              Satellite_Bot.lat_poz, Satellite_Bot.height_poz,
                                                              tol=0.001,
                                                              horizon=Satellite_Bot.pitch)

        self.passes = {'noaa15': self.plans_noaa15,  # конфигурация словаря
                       'noaa18': self.plans_noaa18,
                       'noaa19': self.plans_noaa19,
                       'meteor_m2': self.plans_meteor_m2}
        return self.passes  # Возврат словоря спутник: список пролетов

    def plans_txt_list(self, passes_slovar: dict):
        mass = ['noaa15', 'noaa18', 'noaa19', 'meteor_m2']
        self.plans = open('plans_1.txt', 'w')
        for n in mass:
            for i in passes_slovar[n]:
                self.plans.write(f'{n}\n')
                for a in i:
                    self.plans.write(f'{a}\n')
                self.plans.write('----------\n')

    def loger_start_proger(self):  # Логирование запуска
        self.log = open('log.txt', 'a+')
        self.log.write('Programm_Start: ' + str(datetime.today())[:-7] + '\n')
        self.log.close()

    def loger_stop_proger(self):  # Логирование завершения работы
        self.log = open('log.txt', 'a+')
        self.log.write('Programm_Stop: ' + str(datetime.today())[:-7] + '\n')
        self.log.write('----------\n')
        self.log.close()


satellite = Satellite_Bot()

passes = satellite.calculation_satellite()
print(passes)
photos = []
current_files = []  #список текущих фоток
satellite.plans_txt_list(satellite.calculation_satellite())
for i in passes:
    for j in range(len(passes[i])):
       if passes[i][j][1] + datetime.timedelta(minutes=5) == datetime.now():
           pass

