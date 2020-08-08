from .movie_controller import MoviesController


def initialize_routes(api):
    api.add_resource(MoviesController, '/movies')
