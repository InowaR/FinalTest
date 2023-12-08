CREATE DATABASE HumanFriends;

USE HumanFriends;

CREATE TABLE HumanFriends.animals (
	id INT AUTO_INCREMENT,
	color TEXT,
	name TEXT,
	lifetime INT,
	mass INT,
	sex TEXT,
	PRIMARY KEY (id)
);

CREATE TABLE HumanFriends.pets (
	id INT AUTO_INCREMENT,
	animal_id INT,
	price INT,
	nickname TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY (animal_id) REFERENCES animals (id)	
);

CREATE TABLE HumanFriends.pack_animals (
	id INT AUTO_INCREMENT,
	animal_id INT,	
	lifting_capacity INT,
	PRIMARY KEY (id),
	FOREIGN KEY (animal_id) REFERENCES animals (id)		
);

CREATE TABLE HumanFriends.dogs (
	dog_id INT,
	breed TEXT,
	sound TEXT,
	date_of_birth DATETIME,
	commands TEXT,
	FOREIGN KEY (dog_id) REFERENCES pets (id)		
);

CREATE TABLE HumanFriends.cats (
	cat_id INT,
	breed TEXT,
	sound TEXT,
	date_of_birth DATETIME,
	commands TEXT,
	FOREIGN KEY (cat_id) REFERENCES pets (id)		
);

CREATE TABLE HumanFriends.hamsters (
	hamster_id INT,
	breed TEXT,
	sound TEXT,
	date_of_birth DATETIME,
	commands TEXT,
	FOREIGN KEY (hamster_id) REFERENCES pets (id)		
);

CREATE TABLE HumanFriends.horses (
	horse_id INT,
	breed TEXT,
	sound TEXT,
	date_of_birth DATETIME,
	commands TEXT,
	FOREIGN KEY (horse_id) REFERENCES pack_animals (id)		
);

CREATE TABLE HumanFriends.camels (
	camel_id INT,
	breed TEXT,
	sound TEXT,
	date_of_birth DATETIME,
	commands TEXT,
	FOREIGN KEY (camel_id) REFERENCES pack_animals (id)		
);

CREATE TABLE HumanFriends.donkeys (
	donkey_id INT,
	breed TEXT,
	sound TEXT,
	date_of_birth DATETIME,
	commands TEXT,
	FOREIGN KEY (donkey_id) REFERENCES pack_animals (id)		
);
