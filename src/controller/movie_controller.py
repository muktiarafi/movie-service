import sys
sys.path.append('..')

from models.movie import Movie
from flask_restful import Resource
from flask import Response, request


class MoviesController(Resource):
    def get(self):
        movies = Movie.objects().to_json()
        return Response(movies, mimetype="application/json", status=200)
