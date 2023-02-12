from .db import db


class User(db.Document):
    username = db.StringField(
        required=True,
        unique=True,
        min_length=3,
        max_length=32
    )
    password = db.StringField(
        required=True,
        min_length=8,
        max_length=16
    )
    age = db.IntField(
        min_value=0,
        max_value=128
    )
