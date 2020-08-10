import sys
sys.path.append('..')

from models.movie import Movie, movie_schema
from flask_restful import Resource
from flask import Response, request
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError
from errors.field_validation_error import FieldValidationError
from errors.not_found_error import NotFoundError
from errors.duplicate_key_error import DuplicateKeyError

class MoviesController(Resource):
    def get(self):
        movies = Movie.objects().to_json()
        return Response(movies, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        validate = movie_schema.validate(body)

        if validate:
            raise FieldValidationError(validate)

        try:    
            movie = Movie(**body)
            movie.version = 1
            movie.save()
        except NotUniqueError as err:
            raise DuplicateKeyError({ 'name': 'duplicate key error'})

        return Response(movie.to_json(), mimetype="application/json", status=201)

class MovieController(Resource):
    def put(self, id):
        body = request.get_json()
        validate = movie_schema.validate(body)

        if validate:
            raise FieldValidationError(validate)

        try:
            movie = Movie.objects.get(id=id)
        except DoesNotExist:
            raise NotFoundError()

        movie.name = body['name']
        movie.genres = body['genres']
        movie.casts = body['casts']
        movie.version += 1
        movie.save()

        return Response(movie.to_json(), mimetype="application/json", status=200)

    def delete(self, id):
        try:
            movie = Movie.objects.get(id=id)
            movie.delete()
        except DoesNotExist:
            raise NotFoundError()

        return Response(movie.to_json(), mimetype="application/json", status=200)