CREATE TABLE merged_animals (
  id INT NOT NULL AUTO_INCREMENT,
  color TEXT,
  name TEXT,
  lifetime INT,
  mass INT,
  sex TEXT,
  price INT,
  nickname TEXT,
  breed TEXT,
  sound TEXT,
  date_of_birth DATETIME,
  commands TEXT,
  lifting_capacity INT,
  PRIMARY KEY (id),
  FOREIGN KEY (color) REFERENCES HumanFriends.animals (color),
  FOREIGN KEY (name) REFERENCES HumanFriends.animals (name),
  FOREIGN KEY (lifetime) REFERENCES HumanFriends.animals (lifetime),
  FOREIGN KEY (mass) REFERENCES HumanFriends.animals (mass),
  FOREIGN KEY (sex) REFERENCES HumanFriends.animals (sex),
  FOREIGN KEY (price) REFERENCES HumanFriends.pets (price),
  FOREIGN KEY (nickname) REFERENCES HumanFriends.pets (nickname),
  FOREIGN KEY (breed) REFERENCES HumanFriends.horses (breed),
  FOREIGN KEY (sound) REFERENCES HumanFriends.horses (sound),
  FOREIGN KEY (date_of_birth) REFERENCES HumanFriends.horses (date_of_birth),
  FOREIGN KEY (commands) REFERENCES HumanFriends.horses (commands),
  FOREIGN KEY (lifting_capacity) REFERENCES HumanFriends.horses (lifting_capacity)
);
