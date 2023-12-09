class ShowCommands:
    def __init__(self, presenter):
        self.name = "Показать команды"
        self.presenter = presenter

    def get_name(self):
        return self.name

    def execute(self):
        self.presenter.show_commands()
