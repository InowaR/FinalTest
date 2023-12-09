from python.presenter.presenter import Presenter
from python.view.commands.add_new_command import AddNewCommand
from python.view.commands.create_dog import CreateDog
from python.view.commands.save_dogs import SaveDogs
from python.view.commands.show_animals import ShowRegistry
from python.view.commands.show_commands import ShowCommands
from python.view.commands.sort_by_date_of_birth import SortByDateOfBirth


class Menu:
    def __init__(self):
        self.presenter = Presenter()
        self.commands_main_menu = []
        self.commands_main_menu.append(ShowRegistry(self.presenter))
        self.commands_main_menu.append(CreateDog(self.presenter))
        self.commands_main_menu.append(SaveDogs(self.presenter))
        self.commands_main_menu.append(SortByDateOfBirth(self.presenter))
        self.commands_main_menu.append(ShowCommands(self.presenter))
        self.commands_main_menu.append(AddNewCommand(self.presenter))

    def print_main_menu(self):
        print("Меню:")
        for i in self.commands_main_menu:
            print(f'{self.commands_main_menu.index(i)}. {i.get_name()}')

    def execute(self, number):
        self.commands_main_menu[number].execute()