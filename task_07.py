# Необходимо дополнить "Практическое задание №6" таким образом, чтобы в
# конце программы мы вызвали статический метод родительского класса Animal,
# который вывел бы нам количество всех созданных экземпляров.


class Animal:
    number_of_instances = 0

    def __init__(self):
        Animal.number_of_instances += 1

    @staticmethod
    def print_number_of_instances():
        print('\nКоличество экземпляров класса Animal: ', Animal.number_of_instances)

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

Animal.print_number_of_instances()
