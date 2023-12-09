from python.model.service import Service


class Presenter:
    def __init__(self):
        self.service = Service()

    def create_dog(self):
        self.service.create_dog()

    def show_registry(self):
        self.service.show_registry()

    def sort_by_date_of_birth(self):
        self.service.sort_by_date_of_birth()

    def save_dogs(self):
        self.service.save_dogs()

    def show_commands(self):
        self.service.show_commands()

    def add_new_command(self):
        self.service.add_new_command()