from threading import Thread
from Satelite.config import *
from Satelite.FFGH import LorettPlay



az = []
h = []
def get_SatPos(temp):
    
    while temp <= passes[0][2]:
        az.append(orb.get_observer_look(temp, coord.latlng[1], coord.latlng[0], height)[0])     # азимут
        h.append(orb.get_observer_look(temp, coord.latlng[1], coord.latlng[0], height)[1])      # высота
        temp += timedelta(seconds=1)
    print(az)
    thread._delete
    LorettPlay(passes[0][0], az, h)
    #return  az, h

def ThreadStart(i):         # блять, найс костыль
    thread.start()

temp = passes[0][0]
thread = Thread(target = get_SatPos, args=[temp])                                           # расчет координат спутника в отдельном потоке
#thread.start()


