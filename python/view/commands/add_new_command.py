class AddNewCommand:
    def __init__(self, presenter):
        self.name = "Добавить команду"
        self.presenter = presenter

    def get_name(self):
        return self.name

    def execute(self):
        self.presenter.add_new_command()
