from python.model.service import Service


class Presenter:
    def __init__(self):
        self.service = Service()

    def animal_menu(self):
        print(f"Всего животных в питомнике: {self.service.count}")
        print("1. Собака")
        print("2. Кошка")
        print("3. Хомяк")
        print("4. Лошадь")
        print("5. Верблюд")
        print("6. Осел")
        print("7. Назад")
        try:
            animal_number = int(input("Выберите животное:"))
            return animal_number
        except ValueError:
            print("Ошибка. Введите число.")

    def create_animal(self):
        animal_number = self.animal_menu()
        if animal_number == "7":
            return
        self.service.create_animal(animal_number)

    def show_registry(self):
        animal_number = self.animal_menu()
        if animal_number == "7":
            return
        self.service.show_registry(animal_number)

    def sort_by_date_of_birth(self):
        animal_number = self.animal_menu()
        if animal_number == "7":
            return
        self.service.sort_by_date_of_birth(animal_number)

    def save_animals(self):
        animal_number = self.animal_menu()
        if animal_number == "7":
            return
        self.service.save_animals(animal_number)

    def show_commands(self):
        animal_number = self.animal_menu()
        if animal_number == "7":
            return
        self.service.show_commands(animal_number)

    def add_new_command(self):
        animal_number = self.animal_menu()
        if animal_number == "7":
            return
        self.service.add_new_command(animal_number)
