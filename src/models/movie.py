import mongoengine_goodjson as gj
from .db import db


class Movie(gj.Document):
    name = db.StringField(required=True, unique=True)
    casts = db.ListField(db.StringField(), required=True)
    genres = db.ListField(db.StringField(), required=True)
    version = db.IntField(min_value=0, default=1)
