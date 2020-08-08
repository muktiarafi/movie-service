import sys
sys.path.append('..')

from models.movie import Movie
from flask_restful import Resource
from flask import Response, request


class MoviesController(Resource):
    def get(self):
        movies = Movie.objects().to_json()
        return Response(movies, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        movie = Movie(**body)
        movie.version = 1
        movie.save()
        return Response(movie.to_json(), mimetype="application/json", status=201)

class MovieController(Resource):
    def put(self, id):
        body = request.get_json()
        movie = Movie.objects.get(id=id)
        movie.name = body['name']
        movie.genres = body['genres']
        movie.casts = body['casts']
        movie.version += 1
        movie.save()

        return Response(movie.to_json(), mimetype="application/json", status=200)

    def delete(self, id):
        movie = Movie.objects.get(id=id)
        movie.delete()

        return Response(movie.to_json(), mimetype="application/json", status=200)