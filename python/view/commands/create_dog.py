class CreateDog:
    def __init__(self, presenter):
        self.name = "Добавить собаку"
        self.presenter = presenter

    def get_name(self):
        return self.name

    def execute(self):
        self.presenter.create_dog()
