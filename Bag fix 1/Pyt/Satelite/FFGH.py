

#ААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААА
import datetime
import os
from Satelite import GetSatPos
#Az, Vi = get_SatPos(temp)
#print (Az, Vi, sep = "\n")
def LorettPlay(timeStart, Az, Vi):
    file = open('Track.txt', 'w')
    file.write('Satellite: NOAA-18\nStart date & time: ' + str(timeStart.year) + '-' + str(timeStart.month) + '-' + str(timeStart.day) + '   '  + str(timeStart.hour) + ':' + str(timeStart.minute) + ':' + str(timeStart.second) + ' UTC\nOrbit: 32474\n\nTime (UTC)   Azimuth (deg:min)   Elevation (deg:min)\n\n') #заполняем шапку программы
    #
    i = 0
    Az12 = []
    Vi12 = []
    d = None
    h = 0
    j = 0
    for d in Az:#переводим азимут в градусы и минуты
        h = int(d//1)           #Математика \/
        j = int(d % 1 / (1/60))
        if h < 100:
            h = '0' + str(h)
            if int(h) < 10:
                h = '0' + h
        if j < 10:
            j = '0' + str(j)
        Az12.append(str(h) + ':' + str(j))#Записываем в cписок
    #
    #
    for d in Vi:#переводим высоту в градусы и минуты
        h = int(d)             #Математика \/
        j = int(d % 1 / (1/60))
        if h < 100:
            h= '0' + str(h)
        if j < 10:
            j = '0' + str(j)
        Vi12.append(str(h) + ':' + str(j))#Записываем в список
    #
    h = 0
    for d in Vi12:#Записываем в файл наши данные
        file.write(str(timeStart.hour) + ':' + str(timeStart.minute) + ':' + str(timeStart.second) + '   ' + Az12[int(h)] + '   ' + '0' + Vi12[int(h)] + '\n')
        h += 1
    #
    os.system('start C:/Users/student/Downloads/release_3_808/release_3_808/loret.exe')#
    print('Всё блять')

def SDRTest():
    print('bhj')

#LorettPlay(temp,Az , Vi)