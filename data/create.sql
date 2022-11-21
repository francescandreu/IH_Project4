DROP DATABASE IF EXISTS movies;
CREATE DATABASE movies;
USE movies;

SET GLOBAL local_infile=1;
SET SQL_SAFE_UPDATES = 0;

-- Directors
CREATE TABLE directors(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50)
);

-- Genres
CREATE TABLE genres(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50)
);

-- Movies
CREATE TABLE movies(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    id_director INT NOT NULL,
    id_genre INT NOT NULL,
    title VARCHAR(50),
    year INT,
    rating FLOAT,
    runtime INT,
    censor VARCHAR(10),
    total_gross VARCHAR(20),
	FOREIGN KEY (id_director) REFERENCES directors(id),
    FOREIGN KEY (id_genre) REFERENCES genres(id)
);