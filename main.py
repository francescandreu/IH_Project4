import utils

import os
import pandas as pd

from flask import Flask, request, jsonify
import markdown.extensions.fenced_code
from tools import sql_queries as esquele
#from nltk.sentiment.vader import SentimentIntensityAnalyzer


#sia = SentimentIntensityAnalyzer()
app = Flask(__name__)

# Render the markdwon
@app.route("/")
def readme ():
    readme_file = open("README.md", "r")
    return markdown.markdown(readme_file.read(), extensions = ["fenced_code"])

# GET ENDPOINTS: SQL 
# Genre Related
@app.route("/sql/genres")
def genres_names():
    return jsonify(esquele.get_genres_name())

@app.route("/sql/genres/<genre>")
def se_genre_movies(genre):
    return jsonify(esquele.search_genre_movies(genre))


# Director Related
@app.route("/sql/directors")
def directors_names():
    return jsonify(esquele.get_directors_name())

@app.route("/sql/directors/<director>")
def se_director_movies(director):
    return jsonify(esquele.search_director_movies(director))


# Movie (General) Related
@app.route("/sql/movies")
def movies_everything():
    return jsonify(esquele.get_movies_everything())

@app.route("/sql/movies_titles")
def movies_titles():
    return jsonify(esquele.get_movies_title())


if __name__ == '__main__':
    app.run(port=9000, debug=True)