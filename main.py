import pandas as pd

from flask import Flask, request, jsonify
import markdown.extensions.fenced_code
from tools import sql_queries as esquele
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()
app = Flask(__name__)

# Render the markdwon
@app.route("/")
def readme ():
    readme_file = open("README.md", "r")
    return markdown.markdown(readme_file.read(), extensions = ["fenced_code"])


# -------------- SQL: GET ENDPOINTS --------------
# --- Genre Related ---
@app.route("/sql/get/genres")
def genres_names():
    return jsonify(esquele.get_genres_name())

# --- Director Related ---
@app.route("/sql/get/directors")
def directors_names():
    return jsonify(esquele.get_directors_name())

# --- Movie (General) Related ---
@app.route("/sql/get/movies")
def movies_everything():
    return jsonify(esquele.get_movies_everything())

@app.route("/sql/get/movies_titles")
def movies_titles():
    return jsonify(esquele.get_movies_title())



# -------------- SQL: SEARCH ENDPOINTS --------------
# --- Genre Related ---
@app.route("/sql/search/genres/<genre>", )
def se_genre_movies(genre):
    return jsonify(esquele.search_genre_movies(genre))

# --- Director Related ---
@app.route("/sql/search/directors/<director>", )
def se_director_movies(director):
    return jsonify(esquele.search_director_movies(director))

# --- Movie (General) Related ---
@app.route("/sql/search/movies/<movie>", )
def se_movie(movie):
    return jsonify(esquele.search_movie(movie))



# -------------- SQL: INSERT QUERIES --------------
# --- Genre Related ---
@app.route("/sql/insert/genre", methods=["POST"])
def in_genre():
    my_params = request.args
    genre_name = my_params["name"]
    esquele.insert_genre(genre_name)
    return f"Query succesfully inserted."


# --- Director Related ---
@app.route("/sql/insert/director", methods=["POST"])
def in_director():
    my_params = request.args
    director_name = my_params["name"]
    esquele.insert_genre(director_name)
    return f"Query succesfully inserted."


# --- Movies (General) Related ---
@app.route("/sql/insert/movie", methods=["POST"])
def in_movie():
    my_params = request.args
    title = my_params["title"]
    year = my_params["year"]
    rating = my_params["rating"]
    runtime = my_params["runtime"]
    censor = my_params["censor"]
    total_gross = my_params["total_gross"]
    director = my_params["director"]
    genre = my_params["genre"]
    esquele.insert_movie(title, year, rating, runtime, censor, total_gross, director, genre)
    return f"Query succesfully inserted."


# --------------------- Main ----------------------
if __name__ == '__main__':
    app.run(port=8000, debug=True)