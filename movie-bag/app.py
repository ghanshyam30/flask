# from flask import Flask, jsonify, request
from flask import Flask, request, Response
from database.db import initialize_db
from database.models import Movie

app = Flask(__name__)

# movies = [
#     {
#         "name": "The Shawshank Redemption",
#         "casts": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"],
#         "genres": ["Drama"]
#     },
#     {
#         "name":"The Godfather",
#         "casts": ["Marlon Brando","Al Pacino","James Caan", "Diane Keaton"],
#         "genres": ["Crime", "Drama"]
#     }
# ]

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/movie-bag'
}
initialize_db(app)

@app.route("/movies")
def get_movies():
    movies = Movie.objects().to_json()
    return Response(movies, mimetype="application/json",status=200)

@app.route('/movies/<id>')
def get_movie(id):
    movies = Movie.objects.get(id=id).to_json()
    return Response(movies, mimetype="application/json", status=200)

# # @app.route('/')
# def hello():
#     return jsonify(movies)

# @app.route("/movies", methods=['POST'])
# def add_movie():
#     movie = request.get_json()
#     movies.append(movie)
#     return {'id': len(movies)}, 201

@app.route('/movies', methods=['POST'])
def add_movie():
    body = request.get_json()
    movie = Movie(**body).save()
    id = movie.id
    return {'id':str(id)}, 200

@app.route('/movies/<id>', methods= ['PUT'])
def update_movie(id):
    body = request.get_json()
    Movie.objects.get(id=id).update(**body)
    return '', 200

@app.route('/movies/<id>', methods=['DELETE'])
def delete_movie(id):
    Movie.objects.get(id=id).delete()
    return '',204

# @app.route("/movies/<int:index>", methods=['PUT'])
# def update_movie(index):
#     movie = request.get_json()
#     movies[index] = movie
#     return jsonify(movies[index]), 200

# @app.route('/movies/<int:index>', methods=['DELETE'])
# def delete_movie(index):
#     movies.pop(index)
#     return 'Record removed', 204
app.run()