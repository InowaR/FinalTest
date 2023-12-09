from python.model.service import Service


class Presenter:
    def __init__(self):
        self.service = Service()

    def create_dog(self):
        self.service.create_dog()

    def show_registry(self):
        self.service.show_registry()

    def show_animals_sorted_by_date_of_birth(self):
        self.service.show_animals_sorted_by_date_of_birth()

    def save_dogs(self):
        self.service.save_dogs()