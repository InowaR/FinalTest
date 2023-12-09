from typing import List


class Animal:
    def __init__(self, number, color, name, lifetime, mass, sex):
        self.number = number
        self.color = color
        self.name = name
        self.lifetime = lifetime
        self.mass = mass
        self.sex = sex


class Pet(Animal):
    def __init__(self, number, color, name, lifetime, mass, sex, price, nickname):
        super().__init__(number, color, name, lifetime, mass, sex)
        self.price = price
        self.nickname = nickname


class PackAnimal(Animal):
    def __init__(self, number, color, name, lifetime, mass, sex, lifting_capacity):
        super().__init__(number, color, name, lifetime, mass, sex)
        self.lifting_capacity = lifting_capacity


class Dog(Pet):
    def __init__(self, number, color, name, lifetime, mass, sex, price, nickname, breed, sound, date_of_birth,
                 commands):
        super().__init__(number, color, name, lifetime, mass, sex, price, nickname)
        self.breed = breed
        self.sound = sound
        self.date_of_birth = date_of_birth
        self.commands = commands

    def __str__(self):
        return f'{self.number}, {self.color}, {self.name}, {self.lifetime}, {self.mass}, {self.sex}, ' \
               f'{self.price}, {self.nickname}, {self.breed}, {self.sound}, {self.date_of_birth}, {self.commands}'

    def info(self):
        return ['id', 'color', 'name', 'lifetime', 'mass', 'sex', 'price', 'nickname', 'breed', 'sound',
                'date_of_birth',
                'commands'], (
            self.number, self.color, self.name, self.lifetime, self.mass, self.sex, self.price, self.nickname,
            self.breed, self.sound, self.date_of_birth, self.commands)

    def add_new_command(self, command):
        self.commands.append(command)


class Cat(Pet):
    def __init__(self, number, color, name, lifetime, mass, sex, price, nickname, breed, sound, date_of_birth,
                 commands):
        super().__init__(number, color, name, lifetime, mass, sex, price, nickname)
        self.breed = breed
        self.sound = sound
        self.date_of_birth = date_of_birth
        self.commands: List = commands

    def __str__(self):
        return f'{self.number}, {self.color}, {self.name}, {self.lifetime}, {self.mass}, {self.sex}, ' \
               f'{self.price}, {self.nickname}, {self.breed}, {self.sound}, {self.date_of_birth}, {self.commands}'

    def info(self):
        return ['id', 'color', 'name', 'lifetime', 'mass', 'sex', 'price', 'nickname', 'breed', 'sound',
                'date_of_birth',
                'commands'], (
            self.number, self.color, self.name, self.lifetime, self.mass, self.sex, self.price, self.nickname,
            self.breed, self.sound, self.date_of_birth, self.commands)


class Hamster(Pet):
    def __init__(self, number, color, name, lifetime, mass, sex, price, nickname, breed, sound, date_of_birth,
                 commands):
        super().__init__(number, color, name, lifetime, mass, sex, price, nickname)
        self.breed = breed
        self.sound = sound
        self.date_of_birth = date_of_birth
        self.commands = commands

    def __str__(self):
        return f'{self.number}, {self.color}, {self.name}, {self.lifetime}, {self.mass}, {self.sex}, ' \
               f'{self.price}, {self.nickname}, {self.breed}, {self.sound}, {self.date_of_birth}, {self.commands}'

    def info(self):
        return ['id', 'color', 'name', 'lifetime', 'mass', 'sex', 'price', 'nickname', 'breed', 'sound',
                'date_of_birth',
                'commands'], (
            self.number, self.color, self.name, self.lifetime, self.mass, self.sex, self.price, self.nickname,
            self.breed, self.sound, self.date_of_birth, self.commands)


class Horse(PackAnimal):
    def __init__(self, number, color, name, lifetime, mass, sex, lifting_capacity, breed, sound, date_of_birth,
                 commands):
        super().__init__(number, color, name, lifetime, mass, sex, lifting_capacity)
        self.breed = breed
        self.sound = sound
        self.date_of_birth = date_of_birth
        self.commands = commands

    def __str__(self):
        return f'{self.number}, {self.color}, {self.name}, {self.lifetime}, {self.mass}, {self.sex}, ' \
               f'{self.lifting_capacity}, {self.breed}, {self.sound}, {self.date_of_birth}, {self.commands}'

    def info(self):
        return ['id', 'color', 'name', 'lifetime', 'mass', 'sex', 'lifting_capacity', 'breed', 'sound', 'date_of_birth',
                'commands'], (
            self.number, self.color, self.name, self.lifetime, self.mass, self.sex, self.lifting_capacity,
            self.breed, self.sound, self.date_of_birth, self.commands)


class Camel(PackAnimal):
    def __init__(self, number, color, name, lifetime, mass, sex, lifting_capacity, breed, sound, date_of_birth,
                 commands):
        super().__init__(number, color, name, lifetime, mass, sex, lifting_capacity)
        self.breed = breed
        self.sound = sound
        self.date_of_birth = date_of_birth
        self.commands = commands

    def __str__(self):
        return f'{self.number}, {self.color}, {self.name}, {self.lifetime}, {self.mass}, {self.sex}, ' \
               f'{self.lifting_capacity}, {self.breed}, {self.sound}, {self.date_of_birth}, {self.commands}'

    def info(self):
        return ['id', 'color', 'name', 'lifetime', 'mass', 'sex', 'lifting_capacity', 'breed', 'sound', 'date_of_birth',
                'commands'], (
            self.number, self.color, self.name, self.lifetime, self.mass, self.sex, self.lifting_capacity,
            self.breed, self.sound, self.date_of_birth, self.commands)


class Donkey(PackAnimal):
    def __init__(self, number, color, name, lifetime, mass, sex, lifting_capacity, breed, sound, date_of_birth,
                 commands):
        super().__init__(number, color, name, lifetime, mass, sex, lifting_capacity)
        self.breed = breed
        self.sound = sound
        self.date_of_birth = date_of_birth
        self.commands = commands

    def __str__(self):
        return f'{self.number}, {self.color}, {self.name}, {self.lifetime}, {self.mass}, {self.sex}, ' \
               f'{self.lifting_capacity}, {self.breed}, {self.sound}, {self.date_of_birth}, {self.commands}'

    def info(self):
        return ['id', 'color', 'name', 'lifetime', 'mass', 'sex', 'lifting_capacity', 'breed', 'sound', 'date_of_birth',
                'commands'], (
            self.number, self.color, self.name, self.lifetime, self.mass, self.sex, self.lifting_capacity,
            self.breed, self.sound, self.date_of_birth, self.commands)
