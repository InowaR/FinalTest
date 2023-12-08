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
        print(self.list_dogs)

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
