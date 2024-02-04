from . import db
from sqlalchemy.sql import func

class Wish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)
    author = db.Column(db.String)