from threading import Thread
from Satelite.config import chdir, direct, getcwd, coord, Sat, orb, height, timedelta, timeUTC, Orbital, TRACKOrbit
from datetime import datetime, date
from subprocess import call, Popen
from requests import get

az = []                                         # список азимутов во время приема посекудно 
h = []                                          # список высот во время приема посекудно 
time = []                                       
Sat = 0

# беды без интернета
# в track пишем номер витка
# запускать программу loret от админа
# ПОЧЕМУ НЕ ПАШЕТ GPS
# исключения




def AutoUpdate_tle():

    try:
        file = open("tle.txt", "r")
        fixdate = file.readline().split("\n")[0]
    
        if date.today() > date(int(fixdate.split(".")[2]), int(fixdate.split(".")[1]), int(fixdate.split(".")[0])):         # проверяем прошел ли хотябы день с момента заграски tle
            update_tle(1)
    
        file.close

    except FileNotFoundError:
        update_tle(1)


def update_tle(i):
    
    file = open("tle.txt", "w")
    print(datetime.today().strftime("%d.%m.%Y"))
    file.write(datetime.today().strftime("%d.%m.%Y") + "\n")
    file.close

    file = open("tle.txt", "ab")
    file.write(get("http://www.celestrak.com/NORAD/elements/weather.txt").content)                      # загружаем актуальные tle
    print("get tle successfull")
    file.close


def ChooseSAT(sender):                                                                                  # Принудительно обновляем tle ! требуется переписать систему обработки исключений
    try:
        print("Выбор")
        orb = Orbital( sender.text, direct + "Pyt\\tle.txt")
        global Sat
        Sat = sender.text
        print (Sat)
        
        try:
            passes = orb.get_next_passes(timeUTC, 48, coord.latlng[1], coord.latlng[0], height, tol=0.001, horizon=57) # расчет пролетов
            print(passes)
            
            try:
                firstPasse = passes[0][0]

            except IndexError:
                print("No passes")
                firstPasse = None

        except TypeError:
            print ("No internet connection")
        
    except FileNotFoundError:
        
        print ("Warning: File tle not found")
        Sat = sender.text
        orb = Orbital(sender.text)
        print (Sat)
        firstPasse = passes[0][0]
        passes = orb.get_next_passes(timeUTC, 48, coord.latlng[1], coord.latlng[0], height, tol=0.001, horizon=57) # расчет пролетов
        
    except KeyError:
        
        print("Warning: Found no TLE entry for {}, The default value is set".format(sender.text))  
        Sat = sender.text
        orb = Orbital(sender.text)
        #orb.orbit_elements.
        print (Sat)
        firstPasse = passes[0][0]
        passes = orb.get_next_passes(timeUTC, 48, coord.latlng[1], coord.latlng[0], height, tol=0.001, horizon=57) # расчет пролетов
    

def get_SatPos(firstPasse, passes, orb):                                                                        # генерация алгоритма для манипулятора
    global az, h, time, Sat
    
    while firstPasse <= passes[0][1]:
        az.append(orb.get_observer_look(firstPasse, coord.latlng[1], coord.latlng[0], height)[0])               # азимут
        h.append(orb.get_observer_look(firstPasse, coord.latlng[1], coord.latlng[0], height)[1])                # высота
        time.append(firstPasse)
        firstPasse += timedelta(seconds=1)
    lorettPlay(passes[0][0], az, h, Sat, TRACKOrbit)
    az = []; h = []; time= []


def ThreadStart(i):
    global Sat, TRACKOrbit                                                                                      # блять, найс костыль ! нужжно переделать
    orb  = Orbital(Sat, direct + "Pyt\\tle.txt")                    
    TRACKOrbit = orb.get_orbit_number( timeUTC, tbus_style = False )                                            # подсчет номера витка                  
    passes = orb.get_next_passes(timeUTC, 48, coord.latlng[1], coord.latlng[0], height, tol=0.001, horizon=57)  # расчет пролетов
    get_SatPos(passes[0][0], passes, orb)

