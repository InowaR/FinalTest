import csv
from datetime import datetime
from tabulate import tabulate

from python.model.animal import *


class Registry:
    def __init__(self):
        self.list_dogs: List[Dog] = []
        self.list_cats: List[Cat] = []
        self.list_hamsters: List[Hamster] = []
        self.list_horses: List[Horse] = []
        self.list_camels: List[Camel] = []
        self.list_donkeys: List[Donkey] = []

    def show_registry(self, number):
        if number == '1':
            print("Собаки")
            headers = None
            dogs = []
            for dog in self.list_dogs:
                headers = dog.info()[0]
                dogs.append(dog.info()[1])
            try:
                print(tabulate(dogs, headers=headers, tablefmt='grid', stralign='center'))
            except TypeError:
                print("Пусто")
            # ----------------------------------------------------------------------------
        elif number == '2':
            print("Кошки")
            headers = None
            cats = []
            for cat in self.list_cats:
                headers = cat.info()[0]
                cats.append(cat.info()[1])
            try:
                print(tabulate(cats, headers=headers, tablefmt='grid', stralign='center'))
            except TypeError:
                print("Пусто")
            # ----------------------------------------------------------------------------
        elif number == '3':
            print("Хомяки")
            headers = None
            hamsters = []
            for hamster in self.list_hamsters:
                headers = hamster.info()[0]
                hamsters.append(hamster.info()[1])
            try:
                print(tabulate(hamsters, headers=headers, tablefmt='grid', stralign='center'))
            except TypeError:
                print("Пусто")
            # ----------------------------------------------------------------------------
        elif number == '4':
            print("Лошади")
            headers = None
            horses = []
            for horse in self.list_horses:
                headers = horse.info()[0]
                horses.append(horse.info()[1])
            try:
                print(tabulate(horses, headers=headers, tablefmt='grid', stralign='center'))
            except TypeError:
                print("Пусто")
            # ----------------------------------------------------------------------------
        elif number == '5':
            print("Верблюды")
            headers = None
            camels = []
            for camel in self.list_camels:
                headers = camel.info()[0]
                camels.append(camel.info()[1])
            try:
                print(tabulate(camels, headers=headers, tablefmt='grid', stralign='center'))
            except TypeError:
                print("Пусто")
            # ----------------------------------------------------------------------------
        elif number == '6':
            print("Ослы")
            headers = None
            donkeys = []
            for donkey in self.list_donkeys:
                headers = donkey.info()[0]
                donkeys.append(donkey.info()[1])
            try:
                print(tabulate(donkeys, headers=headers, tablefmt='grid', stralign='center'))
            except TypeError:
                print("Пусто")
            # ----------------------------------------------------------------------------

    def create_dog(self, number, color, name, lifetime, mass, sex, price, nickname, breed, sound, date_of_birth,
                   commands):
        dog = Dog(number, color, name, lifetime, mass, sex, price, nickname, breed, sound, date_of_birth,
                  commands)
        self.list_dogs.append(dog)

    def create_cat(self, number, color, name, lifetime, mass, sex, price, nickname, breed, sound, date_of_birth,
                   commands):
        cat = Cat(number, color, name, lifetime, mass, sex, price, nickname, breed, sound, date_of_birth,
                  commands)
        self.list_cats.append(cat)

    def create_hamster(self, number, color, name, lifetime, mass, sex, price, nickname, breed, sound, date_of_birth,
                       commands):
        hamster = Hamster(number, color, name, lifetime, mass, sex, price, nickname, breed, sound, date_of_birth,
                          commands)
        self.list_hamsters.append(hamster)

    def create_horse(self, number, color, name, lifetime, mass, sex, lifting_capacity, breed, sound, date_of_birth,
                     commands):
        horse = Horse(number, color, name, lifetime, mass, sex, lifting_capacity, breed, sound, date_of_birth,
                      commands)
        self.list_horses.append(horse)

    def create_camel(self, number, color, name, lifetime, mass, sex, lifting_capacity, breed, sound, date_of_birth,
                     commands):
        camel = Camel(number, color, name, lifetime, mass, sex, lifting_capacity, breed, sound, date_of_birth,
                      commands)
        self.list_camels.append(camel)

    def create_donkey(self, number, color, name, lifetime, mass, sex, lifting_capacity, breed, sound, date_of_birth,
                      commands):
        donkey = Donkey(number, color, name, lifetime, mass, sex, lifting_capacity, breed, sound, date_of_birth,
                        commands)
        self.list_donkeys.append(donkey)

    def find_animal_by_id(self, number, animal_number):
        if animal_number == '1':
            for dog in self.list_dogs:
                if dog.number == number:
                    print("Собака найдена")
                    return dog
        elif animal_number == '2':
            for cat in self.list_cats:
                if cat.number == number:
                    print("Кошка найдена")
                    return cat
        elif animal_number == '3':
            for hamster in self.list_hamsters:
                if hamster.number == number:
                    print("Хомяк найден")
                    return hamster
        elif animal_number == '4':
            for horse in self.list_horses:
                if horse.number == number:
                    print("Лошадь найдена")
                    return horse
        elif animal_number == '5':
            for camel in self.list_camels:
                if camel.number == number:
                    print("Верблюд найден")
                    return camel
        elif animal_number == '6':
            for donkey in self.list_donkeys:
                if donkey.number == number:
                    print("Осел найден")
                    return donkey

    # def add_new_command(self, number, command):
    #     for dog in self.list_dogs:
    #         if dog.number == number:
    #             dog.add_new_command(command)

    def sort_by_date_of_birth(self, animal_number):
        if animal_number == "1":
            sorted_dogs = sorted(self.list_dogs, key=lambda __dog: __dog.date_of_birth)
            print("Собаки")
            headers = None
            dogs = []
            for dog in sorted_dogs:
                headers = dog.info()[0]
                dogs.append(dog.info()[1])
            try:
                print(tabulate(dogs, headers=headers, tablefmt='grid', stralign='center'))
            except TypeError:
                print("Пусто")
        elif animal_number == "2":
            sorted_cats = sorted(self.list_cats, key=lambda __cat: __cat.date_of_birth)
            print("Кошки")
            headers = None
            cats = []
            for cat in sorted_cats:
                headers = cat.info()[0]
                cats.append(cat.info()[1])
            try:
                print(tabulate(cats, headers=headers, tablefmt='grid', stralign='center'))
            except TypeError:
                print("Пусто")
        elif animal_number == "3":
            sorted_hamsters = sorted(self.list_dogs, key=lambda __hamster: __hamster.date_of_birth)
            print("Хомяки")
            headers = None
            hamsters = []
            for hamster in sorted_hamsters:
                headers = hamster.info()[0]
                hamsters.append(hamster.info()[1])
            try:
                print(tabulate(hamsters, headers=headers, tablefmt='grid', stralign='center'))
            except TypeError:
                print("Пусто")
        elif animal_number == "4":
            sorted_horses = sorted(self.list_horses, key=lambda __horse: __horse.date_of_birth)
            print("Лошади")
            headers = None
            horses = []
            for horse in sorted_horses:
                headers = horse.info()[0]
                horses.append(horse.info()[1])
            try:
                print(tabulate(horses, headers=headers, tablefmt='grid', stralign='center'))
            except TypeError:
                print("Пусто")
        elif animal_number == "5":
            sorted_camels = sorted(self.list_camels, key=lambda __camel: __camel.date_of_birth)
            print("Верблюды")
            headers = None
            camels = []
            for camel in sorted_camels:
                headers = camel.info()[0]
                camels.append(camel.info()[1])
            try:
                print(tabulate(camels, headers=headers, tablefmt='grid', stralign='center'))
            except TypeError:
                print("Пусто")
        elif animal_number == "6":
            sorted_donkeys = sorted(self.list_donkeys, key=lambda __donkey: __donkey.date_of_birth)
            print("Ослы")
            headers = None
            donkeys = []
            for donkey in sorted_donkeys:
                headers = donkey.info()[0]
                donkeys.append(donkey.info()[1])
            try:
                print(tabulate(donkeys, headers=headers, tablefmt='grid', stralign='center'))
            except TypeError:
                print("Пусто")

    def save_animals(self, animal_number):
        if animal_number == "1":
            filename = 'dogs.csv'
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                for dog in self.list_dogs:
                    writer.writerow(
                        [dog.number, dog.color, dog.name, dog.lifetime, dog.mass, dog.sex, dog.price, dog.nickname,
                         dog.breed, dog.sound, dog.date_of_birth, dog.commands])
            print("Собаки сохранены в файл")
        elif animal_number == "2":
            filename = 'cats.csv'
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                for cat in self.list_cats:
                    writer.writerow(
                        [cat.number, cat.color, cat.name, cat.lifetime, cat.mass, cat.sex, cat.price, cat.nickname,
                         cat.breed, cat.sound, cat.date_of_birth, cat.commands])
            print("Кошки сохранены в файл")
        elif animal_number == "3":
            filename = 'hamsters.csv'
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                for hamster in self.list_hamsters:
                    writer.writerow(
                        [hamster.number, hamster.color, hamster.name, hamster.lifetime, hamster.mass, hamster.sex,
                         hamster.price, hamster.nickname, hamster.breed, hamster.sound, hamster.date_of_birth,
                         hamster.commands])
            print("Хомяки сохранены в файл")
        elif animal_number == "4":
            filename = 'horses.csv'
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                for horse in self.list_horses:
                    writer.writerow(
                        [horse.number, horse.color, horse.name, horse.lifetime, horse.mass, horse.sex,
                         horse.lifting_capacity, horse.breed, horse.sound, horse.date_of_birth, horse.commands])
            print("Лошади сохранены в файл")
        elif animal_number == "5":
            filename = 'camels.csv'
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                for camel in self.list_camels:
                    writer.writerow(
                        [camel.number, camel.color, camel.name, camel.lifetime, camel.mass, camel.sex,
                         camel.lifting_capacity, camel.breed, camel.sound, camel.date_of_birth, camel.commands])
            print("Верблюды сохранены в файл")
        elif animal_number == "6":
            filename = 'donkeys.csv'
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                for donkey in self.list_donkeys:
                    writer.writerow(
                        [donkey.number, donkey.color, donkey.name, donkey.lifetime, donkey.mass, donkey.sex,
                         donkey.lifting_capacity, donkey.breed, donkey.sound, donkey.date_of_birth, donkey.commands])
            print("Ослы сохранены в файл")

    def load_animals(self):
        try:
            filename = 'dogs.csv'
            with open(filename, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    number = int(row[0])
                    color = row[1]
                    name = row[2]
                    lifetime = int(row[3])
                    mass = int(row[4])
                    sex = row[5]
                    price = int(row[6])
                    nickname = row[7]
                    breed = row[8]
                    sound = row[9]
                    date_of_birth = datetime.strptime(row[10], '%Y-%m-%d %H:%M:%S')
                    commands = row[11]
                    command_list = [item.strip("'") for item in commands[1:-1].split(", ")]
                    self.list_dogs.append(Dog(number, color, name, lifetime, mass, sex, price, nickname,
                                              breed, sound, date_of_birth, command_list))
        except FileNotFoundError:
            print("Файл не найден")
        try:
            filename = 'cats.csv'
            with open(filename, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    number = int(row[0])
                    color = row[1]
                    name = row[2]
                    lifetime = int(row[3])
                    mass = int(row[4])
                    sex = row[5]
                    price = int(row[6])
                    nickname = row[7]
                    breed = row[8]
                    sound = row[9]
                    date_of_birth = datetime.strptime(row[10], '%Y-%m-%d %H:%M:%S')
                    commands = row[11]
                    command_list = [item.strip("'") for item in commands[1:-1].split(", ")]
                    self.list_cats.append(Cat(number, color, name, lifetime, mass, sex, price, nickname,
                                              breed, sound, date_of_birth, command_list))
        except FileNotFoundError:
            print("Файл не найден")
        try:
            filename = 'hamsters.csv'
            with open(filename, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    number = int(row[0])
                    color = row[1]
                    name = row[2]
                    lifetime = int(row[3])
                    mass = int(row[4])
                    sex = row[5]
                    price = int(row[6])
                    nickname = row[7]
                    breed = row[8]
                    sound = row[9]
                    date_of_birth = datetime.strptime(row[10], '%Y-%m-%d %H:%M:%S')
                    commands = row[11]
                    command_list = [item.strip("'") for item in commands[1:-1].split(", ")]
                    self.list_hamsters.append(Hamster(number, color, name, lifetime, mass, sex, price, nickname,
                                                      breed, sound, date_of_birth, command_list))
        except FileNotFoundError:
            print("Файл не найден")
        try:
            filename = 'horses.csv'
            with open(filename, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    number = int(row[0])
                    color = row[1]
                    name = row[2]
                    lifetime = int(row[3])
                    mass = int(row[4])
                    sex = row[5]
                    lifting_capacity = int(row[6])
                    breed = row[7]
                    sound = row[8]
                    date_of_birth = datetime.strptime(row[9], '%Y-%m-%d %H:%M:%S')
                    commands = row[10]
                    command_list = [item.strip("'") for item in commands[1:-1].split(", ")]
                    self.list_horses.append(Horse(number, color, name, lifetime, mass, sex, lifting_capacity,
                                                  breed, sound, date_of_birth, command_list))
        except FileNotFoundError:
            print("Файл не найден")
        try:
            filename = 'camels.csv'
            with open(filename, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    number = int(row[0])
                    color = row[1]
                    name = row[2]
                    lifetime = int(row[3])
                    mass = int(row[4])
                    sex = row[5]
                    lifting_capacity = int(row[6])
                    breed = row[7]
                    sound = row[8]
                    date_of_birth = datetime.strptime(row[9], '%Y-%m-%d %H:%M:%S')
                    commands = row[10]
                    command_list = [item.strip("'") for item in commands[1:-1].split(", ")]
                    self.list_camels.append(Camel(number, color, name, lifetime, mass, sex, lifting_capacity,
                                                  breed, sound, date_of_birth, command_list))
        except FileNotFoundError:
            print("Файл не найден")
        try:
            filename = 'donkeys.csv'
            with open(filename, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    number = int(row[0])
                    color = row[1]
                    name = row[2]
                    lifetime = int(row[3])
                    mass = int(row[4])
                    sex = row[5]
                    lifting_capacity = int(row[6])
                    breed = row[7]
                    sound = row[8]
                    date_of_birth = datetime.strptime(row[9], '%Y-%m-%d %H:%M:%S')
                    commands = row[10]
                    command_list = [item.strip("'") for item in commands[1:-1].split(", ")]
                    self.list_donkeys.append(Donkey(number, color, name, lifetime, mass, sex, lifting_capacity,
                                                    breed, sound, date_of_birth, command_list))
        except FileNotFoundError:
            print("Файл не найден")
