import sys
import mongoengine_goodjson as gj
from marshmallow import fields, Schema
from marshmallow.validate import Length
from .db import db

class Movie(gj.Document):
    name = db.StringField(required=True, unique=True)
    casts = db.ListField(db.StringField(), required=True)
    genres = db.ListField(db.StringField(), required=True)
    version = db.IntField(min_value=0, default=1)

class MovieSchema(Schema):
    name = fields.Str(required=True)
    casts = fields.List(fields.Str(), required=True)
    genres = fields.List(fields.Str(), required=True)

    class Meta:
        fields = ('name', 'casts', 'genres')

movie_schema = MovieSchema()
