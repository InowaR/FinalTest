class CreateAnimal:
    def __init__(self, presenter):
        self.name = "Добавить животное"
        self.presenter = presenter

    def get_name(self):
        return self.name

    def execute(self):
        self.presenter.create_animal()
