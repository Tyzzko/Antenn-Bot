import sdr 
from time import time, sleep
from datetime import datetime
def SDR(name, timeSta, timeSto, timeReal): # sat, timestart, time end, timenow 
    timeProc = time()
    print ("Starting SDR test....")
    SDR = sdr.OSMO_SDR("airspy")

    if SDR.load_config(name):
        while (True):
            DeltaTime = time() - timeProc
            timeRe = datetime(timeReal.year, timeReal.month, int((timeReal.day + (timeReal.hour * 3600 + timeReal.minute * 60 + timeReal.second + DeltaTime) // 86400) % 24), int((timeReal.hour + (timeReal.minute * 60 + timeReal.second + DeltaTime) // 3600) % 60), int((timeReal.minute + (timeReal.second + DeltaTime)//60) % 60), int((timeReal.second + DeltaTime + 10)%60)) 
            if (timeRe == timeSta):
                SDR.start("SDR.iq")
                sleep(timeSto.hour * 3600 - timeSta.hour * 3600 + timeSto.minute * 60 - timeSta.minute * 60 + timeSto.second - timeSta.second + 10)
                SDR.stop()
                break



if (input() == '12'):
    SDR('METEOR-M2 2', datetime(2020, 3, int(input('день')), int(input('Часы')), int(input('минуты')), int(input('секунды'))), datetime(2020, 3, int(input('день')), int(input('Часы')), int(input('минуты')), int(input('секунды'))), datetime.now())
input()