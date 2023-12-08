DELETE FROM HumanFriends.camels;

INSERT INTO HumanFriends.horses
(horse_id, breed, sound, date_of_birth, commands)
SELECT
    camel_id,
    breed,
    sound,
    date_of_birth,
    commands
FROM HumanFriends.camels;

DROP TABLE HumanFriends.camels;

RENAME TABLE HumanFriends.donkeys TO HumanFriends.pack_animals;

ALTER TABLE HumanFriends.horses
ADD COLUMN lifting_capacity INT;

UPDATE HumanFriends.horses
SET lifting_capacity = 500;
