CREATE TABLE HumanFriends.young_animals (
  id INT NOT NULL AUTO_INCREMENT,
  animal_id INT,
  age INT,
  PRIMARY KEY (id),
  FOREIGN KEY (animal_id) REFERENCES HumanFriends.animals (id)
);

INSERT INTO HumanFriends.young_animals (animal_id)
SELECT a.id
FROM HumanFriends.animals a
INNER JOIN HumanFriends.pets p
ON a.id = p.animal_id
WHERE a.lifetime > 3 AND a.lifetime < 10;

UPDATE HumanFriends.young_animals y
SET y.age = TIMESTAMPDIFF(MONTH, a.date_of_birth, CURRENT_TIMESTAMP()) / 12 + 1
FROM HumanFriends.animals a
WHERE y.animal_id = a.id;
