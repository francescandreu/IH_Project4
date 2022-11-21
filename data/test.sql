USE movies;
	
SELECT * FROM genres;

SELECT * FROM directors;

SELECT * FROM movies;

SELECT m.title 
	FROM movies AS m
	JOIN genres AS g
		ON g.id = m.id_genre
	WHERE g.name='Animation';
    
