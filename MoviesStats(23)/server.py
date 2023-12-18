from flask import Flask, request, jsonify
import requests
from youtubesearchpython import VideosSearch
from bs4 import BeautifulSoup
import MoviesDB

def get_trailer(movie_name):
    search = VideosSearch(f"{movie_name} trailer"  , limit = 1)
    result = search.result()
    trailer = result['result'][0]['link']
    return trailer

def get_rating_from_rotten_tomatoes(movie_name):
    html = requests.get(f"https://www.rottentomatoes.com/m/{movie_name}")
    soup = BeautifulSoup(html.text, 'html.parser')
    result = soup.find(attrs={"data-qa": "audience-score"})
    return result.text
    
mdb = MoviesDB.MovieDb()
app = Flask(__name__)

@app.route("/movies/<movie_name>", methods=["GET"])
def get_movie(movie_name):
    movie_data={
        "trailer": get_trailer(movie_name),
        "movie_name": movie_name,
        "rating": mdb.find_rating_by_title(movie_name),
    }
    return jsonify(movie_data),200

@app.route("/actors/<actor_name>", methods=["GET"])
def get_actor(actor_name):
    actor_data={
        "actor_name": actor_name,
        "rating": "8.5"
    }
    return jsonify(actor_data),200

if __name__ == '__main__':
    app.run(debug=True)