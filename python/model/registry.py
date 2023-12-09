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

    def show_registry(self):
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
        print("Лошади")
        headers = None
        horses = []
        for horse in self.list_horses:
            headers = horse.info()[0]
            hamsters.append(horse.info()[1])
        try:
            print(tabulate(horses, headers=headers, tablefmt='grid', stralign='center'))
        except TypeError:
            print("Пусто")
        # ----------------------------------------------------------------------------
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

    def find_dog_by_id(self, number):
        for dog in self.list_dogs:
            if dog.number == number:
                print("Собака найдена")
                return dog

    def add_new_command(self, number, command):
        for dog in self.list_dogs:
            if dog.number == number:
                dog.add_new_command(command)

    def sort_by_date_of_birth(self):
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

    def save_dogs(self):
        filename = 'dogs.csv'
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for dog in self.list_dogs:
                writer.writerow(
                    [dog.number, dog.color, dog.name, dog.lifetime, dog.mass, dog.sex, dog.price, dog.nickname,
                     dog.breed, dog.sound, dog.date_of_birth, dog.commands])
        print("Собаки сохранены в файл")

    def load_dogs(self):
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
