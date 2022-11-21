USE movies;

INSERT INTO genres(name)
SELECT DISTINCT genre FROM buffer_table
ORDER BY genre ASC;

INSERT INTO directors(name)
SELECT DISTINCT director FROM buffer_table
ORDER BY director ASC;

INSERT INTO movies (id_director, id_genre, title, year, rating, runtime, censor, total_gross)
SELECT d.id, g.id, title, year, rating, runtime, censor, total_gross
FROM buffer_table AS bt
JOIN genres AS g
	ON g.name = bt.genre
JOIN directors AS d
	ON d.name = bt.director
ORDER BY year, title ASC;

UPDATE genres SET name = REPLACE(name, '\r', '')
WHERE name LIKE '%\r';

DROP TABLE IF EXISTS buffer_table;