def ThreadTestStart(i):                                                                                         # запуск программы lorett в режиме корректировки
    print("ЙОУ СОБАКИ, Я НАРУТО УЗУМАКИ")
    program = direct + "loret.exe adm"
    process = Popen(program)
    


def setLorettIni():                                                                                             # редактирование параметров lorett.ini
    file = open(direct + "lorett.ini", "r")
    data = file.readlines()

    for i in range(len(data)):
        if i == 4:
            data[i] = direct + "\Track.txt\n"
    file.close

    file = open(direct + "lorett.ini", "w")

    for i in data:
        file.write(i)
    file.close




def lorettPlay(timeStart, Az, Vi, Sat, TRACKOrbit):                                                             # запись файла Track.txt ! однозначно переделывать
    print(Sat)
    print(TRACKOrbit)
    setLorettIni()
    for i in range(len(az)):
        print (i + 1,") az = ", az[i], "h = ", Vi[i], " time: ", time[i])   

    file = open(direct + 'Track.txt', 'w')
    file.write('Satellite: {}\nStart date & time: '.format(Sat) + str(timeStart.year) + '-' + str(timeStart.month // 10) + str(timeStart.month % 10) + '-' + str(timeStart.day // 10) + str(timeStart.day % 10) + '   '  + str(timeStart.hour // 10) + str(timeStart.hour % 10) + ':' + str(timeStart.minute // 10) + str(timeStart.minute % 10) + ':' + str(timeStart.second // 10) + str(timeStart.second % 10) + ' UTC\nOrbit: 32474\n\nTime (UTC)   Azimuth (deg:min)   Elevation (deg:min)\n\n') #заполняем шапку программы
    
    
    Az12 = []
    Vi12 = []

    for d in Az:                                                                                                # переводим азимут в градусы и минуты
        h = int(d//1)                                                                       
        j = int(d % 1 / (1/60))

        if h < 100:
            h = '0' + str(h)

            if int(h) < 10:
                h = '0' + h

        if j < 10:
            j = '0' + str(j)

        Az12.append(str(h) + ':' + str(j))                                                  
    
    
    for d in Vi:                                                                                                # переводим высоту в градусы и минуты

        h = int(d)                                                                         
        j = int(d % 1 / (1/60))

        if h < 100:
            h= '0' + str(h)
            if int(h) < 10:
                h = '0' + h 

        if j < 10:
            j = '0' + str(j)

        Vi12.append(str(h) + ':' + str(j))                                                  
    
    h = 0
    
    for d in Vi12:                                                                                              # записываем в файл данные ! явно нужно переписать
        file.write(str((timeStart.hour + h // 3600) // 10) + str((timeStart.hour + h // 3600) % 10) + ':' + str((timeStart.minute + h // 60 - (h // 60 + timeStart.minute) // 60 * 60) // 10) + str((timeStart.minute + h // 60 - (h // 60 + timeStart.minute) // 60 * 60)%10) + ':' + str((timeStart.second + h - (h + timeStart.second) // 60 * 60)//10) + str((timeStart.second + h - (h + timeStart.second) // 60 * 60)%10) + '   ' + Az12[int(h)] + '   ' + Vi12[int(h)] + '\n')
        h += 1
    file.close

                                                                                                                # записываем в файл номер витка ! похорошему переделать
    file = open(direct + "Track.txt", "r")
    data = file.readlines()

    for i in range(len(data)):
        if i == 2:
            data[i] = "Orbit: " + str(TRACKOrbit)
    file.close


    file = open(direct + "Track.txt", "w")

    for i in data:
        file.write(i)

    file.close
    
    
    file.close
    chdir(direct)
    print("\n dir = ", getcwd(), "\n")
    program = direct + "loret.exe"
    print (program)
    #process = Popen(program)                                                                                   # открываем программу lorett в дежурном режиме 