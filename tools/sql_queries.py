from config.sql_connection import engine
import pandas as pd

# Genre Related Queries
def get_genres_name():
    query = """SELECT name FROM genres;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient='records')

def search_genre_movies(name):
    query = f"""SELECT m.title 
                    FROM movies AS m
                    JOIN genres AS g
                        ON g.id = m.id_genre
                    WHERE g.name='{name}';"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient='records')


# Director Related Queries
def get_directors_name():
    query = """SELECT name FROM directors;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient='records')

def search_director_movies(name):
    query = f"""SELECT m.title 
                    FROM movies AS m
                    LEFT JOIN directors AS d
                        ON d.id = m.id_director
                    WHERE d.name='{name}';"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient='records')


# Movies (General) Related Queries
def get_movies_title():
    query = """SELECT title FROM movies;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient='records')

def get_movies_everything():
    query = """SELECT * FROM movies;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient='records')
