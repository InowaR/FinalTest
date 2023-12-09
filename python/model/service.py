from datetime import datetime

from python.model.registry import Registry


class Service:
    def __init__(self):
        self.dog_id = 0
        self.registry = Registry()
        self.registry.load_dogs()

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
        self.registry.create_dog(self.dog_id, "коричневый", "собака", 10, 3, "мужской", 10000, "Барли", "Овчарка",
                                 "гав",
                                 datetime(2023, 1, 1), ["Cидеть", "Голос", "Ко мне"])
        for dog in self.registry.list_dogs:
            dog.number = self.dog_id
            self.dog_id += 1

    def show_registry(self):
        self.registry.show_registry()

    def sort_by_date_of_birth(self):
        self.registry.sort_by_date_of_birth()

    def save_dogs(self):
        self.registry.save_dogs()

    def show_commands(self):
        # number = input("Введите ID собаки:")
        number = 0
        dog = self.registry.find_dog_by_id(number)
        print("Список команд")
        print(dog.commands)

    def add_new_command(self):
        # number = input("Введите ID собаки:")
        number = 0
        dog = self.registry.find_dog_by_id(number)
        # command = input("Введите команду:")
        command = "Рядом"
        dog.commands.append(command)
        print("Список команд")
        print(dog.commands)


