from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/movies/<movie_name>", methods=["GET"])
def get_movie(movie_name):
    movie_data={
        "movie_name": movie_name,
        "rating": "8.5"
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