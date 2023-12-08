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
        print("Собаки")
        for dog in self.list_dogs:
            print(tabulate(dog.info()[1], headers=dog.info()[0], tablefmt='grid', stralign='center'))
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
