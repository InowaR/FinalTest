import csv
from datetime import datetime
from typing import List
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
        try:
            print("Собаки")
            headers = None
            dogs = []
            for dog in self.list_dogs:
                headers = dog.info()[0]
                dogs.append(dog.info()[1])
            print(tabulate(dogs, headers=headers, tablefmt='grid', stralign='center'))
            print("Кошки")
            for cat in self.list_cats:
                print(tabulate(cat.info()[1], headers=cat.info()[0], tablefmt='grid', stralign='center'))
            print("Хомяки")
            for hamster in self.list_hamsters:
                print(tabulate(hamster.info()[1], headers=hamster.info()[0], tablefmt='grid', stralign='center'))
            print("Лошади")
            for horse in self.list_horses:
                print(tabulate(horse.info()[1], headers=horse.info()[0], tablefmt='grid', stralign='center'))
            print("Верблюды")
            for camel in self.list_camels:
                print(tabulate(camel.info()[1], headers=camel.info()[0], tablefmt='grid', stralign='center'))
            print("Ослы")
            for donkey in self.list_donkeys:
                print(tabulate(donkey.info()[1], headers=donkey.info()[0], tablefmt='grid', stralign='center'))
        except IndexError:
            print("Ошибка файла")

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
                return dog.commands

    def add_new_command(self, number, command):
        for dog in self.list_dogs:
            if dog.number == number:
                dog.add_new_command(command)

    def show_animals_sorted_by_date_of_birth(self):
        print(self.list_dogs[0].date_of_birth)

        # s = self.list_dogs.sort(key = date_of_birth)
        # for dog in self.list_dogs:
        #     print(tabulate(dog.info()[1], headers=dog.info()[0], tablefmt='grid', stralign='center'))

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
                try:
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
                        self.list_dogs.append(Dog(number, color, name, lifetime, mass, sex, price, nickname,
                                                  breed, sound, date_of_birth, commands))
                        # print("Собаки загружены из файла")
                except IndexError:
                    print("Файл пустой")
        except FileNotFoundError:
            print("Файл не найден")
