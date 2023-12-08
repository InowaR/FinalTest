from datetime import datetime

from python.model.registry import Registry


class Service:
    def __init__(self):
        self.dog_id = 0
        self.registry = Registry()

    def create_dog(self):
        # number = self.dog_id
        # color = input("Введите цвет собаки:")
        # name = "Cобакa"
        # lifetime = 10
        # mass = input("Введите вес собаки:")
        # sex = input("Введите пол собаки:")
        # price = input("Введите цену собаки:")
        # nickname = input("Введите имя собаки:")
        # breed = input("Введите породу собаки:")
        # sound = "гав"
        # date_of_birth = input("Введите дату рождения собаки:")
        # commands = input("Введите команды собаки:")
        # self.registry.create_dog(number, color, name, lifetime, mass, sex, price, nickname, breed, sound,
        #                          date_of_birth, commands)
        self.registry.create_dog(1, "коричневый", "собака", 10, 3, "мужской", 10000, "Барли", "Овчарка", "гав",
                                 datetime(2023, 1, 1), ["Cидеть", "Голос", "Ко мне"])

    def show_registry(self):
        self.registry.show_registry()


s = Service()
s.create_dog()
s.show_registry()
