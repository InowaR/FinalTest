USE HumanFriends;



INSERT INTO HumanFriends.animals (color, name, lifetime, mass, sex)

VALUES ("черный", "Собака", 15, 5, "мальчик");



INSERT INTO HumanFriends.pets (animal_id, price, nickname)

VALUES ((SELECT id FROM HumanFriends.animals

    WHERE name = "Собака"), 10000, "Барсик");



INSERT INTO HumanFriends.dogs (dog_id, breed, sound, date_of_birth, commands)

VALUES ((SELECT id FROM HumanFriends.pets

    WHERE nickname = "Барсик"), "Немецкая овчарка", "гав", "2023-01-01 10:00:00", "сидеть, лежать, ко мне");

     
-- ---------------------------------------------------------------------------------------------------------


INSERT INTO HumanFriends.animals (color, name, lifetime, mass, sex)

VALUES ("серый", "Кошка", 10, 2, "мальчик");



INSERT INTO HumanFriends.pets (animal_id, price, nickname)

VALUES ((SELECT id FROM HumanFriends.animals

    WHERE name = "Кошка"), 10000, "Мурзик");



INSERT INTO HumanFriends.cats (cat_id, breed, sound, date_of_birth, commands)

VALUES ((SELECT id FROM HumanFriends.pets

    WHERE nickname = "Мурзик"), "Сиамская", "мяу", "2023-01-01 10:00:00", "сидеть, лежать, ко мне, дай лапу");


-- ---------------------------------------------------------------------------------------------------------


INSERT INTO HumanFriends.animals (color, name, lifetime, mass, sex)

VALUES ("черный", "Хомяк", 5, 1, "мальчик");



INSERT INTO HumanFriends.pets (animal_id, price, nickname)

VALUES ((SELECT id FROM HumanFriends.animals

    WHERE name = "Хомяк"), 10000, "Пухлик");



INSERT INTO HumanFriends.hamsters (hamster_id, breed, sound, date_of_birth, commands)

VALUES ((SELECT id FROM HumanFriends.pets

    WHERE nickname = "Пухлик"), "Обыкновенный", "чирк", "2023-01-01 10:00:00", "сидеть, лежать, ко мне")


-- ---------------------------------------------------------------------------------------------------------


INSERT INTO HumanFriends.animals (color, name, lifetime, mass, sex)

VALUES ("Черный", "Лошадь", 5, 1, "мальчик");



INSERT INTO HumanFriends.pack_animals (animal_id, lifting_capacity)

VALUES ((SELECT id FROM HumanFriends.animals

    WHERE name = "Лошадь"), 100);



INSERT INTO HumanFriends.horses (horse_id, breed, sound, date_of_birth, commands)

VALUES ((SELECT id FROM HumanFriends.pack_animals

    WHERE lifting_capacity = 100), "Обыкновенный", "фыр", "2023-01-01 10:00:00", "сидеть, лежать, ко мне")


-- ---------------------------------------------------------------------------------------------------------


INSERT INTO HumanFriends.animals (color, name, lifetime, mass, sex)

VALUES ("желтый", "Верблюд", 10, 100, "мальчик");



INSERT INTO HumanFriends.pack_animals (animal_id, lifting_capacity)

VALUES ((SELECT id FROM HumanFriends.animals

    WHERE name = "Верблюд"), 150);



INSERT INTO HumanFriends.camels (camel_id, breed, sound, date_of_birth, commands)

VALUES ((SELECT id FROM HumanFriends.pack_animals

    WHERE lifting_capacity = 150), "Обыкновенный", "хей-хо", "2023-01-01 10:00:00", "Шагать, рысью, верблюд")


-- ---------------------------------------------------------------------------------------------------------
    

INSERT INTO HumanFriends.animals (color, name, lifetime, mass, sex)

VALUES ("Серый", "Осел", 10, 50, "мальчик");



INSERT INTO HumanFriends.pack_animals (animal_id, lifting_capacity)

VALUES ((SELECT id FROM HumanFriends.animals

    WHERE name = "Осел"), 90);



INSERT INTO HumanFriends.donkeys (donkey_id, breed, sound, date_of_birth, commands)

VALUES ((SELECT id FROM HumanFriends.pack_animals

    WHERE lifting_capacity = 90), "Обыкновенный", "и-а", "2023-01-01 10:00:00", "Шагать, рысью, ехать")