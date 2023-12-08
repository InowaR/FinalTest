from datetime import datetime

from python.model.registry import Registry


reg = Registry()
reg.create_dog(1, "коричневый", "собака", 10, 3, "мужской", 10000, "Барли", "Овчарка", "гав", datetime(2023, 1, 1), ["Cидеть", "Голос", "Ко мне"])
reg.show_registry()
