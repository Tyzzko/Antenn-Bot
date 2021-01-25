from threading import Thread
from time import sleep
# Функция доп потока 
def func():
    while True:
        print('Temp_1')
        sleep(0.2)
# Две строчки для распаралеливания процессов 
th = Thread(target=func)
th.start()
# Основной поток 
while True:
    print(12345)
    sleep(2)