USE movies;

-- Creating buffer table to then move data to each table
DROP TABLE IF EXISTS buffer_table;
CREATE TABLE buffer_table(
	id INT,
	title VARCHAR(30),	
    year INT,
    director VARCHAR(30),
    actors VARCHAR(100),
    rating FLOAT,
    runtime INT,
    censor VARCHAR(10),
    total_gross VARCHAR(20),
    genre VARCHAR(20), 
    sec_genre VARCHAR(100)
);

-- Loading data from csv to buffer_table
LOAD DATA LOCAL INFILE 'C:/Users/franc/OneDrive/Escritorio/PROJECTS/IH_Project4/data/movies_clean.csv'
INTO TABLE buffer_table
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(id, title, year, director, actors, rating, runtime, censor, total_gross, sec_genre, genre);