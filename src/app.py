import os
from flask import Flask, Response
from models.db import initialize_db
from models.movie import Movie

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': os.environ.get('MONGO_URI')
}
initialize_db(app)


@app.route('/')
def index():
    return 'yeet'


@app.route('/movies')
def get_movies():
    movies = Movie.objects().to_json()
    print(movies)
    return Response(movies, mimetype="application/json", status=200)


app.run()
