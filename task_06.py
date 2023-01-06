# Есть класс Animal c одним методом voice().
# class Animal:
# def voice(self):
# pass
# 1. Создать от него три класса наследника и для каждого сделать свою реализацию метода voice().
# 2. Создать по одному экземпляру всех наследников и вызвать для каждого переопределенный метод voice().

class Animal:
    def voice(self):
        pass


class Dog(Animal):
    def voice(self):
        print('hav hav')


class Cat(Animal):
    def voice(self):
        print('mur mur')


class Parrot(Animal):
    def voice(self, st='car car'):
        print(st)


sharik = Dog()
sharik.voice()

murzik = Cat()
murzik.voice()

kesha = Parrot()
kesha.voice()

kesha.voice('popka durtak')
