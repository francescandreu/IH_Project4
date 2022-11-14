from config.sql_connection import engine
import pandas as pd

# -------------- SQL: GET QUERIES --------------
# --- Genre Related ---
def get_genres_name():
    query = """SELECT name FROM genres ORDER BY name;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient='records')

# --- Director Related ---
def get_directors_name():
    query = """SELECT name FROM directors ORDER BY name;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient='records')

# --- Movies (General) Related ---
def get_movies_title():
    query = """SELECT title FROM movies ORDER BY title;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient='records')

def get_movies_everything():
    query = """SELECT * FROM movies  ORDER BY title;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient='records')



# -------------- SQL: SEARCH QUERIES --------------
# --- Genre Related ---
def search_genre_movies(name):
    query = f"""SELECT m.title 
                    FROM movies AS m
                    JOIN genres AS g
                        ON g.id = m.id_genre
                    WHERE g.name='{name}';"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient='records')

# --- Director Related ---
def search_director_movies(name):
    query = f"""SELECT m.title 
                    FROM movies AS m
                    LEFT JOIN directors AS d
                        ON d.id = m.id_director
                    WHERE d.name='{name}';"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient='records')

# --- Movies (General) Related ---
def search_movie(movie):
    query = f"""SELECT * 
                    FROM movies AS m
                    WHERE m.title='{movie}';"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient='records')



# -------------- SQL: INSERT QUERIES --------------
# --- Genre Related ---
def insert_genre(name):
    query = f"""INSERT INTO genres(name)
                VALUES("{name}");"""
    engine.execute(query)
    return f"Genre correctly introduced!"

# --- Director Related ---
def insert_director(name):
    query = f"""INSERT INTO directors(name)
                VALUES("{name}");"""
    engine.execute(query)
    return f"Director correctly introduced!"

# --- Movies (General) Related ---
def insert_movie(title, year, rating, runtime, censor, total_gross, director, genre):
    query = f"""INSERT INTO movies(title, year, rating, runtime, censor, total_gross, id_director, id_genre)
                VALUES("{title}", {year}, {rating}, {runtime}, "{censor}", "{total_gross}",
                        (SELECT id FROM directors WHERE name="{director}"),
                        (SELECT id FROM genres WHERE name="{genre}"));"""
    engine.execute(query)
    return f"Movie correctly introduced!"