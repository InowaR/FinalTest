from python.model.registry import Registry


class Service:
    def __init__(self):
        self.registry = Registry()
        self.registry.load_animals()
        self.dog_id = len(self.registry.list_dogs)
        self.cat_id = len(self.registry.list_cats)
        self.hamster_id = len(self.registry.list_hamsters)
        self.horse_id = len(self.registry.list_horses)
        self.camel_id = len(self.registry.list_camels)
        self.donkey_id = len(self.registry.list_donkeys)
        self.count = self.dog_id + self.cat_id + self.hamster_id + self.horse_id + self.camel_id + self.donkey_id

    def create_animal(self, animal_number):
        if animal_number == 1:
            number = self.dog_id
            color = input("Введите цвет собаки:")
            name = "Cобакa"
            lifetime = 15
            mass = input("Введите вес собаки:")
            sex = input("Введите пол собаки:")
            price = input("Введите цену собаки:")
            nickname = input("Введите имя собаки:")
            breed = input("Введите породу собаки:")
            sound = "гав"
            date_of_birth = input("Введите дату рождения собаки в формате 2023-01-01 00:00:00:")
            commands = input("Введите команды собаки:")
            self.registry.create_dog(number, color, name, lifetime, mass, sex, price, nickname, breed, sound,
                                     date_of_birth, commands + ' ')
            for dog in self.registry.list_dogs:
                dog.number = self.dog_id
                self.dog_id += 1
        elif animal_number == 2:
            number = self.cat_id
            color = input("Введите цвет кошки:")
            name = "Кошка"
            lifetime = 15
            mass = input("Введите вес кошки:")
            sex = input("Введите пол кошки:")
            price = input("Введите цену кошки:")
            nickname = input("Введите имя кошки:")
            breed = input("Введите породу кошки:")
            sound = "мяу"
            date_of_birth = input("Введите дату рождения кошки в формате 2023-01-01 00:00:00:")
            commands = input("Введите команды кошки:")
            self.registry.create_cat(number, color, name, lifetime, mass, sex, price, nickname, breed, sound,
                                     date_of_birth, commands + ' ')
            for cat in self.registry.list_cats:
                cat.number = self.cat_id
                self.cat_id += 1
        elif animal_number == 3:
            number = self.hamster_id
            color = input("Введите цвет хомяка:")
            name = "Хомяк"
            lifetime = 10
            mass = input("Введите вес хомяка:")
            sex = input("Введите пол хомяка:")
            price = input("Введите цену хомяка:")
            nickname = input("Введите имя хомяка:")
            breed = input("Введите породу хомяка:")
            sound = "чирк"
            date_of_birth = input("Введите дату рождения хомяка в формате 2023-01-01 00:00:00:")
            commands = input("Введите команды хомяка:")
            self.registry.create_hamster(number, color, name, lifetime, mass, sex, price, nickname, breed, sound,
                                         date_of_birth, commands + ' ')
            for hamster in self.registry.list_hamsters:
                hamster.number = self.hamster_id
                self.hamster_id += 1
        elif animal_number == 4:
            number = self.horse_id
            color = input("Введите цвет лошади:")
            name = "Лошадь"
            lifetime = 10
            mass = input("Введите вес лошади:")
            sex = input("Введите пол лошади:")
            lifting_capacity = int(input("Введите грузоподъемность лошади в формате 2023-01-01 00:00:00:"))
            breed = input("Введите породу лошади:")
            sound = "игого"
            date_of_birth = input("Введите дату рождения лошади:")
            commands = input("Введите команды лошади:")
            self.registry.create_horse(number, color, name, lifetime, mass, sex, lifting_capacity, breed, sound,
                                       date_of_birth, commands + ' ')
            for horse in self.registry.list_horses:
                horse.number = self.horse_id
                self.horse_id += 1
        elif animal_number == 5:
            number = self.camel_id
            color = input("Введите цвет верблюда:")
            name = "Верблюд"
            lifetime = 10
            mass = input("Введите вес верблюда:")
            sex = input("Введите пол верблюда:")
            lifting_capacity = int(input("Введите грузоподъемность верблюда:"))
            breed = input("Введите породу верблюда:")
            sound = "охо"
            date_of_birth = input("Введите дату рождения верблюда в формате 2023-01-01 00:00:00:")
            commands = input("Введите команды верблюда:")
            self.registry.create_camel(number, color, name, lifetime, mass, sex, lifting_capacity, breed, sound,
                                       date_of_birth, commands + ' ')
            for camel in self.registry.list_camels:
                camel.number = self.camel_id
                self.camel_id += 1
        elif animal_number == 6:
            number = self.donkey_id
            color = input("Введите цвет осла:")
            name = "Осел"
            lifetime = 10
            mass = input("Введите вес осла:")
            sex = input("Введите пол осла:")
            lifting_capacity = int(input("Введите грузоподъемность осла:"))
            breed = input("Введите породу осла:")
            sound = "иа"
            date_of_birth = input("Введите дату рождения осла в формате 2023-01-01 00:00:00:")
            commands = input("Введите команды осла:")
            self.registry.create_donkey(number, color, name, lifetime, mass, sex, lifting_capacity, breed, sound,
                                        date_of_birth, commands + ' ')
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
        number = int(input("Введите ID животного:"))
        animal = self.registry.find_animal_by_id(number, animal_number)
        print("Список команд")
        print(animal.commands)

    def add_new_command(self, animal_number):
        number = int(input("Введите ID животного:"))
        animal = self.registry.find_animal_by_id(number, animal_number)
        command = input("Введите новую команду для животного:")
        animal.commands.append(command)
        print("Список команд")
        print(animal.commands)
