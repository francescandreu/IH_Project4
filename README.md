# Ironhack Project 4
# Building a Database with related API

## Project description
The goal of this project is to build a Database and seed it with a dataset obtained previously, and then develop a API from which to query the build DB.

## Table of contents
1. Libraries required
2. Modules description
3. List of directories


## 1. Libraries required
For the correct execution of this project there will be multiple libraries needed, mainly Flask to build the app and markdown to print the readme as the webpage. Others will also be needed such as Panda, Alchemy and Dotenv.


## 2. Modules description
The project has various dedicated modules to run the program properly. Firs of all there's the utils.py which will work around the Dataset that we obtained and prepare the data for an easier loading into the Database.

The Database is build in a MySQL environment and has three tables (movies, directors and genres).

Then using the sql_connection and sql_queries we setup the connection from the API to the Database so the clients can perform queries into the DB.

The main module brings everything together and the clien.ipnyb allows us to execute input queries with easy usage.


## 3. List of directories

Genres:
>- List of all genres in the Database: /sql/get/genres
>- Search for movies from a certain genre: /sql/search/genres/'genre'
>- Insert new movie genre: Call function -> post_new_genre(genre_name)

Directors:
>- List of all directors in the Database: /sql/get/directors
>- Search for movies from a certain director: /sql/search/directors/'director'
>- Insert new director: Call function -> post_new_director(director_name)

Movies:
>- List all movies and all their information of them: sql/get/movies
>- List all movie titles: sql/get/movies_titles
>- Search movie by title: sql/search/movies/'movie'
>- Insert new movie: Call function -> post_new_movie(movie_dict)