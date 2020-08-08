import os
from flask import Flask, Response
from flask_restful import Api
from models.db import initialize_db
from controller.routes import initialize_routes

app = Flask(__name__)
api = Api(app)

app.config['MONGODB_SETTINGS'] = {
    'host': os.environ.get('MONGO_URI')
}
initialize_db(app)
initialize_routes(api)

app.run()
