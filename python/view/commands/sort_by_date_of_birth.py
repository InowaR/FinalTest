class SortByDateOfBirth:
    def __init__(self, presenter):
        self.name = "Отсортировать животных по дате рождения"
        self.presenter = presenter

    def get_name(self):
        return self.name

    def execute(self):
        self.presenter.sort_by_date_of_birth()
