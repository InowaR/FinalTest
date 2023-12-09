from datetime import datetime

from python.model.registry import Registry


class Service:
    def __init__(self):
        self.dog_id = 0
        self.cat_id = 0
        self.hamster_id = 0
        self.horse_id = 0
        self.camel_id = 0
        self.donkey_id = 0
        self.registry = Registry()
        self.registry.load_animals()

    def create_animal(self, animal_number):
        if animal_number == "1":
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
                                     "гав", datetime(2023, 1, 1), ["Cидеть", "Голос", "Ко мне"])
            for dog in self.registry.list_dogs:
                dog.number = self.dog_id
                self.dog_id += 1
        elif animal_number == "2":
            # number = self.cat_id
            # color = input("Введите цвет кошки:")
            # name = "Кошка"
            # lifetime = 10
            # mass = input("Введите вес кошки:")
            # sex = input("Введите пол кошки:")
            # price = input("Введите цену кошки:")
            # nickname = input("Введите имя кошки:")
            # breed = input("Введите породу кошки:")
            # sound = "мяу"
            # date_of_birth = input("Введите дату рождения кошки:")
            # commands = input("Введите команды кошки:")
            # self.registry.create_cat(number, color, name, lifetime, mass, sex, price, nickname, breed, sound,
            #                          date_of_birth, commands)
            self.registry.create_cat(self.cat_id, "белый", "кошка", 10, 3, "мужской", 10000, "Киса",
                                     "Сиамская", "мяу", datetime(2023, 1, 1), ["Cидеть", "Голос", "Ко мне"])
            for cat in self.registry.list_cats:
                cat.number = self.cat_id
                self.cat_id += 1
        elif animal_number == "3":
            # number = self.hamster_id
            # color = input("Введите цвет хомяка:")
            # name = "Хомяк"
            # lifetime = 10
            # mass = input("Введите вес хомяка:")
            # sex = input("Введите пол хомяка:")
            # price = input("Введите цену хомяка:")
            # nickname = input("Введите имя хомяка:")
            # breed = input("Введите породу хомяка:")
            # sound = "чирк"
            # date_of_birth = input("Введите дату рождения хомяка:")
            # commands = input("Введите команды хомяка:")
            # self.registry.create_hamster(number, color, name, lifetime, mass, sex, price, nickname, breed, sound,
            #                          date_of_birth, commands)
            self.registry.create_hamster(self.cat_id, "серый", "хомяк", 10, 3, "мужской", 10000, "Толстик",
                                         "Степной", "чирк", datetime(2023, 1, 1), ["Cидеть", "Голос", "Ко мне"])
            for hamster in self.registry.list_hamsters:
                hamster.number = self.hamster_id
                self.hamster_id += 1
        elif animal_number == "4":
            # number = self.horse_id
            # color = input("Введите цвет лошади:")
            # name = "Лошадь"
            # lifetime = 10
            # mass = input("Введите вес лошади:")
            # sex = input("Введите пол лошади:")
            # lifting_capacity = int(input("Введите грузоподъемность животного:"))
            # breed = input("Введите породу лошади:")
            # sound = "игого"
            # date_of_birth = input("Введите дату рождения лошади:")
            # commands = input("Введите команды лошади:")
            # self.registry.create_horse(number, color, name, lifetime, mass, sex, price, lifting_capacity, sound,
            #                          date_of_birth, commands)
            self.registry.create_horse(self.horse_id, "красный", "лошадь", 10, 3, "мужской", 90, "красная",
                                       "игого", datetime(2023, 1, 1), ["Cидеть", "Голос", "Ко мне"])
            for horse in self.registry.list_horses:
                horse.number = self.horse_id
                self.horse_id += 1
        elif animal_number == "5":
            # number = self.camel_id
            # color = input("Введите цвет верблюда:")
            # name = "Верблюд"
            # lifetime = 10
            # mass = input("Введите вес верблюда:")
            # sex = input("Введите пол верблюда:")
            # lifting_capacity = int(input("Введите грузоподъемность животного:"))
            # breed = input("Введите породу верблюда:")
            # sound = "гав"
            # date_of_birth = input("Введите дату рождения верблюда:")
            # commands = input("Введите команды верблюда:")
            # self.registry.create_camel(number, color, name, lifetime, mass, sex, price, lifting_capacity, sound,
            #                          date_of_birth, commands)
            self.registry.create_camel(self.camel_id, "желтый", "верблюд", 10, 3, "мужской", 90, "тихий",
                                       "охо", datetime(2023, 1, 1), ["Cидеть", "Голос", "Ко мне"])
            for camel in self.registry.list_camels:
                camel.number = self.camel_id
                self.camel_id += 1
        elif animal_number == "6":
            # number = self.donkey_id
            # color = input("Введите цвет осла:")
            # name = "Осел"
            # lifetime = 10
            # mass = input("Введите вес осла:")
            # sex = input("Введите пол осла:")
            # lifting_capacity = int(input("Введите грузоподъемность животного:"))
            # breed = input("Введите породу осла:")
            # sound = "гав"
            # date_of_birth = input("Введите дату рождения осла:")
            # commands = input("Введите команды осла:")
            # self.registry.create_donkey(number, color, name, lifetime, mass, sex, price, lifting_capacity, sound,
            #                          date_of_birth, commands)
            self.registry.create_donkey(self.donkey_id, "серый", "осел", 10, 3, "мужской", 90, "ослик",
                                        "иа", datetime(2023, 1, 1), ["Cидеть", "Голос", "Ко мне"])
            for donkey in self.registry.list_donkeys:
                donkey.number = self.donkey_id
                self.donkey_id += 1

    def show_registry(self, animal_number):
        self.registry.show_registry(animal_number)

    def sort_by_date_of_birth(self, animal_number):
        self.registry.sort_by_date_of_birth(animal_number)

    def save_animals(self, animal_number):
        self.registry.save_animals(animal_number)

    def show_commands(self, animal_number):
        # number = input("Введите ID собаки:")
        number = 0
        animal = self.registry.find_animal_by_id(number, animal_number)
        print("Список команд")
        print(animal.commands)

    def add_new_command(self, animal_number):
        # number = input("Введите ID собаки:")
        number = 0
        animal = self.registry.find_animal_by_id(number, animal_number)
        # command = input("Введите команду:")
        command = "Рядом"
        animal.commands.append(command)
        print("Список команд")
        print(animal.commands)
