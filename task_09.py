# Необходимо создать два параллельных потока, каждый из которых выводил бы
# на экран числа от 10 до 1 в обратном порядке с интервалом в одну секунду.
# В выводе должно быть понятно какая нить выполняется, и когда каждая из них
# начинает и заканчивает своё выполнение.

import threading
import time

"""Класс PrintNumberThread используется для вывода чисел от 10 до 1 с заданным интервалом.
Интервал и номер потока задаются при создании экземпляра класса.
"""
class PrintNumberThread(threading.Thread):
    def __init__(self, interval=1, number=0):
        threading.Thread.__init__(self)
        self.interval = interval
        self.number = number

    def run(self):
        print(f'Время начала работы потока {self.number}: {time.ctime()}')
        for i in range(1, 11)[::-1]:
            print(f'{" "*25*self.number}Число = {i} Номер потока: {self.number}')
            time.sleep(self.interval)
        print(f'Время окончания работы потока {self.number}: {time.ctime()}')


potok_one = PrintNumberThread(1, 1)
potok_one.start()
time.sleep(2.5) # задержка для наглядности, чтобы время старта и окончания потоков 1 и 2 было разным
potok_two = PrintNumberThread(1, 2)
potok_two.start()
