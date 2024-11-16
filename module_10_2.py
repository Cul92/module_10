import time
import threading


class Knight(threading.Thread):
    lock = threading.Lock()

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        with Knight.lock:
            print(f"{self.name}, на нас напали!")
        enemies = 100
        days = 0
        while enemies > 0:
            time.sleep(1)
            days += 1
            enemies = max(0, enemies - self.power)
            with Knight.lock:
                print(f"{self.name} сражается {days} день(дня)... осталось {enemies} воинов.")

        with Knight.lock:
            print(f"{self.name} одержал победу спустя {days} день(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все сражения завершены.")