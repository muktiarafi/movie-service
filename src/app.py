import os
from flask import Flask, Response, jsonify
from flask_restful import Api
from models.db import initialize_db
from controller.routes import initialize_routes
from errors.field_validation_error import FieldValidatonError
from errors.not_found_error import NotFoundError

app = Flask(__name__)
api = Api(app)

app.config['MONGODB_SETTINGS'] = {
    'host': os.environ.get('MONGO_URI')
}
initialize_db(app)
initialize_routes(api)

@app.errorhandler(FieldValidatonError)
def fieldValidationError(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@app.errorhandler(NotFoundError)
def notFoundError(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

app.run(debug=True)
